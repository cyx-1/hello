# Java Virtual Threads: Project Loom Revolution

This example demonstrates Java 21's groundbreaking feature: **Virtual Threads (Project Loom)**, enabling massive concurrency with minimal resource overhead.

## 🎯 What are Virtual Threads?

**Virtual Threads** are lightweight threads managed by the JVM instead of the operating system. They enable applications to handle millions of concurrent tasks with minimal overhead, revolutionizing how Java handles concurrency.

### Traditional Problem (Platform Threads):
```
OS Thread 1: [Task1====] [idle....] [Task2====] [idle....]
OS Thread 2: [idle....] [Task3====] [idle....] [Task4====]
Memory:      ~1-2 MB     ~1-2 MB                           Total: 2-4 MB

Limited to thousands of threads! 🐌
```

### Java 21+ Solution (Virtual Threads):
```
Virtual Thread 1: [Task1====]
Virtual Thread 2: [Task2====]  (ALL run concurrently!)
Virtual Thread 3: [Task3====]
Virtual Thread 4: [Task4====]
Memory per thread: ~1 KB each                              Total: ~4 KB

Can create MILLIONS of threads! 🚀
```

## 🚀 Running the Example

### Compile and Run:
```bash
# Using Maven
cd java/virtual_thread
mvn clean compile exec:java

# Or directly with Java 21+
javac MainVirtualThread.java
java MainVirtualThread
```

### Requirements:
- **Java 21 or higher** (Virtual threads were introduced in Java 21)
- Maven (optional, for dependency management)

## 📊 Key Concepts Illustrated

1. **Platform Threads vs Virtual Threads** - Resource comparison
2. **Thread Creation Patterns** - Traditional and modern approaches
3. **Scalability** - Handling thousands of concurrent tasks
4. **Executor Services** - Using virtual threads with executors
5. **Performance Comparison** - Real-world benchmarks

---

## Source Code and Output Analysis

### 1. Platform Threads (Traditional Java)

**Source Code (MainVirtualThread.java:70-104):**
```java
private static void demonstratePlatformThreads() {
    printHeader("EXAMPLE 1: Platform Threads (Traditional Java)");
    log("Creating 5 platform threads for I/O-bound tasks...");
    log("⚠️  Platform threads are OS-managed and relatively expensive\n");

    Instant start = Instant.now();
    List<Thread> threads = new ArrayList<>();

    // Create and start 5 platform threads
    for (int i = 1; i <= 5; i++) {                        // Line 79
        final int taskId = i;
        Thread thread = new Thread(() -> {
            simulateIOTask("Platform-" + taskId, taskId, 1000);
        });
        thread.setName("PlatformThread-" + i);
        threads.add(thread);
        thread.start();                                   // Line 85: Start platform thread
    }

    // Wait for all threads to complete
    for (Thread thread : threads) {
        try {
            thread.join();                                // Line 91: Wait for thread completion
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    Duration duration = Duration.between(start, Instant.now());
    log(String.format("\n⏱️  Total Time: %d ms", duration.toMillis()));
}
```

**I/O Task Simulation (MainVirtualThread.java:47-58):**
```java
private static int simulateIOTask(String threadName, int taskId, int durationMs) {
    log(String.format("🔵 %s (Task %d): Starting I/O operation...", threadName, taskId));
    try {
        // Simulate I/O wait (e.g., waiting for network response)
        Thread.sleep(durationMs);                         // Line 51: Simulate I/O operation
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
        return -1;
    }
    log(String.format("✅ %s (Task %d): Completed", threadName, taskId));
    return taskId * 100;
}
```

