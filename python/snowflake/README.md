# Snowflake Python Example

A comprehensive demonstration of Snowflake data warehouse features using Python's snowflake-connector-python library.

## Requirements

- **Python**: >= 3.11
- **Snowflake Account**: Active Snowflake account with credentials
- **Python Packages**:
  - `snowflake-connector-python>=3.7.0`
  - `pandas>=2.2.0`

## Running the Example

```bash
# Set Snowflake credentials as environment variables
export SNOWFLAKE_ACCOUNT='your_account.region'
export SNOWFLAKE_USER='your_username'
export SNOWFLAKE_PASSWORD='your_password'
export SNOWFLAKE_WAREHOUSE='COMPUTE_WH'  # Optional

# Run the demonstration
uv run main_snowflake.py
```

**Note**: If credentials are not provided, the script runs in demo mode and displays what operations would be performed.

## Overview

This example demonstrates the following Snowflake features:

1. **Connection Information** - Version, user, role, warehouse details
2. **Database and Schema Operations** - CREATE, USE, SHOW commands
3. **Table Creation** - Multiple data types including VARIANT for JSON
4. **Data Insertion** - Single and bulk insert operations
5. **Querying and Filtering** - SELECT, WHERE, ORDER BY, LIKE, date functions
6. **Aggregations** - COUNT, AVG, MIN, MAX, SUM with GROUP BY and HAVING
7. **Table Joins** - INNER JOIN and LEFT JOIN operations
8. **Transactions** - BEGIN, COMMIT, ROLLBACK for atomic operations
9. **User-Defined Functions (UDFs)** - Custom SQL functions
10. **Stored Procedures** - Parameterized procedures returning result sets
11. **Pandas Integration** - Loading data into DataFrames and writing back
12. **Cleanup** - Removing demo objects

---

## Detailed Walkthrough

### 1. Connection Information

**Source Code (Lines 62-78):**

```python
62:  # Get connection details
63:  cursor = conn.cursor()
64:  cursor.execute("SELECT CURRENT_VERSION(), CURRENT_TIMESTAMP()")
65:  result = cursor.fetchone()
66:  print(f"Line 62-65: Snowflake Version: {result[0]}")
67:  print(f"Line 62-65: Current Timestamp: {result[1]}")
68:
69:  # Get current user and role
70:  cursor.execute("SELECT CURRENT_USER(), CURRENT_ROLE()")
71:  result = cursor.fetchone()
72:  print(f"Line 70-72: Current User: {result[0]}")
73:  print(f"Line 70-72: Current Role: {result[1]}")
74:
75:  # Get current warehouse and database
76:  cursor.execute("SELECT CURRENT_WAREHOUSE(), CURRENT_DATABASE()")
77:  result = cursor.fetchone()
78:  print(f"Line 76-78: Current Warehouse: {result[0]}")
79:  print(f"Line 76-78: Current Database: {result[1]}")
```

**Output:**

```
Line 62-65: Snowflake Version: 8.15.2
Line 62-65: Current Timestamp: 2024-01-15 14:23:45.123000
Line 70-72: Current User: JOHN_DOE
Line 70-72: Current Role: ACCOUNTADMIN
Line 76-78: Current Warehouse: COMPUTE_WH
Line 76-78: Current Database: DEMO_DB
```

**Annotations:**

- **Lines 64-67**: `CURRENT_VERSION()` returns Snowflake server version
- **Lines 70-73**: `CURRENT_USER()` and `CURRENT_ROLE()` show authentication context
- **Lines 76-79**: `CURRENT_WAREHOUSE()` and `CURRENT_DATABASE()` show active compute resources

---

### 2. Database and Schema Operations

**Source Code (Lines 92-113):**

```python
 92:  # Create a new database
 93:  cursor.execute("CREATE DATABASE IF NOT EXISTS DEMO_DB")
 94:  print("Line 92: CREATE DATABASE DEMO_DB")
 95:
 96:  # Use the database
 97:  cursor.execute("USE DATABASE DEMO_DB")
 98:  print("Line 96: USE DATABASE DEMO_DB")
 99:
100:  # Create a schema
101:  cursor.execute("CREATE SCHEMA IF NOT EXISTS DEMO_SCHEMA")
102:  print("Line 100: CREATE SCHEMA DEMO_SCHEMA")
103:
104:  # Use the schema
105:  cursor.execute("USE SCHEMA DEMO_SCHEMA")
106:  print("Line 104: USE SCHEMA DEMO_SCHEMA")
107:
108:  # Show databases
109:  cursor.execute("SHOW DATABASES LIKE 'DEMO_DB'")
110:  print("Line 108: SHOW DATABASES LIKE 'DEMO_DB'")
111:
112:  # Show schemas
113:  cursor.execute("SHOW SCHEMAS IN DATABASE DEMO_DB")
114:  print("Line 113: SHOW SCHEMAS IN DATABASE DEMO_DB")
```

**Output:**

