"""
List Comprehension Example: Elegant and Efficient Iteration in Python

This example showcases the power of list comprehensions:
1. Basic list comprehension vs traditional loops
2. List comprehension with filtering (if condition)
3. List comprehension with if-else expressions
4. Nested list comprehensions
5. Dictionary comprehensions
6. Set comprehensions
7. Generator expressions
8. Performance comparison
"""

import time


def print_section(title):
    """Helper function to print section headers."""
    print(f"\n{'=' * 70}")
    print(f"{title}")
    print(f"{'=' * 70}\n")


# Example 1: Basic List Comprehension vs Traditional Loop
def example_basic():
    """Demonstrates basic list comprehension syntax."""
    print_section("EXAMPLE 1: Basic List Comprehension vs Traditional Loop")

    # Traditional way: Using for loop
    print("Traditional Loop Approach:")
    numbers = [1, 2, 3, 4, 5]
    print(f"Input: {numbers}")
    squares_loop = []
    for n in numbers:
        squares_loop.append(n**2)
    print(f"Output: {squares_loop}")
    print("Code: Multiple lines needed\n")

    # List comprehension way: One-liner!
    print("List Comprehension Approach:")
    print(f"Input: {numbers}")
    squares_comp = [n**2 for n in numbers]  # Line 46: All in one line!
    print(f"Output: {squares_comp}")
    print("Code: [n**2 for n in numbers]  ← One line! ✨")


# Example 2: List Comprehension with Filtering (if condition)
def example_filtering():
    """Shows how to filter elements with if condition."""
    print_section("EXAMPLE 2: List Comprehension with Filtering")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Input: {numbers}\n")

    # Get only even numbers
    print("Filter: Only Even Numbers")
    evens = [n for n in numbers if n % 2 == 0]  # Line 63: if at the end filters
    print(f"Output: {evens}")
    print("Code: [n for n in numbers if n % 2 == 0]")
    print("      └─ 'if' at the end acts as a filter ✅\n")

    # Get squares of odd numbers
    print("Filter and Transform: Squares of Odd Numbers")
    odd_squares = [n**2 for n in numbers if n % 2 != 0]  # Line 71
    print(f"Output: {odd_squares}")
    print("Code: [n**2 for n in numbers if n % 2 != 0]")
    print("      └─ Transform (n**2) + Filter (if odd) 🔥")


# Example 3: List Comprehension with if-else
def example_if_else():
    """Demonstrates if-else expressions in list comprehensions."""
    print_section("EXAMPLE 3: List Comprehension with If-Else")

    numbers = [1, 2, 3, 4, 5]
    print(f"Input: {numbers}\n")

    # Label numbers as 'even' or 'odd'
    print("If-Else: Label Each Number")
    labels = ["even" if n % 2 == 0 else "odd" for n in numbers]  # Line 89
    print(f"Output: {labels}")
    print("Code: ['even' if n % 2 == 0 else 'odd' for n in numbers]")
    print("      └─ if-else goes BEFORE 'for' (ternary expression) 💡\n")

    # Different transformation based on condition
    print("If-Else: Different Transformations")
    result = [n * 2 if n % 2 == 0 else n * 3 for n in numbers]  # Line 97
    print(f"Output: {result}")
    print("Code: [n*2 if n % 2 == 0 else n*3 for n in numbers]")
    print("      └─ Even: multiply by 2, Odd: multiply by 3 🎯")


# Example 4: Nested List Comprehensions
def example_nested():
    """Shows nested list comprehensions for 2D data."""
    print_section("EXAMPLE 4: Nested List Comprehensions")

    # Create a 3x3 matrix
    print("Create a 3x3 Matrix:")
    matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]  # Line 111
    for row in matrix:
        print(f"  {row}")
    print("Code: [[i*3 + j + 1 for j in range(3)] for i in range(3)]")
    print("      └─ Outer loop (i): rows, Inner loop (j): columns\n")

    # Flatten a 2D list
    print("Flatten the Matrix:")
    flat = [num for row in matrix for num in row]  # Line 120
    print(f"Output: {flat}")
    print("Code: [num for row in matrix for num in row]")
    print("      └─ Read left to right: for each row, for each num ↔️\n")

    # Get diagonal elements
    print("Extract Diagonal Elements:")
    diagonal = [matrix[i][i] for i in range(3)]  # Line 128
    print(f"Output: {diagonal}")
    print("Code: [matrix[i][i] for i in range(3)]")
    print("      └─ Elements where row index == column index 📐")


