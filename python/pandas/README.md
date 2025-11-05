# Pandas Example: Comprehensive Data Analysis Library

This example demonstrates Python's `pandas` library, the most powerful and popular data analysis and manipulation tool in the Python ecosystem.

## Key Concepts Illustrated

1. **DataFrame Creation** - Creating DataFrames from dictionaries
2. **Data Selection** - Accessing columns and rows using [], .loc, .iloc
3. **Filtering** - Boolean indexing and complex conditions
4. **Data Transformation** - Adding columns, applying functions, sorting
5. **Grouping and Aggregation** - GroupBy operations and aggregations
6. **Missing Data** - Handling NaN values with fillna(), dropna(), ffill()
7. **Merging and Joining** - Combining DataFrames with merge()
8. **Time Series** - Working with dates, resampling, rolling windows
9. **Statistical Operations** - Descriptive statistics and correlations
10. **String Operations** - Text manipulation with .str accessor
11. **Advanced Indexing** - Single and multi-level indexes

## Requirements

- Python 3.11+
- pandas 2.0+
- numpy 1.24+

## Running the Example

```bash
# Run the example
uv run python main_pandas.py
```

## Source Code and Output Analysis

### 1. DataFrame Creation and Basic Operations

**Source Code (main_pandas.py:23-36):**
```python
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 28, 32],
    "city": ["New York", "San Francisco", "Los Angeles", "Chicago", "Boston"],
    "salary": [70000, 85000, 90000, 75000, 82000],
}

df = pd.DataFrame(data)
print("\nDataFrame created from dictionary:")
print(df)
print(f"\nShape: {df.shape}")  # (rows, columns)
print(f"Columns: {list(df.columns)}")
print(f"\nData types:\n{df.dtypes}")
```

**Output:**
```
DataFrame created from dictionary:
      name  age           city  salary
0    Alice   25       New York   70000      ← Line 30: DataFrame displays with index
1      Bob   30  San Francisco   85000
2  Charlie   35    Los Angeles   90000
3    David   28        Chicago   75000
4      Eve   32         Boston   82000

Shape: (5, 4)                                ← Line 33: 5 rows, 4 columns
Columns: ['name', 'age', 'city', 'salary']   ← Line 34: Column names

Data types:                                  ← Line 36: Each column's data type
name      object
age        int64
city      object
salary     int64
dtype: object
```

**Key Insight:**
- **Line 30:** `pd.DataFrame()` creates a DataFrame from a dictionary where keys become column names
- **Line 33:** `.shape` returns a tuple of (rows, columns)
- **Line 36:** `.dtypes` shows the data type of each column (object = string, int64 = integer)

---

### 2. Data Selection and Filtering

**Source Code (main_pandas.py:46-60):**
```python
# Select a single column
print("\nSelect 'name' column:")
print(df["name"])

# Select multiple columns
print("\nSelect 'name' and 'salary' columns:")
print(df[["name", "salary"]])

# Filter rows based on condition
print("\nFilter: People with age > 30:")
filtered_df = df[df["age"] > 30]
print(filtered_df)

# Multiple conditions
print("\nFilter: People with age > 28 AND salary > 80000:")
complex_filter = df[(df["age"] > 28) & (df["salary"] > 80000)]
print(complex_filter)
```

**Output:**
```
Select 'name' column:                        ← Line 48: Single column returns Series
0      Alice
1        Bob
2    Charlie
3      David
4        Eve
Name: name, dtype: object

Filter: People with age > 30:                ← Line 56: Boolean condition filters rows
      name  age         city  salary
2  Charlie   35  Los Angeles   90000
4      Eve   32       Boston   82000

Filter: People with age > 28 AND salary > 80000:  ← Line 61: Multiple conditions with &
      name  age           city  salary
1      Bob   30  San Francisco   85000
2  Charlie   35    Los Angeles   90000
4      Eve   32         Boston   82000
```

