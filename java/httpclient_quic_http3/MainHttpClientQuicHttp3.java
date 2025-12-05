import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.time.Instant;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.stream.Collectors;

/**
 * Java HttpClient with HTTP/3 and QUIC Support Demonstration (Java 21+)
 *
 * This example demonstrates the modern HttpClient API in Java 21 and discusses
 * HTTP/3 (QUIC) protocol support and future directions.
 *
 * Key Topics Covered:
 * 1. HttpClient configuration and HTTP protocol versions (HTTP/1.1, HTTP/2)
 * 2. HTTP/3 and QUIC protocol overview
 * 3. Current state of HTTP/3 support in Java
 * 4. Synchronous and asynchronous HTTP requests
 * 5. HTTP/2 features: multiplexing, server push capabilities
 * 6. Detecting HTTP/3 support via Alt-Svc headers
 * 7. Performance characteristics
 *
 * IMPORTANT NOTE ABOUT HTTP/3 IN JAVA 21:
 * As of Java 21, the standard HttpClient does NOT natively support HTTP/3/QUIC.
 * - HTTP/1.1 and HTTP/2 are fully supported
 * - HTTP/3 requires third-party libraries (e.g., Netty with QUIC support)
 * - This demo shows HTTP/2 capabilities and explains HTTP/3 concepts
 */
public class MainHttpClientQuicHttp3 {

    private static final String ANSI_RESET = "\u001B[0m";
    private static final String ANSI_BLUE = "\u001B[34m";
    private static final String ANSI_GREEN = "\u001B[32m";
    private static final String ANSI_YELLOW = "\u001B[33m";
    private static final String ANSI_CYAN = "\u001B[36m";
    private static final String ANSI_RED = "\u001B[31m";

    private static void log(String message) {
        System.out.printf("[%s] %s%n", Instant.now().toString().substring(11, 23), message);
    }

    private static void printHeader(String title) {
        System.out.println("\n" + "=".repeat(80));
        log(title);
        System.out.println("=".repeat(80));
    }

    private static void printSubHeader(String title) {
        System.out.println("\n" + "-".repeat(80));
        log(title);
        System.out.println("-".repeat(80));
    }

    /**
     * Print detailed introduction about HTTP protocols and QUIC
     */
    private static void printIntroduction() {
        System.out.println("=".repeat(80));
        log("🌐 Java HttpClient: HTTP/1.1, HTTP/2, and the Future of HTTP/3 (QUIC)");
        System.out.println("=".repeat(80));
        System.out.println();

        log("📚 HTTP PROTOCOL EVOLUTION:");
        System.out.println();
        log("   HTTP/1.1 (1997):");
        log("   • One request per TCP connection (or sequential with keep-alive)");
        log("   • Head-of-line blocking");
        log("   • Text-based protocol");
        System.out.println();

        log("   HTTP/2 (2015):");
        log("   • Binary protocol");
        log("   • Multiplexing: Multiple requests over single connection");
        log("   • Header compression (HPACK)");
        log("   • Server push capability");
        log("   • Still uses TCP");
        System.out.println();

        log("   HTTP/3 (2022) with QUIC:");
        log("   • Uses UDP instead of TCP");
        log("   • Built-in encryption (TLS 1.3)");
        log("   • Eliminates head-of-line blocking at transport layer");
        log("   • Faster connection establishment (0-RTT)");
        log("   • Better performance on unstable networks");
        log("   • Connection migration (survives IP address changes)");
        System.out.println();

        log("🔧 JAVA 21 HttpClient SUPPORT:");
        log("   ✅ HTTP/1.1 - Fully supported");
        log("   ✅ HTTP/2 - Fully supported (default when available)");
        log("   ❌ HTTP/3 (QUIC) - NOT supported in standard library");
        System.out.println();

        log("💡 HTTP/3 ALTERNATIVES IN JAVA:");
        log("   • Netty with netty-incubator-codec-http3");
        log("   • Eclipse Jetty 12+ (experimental HTTP/3 support)");
        log("   • Third-party QUIC implementations");
        System.out.println();

        log(String.format("☕ Java Version: %s", System.getProperty("java.version")));
        System.out.println("=".repeat(80));
    }

    /**
     * Example 1: Basic HTTP/2 Request
     * Demonstrates how Java HttpClient automatically uses HTTP/2 when available
     */
    private static void demonstrateBasicHttp2() throws IOException, InterruptedException {
        printHeader("EXAMPLE 1: Basic HTTP/2 Request");
        log("Demonstrating HTTP/2 support in Java HttpClient");
        log("The client will automatically negotiate HTTP/2 when the server supports it\n");

        // Line 129: Create HttpClient with HTTP/2 preference
        HttpClient client = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_2)  // Prefer HTTP/2
                .connectTimeout(Duration.ofSeconds(10))
                .build();

