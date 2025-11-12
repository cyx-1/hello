# Parquet Format Illustration in Python

This example demonstrates Apache Parquet, a columnar storage file format optimized for analytics workloads. Parquet provides efficient compression, encoding schemes, and supports complex nested data structures.

## Requirements

- **Python**: >= 3.9
- **Dependencies**:
  - `pandas >= 2.0.0`
  - `pyarrow >= 14.0.0`

## Running the Example

```bash
uv run --with pandas --with pyarrow python main_parquet.py
```

## Key Concepts Demonstrated

1. **Basic Write/Read Operations** - Creating and reading Parquet files
2. **Compression Algorithms** - Comparing snappy, gzip, brotli, and uncompressed
3. **Schema and Metadata** - Inspecting file structure and custom metadata
4. **Partitioned Datasets** - Organizing data in hierarchical partitions
5. **Column Selection** - Efficient reading of specific columns

---

## Source Code with Annotations

### 1. Basic Write and Read (Lines 39-73)

**Key Code:**
```python
# Lines 45-52: Create sample DataFrame
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 42],
    'salary': [50000.0, 60000.0, 75000.0, 55000.0, 90000.0],
    'is_active': [True, True, False, True, True]
}
df = pd.DataFrame(data)

# Line 61: Write to Parquet file
df.to_parquet('sample.parquet', engine='pyarrow', index=False)

# Line 66: Read from Parquet file
df_read = pd.read_parquet('sample.parquet', engine='pyarrow')
```

**Output:**
```
======================================================================
  1. Basic Write and Read
======================================================================

Original DataFrame:
   id     name  age   salary  is_active
0   1    Alice   25  50000.0       True
1   2      Bob   30  60000.0       True
2   3  Charlie   35  75000.0      False
3   4    David   28  55000.0       True
4   5      Eve   42  90000.0       True

DataFrame shape: (5, 5)
Memory usage: 565 bytes

Parquet file written: sample.parquet (3310 bytes)

DataFrame read from Parquet:
   id     name  age   salary  is_active
0   1    Alice   25  50000.0       True
1   2      Bob   30  60000.0       True
2   3  Charlie   35  75000.0      False
3   4    David   28  55000.0       True
4   5      Eve   42  90000.0       True
Data types preserved: True
```

**📝 Annotation:**
- **Line 52**: Creating a DataFrame with mixed data types (int, string, float, boolean)
- **Line 61**: Writing to Parquet takes 565 bytes of in-memory data and stores it as 3310 bytes on disk (includes metadata and compression)
- **Line 66**: Reading preserves all data types exactly - this is a key advantage of Parquet over CSV
- **File size**: The Parquet file is larger than memory for small datasets due to metadata overhead, but this reverses with larger datasets

---

### 2. Compression Comparison (Lines 76-106)

**Key Code:**
```python
# Lines 81-87: Create test dataset with 10,000 rows
data = {
    'id': range(10000),
    'value': np.random.randn(10000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 10000),
    'timestamp': pd.date_range('2024-01-01', periods=10000, freq='min')
}

# Lines 93-95: Test different compression algorithms
compression_methods = ['snappy', 'gzip', 'brotli', None]
for compression in compression_methods:
    df.to_parquet(filename, compression=compression, engine='pyarrow', index=False)
```

**Output:**
```
======================================================================
  2. Compression Comparison
======================================================================

Test dataset: 10000 rows, 4 columns
Memory usage: 820,132 bytes

Compression Results:
Compression  File Size (bytes) Compression Ratio
     snappy             248221             3.30x
       gzip             194877             4.21x
     brotli             180811             4.54x
       none             297961             2.75x
```

**📝 Annotation:**
- **Line 87**: Original dataset uses ~820KB in memory
- **Line 95**: Testing 4 compression algorithms shows significant storage savings:
  - **Snappy** (default): Fast compression with 3.30x ratio - best for speed
  - **Gzip**: Moderate speed with 4.21x ratio - balanced approach
  - **Brotli**: Slower compression with best 4.54x ratio - optimal for storage
  - **None**: 2.75x ratio even without compression due to columnar format efficiency
- **Key insight**: Even uncompressed Parquet achieves 2.75x compression through columnar storage and encoding

---

### 3. Schema and Metadata (Lines 109-171)

