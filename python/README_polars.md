# Polars: A Lightning-Fast Alternative to Pandas

This example demonstrates **Polars**, a modern DataFrame library written in Rust with Python bindings, as a high-performance alternative to pandas.

## Version Requirements

- **Python**: >= 3.10
- **Polars**: >= 0.20.0

## Running the Example

```bash
uv run main_polars.py
```

## Key Features Demonstrated

### 1. DataFrame Creation (Lines 29-47)

**Source Code:**
```python
29    df = pl.DataFrame({
30        "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", "Mouse", "Keyboard"],
31        "category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Accessories", "Accessories"],
32        "price": [1200.00, 25.50, 75.00, 350.00, 1100.00, 22.00, 80.00],
33        "quantity": [2, 10, 5, 3, 1, 15, 4],
34        "date": [
35            datetime(2024, 1, 15),
36            datetime(2024, 1, 16),
37            datetime(2024, 1, 16),
38            datetime(2024, 1, 17),
39            datetime(2024, 1, 18),
40            datetime(2024, 1, 18),
41            datetime(2024, 1, 19),
42        ]
43    })
44
45    print("Original DataFrame:")
46    print(df)
```

**Output:**
```
Original DataFrame:
shape: (7, 5)
┌──────────┬─────────────┬────────┬──────────┬─────────────────────┐
│ product  ┆ category    ┆ price  ┆ quantity ┆ date                │
│ ---      ┆ ---         ┆ ---    ┆ ---      ┆ ---                 │
│ str      ┆ str         ┆ f64    ┆ i64      ┆ datetime[μs]        │
╞══════════╪═════════════╪════════╪══════════╪═════════════════════╡
│ Laptop   ┆ Electronics ┆ 1200.0 ┆ 2        ┆ 2024-01-15 00:00:00 │
│ Mouse    ┆ Accessories ┆ 25.5   ┆ 10       ┆ 2024-01-16 00:00:00 │
│ Keyboard ┆ Accessories ┆ 75.0   ┆ 5        ┆ 2024-01-16 00:00:00 │
│ Monitor  ┆ Electronics ┆ 350.0  ┆ 3        ┆ 2024-01-17 00:00:00 │
│ Laptop   ┆ Electronics ┆ 1100.0 ┆ 1        ┆ 2024-01-18 00:00:00 │
│ Mouse    ┆ Accessories ┆ 22.0   ┆ 15       ┆ 2024-01-18 00:00:00 │
│ Keyboard ┆ Accessories ┆ 80.0   ┆ 4        ┆ 2024-01-19 00:00:00 │
└──────────┴─────────────┴────────┴──────────┴─────────────────────┘
```

**Note:** Polars automatically infers data types and displays them clearly (str, f64, i64, datetime[μs]). The table format is clean and easy to read.

---

### 2. Column Selection and Filtering (Lines 53-61)

**Source Code:**
```python
53    # Select columns using expression syntax
54    result = df.select(["product", "price", "quantity"])
55    print("Selected columns (product, price, quantity):")
56    print(result)
57
58    # Filter with expressions
59    print("\nProducts with price > $50:")
60    filtered = df.filter(pl.col("price") > 50)
61    print(filtered)
```

