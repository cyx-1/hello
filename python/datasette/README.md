# Datasette Data Analysis Example

This example demonstrates how to use **Datasette** - a powerful tool for exploring and publishing SQLite databases through an interactive web interface.

## What is Datasette?

Datasette is an open-source tool that allows you to:
- Instantly publish data and databases to the web
- Explore and analyze data through a web UI
- Execute SQL queries with autocomplete
- Export data in JSON, CSV, and other formats
- Create custom views and dashboards with plugins

## Requirements

- **Python**: >= 3.10
- **Dependencies**: datasette, sqlite-utils, pandas>=2.0
  - Note: pandas>=2.0 is required due to compatibility with sqlite-utils

## Running the Example

```bash
uv run python python/datasette/main_datasette.py
```

## Source Code

```python
1   #!/usr/bin/env python3
2   # /// script
3   # requires-python = ">=3.10"
4   # dependencies = [
5   #     "datasette",
6   #     "sqlite-utils",
7   #     "pandas>=2.0",
8   # ]
9   # ///
10  """
11  Datasette Data Analysis Example
12
13  This script demonstrates how to use Datasette to analyze data:
14  1. Create a SQLite database with sample data
15  2. Use sqlite-utils to insert and query data
16  3. Launch Datasette to explore and analyze the data through its web interface
17  """
18
19  import sqlite3
20  import tempfile
21  from pathlib import Path
22
23  from sqlite_utils import Database
24
25
26  def create_sample_data():
27      """Create a temporary SQLite database with sample sales data."""
28      # Create a temporary database file
29      db_path = Path(tempfile.gettempdir()) / "sales_analysis.db"
30
31      # Initialize database with sqlite-utils
32      db = Database(db_path)
33
34      # Sample sales data
35      sales_data = [
36          {"id": 1, "product": "Laptop", "category": "Electronics", "price": 999.99, "quantity": 5, "region": "North"},
37          {"id": 2, "product": "Mouse", "category": "Electronics", "price": 29.99, "quantity": 50, "region": "North"},
38          {"id": 3, "product": "Keyboard", "category": "Electronics", "price": 79.99, "quantity": 30, "region": "South"},
39          {"id": 4, "product": "Monitor", "category": "Electronics", "price": 299.99, "quantity": 15, "region": "East"},
40          {"id": 5, "product": "Desk Chair", "category": "Furniture", "price": 199.99, "quantity": 20, "region": "West"},
41          {"id": 6, "product": "Desk", "category": "Furniture", "price": 399.99, "quantity": 10, "region": "North"},
42          {"id": 7, "product": "Lamp", "category": "Furniture", "price": 49.99, "quantity": 40, "region": "South"},
43          {"id": 8, "product": "Notebook", "category": "Stationery", "price": 4.99, "quantity": 200, "region": "East"},
44          {"id": 9, "product": "Pen Set", "category": "Stationery", "price": 12.99, "quantity": 100, "region": "West"},
45          {"id": 10, "product": "Headphones", "category": "Electronics", "price": 149.99, "quantity": 25, "region": "North"},
46      ]
47
48      # Insert data into 'sales' table
49      db["sales"].insert_all(sales_data, pk="id")
50
51      print("=" * 70)
52      print("DATASETTE DATA ANALYSIS EXAMPLE")
53      print("=" * 70)
54      print(f"\n[Line 44] Created database at: {db_path}")
55      print(f"[Line 46] Inserted {len(sales_data)} sales records\n")
56
57      return db, db_path
58
59
60  def analyze_with_sqlite_utils(db):
61      """Demonstrate data analysis using sqlite-utils."""
62      print("=" * 70)
63      print("ANALYSIS USING SQLITE-UTILS")
64      print("=" * 70)
65
66      # Query 1: Total revenue by category
67      print("\n[Line 59] Total Revenue by Category:")
68      print("-" * 50)
69      query = """
70          SELECT category,
71                 SUM(price * quantity) as total_revenue,
72                 COUNT(*) as product_count
73          FROM sales
74          GROUP BY category
75          ORDER BY total_revenue DESC
76      """
77      for row in db.execute(query).fetchall():
78          print(f"  {row[0]:15} | Revenue: ${row[1]:10,.2f} | Products: {row[2]}")
79
80      # Query 2: Top 5 products by revenue
81      print("\n[Line 74] Top 5 Products by Revenue:")
82      print("-" * 50)
83      query = """
84          SELECT product,
85                 price * quantity as revenue,
86                 region
87          FROM sales
88          ORDER BY revenue DESC
89          LIMIT 5
90      """
91      for row in db.execute(query).fetchall():
92          print(f"  {row[0]:15} | ${row[1]:10,.2f} | Region: {row[2]}")
93
94      # Query 3: Sales by region
95      print("\n[Line 89] Sales Summary by Region:")
96      print("-" * 50)
97      query = """
98          SELECT region,
99                 COUNT(*) as num_products,
100                SUM(quantity) as total_units,
101                SUM(price * quantity) as total_revenue
102         FROM sales
103         GROUP BY region
104         ORDER BY total_revenue DESC
105     """
106     for row in db.execute(query).fetchall():
107         print(f"  {row[0]:10} | Products: {row[1]} | Units: {row[2]:4} | Revenue: ${row[3]:10,.2f}")
108
109
110 def demonstrate_datasette_features(db_path):
111     """Show how to launch Datasette for interactive analysis."""
112     print("\n" + "=" * 70)
113     print("DATASETTE INTERACTIVE FEATURES")
114     print("=" * 70)
115
116     print(f"\n[Line 111] To launch Datasette web interface, run:")
117     print(f"  uv run datasette {db_path}")
118
119     print("\n[Line 114] Datasette provides:")
120     print("  • Interactive SQL query editor with autocomplete")
121     print("  • Automatic API endpoints (JSON/CSV export)")
122     print("  • Faceted search and filtering")
123     print("  • Full-text search capabilities")
124     print("  • Custom SQL query sharing via URLs")
125     print("  • Plugins for charts, maps, and more")
126
127     print("\n[Line 123] Example API endpoints (when server is running):")
128     print("  • All sales: http://localhost:8001/sales_analysis/sales.json")
129     print("  • Filter by category: http://localhost:8001/sales_analysis/sales.json?category=Electronics")
130     print("  • Custom SQL: http://localhost:8001/sales_analysis.json?sql=SELECT+*+FROM+sales")
131
132     print("\n[Line 128] Try these SQL queries in Datasette:")
133     print("  1. SELECT * FROM sales WHERE price > 100")
134     print("  2. SELECT category, AVG(price) FROM sales GROUP BY category")
135     print("  3. SELECT * FROM sales ORDER BY price * quantity DESC")
136
137
138 def main():
139     """Main execution function."""
140     # Create sample database and analyze
141     db, db_path = create_sample_data()
142     analyze_with_sqlite_utils(db)
143     demonstrate_datasette_features(db_path)
144
145     print("\n" + "=" * 70)
146     print("[Line 143] Analysis complete! Database ready for Datasette exploration.")
147     print("=" * 70)
148
149
150 if __name__ == "__main__":
151     main()
```