**Key Code:**
```python
# Lines 114-122: Create DataFrame with diverse types
data = {
    'int_col': [1, 2, 3],
    'float_col': [1.1, 2.2, 3.3],
    'str_col': ['a', 'b', 'c'],
    'datetime_col': pd.date_range('2024-01-01', periods=3),
    'bool_col': [True, False, True],
    'nullable_int': pd.array([1, None, 3], dtype='Int64')
}

# Lines 126-131: Add custom metadata
metadata = {
    b'author': b'Parquet Demo',
    b'created_date': b'2024-01-01',
    b'description': b'Sample dataset for schema demonstration'
}
table = table.replace_schema_metadata(metadata)

# Lines 138-139: Inspect schema
parquet_file = pq.ParquetFile('sample.parquet')
print(parquet_file.schema)
```

**Output:**
```
======================================================================
  3. Schema and Metadata
======================================================================

Parquet Schema:
<pyarrow._parquet.ParquetSchema object at 0x7edf0346ebc0>
required group field_id=-1 schema {
  optional int64 field_id=-1 int_col;
  optional double field_id=-1 float_col;
  optional binary field_id=-1 str_col (String);
  optional int64 field_id=-1 datetime_col (Timestamp(isAdjustedToUTC=false, timeUnit=nanoseconds, is_from_converted_type=false, force_set_converted_type=false));
  optional boolean field_id=-1 bool_col;
  optional int64 field_id=-1 nullable_int;
}


Custom Metadata:
  author: Parquet Demo
  created_date: 2024-01-01
  description: Sample dataset for schema demonstration

File Metadata:
  Number of rows: 3
  Number of row groups: 1
  Number of columns: 6
  Format version: 2.6
  Created by: parquet-cpp-arrow version 22.0.0

Column Statistics (Row Group 0):
  Column 0 (int_col):
    Physical type: INT64
    Compression: SNAPPY
    Total compressed size: 112 bytes
    Has min/max: True
    Null count: 0
  Column 1 (float_col):
    Physical type: DOUBLE
    Compression: SNAPPY
    Total compressed size: 111 bytes
    Has min/max: True
    Null count: 0
  Column 2 (str_col):
    Physical type: BYTE_ARRAY
    Compression: SNAPPY
    Total compressed size: 72 bytes
    Has min/max: True
    Null count: 0
  Column 3 (datetime_col):
    Physical type: INT64
    Compression: SNAPPY
    Total compressed size: 115 bytes
    Has min/max: True
    Null count: 0
  Column 4 (bool_col):
    Physical type: BOOLEAN
    Compression: SNAPPY
    Total compressed size: 44 bytes
    Has min/max: True
    Null count: 0
  Column 5 (nullable_int):
    Physical type: INT64
    Compression: SNAPPY
    Total compressed size: 106 bytes
    Has min/max: True
    Null count: 1
```

**📝 Annotation:**
- **Lines 114-122**: Demonstrates various Python/Pandas types and how they map to Parquet physical types
- **Line 122**: `nullable_int` with `Int64` dtype properly handles NULL values (see null count: 1 in output)
- **Lines 126-131**: Custom metadata can store arbitrary key-value pairs (useful for data lineage)
- **Schema output**: Shows the logical schema with type information:
  - Python `int` → Parquet `INT64`
  - Python `float` → Parquet `DOUBLE`
  - Python `str` → Parquet `BYTE_ARRAY (String)`
  - Python `datetime` → Parquet `INT64 (Timestamp)`
  - Python `bool` → Parquet `BOOLEAN`
- **Column Statistics**: Parquet automatically tracks min/max values and null counts - crucial for query optimization and predicate pushdown
- **Line 160+**: Each column shows compression effectiveness (e.g., str_col: only 72 bytes for 3 strings)

---

### 4. Partitioned Datasets (Lines 174-220)

**Key Code:**
```python
# Lines 179-185: Create dataset suitable for partitioning
data = {
    'year': [2023, 2023, 2024, 2024, 2024],
    'month': [12, 12, 1, 1, 2],
    'sales': [1000, 1500, 2000, 2500, 3000],
    'product': ['A', 'B', 'A', 'B', 'A']
}

# Lines 192-197: Write with partitioning
df.to_parquet(
    'partitioned_data',
    engine='pyarrow',
    partition_cols=['year', 'month'],
    index=False
)

# Line 207: Read entire partitioned dataset
df_read = pd.read_parquet('partitioned_data', engine='pyarrow')

# Lines 212-216: Read with filter (partition pruning)
df_filtered = pd.read_parquet(
    'partitioned_data',
    filters=[('year', '=', 2024)],
    engine='pyarrow'
)
```

