# H2 Database Table Creation Demo

This example demonstrates the use of H2, a lightweight in-memory Java database, with comprehensive table creation and manipulation operations.

## Version Requirements

- **Java**: 17 or higher
- **H2 Database**: 2.2.224 (included via Maven dependency)

## Overview

This demonstration showcases:
- Creating an in-memory H2 database connection
- Creating tables with various data types and constraints
- Inserting sample data using PreparedStatements
- Querying data with SELECT statements
- Retrieving table metadata
- Performing JOIN operations

## How to Run

### Using Maven:
```bash
mvn clean compile exec:java
```

### Manual Compilation:
```bash
# Download H2 jar
curl -L -o h2.jar https://repo1.maven.org/maven2/com/h2database/h2/2.2.224/h2-2.2.224.jar

# Compile
javac -cp h2.jar MainH2DatabaseTableCreation.java

# Run
java -cp .:h2.jar MainH2DatabaseTableCreation
```

## Source Code with Line Numbers

```java
     1  import java.sql.*;
     2
     3  /**
     4   * Demonstrates H2 Database operations including:
     5   * - Creating an in-memory database
     6   * - Creating tables with various data types
     7   * - Inserting sample data
     8   * - Querying data
     9   * - Viewing table metadata
    10   */
    11  public class MainH2DatabaseTableCreation {
    12
    13      // H2 in-memory database connection URL
    14      private static final String DB_URL = "jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1";
    15      private static final String DB_USER = "sa";
    16      private static final String DB_PASSWORD = "";
    17
    18      public static void main(String[] args) {
    19          System.out.println("=== H2 Database Table Creation Demo ===\n");
    20
    21          try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
    22              System.out.println("1. Connected to H2 database successfully");
    23              System.out.println("   Database URL: " + DB_URL);
    24              System.out.println("   Database Product: " + conn.getMetaData().getDatabaseProductName());
    25              System.out.println("   Database Version: " + conn.getMetaData().getDatabaseProductVersion() + "\n");
    26
    27              // Create tables
    28              createEmployeesTable(conn);
    29              createDepartmentsTable(conn);
    30
    31              // Insert sample data
    32              insertDepartments(conn);
    33              insertEmployees(conn);
    34
    35              // Query and display data
    36              queryEmployees(conn);
    37              queryDepartments(conn);
    38
    39              // Show table metadata
    40              showTableMetadata(conn, "EMPLOYEES");
    41
    42              // Demonstrate JOIN query
    43              demonstrateJoinQuery(conn);
    44
    45              System.out.println("\n=== Demo completed successfully ===");
    46
    47          } catch (SQLException e) {
    48              System.err.println("Database error: " + e.getMessage());
    49              e.printStackTrace();
    50          }
    51      }
    52
    53      /**
    54       * Creates the EMPLOYEES table with various column types
    55       */
    56      private static void createEmployeesTable(Connection conn) throws SQLException {
    57          String createTableSQL = """
    58              CREATE TABLE IF NOT EXISTS EMPLOYEES (
    59                  employee_id INT PRIMARY KEY AUTO_INCREMENT,
    60                  first_name VARCHAR(50) NOT NULL,
    61                  last_name VARCHAR(50) NOT NULL,
    62                  email VARCHAR(100) UNIQUE,
    63                  department_id INT,
    64                  salary DECIMAL(10, 2),
    65                  hire_date DATE,
    66                  is_active BOOLEAN DEFAULT TRUE
    67              )
    68              """;
    69
    70          try (Statement stmt = conn.createStatement()) {
    71              stmt.execute(createTableSQL);
    72              System.out.println("2. Created EMPLOYEES table");
    73              System.out.println("   - Columns: employee_id (PK, AUTO_INCREMENT), first_name, last_name,");
    74              System.out.println("     email (UNIQUE), department_id, salary, hire_date, is_active\n");
    75          }
    76      }
    77
    78      /**
    79       * Creates the DEPARTMENTS table
    80       */
    81      private static void createDepartmentsTable(Connection conn) throws SQLException {
    82          String createTableSQL = """
    83              CREATE TABLE IF NOT EXISTS DEPARTMENTS (
    84                  department_id INT PRIMARY KEY,
    85                  department_name VARCHAR(100) NOT NULL,
    86                  location VARCHAR(100)
    87              )
    88              """;
    89
    90          try (Statement stmt = conn.createStatement()) {
    91              stmt.execute(createTableSQL);
    92              System.out.println("3. Created DEPARTMENTS table");
    93              System.out.println("   - Columns: department_id (PK), department_name, location\n");
    94          }
    95      }
    96
    97      /**
    98       * Inserts sample department data
    99       */
   100      private static void insertDepartments(Connection conn) throws SQLException {
   101          String insertSQL = "INSERT INTO DEPARTMENTS (department_id, department_name, location) VALUES (?, ?, ?)";
   102
   103          try (PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {
   104              // Engineering department
   105              pstmt.setInt(1, 1);
   106              pstmt.setString(2, "Engineering");
   107              pstmt.setString(3, "San Francisco");
   108              pstmt.executeUpdate();
   109
   110              // Sales department
   111              pstmt.setInt(1, 2);
   112              pstmt.setString(2, "Sales");
   113              pstmt.setString(3, "New York");
   114              pstmt.executeUpdate();
   115
   116              // HR department
   117              pstmt.setInt(1, 3);
   118              pstmt.setString(2, "Human Resources");
   119              pstmt.setString(3, "Chicago");
   120              pstmt.executeUpdate();
   121
   122              System.out.println("4. Inserted 3 departments into DEPARTMENTS table\n");
   123          }
   124      }
   125
   126      /**
   127       * Inserts sample employee data
   128       */
   129      private static void insertEmployees(Connection conn) throws SQLException {
   130          String insertSQL = """
   131              INSERT INTO EMPLOYEES (first_name, last_name, email, department_id, salary, hire_date, is_active)
   132              VALUES (?, ?, ?, ?, ?, ?, ?)
   133              """;
   134
   135          try (PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {
   136              // Employee 1
   137              pstmt.setString(1, "John");
   138              pstmt.setString(2, "Doe");
   139              pstmt.setString(3, "john.doe@example.com");
   140              pstmt.setInt(4, 1);
   141              pstmt.setBigDecimal(5, new java.math.BigDecimal("95000.00"));
   142              pstmt.setDate(6, Date.valueOf("2022-01-15"));
   143              pstmt.setBoolean(7, true);
   144              pstmt.executeUpdate();
   145
   146              // Employee 2
   147              pstmt.setString(1, "Jane");
   148              pstmt.setString(2, "Smith");
   149              pstmt.setString(3, "jane.smith@example.com");
   150              pstmt.setInt(4, 2);
   151              pstmt.setBigDecimal(5, new java.math.BigDecimal("87000.00"));
   152              pstmt.setDate(6, Date.valueOf("2021-06-20"));
   153              pstmt.setBoolean(7, true);
   154              pstmt.executeUpdate();
   155
   156              // Employee 3
   157              pstmt.setString(1, "Bob");
   158              pstmt.setString(2, "Johnson");
   159              pstmt.setString(3, "bob.johnson@example.com");
   160              pstmt.setInt(4, 1);
   161              pstmt.setBigDecimal(5, new java.math.BigDecimal("102000.00"));
   162              pstmt.setDate(6, Date.valueOf("2020-03-10"));
   163              pstmt.setBoolean(7, true);
   164              pstmt.executeUpdate();
   165
   166              // Employee 4
   167              pstmt.setString(1, "Alice");
   168              pstmt.setString(2, "Williams");
   169              pstmt.setString(3, "alice.williams@example.com");
   170              pstmt.setInt(4, 3);
   171              pstmt.setBigDecimal(5, new java.math.BigDecimal("78000.00"));
   172              pstmt.setDate(6, Date.valueOf("2023-02-01"));
   173              pstmt.setBoolean(7, true);
   174              pstmt.executeUpdate();
   175
   176              System.out.println("5. Inserted 4 employees into EMPLOYEES table\n");
   177          }
   178      }
   179
   180      /**
   181       * Queries and displays all employees
   182       */
   183      private static void queryEmployees(Connection conn) throws SQLException {
   184          String query = "SELECT * FROM EMPLOYEES ORDER BY employee_id";
   185
   186          try (Statement stmt = conn.createStatement();
   187               ResultSet rs = stmt.executeQuery(query)) {
   188
   189              System.out.println("6. Querying EMPLOYEES table:");
   190              System.out.println("   " + "-".repeat(120));
   191              System.out.printf("   %-4s %-12s %-12s %-30s %-6s %-12s %-12s %-8s%n",
   192                      "ID", "First Name", "Last Name", "Email", "Dept", "Salary", "Hire Date", "Active");
   193              System.out.println("   " + "-".repeat(120));
   194
   195              while (rs.next()) {
   196                  System.out.printf("   %-4d %-12s %-12s %-30s %-6d $%-11.2f %-12s %-8s%n",
   197                      rs.getInt("employee_id"),
   198                      rs.getString("first_name"),
   199                      rs.getString("last_name"),
   200                      rs.getString("email"),
   201                      rs.getInt("department_id"),
   202                      rs.getBigDecimal("salary"),
   203                      rs.getDate("hire_date"),
   204                      rs.getBoolean("is_active"));
   205              }
   206              System.out.println("   " + "-".repeat(120) + "\n");
   207          }
   208      }
   209
   210      /**
   211       * Queries and displays all departments
   212       */
   213      private static void queryDepartments(Connection conn) throws SQLException {
   214          String query = "SELECT * FROM DEPARTMENTS ORDER BY department_id";
   215
   216          try (Statement stmt = conn.createStatement();
   217               ResultSet rs = stmt.executeQuery(query)) {
   218
   219              System.out.println("7. Querying DEPARTMENTS table:");
   220              System.out.println("   " + "-".repeat(70));
   221              System.out.printf("   %-6s %-30s %-20s%n", "ID", "Department Name", "Location");
   222              System.out.println("   " + "-".repeat(70));
   223
   224              while (rs.next()) {
   225                  System.out.printf("   %-6d %-30s %-20s%n",
   226                      rs.getInt("department_id"),
   227                      rs.getString("department_name"),
   228                      rs.getString("location"));
   229              }
   230              System.out.println("   " + "-".repeat(70) + "\n");
   231          }
   232      }
   233
   234      /**
   235       * Displays metadata information about a table
   236       */
   237      private static void showTableMetadata(Connection conn, String tableName) throws SQLException {
   238          DatabaseMetaData metaData = conn.getMetaData();
   239
   240          System.out.println("8. Table Metadata for " + tableName + ":");
   241
   242          try (ResultSet columns = metaData.getColumns(null, null, tableName, null)) {
   243              System.out.println("   " + "-".repeat(100));
   244              System.out.printf("   %-20s %-15s %-10s %-10s %-15s%n",
   245                      "Column Name", "Data Type", "Size", "Nullable", "Auto Increment");
   246              System.out.println("   " + "-".repeat(100));
   247
   248              while (columns.next()) {
   249                  String columnName = columns.getString("COLUMN_NAME");
   250                  String dataType = columns.getString("TYPE_NAME");
   251                  int columnSize = columns.getInt("COLUMN_SIZE");
   252                  String isNullable = columns.getString("IS_NULLABLE");
   253                  String isAutoIncrement = columns.getString("IS_AUTOINCREMENT");
   254
   255                  System.out.printf("   %-20s %-15s %-10d %-10s %-15s%n",
   256                      columnName, dataType, columnSize, isNullable, isAutoIncrement);
   257              }
   258              System.out.println("   " + "-".repeat(100) + "\n");
   259          }
   260      }
   261
   262      /**
   263       * Demonstrates a JOIN query between EMPLOYEES and DEPARTMENTS
   264       */
   265      private static void demonstrateJoinQuery(Connection conn) throws SQLException {
   266          String joinQuery = """
   267              SELECT e.employee_id, e.first_name, e.last_name, e.salary,
   268                     d.department_name, d.location
   269              FROM EMPLOYEES e
   270              JOIN DEPARTMENTS d ON e.department_id = d.department_id
   271              ORDER BY e.salary DESC
   272              """;
   273
   274          try (Statement stmt = conn.createStatement();
   275               ResultSet rs = stmt.executeQuery(joinQuery)) {
   276
   277              System.out.println("9. JOIN Query (Employees with Department Information):");
   278              System.out.println("   " + "-".repeat(110));
   279              System.out.printf("   %-4s %-12s %-12s %-12s %-30s %-20s%n",
   280                      "ID", "First Name", "Last Name", "Salary", "Department", "Location");
   281              System.out.println("   " + "-".repeat(110));
   282
   283              while (rs.next()) {
   284                  System.out.printf("   %-4d %-12s %-12s $%-11.2f %-30s %-20s%n",
   285                      rs.getInt("employee_id"),
   286                      rs.getString("first_name"),
   287                      rs.getString("last_name"),
   288                      rs.getBigDecimal("salary"),
   289                      rs.getString("department_name"),
   290                      rs.getString("location"));
   291              }
   292              System.out.println("   " + "-".repeat(110));
   293          }
   294      }
   295  }
```