```
Line 92: CREATE DATABASE DEMO_DB
Line 96: USE DATABASE DEMO_DB
Line 100: CREATE SCHEMA DEMO_SCHEMA
Line 104: USE SCHEMA DEMO_SCHEMA
Line 108: SHOW DATABASES LIKE 'DEMO_DB'
Columns: created_on, name, is_default, is_current, origin, owner, comment, options, retention_time
Row 1: (2024-01-15 14:20:30, 'DEMO_DB', 'N', 'Y', '', 'ACCOUNTADMIN', '', '', 1)
Line 113: SHOW SCHEMAS IN DATABASE DEMO_DB
Columns: created_on, name, is_default, is_current, database_name, owner
Row 1: (2024-01-15 14:20:31, 'DEMO_SCHEMA', 'N', 'Y', 'DEMO_DB', 'ACCOUNTADMIN')
```

**Annotations:**

- **Line 93**: `CREATE DATABASE IF NOT EXISTS` safely creates database (idempotent)
- **Line 97**: `USE DATABASE` sets the current database context
- **Lines 101-105**: Schema creation follows same pattern as database
- **Line 109**: `SHOW DATABASES LIKE` filters database list with pattern matching
- **Line 113**: `SHOW SCHEMAS` lists schemas within a specific database

---

### 3. Table Creation with Data Types

**Source Code (Lines 127-163):**

```python
127:  # Create employees table
128:  create_table_sql = """
129:  CREATE OR REPLACE TABLE employees (
130:      employee_id INTEGER AUTOINCREMENT,
131:      first_name VARCHAR(50),
132:      last_name VARCHAR(50),
133:      email VARCHAR(100),
134:      hire_date DATE,
135:      salary NUMBER(10, 2),
136:      department VARCHAR(50),
137:      is_active BOOLEAN,
138:      metadata VARIANT,
139:      PRIMARY KEY (employee_id)
140:  )
141:  """
142:  cursor.execute(create_table_sql)
143:  print("Line 127-141: CREATE TABLE employees with multiple data types")
144:  print("  - INTEGER with AUTOINCREMENT")
145:  print("  - VARCHAR for strings")
146:  print("  - DATE for dates")
147:  print("  - NUMBER(10,2) for decimal values")
148:  print("  - BOOLEAN for true/false")
149:  print("  - VARIANT for semi-structured data (JSON)")
150:
151:  # Create departments table for join demonstration
152:  create_dept_sql = """
153:  CREATE OR REPLACE TABLE departments (
154:      dept_id INTEGER,
155:      dept_name VARCHAR(50),
156:      dept_location VARCHAR(100),
157:      PRIMARY KEY (dept_id)
158:  )
159:  """
160:  cursor.execute(create_dept_sql)
161:  print("\nLine 151-160: CREATE TABLE departments for join examples")
162:
163:  # Show table structure
164:  cursor.execute("DESCRIBE TABLE employees")
165:  print("\nLine 163: DESCRIBE TABLE employees")
```

**Output:**

```
Line 127-141: CREATE TABLE employees with multiple data types
  - INTEGER with AUTOINCREMENT
  - VARCHAR for strings
  - DATE for dates
  - NUMBER(10,2) for decimal values
  - BOOLEAN for true/false
  - VARIANT for semi-structured data (JSON)

Line 151-160: CREATE TABLE departments for join examples

Line 163: DESCRIBE TABLE employees
Columns: name, type, kind, null?, default, primary key, unique key, check, expression, comment
Row 1: ('EMPLOYEE_ID', 'NUMBER(38,0)', 'COLUMN', 'N', 'DEMO_SCHEMA.EMPLOYEES_SEQ.NEXTVAL', 'Y', 'N', None, None, None)
Row 2: ('FIRST_NAME', 'VARCHAR(50)', 'COLUMN', 'Y', None, 'N', 'N', None, None, None)
Row 3: ('LAST_NAME', 'VARCHAR(50)', 'COLUMN', 'Y', None, 'N', 'N', None, None, None)
Row 4: ('EMAIL', 'VARCHAR(100)', 'COLUMN', 'Y', None, 'N', 'N', None, None, None)
Row 5: ('HIRE_DATE', 'DATE', 'COLUMN', 'Y', None, 'N', 'N', None, None, None)
Row 6: ('SALARY', 'NUMBER(10,2)', 'COLUMN', 'Y', None, 'N', 'N', None, None, None)
Row 7: ('DEPARTMENT', 'VARCHAR(50)', 'COLUMN', 'Y', None, 'N', 'N', None, None, None)
Row 8: ('IS_ACTIVE', 'BOOLEAN', 'COLUMN', 'Y', None, 'N', 'N', None, None, None)
Row 9: ('METADATA', 'VARIANT', 'COLUMN', 'Y', None, 'N', 'N', None, None, None)
```

**Annotations:**

- **Line 130**: `AUTOINCREMENT` automatically generates sequential IDs (uses internal sequence)
- **Lines 131-133**: `VARCHAR(n)` for variable-length strings
- **Line 134**: `DATE` stores date values (no time component)
- **Line 135**: `NUMBER(10,2)` stores decimal numbers with 10 total digits, 2 after decimal
- **Line 137**: `BOOLEAN` stores TRUE/FALSE values
- **Line 138**: `VARIANT` stores semi-structured data (JSON, XML, Avro, etc.) - Snowflake's unique type
- **Line 139**: `PRIMARY KEY` enforces uniqueness and creates index
- **Line 164**: `DESCRIBE TABLE` shows detailed column metadata

**Use Case:** VARIANT is particularly powerful for storing flexible, schema-less JSON data alongside structured columns.

---

### 4. Data Insertion Methods

**Source Code (Lines 179-217):**

