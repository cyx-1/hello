# SQLite Database Operations in Python

This example demonstrates comprehensive SQLite database usage in Python, including database creation, table initialization, data manipulation, and table dropping.

## Running the Program

```bash
uv run python main_sqlite.py
```

## Key Features Demonstrated

1. **Database Creation** - Creating a SQLite database file
2. **Table Initialization** - Creating tables with various column types and constraints
3. **Data Insertion** - Adding records using parameterized queries
4. **Data Querying** - Retrieving and displaying data
5. **Schema Inspection** - Viewing table structure and metadata
6. **Table Dropping** - Removing tables from the database
7. **Resource Cleanup** - Properly closing connections and removing database files

## Source Code Breakdown

### 1. Database Creation (Lines 37-40)

```python
conn = sqlite3.connect(db_path)  # Line 37
cursor = conn.cursor()           # Line 38
```

**Output:**
```
============================================================
1. DATABASE CREATION
============================================================

✓ Database created: demo.db
✓ Connection established
```

**Annotation:** Line 37 creates a new SQLite database file named `demo.db`. If the file doesn't exist, SQLite creates it automatically. Line 38 creates a cursor object to execute SQL commands.

---

### 2. Table Initialization (Lines 46-66)

**Users Table Creation (Lines 46-54):**
```python
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
```

**Products Table Creation (Lines 59-66):**
```python
cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER DEFAULT 0
    )
""")
```

**Output:**
```
============================================================
2. TABLE INITIALIZATION
============================================================

✓ Created table: users
  Columns: id, username, email, age, created_at
✓ Created table: products
  Columns: id, name, price, stock
```

**Annotation:** Line 46 creates the `users` table with an auto-incrementing primary key, NOT NULL constraints, and a UNIQUE constraint on username. Line 59 creates the `products` table with similar structure. Line 70 commits these changes to the database.

---

### 3. Data Insertion (Lines 76-97)

**Bulk Insert with executemany (Lines 82-84):**
```python
cursor.executemany(
    "INSERT INTO users (username, email, age) VALUES (?, ?, ?)", users_data
)
```

**Output:**
```
============================================================
3. DATA INSERTION
============================================================

✓ Inserted 3 users
✓ Inserted 3 products
```

**Annotation:** Line 82-84 demonstrates parameterized queries using `executemany()` for efficient bulk insertion. The `?` placeholders prevent SQL injection attacks. Line 85 shows `cursor.rowcount` which returns the number of rows affected by the last operation.

---

### 4. Data Querying (Lines 106-115)

**SELECT Query (Lines 106-109):**
```python
cursor.execute("SELECT id, username, email, age FROM users")
rows = cursor.fetchall()
for row in rows:
    print(f"  ID: {row[0]}, Username: {row[1]}, Email: {row[2]}, Age: {row[3]}")
```

**Output:**
```
============================================================
4. DATA QUERYING
============================================================

Users table:
  ID: 1, Username: alice, Email: alice@example.com, Age: 28
  ID: 2, Username: bob, Email: bob@example.com, Age: 34
  ID: 3, Username: charlie, Email: charlie@example.com, Age: 22

Products table:
  ID: 1, Name: Laptop, Price: $999.99, Stock: 15
  ID: 2, Name: Mouse, Price: $29.99, Stock: 50
  ID: 3, Name: Keyboard, Price: $79.99, Stock: 30
```

**Annotation:** Line 106 executes a SELECT query. Line 107 uses `fetchall()` to retrieve all matching rows as a list of tuples. Lines 108-109 iterate through the results and display each record.

---

### 5. Listing Tables (Lines 119-123)

**Query sqlite_master (Line 119):**
```python
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
```

**Output:**
```
============================================================
5. LIST ALL TABLES
============================================================

Tables in database:
  • users
  • sqlite_sequence
  • products
```

**Annotation:** Line 119 queries the `sqlite_master` system table, which contains metadata about all database objects. The `sqlite_sequence` table is automatically created by SQLite to track AUTOINCREMENT values.

---

### 6. Table Schema Inspection (Lines 127-131)

**PRAGMA table_info (Line 127):**
```python
cursor.execute("PRAGMA table_info(users)")
```

**Output:**
```
============================================================
6. TABLE SCHEMA
============================================================

Users table schema:
  id (INTEGER) - PK: True, NOT NULL: False
  username (TEXT) - PK: False, NOT NULL: True
  email (TEXT) - PK: False, NOT NULL: True
  age (INTEGER) - PK: False, NOT NULL: False
  created_at (TIMESTAMP) - PK: False, NOT NULL: False
```

