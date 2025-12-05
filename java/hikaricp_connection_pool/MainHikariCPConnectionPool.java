import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import com.zaxxer.hikari.HikariPoolMXBean;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * Demonstrates HikariCP connection pool features including:
 * - Connection pool configuration and initialization
 * - Connection leak detection mechanism
 * - Proper connection handling with try-with-resources
 * - Connection leak demonstration
 * - Pool statistics and monitoring
 * - Pool health checks
 */
public class MainHikariCPConnectionPool {

    public static void main(String[] args) {
        System.out.println("=== HikariCP Connection Pool Demo ===\n");

        // Demo 1: Basic pool configuration
        demonstrateBasicConfiguration();

        // Demo 2: Proper connection usage (no leaks)
        demonstrateProperConnectionUsage();

        // Demo 3: Connection leak detection
        demonstrateConnectionLeakDetection();

        // Demo 4: Pool statistics and monitoring
        demonstratePoolMonitoring();

        System.out.println("\n=== Demo completed successfully ===");
    }

    /**
     * Demonstrates basic HikariCP configuration with key properties
     */
    private static void demonstrateBasicConfiguration() {
        System.out.println("1. Basic HikariCP Configuration");
        System.out.println("   --------------------------------");

        HikariConfig config = new HikariConfig();

        // Database connection settings
        config.setJdbcUrl("jdbc:h2:mem:hikaridb;DB_CLOSE_DELAY=-1");
        config.setUsername("sa");
        config.setPassword("");

        // Pool size configuration
        config.setMaximumPoolSize(10);  // Maximum number of connections in the pool
        config.setMinimumIdle(2);       // Minimum idle connections maintained

        // Connection timeout settings
        config.setConnectionTimeout(30000);      // 30 seconds to get a connection
        config.setIdleTimeout(600000);           // 10 minutes before idle connection is removed
        config.setMaxLifetime(1800000);          // 30 minutes max lifetime for a connection

        // Leak detection - key protection mechanism!
        config.setLeakDetectionThreshold(5000);  // Warn if connection held > 5 seconds

        // Pool name for logging
        config.setPoolName("HikariPool-Demo");

        // Auto-commit behavior
        config.setAutoCommit(true);

        System.out.println("   Configuration created with:");
        System.out.println("   - Maximum pool size: " + config.getMaximumPoolSize());
        System.out.println("   - Minimum idle connections: " + config.getMinimumIdle());
        System.out.println("   - Connection timeout: " + config.getConnectionTimeout() + "ms");
        System.out.println("   - Leak detection threshold: " + config.getLeakDetectionThreshold() + "ms");
        System.out.println("   - Pool name: " + config.getPoolName());
        System.out.println();

        // Create the data source (this initializes the pool)
        try (HikariDataSource dataSource = new HikariDataSource(config)) {
            System.out.println("   Pool initialized successfully!");
            System.out.println("   Pool is ready to serve connections.\n");
        }
    }

    /**
     * Demonstrates proper connection usage with try-with-resources
     * This prevents connection leaks by ensuring connections are always closed
     */
    private static void demonstrateProperConnectionUsage() {
        System.out.println("2. Proper Connection Usage (No Leaks)");
        System.out.println("   ------------------------------------");

        HikariConfig config = createConfig(10000); // 10 second leak threshold

        try (HikariDataSource dataSource = new HikariDataSource(config)) {

            // Create a test table
            initializeDatabase(dataSource);

            System.out.println("   Initial pool stats:");
            printPoolStats(dataSource);

            // Proper usage with try-with-resources
            System.out.println("\n   Acquiring connection with try-with-resources...");
            try (Connection conn = dataSource.getConnection()) {
                System.out.println("   ✓ Connection acquired: " + conn);

                // Execute a query
                try (Statement stmt = conn.createStatement();
                     ResultSet rs = stmt.executeQuery("SELECT COUNT(*) as count FROM USERS")) {
                    if (rs.next()) {
                        System.out.println("   ✓ Query executed: User count = " + rs.getInt("count"));
                    }
                }

                System.out.println("   ✓ Connection will be automatically returned to pool");
            } // Connection is automatically closed here

            System.out.println("\n   Pool stats after proper connection close:");
            printPoolStats(dataSource);
            System.out.println("   ✓ No connection leak - connection returned to pool!\n");

        } catch (Exception e) {
            System.err.println("   Error: " + e.getMessage());
        }
    }

