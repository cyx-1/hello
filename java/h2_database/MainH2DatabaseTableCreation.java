import java.sql.*;

/**
 * Demonstrates H2 Database operations including:
 * - Creating an in-memory database
 * - Creating tables with various data types
 * - Inserting sample data
 * - Querying data
 * - Viewing table metadata
 */
public class MainH2DatabaseTableCreation {

    // H2 in-memory database connection URL
    private static final String DB_URL = "jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1";
    private static final String DB_USER = "sa";
    private static final String DB_PASSWORD = "";

    public static void main(String[] args) {
        System.out.println("=== H2 Database Table Creation Demo ===\n");

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            System.out.println("1. Connected to H2 database successfully");
            System.out.println("   Database URL: " + DB_URL);
            System.out.println("   Database Product: " + conn.getMetaData().getDatabaseProductName());
            System.out.println("   Database Version: " + conn.getMetaData().getDatabaseProductVersion() + "\n");

            // Create tables
            createEmployeesTable(conn);
            createDepartmentsTable(conn);

            // Insert sample data
            insertDepartments(conn);
            insertEmployees(conn);

            // Query and display data
            queryEmployees(conn);
            queryDepartments(conn);

            // Show table metadata
            showTableMetadata(conn, "EMPLOYEES");

            // Demonstrate JOIN query
            demonstrateJoinQuery(conn);

            System.out.println("\n=== Demo completed successfully ===");

        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * Creates the EMPLOYEES table with various column types
     */
    private static void createEmployeesTable(Connection conn) throws SQLException {
        String createTableSQL = """
            CREATE TABLE IF NOT EXISTS EMPLOYEES (
                employee_id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                email VARCHAR(100) UNIQUE,
                department_id INT,
                salary DECIMAL(10, 2),
                hire_date DATE,
                is_active BOOLEAN DEFAULT TRUE
            )
            """;

        try (Statement stmt = conn.createStatement()) {
            stmt.execute(createTableSQL);
            System.out.println("2. Created EMPLOYEES table");
            System.out.println("   - Columns: employee_id (PK, AUTO_INCREMENT), first_name, last_name,");
            System.out.println("     email (UNIQUE), department_id, salary, hire_date, is_active\n");
        }
    }

    /**
     * Creates the DEPARTMENTS table
     */
    private static void createDepartmentsTable(Connection conn) throws SQLException {
        String createTableSQL = """
            CREATE TABLE IF NOT EXISTS DEPARTMENTS (
                department_id INT PRIMARY KEY,
                department_name VARCHAR(100) NOT NULL,
                location VARCHAR(100)
            )
            """;

        try (Statement stmt = conn.createStatement()) {
            stmt.execute(createTableSQL);
            System.out.println("3. Created DEPARTMENTS table");
            System.out.println("   - Columns: department_id (PK), department_name, location\n");
        }
    }

    /**
     * Inserts sample department data
     */
    private static void insertDepartments(Connection conn) throws SQLException {
        String insertSQL = "INSERT INTO DEPARTMENTS (department_id, department_name, location) VALUES (?, ?, ?)";

        try (PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {
            // Engineering department
            pstmt.setInt(1, 1);
            pstmt.setString(2, "Engineering");
            pstmt.setString(3, "San Francisco");
            pstmt.executeUpdate();

            // Sales department
            pstmt.setInt(1, 2);
            pstmt.setString(2, "Sales");
            pstmt.setString(3, "New York");
            pstmt.executeUpdate();

            // HR department
            pstmt.setInt(1, 3);
            pstmt.setString(2, "Human Resources");
            pstmt.setString(3, "Chicago");
            pstmt.executeUpdate();

            System.out.println("4. Inserted 3 departments into DEPARTMENTS table\n");
        }
    }

    /**
     * Inserts sample employee data
     */
    private static void insertEmployees(Connection conn) throws SQLException {
        String insertSQL = """
            INSERT INTO EMPLOYEES (first_name, last_name, email, department_id, salary, hire_date, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """;

        try (PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {
            // Employee 1
            pstmt.setString(1, "John");
            pstmt.setString(2, "Doe");
            pstmt.setString(3, "john.doe@example.com");
            pstmt.setInt(4, 1);
            pstmt.setBigDecimal(5, new java.math.BigDecimal("95000.00"));
            pstmt.setDate(6, Date.valueOf("2022-01-15"));
            pstmt.setBoolean(7, true);
            pstmt.executeUpdate();

            // Employee 2
            pstmt.setString(1, "Jane");
            pstmt.setString(2, "Smith");
            pstmt.setString(3, "jane.smith@example.com");
            pstmt.setInt(4, 2);
            pstmt.setBigDecimal(5, new java.math.BigDecimal("87000.00"));
            pstmt.setDate(6, Date.valueOf("2021-06-20"));
            pstmt.setBoolean(7, true);
            pstmt.executeUpdate();

            // Employee 3
            pstmt.setString(1, "Bob");
            pstmt.setString(2, "Johnson");
            pstmt.setString(3, "bob.johnson@example.com");
            pstmt.setInt(4, 1);
            pstmt.setBigDecimal(5, new java.math.BigDecimal("102000.00"));
            pstmt.setDate(6, Date.valueOf("2020-03-10"));
            pstmt.setBoolean(7, true);
            pstmt.executeUpdate();

            // Employee 4
            pstmt.setString(1, "Alice");
            pstmt.setString(2, "Williams");
            pstmt.setString(3, "alice.williams@example.com");
            pstmt.setInt(4, 3);
            pstmt.setBigDecimal(5, new java.math.BigDecimal("78000.00"));
            pstmt.setDate(6, Date.valueOf("2023-02-01"));
            pstmt.setBoolean(7, true);
            pstmt.executeUpdate();

            System.out.println("5. Inserted 4 employees into EMPLOYEES table\n");
        }
    }

    /**
     * Queries and displays all employees
     */
    private static void queryEmployees(Connection conn) throws SQLException {
        String query = "SELECT * FROM EMPLOYEES ORDER BY employee_id";

        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            System.out.println("6. Querying EMPLOYEES table:");
            System.out.println("   " + "-".repeat(120));
            System.out.printf("   %-4s %-12s %-12s %-30s %-6s %-12s %-12s %-8s%n",
                    "ID", "First Name", "Last Name", "Email", "Dept", "Salary", "Hire Date", "Active");
            System.out.println("   " + "-".repeat(120));

            while (rs.next()) {
                System.out.printf("   %-4d %-12s %-12s %-30s %-6d $%-11.2f %-12s %-8s%n",
                        rs.getInt("employee_id"),
                        rs.getString("first_name"),
                        rs.getString("last_name"),
                        rs.getString("email"),
                        rs.getInt("department_id"),
                        rs.getBigDecimal("salary"),
                        rs.getDate("hire_date"),
                        rs.getBoolean("is_active"));
            }
            System.out.println("   " + "-".repeat(120) + "\n");
        }
    }

    /**
     * Queries and displays all departments
     */
    private static void queryDepartments(Connection conn) throws SQLException {
        String query = "SELECT * FROM DEPARTMENTS ORDER BY department_id";

        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            System.out.println("7. Querying DEPARTMENTS table:");
            System.out.println("   " + "-".repeat(70));
            System.out.printf("   %-6s %-30s %-20s%n", "ID", "Department Name", "Location");
            System.out.println("   " + "-".repeat(70));

            while (rs.next()) {
                System.out.printf("   %-6d %-30s %-20s%n",
                        rs.getInt("department_id"),
                        rs.getString("department_name"),
                        rs.getString("location"));
            }
            System.out.println("   " + "-".repeat(70) + "\n");
        }
    }

    /**
     * Displays metadata information about a table
     */
    private static void showTableMetadata(Connection conn, String tableName) throws SQLException {
        DatabaseMetaData metaData = conn.getMetaData();

        System.out.println("8. Table Metadata for " + tableName + ":");

        try (ResultSet columns = metaData.getColumns(null, null, tableName, null)) {
            System.out.println("   " + "-".repeat(100));
            System.out.printf("   %-20s %-15s %-10s %-10s %-15s%n",
                    "Column Name", "Data Type", "Size", "Nullable", "Auto Increment");
            System.out.println("   " + "-".repeat(100));

            while (columns.next()) {
                String columnName = columns.getString("COLUMN_NAME");
                String dataType = columns.getString("TYPE_NAME");
                int columnSize = columns.getInt("COLUMN_SIZE");
                String isNullable = columns.getString("IS_NULLABLE");
                String isAutoIncrement = columns.getString("IS_AUTOINCREMENT");

                System.out.printf("   %-20s %-15s %-10d %-10s %-15s%n",
                        columnName, dataType, columnSize, isNullable, isAutoIncrement);
            }
            System.out.println("   " + "-".repeat(100) + "\n");
        }
    }

    /**
     * Demonstrates a JOIN query between EMPLOYEES and DEPARTMENTS
     */
    private static void demonstrateJoinQuery(Connection conn) throws SQLException {
        String joinQuery = """
            SELECT e.employee_id, e.first_name, e.last_name, e.salary,
                   d.department_name, d.location
            FROM EMPLOYEES e
            JOIN DEPARTMENTS d ON e.department_id = d.department_id
            ORDER BY e.salary DESC
            """;

        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(joinQuery)) {

            System.out.println("9. JOIN Query (Employees with Department Information):");
            System.out.println("   " + "-".repeat(110));
            System.out.printf("   %-4s %-12s %-12s %-12s %-30s %-20s%n",
                    "ID", "First Name", "Last Name", "Salary", "Department", "Location");
            System.out.println("   " + "-".repeat(110));

            while (rs.next()) {
                System.out.printf("   %-4d %-12s %-12s $%-11.2f %-30s %-20s%n",
                        rs.getInt("employee_id"),
                        rs.getString("first_name"),
                        rs.getString("last_name"),
                        rs.getBigDecimal("salary"),
                        rs.getString("department_name"),
                        rs.getString("location"));
            }
            System.out.println("   " + "-".repeat(110));
        }
    }
}
