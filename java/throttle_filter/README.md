# Throttle Servlet Filter for Spring Boot

This example demonstrates how to implement a **rate limiting servlet filter** in Spring Boot that prevents consumers from sending too many requests in a short burst. The implementation uses the **Token Bucket Algorithm** to enforce rate limits per client IP address.

## What is Rate Limiting?

Rate limiting (throttling) is a technique to control the rate at which clients can make requests to your API. It helps:
- Prevent abuse and DoS attacks
- Ensure fair resource allocation among clients
- Protect backend services from overload
- Maintain quality of service

## Algorithm: Token Bucket

The **Token Bucket Algorithm** works as follows:
1. Each client gets a bucket that starts with a maximum number of tokens (capacity)
2. Each request consumes one token from the bucket
3. Tokens are refilled at a constant rate over time
4. If no tokens are available, the request is rejected with HTTP 429

This allows for **burst traffic** (up to capacity) while enforcing a **sustained rate limit**.

## Configuration

```java
// Line 107-108: Configuration constants
private static final long CAPACITY = 10;           // Max burst capacity
private static final double REFILL_RATE = 5.0;    // 5 tokens per second
```

This configuration means:
- Clients can burst up to **10 requests** instantly
- Sustained rate is limited to **5 requests per second**
- After burst, clients must wait for tokens to refill

## Key Components

### 1. Token Bucket Class (Lines 31-76)

The `TokenBucket` class implements the core rate limiting logic:

```java
// Line 31-55: Token Bucket implementation
class TokenBucket {
    private final long capacity;           // Maximum number of tokens
    private final double refillRate;       // Tokens added per second
    private double tokens;                 // Current available tokens
    private long lastRefillTimestamp;      // Last time tokens were refilled

    public TokenBucket(long capacity, double refillRate) {
        this.capacity = capacity;
        this.refillRate = refillRate;
        this.tokens = capacity;  // Start with full capacity
        this.lastRefillTimestamp = System.currentTimeMillis();
    }

    // Line 60-68: Token consumption
    public synchronized boolean tryConsume() {
        refill();
        if (tokens >= 1) {
            tokens--;
            return true;
        }
        return false;
    }

    // Line 73-80: Token refill based on elapsed time
    private void refill() {
        long now = System.currentTimeMillis();
        double elapsedSeconds = (now - lastRefillTimestamp) / 1000.0;
        double tokensToAdd = elapsedSeconds * refillRate;
        tokens = Math.min(capacity, tokens + tokensToAdd);
        lastRefillTimestamp = now;
    }
}
```

**Key Points:**
- **Line 60**: `tryConsume()` is synchronized to prevent race conditions
- **Line 61**: Always refill before checking token availability
- **Line 79**: Tokens are capped at capacity (no accumulation beyond max)
- **Line 78**: New tokens = elapsed time × refill rate

### 2. Throttle Filter (Lines 92-185)

The servlet filter intercepts all HTTP requests:

```java
// Line 92-100: Filter configuration
@Component
class ThrottleFilter implements Filter {
    private static final long CAPACITY = 10;
    private static final double REFILL_RATE = 5.0;

    // Line 103: Track token buckets per client IP
    private final Map<String, TokenBucket> buckets = new ConcurrentHashMap<>();

    // Line 106-107: Statistics tracking
    private final AtomicLong totalRequests = new AtomicLong(0);
    private final AtomicLong throttledRequests = new AtomicLong(0);
```

**Line 103**: Uses `ConcurrentHashMap` for thread-safe IP tracking

