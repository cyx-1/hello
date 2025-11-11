import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Java Virtual Threads Demonstration (Java 21+ Project Loom)
 *
 * This example demonstrates the revolutionary virtual threads feature in Java 21,
 * which enables massive concurrency with minimal resource overhead.
 *
 * Key Concepts:
 * 1. Platform Threads vs Virtual Threads
 * 2. Thread creation and lifecycle
 * 3. Performance comparison with I/O-bound tasks
 * 4. Scalability - handling thousands of concurrent tasks
 * 5. Thread pool alternatives
 *
 * Virtual threads are lightweight threads managed by the JVM rather than the OS,
 * allowing applications to handle millions of concurrent tasks efficiently.
 */
public class MainVirtualThread {

    private static final String ANSI_RESET = "\u001B[0m";
    private static final String ANSI_BLUE = "\u001B[34m";
    private static final String ANSI_GREEN = "\u001B[32m";
    private static final String ANSI_YELLOW = "\u001B[33m";
    private static final String ANSI_CYAN = "\u001B[36m";

    // Simple logging with timestamp
    private static void log(String message) {
        System.out.printf("[%s] %s%n", Instant.now().toString().substring(11, 23), message);
    }

    private static void printHeader(String title) {
        System.out.println("\n" + "=".repeat(70));
        log(title);
        System.out.println("=".repeat(70));
    }

    /**
     * Simulates an I/O-bound task (e.g., network call, database query)
     * Virtual threads excel at these types of operations.
     */
    private static int simulateIOTask(String threadName, int taskId, int durationMs) {
        log(String.format("🔵 %s (Task %d): Starting I/O operation...", threadName, taskId));
        try {
            // Simulate I/O wait (e.g., waiting for network response)
            Thread.sleep(durationMs);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return -1;
        }
        log(String.format("✅ %s (Task %d): Completed", threadName, taskId));
        return taskId * 100;  // Return some result
    }

