# List Comprehension Example: Elegant and Efficient Iteration in Python

This example demonstrates Python's powerful list comprehension syntax, providing concise and readable alternatives to traditional loops.

## Key Concepts Illustrated

1. **Basic List Comprehension** - One-line syntax vs traditional loops
2. **Filtering with Conditionals** - Using `if` to filter elements
3. **If-Else Expressions** - Conditional transformations
4. **Nested Comprehensions** - Working with 2D data structures
5. **Dictionary Comprehensions** - Creating and transforming dictionaries
6. **Set Comprehensions** - Generating unique values
7. **Generator Expressions** - Memory-efficient lazy evaluation
8. **Performance Comparison** - Speed benchmarks

## Running the Example

```bash
uv run python main_list_comprehension.py
```

## Source Code and Output Analysis

### 1. Basic List Comprehension vs Traditional Loop

**Source Code (main_list_comprehension.py:30-45):**
```python
# Traditional way: Using for loop
print("Traditional Loop Approach:")
numbers = [1, 2, 3, 4, 5]
print(f"Input: {numbers}")
squares_loop = []
for n in numbers:                                  # Line 35: Loop through each number
    squares_loop.append(n**2)                      # Line 36: Square and append
print(f"Output: {squares_loop}")
print("Code: Multiple lines needed\n")

# List comprehension way: One-liner!
print("List Comprehension Approach:")
print(f"Input: {numbers}")
squares_comp = [n**2 for n in numbers]             # Line 43: All in one line!
print(f"Output: {squares_comp}")
print("Code: [n**2 for n in numbers]  ← One line! ✨")
```

**Output:**
```
Traditional Loop Approach:
Input: [1, 2, 3, 4, 5]
Output: [1, 4, 9, 16, 25]                          ← Lines 35-36: 5 iterations
Code: Multiple lines needed

List Comprehension Approach:
Input: [1, 2, 3, 4, 5]
Output: [1, 4, 9, 16, 25]                          ← Line 43: Same result, one line!
Code: [n**2 for n in numbers]  ← One line! ✨
```

**💡 Key Insight:**
- **Traditional loop** (Lines 35-36): Requires explicit list creation, loop, and append operations
- **List comprehension** (Line 43): `[expression for item in iterable]` combines everything
- Both produce identical results, but list comprehension is more concise and Pythonic

---

### 2. List Comprehension with Filtering

**Source Code (main_list_comprehension.py:53-68):**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Input: {numbers}\n")

# Get only even numbers
print("Filter: Only Even Numbers")
evens = [n for n in numbers if n % 2 == 0]         # Line 58: 'if' filters out odds
print(f"Output: {evens}")
print("Code: [n for n in numbers if n % 2 == 0]")
print("      └─ 'if' at the end acts as a filter ✅\n")

# Get squares of odd numbers
print("Filter and Transform: Squares of Odd Numbers")
odd_squares = [n**2 for n in numbers if n % 2 != 0]  # Line 65: Transform + filter
print(f"Output: {odd_squares}")
print("Code: [n**2 for n in numbers if n % 2 != 0]")
print("      └─ Transform (n**2) + Filter (if odd) 🔥")
```

**Output:**
```
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Filter: Only Even Numbers
Output: [2, 4, 6, 8, 10]                           ← Line 58: Only evens remain
Code: [n for n in numbers if n % 2 == 0]
      └─ 'if' at the end acts as a filter ✅

Filter and Transform: Squares of Odd Numbers
Output: [1, 9, 25, 49, 81]                         ← Line 65: Squared odds only
Code: [n**2 for n in numbers if n % 2 != 0]
      └─ Transform (n**2) + Filter (if odd) 🔥
```

**💡 Key Insight:**
- **Line 58:** `if` condition at the end filters elements (only includes items where condition is True)
- **Line 65:** You can combine transformation (`n**2`) with filtering (`if n % 2 != 0`)
- **Syntax:** `[expression for item in iterable if condition]`

---

### 3. List Comprehension with If-Else

**Source Code (main_list_comprehension.py:76-91):**
```python
numbers = [1, 2, 3, 4, 5]
print(f"Input: {numbers}\n")