**Output:**
```
Selected columns (product, price, quantity):
shape: (7, 3)
┌──────────┬────────┬──────────┐
│ product  ┆ price  ┆ quantity │
│ ---      ┆ ---    ┆ ---      │
│ str      ┆ f64    ┆ i64      │
╞══════════╪════════╪══════════╡
│ Laptop   ┆ 1200.0 ┆ 2        │
│ Mouse    ┆ 25.5   ┆ 10       │
│ Keyboard ┆ 75.0   ┆ 5        │
...

Products with price > $50:
shape: (5, 5)
┌──────────┬─────────────┬────────┬──────────┬─────────────────────┐
│ product  ┆ category    ┆ price  ┆ quantity ┆ date                │
│ ---      ┆ ---         ┆ ---    ┆ ---      ┆ ---                 │
│ str      ┆ str         ┆ f64    ┆ i64      ┆ datetime[μs]        │
╞══════════╪═════════════╪════════╪══════════╪═════════════════════╡
│ Laptop   ┆ Electronics ┆ 1200.0 ┆ 2        ┆ 2024-01-15 00:00:00 │
│ Keyboard ┆ Accessories ┆ 75.0   ┆ 5        ┆ 2024-01-16 00:00:00 │
│ Monitor  ┆ Electronics ┆ 350.0  ┆ 3        ┆ 2024-01-17 00:00:00 │
│ Laptop   ┆ Electronics ┆ 1100.0 ┆ 1        ┆ 2024-01-18 00:00:00 │
│ Keyboard ┆ Accessories ┆ 80.0   ┆ 4        ┆ 2024-01-19 00:00:00 │
└──────────┴─────────────┴────────┴──────────┴─────────────────────┘
```

**Note:** The `pl.col()` expression syntax is Polars' powerful way to reference columns. Notice how filtering automatically reduced the shape from (7,5) to (5,5).

---

### 3. Powerful Expression Syntax (Lines 66-80)

**Source Code:**
```python
66    # Calculate total value with expressions
67    result = df.with_columns(
68        (pl.col("price") * pl.col("quantity")).alias("total_value")
69    )
70    print("DataFrame with calculated total_value column:")
71    print(result)
72
73    # Multiple transformations in one go
74    result = df.with_columns([
75        (pl.col("price") * pl.col("quantity")).alias("total_value"),
76        (pl.col("price") * 0.9).alias("discounted_price"),
77        pl.col("product").str.to_uppercase().alias("product_upper")
78    ])
79    print("\nMultiple transformations applied:")
80    print(result.select(["product", "product_upper", "price", "discounted_price", "total_value"]))
```

**Output:**
```
DataFrame with calculated total_value column:
shape: (7, 6)
┌──────────┬─────────────┬────────┬──────────┬─────────────────────┬─────────────┐
│ product  ┆ category    ┆ price  ┆ quantity ┆ date                ┆ total_value │
│ ---      ┆ ---         ┆ ---    ┆ ---      ┆ ---                 ┆ ---         │
│ str      ┆ str         ┆ f64    ┆ i64      ┆ datetime[μs]        ┆ f64         │
╞══════════╪═════════════╪════════╪══════════╪═════════════════════╪═════════════╡
│ Laptop   ┆ Electronics ┆ 1200.0 ┆ 2        ┆ 2024-01-15 00:00:00 ┆ 2400.0      │
│ Mouse    ┆ Accessories ┆ 25.5   ┆ 10       ┆ 2024-01-16 00:00:00 ┆ 255.0       │
...

Multiple transformations applied:
shape: (7, 5)
┌──────────┬───────────────┬────────┬──────────────────┬─────────────┐
│ product  ┆ product_upper ┆ price  ┆ discounted_price ┆ total_value │
│ ---      ┆ ---           ┆ ---    ┆ ---              ┆ ---         │
│ str      ┆ str           ┆ f64    ┆ f64              ┆ f64         │
╞══════════╪═══════════════╪════════╪══════════════════╪═════════════╡
│ Laptop   ┆ LAPTOP        ┆ 1200.0 ┆ 1080.0           ┆ 2400.0      │
│ Mouse    ┆ MOUSE         ┆ 25.5   ┆ 22.95            ┆ 255.0       │
│ Keyboard ┆ KEYBOARD      ┆ 75.0   ┆ 67.5             ┆ 375.0       │
...
```

**Note:** `with_columns()` allows you to add multiple derived columns in one efficient operation. Line 67-68 shows a single calculation (price × quantity), while lines 74-77 demonstrate applying multiple transformations simultaneously.

