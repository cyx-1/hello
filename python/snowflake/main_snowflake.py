#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "snowflake-connector-python>=3.7.0",
#     "pandas>=2.2.0",
# ]
# ///

"""
Snowflake Demonstration in Python
Showcases key Snowflake features including:
- Connection management and authentication
- Database and schema operations
- Table creation with various data types
- Data insertion and bulk loading
- Querying and filtering
- Joins and aggregations
- Transactions
- User-defined functions (UDFs)
- Stored procedures
- Pandas integration
"""

import os
from typing import Any

import pandas as pd
import snowflake.connector


def print_section(title: str):
    """Print a formatted section header"""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def print_results(cursor: Any, max_rows: int = 10):
    """Print query results in a formatted way"""
    if cursor.description:
        columns = [desc[0] for desc in cursor.description]
        print(f"Columns: {', '.join(columns)}")
        print("-" * 70)
        rows = cursor.fetchall()
        for i, row in enumerate(rows[:max_rows], 1):
            print(f"Row {i}: {row}")
        if len(rows) > max_rows:
            print(f"... ({len(rows) - max_rows} more rows)")
    else:
        print("No results returned")


def demo_connection(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate Snowflake connection and basic info"""
    print_section("1. CONNECTION INFORMATION")

    # Line 62: Get connection details
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_VERSION(), CURRENT_TIMESTAMP()")
    result = cursor.fetchone()
    print(f"Line 62-65: Snowflake Version: {result[0]}")
    print(f"Line 62-65: Current Timestamp: {result[1]}")

    # Line 70: Get current user and role
    cursor.execute("SELECT CURRENT_USER(), CURRENT_ROLE()")
    result = cursor.fetchone()
    print(f"Line 70-72: Current User: {result[0]}")
    print(f"Line 70-72: Current Role: {result[1]}")

    # Line 76: Get current warehouse and database
    cursor.execute("SELECT CURRENT_WAREHOUSE(), CURRENT_DATABASE()")
    result = cursor.fetchone()
    print(f"Line 76-78: Current Warehouse: {result[0]}")
    print(f"Line 76-78: Current Database: {result[1]}")

    cursor.close()


def demo_database_schema(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate database and schema operations"""
    print_section("2. DATABASE AND SCHEMA OPERATIONS")

    cursor = conn.cursor()

    # Line 92: Create a new database
    cursor.execute("CREATE DATABASE IF NOT EXISTS DEMO_DB")
    print("Line 92: CREATE DATABASE DEMO_DB")

    # Line 96: Use the database
    cursor.execute("USE DATABASE DEMO_DB")
    print("Line 96: USE DATABASE DEMO_DB")

    # Line 100: Create a schema
    cursor.execute("CREATE SCHEMA IF NOT EXISTS DEMO_SCHEMA")
    print("Line 100: CREATE SCHEMA DEMO_SCHEMA")

    # Line 104: Use the schema
    cursor.execute("USE SCHEMA DEMO_SCHEMA")
    print("Line 104: USE SCHEMA DEMO_SCHEMA")

    # Line 108: Show databases
    cursor.execute("SHOW DATABASES LIKE 'DEMO_DB'")
    print("Line 108: SHOW DATABASES LIKE 'DEMO_DB'")
    print_results(cursor, max_rows=3)

    # Line 113: Show schemas
    cursor.execute("SHOW SCHEMAS IN DATABASE DEMO_DB")
    print("\nLine 113: SHOW SCHEMAS IN DATABASE DEMO_DB")
    print_results(cursor, max_rows=3)

    cursor.close()


def demo_table_creation(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate table creation with various data types"""
    print_section("3. TABLE CREATION WITH DATA TYPES")

    cursor = conn.cursor()

    # Line 127: Create employees table
    create_table_sql = """
    CREATE OR REPLACE TABLE employees (
        employee_id INTEGER AUTOINCREMENT,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100),
        hire_date DATE,
        salary NUMBER(10, 2),
        department VARCHAR(50),
        is_active BOOLEAN,
        metadata VARIANT,
        PRIMARY KEY (employee_id)
    )
    """
    cursor.execute(create_table_sql)
    print("Line 127-141: CREATE TABLE employees with multiple data types")
    print("  - INTEGER with AUTOINCREMENT")
    print("  - VARCHAR for strings")
    print("  - DATE for dates")
    print("  - NUMBER(10,2) for decimal values")
    print("  - BOOLEAN for true/false")
    print("  - VARIANT for semi-structured data (JSON)")

    # Line 151: Create departments table for join demonstration
    create_dept_sql = """
    CREATE OR REPLACE TABLE departments (
        dept_id INTEGER,
        dept_name VARCHAR(50),
        dept_location VARCHAR(100),
        PRIMARY KEY (dept_id)
    )
    """
    cursor.execute(create_dept_sql)
    print("\nLine 151-160: CREATE TABLE departments for join examples")

    # Line 163: Show table structure
    cursor.execute("DESCRIBE TABLE employees")
    print("\nLine 163: DESCRIBE TABLE employees")
    print_results(cursor, max_rows=10)

    cursor.close()


def demo_data_insertion(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate various data insertion methods"""
    print_section("4. DATA INSERTION METHODS")

    cursor = conn.cursor()

    # Line 179: Insert single row with VALUES
    insert_sql = """
    INSERT INTO employees (first_name, last_name, email, hire_date, salary, department, is_active, metadata)
    VALUES ('John', 'Doe', 'john.doe@example.com', '2023-01-15', 75000.00, 'Engineering', TRUE,
            PARSE_JSON('{"skills": ["Python", "SQL"], "years_exp": 5}'))
    """
    cursor.execute(insert_sql)
    print("Line 179-184: INSERT single employee with VARIANT (JSON) data")

    # Line 188: Insert multiple rows in single statement
    insert_multiple_sql = """
    INSERT INTO employees (first_name, last_name, email, hire_date, salary, department, is_active, metadata)
    VALUES
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-02-20', 82000.00, 'Engineering', TRUE,
         PARSE_JSON('{"skills": ["Java", "Kubernetes"], "years_exp": 7}')),
        ('Bob', 'Johnson', 'bob.johnson@example.com', '2023-03-10', 68000.00, 'Marketing', TRUE,
         PARSE_JSON('{"skills": ["SEO", "Analytics"], "years_exp": 4}')),
        ('Alice', 'Williams', 'alice.williams@example.com', '2023-04-05', 91000.00, 'Engineering', TRUE,
         PARSE_JSON('{"skills": ["Python", "ML"], "years_exp": 8}')),
        ('Charlie', 'Brown', 'charlie.brown@example.com', '2023-05-12', 72000.00, 'Sales', TRUE,
         PARSE_JSON('{"skills": ["CRM", "Negotiation"], "years_exp": 6}'))
    """
    cursor.execute(insert_multiple_sql)
    print("Line 188-200: INSERT multiple employees in single statement")

    # Line 203: Insert departments
    dept_sql = """
    INSERT INTO departments (dept_id, dept_name, dept_location)
    VALUES
        (1, 'Engineering', 'San Francisco'),
        (2, 'Marketing', 'New York'),
        (3, 'Sales', 'Chicago'),
        (4, 'Finance', 'Boston')
    """
    cursor.execute(dept_sql)
    print("Line 203-212: INSERT department data for joins")

    # Line 215: Verify insertion with count
    cursor.execute("SELECT COUNT(*) FROM employees")
    count = cursor.fetchone()[0]
    print(f"\nLine 215-217: Total employees inserted: {count}")

    cursor.close()


def demo_querying(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate various query operations"""
    print_section("5. QUERYING AND FILTERING")

    cursor = conn.cursor()

    # Line 231: Simple SELECT with all columns
    cursor.execute("SELECT * FROM employees LIMIT 3")
    print("Line 231: SELECT * FROM employees LIMIT 3")
    print_results(cursor)

    # Line 236: SELECT specific columns with WHERE clause
    query_sql = """
    SELECT first_name, last_name, salary, department
    FROM employees
    WHERE salary > 75000
    ORDER BY salary DESC
    """
    cursor.execute(query_sql)
    print("\nLine 236-242: SELECT with WHERE and ORDER BY (salary > 75000)")
    print_results(cursor)

    # Line 246: Query with LIKE pattern matching
    cursor.execute("""
        SELECT first_name, last_name, email
        FROM employees
        WHERE email LIKE '%example.com'
    """)
    print("\nLine 246-250: SELECT with LIKE pattern (emails ending in example.com)")
    print_results(cursor)

    # Line 254: Query with date filtering
    cursor.execute("""
        SELECT first_name, last_name, hire_date,
               DATEDIFF('day', hire_date, CURRENT_DATE()) AS days_employed
        FROM employees
        WHERE hire_date >= '2023-03-01'
        ORDER BY hire_date
    """)
    print("\nLine 254-261: SELECT with date filtering and DATEDIFF calculation")
    print_results(cursor)

    # Line 265: Query VARIANT (JSON) data
    cursor.execute("""
        SELECT first_name, last_name,
               metadata:skills AS skills,
               metadata:years_exp AS experience
        FROM employees
        WHERE metadata:years_exp::INT >= 6
    """)
    print("\nLine 265-272: SELECT querying JSON data from VARIANT column")
    print_results(cursor)

    cursor.close()


def demo_aggregations(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate aggregation functions"""
    print_section("6. AGGREGATIONS AND GROUP BY")

    cursor = conn.cursor()

    # Line 286: Basic aggregation functions
    cursor.execute("""
        SELECT
            COUNT(*) AS total_employees,
            AVG(salary) AS avg_salary,
            MIN(salary) AS min_salary,
            MAX(salary) AS max_salary,
            SUM(salary) AS total_payroll
        FROM employees
    """)
    print("Line 286-295: Aggregate functions (COUNT, AVG, MIN, MAX, SUM)")
    print_results(cursor)

    # Line 299: GROUP BY with aggregations
    cursor.execute("""
        SELECT
            department,
            COUNT(*) AS employee_count,
            AVG(salary) AS avg_salary,
            MAX(salary) AS max_salary
        FROM employees
        GROUP BY department
        ORDER BY avg_salary DESC
    """)
    print("\nLine 299-309: GROUP BY department with aggregations")
    print_results(cursor)

    # Line 313: HAVING clause with GROUP BY
    cursor.execute("""
        SELECT
            department,
            AVG(salary) AS avg_salary
        FROM employees
        GROUP BY department
        HAVING AVG(salary) > 70000
        ORDER BY avg_salary DESC
    """)
    print("\nLine 313-323: GROUP BY with HAVING clause (avg salary > 70000)")
    print_results(cursor)

    cursor.close()


def demo_joins(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate table joins"""
    print_section("7. TABLE JOINS")

    cursor = conn.cursor()

    # Line 337: INNER JOIN
    cursor.execute("""
        SELECT
            e.first_name,
            e.last_name,
            e.department AS dept_name,
            d.dept_location
        FROM employees e
        INNER JOIN departments d ON e.department = d.dept_name
        ORDER BY e.last_name
    """)
    print("Line 337-347: INNER JOIN employees with departments")
    print_results(cursor)

    # Line 351: LEFT JOIN with aggregation
    cursor.execute("""
        SELECT
            d.dept_name,
            d.dept_location,
            COUNT(e.employee_id) AS employee_count,
            AVG(e.salary) AS avg_salary
        FROM departments d
        LEFT JOIN employees e ON d.dept_name = e.department
        GROUP BY d.dept_name, d.dept_location
        ORDER BY employee_count DESC
    """)
    print("\nLine 351-362: LEFT JOIN with aggregation (all departments)")
    print_results(cursor)

    cursor.close()


def demo_transactions(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate transaction management"""
    print_section("8. TRANSACTIONS")

    cursor = conn.cursor()

    try:
        # Line 376: Begin transaction
        conn.autocommit = False
        print("Line 376: BEGIN TRANSACTION (autocommit=False)")

        # Line 380: Update salaries
        cursor.execute("""
            UPDATE employees
            SET salary = salary * 1.10
            WHERE department = 'Engineering'
        """)
        affected_rows = cursor.rowcount
        print("Line 380-384: UPDATE salaries for Engineering (+10%)")
        print(f"  Affected rows: {affected_rows}")

        # Line 389: Verify changes before commit
        cursor.execute("""
            SELECT first_name, last_name, salary
            FROM employees
            WHERE department = 'Engineering'
        """)
        print("\nLine 389-393: SELECT to verify changes (before COMMIT)")
        print_results(cursor)

        # Line 397: Commit transaction
        conn.commit()
        print("\nLine 397: COMMIT TRANSACTION")

        # Line 401: Verify committed changes
        cursor.execute("""
            SELECT first_name, last_name, salary
            FROM employees
            WHERE department = 'Engineering'
        """)
        print("\nLine 401-405: SELECT after COMMIT (changes persisted)")
        print_results(cursor)

    except Exception as e:
        # Line 410: Rollback on error
        conn.rollback()
        print(f"\nLine 410: ROLLBACK TRANSACTION due to error: {e}")
    finally:
        conn.autocommit = True

    cursor.close()


def demo_udf(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate User-Defined Functions (UDFs)"""
    print_section("9. USER-DEFINED FUNCTIONS (UDFs)")

    cursor = conn.cursor()

    # Line 426: Create SQL UDF for salary grade calculation
    create_udf_sql = """
    CREATE OR REPLACE FUNCTION calculate_salary_grade(salary NUMBER)
    RETURNS VARCHAR
    AS
    $$
        CASE
            WHEN salary < 70000 THEN 'Junior'
            WHEN salary >= 70000 AND salary < 80000 THEN 'Mid-Level'
            WHEN salary >= 80000 AND salary < 90000 THEN 'Senior'
            ELSE 'Principal'
        END
    $$
    """
    cursor.execute(create_udf_sql)
    print("Line 426-439: CREATE FUNCTION calculate_salary_grade()")
    print("  Returns salary grade based on salary amount")

    # Line 443: Use the UDF in a query
    cursor.execute("""
        SELECT
            first_name,
            last_name,
            salary,
            calculate_salary_grade(salary) AS salary_grade
        FROM employees
        ORDER BY salary DESC
    """)
    print("\nLine 443-452: SELECT using calculate_salary_grade() UDF")
    print_results(cursor)

    # Line 456: Create UDF for bonus calculation
    cursor.execute("""
        CREATE OR REPLACE FUNCTION calculate_bonus(salary NUMBER, performance_rating NUMBER)
        RETURNS NUMBER(10, 2)
        AS
        $$
            salary * (performance_rating / 100.0)
        $$
    """)
    print("\nLine 456-464: CREATE FUNCTION calculate_bonus()")

    # Line 467: Use bonus calculation UDF
    cursor.execute("""
        SELECT
            first_name,
            last_name,
            salary,
            calculate_bonus(salary, 15) AS bonus_15_percent
        FROM employees
        ORDER BY salary DESC
        LIMIT 3
    """)
    print("\nLine 467-477: SELECT using calculate_bonus() UDF (15% bonus)")
    print_results(cursor)

    cursor.close()


def demo_stored_procedures(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate Stored Procedures"""
    print_section("10. STORED PROCEDURES")

    cursor = conn.cursor()

    # Line 493: Create stored procedure for employee stats
    create_proc_sql = """
    CREATE OR REPLACE PROCEDURE get_department_stats(dept_name VARCHAR)
    RETURNS TABLE(metric VARCHAR, value VARCHAR)
    LANGUAGE SQL
    AS
    $$
    BEGIN
        LET result_query := 'SELECT
            ''Employee Count'' AS metric,
            COUNT(*)::VARCHAR AS value
        FROM employees
        WHERE department = ''' || :dept_name || '''
        UNION ALL
        SELECT
            ''Average Salary'' AS metric,
            ROUND(AVG(salary), 2)::VARCHAR AS value
        FROM employees
        WHERE department = ''' || :dept_name || '''
        UNION ALL
        SELECT
            ''Total Payroll'' AS metric,
            ROUND(SUM(salary), 2)::VARCHAR AS value
        FROM employees
        WHERE department = ''' || :dept_name || '''';

        LET res RESULTSET := (EXECUTE IMMEDIATE :result_query);
        RETURN TABLE(res);
    END;
    $$
    """
    cursor.execute(create_proc_sql)
    print("Line 493-525: CREATE PROCEDURE get_department_stats()")
    print("  Returns employee count, avg salary, and total payroll for a department")

    # Line 529: Call the stored procedure
    cursor.execute("CALL get_department_stats('Engineering')")
    print("\nLine 529: CALL get_department_stats('Engineering')")
    print_results(cursor)

    cursor.close()


def demo_pandas_integration(conn: snowflake.connector.SnowflakeConnection):
    """Demonstrate Pandas integration"""
    print_section("11. PANDAS INTEGRATION")

    # Line 543: Read query results into Pandas DataFrame
    query = """
    SELECT
        e.first_name,
        e.last_name,
        e.salary,
        e.department,
        e.hire_date
    FROM employees e
    ORDER BY salary DESC
    """
    df = pd.read_sql(query, conn)
    print("Line 543-553: pd.read_sql() - Load query results into DataFrame")
    print(f"  DataFrame shape: {df.shape}")
    print(f"  Columns: {df.columns.tolist()}")
    print("\nFirst 3 rows:")
    print(df.head(3).to_string(index=False))

    # Line 562: DataFrame operations
    print("\nLine 562-565: DataFrame operations")
    print(f"  Average salary: ${df['SALARY'].mean():,.2f}")
    print(f"  Median salary: ${df['SALARY'].median():,.2f}")
    print(f"  Salary std dev: ${df['SALARY'].std():,.2f}")

    # Line 569: Group by department in Pandas
    dept_stats = df.groupby('DEPARTMENT')['SALARY'].agg(['count', 'mean', 'min', 'max'])
    print("\nLine 569-571: DataFrame groupby department")
    print(dept_stats.to_string())

    # Line 575: Write DataFrame back to Snowflake
    new_table_name = "employees_analysis"
    df_summary = df.groupby('DEPARTMENT').agg({
        'FIRST_NAME': 'count',
        'SALARY': ['mean', 'min', 'max']
    }).reset_index()
    df_summary.columns = ['department', 'emp_count', 'avg_salary', 'min_salary', 'max_salary']

    # Note: write_pandas requires snowflake.connector.pandas_tools
    from snowflake.connector.pandas_tools import write_pandas

    success, nchunks, nrows, _ = write_pandas(
        conn,
        df_summary,
        new_table_name.upper(),
        auto_create_table=True,
        overwrite=True
    )
    print("\nLine 575-593: write_pandas() - Write DataFrame to Snowflake")
    print(f"  Table: {new_table_name}")
    print(f"  Success: {success}, Rows: {nrows}, Chunks: {nchunks}")

    # Line 598: Verify the new table
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {new_table_name}")
    print(f"\nLine 598-599: SELECT * FROM {new_table_name}")
    print_results(cursor)
    cursor.close()


def cleanup(conn: snowflake.connector.SnowflakeConnection):
    """Clean up created objects"""
    print_section("12. CLEANUP")

    cursor = conn.cursor()

    print("Line 614: Dropping created objects...")
    cleanup_commands = [
        "DROP TABLE IF EXISTS employees_analysis",
        "DROP PROCEDURE IF EXISTS get_department_stats(VARCHAR)",
        "DROP FUNCTION IF EXISTS calculate_bonus(NUMBER, NUMBER)",
        "DROP FUNCTION IF EXISTS calculate_salary_grade(NUMBER)",
        "DROP TABLE IF EXISTS employees",
        "DROP TABLE IF EXISTS departments",
        "DROP SCHEMA IF EXISTS DEMO_SCHEMA",
        "DROP DATABASE IF EXISTS DEMO_DB"
    ]

    for cmd in cleanup_commands:
        try:
            cursor.execute(cmd)
            print(f"  ✓ {cmd}")
        except Exception as e:
            print(f"  ✗ {cmd} - {e}")

    cursor.close()
    print("\nLine 614-634: Cleanup completed")


def main():
    """Main function to run all Snowflake demonstrations"""
    print("\n" + "=" * 70)
    print("  SNOWFLAKE PYTHON DEMONSTRATION")
    print("  Comprehensive Snowflake Feature Showcase")
    print("=" * 70)

    # Connection parameters from environment variables
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    user = os.getenv("SNOWFLAKE_USER")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH")
    database = os.getenv("SNOWFLAKE_DATABASE", "")
    schema = os.getenv("SNOWFLAKE_SCHEMA", "")

    if not all([account, user, password]):
        print("\n" + "=" * 70)
        print("  DEMO MODE - No Snowflake Credentials Provided")
        print("=" * 70)
        print("\nThis demonstration requires Snowflake credentials.")
        print("\nTo run with actual Snowflake connection, set these environment variables:")
        print("  export SNOWFLAKE_ACCOUNT='your_account'")
        print("  export SNOWFLAKE_USER='your_username'")
        print("  export SNOWFLAKE_PASSWORD='your_password'")
        print("  export SNOWFLAKE_WAREHOUSE='your_warehouse'  # Optional, defaults to COMPUTE_WH")
        print("  export SNOWFLAKE_DATABASE='your_database'    # Optional")
        print("  export SNOWFLAKE_SCHEMA='your_schema'        # Optional")
        print("\nExample:")
        print("  export SNOWFLAKE_ACCOUNT='abc12345.us-east-1'")
        print("  export SNOWFLAKE_USER='john_doe'")
        print("  export SNOWFLAKE_PASSWORD='secure_password'")
        print("\n" + "=" * 70)
        print("\nWHAT THIS DEMONSTRATION COVERS:")
        print("=" * 70)
        print("""
1. CONNECTION INFORMATION
   - Snowflake version and timestamp
   - Current user, role, warehouse, database

2. DATABASE AND SCHEMA OPERATIONS
   - CREATE DATABASE and SCHEMA
   - USE DATABASE/SCHEMA commands
   - SHOW DATABASES and SCHEMAS

3. TABLE CREATION WITH DATA TYPES
   - INTEGER, VARCHAR, DATE, NUMBER, BOOLEAN
   - VARIANT for semi-structured JSON data
   - AUTOINCREMENT and PRIMARY KEY

4. DATA INSERTION METHODS
   - Single row INSERT
   - Multi-row INSERT
   - Inserting JSON data into VARIANT columns

5. QUERYING AND FILTERING
   - SELECT with WHERE and ORDER BY
   - LIKE pattern matching
   - Date filtering with DATEDIFF
   - Querying JSON data from VARIANT columns

6. AGGREGATIONS AND GROUP BY
   - COUNT, AVG, MIN, MAX, SUM functions
   - GROUP BY with multiple aggregations
   - HAVING clause for filtered grouping

7. TABLE JOINS
   - INNER JOIN between tables
   - LEFT JOIN with aggregations

8. TRANSACTIONS
   - BEGIN, COMMIT, ROLLBACK
   - Atomic multi-statement operations

9. USER-DEFINED FUNCTIONS (UDFs)
   - SQL-based UDFs
   - Using UDFs in SELECT statements

10. STORED PROCEDURES
    - Creating procedures with LANGUAGE SQL
    - CALL procedure with parameters

11. PANDAS INTEGRATION
    - pd.read_sql() to load data into DataFrames
    - DataFrame operations and analysis
    - write_pandas() to write data back to Snowflake

12. CLEANUP
    - DROP objects to clean up demo resources
        """)
        print("=" * 70)
        return

    try:
        # Line 733: Connect to Snowflake
        print("\nLine 733: Connecting to Snowflake...")
        conn = snowflake.connector.connect(
            account=account,
            user=user,
            password=password,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        print("✓ Connected to Snowflake successfully")

        # Run all demonstrations
        demo_connection(conn)
        demo_database_schema(conn)
        demo_table_creation(conn)
        demo_data_insertion(conn)
        demo_querying(conn)
        demo_aggregations(conn)
        demo_joins(conn)
        demo_transactions(conn)
        demo_udf(conn)
        demo_stored_procedures(conn)
        demo_pandas_integration(conn)

        # Cleanup
        cleanup(conn)

        # Line 763: Close connection
        conn.close()
        print("\nLine 763: Connection closed")

        print("\n" + "=" * 70)
        print("  ✓ All Snowflake demonstrations completed successfully!")
        print("=" * 70 + "\n")

    except snowflake.connector.errors.DatabaseError as e:
        print(f"\n❌ Snowflake Database Error: {e}")
        print("   Check your credentials and connection parameters")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")


if __name__ == "__main__":
    main()