## Program Output

```
=== H2 Database Table Creation Demo ===

1. Connected to H2 database successfully
   Database URL: jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1
   Database Product: H2
   Database Version: 2.2.224 (2023-09-17)

2. Created EMPLOYEES table
   - Columns: employee_id (PK, AUTO_INCREMENT), first_name, last_name,
     email (UNIQUE), department_id, salary, hire_date, is_active

3. Created DEPARTMENTS table
   - Columns: department_id (PK), department_name, location

4. Inserted 3 departments into DEPARTMENTS table

5. Inserted 4 employees into EMPLOYEES table

6. Querying EMPLOYEES table:
   ------------------------------------------------------------------------------------------------------------------------
   ID   First Name   Last Name    Email                          Dept   Salary       Hire Date    Active
   ------------------------------------------------------------------------------------------------------------------------
   1    John         Doe          john.doe@example.com           1      $95000.00    2022-01-15   true
   2    Jane         Smith        jane.smith@example.com         2      $87000.00    2021-06-20   true
   3    Bob          Johnson      bob.johnson@example.com        1      $102000.00   2020-03-10   true
   4    Alice        Williams     alice.williams@example.com     3      $78000.00    2023-02-01   true
   ------------------------------------------------------------------------------------------------------------------------

7. Querying DEPARTMENTS table:
   ----------------------------------------------------------------------
   ID     Department Name                Location
   ----------------------------------------------------------------------
   1      Engineering                    San Francisco
   2      Sales                          New York
   3      Human Resources                Chicago
   ----------------------------------------------------------------------

8. Table Metadata for EMPLOYEES:
   ----------------------------------------------------------------------------------------------------
   Column Name          Data Type       Size       Nullable   Auto Increment
   ----------------------------------------------------------------------------------------------------
   EMPLOYEE_ID          INTEGER         32         NO         YES
   FIRST_NAME           CHARACTER VARYING 50         NO         NO
   LAST_NAME            CHARACTER VARYING 50         NO         NO
   EMAIL                CHARACTER VARYING 100        YES        NO
   DEPARTMENT_ID        INTEGER         32         YES        NO
   SALARY               DECIMAL         10         YES        NO
   HIRE_DATE            DATE            10         YES        NO
   IS_ACTIVE            BOOLEAN         1          YES        NO
   ----------------------------------------------------------------------------------------------------

9. JOIN Query (Employees with Department Information):
   --------------------------------------------------------------------------------------------------------------
   ID   First Name   Last Name    Salary       Department                     Location
   --------------------------------------------------------------------------------------------------------------
   3    Bob          Johnson      $102000.00   Engineering                    San Francisco
   1    John         Doe          $95000.00    Engineering                    San Francisco
   2    Jane         Smith        $87000.00    Sales                          New York
   4    Alice        Williams     $78000.00    Human Resources                Chicago
   --------------------------------------------------------------------------------------------------------------

=== Demo completed successfully ===
```