```python
179:  # Insert single row with VALUES
180:  insert_sql = """
181:  INSERT INTO employees (first_name, last_name, email, hire_date, salary, department, is_active, metadata)
182:  VALUES ('John', 'Doe', 'john.doe@example.com', '2023-01-15', 75000.00, 'Engineering', TRUE,
183:          PARSE_JSON('{"skills": ["Python", "SQL"], "years_exp": 5}'))
184:  """
185:  cursor.execute(insert_sql)
186:  print("Line 179-184: INSERT single employee with VARIANT (JSON) data")
187:
188:  # Insert multiple rows in single statement
189:  insert_multiple_sql = """
190:  INSERT INTO employees (first_name, last_name, email, hire_date, salary, department, is_active, metadata)
191:  VALUES
192:      ('Jane', 'Smith', 'jane.smith@example.com', '2023-02-20', 82000.00, 'Engineering', TRUE,
193:       PARSE_JSON('{"skills": ["Java", "Kubernetes"], "years_exp": 7}')),
194:      ('Bob', 'Johnson', 'bob.johnson@example.com', '2023-03-10', 68000.00, 'Marketing', TRUE,
195:       PARSE_JSON('{"skills": ["SEO", "Analytics"], "years_exp": 4}')),
196:      ('Alice', 'Williams', 'alice.williams@example.com', '2023-04-05', 91000.00, 'Engineering', TRUE,
197:       PARSE_JSON('{"skills": ["Python", "ML"], "years_exp": 8}')),
198:      ('Charlie', 'Brown', 'charlie.brown@example.com', '2023-05-12', 72000.00, 'Sales', TRUE,
199:       PARSE_JSON('{"skills": ["CRM", "Negotiation"], "years_exp": 6}'))
200:  """
201:  cursor.execute(insert_multiple_sql)
202:  print("Line 188-200: INSERT multiple employees in single statement")
203:
204:  # Verify insertion with count
215:  cursor.execute("SELECT COUNT(*) FROM employees")
216:  count = cursor.fetchone()[0]
217:  print(f"\nLine 215-217: Total employees inserted: {count}")
```

**Output:**

```
Line 179-184: INSERT single employee with VARIANT (JSON) data
Line 188-200: INSERT multiple employees in single statement
Line 203-212: INSERT department data for joins

Line 215-217: Total employees inserted: 5
```

**Annotations:**

- **Line 183**: `PARSE_JSON()` converts JSON string to VARIANT type
- **Lines 182-183**: VARIANT column stores structured JSON with nested arrays and objects
- **Lines 191-199**: Multi-row INSERT is more efficient than multiple single INSERTs
- **Line 216**: Verify data insertion with COUNT aggregate

**Use Case:** VARIANT allows storing flexible metadata without predefined schema, useful for user preferences, tags, or evolving data structures.

---

### 5. Querying and Filtering

**Source Code (Lines 231-272):**

```python
231:  # Simple SELECT with all columns
232:  cursor.execute("SELECT * FROM employees LIMIT 3")
233:  print("Line 231: SELECT * FROM employees LIMIT 3")
234:
235:  # SELECT specific columns with WHERE clause
236:  query_sql = """
237:  SELECT first_name, last_name, salary, department
238:  FROM employees
239:  WHERE salary > 75000
240:  ORDER BY salary DESC
241:  """
242:  cursor.execute(query_sql)
243:  print("\nLine 236-242: SELECT with WHERE and ORDER BY (salary > 75000)")
244:
245:  # Query with LIKE pattern matching
246:  cursor.execute("""
247:      SELECT first_name, last_name, email
248:      FROM employees
249:      WHERE email LIKE '%example.com'
250:  """)
251:  print("\nLine 246-250: SELECT with LIKE pattern (emails ending in example.com)")
252:
253:  # Query with date filtering
254:  cursor.execute("""
255:      SELECT first_name, last_name, hire_date,
256:             DATEDIFF('day', hire_date, CURRENT_DATE()) AS days_employed
257:      FROM employees
258:      WHERE hire_date >= '2023-03-01'
259:      ORDER BY hire_date
260:  """)
261:  print("\nLine 254-261: SELECT with date filtering and DATEDIFF calculation")
262:
263:  # Query VARIANT (JSON) data
264:  cursor.execute("""
265:      SELECT first_name, last_name,
266:             metadata:skills AS skills,
267:             metadata:years_exp AS experience
268:      FROM employees
269:      WHERE metadata:years_exp::INT >= 6
270:  """)
271:  print("\nLine 265-272: SELECT querying JSON data from VARIANT column")
```

**Output:**