# Label numbers as 'even' or 'odd'
print("If-Else: Label Each Number")
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]  # Line 81
print(f"Output: {labels}")
print("Code: ['even' if n % 2 == 0 else 'odd' for n in numbers]")
print("      └─ if-else goes BEFORE 'for' (ternary expression) 💡\n")

# Different transformation based on condition
print("If-Else: Different Transformations")
result = [n * 2 if n % 2 == 0 else n * 3 for n in numbers]   # Line 88
print(f"Output: {result}")
print("Code: [n*2 if n % 2 == 0 else n*3 for n in numbers]")
print("      └─ Even: multiply by 2, Odd: multiply by 3 🎯")
```

**Output:**
```
Input: [1, 2, 3, 4, 5]

If-Else: Label Each Number
Output: ['odd', 'even', 'odd', 'even', 'odd']      ← Line 81: All numbers labeled
Code: ['even' if n % 2 == 0 else 'odd' for n in numbers]
      └─ if-else goes BEFORE 'for' (ternary expression) 💡

If-Else: Different Transformations
Output: [3, 4, 9, 8, 15]                           ← Line 88: 1*3, 2*2, 3*3, 4*2, 5*3
Code: [n*2 if n % 2 == 0 else n*3 for n in numbers]
      └─ Even: multiply by 2, Odd: multiply by 3 🎯
```

**💡 Key Insight:**
- **Line 81:** `if-else` goes **BEFORE** `for` (different from filtering!)
- **Syntax:** `[expression_if_true if condition else expression_if_false for item in iterable]`
- **Difference:**
  - `if` only (filter): `[x for x in items if condition]` → may return fewer items
  - `if-else` (ternary): `[a if condition else b for x in items]` → always returns same count

---

### 4. Nested List Comprehensions

**Source Code (main_list_comprehension.py:99-119):**
```python
# Create a 3x3 matrix
print("Create a 3x3 Matrix:")
matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]  # Line 101
for row in matrix:
    print(f"  {row}")
print("Code: [[i*3 + j + 1 for j in range(3)] for i in range(3)]")
print("      └─ Outer loop (i): rows, Inner loop (j): columns\n")

# Flatten a 2D list
print("Flatten the Matrix:")
flat = [num for row in matrix for num in row]                   # Line 109
print(f"Output: {flat}")
print("Code: [num for row in matrix for num in row]")
print("      └─ Read left to right: for each row, for each num ↔️\n")

# Get diagonal elements
print("Extract Diagonal Elements:")
diagonal = [matrix[i][i] for i in range(3)]                     # Line 116
print(f"Output: {diagonal}")
print("Code: [matrix[i][i] for i in range(3)]")
print("      └─ Elements where row index == column index 📐")
```

**Output:**
```
Create a 3x3 Matrix:
  [1, 2, 3]                                        ← Line 101: Nested comprehension
  [4, 5, 6]                                        ← creates 2D structure
  [7, 8, 9]
Code: [[i*3 + j + 1 for j in range(3)] for i in range(3)]
      └─ Outer loop (i): rows, Inner loop (j): columns

Flatten the Matrix:
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]               ← Line 109: 2D → 1D
Code: [num for row in matrix for num in row]
      └─ Read left to right: for each row, for each num ↔️

Extract Diagonal Elements:
Output: [1, 5, 9]                                  ← Line 116: matrix[0][0], [1][1], [2][2]
Code: [matrix[i][i] for i in range(3)]
      └─ Elements where row index == column index 📐