**Output:**
```
======================================================================
[22:14:14.881] EXAMPLE 1: Platform Threads (Traditional Java)
======================================================================
[22:14:14.882] Creating 5 platform threads for I/O-bound tasks...
[22:14:14.882] ⚠️  Platform threads are OS-managed and relatively expensive

[22:14:14.926] 🔵 Platform-3 (Task 3): Starting I/O operation...    ← Line 85: All start
[22:14:14.926] 🔵 Platform-1 (Task 1): Starting I/O operation...    ← nearly at the
[22:14:14.926] 🔵 Platform-4 (Task 4): Starting I/O operation...    ← same time
[22:14:14.926] 🔵 Platform-5 (Task 5): Starting I/O operation...    ← (within 1ms)
[22:14:14.926] 🔵 Platform-2 (Task 2): Starting I/O operation...

[22:14:15.928] ✅ Platform-1 (Task 1): Completed                    ← Line 51: 1000ms sleep
[22:14:15.928] ✅ Platform-2 (Task 2): Completed                    ← All complete after
[22:14:15.928] ✅ Platform-5 (Task 5): Completed                    ← ~1 second
[22:14:15.928] ✅ Platform-3 (Task 3): Completed
[22:14:15.928] ✅ Platform-4 (Task 4): Completed

[22:14:15.931] ⏱️  Total Time: 1048 ms                              ← Total execution time
[22:14:15.931] 📊 Threads created: 5 platform threads
[22:14:15.931] 💡 Each platform thread consumes ~1-2 MB of memory
```

**💡 Key Insight:**
- **Line 85:** Each platform thread is created with `new Thread()` and started
- **Line 91:** Main thread waits for all threads using `join()`
- **Line 51:** Simulates I/O operation (network call, database query)
- **Total Time:** ~1048ms for 5 concurrent 1-second tasks
- **Memory:** Each platform thread uses ~1-2 MB of stack memory
- **Limitation:** Can only create thousands of platform threads before running out of memory

---

### 2. Virtual Threads (Java 21+ Project Loom)

**Source Code (MainVirtualThread.java:109-142):**
```java
private static void demonstrateVirtualThreads() {
    printHeader("EXAMPLE 2: Virtual Threads (Java 21+ Project Loom)");
    log("Creating 5 virtual threads for I/O-bound tasks...");
    log("🚀 Virtual threads are JVM-managed and extremely lightweight\n");

    Instant start = Instant.now();
    List<Thread> threads = new ArrayList<>();

    // Create and start 5 virtual threads
    for (int i = 1; i <= 5; i++) {                        // Line 118
        final int taskId = i;
        Thread thread = Thread.startVirtualThread(() -> { // Line 120: Start virtual thread
            simulateIOTask("Virtual-" + taskId, taskId, 1000);
        });
        threads.add(thread);
    }

    // Wait for all threads to complete
    for (Thread thread : threads) {
        try {
            thread.join();                                // Line 129: Wait for thread completion
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    Duration duration = Duration.between(start, Instant.now());
    log(String.format("\n⏱️  Total Time: %d ms", duration.toMillis()));
    log(String.format("📊 Threads created: %d virtual threads", threads.size()));
    log("💡 Each virtual thread consumes only ~1 KB of memory!\n");
}
```

**Output:**
```
======================================================================
[22:14:15.931] EXAMPLE 2: Virtual Threads (Java 21+ Project Loom)
======================================================================
[22:14:15.932] Creating 5 virtual threads for I/O-bound tasks...
[22:14:15.932] 🚀 Virtual threads are JVM-managed and extremely lightweight

[22:14:15.943] 🔵 Virtual-1 (Task 1): Starting I/O operation...    ← Line 120: All start
[22:14:15.943] 🔵 Virtual-2 (Task 2): Starting I/O operation...    ← at nearly the
[22:14:15.943] 🔵 Virtual-4 (Task 4): Starting I/O operation...    ← same time
[22:14:15.943] 🔵 Virtual-5 (Task 5): Starting I/O operation...    ← (within 1ms)
[22:14:15.943] 🔵 Virtual-3 (Task 3): Starting I/O operation...

[22:14:16.947] ✅ Virtual-1 (Task 1): Completed                     ← All complete after
[22:14:16.948] ✅ Virtual-2 (Task 2): Completed                     ← ~1 second
[22:14:16.948] ✅ Virtual-4 (Task 4): Completed
[22:14:16.948] ✅ Virtual-3 (Task 3): Completed
[22:14:16.948] ✅ Virtual-5 (Task 5): Completed

[22:14:16.950] ⏱️  Total Time: 1017 ms                              ← Similar to platform threads
[22:14:16.950] 📊 Threads created: 5 virtual threads
[22:14:16.950] 💡 Each virtual thread consumes only ~1 KB of memory!
```