        // Line 135: Create HTTP request
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://www.google.com"))
                .timeout(Duration.ofSeconds(10))
                .GET()
                .build();

        log("📤 Sending request to: https://www.google.com");
        Instant start = Instant.now();

        // Line 145: Send synchronous request
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        Duration duration = Duration.between(start, Instant.now());

        log(String.format("📥 Response received in %d ms", duration.toMillis()));
        log(String.format("   Status Code: %d", response.statusCode()));
        log(String.format("   HTTP Version: %s", response.version()));
        log(String.format("   Content Length: %d bytes", response.body().length()));

        // Line 156: Check for Alt-Svc header (indicates HTTP/3 support)
        response.headers().firstValue("alt-svc").ifPresentOrElse(
            altSvc -> {
                log(String.format("   🚀 Alt-Svc Header: %s", altSvc));
                log("   💡 This header indicates the server supports HTTP/3!");
            },
            () -> log("   ℹ️  No Alt-Svc header found (server may not support HTTP/3)")
        );

        // Show some important response headers
        log("\n   📋 Selected Response Headers:");
        List<String> interestingHeaders = List.of("content-type", "server", "cache-control");
        interestingHeaders.forEach(headerName ->
            response.headers().firstValue(headerName).ifPresent(value ->
                log(String.format("      %s: %s", headerName, value))
            )
        );

