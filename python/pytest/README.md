# Pytest Example: Comprehensive Testing Framework

This example demonstrates Python's `pytest` testing framework, the most popular testing tool in the Python ecosystem.

## Key Concepts Illustrated

1. **Basic Test Functions** - Simple test functions with assertions
2. **Fixtures** - Setup/teardown and dependency injection
3. **Parametrized Tests** - Running the same test with different inputs
4. **Test Markers** - Organizing and filtering tests
5. **Test Classes** - Grouping related tests
6. **Exception Testing** - Verifying that code raises expected errors
7. **Expected Failures** - Marking tests that are known to fail

## Requirements

- Python 3.11+
- pytest 8.0+

## Running the Example

```bash
# Run all tests
uv run pytest main_pytest.py -v

# Run all tests with output
uv run python main_pytest.py
```

## Source Code and Output Analysis

### 1. Basic Test Functions and Assertions

**Source Code (main_pytest.py:27-31):**
```python
def test_add_positive_numbers():
    """Test addition with positive numbers."""
    result = add(2, 3)
    assert result == 5, f"Expected 5, got {result}"
```

**Source Code (main_pytest.py:46-49):**
```python
def test_divide_by_zero():
    """Test that division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

**Output:**
```
main_pytest.py::test_add_positive_numbers PASSED
main_pytest.py::test_add_negative_numbers PASSED
main_pytest.py::test_divide_normal PASSED
main_pytest.py::test_divide_by_zero PASSED        ← Line 46-49: Exception caught successfully
```

**Key Insight:**
- **Line 30:** Simple `assert` statement checks if the result equals expected value
- **Line 48:** `pytest.raises()` context manager verifies that an exception is raised
- **Line 48:** `match` parameter validates the error message using regex

---

### 2. Fixtures for Setup and Teardown

**Source Code (main_pytest.py:52-59):**
```python
@pytest.fixture
def sample_data():
    """Fixture that provides sample data for tests."""
    print("\n[FIXTURE] Setting up sample data")
    data = {"users": ["Alice", "Bob", "Charlie"], "count": 3}
    yield data  # Provide data to test
    print("[FIXTURE] Tearing down sample data")
```

**Source Code (main_pytest.py:62-83):**
```python
@pytest.fixture
def database_connection():
    """Fixture simulating a database connection."""
    print("\n[FIXTURE] Opening database connection")

    class MockDB:
        def __init__(self):
            self.connected = True
            self.data = {}

        def insert(self, key, value):
            if not self.connected:
                raise RuntimeError("Database not connected")
            self.data[key] = value

        def get(self, key):
            return self.data.get(key)

        def close(self):
            self.connected = False
            print("[FIXTURE] Closing database connection")

    db = MockDB()
    yield db      # Line 77: Provide db to test
    db.close()    # Line 78: Cleanup after test
```

**Source Code (main_pytest.py:86-90):**
```python
def test_sample_data_structure(sample_data):    # Line 86: Fixture injected
    """Test using the sample_data fixture."""
    assert "users" in sample_data
    assert sample_data["count"] == 3
    assert len(sample_data["users"]) == 3
```

**Output:**
```
main_pytest.py::test_sample_data_structure
[FIXTURE] Setting up sample data               ← Line 55: Setup code runs
PASSED                                         ← Lines 86-90: Test runs
[FIXTURE] Tearing down sample data             ← Line 59: Teardown runs after test

main_pytest.py::test_database_operations
[FIXTURE] Opening database connection          ← Line 64: Setup code runs
PASSED                                         ← Test uses the fixture
[FIXTURE] Closing database connection          ← Line 78: Cleanup runs after test
```

**Key Insight:**
- **Line 52:** `@pytest.fixture` decorator marks a function as a fixture
- **Line 57:** `yield` provides the fixture value to tests and marks the transition point
- **Line 59:** Code after `yield` runs as teardown (cleanup)
- **Line 86:** Test function receives fixture by name matching parameter
- **Guarantee:** Teardown code always runs, even if the test fails

---

### 3. Parametrized Tests

**Source Code (main_pytest.py:104-115):**
```python
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),      # Test case 1
        (0, 0, 0),      # Test case 2
        (-1, 1, 0),     # Test case 3
        (100, 200, 300),# Test case 4
    ],
)
def test_add_parametrized(a, b, expected):
    """Test addition with multiple parameter sets."""
    result = add(a, b)
    assert result == expected, f"add({a}, {b}) should equal {expected}"
```

**Output:**
```
main_pytest.py::test_add_parametrized[1-2-3] PASSED         ← Test case 1: add(1, 2) == 3
main_pytest.py::test_add_parametrized[0-0-0] PASSED         ← Test case 2: add(0, 0) == 0
main_pytest.py::test_add_parametrized[-1-1-0] PASSED        ← Test case 3: add(-1, 1) == 0
main_pytest.py::test_add_parametrized[100-200-300] PASSED   ← Test case 4: add(100, 200) == 300
```

**Running only parametrized tests:**
```bash
$ uv run pytest main_pytest.py -v -k "parametrized"
```

**Output:**
```
collected 26 items / 19 deselected / 7 selected