**Key Insight:**
- **Line 48:** Single brackets `df["name"]` returns a Series (single column)
- **Line 52:** Double brackets `df[["name", "salary"]]` returns a DataFrame (multiple columns)
- **Line 56:** Boolean indexing `df[df["age"] > 30]` filters rows based on condition
- **Line 61:** Multiple conditions require parentheses and `&` (AND) or `|` (OR) operators

---

### 3. Data Manipulation and Transformation

**Source Code (main_pandas.py:75-88):**
```python
# Add a new column
df["bonus"] = df["salary"] * 0.1
print("\nAdded 'bonus' column (10% of salary):")
print(df)

# Modify existing column
df["salary_in_k"] = df["salary"] / 1000
print("\nAdded 'salary_in_k' column:")
print(df[["name", "salary", "salary_in_k"]])

# Apply function to column
df["name_length"] = df["name"].apply(len)
print("\nAdded 'name_length' column:")
print(df[["name", "name_length"]])
```

**Output:**
```
Added 'bonus' column (10% of salary):        ← Line 77: New column calculated from existing
      name  age           city  salary   bonus
0    Alice   25       New York   70000  7000.0
1      Bob   30  San Francisco   85000  8500.0
2  Charlie   35    Los Angeles   90000  9000.0
3    David   28        Chicago   75000  7500.0
4      Eve   32         Boston   82000  8200.0

Added 'name_length' column:                  ← Line 86: Apply function to each element
      name  name_length
0    Alice            5
1      Bob            3
2  Charlie            7
3    David            5
4      Eve            3
```

**Key Insight:**
- **Line 76:** New columns can be created using vectorized operations (fast!)
- **Line 81:** Column operations are element-wise by default
- **Line 86:** `.apply()` applies a function to each element in a column
- **Line 92:** `.sort_values()` sorts DataFrame by specified column

---

### 4. Grouping and Aggregation

**Source Code (main_pandas.py:100-116):**
```python
sales_data = {
    "region": ["East", "East", "West", "West", "East", "West", "North", "North"],
    "product": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "sales": [100, 150, 200, 120, 130, 180, 90, 110],
    "quantity": [10, 15, 20, 12, 13, 18, 9, 11],
}

sales_df = pd.DataFrame(sales_data)

# Group by single column
print("\nGroup by 'region' and sum:")
grouped = sales_df.groupby("region")["sales"].sum()
print(grouped)

# Group by multiple columns
print("\nGroup by 'region' and 'product', calculate mean:")
multi_grouped = sales_df.groupby(["region", "product"])["sales"].mean()
print(multi_grouped)
```

**Output:**
```
Sales DataFrame:
  region product  sales  quantity
0   East       A    100        10
1   East       B    150        15
2   West       A    200        20
3   West       B    120        12
4   East       A    130        13
5   West       B    180        18
6  North       A     90         9
7  North       B    110        11

Group by 'region' and sum:                   ← Line 111: GroupBy aggregation
region
East     380                                 ← East: 100 + 150 + 130 = 380
North    200                                 ← North: 90 + 110 = 200
West     500                                 ← West: 200 + 120 + 180 = 500
Name: sales, dtype: int64

Group by 'region' and 'product', calculate mean:  ← Line 116: Multi-level grouping
region  product
East    A          115.0                     ← East A: (100 + 130) / 2 = 115
        B          150.0
North   A           90.0
        B          110.0
West    A          200.0
        B          150.0                     ← West B: (120 + 180) / 2 = 150
Name: sales, dtype: float64
```

**Source Code (main_pandas.py:119-124):**
```python
# Multiple aggregations
print("\nMultiple aggregations (sum, mean, count):")
agg_result = sales_df.groupby("region").agg(
    {"sales": ["sum", "mean"], "quantity": "sum"}
)
print(agg_result)
```

**Output:**
```
Multiple aggregations (sum, mean, count):    ← Line 121: Multiple aggregation functions
       sales             quantity
         sum        mean      sum
region
East     380  126.666667       38  ← East sales: sum=380, mean=126.67, quantity=38
North    200  100.000000       20
West     500  166.666667       50
```

