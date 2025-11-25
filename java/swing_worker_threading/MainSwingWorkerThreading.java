import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;
import java.util.concurrent.ExecutionException;

/**
 * Demonstrates Java Swing and SwingWorker for proper threading:
 * - Time-consuming operations run on background worker threads
 * - UI updates happen on the Event Dispatch Thread (EDT)
 */
public class MainSwingWorkerThreading extends JFrame {
    private JTextArea outputArea;
    private JProgressBar progressBar;
    private JButton startButton;
    private JButton cancelButton;
    private DataProcessingWorker currentWorker;

    public MainSwingWorkerThreading() {
        // Line 20: Initialize UI on EDT
        setTitle("SwingWorker Threading Demo");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));

        // Line 26: Create UI components
        outputArea = new JTextArea();
        outputArea.setEditable(false);
        outputArea.setFont(new Font("Monospaced", Font.PLAIN, 12));
        JScrollPane scrollPane = new JScrollPane(outputArea);

        // Line 32: Progress bar to show background work progress
        progressBar = new JProgressBar(0, 100);
        progressBar.setStringPainted(true);

        // Line 36: Control buttons
        JPanel buttonPanel = new JPanel();
        startButton = new JButton("Start Processing");
        cancelButton = new JButton("Cancel");
        cancelButton.setEnabled(false);

        // Line 42: Start button action - launches SwingWorker
        startButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                startProcessing();
            }
        });

        // Line 50: Cancel button action - cancels background work
        cancelButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (currentWorker != null) {
                    currentWorker.cancel(true);
                }
            }
        });

        buttonPanel.add(startButton);
        buttonPanel.add(cancelButton);

        // Line 63: Layout components
        add(scrollPane, BorderLayout.CENTER);
        add(progressBar, BorderLayout.NORTH);
        add(buttonPanel, BorderLayout.SOUTH);

        // Line 68: Display initial thread info
        log("Application started on: " + Thread.currentThread().getName());
    }

    // Line 72: Helper method to append text to output area (must be called on EDT)
    private void log(String message) {
        outputArea.append(message + "\n");
        outputArea.setCaretPosition(outputArea.getDocument().getLength());
    }

    // Line 78: Starts the background processing
    private void startProcessing() {
        log("\n=== Starting New Processing Task ===");
        log("Start button clicked on: " + Thread.currentThread().getName());

        // Line 83: Disable start button, enable cancel button
        startButton.setEnabled(false);
        cancelButton.setEnabled(true);
        progressBar.setValue(0);
        outputArea.setText("");

        // Line 89: Create and execute SwingWorker
        currentWorker = new DataProcessingWorker();
        currentWorker.execute();  // This schedules doInBackground() on worker thread
    }

    /**
     * Line 95: SwingWorker<T, V> where:
     * - T (Integer) = type returned by doInBackground() and get()
     * - V (String) = type used for intermediate results (publish/process)
     */
    private class DataProcessingWorker extends SwingWorker<Integer, String> {

        // Line 102: This runs on a BACKGROUND THREAD (not EDT)
        @Override
        protected Integer doInBackground() throws Exception {
            publish("doInBackground() running on: " + Thread.currentThread().getName());
            publish("This is a BACKGROUND thread - safe for time-consuming work");

            int totalItems = 10;
            int processedCount = 0;

            // Line 111: Simulate time-consuming data processing
            for (int i = 1; i <= totalItems; i++) {
                // Line 113: Check if task was cancelled
                if (isCancelled()) {
                    publish("Task cancelled at item " + i);
                    break;
                }

                // Line 119: Simulate heavy computation
                Thread.sleep(500);  // Simulates time-consuming work
                processedCount++;

                // Line 123: Calculate progress
                int progress = (i * 100) / totalItems;
                setProgress(progress);  // Updates progress property

                // Line 127: Publish intermediate results to be processed on EDT
                publish("Processed item " + i + "/" + totalItems +
                       " (Progress: " + progress + "%)");
            }

            // Line 132: Return final result
            return processedCount;
        }

        // Line 136: This runs on EDT - receives data published from background thread
        @Override
        protected void process(List<String> chunks) {
            // Line 139: Process all published chunks
            for (String message : chunks) {
                log(message);
            }
        }

        // Line 145: This runs on EDT when doInBackground() completes
        @Override
        protected void done() {
            log("\ndone() running on: " + Thread.currentThread().getName());
            log("This is the EDT - safe for UI updates");

            try {
                if (isCancelled()) {
                    // Line 153: Handle cancellation
                    log("Task was CANCELLED");
                    progressBar.setValue(0);
                } else {
                    // Line 157: Get the result from doInBackground()
                    Integer result = get();
                    log("Task COMPLETED successfully");
                    log("Total items processed: " + result);
                    progressBar.setValue(100);
                }
            } catch (InterruptedException | ExecutionException e) {
                // Line 165: Handle errors
                log("Error occurred: " + e.getMessage());
                e.printStackTrace();
            } finally {
                // Line 169: Re-enable buttons
                startButton.setEnabled(true);
                cancelButton.setEnabled(false);
            }
        }

        // Line 175: PropertyChangeListener can monitor progress updates
        // This is called automatically when setProgress() is called
    }

    // Line 179: Main method to launch application
    public static void main(String[] args) {
        System.out.println("Main method running on: " + Thread.currentThread().getName());
        System.out.println("Creating GUI...\n");

        // Line 184: CRITICAL: Launch Swing UI on EDT using invokeLater
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                System.out.println("Creating JFrame on: " + Thread.currentThread().getName());
                MainSwingWorkerThreading frame = new MainSwingWorkerThreading();
                frame.setVisible(true);
            }
        });
    }
}