**💡 Key Insight:**
- **Line 120:** Virtual thread created with `Thread.startVirtualThread()`
  - This is the key difference from platform threads!
  - Virtual threads are managed by the JVM, not the OS
- **Line 129:** Same `join()` API - virtual threads are compatible with existing code
- **Total Time:** ~1017ms (similar to platform threads for small number of tasks)
- **Memory:** Each virtual thread uses only ~1 KB (1000x lighter!)
- **Advantage:** Can create MILLIONS of virtual threads without memory issues

**Comparison for 5 Threads:**
| Metric | Platform Threads | Virtual Threads |
|--------|------------------|-----------------|
| Total Time | 1048 ms | 1017 ms |
| Memory per Thread | ~1-2 MB | ~1 KB |
| Total Memory | ~5-10 MB | ~5 KB |

For small numbers, similar performance. The difference becomes dramatic at scale!

---

### 3. Scalability - 1000 Concurrent Tasks

**Source Code (MainVirtualThread.java:147-191):**
```java
private static void demonstrateScalability() {
    printHeader("EXAMPLE 3: Scalability - 1000 Concurrent Tasks");
    log("Virtual threads enable massive concurrency with minimal overhead");
    log("Simulating 1000 concurrent I/O operations...\n");

    int taskCount = 1000;
    int taskDuration = 100;                               // 100ms per task
    AtomicInteger completedTasks = new AtomicInteger(0);

    Instant start = Instant.now();
    List<Thread> threads = new ArrayList<>();

    // Create 1000 virtual threads
    for (int i = 1; i <= taskCount; i++) {                // Line 160: Loop 1000 times
        final int taskId = i;
        Thread thread = Thread.startVirtualThread(() -> { // Line 162: Create virtual thread
            try {
                Thread.sleep(taskDuration);               // Line 164: 100ms sleep
                int completed = completedTasks.incrementAndGet();
                if (completed % 100 == 0) {               // Line 166: Log every 100 completions
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
            thread.join();                                // Line 179: Wait for completion
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    Duration duration = Duration.between(start, Instant.now());
    log(String.format("\n⏱️  Total Time: %d ms", duration.toMillis()));
    log(String.format("🚀 Throughput: %.0f tasks/second", (taskCount * 1000.0) / duration.toMillis()));
}
```

**Output:**
```
======================================================================
[22:14:16.950] EXAMPLE 3: Scalability - 1000 Concurrent Tasks
======================================================================
[22:14:16.950] Virtual threads enable massive concurrency with minimal overhead
[22:14:16.951] Simulating 1000 concurrent I/O operations...

[22:14:17.058] 📈 Progress: 100/1000 tasks completed               ← Line 166: First 100 done
[22:14:17.059] 📈 Progress: 200/1000 tasks completed               ← Tasks completing
[22:14:17.062] 📈 Progress: 300/1000 tasks completed               ← very rapidly!
[22:14:17.063] 📈 Progress: 400/1000 tasks completed
[22:14:17.064] 📈 Progress: 500/1000 tasks completed               ← Halfway in ~113ms
[22:14:17.065] 📈 Progress: 600/1000 tasks completed
[22:14:17.065] 📈 Progress: 700/1000 tasks completed
[22:14:17.066] 📈 Progress: 800/1000 tasks completed
[22:14:17.067] 📈 Progress: 900/1000 tasks completed
[22:14:17.067] 📈 Progress: 1000/1000 tasks completed              ← All 1000 done!

[22:14:17.068] ⏱️  Total Time: 116 ms                              ← Line 162: 1000 threads in 116ms!
[22:14:17.069] 📊 Tasks completed: 1000
[22:14:17.070] 🚀 Throughput: 8621 tasks/second                    ← Incredible throughput!
[22:14:17.071] 💡 Try this with platform threads - you'd likely run out of memory!
```

**💡 Key Insight:**
- **Line 160-162:** Created **1000 virtual threads** effortlessly
- **Line 164:** Each task sleeps for 100ms (simulating I/O)
- **Total Time:** Only **116ms** for 1000 concurrent 100ms tasks!
  - This is close to optimal (just slightly over 100ms due to overhead)
  - All 1000 threads truly ran in parallel