## Program Output

```
======================================================================
DATASETTE DATA ANALYSIS EXAMPLE
======================================================================

[Line 44] Created database at: C:\Users\yexin\AppData\Local\Temp\sales_analysis.db
[Line 46] Inserted 10 sales records

======================================================================
ANALYSIS USING SQLITE-UTILS
======================================================================

[Line 59] Total Revenue by Category:
--------------------------------------------------
  Electronics     | Revenue: $ 17,148.75 | Products: 5
  Furniture       | Revenue: $  9,999.30 | Products: 3
  Stationery      | Revenue: $  2,297.00 | Products: 2

[Line 74] Top 5 Products by Revenue:
--------------------------------------------------
  Laptop          | $  4,999.95 | Region: North
  Monitor         | $  4,499.85 | Region: East
  Desk            | $  3,999.90 | Region: North
  Desk Chair      | $  3,999.80 | Region: West
  Headphones      | $  3,749.75 | Region: North

[Line 89] Sales Summary by Region:
--------------------------------------------------
  North      | Products: 4 | Units:   90 | Revenue: $ 14,249.10
  East       | Products: 2 | Units:  215 | Revenue: $  5,497.85
  West       | Products: 2 | Units:  120 | Revenue: $  5,298.80
  South      | Products: 2 | Units:   70 | Revenue: $  4,399.30

======================================================================
DATASETTE INTERACTIVE FEATURES
======================================================================

[Line 111] To launch Datasette web interface, run:
  uv run datasette C:\Users\yexin\AppData\Local\Temp\sales_analysis.db

[Line 114] Datasette provides:
  • Interactive SQL query editor with autocomplete
  • Automatic API endpoints (JSON/CSV export)
  • Faceted search and filtering
  • Full-text search capabilities
  • Custom SQL query sharing via URLs
  • Plugins for charts, maps, and more

[Line 123] Example API endpoints (when server is running):
  • All sales: http://localhost:8001/sales_analysis/sales.json
  • Filter by category: http://localhost:8001/sales_analysis/sales.json?category=Electronics
  • Custom SQL: http://localhost:8001/sales_analysis.json?sql=SELECT+*+FROM+sales

[Line 128] Try these SQL queries in Datasette:
  1. SELECT * FROM sales WHERE price > 100
  2. SELECT category, AVG(price) FROM sales GROUP BY category
  3. SELECT * FROM sales ORDER BY price * quantity DESC

======================================================================
[Line 143] Analysis complete! Database ready for Datasette exploration.
======================================================================
```

