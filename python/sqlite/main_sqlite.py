#!/usr/bin/env python3
"""
SQLite Database Operations Demo

This script demonstrates:
1. Database creation
2. Table initialization
3. Data insertion and querying
4. Table dropping
"""

import sqlite3
import os
from pathlib import Path


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print(f"{'=' * 60}\n")


def main() -> None:
    """Main function demonstrating SQLite operations."""

    # Define database path
    db_path = Path("demo.db")

    # Remove existing database file if it exists
    if db_path.exists():
        os.remove(db_path)
        print(f"Removed existing database: {db_path}")

    # SECTION 1: Database Creation
    print_section("1. DATABASE CREATION")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print(f"✓ Database created: {db_path}")
    print("✓ Connection established")

    # SECTION 2: Table Initialization
    print_section("2. TABLE INITIALIZATION")

    # Create users table
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("✓ Created table: users")
    print("  Columns: id, username, email, age, created_at")

    # Create products table
    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER DEFAULT 0
        )
    """)
    print("✓ Created table: products")
    print("  Columns: id, name, price, stock")

    conn.commit()

    # SECTION 3: Data Insertion
    print_section("3. DATA INSERTION")

    # Insert users
    users_data = [
        ("alice", "alice@example.com", 28),
        ("bob", "bob@example.com", 34),
        ("charlie", "charlie@example.com", 22),
    ]

    cursor.executemany(
        "INSERT INTO users (username, email, age) VALUES (?, ?, ?)", users_data
    )
    print(f"✓ Inserted {cursor.rowcount} users")

    # Insert products
    products_data = [
        ("Laptop", 999.99, 15),
        ("Mouse", 29.99, 50),
        ("Keyboard", 79.99, 30),
    ]

    cursor.executemany(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", products_data
    )
    print(f"✓ Inserted {cursor.rowcount} products")

    conn.commit()

    # SECTION 4: Data Querying
    print_section("4. DATA QUERYING")

    # Query all users
    print("Users table:")
    cursor.execute("SELECT id, username, email, age FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(f"  ID: {row[0]}, Username: {row[1]}, Email: {row[2]}, Age: {row[3]}")

    print("\nProducts table:")
    cursor.execute("SELECT id, name, price, stock FROM products")
    rows = cursor.fetchall()
    for row in rows:
        print(f"  ID: {row[0]}, Name: {row[1]}, Price: ${row[2]:.2f}, Stock: {row[3]}")

    # SECTION 5: List All Tables
    print_section("5. LIST ALL TABLES")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        print(f"  • {table[0]}")

    # SECTION 6: Table Schema
    print_section("6. TABLE SCHEMA")
    cursor.execute("PRAGMA table_info(users)")
    columns = cursor.fetchall()
    print("Users table schema:")
    for col in columns:
        print(f"  {col[1]} ({col[2]}) - PK: {bool(col[5])}, NOT NULL: {bool(col[3])}")

    # SECTION 7: Dropping Tables
    print_section("7. DROPPING TABLES")

    # Drop products table
    cursor.execute("DROP TABLE products")
    print("✓ Dropped table: products")

    # Verify tables after drop
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("\nRemaining tables:")
    for table in tables:
        print(f"  • {table[0]}")

    # Drop users table
    cursor.execute("DROP TABLE users")
    print("\n✓ Dropped table: users")

    # Verify all tables dropped
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    if not tables:
        print("\n✓ All tables dropped successfully")

    # SECTION 8: Cleanup
    print_section("8. CLEANUP")
    cursor.close()
    conn.close()
    print("✓ Database connection closed")

    # Remove database file
    if db_path.exists():
        os.remove(db_path)
        print(f"✓ Database file removed: {db_path}")

    print("\n" + "=" * 60)
    print("SQLite Demo Completed Successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