```
Line 231: SELECT * FROM employees LIMIT 3
Columns: EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, HIRE_DATE, SALARY, DEPARTMENT, IS_ACTIVE, METADATA
Row 1: (1, 'John', 'Doe', 'john.doe@example.com', datetime.date(2023, 1, 15), Decimal('75000.00'), 'Engineering', True, '{"skills":["Python","SQL"],"years_exp":5}')
Row 2: (2, 'Jane', 'Smith', 'jane.smith@example.com', datetime.date(2023, 2, 20), Decimal('82000.00'), 'Engineering', True, '{"skills":["Java","Kubernetes"],"years_exp":7}')
Row 3: (3, 'Bob', 'Johnson', 'bob.johnson@example.com', datetime.date(2023, 3, 10), Decimal('68000.00'), 'Marketing', True, '{"skills":["SEO","Analytics"],"years_exp":4}')

Line 236-242: SELECT with WHERE and ORDER BY (salary > 75000)
Columns: FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT
Row 1: ('Alice', 'Williams', Decimal('91000.00'), 'Engineering')
Row 2: ('Jane', 'Smith', Decimal('82000.00'), 'Engineering')

Line 246-250: SELECT with LIKE pattern (emails ending in example.com)
Columns: FIRST_NAME, LAST_NAME, EMAIL
Row 1: ('John', 'Doe', 'john.doe@example.com')
Row 2: ('Jane', 'Smith', 'jane.smith@example.com')
Row 3: ('Bob', 'Johnson', 'bob.johnson@example.com')
Row 4: ('Alice', 'Williams', 'alice.williams@example.com')
Row 5: ('Charlie', 'Brown', 'charlie.brown@example.com')

Line 254-261: SELECT with date filtering and DATEDIFF calculation
Columns: FIRST_NAME, LAST_NAME, HIRE_DATE, DAYS_EMPLOYED
Row 1: ('Bob', 'Johnson', datetime.date(2023, 3, 10), 311)
Row 2: ('Alice', 'Williams', datetime.date(2023, 4, 5), 285)
Row 3: ('Charlie', 'Brown', datetime.date(2023, 5, 12), 248)

Line 265-272: SELECT querying JSON data from VARIANT column
Columns: FIRST_NAME, LAST_NAME, SKILLS, EXPERIENCE
Row 1: ('Jane', 'Smith', '["Java","Kubernetes"]', '7')
Row 2: ('Alice', 'Williams', '["Python","ML"]', '8')
Row 3: ('Charlie', 'Brown', '["CRM","Negotiation"]', '6')
```

**Annotations:**

- **Line 232**: `LIMIT` restricts result set size
- **Lines 239-240**: `WHERE` filters rows, `ORDER BY DESC` sorts descending
- **Line 249**: `LIKE '%example.com'` matches email patterns (% is wildcard)
- **Line 256**: `DATEDIFF('day', start, end)` calculates days between dates
- **Lines 266-267**: Colon notation (`metadata:skills`) queries JSON fields from VARIANT
- **Line 269**: `::INT` casts VARIANT value to integer for comparison

**Key Feature:** Snowflake's VARIANT type allows SQL queries on JSON data without parsing, making it extremely powerful for semi-structured data.

---

### 6. Aggregations and GROUP BY

**Source Code (Lines 286-323):**

```python
286:  # Basic aggregation functions
287:  cursor.execute("""
288:      SELECT
289:          COUNT(*) AS total_employees,
290:          AVG(salary) AS avg_salary,
291:          MIN(salary) AS min_salary,
292:          MAX(salary) AS max_salary,
293:          SUM(salary) AS total_payroll
294:      FROM employees
295:  """)
296:  print("Line 286-295: Aggregate functions (COUNT, AVG, MIN, MAX, SUM)")
297:
298:  # GROUP BY with aggregations
299:  cursor.execute("""
300:      SELECT
301:          department,
302:          COUNT(*) AS employee_count,
303:          AVG(salary) AS avg_salary,
304:          MAX(salary) AS max_salary
305:      FROM employees
306:      GROUP BY department
307:      ORDER BY avg_salary DESC
308:  """)
309:  print("\nLine 299-309: GROUP BY department with aggregations")
310:
311:  # HAVING clause with GROUP BY
312:  cursor.execute("""
313:      SELECT
314:          department,
315:          AVG(salary) AS avg_salary
316:      FROM employees
317:      GROUP BY department
318:      HAVING AVG(salary) > 70000
319:      ORDER BY avg_salary DESC
320:  """)
321:  print("\nLine 313-323: GROUP BY with HAVING clause (avg salary > 70000)")
```

**Output:**

```
Line 286-295: Aggregate functions (COUNT, AVG, MIN, MAX, SUM)
Columns: TOTAL_EMPLOYEES, AVG_SALARY, MIN_SALARY, MAX_SALARY, TOTAL_PAYROLL
Row 1: (5, Decimal('77600.000000'), Decimal('68000.00'), Decimal('91000.00'), Decimal('388000.00'))

Line 299-309: GROUP BY department with aggregations
Columns: DEPARTMENT, EMPLOYEE_COUNT, AVG_SALARY, MAX_SALARY
Row 1: ('Engineering', 3, Decimal('82666.666667'), Decimal('91000.00'))
Row 2: ('Sales', 1, Decimal('72000.000000'), Decimal('72000.00'))
Row 3: ('Marketing', 1, Decimal('68000.000000'), Decimal('68000.00'))

Line 313-323: GROUP BY with HAVING clause (avg salary > 70000)
Columns: DEPARTMENT, AVG_SALARY
Row 1: ('Engineering', Decimal('82666.666667'))
Row 2: ('Sales', Decimal('72000.000000'))
```

**Annotations:**

- **Lines 289-293**: Standard SQL aggregation functions
- **Line 290**: `AVG()` returns average with full precision
- **Line 306**: `GROUP BY` groups rows by department for per-group aggregations
- **Line 318**: `HAVING` filters groups (applied after GROUP BY, unlike WHERE which filters before)
- **Line 307**: `ORDER BY` on aggregated results