```java
// Line 119-141: Core filtering logic
@Override
public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
        throws IOException, ServletException {

    String clientIp = getClientIp(httpRequest);
    long requestNum = totalRequests.incrementAndGet();

    // Line 127-129: Get or create token bucket for this client
    TokenBucket bucket = buckets.computeIfAbsent(clientIp,
        k -> new TokenBucket(CAPACITY, REFILL_RATE));

    // Line 131-141: Try to consume a token
    if (bucket.tryConsume()) {
        // ALLOWED: Token available
        System.out.printf("[Request #%d] %s %s from %s - ALLOWED (%.1f tokens remaining)%n",
            requestNum, httpRequest.getMethod(), httpRequest.getRequestURI(),
            clientIp, bucket.getAvailableTokens());

        chain.doFilter(request, response);  // Continue to the endpoint
    } else {
        // THROTTLED: No tokens available
        long throttled = throttledRequests.incrementAndGet();
        System.out.printf("[Request #%d] %s %s from %s - THROTTLED (0 tokens remaining)%n",
            requestNum, httpRequest.getMethod(), httpRequest.getRequestURI(), clientIp);

        // Line 149-153: Return HTTP 429
        httpResponse.setStatus(HttpStatus.TOO_MANY_REQUESTS.value());
        httpResponse.setContentType("application/json");
        httpResponse.getWriter().write(String.format(
            "{\"error\":\"Too Many Requests\",\"message\":\"Rate limit exceeded. Try again later.\",\"limit\":%d,\"rate\":%.1f}",
            CAPACITY, REFILL_RATE));
    }
}
```

**Key Points:**
- **Line 129**: `computeIfAbsent()` creates bucket only if not exists
- **Line 139**: Successful requests continue through the filter chain
- **Line 149**: Throttled requests get HTTP 429 status

```java
// Line 167-176: Extract client IP (handles proxies)
private String getClientIp(HttpServletRequest request) {
    String xForwardedFor = request.getHeader("X-Forwarded-For");
    if (xForwardedFor != null && !xForwardedFor.isEmpty()) {
        return xForwardedFor.split(",")[0].trim();
    }
    return request.getRemoteAddr();
}
```

**Line 167-176**: Handles X-Forwarded-For header for requests behind proxies/load balancers

### 3. Sample REST Controller (Lines 187-221)

Provides test endpoints to demonstrate the throttle filter:

```java
// Line 187-221: Test endpoints
@RestController
@RequestMapping("/api")
class ApiController {
    @GetMapping("/hello")
    public Map<String, Object> hello() { ... }

    @GetMapping("/data")
    public Map<String, Object> getData() { ... }

    @PostMapping("/submit")
    public Map<String, Object> submit(@RequestBody Map<String, Object> payload) { ... }

    @GetMapping("/status")
    public Map<String, String> status() { ... }
}
```

## Running the Application

### Build and Run

```bash
# Build the application
mvn clean package

# Run the application
mvn spring-boot:run

# Or run the JAR directly
java -jar target/throttle-servlet-filter-1.0-SNAPSHOT.jar
```

The application starts on port 8080 by default.

### Testing the Throttle Filter

Use `curl` to test the rate limiting:

```bash
# Send 15 rapid requests to trigger throttling
for i in {1..15}; do
  curl -w "\nStatus: %{http_code}\n" http://localhost:8080/api/hello
  sleep 0.1
done
```

## Expected Output

### Application Startup

```
=== Starting Throttle Servlet Filter Demo ===

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.0)

ThrottleFilter initialized:
  - Rate limit: 5.0 requests/second
  - Burst capacity: 10 requests
  - Algorithm: Token Bucket

Started MainThrottleServletFilter in 1.234 seconds (process running for 1.567)
```

**Annotations:**
- Application starts with embedded Tomcat on port 8080
- Filter initialization displays configuration (capacity: 10, rate: 5 req/s)

### Request Processing (Rapid Burst)