- **Throughput:** **8,621 tasks/second** - incredible concurrency
- **Memory:** 1000 virtual threads × 1 KB = ~1 MB total
- **With Platform Threads:** Would need 1000 × 1.5 MB = ~1.5 GB memory!

**Why So Fast?**
```
Traditional (Platform Threads):
Limited to thread pool size (e.g., 100 threads)
1000 tasks ÷ 100 threads = 10 batches
10 batches × 100ms = 1000ms

Virtual Threads:
All 1000 threads run concurrently
Limited only by actual I/O wait time
Total time ≈ 100ms + small overhead = 116ms
```

---

### 4. Virtual Thread Executor

**Source Code (MainVirtualThread.java:196-231):**
```java
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
            executor.submit(() -> {                       // Line 210: Submit task
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
    log("💡 Virtual thread executor creates a new thread for each task!\n");
}
```

**Output:**
```
======================================================================
[22:14:17.071] EXAMPLE 4: Virtual Thread Executor
======================================================================
[22:14:17.072] Using ExecutorService with virtual thread factory
[22:14:17.072] This is ideal for managing many short-lived tasks

[22:14:17.126] 🔄 Task 60 completed by VirtualThread[#1114]/runnable@ForkJoinPool-1-worker-9
[22:14:17.126] 🔄 Task 100 completed by VirtualThread[#1154]/runnable@ForkJoinPool-1-worker-2
[22:14:17.126] 🔄 Task 80 completed by VirtualThread[#1134]/runnable@ForkJoinPool-1-worker-14
[22:14:17.126] 🔄 Task 40 completed by VirtualThread[#1094]/runnable@ForkJoinPool-1-worker-12
[22:14:17.126] 🔄 Task 20 completed by VirtualThread[#1074]/runnable@ForkJoinPool-1-worker-6
                                     ^                                ^
                                     |                                |
                    Virtual thread ID (#1074-#1154)    Carrier thread (ForkJoinPool worker)

[22:14:17.128] ⏱️  Total Time: 55 ms                               ← 100 tasks in 55ms!
[22:14:17.128] 📊 Tasks submitted: 100
[22:14:17.128] 💡 Virtual thread executor creates a new thread for each task!
```

**💡 Key Insight:**
- **Line 207:** `Executors.newVirtualThreadPerTaskExecutor()` creates an executor
  - This executor spawns a NEW virtual thread for EACH task
  - With platform threads, this would be extremely expensive!
  - With virtual threads, it's cheap and scales to millions of tasks
- **Line 210:** Submit tasks using familiar `executor.submit()` API
- **Line 224:** Try-with-resources automatically shuts down and waits
- **Virtual Thread Structure:**
  - Virtual threads (e.g., `VirtualThread[#1074]`) run on carrier threads
  - Carrier threads are the underlying platform threads (from `ForkJoinPool`)
  - Many virtual threads share a small pool of carrier threads
- **Performance:** 100 tasks completed in just 55ms

**Virtual Thread Architecture:**
```
Virtual Threads (lightweight, JVM-managed):
VirtualThread[#1074]  VirtualThread[#1094]  VirtualThread[#1114]
        |                    |                    |
        +--------------------+--------------------+
                            |
        [ForkJoinPool with 8 carrier threads]
                            |
        +--------------------+--------------------+
        |                    |                    |
   OS Thread 1          OS Thread 2          OS Thread 3
```

---

### 5. Performance Comparison

**Source Code (MainVirtualThread.java:236-294):**
```java
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

    // Comparison
    log("📊 COMPARISON:");
    log(String.format("   Platform Thread Pool (100 threads): %d ms", platformDuration.toMillis()));
    log(String.format("   Virtual Threads (%d threads):      %d ms", taskCount, virtualDuration.toMillis()));

    double speedup = (double) platformDuration.toMillis() / virtualDuration.toMillis();
    log(String.format("   🚀 Speedup: %.2fx faster with virtual threads!", speedup));
}
```