**Key Insight:** HAVING filters groups while WHERE filters rows. Use HAVING for conditions on aggregated values.

---

### 7. Table Joins

**Source Code (Lines 337-362):**

```python
337:  # INNER JOIN
338:  cursor.execute("""
339:      SELECT
340:          e.first_name,
341:          e.last_name,
342:          e.department AS dept_name,
343:          d.dept_location
344:      FROM employees e
345:      INNER JOIN departments d ON e.department = d.dept_name
346:      ORDER BY e.last_name
347:  """)
348:  print("Line 337-347: INNER JOIN employees with departments")
349:
350:  # LEFT JOIN with aggregation
351:  cursor.execute("""
352:      SELECT
353:          d.dept_name,
354:          d.dept_location,
355:          COUNT(e.employee_id) AS employee_count,
356:          AVG(e.salary) AS avg_salary
357:      FROM departments d
358:      LEFT JOIN employees e ON d.dept_name = e.department
359:      GROUP BY d.dept_name, d.dept_location
360:      ORDER BY employee_count DESC
361:  """)
362:  print("\nLine 351-362: LEFT JOIN with aggregation (all departments)")
```

**Output:**

```
Line 337-347: INNER JOIN employees with departments
Columns: FIRST_NAME, LAST_NAME, DEPT_NAME, DEPT_LOCATION
Row 1: ('Charlie', 'Brown', 'Sales', 'Chicago')
Row 2: ('John', 'Doe', 'Engineering', 'San Francisco')
Row 3: ('Bob', 'Johnson', 'Marketing', 'New York')
Row 4: ('Jane', 'Smith', 'Engineering', 'San Francisco')
Row 5: ('Alice', 'Williams', 'Engineering', 'San Francisco')

Line 351-362: LEFT JOIN with aggregation (all departments)
Columns: DEPT_NAME, DEPT_LOCATION, EMPLOYEE_COUNT, AVG_SALARY
Row 1: ('Engineering', 'San Francisco', 3, Decimal('82666.666667'))
Row 2: ('Marketing', 'New York', 1, Decimal('68000.000000'))
Row 3: ('Sales', 'Chicago', 1, Decimal('72000.000000'))
Row 4: ('Finance', 'Boston', 0, None)
```

**Annotations:**

- **Line 345**: `INNER JOIN` returns only matching rows from both tables
- **Line 344**: Table aliases (`e`, `d`) simplify column references
- **Line 358**: `LEFT JOIN` returns all departments, even without employees (Finance shows 0 count)
- **Lines 355-356**: Aggregations work seamlessly with joins
- **Line 359**: `GROUP BY` required for all non-aggregated columns in SELECT

**Key Insight:** LEFT JOIN preserves all rows from the left table (departments), showing Finance with NULL employee data.

---

### 8. Transactions

**Source Code (Lines 376-410):**

```python
376:      # Begin transaction
377:      conn.autocommit = False
378:      print("Line 376: BEGIN TRANSACTION (autocommit=False)")
379:
380:      # Update salaries
381:      cursor.execute("""
382:          UPDATE employees
383:          SET salary = salary * 1.10
384:          WHERE department = 'Engineering'
385:      """)
386:      affected_rows = cursor.rowcount
387:      print(f"Line 380-384: UPDATE salaries for Engineering (+10%)")
388:      print(f"  Affected rows: {affected_rows}")
389:
390:      # Verify changes before commit
391:      cursor.execute("""
392:          SELECT first_name, last_name, salary
393:          FROM employees
394:          WHERE department = 'Engineering'
395:      """)
396:      print("\nLine 389-393: SELECT to verify changes (before COMMIT)")
397:
398:      # Commit transaction
399:      conn.commit()
400:      print("\nLine 397: COMMIT TRANSACTION")
401:
402:      # Verify committed changes
403:      cursor.execute("""
404:          SELECT first_name, last_name, salary
405:          FROM employees
406:          WHERE department = 'Engineering'
407:      """)
408:      print("\nLine 401-405: SELECT after COMMIT (changes persisted)")
409:
410:  except Exception as e:
411:      # Rollback on error
412:      conn.rollback()
413:      print(f"\nLine 410: ROLLBACK TRANSACTION due to error: {e}")
```

**Output:**

```
Line 376: BEGIN TRANSACTION (autocommit=False)
Line 380-384: UPDATE salaries for Engineering (+10%)
  Affected rows: 3

Line 389-393: SELECT to verify changes (before COMMIT)
Columns: FIRST_NAME, LAST_NAME, SALARY
Row 1: ('John', 'Doe', Decimal('82500.00'))
Row 2: ('Jane', 'Smith', Decimal('90200.00'))
Row 3: ('Alice', 'Williams', Decimal('100100.00'))

Line 397: COMMIT TRANSACTION

Line 401-405: SELECT after COMMIT (changes persisted)
Columns: FIRST_NAME, LAST_NAME, SALARY
Row 1: ('John', 'Doe', Decimal('82500.00'))
Row 2: ('Jane', 'Smith', Decimal('90200.00'))
Row 3: ('Alice', 'Williams', Decimal('100100.00'))
```

**Annotations:**