```
[Request #1] GET /api/hello from 127.0.0.1 - ALLOWED (9.0 tokens remaining)
[Request #2] GET /api/hello from 127.0.0.1 - ALLOWED (8.0 tokens remaining)
[Request #3] GET /api/hello from 127.0.0.1 - ALLOWED (7.0 tokens remaining)
[Request #4] GET /api/hello from 127.0.0.1 - ALLOWED (6.0 tokens remaining)
[Request #5] GET /api/hello from 127.0.0.1 - ALLOWED (5.0 tokens remaining)
[Request #6] GET /api/hello from 127.0.0.1 - ALLOWED (4.0 tokens remaining)
[Request #7] GET /api/hello from 127.0.0.1 - ALLOWED (3.0 tokens remaining)
[Request #8] GET /api/hello from 127.0.0.1 - ALLOWED (2.0 tokens remaining)
[Request #9] GET /api/hello from 127.0.0.1 - ALLOWED (1.0 tokens remaining)
[Request #10] GET /api/hello from 127.0.0.1 - ALLOWED (0.0 tokens remaining)
[Request #11] GET /api/hello from 127.0.0.1 - THROTTLED (0 tokens remaining)
[Request #12] GET /api/hello from 127.0.0.1 - THROTTLED (0 tokens remaining)
[Request #13] GET /api/hello from 127.0.0.1 - THROTTLED (0 tokens remaining)
[Request #14] GET /api/hello from 127.0.0.1 - THROTTLED (0 tokens remaining)
[Request #15] GET /api/hello from 127.0.0.1 - THROTTLED (0 tokens remaining)
```

**Annotations:**
- **Requests 1-10**: Allowed (consuming the initial 10-token burst capacity)
  - Line 133-141 in code: `tryConsume()` returns true, request proceeds
  - Each request depletes one token from the bucket
- **Requests 11-15**: Throttled (bucket empty, no tokens available)
  - Line 143-153 in code: `tryConsume()` returns false, HTTP 429 returned
  - Tokens need time to refill (5 tokens/second = 200ms per token)

### Client Response (Successful)

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Hello! Request processed successfully.",
  "requestNumber": 1,
  "timestamp": 1699876543210
}

Status: 200
```

**Annotations:**
- Successful requests (with available tokens) return 200 OK
- Response includes request counter and timestamp

### Client Response (Throttled)

```
HTTP/1.1 429 Too Many Requests
Content-Type: application/json

{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Try again later.",
  "limit": 10,
  "rate": 5.0
}