main_pytest.py::test_add_parametrized[1-2-3] PASSED                      [ 14%]
main_pytest.py::test_add_parametrized[0-0-0] PASSED                      [ 28%]
main_pytest.py::test_add_parametrized[-1-1-0] PASSED                     [ 42%]
main_pytest.py::test_add_parametrized[100-200-300] PASSED                [ 57%]
main_pytest.py::test_divide_parametrized[10-2-5.0] PASSED                [ 71%]
main_pytest.py::test_divide_parametrized[9-3-3.0] PASSED                 [ 85%]
main_pytest.py::test_divide_parametrized[7-2-3.5] PASSED                 [100%]

======================= 7 passed, 19 deselected in 0.03s =======================
```

**Key Insight:**
- **Line 104:** `@pytest.mark.parametrize` decorator creates multiple test cases
- **Line 105:** First argument defines parameter names
- **Line 106-111:** Each tuple becomes a separate test case
- **Line 113:** Test function receives parameters as arguments
- **Result:** One test function generates 4 separate test runs
- **Benefit:** Reduces code duplication when testing multiple inputs

---

### 4. Test Markers

**Source Code (main_pytest.py:135-143):**
```python
@pytest.mark.slow
def test_slow_operation():
    """Test marked as slow (can be skipped with -m 'not slow')."""
    import time
    time.sleep(0.1)  # Simulate slow operation
    assert True

@pytest.mark.fast
def test_fast_operation():
    """Test marked as fast."""
    assert 1 + 1 == 2
```

**Source Code (main_pytest.py:146-148):**
```python
@pytest.mark.skip(reason="Demonstrating skip marker")
def test_skipped():
    """This test is intentionally skipped."""
    assert False  # This won't run
```

**Source Code (main_pytest.py:151-153):**
```python
@pytest.mark.skipif(pytest.__version__ < "7.0", reason="Requires pytest 7.0+")
def test_conditional_skip():
    """Test skipped based on condition."""
    assert True
```

**Marker Configuration (pyproject.toml:10-14):**
```toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "fast: marks tests as fast",
]
```

**Output:**
```
main_pytest.py::test_slow_operation PASSED
main_pytest.py::test_fast_operation PASSED
main_pytest.py::test_skipped SKIPPED (Demonstrating skip marker)  ← Line 146: Skipped
main_pytest.py::test_conditional_skip PASSED                      ← Line 151: Not skipped (pytest >= 7.0)
```

**Running only fast tests:**
```bash
$ uv run pytest main_pytest.py -v -m "fast"
```

**Running all except slow tests:**
```bash
$ uv run pytest main_pytest.py -v -m "not slow"
```

**Key Insight:**
- **Line 135:** `@pytest.mark.slow` adds custom marker to organize tests
- **Line 146:** `@pytest.mark.skip` unconditionally skips a test
- **Line 151:** `@pytest.mark.skipif` conditionally skips based on a boolean expression
- **pyproject.toml:** Register custom markers to avoid warnings
- **Use case:** Organize tests and run specific subsets (e.g., skip slow tests in CI)

---

### 5. Test Classes

**Source Code (main_pytest.py:157-174):**
```python
class TestCalculator:
    """Group related tests in a class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Automatically runs before each test method."""
        print("\n[CLASS FIXTURE] Setting up calculator test")
        self.calculator_name = "TestCalculator"

    def test_addition_in_class(self):
        """Test addition within a test class."""
        assert add(5, 5) == 10

    def test_division_in_class(self):
        """Test division within a test class."""
        assert divide(20, 4) == 5.0

    @pytest.mark.parametrize("a,b", [(1, 1), (2, 2), (3, 3)])
    def test_add_same_numbers(self, a, b):
        """Parametrized test within a class."""
        result = add(a, b)
        assert result == a + b
```

**Output:**
```
main_pytest.py::TestCalculator::test_addition_in_class
[CLASS FIXTURE] Setting up calculator test     ← Line 165: Setup runs for each test
PASSED
main_pytest.py::TestCalculator::test_division_in_class
[CLASS FIXTURE] Setting up calculator test     ← Line 165: Setup runs again
PASSED
main_pytest.py::TestCalculator::test_add_same_numbers[1-1]
[CLASS FIXTURE] Setting up calculator test     ← Line 165: Setup for parametrized test 1
PASSED
main_pytest.py::TestCalculator::test_add_same_numbers[2-2]
[CLASS FIXTURE] Setting up calculator test     ← Line 165: Setup for parametrized test 2
PASSED
main_pytest.py::TestCalculator::test_add_same_numbers[3-3]
[CLASS FIXTURE] Setting up calculator test     ← Line 165: Setup for parametrized test 3
PASSED
```

**Key Insight:**
- **Line 157:** Test classes must start with `Test` prefix
- **Line 161:** `autouse=True` makes the fixture run automatically before each test method
- **Line 165:** Setup code runs before each test method in the class
- **Line 174:** Can combine class tests with parametrization
- **Benefit:** Group related tests together and share common setup

---

### 6. Expected Failures (xfail)

**Source Code (main_pytest.py:177-185):**
```python
@pytest.mark.xfail(reason="Demonstrating expected failure")
def test_expected_to_fail():
    """This test is expected to fail."""
    assert 1 == 2  # Intentionally wrong