---

### 4. Aggregations and GroupBy (Lines 85-107)

**Source Code:**
```python
85    df_with_total = df.with_columns(
86        (pl.col("price") * pl.col("quantity")).alias("total_value")
87    )
88
89    # Group by category
90    grouped = df_with_total.group_by("category").agg([
91        pl.col("total_value").sum().alias("total_revenue"),
92        pl.col("quantity").sum().alias("total_quantity"),
93        pl.col("price").mean().alias("avg_price"),
94        pl.col("product").count().alias("num_transactions")
95    ])
96    print("Aggregated by category:")
97    print(grouped)
98
99    # Group by product with multiple aggregations
100   product_summary = df_with_total.group_by("product").agg([
101       pl.col("quantity").sum().alias("total_sold"),
102       pl.col("price").mean().alias("avg_price"),
103       pl.col("total_value").sum().alias("revenue")
104   ]).sort("revenue", descending=True)
105   print("\nProduct summary (sorted by revenue):")
106   print(product_summary)
```

**Output:**
```
Aggregated by category:
shape: (2, 5)
┌─────────────┬───────────────┬────────────────┬────────────┬──────────────────┐
│ category    ┆ total_revenue ┆ total_quantity ┆ avg_price  ┆ num_transactions │
│ ---         ┆ ---           ┆ ---            ┆ ---        ┆ ---              │
│ str         ┆ f64           ┆ i64            ┆ f64        ┆ u32              │
╞═════════════╪═══════════════╪════════════════╪════════════╪══════════════════╡
│ Accessories ┆ 1280.0        ┆ 34             ┆ 50.625     ┆ 4                │
│ Electronics ┆ 4550.0        ┆ 6              ┆ 883.333333 ┆ 3                │
└─────────────┴───────────────┴────────────────┴────────────┴──────────────────┘

Product summary (sorted by revenue):
shape: (4, 4)
┌──────────┬────────────┬───────────┬─────────┐
│ product  ┆ total_sold ┆ avg_price ┆ revenue │
│ ---      ┆ ---        ┆ ---       ┆ ---     │
│ str      ┆ i64        ┆ f64       ┆ f64     │
╞══════════╪════════════╪═══════════╪═════════╡
│ Laptop   ┆ 3          ┆ 1150.0    ┆ 3500.0  │
│ Monitor  ┆ 3          ┆ 350.0     ┆ 1050.0  │
│ Keyboard ┆ 9          ┆ 77.5      ┆ 695.0   │
│ Mouse    ┆ 25         ┆ 23.75     ┆ 585.0   │
└──────────┴────────────┴───────────┴─────────┘
```

**Note:** Lines 90-95 show Polars' `.agg()` method for applying multiple aggregation functions. Electronics category has higher revenue ($4550) despite fewer transactions (3) compared to Accessories ($1280, 4 transactions).

---

### 5. Lazy Execution - Query Optimization (Lines 112-139)

**Source Code:**
```python
115   # Create a lazy frame
116   lazy_df = df.lazy()
117
118   # Build a query (not executed yet)
119   lazy_query = (
120       lazy_df
121       .with_columns((pl.col("price") * pl.col("quantity")).alias("total_value"))
122       .filter(pl.col("total_value") > 100)
123       .group_by("category")
124       .agg([
125           pl.col("total_value").sum().alias("revenue"),
126           pl.col("product").count().alias("count")
127       ])
128       .sort("revenue", descending=True)
129   )
130
131   print("Lazy query plan:")
132   print(lazy_query.explain())
133
134   print("\nExecuting lazy query:")
135   result = lazy_query.collect()
136   print(result)
```