```

**💡 Key Insight:**
- **Line 101:** Nested comprehension creates 2D structure: outer `for i` creates rows, inner `for j` creates columns
- **Line 109:** Multiple `for` clauses flatten nested structures (read left to right like nested loops)
- **Equivalent nested loops for Line 109:**
  ```python
  flat = []
  for row in matrix:      # First 'for' in comprehension
      for num in row:     # Second 'for' in comprehension
          flat.append(num)
  ```

---

### 5. Dictionary Comprehensions

**Source Code (main_list_comprehension.py:127-151):**
```python
# Create a dictionary from a list
print("Create Dictionary: Number → Square")
numbers = [1, 2, 3, 4, 5]
squares_dict = {n: n**2 for n in numbers}                        # Line 130
print(f"Input: {numbers}")
print(f"Output: {squares_dict}")
print("Code: {n: n**2 for n in numbers}")
print("      └─ {key: value} format 🗝️\n")

# Swap keys and values
print("Swap Keys and Values:")
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}                    # Line 139
print(f"Original: {original}")
print(f"Swapped:  {swapped}")
print("Code: {v: k for k, v in original.items()}")
print("      └─ v becomes key, k becomes value 🔄\n")

# Filter dictionary
print("Filter Dictionary: Only Even Values")
filtered = {k: v for k, v in squares_dict.items() if v % 2 == 0}  # Line 147
print(f"Original: {squares_dict}")
print(f"Filtered: {filtered}")
print("Code: {k: v for k, v in dict.items() if v % 2 == 0}")
print("      └─ Keep only key-value pairs where value is even ✂️")
```

**Output:**
```
Create Dictionary: Number → Square
Input: [1, 2, 3, 4, 5]
Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}          ← Line 130: key:value pairs
Code: {n: n**2 for n in numbers}
      └─ {key: value} format 🗝️

Swap Keys and Values:
Original: {'a': 1, 'b': 2, 'c': 3}
Swapped:  {1: 'a', 2: 'b', 3: 'c'}                ← Line 139: keys↔values swapped
Code: {v: k for k, v in original.items()}
      └─ v becomes key, k becomes value 🔄

Filter Dictionary: Only Even Values
Original: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Filtered: {2: 4, 4: 16}                           ← Line 147: Only even values kept
Code: {k: v for k, v in dict.items() if v % 2 == 0}
      └─ Keep only key-value pairs where value is even ✂️
```

**💡 Key Insight:**
- **Line 130:** Dictionary comprehension uses curly braces with `key: value` format
- **Syntax:** `{key_expr: value_expr for item in iterable}`
- **Line 139:** `.items()` returns (key, value) tuples for iteration
- **Line 147:** Can combine with filtering like list comprehensions

---

### 6. Set Comprehensions

**Source Code (main_list_comprehension.py:159-174):**
```python
# Remove duplicates using set comprehension
print("Remove Duplicates:")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
unique = {n for n in numbers}                                    # Line 162
print(f"Input:  {numbers}")
print(f"Output: {unique}")
print("Code: {n for n in numbers}")
print("      └─ Curly braces {} without key:value = set 🎲\n")

