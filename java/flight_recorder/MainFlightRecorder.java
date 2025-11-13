import jdk.jfr.*;
import jdk.jfr.consumer.*;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * Demonstration of Java Flight Recorder (JFR) - a profiling and diagnostics tool
 * JFR has minimal performance overhead (typically < 1%) and can be used in production
 */
public class MainFlightRecorder {

    // Custom JFR Event - Line 18
    @Name("com.example.BusinessOperation")
    @Label("Business Operation")
    @Description("Custom event tracking business operations")
    @Category("Application")
    static class BusinessOperationEvent extends Event {
        @Label("Operation Name")
        String operationName;

        @Label("Duration (ms)")
        long durationMs;

        @Label("Items Processed")
        int itemsProcessed;

        @Label("Status")
        String status;
    }

    public static void main(String[] args) throws Exception {
        System.out.println("=== Java Flight Recorder Demo ===\n");

        // Line 44: Configure and start JFR recording
        Configuration config = Configuration.getConfiguration("default");
        Path recordingFile = Paths.get("recording.jfr");

        System.out.println("1. Starting Flight Recorder...");
        Recording recording = new Recording(config);
        // Line 51: Configure recording settings
        recording.setName("Performance Analysis");
        recording.setMaxAge(Duration.ofMinutes(5));
        recording.setMaxSize(50 * 1024 * 1024); // 50 MB

        // Line 58: Enable specific event types
        recording.enable("jdk.CPULoad").withPeriod(Duration.ofSeconds(1));
        recording.enable("jdk.GarbageCollection");
        recording.enable("jdk.JavaMonitorEnter");
        recording.enable("jdk.ThreadAllocationStatistics");
        recording.enable("com.example.BusinessOperation"); // Our custom event

        recording.start();
        System.out.println("   Recording started: " + recording.getName());
        System.out.println("   Recording to file: " + recordingFile.toAbsolutePath());
        System.out.println();

        // Line 70: Simulate application workload
        System.out.println("2. Simulating application workload...");
        performDatabaseOperations();
        performCpuIntensiveWork();
        performMemoryIntensiveWork();
        performConcurrentOperations();

        // Line 77: Stop recording and dump to file
        System.out.println("\n3. Stopping recording and dumping data...");
        recording.stop();
        recording.dump(recordingFile);
        recording.close();
        System.out.println("   Recording saved to: " + recordingFile.toAbsolutePath());
        System.out.println();

        // Line 85: Read and analyze the recording
        System.out.println("4. Analyzing Flight Recording Data...\n");
        analyzeRecording(recordingFile);

        System.out.println("\n=== Demo Complete ===");
        System.out.println("\nTo view the full recording in JDK Mission Control:");
        System.out.println("  jmc -open " + recordingFile.toAbsolutePath());
        System.out.println("\nOr use 'jfr print recording.jfr' for text output");
    }

    // Line 96: Simulate database operations with custom events
    private static void performDatabaseOperations() throws InterruptedException {
        System.out.println("   > Database operations...");
        long startTime = System.currentTimeMillis();
        BusinessOperationEvent event = new BusinessOperationEvent();
        event.begin(); // Start timing

        event.operationName = "Database Query";
        Thread.sleep(150); // Simulate DB query time
        int recordsProcessed = 1250;
        event.itemsProcessed = recordsProcessed;

        event.end(); // Stop timing
        event.durationMs = System.currentTimeMillis() - startTime;
        event.status = "SUCCESS";
        event.commit(); // Record to JFR

        System.out.println("     Processed " + recordsProcessed + " records in " + event.durationMs + "ms");
    }

    // Line 116: Simulate CPU-intensive work
    private static void performCpuIntensiveWork() {
        System.out.println("   > CPU-intensive computation...");
        long startTime = System.currentTimeMillis();
        BusinessOperationEvent event = new BusinessOperationEvent();
        event.begin();

        event.operationName = "Prime Number Calculation";
        int count = calculatePrimes(100000);

        event.itemsProcessed = count;
        event.end();
        event.durationMs = System.currentTimeMillis() - startTime;
        event.status = "SUCCESS";
        event.commit();

        System.out.println("     Found " + count + " primes in " + event.durationMs + "ms");
    }

