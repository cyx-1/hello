#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "datasette",
#     "sqlite-utils",
#     "pandas>=2.0",
# ]
# ///
"""
Datasette Data Analysis Example

This script demonstrates how to use Datasette to analyze data:
1. Create a SQLite database with sample data
2. Use sqlite-utils to insert and query data
3. Launch Datasette to explore and analyze the data through its web interface
"""

import tempfile
from pathlib import Path

from sqlite_utils import Database


def create_sample_data():
    """Create a temporary SQLite database with sample sales data."""
    # Create a temporary database file
    db_path = Path(tempfile.gettempdir()) / "sales_analysis.db"

    # Initialize database with sqlite-utils
    db = Database(db_path)

    # Sample sales data
    sales_data = [
        {"id": 1, "product": "Laptop", "category": "Electronics", "price": 999.99, "quantity": 5, "region": "North"},
        {"id": 2, "product": "Mouse", "category": "Electronics", "price": 29.99, "quantity": 50, "region": "North"},
        {"id": 3, "product": "Keyboard", "category": "Electronics", "price": 79.99, "quantity": 30, "region": "South"},
        {"id": 4, "product": "Monitor", "category": "Electronics", "price": 299.99, "quantity": 15, "region": "East"},
        {"id": 5, "product": "Desk Chair", "category": "Furniture", "price": 199.99, "quantity": 20, "region": "West"},
        {"id": 6, "product": "Desk", "category": "Furniture", "price": 399.99, "quantity": 10, "region": "North"},
        {"id": 7, "product": "Lamp", "category": "Furniture", "price": 49.99, "quantity": 40, "region": "South"},
        {"id": 8, "product": "Notebook", "category": "Stationery", "price": 4.99, "quantity": 200, "region": "East"},
        {"id": 9, "product": "Pen Set", "category": "Stationery", "price": 12.99, "quantity": 100, "region": "West"},
        {"id": 10, "product": "Headphones", "category": "Electronics", "price": 149.99, "quantity": 25, "region": "North"},
    ]

    # Insert data into 'sales' table
    db["sales"].insert_all(sales_data, pk="id")

    print("=" * 70)
    print("DATASETTE DATA ANALYSIS EXAMPLE")
    print("=" * 70)
    print(f"\n[Line 44] Created database at: {db_path}")
    print(f"[Line 46] Inserted {len(sales_data)} sales records\n")

    return db, db_path


def analyze_with_sqlite_utils(db):
    """Demonstrate data analysis using sqlite-utils."""
    print("=" * 70)
    print("ANALYSIS USING SQLITE-UTILS")
    print("=" * 70)

    # Query 1: Total revenue by category
    print("\n[Line 59] Total Revenue by Category:")
    print("-" * 50)
    query = """
        SELECT category,
               SUM(price * quantity) as total_revenue,
               COUNT(*) as product_count
        FROM sales
        GROUP BY category
        ORDER BY total_revenue DESC
    """
    for row in db.execute(query).fetchall():
        print(f"  {row[0]:15} | Revenue: ${row[1]:10,.2f} | Products: {row[2]}")

    # Query 2: Top 5 products by revenue
    print("\n[Line 74] Top 5 Products by Revenue:")
    print("-" * 50)
    query = """
        SELECT product,
               price * quantity as revenue,
               region
        FROM sales
        ORDER BY revenue DESC
        LIMIT 5
    """
    for row in db.execute(query).fetchall():
        print(f"  {row[0]:15} | ${row[1]:10,.2f} | Region: {row[2]}")

    # Query 3: Sales by region
    print("\n[Line 89] Sales Summary by Region:")
    print("-" * 50)
    query = """
        SELECT region,
               COUNT(*) as num_products,
               SUM(quantity) as total_units,
               SUM(price * quantity) as total_revenue
        FROM sales
        GROUP BY region
        ORDER BY total_revenue DESC
    """
    for row in db.execute(query).fetchall():
        print(f"  {row[0]:10} | Products: {row[1]} | Units: {row[2]:4} | Revenue: ${row[3]:10,.2f}")


def demonstrate_datasette_features(db_path):
    """Show how to launch Datasette for interactive analysis."""
    print("\n" + "=" * 70)
    print("DATASETTE INTERACTIVE FEATURES")
    print("=" * 70)

    print("\n[Line 111] To launch Datasette web interface, run:")
    print(f"  uv run datasette {db_path}")

    print("\n[Line 114] Datasette provides:")
    print("  • Interactive SQL query editor with autocomplete")
    print("  • Automatic API endpoints (JSON/CSV export)")
    print("  • Faceted search and filtering")
    print("  • Full-text search capabilities")
    print("  • Custom SQL query sharing via URLs")
    print("  • Plugins for charts, maps, and more")

    print("\n[Line 123] Example API endpoints (when server is running):")
    print("  • All sales: http://localhost:8001/sales_analysis/sales.json")
    print("  • Filter by category: http://localhost:8001/sales_analysis/sales.json?category=Electronics")
    print("  • Custom SQL: http://localhost:8001/sales_analysis.json?sql=SELECT+*+FROM+sales")

    print("\n[Line 128] Try these SQL queries in Datasette:")
    print("  1. SELECT * FROM sales WHERE price > 100")
    print("  2. SELECT category, AVG(price) FROM sales GROUP BY category")
    print("  3. SELECT * FROM sales ORDER BY price * quantity DESC")


def main():
    """Main execution function."""
    # Create sample database and analyze
    db, db_path = create_sample_data()
    analyze_with_sqlite_utils(db)
    demonstrate_datasette_features(db_path)

    print("\n" + "=" * 70)
    print("[Line 143] Analysis complete! Database ready for Datasette exploration.")
    print("=" * 70)


if __name__ == "__main__":
    main()