@pytest.mark.xfail(strict=True, reason="Must fail")
def test_strict_xfail():
    """This test must fail, or the test suite will error."""
    assert False
```

**Output:**
```
main_pytest.py::test_expected_to_fail XFAIL (Demonstrating expected ...)  ← Line 177: Expected to fail
main_pytest.py::test_strict_xfail XFAIL (Must fail)                       ← Line 182: Strict xfail

=================== 23 passed, 1 skipped, 2 xfailed in 0.27s ===================
```

**Key Insight:**
- **Line 177:** `@pytest.mark.xfail` marks a test as expected to fail
- **Line 182:** `strict=True` means the test MUST fail, or it's an error
- **Use case:** Document known bugs or features not yet implemented
- **Difference from skip:** xfail still runs the test; skip doesn't run it at all

---

### 7. Multiple Assertions with Good Error Messages

**Source Code (main_pytest.py:194-206):**
```python
def test_string_concatenation(self):
    """Test string concatenation with multiple assertions."""
    first = "Hello"
    second = "World"
    result = first + " " + second

    assert isinstance(result, str), "Result should be a string"
    assert len(result) == 11, f"Expected length 11, got {len(result)}"
    assert result == "Hello World", f"Expected 'Hello World', got '{result}'"
    assert result.startswith("Hello"), "Should start with 'Hello'"
    assert result.endswith("World"), "Should end with 'World'"
```

**Output:**
```
main_pytest.py::TestStringOperations::test_string_concatenation PASSED
main_pytest.py::TestStringOperations::test_string_methods PASSED
```

**Key Insight:**
- **Lines 200-204:** Multiple assertions provide detailed validation
- **Lines 201-203:** Custom error messages help debug failures
- **Best practice:** Include descriptive messages for assertions
- **Pytest advantage:** Provides detailed output showing actual vs expected values

---

## Test Summary

**Final Output:**
```
=================== 23 passed, 1 skipped, 2 xfailed in 0.27s ===================
```

| Status | Count | Description |
|--------|-------|-------------|
| PASSED | 23 | Tests that passed successfully |
| SKIPPED | 1 | Tests intentionally skipped |
| XFAIL | 2 | Tests that failed as expected |

## Useful Pytest Commands

```bash
# Run all tests verbosely
uv run pytest main_pytest.py -v

# Show print output (fixtures print statements)
uv run pytest main_pytest.py -v -s

# Run tests matching a keyword
uv run pytest main_pytest.py -v -k "add"

# Run tests with specific marker
uv run pytest main_pytest.py -v -m "fast"

# Exclude tests with specific marker
uv run pytest main_pytest.py -v -m "not slow"

# Show short traceback on failures
uv run pytest main_pytest.py -v --tb=short

# Stop at first failure
uv run pytest main_pytest.py -x

# Run the last failed tests
uv run pytest main_pytest.py --lf

# Run tests in parallel (requires pytest-xdist)
uv run pytest main_pytest.py -n auto
```

## Key Takeaways

1. **`assert` statement** - Simple and powerful test assertions
2. **`@pytest.fixture`** - Setup/teardown with dependency injection
3. **`@pytest.mark.parametrize`** - Test same function with different inputs
4. **`pytest.raises()`** - Test that exceptions are raised correctly
5. **Test markers** - Organize and filter tests (`@pytest.mark.*`)
6. **Test classes** - Group related tests with `class Test*`
7. **`xfail`** - Mark tests expected to fail

## When to Use Pytest

**Good for:**
- Unit testing individual functions and classes
- Integration testing with fixtures for setup/teardown
- Parametrized testing with many input combinations
- Organizing large test suites with markers
- Test-driven development (TDD)

**Advantages over unittest:**
- Simpler syntax (just `assert`, no `self.assertEqual()`)
- Powerful fixtures with dependency injection
- Better parametrization support
- Rich plugin ecosystem
- More detailed failure messages

## Version Requirements

This example requires:
- **Python 3.11+** (for general compatibility)
- **pytest 8.0+** (tested with pytest 8.4.2)

No special features require newer versions; this works with any recent pytest.