    /**
     * Demonstrates HikariCP's connection leak detection mechanism
     * When a connection is held longer than leakDetectionThreshold, a warning is logged
     */
    private static void demonstrateConnectionLeakDetection() {
        System.out.println("3. Connection Leak Detection Mechanism");
        System.out.println("   -------------------------------------");

        // Configure with a very short leak detection threshold (2 seconds) for demo
        HikariConfig config = createConfig(2000);

        try (HikariDataSource dataSource = new HikariDataSource(config)) {

            initializeDatabase(dataSource);

            System.out.println("   Leak detection threshold set to: 2000ms");
            System.out.println("   This simulates a connection leak scenario...\n");

            // Simulate a connection leak by NOT using try-with-resources
            System.out.println("   Acquiring connection WITHOUT proper closure...");
            Connection leakedConnection = dataSource.getConnection();
            System.out.println("   ✓ Connection acquired: " + leakedConnection);

            System.out.println("\n   Holding connection for 3 seconds (exceeds threshold)...");
            System.out.println("   Watch for HikariCP's leak detection warning below:");
            System.out.println("   " + "-".repeat(80));

            // Hold the connection for 3 seconds to trigger leak detection
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }

            System.out.println("   " + "-".repeat(80));
            System.out.println("\n   ⚠ HikariCP detected a potential connection leak!");
            System.out.println("   The warning message above shows:");
            System.out.println("   - Which connection was leaked");
            System.out.println("   - How long it has been held");
            System.out.println("   - Stack trace showing where it was acquired");

            // Clean up the leaked connection
            leakedConnection.close();
            System.out.println("\n   ✓ Connection manually closed (cleanup performed)");

            System.out.println("\n   Protection Mechanism Benefits:");
            System.out.println("   - Early detection of connection leaks in development");
            System.out.println("   - Stack trace helps identify the leak source");
            System.out.println("   - Prevents pool exhaustion in production");
            System.out.println("   - No performance impact until threshold is exceeded\n");

        } catch (Exception e) {
            System.err.println("   Error: " + e.getMessage());
        }
    }

    /**
     * Demonstrates pool monitoring and statistics
     */
    private static void demonstratePoolMonitoring() {
        System.out.println("4. Pool Monitoring and Statistics");
        System.out.println("   --------------------------------");

        HikariConfig config = createConfig(10000);
        config.setMaximumPoolSize(5);
        config.setMinimumIdle(2);

        try (HikariDataSource dataSource = new HikariDataSource(config)) {

            initializeDatabase(dataSource);

            System.out.println("   Pool configuration:");
            System.out.println("   - Maximum pool size: 5");
            System.out.println("   - Minimum idle: 2\n");

            System.out.println("   Initial state:");
            printDetailedPoolStats(dataSource);

            // Acquire multiple connections
            System.out.println("\n   Acquiring 3 connections...");
            Connection conn1 = dataSource.getConnection();
            Connection conn2 = dataSource.getConnection();
            Connection conn3 = dataSource.getConnection();

            System.out.println("   ✓ 3 connections acquired\n");
            System.out.println("   Pool state with active connections:");
            printDetailedPoolStats(dataSource);

            // Release connections
            System.out.println("\n   Releasing all connections...");
            conn1.close();
            conn2.close();
            conn3.close();

            System.out.println("   ✓ Connections returned to pool\n");
            System.out.println("   Final pool state:");
            printDetailedPoolStats(dataSource);

            System.out.println("\n   Monitoring Benefits:");
            System.out.println("   - Real-time visibility into pool health");
            System.out.println("   - JMX integration for production monitoring");
            System.out.println("   - Helps optimize pool sizing");
            System.out.println("   - Detects performance bottlenecks\n");

        } catch (Exception e) {
            System.err.println("   Error: " + e.getMessage());
        }
    }

    // ============ Helper Methods ============

    /**
     * Creates a HikariConfig with the specified leak detection threshold
     */
    private static HikariConfig createConfig(long leakDetectionThreshold) {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:h2:mem:hikaridb;DB_CLOSE_DELAY=-1");
        config.setUsername("sa");
        config.setPassword("");
        config.setMaximumPoolSize(5);
        config.setMinimumIdle(2);
        config.setLeakDetectionThreshold(leakDetectionThreshold);
        config.setPoolName("HikariPool-" + System.currentTimeMillis());
        return config;
    }

    /**
     * Initializes the database with a sample table
     */
    private static void initializeDatabase(HikariDataSource dataSource) throws SQLException {
        try (Connection conn = dataSource.getConnection();
             Statement stmt = conn.createStatement()) {

            // Create table if not exists
            stmt.execute("CREATE TABLE IF NOT EXISTS USERS (id INT PRIMARY KEY, name VARCHAR(100))");

            // Insert sample data
            stmt.execute("DELETE FROM USERS"); // Clear existing data
            stmt.execute("INSERT INTO USERS VALUES (1, 'Alice')");
            stmt.execute("INSERT INTO USERS VALUES (2, 'Bob')");
            stmt.execute("INSERT INTO USERS VALUES (3, 'Charlie')");
        }
    }

    /**
     * Prints basic pool statistics
     */
    private static void printPoolStats(HikariDataSource dataSource) {
        HikariPoolMXBean poolMXBean = dataSource.getHikariPoolMXBean();
        System.out.println("   - Active connections: " + poolMXBean.getActiveConnections());
        System.out.println("   - Idle connections: " + poolMXBean.getIdleConnections());
        System.out.println("   - Total connections: " + poolMXBean.getTotalConnections());
        System.out.println("   - Threads awaiting connection: " + poolMXBean.getThreadsAwaitingConnection());
    }

    /**
     * Prints detailed pool statistics
     */
    private static void printDetailedPoolStats(HikariDataSource dataSource) {
        HikariPoolMXBean poolMXBean = dataSource.getHikariPoolMXBean();
        System.out.println("   ┌─────────────────────────────────────────┐");
        System.out.println("   │ Pool Statistics                         │");
        System.out.println("   ├─────────────────────────────────────────┤");
        System.out.printf("   │ Active connections:          %-10d │%n", poolMXBean.getActiveConnections());
        System.out.printf("   │ Idle connections:            %-10d │%n", poolMXBean.getIdleConnections());
        System.out.printf("   │ Total connections:           %-10d │%n", poolMXBean.getTotalConnections());
        System.out.printf("   │ Threads awaiting:            %-10d │%n", poolMXBean.getThreadsAwaitingConnection());
        System.out.println("   └─────────────────────────────────────────┘");
    }
}