# Example 5: Dictionary Comprehensions
def example_dict():
    """Demonstrates dictionary comprehensions."""
    print_section("EXAMPLE 5: Dictionary Comprehensions")

    # Create a dictionary from a list
    print("Create Dictionary: Number → Square")
    numbers = [1, 2, 3, 4, 5]
    squares_dict = {n: n**2 for n in numbers}  # Line 144: {key: value for ...}
    print(f"Input: {numbers}")
    print(f"Output: {squares_dict}")
    print("Code: {n: n**2 for n in numbers}")
    print("      └─ {key: value} format 🗝️\n")

    # Swap keys and values
    print("Swap Keys and Values:")
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in original.items()}  # Line 154
    print(f"Original: {original}")
    print(f"Swapped:  {swapped}")
    print("Code: {v: k for k, v in original.items()}")
    print("      └─ v becomes key, k becomes value 🔄\n")

    # Filter dictionary
    print("Filter Dictionary: Only Even Values")
    filtered = {k: v for k, v in squares_dict.items() if v % 2 == 0}  # Line 163
    print(f"Original: {squares_dict}")
    print(f"Filtered: {filtered}")
    print("Code: {k: v for k, v in dict.items() if v % 2 == 0}")
    print("      └─ Keep only key-value pairs where value is even ✂️")


# Example 6: Set Comprehensions
def example_set():
    """Shows set comprehensions for unique values."""
    print_section("EXAMPLE 6: Set Comprehensions")

    # Remove duplicates using set comprehension
    print("Remove Duplicates:")
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    unique = {n for n in numbers}  # Line 180: {expression for ...} (no colon)
    print(f"Input:  {numbers}")
    print(f"Output: {unique}")
    print("Code: {n for n in numbers}")
    print("      └─ Curly braces {} without key:value = set 🎲\n")

    # Get unique remainders
    print("Unique Remainders When Divided by 3:")
    remainders = {n % 3 for n in range(10)}  # Line 189
    print("Input range: 0-9")
    print(f"Output: {remainders}")
    print("Code: {n % 3 for n in range(10)}")
    print("      └─ Set automatically removes duplicates ♻️")


# Example 7: Generator Expressions
def example_generator():
    """Demonstrates generator expressions for memory efficiency."""
    print_section("EXAMPLE 7: Generator Expressions")

    # List comprehension: Creates entire list in memory
    print("List Comprehension (Eager):")
    numbers = range(5)
    squares_list = [n**2 for n in numbers]  # Line 204: Square brackets = list
    print("Input: range(5)")
    print(f"Output: {squares_list}")
    print(f"Type: {type(squares_list)}")
    print("Memory: Full list stored in memory 📦\n")

    # Generator expression: Lazy evaluation
    print("Generator Expression (Lazy):")
    squares_gen = (n**2 for n in numbers)  # Line 213: Parentheses = generator
    print("Input: range(5)")
    print(f"Output: {squares_gen}")
    print(f"Type: {type(squares_gen)}")
    print(f"Values: {list(squares_gen)}  ← Converted to list to display")
    print("Memory: Values generated on-demand, one at a time ⚡\n")

    # Memory usage comparison
    print("Memory Usage Comparison:")
    import sys

    list_comp = [n for n in range(1000)]
    gen_expr = (n for n in range(1000))
    print(f"List comprehension [1000 items]: {sys.getsizeof(list_comp)} bytes")
    print(f"Generator expression [1000 items]: {sys.getsizeof(gen_expr)} bytes")
    print("      └─ Generator is much more memory efficient! 💾")


# Example 8: Performance Comparison
def example_performance():
    """Compares performance of different approaches."""
    print_section("EXAMPLE 8: Performance Comparison")

    n = 1000000  # One million items
    print(f"Task: Square {n:,} numbers\n")

    # Traditional loop
    print("Approach 1: Traditional Loop")
    start = time.time()
    result_loop = []
    for i in range(n):
        result_loop.append(i**2)  # Line 247
    time_loop = time.time() - start
    print(f"Time: {time_loop:.4f}s")
    print("Code: for i in range(n): result.append(i**2)\n")

    # List comprehension
    print("Approach 2: List Comprehension")
    start = time.time()
    [i**2 for i in range(n)]  # Line 256
    time_comp = time.time() - start
    print(f"Time: {time_comp:.4f}s")
    print("Code: [i**2 for i in range(n)]\n")

    # Generator expression (consumed immediately)
    print("Approach 3: Generator Expression")
    start = time.time()
    list(i**2 for i in range(n))  # Line 264
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


# Main function
def main():
    """Main entry point for all examples."""
    print("\n🐍 List Comprehension Examples - Python's Elegant Syntax\n")

    example_basic()
    example_filtering()
    example_if_else()
    example_nested()
    example_dict()
    example_set()
    example_generator()
    example_performance()

    print("\n" + "=" * 70)
    print("✨ All demonstrations completed!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