## Code Annotations

### Database Connection (Lines 14-25)
- **Line 14**: Defines the H2 in-memory database URL with `DB_CLOSE_DELAY=-1` to keep the database alive
- **Line 21**: Establishes connection using try-with-resources for automatic cleanup
- **Lines 24-25**: Retrieves database metadata showing **H2 version 2.2.224** (see output lines 4-5)

### Table Creation (Lines 56-76, 81-95)
- **Lines 58-67**: Creates EMPLOYEES table with:
  - `employee_id`: Primary key with AUTO_INCREMENT (see metadata output showing "YES" for auto increment)
  - `email`: UNIQUE constraint
  - `salary`: DECIMAL(10,2) for precise financial data
  - `is_active`: BOOLEAN with DEFAULT TRUE
- **Lines 83-87**: Creates DEPARTMENTS table with simpler structure
- **Output lines 6-9**: Confirms successful table creation

### Data Insertion (Lines 100-177)
- **Lines 103-120**: Uses PreparedStatement to insert 3 departments safely (prevents SQL injection)
- **Lines 135-174**: Inserts 4 employees with various data types:
  - BigDecimal for salary precision (lines 141, 151, 161, 171)
  - Date.valueOf for date handling (lines 142, 152, 162, 172)
- **Output lines 10-13**: Confirms data insertion

