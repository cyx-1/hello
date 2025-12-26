# Syrupy - Snapshot Testing for pytest

This example demonstrates **Syrupy**, a pytest plugin for snapshot testing. Snapshot testing captures the output of your code and compares it against stored snapshots on future runs, making it ideal for testing complex data structures, API responses, and more.

## What is Snapshot Testing?

Snapshot testing is a testing technique where you:
1. Run your code and capture its output
2. Store that output as a "snapshot"
3. On subsequent runs, compare the new output against the stored snapshot
4. If they match, the test passes; if they differ, you can review and update the snapshot

## Installation and Running

```bash
# Run the demonstration
uv run --script main_syrupy.py

# Create/update snapshots when code changes
UPDATE_SNAPSHOTS=1 uv run --script main_syrupy.py
```

## Key Source Code

Below are the important sections of the code with line number references:

### Lines 23-42: Data Structures for Testing

```python
@dataclass
class User:
    """Sample user data class."""
    id: int
    name: str
    email: str
    is_active: bool = True

@dataclass
class Product:
    """Sample product data class."""
    id: int
    name: str
    price: float
    tags: list[str]
```

These dataclasses represent typical domain objects you might test in a real application.

### Lines 44-59: Basic Snapshot Test

```python
def test_basic_snapshot(snapshot: Any) -> None:
    """
    Demonstrate basic snapshot testing with a dictionary.
    The 'snapshot' fixture is provided by syrupy.
    """
    user_data = {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "role": "admin",
        "created_at": "2024-01-15T10:30:00Z",
    }
    # Line 58: First snapshot assertion - will create snapshot on first run
    assert user_data == snapshot
```

**Line 58** creates the first snapshot. On initial run with `UPDATE_SNAPSHOTS=1`, this creates a snapshot file.

### Lines 62-70: Dataclass Snapshot

```python
def test_dataclass_snapshot(snapshot: Any) -> None:
    """Test snapshot with dataclass objects."""
    user = User(
        id=42, name="Bob Smith", email="bob@example.com", is_active=True
    )
    # Line 69: Snapshot will capture the dataclass representation
    assert user == snapshot
```

**Line 69** demonstrates snapshot testing with custom dataclass objects.

### Lines 86-97: Multiple Named Snapshots

```python
def test_multiple_snapshots(snapshot: Any) -> None:
    """Demonstrate multiple snapshots in a single test function."""
    user = User(id=1, name="Alice", email="alice@example.com")
    product = Product(
        id=101, name="Laptop", price=999.99, tags=["electronics", "computers"]
    )

    # Line 95: Each snapshot call gets a unique index
    assert user == snapshot(name="user_snapshot")
    assert product == snapshot(name="product_snapshot")
```

**Lines 95-96** show how to create multiple named snapshots within a single test, using the `name` parameter.

### Lines 127-146: Parameterized Tests with Snapshots

```python
@pytest.mark.parametrize(
    "product_id,name,price,tags",
    [
        (1, "Laptop", 999.99, ["electronics", "computers"]),
        (2, "Mouse", 25.50, ["electronics", "accessories"]),
        (3, "Keyboard", 75.00, ["electronics", "accessories", "mechanical"]),
    ],
)
def test_parametrized_snapshot(
    snapshot: Any, product_id: int, name: str, price: float, tags: list[str]
) -> None:
    """Each parameter set gets its own snapshot."""
    product = Product(id=product_id, name=name, price=price, tags=tags)
    # Line 145: Each parametrized run creates a separate snapshot
    assert product == snapshot
```

**Line 145** creates separate snapshots for each parameterized test case (3 snapshots total).

## Program Output

### First Run (Creating Snapshots)

When you run with `UPDATE_SNAPSHOTS=1`:

```
======================================================================
Syrupy Snapshot Testing Demonstration
======================================================================

Running pytest...

============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-9.0.2, pluggy-1.6.0
plugins: syrupy-5.0.0
collected 12 items

main_syrupy.py::test_basic_snapshot PASSED                               [  8%]
main_syrupy.py::test_dataclass_snapshot PASSED                           [ 16%]
main_syrupy.py::test_list_snapshot PASSED                                [ 25%]
main_syrupy.py::test_multiple_snapshots PASSED                           [ 33%]
main_syrupy.py::test_nested_structure_snapshot PASSED                    [ 41%]
main_syrupy.py::test_parametrized_snapshot[1-Laptop-999.99-tags0] PASSED [ 50%]
main_syrupy.py::test_parametrized_snapshot[2-Mouse-25.5-tags1] PASSED    [ 58%]
main_syrupy.py::test_parametrized_snapshot[3-Keyboard-75.0-tags2] PASSED [ 66%]
main_syrupy.py::test_function_output_snapshot PASSED                     [ 75%]
main_syrupy.py::test_api_response_snapshot PASSED                        [ 83%]
main_syrupy.py::test_list_comprehension_snapshot PASSED                  [ 91%]
main_syrupy.py::test_exception_message_snapshot PASSED                   [100%]

--------------------------- snapshot report summary ----------------------------
13 snapshots generated.
============================== 12 passed in 0.05s ==============================
```

**Note:** "13 snapshots generated" includes the 2 named snapshots from `test_multiple_snapshots` and 3 from the parameterized test.

### Subsequent Runs (Validating Against Snapshots)

When you run without the UPDATE flag:

