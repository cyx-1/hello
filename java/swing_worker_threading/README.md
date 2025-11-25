# Java Swing and SwingWorker Threading Example

This example demonstrates the proper threading model in Java Swing applications using **SwingWorker** to execute time-consuming operations on background threads while keeping UI updates on the Event Dispatch Thread (EDT).

## Key Concepts

### The Problem
In Swing, all UI components and operations must be performed on the **Event Dispatch Thread (EDT)**. If you perform time-consuming operations on the EDT, the UI will freeze and become unresponsive.

### The Solution: SwingWorker
`SwingWorker` provides a framework for:
- Running time-consuming tasks on **background worker threads**
- Publishing intermediate results from background threads
- Processing results and updating UI on the **EDT**
- Handling task completion and cancellation

## Important Source Code

### Lines 95-176: SwingWorker Implementation

```java
95:     /**
96:      * SwingWorker<T, V> where:
97:      * - T (Integer) = type returned by doInBackground() and get()
98:      * - V (String) = type used for intermediate results (publish/process)
99:      */
100:    private class DataProcessingWorker extends SwingWorker<Integer, String> {
101:
102:        // This runs on a BACKGROUND THREAD (not EDT)
103:        @Override
104:        protected Integer doInBackground() throws Exception {
105:            publish("doInBackground() running on: " + Thread.currentThread().getName());
106:            publish("This is a BACKGROUND thread - safe for time-consuming work");
107:
108:            int totalItems = 10;
109:            int processedCount = 0;
110:
111:            // Simulate time-consuming data processing
112:            for (int i = 1; i <= totalItems; i++) {
113:                // Check if task was cancelled
114:                if (isCancelled()) {
115:                    publish("Task cancelled at item " + i);
116:                    break;
117:                }
118:
119:                // Simulate heavy computation
120:                Thread.sleep(500);  // Simulates time-consuming work
121:                processedCount++;
122:
123:                // Calculate progress
124:                int progress = (i * 100) / totalItems;
125:                setProgress(progress);  // Updates progress property
126:
127:                // Publish intermediate results to be processed on EDT
128:                publish("Processed item " + i + "/" + totalItems +
129:                       " (Progress: " + progress + "%)");
130:            }
131:
132:            // Return final result
133:            return processedCount;
134:        }
135:
136:        // This runs on EDT - receives data published from background thread
137:        @Override
138:        protected void process(List<String> chunks) {
139:            // Process all published chunks
140:            for (String message : chunks) {
141:                log(message);
142:            }
143:        }
144:
145:        // This runs on EDT when doInBackground() completes
146:        @Override
147:        protected void done() {
148:            log("\ndone() running on: " + Thread.currentThread().getName());
149:            log("This is the EDT - safe for UI updates");
150:
151:            try {
152:                if (isCancelled()) {
153:                    // Handle cancellation
154:                    log("Task was CANCELLED");
155:                    progressBar.setValue(0);
156:                } else {
157:                    // Get the result from doInBackground()
158:                    Integer result = get();
159:                    log("Task COMPLETED successfully");
160:                    log("Total items processed: " + result);
161:                    progressBar.setValue(100);
162:                }
163:            } catch (InterruptedException | ExecutionException e) {
164:                // Handle errors
165:                log("Error occurred: " + e.getMessage());
166:                e.printStackTrace();
167:            } finally {
168:                // Re-enable buttons
169:                startButton.setEnabled(true);
170:                cancelButton.setEnabled(false);
171:            }
172:        }
173:    }
```

**Annotations:**
- **Line 100**: `DataProcessingWorker extends SwingWorker<Integer, String>`
  - First type parameter (`Integer`): Return type from `doInBackground()`
  - Second type parameter (`String`): Type for intermediate results via `publish()`
- **Line 104**: `doInBackground()` - Runs on **background worker thread**, NOT the EDT
  - This is where time-consuming work should be performed
  - Line 120: `Thread.sleep(500)` simulates heavy computation without freezing UI
- **Line 128**: `publish()` - Sends intermediate results to be processed on EDT
  - Can be called multiple times from background thread
  - Results are batched and delivered to `process()` method
- **Line 138**: `process()` - Runs on **EDT**, receives published data
  - Safe to update UI components here (Line 141: updating text area)
  - Called with batched chunks for efficiency
- **Line 147**: `done()` - Runs on **EDT** when background task completes
  - Line 158: `get()` retrieves the final result from `doInBackground()`
  - Lines 155, 161, 169-170: Safe to update UI components (progress bar, buttons)

### Lines 184-192: Launching Swing on EDT