**Key Insight:**
- **Line 111:** `.groupby()` groups data by one or more columns for aggregation
- **Line 116:** Multiple groupby columns create hierarchical indexes
- **Line 121:** `.agg()` allows applying multiple aggregation functions at once
- GroupBy operations are fundamental for data analysis and reporting

---

### 5. Handling Missing Data

**Source Code (main_pandas.py:133-162):**
```python
# Create DataFrame with missing values
data_with_nulls = {
    "A": [1, 2, np.nan, 4, 5],
    "B": [np.nan, 2, 3, 4, 5],
    "C": [1, 2, 3, np.nan, 5],
}

df_nulls = pd.DataFrame(data_with_nulls)
print("\nDataFrame with missing values:")
print(df_nulls)

# Check for missing values
print("\nMissing values per column:")
print(df_nulls.isnull().sum())

# Fill missing values
print("\nFill missing values with 0:")
filled_df = df_nulls.fillna(0)
print(filled_df)

# Forward fill
print("\nForward fill (use previous value):")
ffill_df = df_nulls.ffill()
print(ffill_df)
```

**Output:**
```
DataFrame with missing values:               ← Line 142: NaN represents missing data
     A    B    C
0  1.0  NaN  1.0                            ← Row 0: B is missing
1  2.0  2.0  2.0
2  NaN  3.0  3.0                            ← Row 2: A is missing
3  4.0  4.0  NaN                            ← Row 3: C is missing
4  5.0  5.0  5.0

Missing values per column:                   ← Line 146: Count nulls in each column
A    1
B    1
C    1
dtype: int64

Fill missing values with 0:                  ← Line 150: Replace NaN with 0
     A    B    C
0  1.0  0.0  1.0
1  2.0  2.0  2.0
2  0.0  3.0  3.0
3  4.0  4.0  0.0
4  5.0  5.0  5.0

Forward fill (use previous value):           ← Line 161: Use previous row's value
     A    B    C
0  1.0  NaN  1.0                            ← Row 0 B: No previous value, stays NaN
1  2.0  2.0  2.0
2  2.0  3.0  3.0                            ← Row 2 A: Filled with 2.0 from row 1
3  4.0  4.0  3.0                            ← Row 3 C: Filled with 3.0 from row 2
4  5.0  5.0  5.0
```

**Key Insight:**
- **Line 142:** `np.nan` represents missing values in pandas
- **Line 146:** `.isnull().sum()` counts missing values per column
- **Line 150:** `.fillna(0)` replaces all NaN with specified value
- **Line 156:** `.dropna()` removes rows containing any NaN
- **Line 161:** `.ffill()` propagates last valid value forward

---

### 6. Merging and Joining DataFrames

**Source Code (main_pandas.py:170-196):**
```python
# Create two DataFrames to merge
employees = pd.DataFrame(
    {
        "emp_id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "dept_id": [10, 20, 10, 30],
    }
)

departments = pd.DataFrame(
    {"dept_id": [10, 20, 30, 40], "dept_name": ["Sales", "Engineering", "HR", "Marketing"]}
)

# Inner join
print("\nInner join on 'dept_id':")
inner_merged = pd.merge(employees, departments, on="dept_id", how="inner")
print(inner_merged)
```

**Output:**
```
Employees DataFrame:
   emp_id     name  dept_id
0       1    Alice       10
1       2      Bob       20
2       3  Charlie       10
3       4    David       30

Departments DataFrame:
   dept_id    dept_name
0       10        Sales
1       20  Engineering
2       30           HR
3       40    Marketing                      ← Dept 40 has no employees

Inner join on 'dept_id':                     ← Line 190: Only matching rows
   emp_id     name  dept_id    dept_name
0       1    Alice       10        Sales   ← Matched on dept_id=10
1       2      Bob       20  Engineering   ← Matched on dept_id=20
2       3  Charlie       10        Sales   ← Matched on dept_id=10
3       4    David       30           HR   ← Matched on dept_id=30
                                           ← Dept 40 (Marketing) excluded - no match
```

