import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Component;
import org.springframework.http.HttpStatus;
import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Spring Boot Example - Throttle Servlet Filter
 *
 * Demonstrates a rate limiting filter that prevents consumers from sending
 * too many requests in a short burst. Uses a token bucket algorithm to
 * enforce rate limits per client IP address.
 *
 * Key Features:
 * - Token bucket algorithm for smooth rate limiting
 * - Per-IP address tracking
 * - Configurable rate (requests per second) and burst capacity
 * - Returns HTTP 429 (Too Many Requests) when limit exceeded
 * - Automatic token refill over time
 */
@SpringBootApplication
public class MainThrottleServletFilter {

    public static void main(String[] args) {
        System.out.println("=== Starting Throttle Servlet Filter Demo ===\n");
        SpringApplication.run(MainThrottleServletFilter.class, args);
    }
}

/**
 * Token Bucket - Implements the token bucket algorithm for rate limiting.
 *
 * How it works:
 * - Each bucket starts with a maximum number of tokens (capacity)
 * - Each request consumes one token
 * - Tokens are refilled at a fixed rate over time
 * - If no tokens are available, the request is rejected
 */
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

    /**
     * Attempts to consume one token. Returns true if successful, false otherwise.
     */
    public synchronized boolean tryConsume() {
        refill();

        if (tokens >= 1) {
            tokens--;
            return true;
        }
        return false;
    }

    /**
     * Refills tokens based on elapsed time since last refill.
     */
    private void refill() {
        long now = System.currentTimeMillis();
        double elapsedSeconds = (now - lastRefillTimestamp) / 1000.0;
        double tokensToAdd = elapsedSeconds * refillRate;

        tokens = Math.min(capacity, tokens + tokensToAdd);
        lastRefillTimestamp = now;
    }

    public synchronized double getAvailableTokens() {
        refill();
        return tokens;
    }
}

/**
 * Throttle Filter - A servlet filter that enforces rate limits.
 *
 * Configuration:
 * - Rate: 5 requests per second
 * - Burst capacity: 10 requests
 *
 * This allows clients to burst up to 10 requests, but sustained load
 * cannot exceed 5 requests per second.
 */
@Component
class ThrottleFilter implements Filter {

    // Configuration
    private static final long CAPACITY = 10;           // Max burst capacity
    private static final double REFILL_RATE = 5.0;    // 5 tokens per second

    // Track token buckets per client IP
    private final Map<String, TokenBucket> buckets = new ConcurrentHashMap<>();

    // Statistics
    private final AtomicLong totalRequests = new AtomicLong(0);
    private final AtomicLong throttledRequests = new AtomicLong(0);

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        System.out.println("ThrottleFilter initialized:");
        System.out.println("  - Rate limit: " + REFILL_RATE + " requests/second");
        System.out.println("  - Burst capacity: " + CAPACITY + " requests");
        System.out.println("  - Algorithm: Token Bucket\n");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        HttpServletRequest httpRequest = (HttpServletRequest) request;
        HttpServletResponse httpResponse = (HttpServletResponse) response;

        String clientIp = getClientIp(httpRequest);
        long requestNum = totalRequests.incrementAndGet();

        // Get or create token bucket for this client
        TokenBucket bucket = buckets.computeIfAbsent(clientIp,
            k -> new TokenBucket(CAPACITY, REFILL_RATE));

        // Try to consume a token
        if (bucket.tryConsume()) {
            // Token available - allow the request
            System.out.printf("[Request #%d] %s %s from %s - ALLOWED (%.1f tokens remaining)%n",
                requestNum,
                httpRequest.getMethod(),
                httpRequest.getRequestURI(),
                clientIp,
                bucket.getAvailableTokens());

            chain.doFilter(request, response);
        } else {
            // No tokens available - throttle the request
            long throttled = throttledRequests.incrementAndGet();
            System.out.printf("[Request #%d] %s %s from %s - THROTTLED (0 tokens remaining)%n",
                requestNum,
                httpRequest.getMethod(),
                httpRequest.getRequestURI(),
                clientIp);

            httpResponse.setStatus(HttpStatus.TOO_MANY_REQUESTS.value());
            httpResponse.setContentType("application/json");
            httpResponse.getWriter().write(String.format(
                "{\"error\":\"Too Many Requests\",\"message\":\"Rate limit exceeded. Try again later.\",\"limit\":%d,\"rate\":%.1f}",
                CAPACITY, REFILL_RATE));
        }
    }

    @Override
    public void destroy() {
        System.out.println("\nThrottleFilter statistics:");
        System.out.println("  - Total requests: " + totalRequests.get());
        System.out.println("  - Throttled requests: " + throttledRequests.get());
        System.out.println("  - Success rate: " +
            String.format("%.1f%%", 100.0 * (totalRequests.get() - throttledRequests.get()) / totalRequests.get()));
    }

    /**
     * Extracts the client IP address from the request.
     * Checks X-Forwarded-For header first (for proxied requests).
     */
    private String getClientIp(HttpServletRequest request) {
        String xForwardedFor = request.getHeader("X-Forwarded-For");
        if (xForwardedFor != null && !xForwardedFor.isEmpty()) {
            return xForwardedFor.split(",")[0].trim();
        }
        return request.getRemoteAddr();
    }
}

/**
 * Sample REST Controller to test the throttle filter.
 */
@RestController
@RequestMapping("/api")
class ApiController {

    private final AtomicLong requestCounter = new AtomicLong(0);

    @GetMapping("/hello")
    public Map<String, Object> hello() {
        long count = requestCounter.incrementAndGet();
        return Map.of(
            "message", "Hello! Request processed successfully.",
            "requestNumber", count,
            "timestamp", System.currentTimeMillis()
        );
    }

    @GetMapping("/data")
    public Map<String, Object> getData() {
        return Map.of(
            "data", "Some important data",
            "status", "success",
            "timestamp", System.currentTimeMillis()
        );
    }

    @PostMapping("/submit")
    public Map<String, Object> submit(@RequestBody(required = false) Map<String, Object> payload) {
        return Map.of(
            "status", "received",
            "payload", payload != null ? payload : Map.of(),
            "timestamp", System.currentTimeMillis()
        );
    }

    @GetMapping("/status")
    public Map<String, String> status() {
        return Map.of(
            "status", "UP",
            "service", "Throttled API"
        );
    }
}