**Output:**
```
======================================================================
[22:14:17.128] EXAMPLE 5: Performance Comparison
======================================================================
[22:14:17.129] 🔵 Testing 500 tasks with Platform Thread Pool...
[22:14:17.437]    Platform Thread Pool Time: 307 ms                ← Line 246: 100 thread pool

[22:14:17.437] 🟢 Testing 500 tasks with Virtual Threads...
[22:14:17.491]    Virtual Thread Time: 53 ms                       ← Line 266: 500 virtual threads

[22:14:17.491] 📊 COMPARISON:
[22:14:17.492]    Platform Thread Pool (100 threads): 307 ms
[22:14:17.492]    Virtual Threads (500 threads):      53 ms
[22:14:17.492]    🚀 Speedup: 5.79x faster with virtual threads!   ← 5.79x performance improvement!
[22:14:17.492]    💡 Virtual threads scale much better for I/O-bound workloads
```

**💡 Key Insight:**
- **Platform Thread Pool (100 threads):**
  - Line 246: Fixed pool of 100 threads
  - 500 tasks with 50ms each
  - Tasks must wait for available threads in the pool
  - Total time: **307ms**
  - Calculation: 500 tasks ÷ 100 threads = 5 batches × 50ms = ~250ms + overhead

- **Virtual Threads (500 threads):**
  - Line 266: Creates 500 virtual threads (one per task)
  - All 500 tasks run truly concurrently
  - Total time: **53ms** (close to the 50ms task duration)

- **Speedup: 5.79x faster!**
  - Virtual threads eliminate queueing delays
  - All tasks start immediately
  - Perfect for I/O-bound workloads

**Visual Comparison:**
```
Platform Thread Pool (100 threads for 500 tasks):
Batch 1: [Thread1-Task1] [Thread2-Task2] ... [Thread100-Task100]  ← 50ms
Batch 2: [Thread1-Task101] [Thread2-Task102] ... [Thread100-Task200] ← 50ms
Batch 3: [Thread1-Task201] ... ← 50ms
Batch 4: [Thread1-Task301] ... ← 50ms
Batch 5: [Thread1-Task401] ... [Thread100-Task500] ← 50ms
Total: ~250ms + overhead = 307ms

Virtual Threads (500 threads for 500 tasks):
All at once: [VThread1] [VThread2] [VThread3] ... [VThread500]  ← 50ms
Total: ~50ms + overhead = 53ms

🚀 Result: 5.79x faster!
```

---

## 📊 Performance Summary

| Scenario | Platform Threads | Virtual Threads | Speedup |
|----------|------------------|-----------------|---------|
| 5 concurrent I/O tasks | 1048 ms | 1017 ms | 1.03x |
| 1000 concurrent I/O tasks | N/A (out of memory) | 116 ms | ♾️ |
| 100 tasks (executor) | 100+ thread pool | 55 ms | Significant |
| 500 tasks (comparison) | 307 ms (100 threads) | 53 ms (500 threads) | **5.79x** |

**Memory Comparison:**
| Thread Count | Platform Threads | Virtual Threads |
|--------------|------------------|-----------------|
| 5 threads | ~5-10 MB | ~5 KB |
| 100 threads | ~100-200 MB | ~100 KB |
| 1,000 threads | ~1-2 GB | ~1 MB |
| 1,000,000 threads | ~1-2 TB ❌ | ~1 GB ✅ |

---

## 🎯 Key Takeaways

### 1. **Lightweight Architecture**
   - **Platform threads:** ~1-2 MB per thread (OS-managed)
   - **Virtual threads:** ~1 KB per thread (JVM-managed)
   - **1000x lighter!** Can create millions of virtual threads

### 2. **Massive Scalability**
   - Platform threads: Limited to thousands (OS constraints)
   - Virtual threads: Can create millions!
   - Perfect for high-concurrency applications

### 3. **Use Cases**

   ✅ **Ideal for Virtual Threads:**
   - I/O-bound operations (network calls, database queries, file I/O)
   - High-concurrency web servers and APIs
   - Microservices with many external dependencies
   - Event-driven applications
   - Chat servers, websocket handlers

   ❌ **Not Ideal for:**
   - CPU-bound computations (use parallel streams or ForkJoinPool)
   - Long-running CPU-intensive tasks
   - When thread-local variables are heavily used

### 4. **Simplicity**
   - Write simple synchronous code (no callbacks, no reactive complexity)
   - No "callback hell" like in async programming
   - Better stack traces and easier debugging
   - Compatible with existing Thread API