```
============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-9.0.2, pluggy-1.6.0
plugins: syrupy-5.0.0
collected 12 items

main_syrupy.py::test_basic_snapshot PASSED                               [  8%]
main_syrupy.py::test_dataclass_snapshot PASSED                           [ 16%]
main_syrupy.py::test_list_snapshot PASSED                                [ 25%]
main_syrupy.py::test_multiple_snapshots PASSED                           [ 33%]
main_syrupy.py::test_nested_structure_snapshot PASSED                    [ 41%]
main_syrupy.py::test_parametrized_snapshot[1-Laptop-999.99-tags0] PASSED [ 50%]
main_syrupy.py::test_parametrized_snapshot[2-Mouse-25.5-tags1] PASSED    [ 58%]
main_syrupy.py::test_parametrized_snapshot[3-Keyboard-75.0-tags2] PASSED [ 66%]
main_syrupy.py::test_function_output_snapshot PASSED                     [ 75%]
main_syrupy.py::test_api_response_snapshot PASSED                        [ 83%]
main_syrupy.py::test_list_comprehension_snapshot PASSED                  [ 91%]
main_syrupy.py::test_exception_message_snapshot PASSED                   [100%]

--------------------------- snapshot report summary ----------------------------
13 snapshots passed.
============================== 12 passed in 0.04s ==============================
```

**Note:** "13 snapshots passed" indicates all snapshots matched their stored values.

## Generated Snapshot File

Snapshots are stored in `__snapshots__/main_syrupy.ambr`. Here's an excerpt showing how snapshots are stored:

```python
# name: test_basic_snapshot
  dict({
    'created_at': '2024-01-15T10:30:00Z',
    'email': 'alice@example.com',
    'id': 1,
    'name': 'Alice Johnson',
    'role': 'admin',
  })
# ---
# name: test_dataclass_snapshot
  User(id=42, name='Bob Smith', email='bob@example.com', is_active=True)
# ---
# name: test_list_snapshot
  list([
    User(id=1, name='Alice', email='alice@example.com', is_active=True),
    User(id=2, name='Bob', email='bob@example.com', is_active=True),
    User(id=3, name='Charlie', email='charlie@example.com', is_active=False),
  ])
# ---
# name: test_parametrized_snapshot[1-Laptop-999.99-tags0]
  Product(id=1, name='Laptop', price=999.99, tags=['electronics', 'computers'])
# ---
# name: test_parametrized_snapshot[2-Mouse-25.5-tags1]
  Product(id=2, name='Mouse', price=25.5, tags=['electronics', 'accessories'])
```

## Correlation Guide

| Test Function | Line | Snapshot Name | Description |
|--------------|------|---------------|-------------|
| `test_basic_snapshot` | 58 | `test_basic_snapshot` | Dictionary snapshot |
| `test_dataclass_snapshot` | 69 | `test_dataclass_snapshot` | Dataclass object snapshot |
| `test_list_snapshot` | 82 | `test_list_snapshot` | List of dataclass objects |
| `test_multiple_snapshots` | 95 | `test_multiple_snapshots[user_snapshot]` | Named snapshot #1 |
| `test_multiple_snapshots` | 96 | `test_multiple_snapshots[product_snapshot]` | Named snapshot #2 |
| `test_nested_structure_snapshot` | 123 | `test_nested_structure_snapshot` | Complex nested dict |
| `test_parametrized_snapshot` | 145 | `test_parametrized_snapshot[1-Laptop-999.99-tags0]` | Parameterized test #1 |
| `test_parametrized_snapshot` | 145 | `test_parametrized_snapshot[2-Mouse-25.5-tags1]` | Parameterized test #2 |
| `test_parametrized_snapshot` | 145 | `test_parametrized_snapshot[3-Keyboard-75.0-tags2]` | Parameterized test #3 |
| `test_function_output_snapshot` | 170 | `test_function_output_snapshot` | Function result snapshot |
| `test_api_response_snapshot` | 197 | `test_api_response_snapshot` | API response structure |
| `test_list_comprehension_snapshot` | 208 | `test_list_comprehension_snapshot` | Computed list result |
| `test_exception_message_snapshot` | 226 | `test_exception_message_snapshot` | Exception info snapshot |

## Key Features Demonstrated

1. **Basic Snapshot Testing** (Line 58): Simple dictionary comparison
2. **Dataclass Snapshots** (Line 69): Custom object snapshot
3. **List Snapshots** (Line 82): Collection of objects
4. **Multiple Named Snapshots** (Lines 95-96): Multiple assertions per test
5. **Nested Structures** (Line 123): Complex nested dictionaries
6. **Parameterized Tests** (Line 145): Each parameter set gets its own snapshot
7. **Function Output** (Line 170): Testing computed results
8. **API Responses** (Line 197): Simulated API testing
9. **List Comprehensions** (Line 208): Testing computed lists
10. **Exception Handling** (Line 226): Capturing error information

## When to Use Snapshot Testing

✅ **Good use cases:**
- Testing API response structures
- Validating complex data transformations
- Ensuring consistent serialization output
- Regression testing for complex objects
- Testing rendered output (HTML, JSON, etc.)

❌ **Not recommended for:**
- Values that change frequently (timestamps, random IDs)
- Large binary data
- Testing simple calculations (use assertions instead)
- When you need to test specific values (use explicit assertions)

## Version Requirements

- **Python**: 3.10+ (as specified in inline dependencies)
- **pytest**: 8.0.0+
- **syrupy**: 4.7.0+ (this example uses 5.0.0)

## Dependencies

This example uses inline script metadata (PEP 723) for dependency management:

```python
# /// script
# dependencies = [
#   "pytest>=8.0.0",
#   "syrupy>=4.7.0",
# ]
# ///
```

No `pyproject.toml` or `.python-version` files are needed when using `uv run --script`.