**Output:**
```
Lazy query plan:
SORT BY [descending: [true]] [col("revenue")]
  AGGREGATE[maintain_order: false]
    [col("total_value").sum().alias("revenue"), col("product").count().alias("count")] BY [col("category")]
    FROM
    FILTER [(col("total_value")) > (100.0)]
    FROM
       WITH_COLUMNS:
       [[(col("price")) * (col("quantity").cast(Float64))].alias("total_value")]
        DF ["product", "category", "price", "quantity", ...]; PROJECT["product", "category", "price", "quantity"] 4/5 COLUMNS

Executing lazy query:
shape: (2, 3)
┌─────────────┬─────────┬───────┐
│ category    ┆ revenue ┆ count │
│ ---         ┆ ---     ┆ ---   │
│ str         ┆ f64     ┆ u32   │
╞═════════════╪═════════╪═══════╡
│ Electronics ┆ 4550.0  ┆ 3     │
│ Accessories ┆ 1280.0  ┆ 4     │
└─────────────┴─────────┴───────┘
```

**Note:** The lazy query plan (line 132) shows how Polars optimizes the query execution order. Notice "PROJECT 4/5 COLUMNS" - Polars automatically determined it only needs 4 of 5 columns, optimizing memory usage. The query is only executed when `.collect()` is called (line 135).

---

### 6. String Operations (Lines 144-152)

**Source Code:**
```python
144   # String manipulations
145   string_ops = df.select([
146       pl.col("product"),
147       pl.col("product").str.to_lowercase().alias("lowercase"),
148       pl.col("product").str.len_chars().alias("name_length"),
149       pl.col("product").str.contains("top").alias("contains_top")
150   ])
151   print("String operations:")
152   print(string_ops)
```

**Output:**
```
String operations:
shape: (7, 4)
┌──────────┬───────────┬─────────────┬──────────────┐
│ product  ┆ lowercase ┆ name_length ┆ contains_top │
│ ---      ┆ ---       ┆ ---         ┆ ---          │
│ str      ┆ str       ┆ u32         ┆ bool         │
╞══════════╪═══════════╪═════════════╪══════════════╡
│ Laptop   ┆ laptop    ┆ 6           ┆ true         │
│ Mouse    ┆ mouse     ┆ 5           ┆ false        │
│ Keyboard ┆ keyboard  ┆ 8           ┆ false        │
│ Monitor  ┆ monitor   ┆ 7           ┆ false        │
│ Laptop   ┆ laptop    ┆ 6           ┆ true         │
│ Mouse    ┆ mouse     ┆ 5           ┆ false        │
│ Keyboard ┆ keyboard  ┆ 8           ┆ false        │
└──────────┴───────────┴─────────────┴──────────────┘
```

**Note:** The `str` namespace (line 147-149) provides vectorized string operations. Line 149 shows pattern matching - "Laptop" contains "top" (case-sensitive) returns `true`.

---

### 7. Date/Time Operations (Lines 157-167)

**Source Code:**
```python
157   date_ops = df.select([
158       pl.col("date"),
159       pl.col("date").dt.year().alias("year"),
160       pl.col("date").dt.month().alias("month"),
161       pl.col("date").dt.day().alias("day"),
162       pl.col("date").dt.weekday().alias("weekday")
163   ])
164   print("Date operations:")
165   print(date_ops)
```

**Output:**
```
Date operations:
shape: (7, 5)
┌─────────────────────┬──────┬───────┬─────┬─────────┐
│ date                ┆ year ┆ month ┆ day ┆ weekday │
│ ---                 ┆ ---  ┆ ---   ┆ --- ┆ ---     │
│ datetime[μs]        ┆ i32  ┆ i8    ┆ i8  ┆ i8      │
╞═════════════════════╪══════╪═══════╪═════╪═════════╡
│ 2024-01-15 00:00:00 ┆ 2024 ┆ 1     ┆ 15  ┆ 1       │
│ 2024-01-16 00:00:00 ┆ 2024 ┆ 1     ┆ 16  ┆ 2       │
│ 2024-01-17 00:00:00 ┆ 2024 ┆ 1     ┆ 17  ┆ 3       │
...
```