**Key Insight:**
- **Line 190:** `pd.merge()` combines DataFrames based on common columns
- **Inner join:** Only keeps rows where the key exists in both DataFrames
- **Left join:** Keeps all rows from left DataFrame, fills NaN for missing right values
- The `on` parameter specifies the column(s) to join on

---

### 7. Time Series Operations

**Source Code (main_pandas.py:204-228):**
```python
# Create date range
date_range = pd.date_range(start="2024-01-01", periods=10, freq="D")
print("\nDate range:")
print(date_range)

# Create time series DataFrame
ts_data = {
    "date": date_range,
    "value": [100 + i * 5 + np.random.randint(-10, 10) for i in range(10)],
}

ts_df = pd.DataFrame(ts_data)
ts_df.set_index("date", inplace=True)
print("\nTime series DataFrame:")
print(ts_df)

# Resample to weekly frequency
print("\nResample to weekly frequency (mean):")
weekly = ts_df.resample("W").mean()
print(weekly)

# Rolling window calculations
print("\nRolling 3-day average:")
rolling_avg = ts_df.rolling(window=3).mean()
print(rolling_avg)
```

**Output:**
```
Date range:                                  ← Line 207: Generate sequence of dates
DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
               '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08',
               '2024-01-09', '2024-01-10'],
              dtype='datetime64[ns]', freq='D')

Time series DataFrame:                       ← Line 218: Date index for time series
            value
date
2024-01-01     99
2024-01-02    100
2024-01-03    116
...

Resample to weekly frequency (mean):         ← Line 222: Aggregate by week
                 value
date
2024-01-07  113.142857                       ← Week ending Jan 7: avg of 7 days
2024-01-14  132.333333                       ← Week ending Jan 14: avg of 3 days

Rolling 3-day average:                       ← Line 227: Moving window
                 value
date
2024-01-01         NaN                       ← Day 1: Not enough data (need 3)
2024-01-02         NaN                       ← Day 2: Not enough data (need 3)
2024-01-03  105.000000                       ← Day 3: avg(99, 100, 116) = 105
2024-01-04  108.333333                       ← Day 4: avg(100, 116, 109) = 108.33
2024-01-05  113.333333                       ← Day 5: avg(116, 109, 115) = 113.33
...
```

**Key Insight:**
- **Line 205:** `pd.date_range()` creates sequences of dates with specified frequency
- **Line 216:** Setting date as index enables time series operations
- **Line 222:** `.resample()` aggregates data to different time frequencies (D, W, M, Y)
- **Line 227:** `.rolling()` computes moving window calculations (smoothing, trends)

---

### 8. Statistical Operations

**Source Code (main_pandas.py:237-246):**
```python
# Basic statistics
print("\nBasic statistics for original employee DataFrame:")
print(df[["age", "salary"]].describe())

# Correlation
print("\nCorrelation between age and salary:")
print(df[["age", "salary"]].corr())

# Value counts
print("\nValue counts for 'city':")
print(df["city"].value_counts())
```

**Output:**
```
Basic statistics for original employee DataFrame:  ← Line 238: Descriptive statistics
             age        salary
count   5.000000      5.000000  ← Number of non-null entries
mean   30.000000  80400.000000  ← Average values
std     3.807887   7956.129712  ← Standard deviation
min    25.000000  70000.000000  ← Minimum values
25%    28.000000  75000.000000  ← 25th percentile (Q1)
50%    30.000000  82000.000000  ← 50th percentile (median)
75%    32.000000  85000.000000  ← 75th percentile (Q3)
max    35.000000  90000.000000  ← Maximum values

Correlation between age and salary:              ← Line 242: Correlation matrix
             age    salary
age     1.000000  0.940717                      ← Strong positive correlation (0.94)
salary  0.940717  1.000000                      ← Age and salary are highly correlated
```

**Key Insight:**
- **Line 238:** `.describe()` provides comprehensive statistical summary
- **Line 242:** `.corr()` calculates correlation coefficients (-1 to 1)
- **0.94 correlation:** Age and salary are strongly positively correlated
- **Line 246:** `.value_counts()` counts frequency of unique values

