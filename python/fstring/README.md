# Python F-String Illustration

This example demonstrates the comprehensive features of Python f-strings (formatted string literals), introduced in Python 3.6 via PEP 498.

## Version Requirements

- **Python**: 3.6+ (basic f-strings)
- **Python**: 3.8+ (for the `=` debug feature shown in section 8)

## Running the Example

```bash
uv run python main_fstring.py
```

## Source Code and Output Correlation

### 1. Basic Variable Interpolation

The simplest use of f-strings is to embed variable values directly into strings.

**Source Code (lines 18-22):**
```python
18    name = "Alice"
19    age = 30
20    print(f"My name is {name} and I am {age} years old.")
```

**Output:**
```
My name is Alice and I am 30 years old.
```

**Explanation:** Variables are embedded in the string using `{variable_name}` syntax.

---

### 2. Expressions in F-Strings

F-strings can evaluate Python expressions inside the curly braces.

**Source Code (lines 24-30):**
```python
26    a = 10
27    b = 20
28    print(f"The sum of {a} and {b} is {a + b}")
29    print(f"The product is {a * b}")
30    print(f"Is a greater than b? {a > b}")
```

**Output:**
```
The sum of 10 and 20 is 30
The product is 200
Is a greater than b? False
```

**Explanation:** Expressions like `a + b`, `a * b`, and `a > b` are evaluated and their results are inserted into the string.

---

### 3. Number Formatting

F-strings support format specifications for precise control over number display.

**Source Code (lines 33-42):**
```python
36    pi = 3.141592653589793
37    print(f"Pi with 2 decimals: {pi:.2f}")
38    print(f"Pi with 4 decimals: {pi:.4f}")
39    print(f"Pi in scientific notation: {pi:.2e}")
40
41    large_num = 1234567890
42    print(f"Large number with commas: {large_num:,}")
43    print(f"Large number with underscores: {large_num:_}")
```

**Output:**
```
Pi with 2 decimals: 3.14
Pi with 4 decimals: 3.1416
Pi in scientific notation: 3.14e+00
Large number with commas: 1,234,567,890
Large number with underscores: 1_234_567_890
```

**Explanation:**
- `:.2f` formats a float to 2 decimal places
- `:.4f` formats a float to 4 decimal places
- `:.2e` formats in scientific notation
- `:,` adds comma separators for thousands
- `:_` adds underscore separators for thousands

---

### 4. Width and Alignment

Control the width and alignment of values within the string.

**Source Code (lines 45-53):**
```python
48    item = "Apple"
49    price = 1.25
50    print(f"{'Item':<10} {'Price':>10}")  # Headers
51    print(f"{item:<10} ${price:>9.2f}")  # Left align item, right align price
52
53    # Center alignment
54    title = "Menu"
55    print(f"{title:^20}")  # Center in 20 chars
```

**Output:**
```
Item            Price
Apple      $     1.25
        Menu
```

**Explanation:**
- `<10` left-aligns in a field of width 10
- `>10` right-aligns in a field of width 10
- `^20` center-aligns in a field of width 20
- `>9.2f` right-aligns with 2 decimal places in width 9

---

### 5. Number Bases (Binary, Octal, Hexadecimal)

Display integers in different number bases.

**Source Code (lines 58-65):**
```python
61    num = 42
62    print(f"Decimal: {num}")
63    print(f"Binary: {num:b}")
64    print(f"Octal: {num:o}")
65    print(f"Hexadecimal: {num:x}")
66    print(f"Hexadecimal (uppercase): {num:X}")
```

**Output:**
```
Decimal: 42
Binary: 101010
Octal: 52
Hexadecimal: 2a
Hexadecimal (uppercase): 2A
```

**Explanation:**
- `:b` converts to binary
- `:o` converts to octal
- `:x` converts to lowercase hexadecimal
- `:X` converts to uppercase hexadecimal

---

### 6. Date and Time Formatting

Format datetime objects using strftime-style format codes.

**Source Code (lines 68-75):**
```python
71    now = datetime.now()
72    print(f"Current date and time: {now}")
73    print(f"Formatted: {now:%Y-%m-%d %H:%M:%S}")
74    print(f"Date only: {now:%B %d, %Y}")
75    print(f"Time only: {now:%I:%M %p}")
```

**Output:**
```
Current date and time: 2025-11-04 14:31:47.810021
Formatted: 2025-11-04 14:31:47
Date only: November 04, 2025
Time only: 02:31 PM
```

**Explanation:** Use `:%` followed by strftime format codes:
- `%Y-%m-%d %H:%M:%S` for ISO format
- `%B %d, %Y` for month name, day, year
- `%I:%M %p` for 12-hour time with AM/PM

---

### 7. Dictionary and Object Access

Access dictionary keys and object attributes directly in f-strings.

**Source Code (lines 78-90):**
```python
81    person = {"name": "Bob", "age": 25, "city": "New York"}
82    print(f"Person: {person['name']}, {person['age']}, {person['city']}")
83
84    # Object attribute access
85    class Point:
86        def __init__(self, x, y):
87            self.x = x
88            self.y = y
89
90    point = Point(10, 20)
91    print(f"Point coordinates: ({point.x}, {point.y})")
```

**Output:**
```
Person: Bob, 25, New York
Point coordinates: (10, 20)
```

**Explanation:**
- Use `{dict['key']}` for dictionary access
- Use `{obj.attribute}` for object attribute access

---