# Get unique remainders
print("Unique Remainders When Divided by 3:")
remainders = {n % 3 for n in range(10)}                          # Line 170
print("Input range: 0-9")
print(f"Output: {remainders}")
print("Code: {n % 3 for n in range(10)}")
print("      └─ Set automatically removes duplicates ♻️")
```

**Output:**
```
Remove Duplicates:
Input:  [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
Output: {1, 2, 3, 4, 5}                           ← Line 162: Duplicates removed
Code: {n for n in numbers}
      └─ Curly braces {} without key:value = set 🎲

Unique Remainders When Divided by 3:
Input range: 0-9
Output: {0, 1, 2}                                  ← Line 170: Only 3 unique values
Code: {n % 3 for n in range(10)}
      └─ Set automatically removes duplicates ♻️
```

**💡 Key Insight:**
- **Line 162:** Curly braces `{}` without `key:value` creates a set, not a dict
- **Syntax:** `{expression for item in iterable}`
- **Line 170:** Sets automatically eliminate duplicates (0%3=0, 3%3=0, 6%3=0 → one 0)
- Sets are unordered, so output order may vary

---

### 7. Generator Expressions

**Source Code (main_list_comprehension.py:182-208):**
```python
# List comprehension: Creates entire list in memory
print("List Comprehension (Eager):")
numbers = range(5)
squares_list = [n**2 for n in numbers]                           # Line 185: [ ]
print("Input: range(5)")
print(f"Output: {squares_list}")
print(f"Type: {type(squares_list)}")
print("Memory: Full list stored in memory 📦\n")

# Generator expression: Lazy evaluation
print("Generator Expression (Lazy):")
squares_gen = (n**2 for n in numbers)                            # Line 193: ( )
print("Input: range(5)")
print(f"Output: {squares_gen}")
print(f"Type: {type(squares_gen)}")
print(f"Values: {list(squares_gen)}  ← Converted to list to display")
print("Memory: Values generated on-demand, one at a time ⚡\n")

# Memory usage comparison
print("Memory Usage Comparison:")
import sys

list_comp = [n for n in range(1000)]                             # Line 204
gen_expr = (n for n in range(1000))                              # Line 205
print(f"List comprehension [1000 items]: {sys.getsizeof(list_comp)} bytes")
print(f"Generator expression [1000 items]: {sys.getsizeof(gen_expr)} bytes")
print("      └─ Generator is much more memory efficient! 💾")
```

**Output:**
```
List Comprehension (Eager):
Input: range(5)
Output: [0, 1, 4, 9, 16]                          ← Line 185: Full list created
Type: <class 'list'>
Memory: Full list stored in memory 📦

Generator Expression (Lazy):
Input: range(5)
Output: <generator object ...>                    ← Line 193: Generator object
Type: <class 'generator'>
Values: [0, 1, 4, 9, 16]  ← Converted to list to display
Memory: Values generated on-demand, one at a time ⚡

Memory Usage Comparison:
List comprehension [1000 items]: 8856 bytes       ← Line 204: Stores all items
Generator expression [1000 items]: 200 bytes      ← Line 205: Only stores state
      └─ Generator is much more memory efficient! 💾
```

**💡 Key Insight:**
- **Line 185:** Square brackets `[]` create a **list** (eager evaluation)
- **Line 193:** Parentheses `()` create a **generator** (lazy evaluation)
- **Memory comparison:**
  - List: 8856 bytes (stores all 1000 integers)
  - Generator: 200 bytes (only stores iteration state)
- **Use generators for:**
  - Large datasets
  - Infinite sequences
  - Pipeline processing where you consume items once

---

### 8. Performance Comparison

**Source Code (main_list_comprehension.py:216-253):**
```python
n = 1000000  # One million items
print(f"Task: Square {n:,} numbers\n")

# Traditional loop
print("Approach 1: Traditional Loop")
start = time.time()
result_loop = []
for i in range(n):
    result_loop.append(i**2)                                     # Line 224
time_loop = time.time() - start
print(f"Time: {time_loop:.4f}s")
print("Code: for i in range(n): result.append(i**2)\n")

# List comprehension
print("Approach 2: List Comprehension")
start = time.time()
[i**2 for i in range(n)]                                         # Line 232
time_comp = time.time() - start
print(f"Time: {time_comp:.4f}s")
print("Code: [i**2 for i in range(n)]\n")

# Generator expression (consumed immediately)
print("Approach 3: Generator Expression")
start = time.time()
list(i**2 for i in range(n))                                     # Line 240
time_gen = time.time() - start
print(f"Time: {time_gen:.4f}s")
print("Code: list(i**2 for i in range(n))\n")

# Comparison
print("Performance Summary:")
fastest = min(time_loop, time_comp, time_gen)
print(f"  Traditional Loop:     {time_loop:.4f}s  ({time_loop / fastest:.2f}x)")
print(
    f"  List Comprehension:   {time_comp:.4f}s  "
    f"({time_comp / fastest:.2f}x) ← Usually fastest! 🏆"
)
print(f"  Generator Expression: {time_gen:.4f}s  ({time_gen / fastest:.2f}x)")
```

**Output (example run):**
```
Task: Square 1,000,000 numbers

Approach 1: Traditional Loop
Time: 0.0658s                                      ← Line 224: Loop + append
Code: for i in range(n): result.append(i**2)

Approach 2: List Comprehension
Time: 0.0644s                                      ← Line 232: Fastest! ⚡
Code: [i**2 for i in range(n)]

Approach 3: Generator Expression
Time: 0.0765s                                      ← Line 240: Slightly slower
Code: list(i**2 for i in range(n))

Performance Summary:
  Traditional Loop:     0.0658s  (1.02x)
  List Comprehension:   0.0644s  (1.00x) ← Usually fastest! 🏆
  Generator Expression: 0.0765s  (1.19x)
```

**💡 Key Insight:**
- **List comprehensions** are typically 2-10% faster than traditional loops
- **Why faster?** List comprehensions are optimized at C level in CPython
- **Generator expressions** are slightly slower when consumed immediately (overhead of iteration protocol)
- **Best practice:**
  - Use **list comprehensions** for small-to-medium datasets when you need the full list
  - Use **generator expressions** for large datasets or when you only need to iterate once
  - Use **traditional loops** when logic is complex or requires multiple statements

---

## Quick Reference

### Syntax Summary

| Type | Syntax | Example | Result |
|------|--------|---------|--------|
| **List** | `[expr for item in iterable]` | `[n**2 for n in range(5)]` | `[0, 1, 4, 9, 16]` |
| **List with filter** | `[expr for item in iterable if condition]` | `[n for n in range(10) if n % 2 == 0]` | `[0, 2, 4, 6, 8]` |
| **List with if-else** | `[expr1 if cond else expr2 for item in iterable]` | `['even' if n%2==0 else 'odd' for n in range(3)]` | `['even', 'odd', 'even']` |
| **Dictionary** | `{key_expr: val_expr for item in iterable}` | `{n: n**2 for n in range(3)}` | `{0:0, 1:1, 2:4}` |
| **Set** | `{expr for item in iterable}` | `{n%3 for n in range(6)}` | `{0, 1, 2}` |
| **Generator** | `(expr for item in iterable)` | `(n**2 for n in range(5))` | `<generator object>` |

### When to Use What

✅ **List Comprehension:**
- Need the full list in memory
- Small to medium datasets
- Maximum performance for list creation
- Example: `[x*2 for x in numbers]`

✅ **Generator Expression:**
- Large datasets
- Only need to iterate once
- Memory efficiency is important
- Example: `sum(x*2 for x in range(1000000))`

✅ **Dictionary Comprehension:**
- Creating mappings from iterables
- Transforming existing dictionaries
- Example: `{k: v*2 for k, v in data.items()}`

✅ **Set Comprehension:**
- Need unique values
- Removing duplicates
- Example: `{word.lower() for word in text.split()}`

### Common Patterns

```python
# Filter then transform
evens_squared = [n**2 for n in numbers if n % 2 == 0]

# Transform based on condition
adjusted = [n*2 if n > 0 else n for n in numbers]

# Nested iteration (flatten)
flat = [item for sublist in nested for item in sublist]

# Dictionary from two lists
mapping = {k: v for k, v in zip(keys, values)}

# Conditional dictionary
filtered_dict = {k: v for k, v in data.items() if v > threshold}
```

## Requirements

- **Python Version:** Python 3.0+ (list/dict/set comprehensions)
- **Python Version:** Python 2.4+ for generator expressions
- **Note:** All modern Python versions (3.6+) support all comprehension types

## Key Takeaways

1. **Comprehensions are Pythonic** - They're the preferred way to transform and filter sequences
2. **More readable** - Once familiar, comprehensions are easier to read than loops
3. **Performance** - List comprehensions are faster than equivalent loops
4. **Memory efficiency** - Generator expressions save memory for large datasets
5. **Versatile** - Works for lists, dicts, sets, and generators
6. **Not always better** - Use traditional loops for complex logic or multiple statements