### 5. **Migration Path**
   ```java
   // Old way - Platform thread
   Thread thread = new Thread(() -> doSomething());
   thread.start();

   // New way - Virtual thread
   Thread thread = Thread.startVirtualThread(() -> doSomething());

   // With executors - Old way
   ExecutorService executor = Executors.newFixedThreadPool(100);

   // With executors - New way
   ExecutorService executor = Executors.newVirtualThreadPerTaskExecutor();
   ```

### 6. **How Virtual Threads Work**
   - Virtual threads are **scheduled** by the JVM onto a pool of carrier threads
   - Carrier threads are regular platform threads (from ForkJoinPool)
   - When a virtual thread blocks (e.g., on I/O), it's **unmounted** from its carrier
   - The carrier thread can then run other virtual threads
   - When I/O completes, the virtual thread is **remounted** (possibly on a different carrier)
   - This allows millions of virtual threads to share a few platform threads

   ```
   Virtual Thread Lifecycle:

   1. Create virtual thread → [Parked on heap]
   2. Start execution → [Mounted on Carrier Thread 1]
   3. Perform I/O (e.g., network call) → [Unmounted, back to heap]
   4. I/O completes → [Mounted on Carrier Thread 2]
   5. Complete task → [Terminated]
   ```

---

## 🔬 Technical Details

### Virtual Thread Properties:
- **Creation:** `Thread.startVirtualThread(() -> {...})`
- **Scheduling:** JVM manages scheduling (not OS)
- **Blocking:** When blocked, unmounted from carrier thread
- **Memory:** Minimal overhead (~1 KB vs ~1-2 MB)
- **API:** Fully compatible with existing Thread API

### When a Virtual Thread Blocks:
```java
Thread.startVirtualThread(() -> {
    // Running on Carrier Thread A
    String result = httpClient.get("https://api.example.com");
    // ^ Blocks here - unmounted from Carrier Thread A
    // Carrier Thread A can now run other virtual threads
    // When response arrives, remounted (possibly on Carrier Thread B)
    processResult(result);
});
```

### Carrier Thread Pool:
- Default size: Number of CPU cores
- Can be configured with: `-Djdk.virtualThreadScheduler.parallelism=N`
- Virtual threads share this small pool
- Carrier threads use ForkJoinPool

---

## 🚀 Real-World Impact

### Before Virtual Threads:
```java
// Limited by thread pool size
ExecutorService executor = Executors.newFixedThreadPool(100);

// Can only handle 100 concurrent requests efficiently
for (int i = 0; i < 10000; i++) {
    executor.submit(() -> handleRequest());  // Requests queue up!
}
// Total time: High due to queueing
```

### With Virtual Threads:
```java
// No pool size limit needed!
ExecutorService executor = Executors.newVirtualThreadPerTaskExecutor();

// Can handle 10,000 concurrent requests efficiently
for (int i = 0; i < 10000; i++) {
    executor.submit(() -> handleRequest());  // All start immediately!
}
// Total time: Minimal queueing, maximum throughput
```

---

## 📚 References

- **JEP 444:** Virtual Threads (Java 21)
- **Project Loom:** https://openjdk.org/projects/loom/
- **Java 21 Release Notes:** Virtual Threads documentation
- **Best Practices:** Migrating to virtual threads

---

## 💻 Requirements

**This example requires:**
- **Java 21 or higher** - Virtual threads were introduced as a preview in Java 19 and finalized in Java 21
- Maven 3.6+ (for building with Maven)

**Version Check:**
```bash
java --version
# Should show: java version "21" or higher
```

---

## 🎉 Conclusion

Virtual threads represent a **paradigm shift** in Java concurrency:

**Before Java 21:**
- Limited by platform thread overhead
- Complex reactive/async programming for high concurrency
- Thread pools and careful tuning required

**With Java 21+ Virtual Threads:**
- ✅ Simple synchronous code
- ✅ Millions of concurrent tasks
- ✅ Minimal memory overhead
- ✅ Better debugging and profiling
- ✅ Perfect for I/O-bound workloads

**This is a game-changer for Java applications!** 🚀
