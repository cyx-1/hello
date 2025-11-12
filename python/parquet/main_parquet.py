#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pandas>=2.0.0",
#     "pyarrow>=14.0.0",
# ]
# ///

"""
Parquet Format Illustration in Python

This script demonstrates:
- Creating and writing Parquet files
- Reading Parquet files
- Compression options
- Schema inspection
- Metadata handling
- Partitioned datasets
"""

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path
import shutil


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print("=" * 70)


def cleanup_files() -> None:
    """Clean up any existing parquet files from previous runs."""
    for path in ["sample.parquet", "compressed.parquet", "partitioned_data"]:
        p = Path(path)
        if p.exists():
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()


def basic_write_read() -> None:
    """Demonstrate basic Parquet write and read operations."""
    print_section("1. Basic Write and Read")

    # Create sample data
    data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "age": [25, 30, 35, 28, 42],
        "salary": [50000.0, 60000.0, 75000.0, 55000.0, 90000.0],
        "is_active": [True, True, False, True, True],
    }
    df = pd.DataFrame(data)

    print("\nOriginal DataFrame:")
    print(df)
    print(f"\nDataFrame shape: {df.shape}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum()} bytes")

    # Write to Parquet
    df.to_parquet("sample.parquet", engine="pyarrow", index=False)
    file_size = Path("sample.parquet").stat().st_size
    print(f"\nParquet file written: sample.parquet ({file_size} bytes)")

    # Read from Parquet
    df_read = pd.read_parquet("sample.parquet", engine="pyarrow")
    print("\nDataFrame read from Parquet:")
    print(df_read)
    print(f"Data types preserved: {df.dtypes.equals(df_read.dtypes)}")


def compression_comparison() -> None:
    """Compare different compression algorithms."""
    print_section("2. Compression Comparison")

    # Create larger dataset for compression testing
    import numpy as np

    data = {
        "id": range(10000),
        "value": np.random.randn(10000),
        "category": np.random.choice(["A", "B", "C", "D"], 10000),
        "timestamp": pd.date_range("2024-01-01", periods=10000, freq="min"),
    }
    df = pd.DataFrame(data)

    print(f"\nTest dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Memory usage: {df.memory_usage(deep=True).sum():,} bytes")

    compression_methods = ["snappy", "gzip", "brotli", None]
    results = []

    for compression in compression_methods:
        filename = f"compressed_{compression}.parquet"
        df.to_parquet(filename, compression=compression, engine="pyarrow", index=False)
        size = Path(filename).stat().st_size
        results.append(
            {
                "Compression": compression or "none",
                "File Size (bytes)": size,
                "Compression Ratio": f"{df.memory_usage(deep=True).sum() / size:.2f}x",
            }
        )
        Path(filename).unlink()  # Clean up

    results_df = pd.DataFrame(results)
    print("\nCompression Results:")
    print(results_df.to_string(index=False))