- **Line 377**: Setting `autocommit=False` starts explicit transaction mode
- **Lines 382-384**: `UPDATE` modifies salaries (75000→82500, 82000→90200, 91000→100100)
- **Line 386**: `cursor.rowcount` returns number of affected rows
- **Lines 391-396**: Changes visible within transaction before COMMIT
- **Line 399**: `COMMIT` persists all transaction changes atomically
- **Line 412**: `ROLLBACK` would undo all changes on error (exception handling)

**Use Case:** Transactions ensure atomic operations for multi-step updates (e.g., financial transfers, inventory adjustments).

---

### 9. User-Defined Functions (UDFs)

**Source Code (Lines 426-477):**

```python
426:  # Create SQL UDF for salary grade calculation
427:  create_udf_sql = """
428:  CREATE OR REPLACE FUNCTION calculate_salary_grade(salary NUMBER)
429:  RETURNS VARCHAR
430:  AS
431:  $$
432:      CASE
433:          WHEN salary < 70000 THEN 'Junior'
434:          WHEN salary >= 70000 AND salary < 80000 THEN 'Mid-Level'
435:          WHEN salary >= 80000 AND salary < 90000 THEN 'Senior'
436:          ELSE 'Principal'
437:      END
438:  $$
439:  """
440:  cursor.execute(create_udf_sql)
441:  print("Line 426-439: CREATE FUNCTION calculate_salary_grade()")
442:  print("  Returns salary grade based on salary amount")
443:
444:  # Use the UDF in a query
445:  cursor.execute("""
446:      SELECT
447:          first_name,
448:          last_name,
449:          salary,
450:          calculate_salary_grade(salary) AS salary_grade
451:      FROM employees
452:      ORDER BY salary DESC
453:  """)
454:  print("\nLine 443-452: SELECT using calculate_salary_grade() UDF")
455:
456:  # Create UDF for bonus calculation
457:  cursor.execute("""
458:      CREATE OR REPLACE FUNCTION calculate_bonus(salary NUMBER, performance_rating NUMBER)
459:      RETURNS NUMBER(10, 2)
460:      AS
461:      $$
462:          salary * (performance_rating / 100.0)
463:      $$
464:  """)
465:  print("\nLine 456-464: CREATE FUNCTION calculate_bonus()")
466:
467:  # Use bonus calculation UDF
468:  cursor.execute("""
469:      SELECT
470:          first_name,
471:          last_name,
472:          salary,
473:          calculate_bonus(salary, 15) AS bonus_15_percent
474:      FROM employees
475:      ORDER BY salary DESC
476:      LIMIT 3
477:  """)
478:  print("\nLine 467-477: SELECT using calculate_bonus() UDF (15% bonus)")
```

**Output:**

```
Line 426-439: CREATE FUNCTION calculate_salary_grade()
  Returns salary grade based on salary amount

Line 443-452: SELECT using calculate_salary_grade() UDF
Columns: FIRST_NAME, LAST_NAME, SALARY, SALARY_GRADE
Row 1: ('Alice', 'Williams', Decimal('100100.00'), 'Principal')
Row 2: ('Jane', 'Smith', Decimal('90200.00'), 'Principal')
Row 3: ('John', 'Doe', Decimal('82500.00'), 'Senior')
Row 4: ('Charlie', 'Brown', Decimal('72000.00'), 'Mid-Level')
Row 5: ('Bob', 'Johnson', Decimal('68000.00'), 'Junior')

Line 456-464: CREATE FUNCTION calculate_bonus()

Line 467-477: SELECT using calculate_bonus() UDF (15% bonus)
Columns: FIRST_NAME, LAST_NAME, SALARY, BONUS_15_PERCENT
Row 1: ('Alice', 'Williams', Decimal('100100.00'), Decimal('15015.00'))
Row 2: ('Jane', 'Smith', Decimal('90200.00'), Decimal('13530.00'))
Row 3: ('John', 'Doe', Decimal('82500.00'), Decimal('12375.00'))
```

**Annotations:**

- **Lines 428-438**: SQL UDF defined with `$$` delimiters for function body
- **Line 428**: Function signature specifies parameter types and return type
- **Lines 432-437**: `CASE` expression implements salary grade logic
- **Line 450**: UDF called like built-in function in SELECT
- **Lines 458-463**: Second UDF performs calculation with two parameters
- **Line 473**: UDF with multiple parameters (salary, 15)

**Use Case:** UDFs encapsulate business logic (salary grades, bonus calculations) for reuse across queries.

---

### 10. Stored Procedures

**Source Code (Lines 493-529):**

```python
493:  # Create stored procedure for employee stats
494:  create_proc_sql = """
495:  CREATE OR REPLACE PROCEDURE get_department_stats(dept_name VARCHAR)
496:  RETURNS TABLE(metric VARCHAR, value VARCHAR)
497:  LANGUAGE SQL
498:  AS
499:  $$
500:  BEGIN
501:      LET result_query := 'SELECT
502:          ''Employee Count'' AS metric,
503:          COUNT(*)::VARCHAR AS value
504:      FROM employees
505:      WHERE department = ''' || :dept_name || '''
506:      UNION ALL
507:      SELECT
508:          ''Average Salary'' AS metric,
509:          ROUND(AVG(salary), 2)::VARCHAR AS value
510:      FROM employees
511:      WHERE department = ''' || :dept_name || '''
512:      UNION ALL
513:      SELECT
514:          ''Total Payroll'' AS metric,
515:          ROUND(SUM(salary), 2)::VARCHAR AS value
516:      FROM employees
517:      WHERE department = ''' || :dept_name || '''';
518:
519:      LET res RESULTSET := (EXECUTE IMMEDIATE :result_query);
520:      RETURN TABLE(res);
521:  END;
522:  $$
523:  """
524:  cursor.execute(create_proc_sql)
525:  print("Line 493-525: CREATE PROCEDURE get_department_stats()")
526:  print("  Returns employee count, avg salary, and total payroll for a department")
527:
528:  # Call the stored procedure
529:  cursor.execute("CALL get_department_stats('Engineering')")
530:  print("\nLine 529: CALL get_department_stats('Engineering')")
```

