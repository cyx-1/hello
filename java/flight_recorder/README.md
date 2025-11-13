# Java Flight Recorder (JFR) Demo

This example demonstrates **Java Flight Recorder (JFR)**, a powerful profiling and diagnostics tool built into the JVM. JFR provides deep insights into application performance with minimal overhead (typically < 1%), making it suitable for production environments.

## What is Java Flight Recorder?

Java Flight Recorder is a profiling and event collection framework built into the JDK since Java 11. It can:
- Record detailed runtime information about Java applications
- Track CPU usage, memory allocation, garbage collection, thread activity
- Define custom application events
- Generate `.jfr` files that can be analyzed with JDK Mission Control or command-line tools

## Requirements

- **Java 11 or later** (this demo uses Java 17+)
- JFR is built into the JDK - no external dependencies needed

## Running the Demo

```bash
javac MainFlightRecorder.java
java MainFlightRecorder
```

Or with Maven:
```bash
mvn clean compile
mvn exec:java
```

## Source Code with Line Numbers

### Custom Event Definition (Lines 18-33)

```java
18    @Name("com.example.BusinessOperation")
19    @Label("Business Operation")
20    @Description("Custom event tracking business operations")
21    @Category("Application")
22    static class BusinessOperationEvent extends Event {
23        @Label("Operation Name")
24        String operationName;
25
26        @Label("Duration (ms)")
27        long durationMs;
28
29        @Label("Items Processed")
30        int itemsProcessed;
31
32        @Label("Status")
33        String status;
34    }
```

**Key Points:**
- Lines 18-21: JFR annotations define event metadata that appears in profiling tools
- Lines 22-34: Custom event class extends `jdk.jfr.Event` to track business operations
- Events can include custom fields to capture application-specific metrics

### Recording Configuration (Lines 44-56)

```java
44        System.out.println("1. Starting Flight Recorder...");
45        Recording recording = new Recording(config);
46        // Line 51: Configure recording settings
47        recording.setName("Performance Analysis");
48        recording.setMaxAge(Duration.ofMinutes(5));
49        recording.setMaxSize(50 * 1024 * 1024); // 50 MB
50
51        // Line 58: Enable specific event types
52        recording.enable("jdk.CPULoad").withPeriod(Duration.ofSeconds(1));
53        recording.enable("jdk.GarbageCollection");
54        recording.enable("jdk.JavaMonitorEnter");
55        recording.enable("jdk.ThreadAllocationStatistics");
56        recording.enable("com.example.BusinessOperation"); // Our custom event
```

**Key Points:**
- Line 45: Create a new recording with default configuration
- Lines 47-49: Set recording constraints (name, max age, max size)
- Lines 52-56: Enable specific event types to track (CPU, GC, threads, custom events)
- Line 52: CPU load sampled every 1 second

### Database Operation Tracking (Lines 91-108)

```java
91    private static void performDatabaseOperations() throws InterruptedException {
92        System.out.println("   > Database operations...");
93        long startTime = System.currentTimeMillis();
94        BusinessOperationEvent event = new BusinessOperationEvent();
95        event.begin(); // Start timing
96
97        event.operationName = "Database Query";
98        Thread.sleep(150); // Simulate DB query time
99        int recordsProcessed = 1250;
100       event.itemsProcessed = recordsProcessed;
101
102       event.end(); // Stop timing
103       event.durationMs = System.currentTimeMillis() - startTime;
104       event.status = "SUCCESS";
105       event.commit(); // Record to JFR
106
107       System.out.println("     Processed " + recordsProcessed + " records in " + event.durationMs + "ms");
108   }
```

**Key Points:**
- Line 95: `event.begin()` starts the JFR event timer
- Lines 97-100: Set event properties during operation execution
- Line 102: `event.end()` stops the timer
- Line 105: `event.commit()` writes the event to the flight recording

### CPU-Intensive Work (Lines 111-127)