---

### 9. String Operations

**Source Code (main_pandas.py:258-265):**
```python
print("\nUppercase names:")
print(df["name"].str.upper())

print("\nNames containing 'a' (case-insensitive):")
print(df[df["name"].str.contains("a", case=False)]["name"])

print("\nExtract first 3 characters:")
print(df["name"].str[:3])
```

**Output:**
```
Uppercase names:                             ← Line 259: String method via .str
0      ALICE
1        BOB
2    CHARLIE
3      DAVID
4        EVE
Name: name, dtype: object

Names containing 'a' (case-insensitive):     ← Line 262: Filter by string pattern
0      Alice                                 ← Contains 'a'
2    Charlie                                 ← Contains 'a'
3      David                                 ← Contains 'a'
Name: name, dtype: object

Extract first 3 characters:                  ← Line 265: String slicing
0    Ali
1    Bob
2    Cha
3    Dav
4    Eve
Name: name, dtype: object
```

**Key Insight:**
- **Line 259:** `.str` accessor provides string methods for Series
- All standard Python string methods available: `.upper()`, `.lower()`, `.split()`, etc.
- **Line 262:** `.contains()` enables pattern matching with regex support
- **Line 265:** String slicing works element-wise on entire column

---

### 10. Advanced Indexing

**Source Code (main_pandas.py:273-285):**
```python
# Set index
indexed_df = df.set_index("name")
print("\nDataFrame with 'name' as index:")
print(indexed_df)

# Multi-index
multi_idx_df = sales_df.set_index(["region", "product"])
print("\nDataFrame with multi-index:")
print(multi_idx_df)

# Access data using multi-index
print("\nAccess 'East' region data:")
print(multi_idx_df.loc["East"])
```

**Output:**
```
DataFrame with 'name' as index:              ← Line 276: Custom index instead of 0,1,2...
         age           city  salary   bonus  salary_in_k  name_length
name
Alice     25       New York   70000  7000.0         70.0            5
Bob       30  San Francisco   85000  8500.0         85.0            3
Charlie   35    Los Angeles   90000  9000.0         90.0            7
David     28        Chicago   75000  7500.0         75.0            5
Eve       32         Boston   82000  8200.0         82.0            3

DataFrame with multi-index:                  ← Line 280: Hierarchical indexing
                sales  quantity
region product
East   A          100        10              ← Level 0: region, Level 1: product
       B          150        15
West   A          200        20
       B          120        12
...

Access 'East' region data:                   ← Line 285: Query by first index level
         sales  quantity
product
A          100        10                     ← All East region products
B          150        15
A          130        13
```

**Key Insight:**
- **Line 274:** `.set_index()` converts column(s) to index for faster lookups
- **Line 279:** Multi-level indexes organize hierarchical data efficiently
- **Line 285:** `.loc[]` enables label-based indexing with custom indexes
- Custom indexes make data access more intuitive and performant

---

## Summary

This comprehensive example demonstrates pandas' capabilities for:

✓ **Data Structure:** Creating and inspecting DataFrames
✓ **Data Access:** Selecting, filtering, and indexing data
✓ **Transformation:** Adding columns, applying functions, sorting
✓ **Aggregation:** GroupBy operations and statistical summaries
✓ **Data Quality:** Handling missing values effectively
✓ **Data Integration:** Merging and joining multiple datasets
✓ **Time Series:** Working with temporal data and resampling
✓ **Analysis:** Statistical operations and correlations
✓ **Text Processing:** String manipulation at scale
✓ **Advanced Features:** Multi-level indexing and hierarchical data

Pandas is the foundation of data analysis in Python, providing powerful and flexible tools for working with structured data. It's essential for data science, machine learning, and analytics workflows.

## Next Steps

To explore further:
- Try reading data from CSV/Excel files with `pd.read_csv()` and `pd.read_excel()`
- Experiment with pivot tables using `.pivot_table()`
- Learn about categorical data and efficient memory usage
- Explore visualization with pandas' `.plot()` integration
- Study advanced merging strategies (outer, cross joins)