    // Line 136: Simulate memory-intensive work
    private static void performMemoryIntensiveWork() {
        System.out.println("   > Memory allocation...");
        long startTime = System.currentTimeMillis();
        BusinessOperationEvent event = new BusinessOperationEvent();
        event.begin();

        event.operationName = "Data Processing";
        List<byte[]> dataChunks = new ArrayList<>();
        Random random = new Random();

        // Allocate memory in chunks
        for (int i = 0; i < 100; i++) {
            byte[] chunk = new byte[100_000]; // 100 KB per chunk
            random.nextBytes(chunk);
            dataChunks.add(chunk);
        }

        event.itemsProcessed = dataChunks.size();
        event.end();
        event.durationMs = System.currentTimeMillis() - startTime;
        event.status = "SUCCESS";
        event.commit();

        long totalBytes = dataChunks.stream().mapToLong(c -> c.length).sum();
        System.out.println("     Allocated " + (totalBytes / 1024 / 1024) + " MB in " +
                          event.durationMs + "ms");
    }

    // Line 165: Simulate concurrent operations
    private static void performConcurrentOperations() throws InterruptedException {
        System.out.println("   > Concurrent thread operations...");
        long startTime = System.currentTimeMillis();
        BusinessOperationEvent event = new BusinessOperationEvent();
        event.begin();

        event.operationName = "Multi-threaded Processing";
        int threadCount = 5;
        Thread[] threads = new Thread[threadCount];

        for (int i = 0; i < threadCount; i++) {
            final int threadId = i;
            threads[i] = new Thread(() -> {
                calculatePrimes(10000 + threadId * 1000);
            }, "Worker-" + i);
            threads[i].start();
        }

        for (Thread thread : threads) {
            thread.join();
        }

        event.itemsProcessed = threadCount;
        event.end();
        event.durationMs = System.currentTimeMillis() - startTime;
        event.status = "SUCCESS";
        event.commit();

        System.out.println("     Completed " + threadCount + " concurrent tasks in " +
                          event.durationMs + "ms");
    }

    // Line 197: Helper method for CPU work
    private static int calculatePrimes(int limit) {
        int count = 0;
        for (int num = 2; num <= limit; num++) {
            if (isPrime(num)) {
                count++;
            }
        }
        return count;
    }

    private static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    // Line 218: Analyze the recorded data
    private static void analyzeRecording(Path recordingFile) throws IOException {
        System.out.println("   Key Metrics from Recording:\n");

        try (RecordingFile recording = new RecordingFile(recordingFile)) {
            int customEventCount = 0;
            int gcEventCount = 0;
            long totalGcPauseMs = 0;

            while (recording.hasMoreEvents()) {
                RecordedEvent event = recording.readEvent();

                // Line 231: Count custom business events
                if (event.getEventType().getName().equals("com.example.BusinessOperation")) {
                    customEventCount++;
                    String opName = event.getString("operationName");
                    long duration = event.getLong("durationMs");
                    int items = event.getInt("itemsProcessed");
                    System.out.println("     • " + opName + ": " + duration + "ms, " +
                                      items + " items");
                }

                // Line 242: Track garbage collection events
                if (event.getEventType().getName().equals("jdk.GarbageCollection")) {
                    gcEventCount++;
                    Duration gcTime = event.getDuration();
                    totalGcPauseMs += gcTime.toMillis();
                }
            }

            System.out.println("\n   Summary Statistics:");
            System.out.println("     • Custom business events: " + customEventCount);
            System.out.println("     • Garbage collections: " + gcEventCount);
            System.out.println("     • Total GC pause time: " + totalGcPauseMs + "ms");

            if (gcEventCount > 0) {
                System.out.println("     • Average GC pause: " +
                                  (totalGcPauseMs / gcEventCount) + "ms");
            }
        }
    }
}