### Querying Data (Lines 183-207, 213-231)
- **Line 184**: Simple SELECT query to retrieve all employees
- **Lines 195-204**: ResultSet iteration demonstrating type-safe data retrieval
- **Output lines 14-23**: Shows all 4 employees with formatted output
- **Output lines 24-30**: Shows all 3 departments

### Metadata Inspection (Lines 237-259)
- **Line 238**: Uses DatabaseMetaData to introspect table structure
- **Lines 248-256**: Iterates through columns extracting:
  - Column names
  - Data types (INTEGER, CHARACTER VARYING, DECIMAL, DATE, BOOLEAN)
  - Column sizes
  - Nullability constraints
  - Auto-increment status
- **Output lines 31-41**: Shows complete metadata for EMPLOYEES table, confirming:
  - EMPLOYEE_ID is auto-increment (YES)
  - FIRST_NAME and LAST_NAME are NOT NULL
  - EMAIL allows NULL values

### JOIN Operations (Lines 265-293)
- **Lines 266-272**: SQL JOIN query combining EMPLOYEES and DEPARTMENTS tables
- **Line 271**: JOIN condition on department_id foreign key
- **Line 271**: ORDER BY salary DESC sorts by highest salary first
- **Output lines 42-50**: Shows combined data with Bob Johnson ($102,000) at the top

## Key H2 Database Features Demonstrated

1. **In-Memory Database**: Fast, lightweight database perfect for testing (line 14)
2. **SQL Compatibility**: Standard SQL DDL and DML operations work seamlessly
3. **Auto-Increment**: Primary key generation without manual ID management (line 59)
4. **Constraints**: PRIMARY KEY, UNIQUE, NOT NULL, DEFAULT (lines 59-66)
5. **Data Types**: VARCHAR, INT, DECIMAL, DATE, BOOLEAN (lines 60-66)
6. **JDBC Compliance**: Standard JDBC API usage throughout
7. **Metadata API**: Complete table introspection capabilities (lines 237-259)
8. **Text Blocks**: Java 15+ text blocks for multi-line SQL (lines 57, 82, 130, 266)

## Why H2 Database?

- **Zero Configuration**: No installation or setup required
- **Embedded Mode**: Runs entirely within the Java application
- **Testing**: Perfect for unit tests and demos
- **Performance**: Extremely fast for in-memory operations
- **Standards Compliant**: Supports most SQL:2003 features
- **Small Footprint**: Entire database engine in a ~2.5MB jar file