        System.out.println();
    }

    /**
     * Example 2: HTTP Version Comparison
     * Tests the same endpoint with HTTP/1.1 and HTTP/2
     */
    private static void demonstrateVersionComparison() throws IOException, InterruptedException {
        printHeader("EXAMPLE 2: HTTP/1.1 vs HTTP/2 Performance Comparison");
        log("Comparing performance between HTTP/1.1 and HTTP/2\n");

        String testUrl = "https://www.cloudflare.com";

        // Test with HTTP/1.1
        printSubHeader("Testing with HTTP/1.1");
        HttpClient http1Client = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_1_1)  // Line 194: Force HTTP/1.1
                .connectTimeout(Duration.ofSeconds(10))
                .build();

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(testUrl))
                .timeout(Duration.ofSeconds(10))
                .GET()
                .build();

        Instant start1 = Instant.now();
        HttpResponse<String> response1 = http1Client.send(request, HttpResponse.BodyHandlers.ofString());
        Duration duration1 = Duration.between(start1, Instant.now());

        log(String.format("📥 HTTP/1.1 Response: %d ms", duration1.toMillis()));
        log(String.format("   Version: %s", response1.version()));
        log(String.format("   Status: %d", response1.statusCode()));

        // Test with HTTP/2
        printSubHeader("Testing with HTTP/2");
        HttpClient http2Client = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_2)  // Line 218: Force HTTP/2
                .connectTimeout(Duration.ofSeconds(10))
                .build();

        Instant start2 = Instant.now();
        HttpResponse<String> response2 = http2Client.send(request, HttpResponse.BodyHandlers.ofString());
        Duration duration2 = Duration.between(start2, Instant.now());

        log(String.format("📥 HTTP/2 Response: %d ms", duration2.toMillis()));
        log(String.format("   Version: %s", response2.version()));
        log(String.format("   Status: %d", response2.statusCode()));

        // Comparison
        printSubHeader("Comparison Results");
        log(String.format("HTTP/1.1 Time: %d ms", duration1.toMillis()));
        log(String.format("HTTP/2 Time:   %d ms", duration2.toMillis()));

        if (duration1.toMillis() > duration2.toMillis()) {
            double improvement = ((double) duration1.toMillis() / duration2.toMillis());
            log(String.format("🚀 HTTP/2 is %.2fx faster for this request!", improvement));
        }

        log("\n💡 Note: HTTP/2 advantages are more pronounced with multiple concurrent requests");
        log("   due to multiplexing (multiple requests over single connection)\n");
    }

    /**
     * Example 3: Asynchronous Requests with HTTP/2
     * Demonstrates non-blocking HTTP requests using CompletableFuture
     */
    private static void demonstrateAsyncRequests() throws InterruptedException, ExecutionException {
        printHeader("EXAMPLE 3: Asynchronous HTTP/2 Requests");
        log("Demonstrating concurrent async requests with HTTP/2 multiplexing");
        log("All requests will use a SINGLE HTTP/2 connection\n");

        // Line 257: Create HTTP/2 client
        HttpClient client = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_2)
                .connectTimeout(Duration.ofSeconds(10))
                .build();

        // Test URLs
        List<String> urls = List.of(
                "https://www.google.com",
                "https://www.cloudflare.com",
                "https://www.github.com",
                "https://www.stackoverflow.com",
                "https://www.wikipedia.org"
        );

        log(String.format("📤 Sending %d async requests concurrently...\n", urls.size()));
        Instant start = Instant.now();

        // Line 275: Send async requests
        List<CompletableFuture<HttpResponse<String>>> futures = urls.stream()
                .map(url -> HttpRequest.newBuilder()
                        .uri(URI.create(url))
                        .timeout(Duration.ofSeconds(10))
                        .GET()
                        .build())
                .map(request -> client.sendAsync(request, HttpResponse.BodyHandlers.ofString())  // Line 283: Async send
                        .thenApply(response -> {
                            log(String.format("📥 Response from %s: %d (%s) - %d bytes",
                                    response.uri().getHost(),
                                    response.statusCode(),
                                    response.version(),
                                    response.body().length()));
                            return response;
                        })
                        .exceptionally(throwable -> {
                            log(String.format("❌ Error fetching %s: %s",
                                    request.uri().getHost(),
                                    throwable.getMessage()));
                            return null;
                        }))
                .collect(Collectors.toList());

        // Line 300: Wait for all requests to complete
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).get();

        Duration duration = Duration.between(start, Instant.now());

        log(String.format("\n⏱️  Total time for %d concurrent requests: %d ms", urls.size(), duration.toMillis()));
        log(String.format("📊 Average time per request: %d ms", duration.toMillis() / urls.size()));
        log("\n💡 HTTP/2 multiplexing allows all requests to share a single connection!");
        log("   This reduces latency and connection overhead significantly.\n");
    }

    /**
     * Example 4: Detecting HTTP/3 Support via Alt-Svc Header
     * Shows how to check if a server advertises HTTP/3 availability
     */
    private static void demonstrateHttp3Detection() throws IOException, InterruptedException {
        printHeader("EXAMPLE 4: Detecting HTTP/3 (QUIC) Support");
        log("Checking if servers advertise HTTP/3 support via Alt-Svc header");
        log("Even though Java's HttpClient can't use HTTP/3, we can detect it\n");

        HttpClient client = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_2)
                .connectTimeout(Duration.ofSeconds(10))
                .build();

        // Known HTTP/3 enabled servers
        List<String> http3Servers = List.of(
                "https://www.cloudflare.com",
                "https://www.google.com",
                "https://www.facebook.com",
                "https://blog.cloudflare.com"
        );

        for (String url : http3Servers) {
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .timeout(Duration.ofSeconds(10))
                    .GET()
                    .build();

            try {
                HttpResponse<Void> response = client.send(request, HttpResponse.BodyHandlers.discarding());

                log(String.format("\n🌐 Checking: %s", url));
                log(String.format("   HTTP Version used: %s", response.version()));

                // Line 349: Check Alt-Svc header
                response.headers().firstValue("alt-svc").ifPresentOrElse(
                    altSvc -> {
                        log(String.format("   ✅ Alt-Svc: %s", altSvc));
                        if (altSvc.contains("h3=") || altSvc.contains("h3-29") || altSvc.contains("h3-27")) {
                            log("   🚀 HTTP/3 IS AVAILABLE on this server!");
                            log("      (A QUIC-capable client could use UDP instead of TCP)");
                        }
                    },
                    () -> log("   ℹ️  No Alt-Svc header found")
                );

            } catch (IOException e) {
                log(String.format("   ❌ Error: %s", e.getMessage()));
            }
        }

        log("\n💡 What is Alt-Svc?");
        log("   The 'alt-svc' (Alternative Service) header tells clients that the");
        log("   same resource is available via a different protocol/port.");
        log("   Format: h3=\":443\"; ma=2592000 means:");
        log("   • h3: HTTP/3 protocol");
        log("   • :443: Available on port 443");
        log("   • ma=2592000: Valid for 30 days (max-age)\n");
    }

    /**
     * Example 5: Advanced HTTP/2 Features
     * Demonstrates POST requests, custom headers, and request configuration
     */
    private static void demonstrateAdvancedFeatures() throws IOException, InterruptedException {
        printHeader("EXAMPLE 5: Advanced HTTP/2 Client Features");
        log("Demonstrating POST requests, custom headers, and client configuration\n");

        // Line 386: Create client with advanced configuration
        HttpClient client = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_2)
                .followRedirects(HttpClient.Redirect.NORMAL)  // Follow redirects
                .connectTimeout(Duration.ofSeconds(10))
                .build();

        // Example: POST request with JSON body
        printSubHeader("POST Request with JSON Body");

        String jsonBody = """
                {
                    "title": "HTTP/3 and QUIC in Java",
                    "content": "Exploring modern HTTP protocols",
                    "tags": ["java", "http3", "quic", "networking"]
                }
                """;

        HttpRequest postRequest = HttpRequest.newBuilder()
                .uri(URI.create("https://jsonplaceholder.typicode.com/posts"))
                .timeout(Duration.ofSeconds(10))
                .header("Content-Type", "application/json")  // Line 407: Custom header
                .header("Accept", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))  // Line 409: POST body
                .build();

        log("📤 Sending POST request with JSON payload...");
        Instant start = Instant.now();

        HttpResponse<String> response = client.send(postRequest, HttpResponse.BodyHandlers.ofString());

        Duration duration = Duration.between(start, Instant.now());

        log(String.format("📥 Response received in %d ms", duration.toMillis()));
        log(String.format("   Status: %d", response.statusCode()));
        log(String.format("   HTTP Version: %s", response.version()));
        log(String.format("   Response body: %s...", response.body().substring(0, Math.min(100, response.body().length()))));

        // Show request details
        printSubHeader("Request Configuration Details");
        log("Request Headers:");
        postRequest.headers().map().forEach((key, values) ->
            log(String.format("   %s: %s", key, String.join(", ", values)))
        );

        log("\n💡 HTTP/2 Features Used:");
        log("   • Binary framing for efficient transmission");
        log("   • Header compression (HPACK) reduces overhead");
        log("   • Stream multiplexing (if multiple requests were sent)");
        log("   • Automatic connection reuse\n");
    }

    /**
     * Print comprehensive summary
     */
    private static void printSummary() {
        printHeader("📊 SUMMARY: HTTP Protocols in Java 21");
        System.out.println();

        log("🎯 JAVA HttpClient CAPABILITIES:");
        System.out.println();
        log("✅ HTTP/1.1:");
        log("   • Fully supported");
        log("   • Sequential request/response model");
        log("   • Good for simple use cases");
        System.out.println();

        log("✅ HTTP/2:");
        log("   • Fully supported (default)");
        log("   • Multiplexing: multiple requests over single connection");
        log("   • Binary protocol with header compression");
        log("   • Much better performance than HTTP/1.1");
        System.out.println();

        log("❌ HTTP/3 (QUIC):");
        log("   • NOT supported in standard Java 21 HttpClient");
        log("   • Requires third-party libraries");
        log("   • Based on UDP instead of TCP");
        log("   • Offers best performance, especially on unstable networks");
        System.out.println();

        log("📈 WHEN TO USE HTTP/3 (Future):");
        log("   ✅ Mobile applications (connection migration)");
        log("   ✅ Real-time applications (lower latency)");
        log("   ✅ Unstable networks (packet loss resilience)");
        log("   ✅ 0-RTT reconnections (faster subsequent connections)");
        System.out.println();

        log("🔧 HTTP/3 SOLUTIONS FOR JAVA:");
        log("   1. Netty with netty-incubator-codec-http3");
        log("   2. Eclipse Jetty 12+ (experimental)");
        log("   3. Wait for future Java versions (JEP proposal pending)");
        System.out.println();

        log("💡 KEY TAKEAWAYS:");
        log("   • Java 21's HttpClient is production-ready for HTTP/1.1 and HTTP/2");
        log("   • HTTP/2 provides excellent performance for most use cases");
        log("   • HTTP/3 support requires third-party libraries");
        log("   • Alt-Svc header indicates HTTP/3 availability");
        log("   • QUIC (HTTP/3's transport) eliminates head-of-line blocking");
        System.out.println();

        System.out.println("=".repeat(80));
        log("✨ Java's HttpClient is a modern, high-performance HTTP library!");
        log("🔮 HTTP/3 support may come in future Java releases");
        System.out.println("=".repeat(80));
    }

    /**
     * Main method - orchestrates all demonstrations
     */
    public static void main(String[] args) {
        try {
            printIntroduction();

            // Run all demonstrations
            demonstrateBasicHttp2();
            demonstrateVersionComparison();
            demonstrateAsyncRequests();
            demonstrateHttp3Detection();
            demonstrateAdvancedFeatures();

            printSummary();

            System.out.println();
            log("🎉 Demonstration complete!");

        } catch (IOException e) {
            System.err.println("❌ IO Error: " + e.getMessage());
            e.printStackTrace();
        } catch (InterruptedException e) {
            System.err.println("❌ Interrupted: " + e.getMessage());
            Thread.currentThread().interrupt();
        } catch (ExecutionException e) {
            System.err.println("❌ Execution Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