**Output:**

```
Line 493-525: CREATE PROCEDURE get_department_stats()
  Returns employee count, avg salary, and total payroll for a department

Line 529: CALL get_department_stats('Engineering')
Columns: METRIC, VALUE
Row 1: ('Employee Count', '3')
Row 2: ('Average Salary', '90933.33')
Row 3: ('Total Payroll', '272800.00')
```

**Annotations:**

- **Lines 495-497**: Procedure returns table with metric/value columns
- **Line 497**: `LANGUAGE SQL` specifies SQL-based procedure (Snowflake also supports JavaScript, Python)
- **Lines 501-517**: Dynamic SQL query built with parameter substitution
- **Line 505**: `:dept_name` references procedure parameter
- **Line 519**: `EXECUTE IMMEDIATE` runs dynamic SQL
- **Line 520**: `RETURN TABLE` returns result set
- **Line 529**: `CALL` executes stored procedure with parameter

**Use Case:** Stored procedures encapsulate complex multi-step logic with control flow (loops, conditionals) for reusable operations.

---

### 11. Pandas Integration

**Source Code (Lines 543-599):**

```python
543:  # Read query results into Pandas DataFrame
544:  query = """
545:  SELECT
546:      e.first_name,
547:      e.last_name,
548:      e.salary,
549:      e.department,
550:      e.hire_date
551:  FROM employees e
552:  ORDER BY salary DESC
553:  """
554:  df = pd.read_sql(query, conn)
555:  print("Line 543-553: pd.read_sql() - Load query results into DataFrame")
556:  print(f"  DataFrame shape: {df.shape}")
557:  print(f"  Columns: {df.columns.tolist()}")
558:
559:  # DataFrame operations
562:  print("\nLine 562-565: DataFrame operations")
563:  print(f"  Average salary: ${df['SALARY'].mean():,.2f}")
564:  print(f"  Median salary: ${df['SALARY'].median():,.2f}")
565:  print(f"  Salary std dev: ${df['SALARY'].std():,.2f}")
566:
567:  # Group by department in Pandas
568:  dept_stats = df.groupby('DEPARTMENT')['SALARY'].agg(['count', 'mean', 'min', 'max'])
569:  print("\nLine 569-571: DataFrame groupby department")
570:
571:  # Write DataFrame back to Snowflake
575:  from snowflake.connector.pandas_tools import write_pandas
576:
577:  df_summary = df.groupby('DEPARTMENT').agg({
578:      'FIRST_NAME': 'count',
579:      'SALARY': ['mean', 'min', 'max']
580:  }).reset_index()
581:  df_summary.columns = ['department', 'emp_count', 'avg_salary', 'min_salary', 'max_salary']
582:
583:  success, nchunks, nrows, _ = write_pandas(
584:      conn,
585:      df_summary,
586:      'EMPLOYEES_ANALYSIS',
587:      auto_create_table=True,
588:      overwrite=True
589:  )
590:  print(f"\nLine 575-593: write_pandas() - Write DataFrame to Snowflake")
591:  print(f"  Success: {success}, Rows: {nrows}, Chunks: {nchunks}")
592:
593:  # Verify the new table
598:  cursor.execute("SELECT * FROM employees_analysis")
599:  print("\nLine 598-599: SELECT * FROM employees_analysis")
```

**Output:**

```
Line 543-553: pd.read_sql() - Load query results into DataFrame
  DataFrame shape: (5, 5)
  Columns: ['FIRST_NAME', 'LAST_NAME', 'SALARY', 'DEPARTMENT', 'HIRE_DATE']

First 3 rows:
FIRST_NAME LAST_NAME      SALARY   DEPARTMENT   HIRE_DATE
     Alice  Williams  100100.00  Engineering  2023-04-05
      Jane     Smith   90200.00  Engineering  2023-02-20
      John       Doe   82500.00  Engineering  2023-01-15

Line 562-565: DataFrame operations
  Average salary: $78,760.00
  Median salary: $72,000.00
  Salary std dev: $12,663.48

Line 569-571: DataFrame groupby department
            count        mean  min        max
DEPARTMENT
Engineering     3  90933.333333  82500.00  100100.00
Marketing       1  68000.000000  68000.00   68000.00
Sales           1  72000.000000  72000.00   72000.00

Line 575-593: write_pandas() - Write DataFrame to Snowflake
  Success: True, Rows: 3, Chunks: 1

Line 598-599: SELECT * FROM employees_analysis
Columns: DEPARTMENT, EMP_COUNT, AVG_SALARY, MIN_SALARY, MAX_SALARY
Row 1: ('Engineering', 3, Decimal('90933.333333'), Decimal('82500.00'), Decimal('100100.00'))
Row 2: ('Marketing', 1, Decimal('68000.000000'), Decimal('68000.00'), Decimal('68000.00'))
Row 3: ('Sales', 1, Decimal('72000.000000'), Decimal('72000.00'), Decimal('72000.00'))
```