Status: 429
```

**Annotations:**
- Throttled requests return **HTTP 429 Too Many Requests** (Line 149)
- Response body includes rate limit configuration for client awareness
- Standard HTTP status for rate limiting (RFC 6585)

### Waiting for Token Refill

After waiting 2 seconds (2 × 5 = 10 tokens refilled):

```
[Request #16] GET /api/hello from 127.0.0.1 - ALLOWED (9.0 tokens remaining)
```

**Annotations:**
- **2 seconds elapsed** = 10 tokens refilled (5 tokens/second)
- Bucket replenishes to full capacity (capped at 10)
- Line 73-80 in code: `refill()` method adds tokens based on elapsed time
- Client can now make requests again

### Sustained Load Test

With 0.3-second delay between requests (slower than refill rate):

```
[Request #17] GET /api/data from 127.0.0.1 - ALLOWED (9.5 tokens remaining)
[Request #18] GET /api/data from 127.0.0.1 - ALLOWED (9.0 tokens remaining)
[Request #19] GET /api/data from 127.0.0.1 - ALLOWED (8.5 tokens remaining)
[Request #20] GET /api/data from 127.0.0.1 - ALLOWED (8.0 tokens remaining)
```

**Annotations:**
- 0.3 seconds between requests = 1.5 tokens refilled per interval
- Each request consumes 1 token
- Net gain: 0.5 tokens per request (1.5 refilled - 1 consumed)
- Sustained rate of ~3.3 req/s is well below the 5 req/s limit
- All requests succeed without throttling

### Multiple Clients

Different IP addresses maintain separate token buckets:

```
[Request #21] GET /api/hello from 192.168.1.100 - ALLOWED (9.0 tokens remaining)
[Request #22] GET /api/hello from 192.168.1.101 - ALLOWED (9.0 tokens remaining)
[Request #23] GET /api/hello from 192.168.1.100 - ALLOWED (8.0 tokens remaining)
[Request #24] GET /api/hello from 192.168.1.101 - ALLOWED (8.0 tokens remaining)
```

**Annotations:**
- Line 103-129: Each IP gets its own token bucket via `ConcurrentHashMap`
- Client 192.168.1.100 and 192.168.1.101 have independent token counts
- Rate limits are enforced **per client**, not globally
- Fair resource allocation across multiple consumers

## How It Works: Flow Diagram

```
Client Request
      ↓
[ThrottleFilter.doFilter()]  ← Line 119
      ↓
Get/Create TokenBucket for client IP  ← Line 127-129
      ↓
[TokenBucket.tryConsume()]  ← Line 131
      ↓
[TokenBucket.refill()]  ← Line 61 → Line 73
      ↓
Calculate tokens to add based on elapsed time  ← Line 77-79
      ↓
Check if tokens >= 1  ← Line 63
      ↓
   ┌──────────┴──────────┐
   ↓ YES                 ↓ NO
Consume 1 token     Return false
   ↓                      ↓
Return true          HTTP 429
   ↓                 Throttled Response
Allow request           ← Line 149-153
   ↓
chain.doFilter()  ← Line 139
   ↓
Endpoint Handler  ← Lines 187-221
   ↓
HTTP 200
Success Response
```

## Configuration Options

You can customize the rate limiting behavior by modifying these constants:

```java
// In ThrottleFilter class (Lines 107-108)
private static final long CAPACITY = 10;           // Burst capacity
private static final double REFILL_RATE = 5.0;    // Tokens per second
```

**Example configurations:**

| Scenario | Capacity | Rate | Behavior |
|----------|----------|------|----------|
| Strict | 5 | 2.0 | Max 5 burst, 2 req/s sustained |
| Moderate | 10 | 5.0 | Max 10 burst, 5 req/s sustained |
| Lenient | 20 | 10.0 | Max 20 burst, 10 req/s sustained |
| API Gateway | 100 | 50.0 | Max 100 burst, 50 req/s sustained |

## Requirements

- **Java 17** or higher
- **Spring Boot 3.2.0** (uses Jakarta Servlet API)
- **Maven** for dependency management

Note: This example requires **Spring Boot 3.x**, which uses the Jakarta EE namespace (`jakarta.servlet.*`) instead of the older Java EE namespace (`javax.servlet.*`). If using Spring Boot 2.x, change the import from `jakarta.servlet` to `javax.servlet`.

## Thread Safety

The implementation is thread-safe:
- **Line 103**: `ConcurrentHashMap` for concurrent IP tracking
- **Line 106-107**: `AtomicLong` for statistics counters
- **Line 60**: `synchronized` method in `TokenBucket.tryConsume()`
- All operations are atomic or properly synchronized

## Production Considerations

For production use, consider:

1. **Distributed Systems**: Use Redis or similar for shared rate limit state across multiple servers
2. **Configuration**: Externalize rate limit settings to application.properties
3. **Headers**: Add rate limit headers (X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset)
4. **Cleanup**: Implement bucket eviction for inactive IPs to prevent memory leaks
5. **Metrics**: Integrate with monitoring systems (Prometheus, Micrometer)
6. **Different Rates**: Support different rate limits per endpoint or user tier
7. **Whitelist**: Allow certain IPs to bypass rate limiting

## Additional Resources

- [Token Bucket Algorithm](https://en.wikipedia.org/wiki/Token_bucket)
- [RFC 6585 - HTTP Status Code 429](https://tools.ietf.org/html/rfc6585#section-4)
- [Spring Boot Servlet Filter Documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/web.html#web.servlet.embedded-container.servlets-filters-listeners)