### 8. Debug Feature (= Suffix)

**Requires Python 3.8+**

The `=` suffix shows both the expression and its value, useful for debugging.

**Source Code (lines 94-103):**
```python
97    x = 42
98    y = 3.14
99    name = "Python"
100   print(f"{x=}")
101   print(f"{y=}")
102   print(f"{name=}")
103   print(f"{x + y=}")  # Shows both expression and result
```

**Output:**
```
x=42
y=3.14
name='Python'
x + y=45.14
```

**Explanation:** Using `{variable=}` prints both the variable name and its value, making debugging easier. Works with expressions too.

---

### 9. Multiline F-Strings

F-strings can span multiple lines using triple quotes.

**Source Code (lines 106-115):**
```python
108   name = "Charlie"
109   age = 35
110   occupation = "Engineer"
111   message = f"""
112   Name: {name}
113   Age: {age}
114   Occupation: {occupation}
115   Summary: {name} is a {age}-year-old {occupation}.
116   """
117   print(message)
```

**Output:**
```
    Name: Charlie
    Age: 35
    Occupation: Engineer
    Summary: Charlie is a 35-year-old Engineer.
```

**Explanation:** Triple-quoted f-strings preserve formatting and allow multiple lines with embedded expressions.

---

### 10. Nested F-Strings

F-strings can be nested to create dynamic format specifications.

**Source Code (lines 119-126):**
```python
121   value = 42.123456
122   decimals = 2
123   print(f"Value with {decimals} decimals: {value:.{decimals}f}")
124
125   width = 10
126   align = ">"
127   print(f"Right-aligned in {width} chars: {f'{value:{align}{width}.2f}'}")
```

**Output:**
```
Value with 2 decimals: 42.12
Right-aligned in 10 chars:      42.12
```

**Explanation:** Use `{value:.{decimals}f}` to dynamically control decimal places. Nested f-strings allow building complex format strings programmatically.

---

### 11. String Conversion Flags

Use `!s`, `!r`, and `!a` for different string representations.

**Source Code (lines 129-136):**
```python
132   text = "Hello\nWorld"
133   print(f"String (!s): {text!s}")
134   print(f"Repr (!r): {text!r}")  # Shows escape sequences
135   print(f"ASCII (!a): {text!a}")
```

**Output:**
```
String (!s): Hello
World
Repr (!r): 'Hello\nWorld'
ASCII (!a): 'Hello\nWorld'
```

**Explanation:**
- `!s` calls `str()` (default behavior)
- `!r` calls `repr()`, showing the string representation including quotes and escape sequences
- `!a` calls `ascii()`, similar to `repr()` but escapes non-ASCII characters

---

### 12. Percentage Formatting

Display numbers as percentages with customizable precision.

**Source Code (lines 139-145):**
```python
141   ratio = 0.75
142   print(f"Completion: {ratio:.0%}")
143   print(f"Completion: {ratio:.1%}")
144   print(f"Completion: {ratio:.2%}")
```

**Output:**
```
Completion: 75%
Completion: 75.0%
Completion: 75.00%
```

**Explanation:** The `%` format specifier multiplies by 100 and adds a percent sign. The number before `%` specifies decimal places.

---

### 13. Zero Padding

Pad numbers with leading zeros.

**Source Code (lines 148-153):**
```python
150   number = 42
151   print(f"Zero padded (5 digits): {number:05d}")
152   print(f"Zero padded (8 digits): {number:08d}")
```

**Output:**
```
Zero padded (5 digits): 00042
Zero padded (8 digits): 00000042
```

**Explanation:** Use `0` followed by width (e.g., `05d`) to pad with zeros. The `d` specifies integer formatting.

---

### 14. Combining Format Specifications

Multiple format specifications can be combined for complex formatting.

**Source Code (lines 156-162):**
```python
158   value = 1234.5678
159   print(f"Complex format: {value:>15,.2f}")  # Right align, 15 width, comma separator, 2 decimals
160   print(f"Complex format: {value:<15,.2f}")  # Left align version
161   print(f"Complex format: {value:^15,.2f}")  # Center align version
```

**Output:**
```
Complex format:        1,234.57
Complex format: 1,234.57
Complex format:    1,234.57
```

**Explanation:** Format specs can combine:
- `>15` or `<15` or `^15` for alignment and width
- `,` for thousand separators
- `.2f` for 2 decimal places

---

### 15. Escaping Braces

Use double braces to display literal curly braces.

**Source Code (lines 165-170):**
```python
167   value = 42
168   print(f"To show braces, use double: {{value}} = {value}")
169   print(f"This prints literal braces: {{{{nested}}}}")
```

**Output:**
```
To show braces, use double: {value} = 42
This prints literal braces: {{nested}}
```

**Explanation:**
- `{{` becomes a literal `{`
- `}}` becomes a literal `}`
- Use `{{{{` to get `{{` in the output

---

## Key Takeaways

1. **F-strings** provide a concise and readable way to format strings in Python
2. They support **arbitrary Python expressions** inside `{}`
3. **Format specifications** use the syntax `{value:format_spec}`
4. The **debug feature** `{var=}` (Python 3.8+) is excellent for debugging
5. F-strings can be **nested** for dynamic formatting
6. They work seamlessly with **objects, dictionaries, and complex expressions**

## Further Reading

- [PEP 498 - Literal String Interpolation](https://www.python.org/dev/peps/pep-0498/)
- [Python Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
