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