**Output:**
```
======================================================================
  4. Partitioned Datasets
======================================================================

Original DataFrame:
   year  month  sales product
0  2023     12   1000       A
1  2023     12   1500       B
2  2024      1   2000       A
3  2024      1   2500       B
4  2024      2   3000       A

Partitioned directory structure:
  partitioned_data/year=2023/month=12/a21058d70e2a40d08b7a39b7b6407b4d-0.parquet
  partitioned_data/year=2024/month=1/a21058d70e2a40d08b7a39b7b6407b4d-0.parquet
  partitioned_data/year=2024/month=2/a21058d70e2a40d08b7a39b7b6407b4d-0.parquet

DataFrame read from partitioned dataset:
   sales product  year month
0   1000       A  2023    12
1   1500       B  2023    12
2   2000       A  2024     1
3   2500       B  2024     1
4   3000       A  2024     2

Filtered read (year=2024):
   sales product  year month
0   2000       A  2024     1
1   2500       B  2024     1
2   3000       A  2024     2
```

**📝 Annotation:**
- **Lines 192-197**: `partition_cols=['year', 'month']` creates hierarchical directory structure
- **Directory structure output**: Shows Hive-style partitioning: `year=2023/month=12/`
  - This allows query engines to skip entire partitions without reading data
  - Each unique year/month combination gets its own directory
- **Line 207**: Reading treats all partitions as a single logical table
- **Lines 212-216**: Filter pushdown - only reads `year=2024` partitions
  - Query engine skips `year=2023/month=12/` directory entirely
  - Massive performance improvement for large datasets (only reads relevant partitions)
- **Key benefit**: For a dataset with years 2020-2024, filtering to 2024 reads only ~20% of files

---

### 5. Column Selection and Filtering (Lines 223-249)

**Key Code:**
```python
# Lines 228-229: Create wide dataset (20 columns)
data = {f'col_{i}': range(1000) for i in range(20)}
df = pd.DataFrame(data)

# Lines 237-238: Read only specific columns
selected_cols = ['col_0', 'col_5', 'col_10']
df_subset = pd.read_parquet('sample.parquet', columns=selected_cols, engine='pyarrow')
```

**Output:**
```
======================================================================
  5. Column Selection and Filtering
======================================================================

Full dataset: 20 columns, 1000 rows

Reading only 3 columns: ['col_0', 'col_5', 'col_10']
Result shape: (1000, 3)

First 5 rows of selected columns:
   col_0  col_5  col_10
0      0      0       0
1      1      1       1
2      2      2       2
3      3      3       3
4      4      4       4
```

**📝 Annotation:**
- **Line 229**: Creates dataset with 20 columns to demonstrate columnar storage benefits
- **Line 238**: `columns=['col_0', 'col_5', 'col_10']` reads only 3 of 20 columns
- **Key insight**: Parquet's columnar format means:
  - Reading 3 columns scans only ~15% of the file (vs 100% for row-based formats like CSV)
  - Decompression happens only for requested columns
  - Memory usage is proportional to columns read, not total columns in file
- **Real-world impact**: For a 100-column table, reading 5 columns is ~20x faster than CSV

---

## Understanding Parquet's Columnar Format

### Row-based vs Column-based Storage

**CSV (Row-based):**
```
id,name,age,salary
1,Alice,25,50000
2,Bob,30,60000
```
- Data stored row by row
- Reading any column requires scanning entire file
- Poor compression (mixed data types in each row)

**Parquet (Column-based):**
```
Column 'id':    [1, 2]
Column 'name':  ['Alice', 'Bob']
Column 'age':   [25, 30]
Column 'salary': [50000, 60000]
```
- Data stored column by column
- Reading specific columns only touches relevant data
- Excellent compression (homogeneous data types)

### Key Advantages Demonstrated

1. **Compression Efficiency** (Section 2): 3-4.5x compression ratios
2. **Schema Evolution** (Section 3): Rich type system with metadata
3. **Partition Pruning** (Section 4): Skip irrelevant data entirely
4. **Column Projection** (Section 5): Read only what you need
5. **Statistics** (Section 3): Min/max/null counts enable predicate pushdown

### Performance Characteristics

- **Best for**: Analytics queries reading few columns from many rows
- **Compression**: Brotli > Gzip > Snappy > None (in terms of size)
- **Speed**: Snappy > None > Gzip > Brotli (in terms of read/write speed)
- **Default**: Snappy offers best speed/size balance for most use cases

## Version Requirements

This example uses:
- **PyArrow >= 14.0.0**: For modern Parquet format 2.6 support and improved performance
- **Pandas >= 2.0.0**: For better nullable type support (`Int64` dtype used in line 122)

Older versions may work but could produce different compression ratios or lack nullable integer support.