**Annotation:** Line 127 uses `PRAGMA table_info()` to retrieve detailed column information. The result includes column name (col[1]), data type (col[2]), NOT NULL constraint (col[3]), and primary key status (col[5]).

---

### 7. Dropping Tables (Lines 137-149)

**DROP TABLE Command (Lines 137, 148):**
```python
cursor.execute("DROP TABLE products")  # Line 137
# ... verify tables ...
cursor.execute("DROP TABLE users")     # Line 148
```

**Output:**
```
============================================================
7. DROPPING TABLES
============================================================

✓ Dropped table: products

Remaining tables:
  • users
  • sqlite_sequence

✓ Dropped table: users

✓ All tables dropped successfully
```

**Annotation:** Line 137 drops the `products` table from the database. Line 141-145 verifies which tables remain. Line 148 drops the `users` table. Lines 152-155 confirm that all tables have been successfully removed.

---

### 8. Cleanup (Lines 159-166)

**Closing Connections (Lines 159-160):**
```python
cursor.close()  # Line 159
conn.close()    # Line 160
```

**Output:**
```
============================================================
8. CLEANUP
============================================================

✓ Database connection closed
✓ Database file removed: demo.db

============================================================
SQLite Demo Completed Successfully!
============================================================
```

**Annotation:** Line 159 closes the cursor object. Line 160 closes the database connection, releasing all resources. Lines 164-166 remove the database file from disk for cleanup.

---

## Important SQLite Concepts Illustrated

### Parameterized Queries
The code uses `?` placeholders (lines 83, 95) instead of string formatting to prevent SQL injection attacks:

```python
cursor.executemany(
    "INSERT INTO users (username, email, age) VALUES (?, ?, ?)", users_data
)
```

### Transaction Management
Changes are committed to disk using `conn.commit()` (lines 70, 99). Without commit, changes remain in memory and are lost when the connection closes.

### Data Types
SQLite supports several storage classes:
- **INTEGER** - whole numbers (lines 48, 51, 61, 64)
- **TEXT** - text strings (lines 49, 50, 62)
- **REAL** - floating point numbers (line 63)
- **TIMESTAMP** - date/time values (line 52)

### Constraints
- **PRIMARY KEY** - uniquely identifies each row (lines 48, 61)
- **AUTOINCREMENT** - automatically generates unique IDs (lines 48, 61)
- **NOT NULL** - prevents NULL values (lines 49, 50, 62, 63)
- **UNIQUE** - ensures no duplicate values (line 49)
- **DEFAULT** - provides default values (lines 52, 64)

### System Tables
- **sqlite_master** - contains schema information for all tables, indexes, and views
- **sqlite_sequence** - tracks the largest ROWID for AUTOINCREMENT columns

## Version Requirements

- **Python**: 3.x (sqlite3 is included in Python's standard library)
- **SQLite**: No minimum version required (uses standard SQL features)

No external dependencies are needed - SQLite is built into Python's standard library.

## Complete Program Output

```
============================================================
1. DATABASE CREATION
============================================================

✓ Database created: demo.db
✓ Connection established

============================================================
2. TABLE INITIALIZATION
============================================================

✓ Created table: users
  Columns: id, username, email, age, created_at
✓ Created table: products
  Columns: id, name, price, stock

============================================================
3. DATA INSERTION
============================================================

✓ Inserted 3 users
✓ Inserted 3 products

============================================================
4. DATA QUERYING
============================================================

Users table:
  ID: 1, Username: alice, Email: alice@example.com, Age: 28
  ID: 2, Username: bob, Email: bob@example.com, Age: 34
  ID: 3, Username: charlie, Email: charlie@example.com, Age: 22

Products table:
  ID: 1, Name: Laptop, Price: $999.99, Stock: 15
  ID: 2, Name: Mouse, Price: $29.99, Stock: 50
  ID: 3, Name: Keyboard, Price: $79.99, Stock: 30

============================================================
5. LIST ALL TABLES
============================================================

Tables in database:
  • users
  • sqlite_sequence
  • products

============================================================
6. TABLE SCHEMA
============================================================

Users table schema:
  id (INTEGER) - PK: True, NOT NULL: False
  username (TEXT) - PK: False, NOT NULL: True
  email (TEXT) - PK: False, NOT NULL: True
  age (INTEGER) - PK: False, NOT NULL: False
  created_at (TIMESTAMP) - PK: False, NOT NULL: False

============================================================
7. DROPPING TABLES
============================================================

✓ Dropped table: products

Remaining tables:
  • users
  • sqlite_sequence

✓ Dropped table: users

============================================================
8. CLEANUP
============================================================

✓ Database connection closed
✓ Database file removed: demo.db

============================================================
SQLite Demo Completed Successfully!
============================================================
```