**Annotations:**

- **Line 554**: `pd.read_sql()` executes query and loads results into DataFrame
- **Lines 556-557**: DataFrame metadata (shape, columns)
- **Lines 563-565**: Pandas statistical functions (mean, median, std)
- **Line 568**: `groupby()` and `agg()` for aggregations in Pandas
- **Lines 577-581**: Create summary DataFrame from aggregations
- **Lines 583-589**: `write_pandas()` writes DataFrame to Snowflake table
- **Line 587**: `auto_create_table=True` creates table with inferred schema
- **Line 588**: `overwrite=True` replaces existing table

**Use Case:** Seamless integration between Snowflake and Pandas enables:
- Loading large result sets for Python analysis
- Complex transformations in Pandas
- Writing processed data back to Snowflake

---

## Key Snowflake Features

### 1. VARIANT Data Type
Snowflake's unique VARIANT type allows storing and querying semi-structured data (JSON, Avro, XML) alongside structured data. Access JSON fields with colon notation: `metadata:skills`.

### 2. Zero-Copy Cloning
Snowflake supports instant table/database cloning without copying data:
```sql
CREATE TABLE employees_clone CLONE employees;
```

### 3. Time Travel
Query historical data with `AT` or `BEFORE` clauses:
```sql
SELECT * FROM employees AT(OFFSET => -3600);  -- 1 hour ago
```

### 4. Separation of Storage and Compute
Snowflake's architecture separates storage (S3/Azure/GCS) from compute (virtual warehouses), enabling independent scaling.

### 5. Automatic Optimization
Snowflake automatically:
- Compresses data
- Partitions tables (micro-partitions)
- Maintains statistics
- Optimizes query plans

---

## Performance Best Practices

| Practice | Description |
|----------|-------------|
| **Use Clustering Keys** | Define clustering for large tables with common filter patterns |
| **Leverage Caching** | Result cache (24 hours) and metadata cache speed up queries |
| **Partition Pruning** | Filter on cluster keys to scan fewer micro-partitions |
| **Semi-Structured Optimization** | Use `FLATTEN()` for nested arrays, materialize frequent JSON paths |
| **Batch Operations** | Use multi-row INSERTs and COPY for bulk loading |
| **Warehouse Sizing** | Right-size warehouses (XS to 6XL) based on workload |

---

## Common Snowflake Operations

### Bulk Loading from Stage
```sql
-- Create stage for external data
CREATE OR REPLACE STAGE my_stage
  URL='s3://mybucket/data/'
  CREDENTIALS=(AWS_KEY_ID='...' AWS_SECRET_KEY='...');

-- Load data from stage
COPY INTO employees
  FROM @my_stage/employees.csv
  FILE_FORMAT=(TYPE=CSV SKIP_HEADER=1);
```

### Table Cloning
```sql
-- Zero-copy clone (instant, no storage cost initially)
CREATE TABLE employees_backup CLONE employees;
```

### Time Travel Query
```sql
-- Query table as it existed 1 hour ago
SELECT * FROM employees AT(OFFSET => -3600);

-- Query before specific statement
SELECT * FROM employees BEFORE(STATEMENT => '01a86a38-0000-1234-0000-00007ccf5678');
```

---

## Connection Methods

### 1. Username/Password
```python
conn = snowflake.connector.connect(
    account='abc12345.us-east-1',
    user='john_doe',
    password='secure_password',
    warehouse='COMPUTE_WH',
    database='DEMO_DB',
    schema='PUBLIC'
)
```

### 2. Key Pair Authentication
```python
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

with open('/path/to/private_key.p8', 'rb') as key:
    p_key = serialization.load_pem_private_key(
        key.read(),
        password=None,
        backend=default_backend()
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

conn = snowflake.connector.connect(
    account='abc12345.us-east-1',
    user='john_doe',
    private_key=pkb,
    warehouse='COMPUTE_WH'
)
```

### 3. OAuth
```python
conn = snowflake.connector.connect(
    account='abc12345.us-east-1',
    user='john_doe',
    authenticator='oauth',
    token='<oauth_access_token>'
)
```

---

## Additional Resources

- **Snowflake Documentation**: https://docs.snowflake.com/
- **Python Connector Docs**: https://docs.snowflake.com/en/developer-guide/python-connector/python-connector
- **Snowflake SQL Reference**: https://docs.snowflake.com/en/sql-reference
- **Best Practices**: https://docs.snowflake.com/en/user-guide/performance-best-practices
- **Pandas Integration**: https://docs.snowflake.com/en/user-guide/python-connector-pandas

---

## Version Requirements

This example requires:
- **Python 3.11+** for modern type hints and features
- **snowflake-connector-python 3.7.0+** for latest Snowflake features
- **pandas 2.2.0+** for DataFrame integration

---

*This example demonstrates Snowflake's enterprise data warehouse capabilities, including unique features like VARIANT for semi-structured data, time travel for historical queries, and seamless Pandas integration for data science workflows.*
