#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "polars>=0.20.0",
# ]
# ///

"""
Polars: A Modern Alternative to Pandas

This script demonstrates Polars, a blazingly fast DataFrame library
implemented in Rust with Python bindings, as an alternative to pandas.
"""

import polars as pl
from datetime import datetime


def section_header(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def main():
    print("Polars: A Lightning-Fast Alternative to Pandas")
    print("=" * 70)

    # Section 1: DataFrame Creation
    section_header("1. DataFrame Creation")

    # Create a sample dataset
    df = pl.DataFrame(
        {
            "product": [
                "Laptop",
                "Mouse",
                "Keyboard",
                "Monitor",
                "Laptop",
                "Mouse",
                "Keyboard",
            ],
            "category": [
                "Electronics",
                "Accessories",
                "Accessories",
                "Electronics",
                "Electronics",
                "Accessories",
                "Accessories",
            ],
            "price": [1200.00, 25.50, 75.00, 350.00, 1100.00, 22.00, 80.00],
            "quantity": [2, 10, 5, 3, 1, 15, 4],
            "date": [
                datetime(2024, 1, 15),
                datetime(2024, 1, 16),
                datetime(2024, 1, 16),
                datetime(2024, 1, 17),
                datetime(2024, 1, 18),
                datetime(2024, 1, 18),
                datetime(2024, 1, 19),
            ],
        }
    )

    print("Original DataFrame:")
    print(df)
    print(f"\nShape: {df.shape}")
    print(f"Columns: {df.columns}")

    # Section 2: Basic Operations
    section_header("2. Column Selection and Filtering")

    # Select columns using expression syntax
    result = df.select(["product", "price", "quantity"])
    print("Selected columns (product, price, quantity):")
    print(result)

    # Filter with expressions
    print("\nProducts with price > $50:")
    filtered = df.filter(pl.col("price") > 50)
    print(filtered)

    # Section 3: Expressions - The Power of Polars
    section_header("3. Powerful Expression Syntax")

    # Calculate total value with expressions
    result = df.with_columns(
        (pl.col("price") * pl.col("quantity")).alias("total_value")
    )
    print("DataFrame with calculated total_value column:")
    print(result)

    # Multiple transformations in one go
    result = df.with_columns(
        [
            (pl.col("price") * pl.col("quantity")).alias("total_value"),
            (pl.col("price") * 0.9).alias("discounted_price"),
            pl.col("product").str.to_uppercase().alias("product_upper"),
        ]
    )
    print("\nMultiple transformations applied:")
    print(
        result.select(
            ["product", "product_upper", "price", "discounted_price", "total_value"]
        )
    )

    # Section 4: Aggregations and GroupBy
    section_header("4. Aggregations and GroupBy")

    # Add total_value column for aggregations
    df_with_total = df.with_columns(
        (pl.col("price") * pl.col("quantity")).alias("total_value")
    )

    # Group by category
    grouped = df_with_total.group_by("category").agg(
        [
            pl.col("total_value").sum().alias("total_revenue"),
            pl.col("quantity").sum().alias("total_quantity"),
            pl.col("price").mean().alias("avg_price"),
            pl.col("product").count().alias("num_transactions"),
        ]
    )
    print("Aggregated by category:")
    print(grouped)

    # Group by product with multiple aggregations
    product_summary = (
        df_with_total.group_by("product")
        .agg(
            [
                pl.col("quantity").sum().alias("total_sold"),
                pl.col("price").mean().alias("avg_price"),
                pl.col("total_value").sum().alias("revenue"),
            ]
        )
        .sort("revenue", descending=True)
    )
    print("\nProduct summary (sorted by revenue):")
    print(product_summary)

    # Section 5: Lazy Execution
    section_header("5. Lazy Execution - Query Optimization")

    print("Lazy evaluation allows Polars to optimize the entire query plan")
    print("before executing, leading to better performance.\n")

    # Create a lazy frame
    lazy_df = df.lazy()

    # Build a query (not executed yet)
    lazy_query = (
        lazy_df.with_columns(
            (pl.col("price") * pl.col("quantity")).alias("total_value")
        )
        .filter(pl.col("total_value") > 100)
        .group_by("category")
        .agg(
            [
                pl.col("total_value").sum().alias("revenue"),
                pl.col("product").count().alias("count"),
            ]
        )
        .sort("revenue", descending=True)
    )

    print("Lazy query plan:")
    print(lazy_query.explain())

    print("\nExecuting lazy query:")
    result = lazy_query.collect()
    print(result)

    # Section 6: String Operations
    section_header("6. String Operations")

    # String manipulations
    string_ops = df.select(
        [
            pl.col("product"),
            pl.col("product").str.to_lowercase().alias("lowercase"),
            pl.col("product").str.len_chars().alias("name_length"),
            pl.col("product").str.contains("top").alias("contains_top"),
        ]
    )
    print("String operations:")
    print(string_ops)

    # Section 7: Date Operations
    section_header("7. Date/Time Operations")

    date_ops = df.select(
        [
            pl.col("date"),
            pl.col("date").dt.year().alias("year"),
            pl.col("date").dt.month().alias("month"),
            pl.col("date").dt.day().alias("day"),
            pl.col("date").dt.weekday().alias("weekday"),
        ]
    )
    print("Date operations:")
    print(date_ops)

    # Section 8: Joins
    section_header("8. Joins")

    # Create a second DataFrame for joining
    product_info = pl.DataFrame(
        {
            "product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
            "manufacturer": ["TechCorp", "Logitech", "Corsair", "Dell"],
            "warranty_years": [2, 1, 2, 3],
        }
    )

    print("Product information DataFrame:")
    print(product_info)

    # Perform an inner join
    joined = df.join(product_info, on="product", how="inner")
    print("\nJoined DataFrame (inner join on 'product'):")
    print(joined.select(["product", "price", "manufacturer", "warranty_years"]))

    # Section 9: Window Functions
    section_header("9. Window Functions")

    # Calculate rank within each category
    windowed = df_with_total.with_columns(
        [
            pl.col("total_value")
            .rank(method="ordinal", descending=True)
            .over("category")
            .alias("rank_in_category")
        ]
    )
    print("Ranking within category:")
    print(windowed.select(["product", "category", "total_value", "rank_in_category"]))

    # Section 10: Pandas Comparison
    section_header("10. Key Differences from Pandas")

    print("Polars vs Pandas:")
    print("-" * 70)
    print("1. Performance: Polars is significantly faster (written in Rust)")
    print("2. Memory: More memory efficient with Arrow memory format")
    print("3. Lazy Execution: Automatic query optimization with LazyFrame")
    print("4. Expression Syntax: More expressive and composable operations")
    print("5. No Index: Polars doesn't use an index (simpler mental model)")
    print("6. Immutability: Operations return new DataFrames (safer)")
    print("7. Parallel Processing: Automatically uses all CPU cores")
    print("8. Type System: Stricter type checking")
    print("-" * 70)

    # Example showing the expression-based approach
    print("\nPolars Expression Example:")
    polars_way = df.select(
        [pl.col("product"), (pl.col("price") * pl.col("quantity")).alias("total")]
    ).filter(pl.col("total") > 100)
    print(polars_way)

    print("\n# Equivalent Pandas approach would be:")
    print('# df_pandas["total"] = df_pandas["price"] * df_pandas["quantity"]')
    print('# result = df_pandas[df_pandas["total"] > 100][["product", "total"]]')


if __name__ == "__main__":
    main()
