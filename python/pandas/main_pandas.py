# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas>=2.0.0",
#     "numpy>=1.24.0",
# ]
# ///
"""
Pandas Example: Comprehensive Data Analysis Library Demonstration

This example showcases key pandas concepts:
1. DataFrame creation and basic operations
2. Data selection and filtering
3. Data manipulation and transformation
4. Grouping and aggregation
5. Handling missing data
6. Merging and joining DataFrames
7. Time series operations
"""

import pandas as pd
import numpy as np


# Example 1: DataFrame Creation and Basic Operations
print("=" * 70)
print("Example 1: DataFrame Creation and Basic Operations")
print("=" * 70)

# Create a DataFrame from a dictionary
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


# Example 2: Data Selection and Filtering
print("\n" + "=" * 70)
print("Example 2: Data Selection and Filtering")
print("=" * 70)

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

# Using .loc (label-based) and .iloc (position-based)
print("\nUsing .loc[0, 'name']:", df.loc[0, "name"])
print("Using .iloc[0, 0]:", df.iloc[0, 0])


# Example 3: Data Manipulation and Transformation
print("\n" + "=" * 70)
print("Example 3: Data Manipulation and Transformation")
print("=" * 70)

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

# Sort by column
print("\nSort by salary (descending):")
sorted_df = df.sort_values("salary", ascending=False)
print(sorted_df[["name", "salary"]])


# Example 4: Grouping and Aggregation
print("\n" + "=" * 70)
print("Example 4: Grouping and Aggregation")
print("=" * 70)

# Create a more complex dataset for grouping
sales_data = {
    "region": ["East", "East", "West", "West", "East", "West", "North", "North"],
    "product": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "sales": [100, 150, 200, 120, 130, 180, 90, 110],
    "quantity": [10, 15, 20, 12, 13, 18, 9, 11],
}

sales_df = pd.DataFrame(sales_data)
print("\nSales DataFrame:")
print(sales_df)

# Group by single column
print("\nGroup by 'region' and sum:")
grouped = sales_df.groupby("region")["sales"].sum()
print(grouped)

# Group by multiple columns
print("\nGroup by 'region' and 'product', calculate mean:")
multi_grouped = sales_df.groupby(["region", "product"])["sales"].mean()
print(multi_grouped)

# Multiple aggregations
print("\nMultiple aggregations (sum, mean, count):")
agg_result = sales_df.groupby("region").agg(
    {"sales": ["sum", "mean"], "quantity": "sum"}
)
print(agg_result)


# Example 5: Handling Missing Data
print("\n" + "=" * 70)
print("Example 5: Handling Missing Data")
print("=" * 70)

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

# Drop rows with missing values
print("\nDrop rows with any missing values:")
dropped_df = df_nulls.dropna()
print(dropped_df)

# Forward fill
print("\nForward fill (use previous value):")
ffill_df = df_nulls.ffill()
print(ffill_df)


# Example 6: Merging and Joining DataFrames
print("\n" + "=" * 70)
print("Example 6: Merging and Joining DataFrames")
print("=" * 70)

# Create two DataFrames to merge
employees = pd.DataFrame(
    {
        "emp_id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "dept_id": [10, 20, 10, 30],
    }
)

departments = pd.DataFrame(
    {
        "dept_id": [10, 20, 30, 40],
        "dept_name": ["Sales", "Engineering", "HR", "Marketing"],
    }
)

print("\nEmployees DataFrame:")
print(employees)
print("\nDepartments DataFrame:")
print(departments)

# Inner join
print("\nInner join on 'dept_id':")
inner_merged = pd.merge(employees, departments, on="dept_id", how="inner")
print(inner_merged)

# Left join
print("\nLeft join on 'dept_id':")
left_merged = pd.merge(employees, departments, on="dept_id", how="left")
print(left_merged)


# Example 7: Time Series Operations
print("\n" + "=" * 70)
print("Example 7: Time Series Operations")
print("=" * 70)

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


# Example 8: Statistical Operations
print("\n" + "=" * 70)
print("Example 8: Statistical Operations")
print("=" * 70)

# Basic statistics
print("\nBasic statistics for original employee DataFrame:")
print(df[["age", "salary"]].describe())

# Correlation
print("\nCorrelation between age and salary:")
print(df[["age", "salary"]].corr())

# Value counts
print("\nValue counts for 'city':")
print(df["city"].value_counts())


# Example 9: String Operations
print("\n" + "=" * 70)
print("Example 9: String Operations")
print("=" * 70)

# String operations using .str accessor
print("\nOriginal names:")
print(df["name"])

print("\nUppercase names:")
print(df["name"].str.upper())

print("\nNames containing 'a' (case-insensitive):")
print(df[df["name"].str.contains("a", case=False)]["name"])

print("\nExtract first 3 characters:")
print(df["name"].str[:3])


# Example 10: Advanced Indexing
print("\n" + "=" * 70)
print("Example 10: Advanced Indexing")
print("=" * 70)

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


# Summary
print("\n" + "=" * 70)
print("Summary: Pandas Key Features Demonstrated")
print("=" * 70)
print("""
1. DataFrame Creation: Created DataFrames from dictionaries
2. Data Selection: Used [], .loc, .iloc for selecting data
3. Filtering: Applied boolean conditions to filter rows
4. Transformation: Added columns, applied functions, sorted data
5. Grouping: Used groupby() for aggregations
6. Missing Data: Handled NaN values with fillna(), dropna()
7. Merging: Combined DataFrames using merge()
8. Time Series: Worked with dates, resampling, rolling windows
9. Statistics: Computed descriptive statistics and correlations
10. String Operations: Manipulated text data with .str accessor
11. Indexing: Set single and multi-level indexes

Pandas is the cornerstone of data analysis in Python, providing powerful
and flexible data structures for working with structured data.
""")
