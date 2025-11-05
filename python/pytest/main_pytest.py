# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pytest>=8.4.2",
# ]
# ///
"""
Pytest Example: Comprehensive Testing Framework Demonstration

This example showcases key pytest concepts:
1. Basic test functions and assertions
2. Fixtures for setup/teardown
3. Parametrized tests for multiple test cases
4. Test markers for organizing tests
5. Test classes for grouping related tests
6. Expected failures and exception testing
"""

import pytest


# Example 1: Basic Test Functions
def add(a, b):
    """Simple addition function to test."""
    return a + b


def divide(a, b):
    """Division function that can raise exceptions."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_add_positive_numbers():
    """Test addition with positive numbers."""
    result = add(2, 3)
    assert result == 5, f"Expected 5, got {result}"


def test_add_negative_numbers():
    """Test addition with negative numbers."""
    result = add(-2, -3)
    assert result == -5


def test_divide_normal():
    """Test normal division."""
    result = divide(10, 2)
    assert result == 5.0


def test_divide_by_zero():
    """Test that division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# Example 2: Fixtures for Setup/Teardown
@pytest.fixture
def sample_data():
    """Fixture that provides sample data for tests."""
    print("\n[FIXTURE] Setting up sample data")
    data = {"users": ["Alice", "Bob", "Charlie"], "count": 3}
    yield data  # Provide data to test
    print("[FIXTURE] Tearing down sample data")


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
    yield db
    db.close()


def test_sample_data_structure(sample_data):
    """Test using the sample_data fixture."""
    assert "users" in sample_data
    assert sample_data["count"] == 3
    assert len(sample_data["users"]) == 3


def test_database_operations(database_connection):
    """Test database operations using fixture."""
    db = database_connection
    db.insert("user_1", "Alice")
    assert db.get("user_1") == "Alice"


# Example 3: Parametrized Tests
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),  # Test case 1
        (0, 0, 0),  # Test case 2
        (-1, 1, 0),  # Test case 3
        (100, 200, 300),  # Test case 4
    ],
)
def test_add_parametrized(a, b, expected):
    """Test addition with multiple parameter sets."""
    result = add(a, b)
    assert result == expected, f"add({a}, {b}) should equal {expected}"


@pytest.mark.parametrize(
    "dividend,divisor,expected",
    [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (7, 2, 3.5),
    ],
)
def test_divide_parametrized(dividend, divisor, expected):
    """Test division with multiple parameter sets."""
    result = divide(dividend, divisor)
    assert result == expected


# Example 4: Test Markers
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


@pytest.mark.skip(reason="Demonstrating skip marker")
def test_skipped():
    """This test is intentionally skipped."""
    assert False  # This won't run


@pytest.mark.skipif(pytest.__version__ < "7.0", reason="Requires pytest 7.0+")
def test_conditional_skip():
    """Test skipped based on condition."""
    assert True


# Example 5: Test Classes
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


# Example 6: Expected Failures
@pytest.mark.xfail(reason="Demonstrating expected failure")
def test_expected_to_fail():
    """This test is expected to fail."""
    assert 1 == 2  # Intentionally wrong


@pytest.mark.xfail(strict=True, reason="Must fail")
def test_strict_xfail():
    """This test must fail, or the test suite will error."""
    assert False


# Example 7: Multiple Assertions with Good Error Messages
class TestStringOperations:
    """Test string operations with detailed assertions."""

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

    def test_string_methods(self):
        """Test various string methods."""
        text = "pytest is awesome"

        assert text.upper() == "PYTEST IS AWESOME"
        assert text.count("e") == 3, "Should have 3 'e' characters"
        assert "pytest" in text
        assert text.split() == ["pytest", "is", "awesome"]


# Main execution for demonstration
if __name__ == "__main__":
    print("=" * 70)
    print("Pytest Example - Running Tests with pytest")
    print("=" * 70)
    print("\nTo run these tests, use:")
    print("  uv run pytest main_pytest.py -v")
    print("\nOther useful commands:")
    print("  uv run pytest main_pytest.py -v -s          # Show print output")
    print("  uv run pytest main_pytest.py -v -k 'add'    # Run only 'add' tests")
    print("  uv run pytest main_pytest.py -v -m 'fast'   # Run only 'fast' tests")
    print("  uv run pytest main_pytest.py -v --tb=short  # Short traceback")
    print("=" * 70)

    # Run pytest programmatically
    import sys

    sys.exit(pytest.main([__file__, "-v", "-s"]))