```java
111   private static void performCpuIntensiveWork() {
112       System.out.println("   > CPU-intensive computation...");
113       long startTime = System.currentTimeMillis();
114       BusinessOperationEvent event = new BusinessOperationEvent();
115       event.begin();
116
117       event.operationName = "Prime Number Calculation";
118       int count = calculatePrimes(100000);
119
120       event.itemsProcessed = count;
121       event.end();
122       event.durationMs = System.currentTimeMillis() - startTime;
123       event.status = "SUCCESS";
124       event.commit();
125
126       System.out.println("     Found " + count + " primes in " + event.durationMs + "ms");
127   }
```

**Key Points:**
- Line 118: CPU-intensive prime number calculation to generate CPU load events
- This operation will show up in JFR's CPU profiling data

### Stopping and Dumping Recording (Lines 70-76)

```java
70        // Line 77: Stop recording and dump to file
71        System.out.println("\n3. Stopping recording and dumping data...");
72        recording.stop();
73        recording.dump(recordingFile);
74        recording.close();
75        System.out.println("   Recording saved to: " + recordingFile.toAbsolutePath());
76        System.out.println();
```

**Key Points:**
- Line 72: Stop collecting events
- Line 73: Write recording to `recording.jfr` file
- Line 74: Clean up recording resources

### Analyzing Recording Data (Lines 218-260)

```java
218   private static void analyzeRecording(Path recordingFile) throws IOException {
219       System.out.println("   Key Metrics from Recording:\n");
220
221       try (RecordingFile recording = new RecordingFile(recordingFile)) {
222           int customEventCount = 0;
223           int gcEventCount = 0;
224           long totalGcPauseMs = 0;
225
226           while (recording.hasMoreEvents()) {
227               RecordedEvent event = recording.readEvent();
228
229               // Line 231: Count custom business events
230               if (event.getEventType().getName().equals("com.example.BusinessOperation")) {
231                   customEventCount++;
232                   String opName = event.getString("operationName");
233                   long duration = event.getLong("durationMs");
234                   int items = event.getInt("itemsProcessed");
235                   System.out.println("     • " + opName + ": " + duration + "ms, " +
236                                     items + " items");
237               }
238
239               // Line 242: Track garbage collection events
240               if (event.getEventType().getName().equals("jdk.GarbageCollection")) {
241                   gcEventCount++;
242                   Duration gcTime = event.getDuration();
243                   totalGcPauseMs += gcTime.toMillis();
244               }
245           }
246
247           System.out.println("\n   Summary Statistics:");
248           System.out.println("     • Custom business events: " + customEventCount);
249           System.out.println("     • Garbage collections: " + gcEventCount);
250           System.out.println("     • Total GC pause time: " + totalGcPauseMs + "ms");
251
252           if (gcEventCount > 0) {
253               System.out.println("     • Average GC pause: " +
254                                 (totalGcPauseMs / gcEventCount) + "ms");
255           }
256       }
257   }
```

**Key Points:**
- Line 221: Open the `.jfr` file for reading
- Lines 226-227: Iterate through all recorded events
- Lines 230-237: Extract and display custom business operation events
- Lines 240-244: Track garbage collection events and pause times
- This demonstrates programmatic analysis of flight recordings

## Program Output

```
=== Java Flight Recorder Demo ===

1. Starting Flight Recorder...
   Recording started: Performance Analysis
   Recording to file: /home/user/hello/java/flight_recorder/recording.jfr

2. Simulating application workload...
   > Database operations...
     Processed 1250 records in 159ms
   > CPU-intensive computation...
     Found 9592 primes in 4ms
   > Memory allocation...
     Allocated 9 MB in 38ms
   > Concurrent thread operations...
     Completed 5 concurrent tasks in 8ms

3. Stopping recording and dumping data...
   Recording saved to: /home/user/hello/java/flight_recorder/recording.jfr

4. Analyzing Flight Recording Data...

   Key Metrics from Recording:

     • Database Query: 159ms, 1250 items
     • Prime Number Calculation: 4ms, 9592 items
     • Data Processing: 38ms, 100 items
     • Multi-threaded Processing: 8ms, 5 items

   Summary Statistics:
     • Custom business events: 4
     • Garbage collections: 1
     • Total GC pause time: 5ms
     • Average GC pause: 5ms

=== Demo Complete ===

To view the full recording in JDK Mission Control:
  jmc -open /home/user/hello/java/flight_recorder/recording.jfr

Or use 'jfr print recording.jfr' for text output
```

