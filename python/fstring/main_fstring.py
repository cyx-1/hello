"""Comprehensive illustration of Python f-strings (formatted string literals).

F-strings were introduced in Python 3.6 (PEP 498) and provide a concise way
to embed expressions inside string literals using curly braces {}.
"""

from datetime import datetime


def main():
    print("=" * 60)
    print("Python F-String Illustration")
    print("=" * 60)
    print()

    # 1. Basic variable interpolation
    print("1. BASIC VARIABLE INTERPOLATION")
    print("-" * 40)
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
    print()

    # 2. Expressions in f-strings
    print("2. EXPRESSIONS IN F-STRINGS")
    print("-" * 40)
    a = 10
    b = 20
    print(f"The sum of {a} and {b} is {a + b}")
    print(f"The product is {a * b}")
    print(f"Is a greater than b? {a > b}")
    print()

    # 3. Formatting specifications - numbers
    print("3. NUMBER FORMATTING")
    print("-" * 40)
    pi = 3.141592653589793
    print(f"Pi with 2 decimals: {pi:.2f}")
    print(f"Pi with 4 decimals: {pi:.4f}")
    print(f"Pi in scientific notation: {pi:.2e}")

    large_num = 1234567890
    print(f"Large number with commas: {large_num:,}")
    print(f"Large number with underscores: {large_num:_}")
    print()

    # 4. Width and alignment
    print("4. WIDTH AND ALIGNMENT")
    print("-" * 40)
    item = "Apple"
    price = 1.25
    print(f"{'Item':<10} {'Price':>10}")  # Headers
    print(f"{item:<10} ${price:>9.2f}")  # Left align item, right align price

    # Center alignment
    title = "Menu"
    print(f"{title:^20}")  # Center in 20 chars
    print()

    # 5. Number bases (binary, octal, hex)
    print("5. NUMBER BASES")
    print("-" * 40)
    num = 42
    print(f"Decimal: {num}")
    print(f"Binary: {num:b}")
    print(f"Octal: {num:o}")
    print(f"Hexadecimal: {num:x}")
    print(f"Hexadecimal (uppercase): {num:X}")
    print()

    # 6. Date and time formatting
    print("6. DATE AND TIME FORMATTING")
    print("-" * 40)
    now = datetime.now()
    print(f"Current date and time: {now}")
    print(f"Formatted: {now:%Y-%m-%d %H:%M:%S}")
    print(f"Date only: {now:%B %d, %Y}")
    print(f"Time only: {now:%I:%M %p}")
    print()

    # 7. Dictionary and object access
    print("7. DICTIONARY AND OBJECT ACCESS")
    print("-" * 40)
    person = {"name": "Bob", "age": 25, "city": "New York"}
    print(f"Person: {person['name']}, {person['age']}, {person['city']}")

    # Object attribute access
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    point = Point(10, 20)
    print(f"Point coordinates: ({point.x}, {point.y})")
    print()

    # 8. Debug feature (Python 3.8+) - the = suffix
    print("8. DEBUG FEATURE (= SUFFIX)")
    print("-" * 40)
    x = 42
    y = 3.14
    name = "Python"
    print(f"{x=}")
    print(f"{y=}")
    print(f"{name=}")
    print(f"{x + y=}")  # Shows both expression and result
    print()

    # 9. Multiline f-strings
    print("9. MULTILINE F-STRINGS")
    print("-" * 40)
    name = "Charlie"
    age = 35
    occupation = "Engineer"
    message = f"""
    Name: {name}
    Age: {age}
    Occupation: {occupation}
    Summary: {name} is a {age}-year-old {occupation}.
    """
    print(message)

    # 10. Nested f-strings
    print("10. NESTED F-STRINGS")
    print("-" * 40)
    value = 42.123456
    decimals = 2
    print(f"Value with {decimals} decimals: {value:.{decimals}f}")

    width = 10
    align = ">"
    print(f"Right-aligned in {width} chars: {f'{value:{align}{width}.2f}'}")
    print()

    # 11. String conversion (!s, !r, !a)
    print("11. STRING CONVERSION FLAGS")
    print("-" * 40)
    text = "Hello\nWorld"
    print(f"String (!s): {text!s}")
    print(f"Repr (!r): {text!r}")  # Shows escape sequences
    print(f"ASCII (!a): {text!a}")
    print()

    # 12. Percentage formatting
    print("12. PERCENTAGE FORMATTING")
    print("-" * 40)
    ratio = 0.75
    print(f"Completion: {ratio:.0%}")
    print(f"Completion: {ratio:.1%}")
    print(f"Completion: {ratio:.2%}")
    print()

    # 13. Padding with zeros
    print("13. ZERO PADDING")
    print("-" * 40)
    number = 42
    print(f"Zero padded (5 digits): {number:05d}")
    print(f"Zero padded (8 digits): {number:08d}")
    print()

    # 14. Combining multiple format specs
    print("14. COMBINING FORMAT SPECIFICATIONS")
    print("-" * 40)
    value = 1234.5678
    print(
        f"Complex format: {value:>15,.2f}"
    )  # Right align, 15 width, comma separator, 2 decimals
    print(f"Complex format: {value:<15,.2f}")  # Left align version
    print(f"Complex format: {value:^15,.2f}")  # Center align version
    print()

    # 15. Escaping braces
    print("15. ESCAPING BRACES")
    print("-" * 40)
    value = 42
    print(f"To show braces, use double: {{value}} = {value}")
    print("This prints literal braces: {{nested}}")
    print()

    print("=" * 60)
    print("F-String illustration complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