def schema_and_metadata() -> None:
    """Demonstrate schema inspection and metadata handling."""
    print_section("3. Schema and Metadata")

    # Create data with various types
    data = {
        "int_col": [1, 2, 3],
        "float_col": [1.1, 2.2, 3.3],
        "str_col": ["a", "b", "c"],
        "datetime_col": pd.date_range("2024-01-01", periods=3),
        "bool_col": [True, False, True],
        "nullable_int": pd.array([1, None, 3], dtype="Int64"),
    }
    df = pd.DataFrame(data)

    # Write with custom metadata
    table = pa.Table.from_pandas(df)
    metadata = {
        b"author": b"Parquet Demo",
        b"created_date": b"2024-01-01",
        b"description": b"Sample dataset for schema demonstration",
    }
    table = table.replace_schema_metadata(metadata)

    pq.write_table(table, "sample.parquet")

    # Read and inspect schema
    parquet_file = pq.ParquetFile("sample.parquet")

    print("\nParquet Schema:")
    print(parquet_file.schema)

    print("\nCustom Metadata:")
    if parquet_file.schema_arrow.metadata:
        for key, value in parquet_file.schema_arrow.metadata.items():
            print(f"  {key.decode()}: {value.decode()}")

    print("\nFile Metadata:")
    metadata = parquet_file.metadata
    print(f"  Number of rows: {metadata.num_rows}")
    print(f"  Number of row groups: {metadata.num_row_groups}")
    print(f"  Number of columns: {metadata.num_columns}")
    print(f"  Format version: {metadata.format_version}")
    print(f"  Created by: {metadata.created_by}")

    print("\nColumn Statistics (Row Group 0):")
    for i in range(metadata.num_columns):
        col_meta = metadata.row_group(0).column(i)
        print(f"  Column {i} ({parquet_file.schema.names[i]}):")
        print(f"    Physical type: {col_meta.physical_type}")
        print(f"    Compression: {col_meta.compression}")
        print(f"    Total compressed size: {col_meta.total_compressed_size} bytes")
        if col_meta.statistics:
            stats = col_meta.statistics
            print(f"    Has min/max: {stats.has_min_max}")
            print(f"    Null count: {stats.null_count}")


def partitioned_dataset() -> None:
    """Demonstrate partitioned Parquet datasets."""
    print_section("4. Partitioned Datasets")

    # Create dataset with partitioning columns
    data = {
        "year": [2023, 2023, 2024, 2024, 2024],
        "month": [12, 12, 1, 1, 2],
        "sales": [1000, 1500, 2000, 2500, 3000],
        "product": ["A", "B", "A", "B", "A"],
    }
    df = pd.DataFrame(data)

    print("\nOriginal DataFrame:")
    print(df)

    # Write partitioned dataset
    df.to_parquet(
        "partitioned_data",
        engine="pyarrow",
        partition_cols=["year", "month"],
        index=False,
    )

    print("\nPartitioned directory structure:")
    for path in sorted(Path("partitioned_data").rglob("*.parquet")):
        print(f"  {path}")

    # Read entire partitioned dataset
    df_read = pd.read_parquet("partitioned_data", engine="pyarrow")
    print("\nDataFrame read from partitioned dataset:")
    print(df_read.sort_values(["year", "month"]).reset_index(drop=True))

    # Read specific partition
    df_filtered = pd.read_parquet(
        "partitioned_data", filters=[("year", "=", 2024)], engine="pyarrow"
    )
    print("\nFiltered read (year=2024):")
    print(df_filtered.sort_values(["year", "month"]).reset_index(drop=True))


def column_selection() -> None:
    """Demonstrate efficient column selection."""
    print_section("5. Column Selection and Filtering")

    # Create wide dataset
    data = {f"col_{i}": range(1000) for i in range(20)}
    df = pd.DataFrame(data)

    df.to_parquet("sample.parquet", engine="pyarrow", index=False)

    print(f"\nFull dataset: {df.shape[1]} columns, {df.shape[0]} rows")

    # Read only specific columns
    selected_cols = ["col_0", "col_5", "col_10"]
    df_subset = pd.read_parquet(
        "sample.parquet", columns=selected_cols, engine="pyarrow"
    )

    print(f"\nReading only {len(selected_cols)} columns: {selected_cols}")
    print(f"Result shape: {df_subset.shape}")
    print("\nFirst 5 rows of selected columns:")
    print(df_subset.head())


def main() -> None:
    """Main execution function."""
    print("=" * 70)
    print("  PARQUET FORMAT ILLUSTRATION IN PYTHON")
    print("=" * 70)
    print("\nApache Parquet is a columnar storage format optimized for")
    print("analytics workloads. It provides efficient compression and")
    print("encoding schemes.")

    # Clean up any existing files
    cleanup_files()

    # Run demonstrations
    basic_write_read()
    compression_comparison()
    schema_and_metadata()
    partitioned_dataset()
    column_selection()

    # Final cleanup
    cleanup_files()

    print("\n" + "=" * 70)
    print("  DEMONSTRATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