## Output Annotations

### Section 1: Starting the Recorder
- **Lines 1-5 (Output)**: Recording initialization corresponding to **Lines 44-60 (Code)**
- The recording is configured with a name, size limits, and enabled event types
- Output confirms the recording file path where data will be saved

### Section 2: Workload Simulation
- **"Database operations" (Output)**: Generated by **Lines 91-108 (Code)**
  - Simulates 150ms query processing 1250 records
  - Actual output shows ~159ms due to system scheduling

- **"CPU-intensive computation" (Output)**: Generated by **Lines 111-127 (Code)**
  - Calculates primes up to 100,000
  - Found 9,592 primes in 4ms, demonstrating efficient prime calculation

- **"Memory allocation" (Output)**: Generated by **Lines 130-156 (Code)**
  - Allocates 100 chunks of 100KB each (9.5 MB total)
  - Completed in 38ms

- **"Concurrent thread operations" (Output)**: Generated by **Lines 159-189 (Code)**
  - Spawns 5 worker threads performing concurrent prime calculations
  - All threads completed in 8ms total

### Section 3: Dumping Recording
- **Lines 16-18 (Output)**: Recording save operation from **Lines 70-76 (Code)**
- Confirms the `.jfr` file has been written to disk

### Section 4: Analysis Results
- **"Key Metrics" (Output)**: Parsed by **Lines 230-237 (Code)**
  - Shows all 4 custom `BusinessOperationEvent` entries with their durations
  - Each event includes operation name, duration, and items processed

- **"Summary Statistics" (Output)**: Calculated by **Lines 247-255 (Code)**
  - 4 custom business events recorded (one for each operation)
  - 1 garbage collection occurred during the 9MB memory allocation
  - GC pause was only 5ms, showing minimal impact on performance

## Advanced Analysis

The generated `recording.jfr` file contains much more data than shown in the output. To view comprehensive details:

### Using Command Line
```bash
# Summary information
jfr summary recording.jfr

# Print all events
jfr print recording.jfr

# Print specific event types
jfr print --events jdk.GarbageCollection recording.jfr
jfr print --events com.example.BusinessOperation recording.jfr

# Generate JSON output
jfr print --json recording.jfr > recording.json
```

### Using JDK Mission Control (GUI)
```bash
jmc -open recording.jfr
```

JMC provides:
- Visual timeline of events
- CPU usage graphs
- Memory allocation flame graphs
- Thread activity analysis
- Lock contention visualization
- Custom event tables and charts

## Key Takeaways

1. **Low Overhead**: JFR has minimal performance impact (< 1%), making it safe for production
2. **Rich Data**: Captures CPU, memory, GC, threads, I/O, and custom events
3. **Custom Events**: Easily define application-specific events for business logic tracking
4. **Post-Mortem Analysis**: Recording files can be analyzed offline with various tools
5. **Built-in Tool**: No external dependencies required - part of the JDK since Java 11

## Use Cases

- **Performance Optimization**: Identify CPU hotspots and memory allocation patterns
- **Production Monitoring**: Diagnose issues in live systems with minimal overhead
- **Capacity Planning**: Understand resource usage patterns under load
- **Troubleshooting**: Record and analyze application behavior during incidents
- **Compliance**: Track business operations and their performance characteristics
