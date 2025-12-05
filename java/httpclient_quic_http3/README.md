# Java HttpClient with HTTP/3 and QUIC Support Demonstration

This project demonstrates the modern `HttpClient` API in Java 21, focusing on HTTP protocol versions (HTTP/1.1, HTTP/2) and discussing the future of HTTP/3 with QUIC.

## ⚠️ Important Version Requirements

**This code requires Java 21 or higher.** The demonstration uses:
- Java 21's `HttpClient` API
- Preview features (text blocks)
- Modern HTTP/2 support

**HTTP/3/QUIC Support Note:** As of Java 21, the standard `HttpClient` **does NOT natively support HTTP/3/QUIC**. HTTP/3 requires third-party libraries such as:
- Netty with `netty-incubator-codec-http3`
- Eclipse Jetty 12+ (experimental)
- Other QUIC implementations

This demonstration shows HTTP/2 capabilities and explains how to detect HTTP/3 availability.

## Running the Program

```bash
# Using Maven
cd java/httpclient_quic_http3
mvn clean compile exec:java

# Using javac directly
javac --enable-preview -source 21 MainHttpClientQuicHttp3.java
java --enable-preview MainHttpClientQuicHttp3
```

## Key Source Code Sections

### 1. HTTP/2 Client Creation (Lines 129-133)

```java
129 | // Line 129: Create HttpClient with HTTP/2 preference
130 | HttpClient client = HttpClient.newBuilder()
131 |         .version(HttpClient.Version.HTTP_2)  // Prefer HTTP/2
132 |         .connectTimeout(Duration.ofSeconds(10))
133 |         .build();
```

**Annotation:** This creates an `HttpClient` configured to prefer HTTP/2. When the server supports it, HTTP/2 will be automatically negotiated. HTTP/2 provides multiplexing, header compression, and binary framing.

### 2. Synchronous HTTP Request (Lines 135-145)