**Note:** The `dt` namespace (lines 159-162) extracts date components. Weekday numbering starts at 1 (Monday=1, Sunday=7).

---

### 8. Joins (Lines 172-189)

**Source Code:**
```python
172   # Create a second DataFrame for joining
173   product_info = pl.DataFrame({
174       "product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
175       "manufacturer": ["TechCorp", "Logitech", "Corsair", "Dell"],
176       "warranty_years": [2, 1, 2, 3]
177   })
178
179   print("Product information DataFrame:")
180   print(product_info)
181
182   # Perform an inner join
183   joined = df.join(product_info, on="product", how="inner")
184   print("\nJoined DataFrame (inner join on 'product'):")
185   print(joined.select(["product", "price", "manufacturer", "warranty_years"]))
```

**Output:**
```
Product information DataFrame:
shape: (4, 3)
┌──────────┬──────────────┬────────────────┐
│ product  ┆ manufacturer ┆ warranty_years │
│ ---      ┆ ---          ┆ ---            │
│ str      ┆ str          ┆ i64            │
╞══════════╪══════════════╪════════════════╡
│ Laptop   ┆ TechCorp     ┆ 2              │
│ Mouse    ┆ Logitech     ┆ 1              │
│ Keyboard ┆ Corsair      ┆ 2              │
│ Monitor  ┆ Dell         ┆ 3              │
└──────────┴──────────────┴────────────────┘

Joined DataFrame (inner join on 'product'):
shape: (7, 4)
┌──────────┬────────┬──────────────┬────────────────┐
│ product  ┆ price  ┆ manufacturer ┆ warranty_years │
│ ---      ┆ ---    ┆ ---          ┆ ---            │
│ str      ┆ f64    ┆ str          ┆ i64            │
╞══════════╪════════╪══════════════╪════════════════╡
│ Laptop   ┆ 1200.0 ┆ TechCorp     ┆ 2              │
│ Mouse    ┆ 25.5   ┆ Logitech     ┆ 1              │
│ Keyboard ┆ 75.0   ┆ Corsair      ┆ 2              │
│ Monitor  ┆ 350.0  ┆ Dell         ┆ 3              │
│ Laptop   ┆ 1100.0 ┆ TechCorp     ┆ 2              │
│ Mouse    ┆ 22.0   ┆ Logitech     ┆ 1              │
│ Keyboard ┆ 80.0   ┆ Corsair      ┆ 2              │
└──────────┴────────┴──────────────┴────────────────┘
```

**Note:** Line 183 performs an inner join on the "product" column. All 7 rows from the original DataFrame found matches in the product_info table.

---

### 9. Window Functions (Lines 194-205)

**Source Code:**
```python
194   # Calculate rank within each category
195   windowed = df_with_total.with_columns([
196       pl.col("total_value")
197         .rank(method="ordinal", descending=True)
198         .over("category")
199         .alias("rank_in_category")
200   ])
201   print("Ranking within category:")
202   print(windowed.select(["product", "category", "total_value", "rank_in_category"]))
```

**Output:**
```
Ranking within category:
shape: (7, 4)
┌──────────┬─────────────┬─────────────┬──────────────────┐
│ product  ┆ category    ┆ total_value ┆ rank_in_category │
│ ---      ┆ ---         ┆ ---         ┆ ---              │
│ str      ┆ str         ┆ f64         ┆ u32              │
╞══════════╪═════════════╪═════════════╪══════════════════╡
│ Laptop   ┆ Electronics ┆ 2400.0      ┆ 1                │
│ Mouse    ┆ Accessories ┆ 255.0       ┆ 4                │
│ Keyboard ┆ Accessories ┆ 375.0       ┆ 1                │
│ Monitor  ┆ Electronics ┆ 1050.0      ┆ 3                │
│ Laptop   ┆ Electronics ┆ 1100.0      ┆ 2                │
│ Mouse    ┆ Accessories ┆ 330.0       ┆ 2                │
│ Keyboard ┆ Accessories ┆ 320.0       ┆ 3                │
└──────────┴─────────────┴─────────────┴──────────────────┘
```