## Code Annotations

### Database Creation (Lines 26-57)
- **Line 29**: Creates a temporary SQLite database file in system temp directory
- **Line 32**: Initializes database using `sqlite-utils.Database` - a high-level wrapper around SQLite
- **Lines 35-46**: Defines 10 sample sales records with product details across multiple categories
- **Line 49**: Uses `insert_all()` to bulk insert data efficiently with `id` as primary key
- **Output Lines 54-55**: Confirms database creation at temp path with 10 records inserted

### Data Analysis with sqlite-utils (Lines 60-108)

#### Query 1: Revenue by Category (Lines 66-78)
- **Lines 69-76**: SQL aggregation query calculating total revenue and product count per category
- **Line 77**: Executes query and iterates through results
- **Output Line 59**: Shows Electronics category leads with $17,148.75 revenue from 5 products
- **Analysis**: Furniture ($9,999.30) and Stationery ($2,297.00) follow, showing Electronics dominates sales

#### Query 2: Top Products (Lines 80-92)
- **Lines 83-90**: SQL query calculating revenue (price × quantity) for each product, sorted descending
- **Line 91**: Iterates through top 5 revenue-generating products
- **Output Line 74**: Laptop tops list at $4,999.95, showing high-value electronics dominate
- **Analysis**: Top 5 are all high-ticket items (Laptop, Monitor, Desk, Desk Chair, Headphones)

#### Query 3: Regional Analysis (Lines 94-107)
- **Lines 97-105**: SQL aggregation computing products, units sold, and revenue per region
- **Line 106**: Prints formatted regional summary
- **Output Line 89**: North region leads with $14,249.10 from 90 units across 4 products
- **Analysis**: North region outperforms others, possibly indicating market concentration

### Datasette Interactive Features (Lines 110-135)
- **Line 117**: Shows command to launch Datasette web server with the created database
- **Lines 119-125**: Lists key Datasette capabilities:
  - Interactive SQL editor with autocomplete helps beginners write queries
  - Automatic REST API endpoints enable programmatic access
  - Faceted search allows filtering without SQL knowledge
  - Plugin ecosystem extends functionality (charts, maps, authentication)
- **Lines 127-130**: Demonstrates REST API patterns:
  - `.json` suffix converts any view to JSON
  - URL parameters enable filtering (e.g., `?category=Electronics`)
  - Custom SQL can be passed via URL encoding
- **Lines 132-135**: Suggests example SQL queries to try interactively:
  - Filtering by price threshold
  - Calculating category averages
  - Sorting by computed revenue

## Key Features Demonstrated

### 1. sqlite-utils Integration
- **Lines 32, 49**: Programmatic database creation and data insertion
- **Lines 77, 91, 106**: Direct SQL execution with Python iteration
- Simpler API than raw sqlite3 module for common operations

### 2. SQL Analytics
- **Aggregation**: `SUM()`, `COUNT()` functions in Lines 70-72, 98-101
- **Grouping**: `GROUP BY` for category and regional analysis (Lines 74, 103)
- **Sorting**: `ORDER BY` for ranked results (Lines 75, 88, 104)

### 3. Datasette Web UI
- Zero-configuration web interface for data exploration
- No need to write HTML/JavaScript for basic data browsing
- Shareable URLs for specific queries and views

### 4. REST API
- Automatic JSON/CSV endpoints for every table and query
- URL-based filtering and querying without coding
- Enables building applications on top of Datasette

### 5. Data Export
- Multiple format support (JSON, CSV, etc.)
- URL-based export (add `.json` or `.csv` to any view)
- Facilitates data sharing and integration

## Next Steps

After running the script, launch Datasette to explore the data interactively:

```bash
uv run datasette C:\Users\yexin\AppData\Local\Temp\sales_analysis.db
```

Then visit `http://localhost:8001` to:
- Browse the sales table with pagination
- Execute custom SQL queries with syntax highlighting
- Export filtered results in JSON or CSV
- Create visualizations using Datasette plugins
- Share specific queries via bookmarkable URLs

## Version Requirements

This code requires **pandas >= 2.0** due to compatibility requirements in sqlite-utils. The code runs successfully on Python 3.10+.