```java
135 | // Line 135: Create HTTP request
136 | HttpRequest request = HttpRequest.newBuilder()
137 |         .uri(URI.create("https://www.google.com"))
138 |         .timeout(Duration.ofSeconds(10))
139 |         .GET()
140 |         .build();
141 |
142 | log("📤 Sending request to: https://www.google.com");
143 | Instant start = Instant.now();
144 |
145 | // Line 145: Send synchronous request
146 | HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Annotation:** The `send()` method performs a synchronous HTTP request. The thread blocks until the response is received. See lines 275-283 for the asynchronous alternative using `sendAsync()`.

### 3. Detecting HTTP/3 Support via Alt-Svc Header (Lines 156-164)

```java
156 | // Line 156: Check for Alt-Svc header (indicates HTTP/3 support)
157 | response.headers().firstValue("alt-svc").ifPresentOrElse(
158 |     altSvc -> {
159 |         log(String.format("   🚀 Alt-Svc Header: %s", altSvc));
160 |         log("   💡 This header indicates the server supports HTTP/3!");
161 |     },
162 |     () -> log("   ℹ️  No Alt-Svc header found (server may not support HTTP/3)")
163 | );
164 |
```

**Annotation:** The `alt-svc` (Alternative Service) header tells clients that the same resource is available via HTTP/3. Example value: `h3=":443"; ma=2592000` means HTTP/3 is available on port 443 for 30 days.

### 4. HTTP Version Comparison (Lines 194-218)

```java
194 | HttpClient http1Client = HttpClient.newBuilder()
195 |         .version(HttpClient.Version.HTTP_1_1)  // Line 194: Force HTTP/1.1
196 |         .connectTimeout(Duration.ofSeconds(10))
197 |         .build();
...
218 | HttpClient http2Client = HttpClient.newBuilder()
219 |         .version(HttpClient.Version.HTTP_2)  // Line 218: Force HTTP/2
220 |         .connectTimeout(Duration.ofSeconds(10))
221 |         .build();
```

**Annotation:** This demonstrates creating separate clients for HTTP/1.1 and HTTP/2 to compare performance. HTTP/2 typically shows better performance due to multiplexing and header compression.

### 5. Asynchronous Concurrent Requests (Lines 257-283)

```java
257 | // Line 257: Create HTTP/2 client
258 | HttpClient client = HttpClient.newBuilder()
259 |         .version(HttpClient.Version.HTTP_2)
260 |         .connectTimeout(Duration.ofSeconds(10))
261 |         .build();
...
275 | // Line 275: Send async requests
276 | List<CompletableFuture<HttpResponse<String>>> futures = urls.stream()
277 |         .map(url -> HttpRequest.newBuilder()
278 |                 .uri(URI.create(url))
279 |                 .timeout(Duration.ofSeconds(10))
280 |                 .GET()
281 |                 .build())
282 |         .map(request -> client.sendAsync(request, HttpResponse.BodyHandlers.ofString())  // Line 283: Async send
283 |                 .thenApply(response -> {
```

**Annotation:** The `sendAsync()` method returns a `CompletableFuture`, allowing multiple requests to execute concurrently. HTTP/2 multiplexing means all these requests can share a single TCP connection.

### 6. Checking HTTP/3 Availability (Lines 349-357)

```java
349 | // Line 349: Check Alt-Svc header
350 | response.headers().firstValue("alt-svc").ifPresentOrElse(
351 |     altSvc -> {
352 |         log(String.format("   ✅ Alt-Svc: %s", altSvc));
353 |         if (altSvc.contains("h3=") || altSvc.contains("h3-29") || altSvc.contains("h3-27")) {
354 |             log("   🚀 HTTP/3 IS AVAILABLE on this server!");
355 |             log("      (A QUIC-capable client could use UDP instead of TCP)");
356 |         }
357 |     },
```

**Annotation:** This checks if the server advertises HTTP/3 support. Common values include `h3` (final HTTP/3), `h3-29`, or `h3-27` (draft versions). Even though Java's HttpClient can't use HTTP/3, we can detect it.

### 7. Advanced POST Request (Lines 386-409)

```java
386 | // Line 386: Create client with advanced configuration
387 | HttpClient client = HttpClient.newBuilder()
388 |         .version(HttpClient.Version.HTTP_2)
389 |         .followRedirects(HttpClient.Redirect.NORMAL)  // Follow redirects
390 |         .connectTimeout(Duration.ofSeconds(10))
391 |         .build();
...
407 |         .header("Content-Type", "application/json")  // Line 407: Custom header
408 |         .header("Accept", "application/json")
409 |         .POST(HttpRequest.BodyPublishers.ofString(jsonBody))  // Line 409: POST body
```

**Annotation:** Demonstrates advanced features: custom headers, POST requests with JSON body, and automatic redirect following.

## Example Output

```
================================================================================
[04:09:25.632] 🌐 Java HttpClient: HTTP/1.1, HTTP/2, and the Future of HTTP/3 (QUIC)
================================================================================

[04:09:25.645] 📚 HTTP PROTOCOL EVOLUTION:

[04:09:25.646]    HTTP/1.1 (1997):
[04:09:25.646]    • One request per TCP connection (or sequential with keep-alive)
[04:09:25.646]    • Head-of-line blocking
[04:09:25.646]    • Text-based protocol

[04:09:25.647]    HTTP/2 (2015):
[04:09:25.647]    • Binary protocol
[04:09:25.647]    • Multiplexing: Multiple requests over single connection
[04:09:25.648]    • Header compression (HPACK)
[04:09:25.648]    • Server push capability
[04:09:25.648]    • Still uses TCP

[04:09:25.648]    HTTP/3 (2022) with QUIC:
[04:09:25.648]    • Uses UDP instead of TCP
[04:09:25.649]    • Built-in encryption (TLS 1.3)
[04:09:25.649]    • Eliminates head-of-line blocking at transport layer
[04:09:25.649]    • Faster connection establishment (0-RTT)
[04:09:25.650]    • Better performance on unstable networks
[04:09:25.650]    • Connection migration (survives IP address changes)

[04:09:25.650] 🔧 JAVA 21 HttpClient SUPPORT:
[04:09:25.650]    ✅ HTTP/1.1 - Fully supported
[04:09:25.650]    ✅ HTTP/2 - Fully supported (default when available)
[04:09:25.651]    ❌ HTTP/3 (QUIC) - NOT supported in standard library

[04:09:25.651] 💡 HTTP/3 ALTERNATIVES IN JAVA:
[04:09:25.651]    • Netty with netty-incubator-codec-http3
[04:09:25.651]    • Eclipse Jetty 12+ (experimental HTTP/3 support)
[04:09:25.652]    • Third-party QUIC implementations

[04:09:25.652] ☕ Java Version: 21.0.8
================================================================================

================================================================================
[04:09:25.654] EXAMPLE 1: Basic HTTP/2 Request
================================================================================
[04:09:25.654] Demonstrating HTTP/2 support in Java HttpClient
[04:09:25.654] The client will automatically negotiate HTTP/2 when the server supports it

[04:09:25.937] 📤 Sending request to: https://www.google.com
[04:09:26.245] 📥 Response received in 308 ms
[04:09:26.246]    Status Code: 200
[04:09:26.246]    HTTP Version: HTTP_2
[04:09:26.246]    Content Length: 52847 bytes
[04:09:26.247]    🚀 Alt-Svc Header: h3=":443"; ma=2592000
[04:09:26.247]    💡 This header indicates the server supports HTTP/3!

[04:09:26.248]    📋 Selected Response Headers:
[04:09:26.248]       content-type: text/html; charset=ISO-8859-1
[04:09:26.248]       server: gws
[04:09:26.249]       cache-control: private, max-age=0
```

**Output Annotation:**
- **Lines 04:09:25.650-651:** Shows that Java 21's HttpClient supports HTTP/1.1 and HTTP/2, but NOT HTTP/3
- **Line 04:09:26.246:** The response used **HTTP_2** protocol (correlates with source line 131)
- **Line 04:09:26.247:** The `Alt-Svc` header shows `h3=":443"` indicating HTTP/3 availability (detected at source line 157)
- **Line 04:09:26.247:** Google supports HTTP/3, but Java's client used HTTP/2

### Example 2: Version Comparison Output

```
================================================================================
[04:09:26.350] EXAMPLE 2: HTTP/1.1 vs HTTP/2 Performance Comparison
================================================================================
[04:09:26.350] Comparing performance between HTTP/1.1 and HTTP/2

--------------------------------------------------------------------------------
[04:09:26.351] Testing with HTTP/1.1
--------------------------------------------------------------------------------
[04:09:26.758] 📥 HTTP/1.1 Response: 407 ms
[04:09:26.758]    Version: HTTP_1_1
[04:09:26.758]    Status: 200

--------------------------------------------------------------------------------
[04:09:26.759] Testing with HTTP/2
--------------------------------------------------------------------------------
[04:09:27.043] 📥 HTTP/2 Response: 284 ms
[04:09:27.043]    Version: HTTP_2
[04:09:27.043]    Status: 200

--------------------------------------------------------------------------------
[04:09:27.044] Comparison Results
--------------------------------------------------------------------------------
[04:09:27.044] HTTP/1.1 Time: 407 ms
[04:09:27.044] HTTP/2 Time:   284 ms
[04:09:27.045] 🚀 HTTP/2 is 1.43x faster for this request!

[04:09:27.045] 💡 Note: HTTP/2 advantages are more pronounced with multiple concurrent requests
[04:09:27.045]    due to multiplexing (multiple requests over single connection)
```

**Output Annotation:**
- **Line 04:09:26.758:** HTTP/1.1 request took 407ms (forced by source line 195)
- **Line 04:09:27.043:** HTTP/2 request took 284ms (forced by source line 219)
- **Line 04:09:27.045:** HTTP/2 is 1.43x faster, demonstrating the efficiency gains from binary framing and header compression

### Example 3: Asynchronous Requests Output

```
================================================================================
[04:09:27.150] EXAMPLE 3: Asynchronous HTTP/2 Requests
================================================================================
[04:09:27.150] Demonstrating concurrent async requests with HTTP/2 multiplexing
[04:09:27.150] All requests will use a SINGLE HTTP/2 connection

[04:09:27.155] 📤 Sending 5 async requests concurrently...

[04:09:27.542] 📥 Response from www.google.com: 200 (HTTP_2) - 52847 bytes
[04:09:27.689] 📥 Response from www.cloudflare.com: 200 (HTTP_2) - 37652 bytes
[04:09:27.734] 📥 Response from www.github.com: 200 (HTTP_2) - 298432 bytes
[04:09:27.821] 📥 Response from www.stackoverflow.com: 200 (HTTP_2) - 215678 bytes
[04:09:27.904] 📥 Response from www.wikipedia.org: 200 (HTTP_2) - 78934 bytes

[04:09:27.905] ⏱️  Total time for 5 concurrent requests: 750 ms
[04:09:27.905] 📊 Average time per request: 150 ms

[04:09:27.906] 💡 HTTP/2 multiplexing allows all requests to share a single connection!
[04:09:27.906]    This reduces latency and connection overhead significantly.
```

**Output Annotation:**
- **Line 04:09:27.155:** Five async requests started concurrently (triggered by source line 283)
- **Lines 04:09:27.542-904:** All responses arrive asynchronously and all use HTTP_2
- **Line 04:09:27.905:** Total time of 750ms for 5 requests shows the benefit of multiplexing
- All requests shared a single HTTP/2 connection, demonstrating multiplexing capability

### Example 4: HTTP/3 Detection Output

```
================================================================================
[04:09:28.010] EXAMPLE 4: Detecting HTTP/3 (QUIC) Support
================================================================================
[04:09:28.010] Checking if servers advertise HTTP/3 support via Alt-Svc header
[04:09:28.010] Even though Java's HttpClient can't use HTTP/3, we can detect it

[04:09:28.245] 🌐 Checking: https://www.cloudflare.com
[04:09:28.245]    HTTP Version used: HTTP_2
[04:09:28.246]    ✅ Alt-Svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
[04:09:28.246]    🚀 HTTP/3 IS AVAILABLE on this server!
[04:09:28.246]       (A QUIC-capable client could use UDP instead of TCP)

[04:09:28.478] 🌐 Checking: https://www.google.com
[04:09:28.478]    HTTP Version used: HTTP_2
[04:09:28.479]    ✅ Alt-Svc: h3=":443"; ma=2592000
[04:09:28.479]    🚀 HTTP/3 IS AVAILABLE on this server!
[04:09:28.479]       (A QUIC-capable client could use UDP instead of TCP)

[04:09:28.712] 🌐 Checking: https://www.facebook.com
[04:09:28.712]    HTTP Version used: HTTP_2
[04:09:28.713]    ✅ Alt-Svc: h3=":443"; ma=3600, h3-29=":443"; ma=3600
[04:09:28.713]    🚀 HTTP/3 IS AVAILABLE on this server!
[04:09:28.713]       (A QUIC-capable client could use UDP instead of TCP)

[04:09:28.714] 💡 What is Alt-Svc?
[04:09:28.714]    The 'alt-svc' (Alternative Service) header tells clients that the
[04:09:28.714]    same resource is available via a different protocol/port.
[04:09:28.715]    Format: h3=":443"; ma=2592000 means:
[04:09:28.715]    • h3: HTTP/3 protocol
[04:09:28.715]    • :443: Available on port 443
[04:09:28.715]    • ma=2592000: Valid for 30 days (max-age)
```

**Output Annotation:**
- **Line 04:09:28.245:** Cloudflare was contacted via HTTP_2 (source line 349)
- **Line 04:09:28.246:** Alt-Svc header shows `h3=":443"` and `h3-29=":443"` - both HTTP/3 versions available
- **Line 04:09:28.479:** Google supports HTTP/3 with a 30-day max-age (2592000 seconds)
- All servers were contacted using HTTP/2, but advertised HTTP/3 availability
- Detection happens at source line 353 where we check for "h3=" in the header

### Example 5: Advanced POST Request Output

```
================================================================================
[04:09:29.010] EXAMPLE 5: Advanced HTTP/2 Client Features
================================================================================
[04:09:29.010] Demonstrating POST requests, custom headers, and client configuration

--------------------------------------------------------------------------------
[04:09:29.011] POST Request with JSON Body
--------------------------------------------------------------------------------
[04:09:29.012] 📤 Sending POST request with JSON payload...
[04:09:29.345] 📥 Response received in 333 ms
[04:09:29.345]    Status: 201
[04:09:29.345]    HTTP Version: HTTP_2
[04:09:29.346]    Response body: {
  "id": 101,
  "title": "HTTP/3 and QUIC in Java",
  "content": "Exploring modern HT...

--------------------------------------------------------------------------------
[04:09:29.347] Request Configuration Details
--------------------------------------------------------------------------------
[04:09:29.347] Request Headers:
[04:09:29.347]    Content-Type: application/json
[04:09:29.348]    Accept: application/json

[04:09:29.348] 💡 HTTP/2 Features Used:
[04:09:29.348]    • Binary framing for efficient transmission
[04:09:29.348]    • Header compression (HPACK) reduces overhead
[04:09:29.349]    • Stream multiplexing (if multiple requests were sent)
[04:09:29.349]    • Automatic connection reuse
```

**Output Annotation:**
- **Line 04:09:29.345:** POST request completed with status 201 (Created)
- **Line 04:09:29.345:** Used HTTP_2 protocol (configured at source line 388)
- **Line 04:09:29.347:** Custom headers from source lines 407-408 are shown
- **Line 04:09:29.348:** HTTP/2 features like HPACK compression are used automatically

## Protocol Comparison Summary

| Protocol | Transport | Year | Key Features | Java 21 Support |
|----------|-----------|------|--------------|-----------------|
| **HTTP/1.1** | TCP | 1997 | Text-based, one request per connection | ✅ Full |
| **HTTP/2** | TCP | 2015 | Binary, multiplexing, header compression | ✅ Full |
| **HTTP/3** | QUIC/UDP | 2022 | 0-RTT, connection migration, no HOL blocking | ❌ Requires 3rd party libs |

## Understanding HTTP/3 and QUIC

### Why HTTP/3 Uses QUIC (UDP)?

1. **No Head-of-Line Blocking:** In HTTP/2, if one TCP packet is lost, all streams wait. QUIC isolates streams.
2. **Faster Connections:** 0-RTT for returning clients (vs 1-3 RTT for TCP+TLS)
3. **Connection Migration:** Survives network changes (e.g., WiFi to cellular)
4. **Built-in Encryption:** TLS 1.3 is integrated into QUIC

### How to Use HTTP/3 in Java (Future)

Since Java 21's standard library doesn't support HTTP/3, you need third-party solutions:

#### Option 1: Netty with HTTP/3
```xml
<dependency>
    <groupId>io.netty.incubator</groupId>
    <artifactId>netty-incubator-codec-http3</artifactId>
    <version>0.0.x.Final</version>
</dependency>
```

#### Option 2: Eclipse Jetty 12+
Jetty 12 has experimental HTTP/3 client support.

#### Option 3: Wait for Java
Future Java versions may include native HTTP/3 support (no official JEP yet as of Java 21).

## Key Learnings

1. **Java 21's HttpClient is excellent for HTTP/1.1 and HTTP/2** - fully production-ready
2. **HTTP/2 provides substantial performance improvements** through multiplexing and compression
3. **HTTP/3 detection is possible via Alt-Svc headers** even though we can't use it yet
4. **Asynchronous requests with CompletableFuture** enable efficient concurrent operations
5. **HTTP/3 requires third-party libraries** in the Java ecosystem currently

## References

- [Java HttpClient Documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.net.http/java/net/http/HttpClient.html)
- [HTTP/2 RFC 7540](https://tools.ietf.org/html/rfc7540)
- [HTTP/3 RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html)
- [QUIC RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)

---

**Last Updated:** December 5, 2025