    /**
     * Example 1: Basic Platform Thread Creation
     * Traditional way of creating threads in Java.
     */
    private static void demonstratePlatformThreads() {
        printHeader("EXAMPLE 1: Platform Threads (Traditional Java)");
        log("Creating 5 platform threads for I/O-bound tasks...");
        log("⚠️  Platform threads are OS-managed and relatively expensive\n");

        Instant start = Instant.now();
        List<Thread> threads = new ArrayList<>();

        // Create and start 5 platform threads
        for (int i = 1; i <= 5; i++) {
            final int taskId = i;
            Thread thread = new Thread(() -> {
                simulateIOTask("Platform-" + taskId, taskId, 1000);
            });
            thread.setName("PlatformThread-" + i);
            threads.add(thread);
            thread.start();  // Line 85: Start platform thread
        }

        // Wait for all threads to complete
        for (Thread thread : threads) {
            try {
                thread.join();  // Line 91: Wait for thread completion
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        Duration duration = Duration.between(start, Instant.now());
        log(String.format("\n⏱️  Total Time: %d ms", duration.toMillis()));
        log(String.format("📊 Threads created: %d platform threads", threads.size()));
        log("💡 Each platform thread consumes ~1-2 MB of memory\n");
    }

    /**
     * Example 2: Virtual Thread Creation
     * New lightweight threads introduced in Java 21.
     */
    private static void demonstrateVirtualThreads() {
        printHeader("EXAMPLE 2: Virtual Threads (Java 21+ Project Loom)");
        log("Creating 5 virtual threads for I/O-bound tasks...");
        log("🚀 Virtual threads are JVM-managed and extremely lightweight\n");

        Instant start = Instant.now();
        List<Thread> threads = new ArrayList<>();

        // Create and start 5 virtual threads
        for (int i = 1; i <= 5; i++) {
            final int taskId = i;
            Thread thread = Thread.startVirtualThread(() -> {  // Line 120: Start virtual thread
                simulateIOTask("Virtual-" + taskId, taskId, 1000);
            });
            threads.add(thread);
        }

        // Wait for all threads to complete
        for (Thread thread : threads) {
            try {
                thread.join();  // Line 129: Wait for thread completion
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        Duration duration = Duration.between(start, Instant.now());
        log(String.format("\n⏱️  Total Time: %d ms", duration.toMillis()));
        log(String.format("📊 Threads created: %d virtual threads", threads.size()));
        log("💡 Each virtual thread consumes only ~1 KB of memory!\n");
    }

    /**
     * Example 3: Scalability Comparison
     * Demonstrates handling many concurrent tasks with virtual threads.
     */
    private static void demonstrateScalability() {
        printHeader("EXAMPLE 3: Scalability - 1000 Concurrent Tasks");
        log("Virtual threads enable massive concurrency with minimal overhead");
        log("Simulating 1000 concurrent I/O operations...\n");

        int taskCount = 1000;
        int taskDuration = 100;  // 100ms per task
        AtomicInteger completedTasks = new AtomicInteger(0);

        Instant start = Instant.now();
        List<Thread> threads = new ArrayList<>();

        // Create 1000 virtual threads
        for (int i = 1; i <= taskCount; i++) {
            final int taskId = i;
            Thread thread = Thread.startVirtualThread(() -> {  // Line 162: Create virtual thread
                try {
                    Thread.sleep(taskDuration);
                    int completed = completedTasks.incrementAndGet();
                    if (completed % 100 == 0) {  // Log every 100 completions
                        log(String.format("📈 Progress: %d/%d tasks completed", completed, taskCount));
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
            threads.add(thread);
        }

        // Wait for all threads to complete
        for (Thread thread : threads) {
            try {
                thread.join();  // Line 179: Wait for completion
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        Duration duration = Duration.between(start, Instant.now());
        log(String.format("\n⏱️  Total Time: %d ms", duration.toMillis()));
        log(String.format("📊 Tasks completed: %d", completedTasks.get()));
        log(String.format("🚀 Throughput: %.0f tasks/second", (taskCount * 1000.0) / duration.toMillis()));
        log("💡 Try this with platform threads - you'd likely run out of memory!\n");
    }

    /**
     * Example 4: Virtual Thread Executor
     * Using Executors API with virtual threads.
     */
    private static void demonstrateVirtualThreadExecutor() {
        printHeader("EXAMPLE 4: Virtual Thread Executor");
        log("Using ExecutorService with virtual thread factory");
        log("This is ideal for managing many short-lived tasks\n");

        int taskCount = 100;
        Instant start = Instant.now();

        // Create executor that uses virtual threads
        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {  // Line 207: Virtual thread executor
            for (int i = 1; i <= taskCount; i++) {
                final int taskId = i;
                executor.submit(() -> {  // Line 210: Submit task
                    try {
                        Thread.sleep(50);
                        if (taskId % 20 == 0) {
                            log(String.format("🔄 Task %d completed by %s",
                                    taskId, Thread.currentThread()));
                        }
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                });
            }
            // Executor automatically waits for all tasks with try-with-resources
        }  // Line 224: Executor shuts down here

        Duration duration = Duration.between(start, Instant.now());
        log(String.format("\n⏱️  Total Time: %d ms", duration.toMillis()));
        log(String.format("📊 Tasks submitted: %d", taskCount));
        log("💡 Virtual thread executor creates a new thread for each task!\n");
    }

    /**
     * Example 5: Performance Comparison
     * Direct comparison between platform and virtual threads.
     */
    private static void demonstratePerformanceComparison() {
        printHeader("EXAMPLE 5: Performance Comparison");

        int taskCount = 500;
        int taskDuration = 50;

        // Test with platform threads (using thread pool to avoid creating too many)
        log(String.format("🔵 Testing %d tasks with Platform Thread Pool...", taskCount));
        Instant platformStart = Instant.now();

        try (var executor = Executors.newFixedThreadPool(100)) {  // Line 246: Fixed thread pool
            for (int i = 0; i < taskCount; i++) {
                executor.submit(() -> {
                    try {
                        Thread.sleep(taskDuration);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                });
            }
        }  // Executor shuts down and waits

        Duration platformDuration = Duration.between(platformStart, Instant.now());
        log(String.format("   Platform Thread Pool Time: %d ms\n", platformDuration.toMillis()));

        // Test with virtual threads
        log(String.format("🟢 Testing %d tasks with Virtual Threads...", taskCount));
        Instant virtualStart = Instant.now();

        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {  // Line 266: Virtual thread executor
            for (int i = 0; i < taskCount; i++) {
                executor.submit(() -> {
                    try {
                        Thread.sleep(taskDuration);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                });
            }
        }  // Executor shuts down and waits

        Duration virtualDuration = Duration.between(virtualStart, Instant.now());
        log(String.format("   Virtual Thread Time: %d ms\n", virtualDuration.toMillis()));

        // Comparison
        log("📊 COMPARISON:");
        log(String.format("   Platform Thread Pool (100 threads): %d ms", platformDuration.toMillis()));
        log(String.format("   Virtual Threads (%d threads):      %d ms", taskCount, virtualDuration.toMillis()));

        double speedup = (double) platformDuration.toMillis() / virtualDuration.toMillis();
        log(String.format("   🚀 Speedup: %.2fx faster with virtual threads!", speedup));
        log("   💡 Virtual threads scale much better for I/O-bound workloads\n");
    }

    /**
     * Print introduction explaining virtual threads.
     */
    private static void printIntroduction() {
        System.out.println("=".repeat(70));
        log("☕ Java Virtual Threads (Project Loom - Java 21+)");
        System.out.println("=".repeat(70));
        System.out.println();
        log("📚 WHAT ARE VIRTUAL THREADS?");
        log("   Virtual threads are lightweight threads managed by the JVM");
        log("   instead of the operating system. They enable applications to");
        log("   handle millions of concurrent tasks with minimal overhead.");
        System.out.println();
        log("🆚 PLATFORM THREADS vs VIRTUAL THREADS:");
        log("   Platform Threads (Traditional):");
        log("   • OS-managed, heavyweight (~1-2 MB stack per thread)");
        log("   • Limited by OS resources (typically 1000s)");
        log("   • Direct 1:1 mapping to OS threads");
        System.out.println();
        log("   Virtual Threads (Java 21+):");
        log("   • JVM-managed, lightweight (~1 KB per thread)");
        log("   • Can create millions of threads");
        log("   • Many virtual threads share a small pool of OS threads");
        System.out.println();
        log("✨ BENEFITS:");
        log("   • Massive concurrency for I/O-bound applications");
        log("   • Simple synchronous code (no callbacks/reactive complexity)");
        log("   • Better resource utilization");
        log("   • Easier debugging and profiling");
        System.out.println();
        log("⚠️  BEST FOR:");
        log("   • I/O-bound tasks (network, database, file operations)");
        log("   • High-concurrency web servers");
        log("   • Microservices with many external API calls");
        System.out.println();
        log("❌ NOT IDEAL FOR:");
        log("   • CPU-bound tasks (use parallel streams or ForkJoin instead)");
        log("   • Tasks with long-running CPU computations");
        System.out.println();
        log(String.format("Java Version: %s", System.getProperty("java.version")));

        // Check if running on Java 21+
        String version = System.getProperty("java.version");
        String majorVersion = version.split("\\.")[0];
        int versionNumber = Integer.parseInt(majorVersion);

        if (versionNumber >= 21) {
            log("✅ Virtual threads are supported!");
        } else {
            log("⚠️  Virtual threads require Java 21 or higher");
        }
        System.out.println("=".repeat(70));
    }

    /**
     * Print summary of demonstrations.
     */
    private static void printSummary() {
        printHeader("📊 SUMMARY");
        System.out.println();
        log("🎯 KEY TAKEAWAYS:");
        System.out.println();
        log("1. LIGHTWEIGHT:");
        log("   • Platform threads: ~1-2 MB per thread");
        log("   • Virtual threads: ~1 KB per thread (1000x lighter!)");
        System.out.println();
        log("2. SCALABILITY:");
        log("   • Platform threads: Limited to 1000s");
        log("   • Virtual threads: Can create millions!");
        System.out.println();
        log("3. USE CASES:");
        log("   ✅ Perfect for I/O-bound operations");
        log("   ✅ High-concurrency web applications");
        log("   ✅ Microservices with many API calls");
        log("   ❌ Not for CPU-intensive computations");
        System.out.println();
        log("4. SIMPLICITY:");
        log("   • Write synchronous code (easier than async/reactive)");
        log("   • No callback hell");
        log("   • Better stack traces and debugging");
        System.out.println();
        log("5. MIGRATION:");
        log("   • Thread.startVirtualThread(() -> {...})");
        log("   • Executors.newVirtualThreadPerTaskExecutor()");
        log("   • Compatible with existing Thread API!");
        System.out.println();
        System.out.println("=".repeat(70));
        log("✨ Virtual threads are a game-changer for concurrent Java applications!");
        System.out.println("=".repeat(70));
    }

    public static void main(String[] args) {
        printIntroduction();

        // Run all demonstrations
        demonstratePlatformThreads();
        demonstrateVirtualThreads();
        demonstrateScalability();
        demonstrateVirtualThreadExecutor();
        demonstratePerformanceComparison();

        printSummary();

        System.out.println();
        log("🎉 Demonstration complete!");
    }
}