**Note:** The `.over("category")` clause (line 198) partitions the ranking operation by category. The first Laptop ($2400) ranks #1 in Electronics, while Keyboard ($375) ranks #1 in Accessories.

---

### 10. Polars vs Pandas Comparison (Lines 210-233)

**Source Code:**
```python
210   print("Polars vs Pandas:")
211   print("-" * 70)
212   print("1. Performance: Polars is significantly faster (written in Rust)")
213   print("2. Memory: More memory efficient with Arrow memory format")
214   print("3. Lazy Execution: Automatic query optimization with LazyFrame")
215   print("4. Expression Syntax: More expressive and composable operations")
216   print("5. No Index: Polars doesn't use an index (simpler mental model)")
217   print("6. Immutability: Operations return new DataFrames (safer)")
218   print("7. Parallel Processing: Automatically uses all CPU cores")
219   print("8. Type System: Stricter type checking")
220   print("-" * 70)
221
222   # Example showing the expression-based approach
223   print("\nPolars Expression Example:")
224   polars_way = df.select([
225       pl.col("product"),
226       (pl.col("price") * pl.col("quantity")).alias("total")
227   ]).filter(pl.col("total") > 100)
228   print(polars_way)
229
230   print("\n# Equivalent Pandas approach would be:")
231   print('# df_pandas["total"] = df_pandas["price"] * df_pandas["quantity"]')
232   print('# result = df_pandas[df_pandas["total"] > 100][["product", "total"]]')
```

**Output:**
```
Polars vs Pandas:
----------------------------------------------------------------------
1. Performance: Polars is significantly faster (written in Rust)
2. Memory: More memory efficient with Arrow memory format
3. Lazy Execution: Automatic query optimization with LazyFrame
4. Expression Syntax: More expressive and composable operations
5. No Index: Polars doesn't use an index (simpler mental model)
6. Immutability: Operations return new DataFrames (safer)
7. Parallel Processing: Automatically uses all CPU cores
8. Type System: Stricter type checking
----------------------------------------------------------------------

Polars Expression Example:
shape: (7, 2)
┌──────────┬────────┐
│ product  ┆ total  │
│ ---      ┆ ---    │
│ str      ┆ f64    │
╞══════════╪════════╡
│ Laptop   ┆ 2400.0 │
│ Mouse    ┆ 255.0  │
│ Keyboard ┆ 375.0  │
│ Monitor  ┆ 1050.0 │
│ Laptop   ┆ 1100.0 │
│ Mouse    ┆ 330.0  │
│ Keyboard ┆ 320.0  │
└──────────┴────────┘

# Equivalent Pandas approach would be:
# df_pandas["total"] = df_pandas["price"] * df_pandas["quantity"]
# result = df_pandas[df_pandas["total"] > 100][["product", "total"]]
```

**Note:** Lines 224-227 demonstrate Polars' expression-based syntax. Unlike Pandas (lines 231-232), Polars chains operations without mutating the DataFrame and executes them efficiently in one pass.

---

## Summary

This example showcases Polars as a modern, high-performance alternative to pandas with:

- **Expression-based API**: More composable and readable data transformations
- **Lazy execution**: Automatic query optimization for better performance
- **Type safety**: Clear, strict type system
- **Performance**: Rust-based implementation with automatic parallelization
- **Memory efficiency**: Apache Arrow memory format
- **Functional approach**: Immutable operations that return new DataFrames

Polars is particularly well-suited for:
- Large datasets that need fast processing
- Complex data transformations with multiple steps
- Production environments requiring predictable performance
- Teams wanting a simpler mental model (no index complications)