```java
184:        // CRITICAL: Launch Swing UI on EDT using invokeLater
185:        SwingUtilities.invokeLater(new Runnable() {
186:            @Override
187:            public void run() {
188:                System.out.println("Creating JFrame on: " + Thread.currentThread().getName());
189:                MainSwingWorkerThreading frame = new MainSwingWorkerThreading();
190:                frame.setVisible(true);
191:            }
192:        });
```

**Annotations:**
- **Line 185**: `SwingUtilities.invokeLater()` - Ensures GUI creation happens on EDT
  - The main thread schedules GUI creation on EDT, then exits
  - EDT takes over and handles all UI events

## Program Output

### Initial Console Output
```
Main method running on: main
Creating GUI...

Creating JFrame on: AWT-EventQueue-0
```

**Output Annotations:**
- Line 1: Shows main method executes on the `main` thread
- Line 3: Shows JFrame creation executes on `AWT-EventQueue-0` (the EDT)

### Expected UI Output (When Start Button Clicked)

```
=== Starting New Processing Task ===
Start button clicked on: AWT-EventQueue-0
doInBackground() running on: SwingWorker-pool-1-thread-1
This is a BACKGROUND thread - safe for time-consuming work
Processed item 1/10 (Progress: 10%)
Processed item 2/10 (Progress: 20%)
Processed item 3/10 (Progress: 30%)
Processed item 4/10 (Progress: 40%)
Processed item 5/10 (Progress: 50%)
Processed item 6/10 (Progress: 60%)
Processed item 7/10 (Progress: 70%)
Processed item 8/10 (Progress: 80%)
Processed item 9/10 (Progress: 90%)
Processed item 10/10 (Progress: 100%)

done() running on: AWT-EventQueue-0
This is the EDT - safe for UI updates
Task COMPLETED successfully
Total items processed: 10
```

**Output Annotations:**
- Line 2: Button click handled on `AWT-EventQueue-0` (EDT)
- Line 3: Background work executes on `SwingWorker-pool-1-thread-1` (background thread)
- Lines 5-14: Intermediate results published from background thread, displayed on EDT
- Line 16: Completion handler runs on `AWT-EventQueue-0` (EDT)

## Threading Model Summary

| Method | Thread | Purpose |
|--------|--------|---------|
| `main()` | main | Application entry point |
| `SwingUtilities.invokeLater()` | main → EDT | Schedule GUI creation on EDT |
| UI Component Creation | AWT-EventQueue-0 (EDT) | Create and initialize UI |
| Button Click Handlers | AWT-EventQueue-0 (EDT) | Handle user interactions |
| `doInBackground()` | SwingWorker-pool-X-thread-Y | Execute time-consuming work |
| `publish()` | SwingWorker thread | Send intermediate results |
| `process()` | AWT-EventQueue-0 (EDT) | Receive results, update UI |
| `done()` | AWT-EventQueue-0 (EDT) | Handle completion, update UI |

## How to Run

### Using Maven
```bash
cd java/swing_worker_threading
mvn compile exec:java
```

### Using javac and java
```bash
cd java/swing_worker_threading
javac MainSwingWorkerThreading.java
java MainSwingWorkerThreading
```

## Requirements

- **Java Version**: Java 11 or higher
- **No External Libraries**: Uses only standard JDK (javax.swing package)

## Key Takeaways

1. **Never block the EDT**: Time-consuming operations must run on background threads
2. **Use SwingWorker for background tasks**: It handles the thread coordination for you
3. **doInBackground() runs on background thread**: Safe for long-running operations
4. **process() and done() run on EDT**: Safe for UI updates
5. **Use publish() for intermediate updates**: Allows UI to show progress during long operations
6. **Always use SwingUtilities.invokeLater()**: To launch the initial GUI on the EDT

## Visual Flow

```
[Main Thread]
    |
    +--> SwingUtilities.invokeLater() ──┐
                                        |
                                        v
                              [Event Dispatch Thread]
                                        |
                                        +--> Create GUI
                                        |
                                        +--> Handle Button Click
                                        |
                                        +--> Execute SwingWorker ──┐
                                        |                          |
                                        |                          v
                                        |              [Background Worker Thread]
                                        |                          |
                                        |                          +--> doInBackground()
                                        |                          |
                                        |                          +--> publish() ──┐
                                        |                                           |
                                        +<-- process() <--------------------------┘
                                        |
                                        +<-- done() <-- [Background Thread Completes]
                                        |
                                        +--> Update UI Components
```

This threading model ensures a responsive UI while performing complex background operations.
