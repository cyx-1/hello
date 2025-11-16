# SQLite Memory Store Demo

A minimal demonstration of capturing and recalling memories using plain SQL with SQLite.

## Key Source Code

```python
#!/usr/bin/env python3
# /// script
# dependencies = []
# ///
"""Minimal SQLite memory store - capture and recall memories with plain SQL."""
import sqlite3

# Line 9: Create in-memory database and cursor
db = sqlite3.connect(":memory:")
cur = db.cursor()

# Line 12-16: Create memories table with timestamp
cur.execute("""
    CREATE TABLE memories (
        id INTEGER PRIMARY KEY,
        key TEXT UNIQUE,
        value TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Line 20-23: Store memories using plain SQL INSERT
memories = [("user_name", "Alice"), ("favorite_color", "blue"), ("last_topic", "SQLite")]
for key, value in memories:
    cur.execute("INSERT INTO memories (key, value) VALUES (?, ?)", (key, value))
    print(f"Stored: {key} = {value}")

# Line 26-28: Recall a specific memory
cur.execute("SELECT value FROM memories WHERE key = ?", ("user_name",))
print(f"\nRecalled user_name: {cur.fetchone()[0]}")

# Line 30-32: Update a memory
cur.execute("UPDATE memories SET value = ? WHERE key = ?", ("green", "favorite_color"))
print("Updated favorite_color to green")

# Line 34-36: List all memories with timestamps
print("\nAll memories:")
for row in cur.execute("SELECT key, value, created_at FROM memories ORDER BY id"):
    print(f"  {row[0]}: {row[1]} (stored at {row[2]})")

# Line 39-41: Search memories by pattern
cur.execute("SELECT key, value FROM memories WHERE key LIKE ?", ("%color%",))
print(f"\nMemories matching 'color': {cur.fetchall()}")

# Line 43: Cleanup
db.close()
```

## Program Output

```
1   Stored: user_name = Alice
2   Stored: favorite_color = blue
3   Stored: last_topic = SQLite
4
5   Recalled user_name: Alice
6   Updated favorite_color to green
7
8   All memories:
9     user_name: Alice (stored at 2025-11-16 11:48:56)
10    favorite_color: green (stored at 2025-11-16 11:48:56)
11    last_topic: SQLite (stored at 2025-11-16 11:48:56)
12
13  Memories matching 'color': [('favorite_color', 'green')]
```

## Annotations

### Source Code to Output Correlation

- **Lines 20-23 (INSERT)** → Output lines 1-3: Each `INSERT` statement stores a key-value pair and prints confirmation
- **Lines 26-28 (SELECT)** → Output line 5: Retrieves single value by exact key match
- **Lines 30-32 (UPDATE)** → Output line 6: Modifies existing memory value in place
- **Lines 34-36 (SELECT all)** → Output lines 8-11: Iterates all rows showing automatic timestamp capture
- **Lines 39-41 (LIKE pattern)** → Output line 13: SQL pattern matching for memory search

### Key Concepts Demonstrated

1. **Zero Dependencies**: Uses only Python's built-in `sqlite3` module (line 2: empty dependencies)
2. **In-Memory Database**: `:memory:` creates ephemeral database (line 9)
3. **Automatic Timestamps**: `DEFAULT CURRENT_TIMESTAMP` records when memories were stored (line 16)
4. **CRUD Operations**: Create (INSERT), Read (SELECT), Update (UPDATE) - all in plain SQL
5. **Parameterized Queries**: `?` placeholders prevent SQL injection (lines 22, 27, 31, 40)
6. **Pattern Search**: SQL `LIKE` with wildcards enables flexible memory retrieval (line 40)

## Requirements

- Python 3.6+ (sqlite3 is included in standard library)
- No external dependencies required
