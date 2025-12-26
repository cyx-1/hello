#!/usr/bin/env python3
"""
Demonstration of Syrupy snapshot testing for pytest.

Syrupy is a pytest plugin that enables snapshot testing - a technique where you
capture the output of your code and compare it against stored snapshots on future runs.
This is particularly useful for testing complex data structures, API responses, and more.

# /// script
# dependencies = [
#   "pytest>=8.0.0",
#   "syrupy>=4.7.0",
# ]
# ///
"""

from dataclasses import dataclass
from typing import Any

import pytest


# Line 23: Define sample data structures for testing
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


# Line 44: Test 1 - Basic snapshot testing with a dictionary
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


# Line 62: Test 2 - Snapshot testing with custom objects
def test_dataclass_snapshot(snapshot: Any) -> None:
    """Test snapshot with dataclass objects."""
    user = User(id=42, name="Bob Smith", email="bob@example.com", is_active=True)
    # Line 69: Snapshot will capture the dataclass representation
    assert user == snapshot


# Line 73: Test 3 - Snapshot testing with lists
def test_list_snapshot(snapshot: Any) -> None:
    """Test snapshot with a list of objects."""
    users = [
        User(id=1, name="Alice", email="alice@example.com"),
        User(id=2, name="Bob", email="bob@example.com"),
        User(id=3, name="Charlie", email="charlie@example.com", is_active=False),
    ]
    # Line 82: Snapshot will capture the entire list structure
    assert users == snapshot


# Line 86: Test 4 - Multiple snapshots in a single test
def test_multiple_snapshots(snapshot: Any) -> None:
    """Demonstrate multiple snapshots in a single test function."""
    user = User(id=1, name="Alice", email="alice@example.com")
    product = Product(
        id=101, name="Laptop", price=999.99, tags=["electronics", "computers"]
    )

    # Line 95: Each snapshot call gets a unique index
    assert user == snapshot(name="user_snapshot")
    assert product == snapshot(name="product_snapshot")


# Line 100: Test 5 - Snapshot with nested data structures
def test_nested_structure_snapshot(snapshot: Any) -> None:
    """Test snapshot with complex nested structures."""
    order = {
        "order_id": "ORD-12345",
        "customer": {
            "id": 1,
            "name": "Alice Johnson",
            "email": "alice@example.com",
        },
        "items": [
            {"product_id": 101, "name": "Laptop", "quantity": 1, "price": 999.99},
            {
                "product_id": 102,
                "name": "Mouse",
                "quantity": 2,
                "price": 25.50,
            },
        ],
        "total": 1050.99,
        "status": "confirmed",
    }
    # Line 123: Snapshot captures the entire nested structure
    assert order == snapshot


# Line 127: Test 6 - Parameterized tests with snapshots
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
    """
    Demonstrate snapshot testing with parameterized tests.
    Each parameter set gets its own snapshot.
    """
    product = Product(id=product_id, name=name, price=price, tags=tags)
    # Line 145: Each parametrized run creates a separate snapshot
    assert product == snapshot


# Line 149: Test 7 - Snapshot with function output
def calculate_statistics(numbers: list[float]) -> dict[str, float]:
    """Calculate basic statistics for a list of numbers."""
    if not numbers:
        return {"count": 0, "sum": 0.0, "mean": 0.0, "min": 0.0, "max": 0.0}

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }


def test_function_output_snapshot(snapshot: Any) -> None:
    """Test snapshot of function output."""
    numbers = [10.5, 20.3, 15.7, 8.9, 12.1, 18.4, 9.6]
    stats = calculate_statistics(numbers)
    # Line 170: Snapshot captures the computed statistics
    assert stats == snapshot


# Line 174: Test 8 - Snapshot with API-like response
def test_api_response_snapshot(snapshot: Any) -> None:
    """Simulate an API response and snapshot it."""
    api_response = {
        "status": "success",
        "code": 200,
        "data": {
            "users": [
                {"id": 1, "name": "Alice", "active": True},
                {"id": 2, "name": "Bob", "active": True},
                {"id": 3, "name": "Charlie", "active": False},
            ],
            "total_count": 3,
            "page": 1,
            "per_page": 10,
        },
        "metadata": {
            "timestamp": "2024-01-15T10:30:00Z",
            "version": "v2",
        },
    }
    # Line 197: Snapshot the entire API response structure
    assert api_response == snapshot


# Line 201: Test 9 - Snapshot with list comprehension result
def test_list_comprehension_snapshot(snapshot: Any) -> None:
    """Test snapshot with result from list comprehension."""
    numbers = list(range(1, 11))
    # Generate squares of even numbers
    result = [{"number": n, "square": n**2} for n in numbers if n % 2 == 0]
    # Line 208: Snapshot the computed list
    assert result == snapshot


# Line 212: Test 10 - Snapshot with error handling
def test_exception_message_snapshot(snapshot: Any) -> None:
    """Capture exception messages in snapshots."""
    try:
        # Intentionally cause an exception
        _ = 10 / 0
        error_info = None
    except ZeroDivisionError as e:
        error_info = {
            "error_type": type(e).__name__,
            "error_message": str(e),
            "handled": True,
        }
    # Line 226: Snapshot the error information
    assert error_info == snapshot


if __name__ == "__main__":
    # Line 231: Entry point - run pytest programmatically
    import sys

    print("=" * 70)
    print("Syrupy Snapshot Testing Demonstration")
    print("=" * 70)
    print("\nThis script demonstrates snapshot testing with Syrupy.")
    print("Run this with: uv run pytest python/syrupy/main_syrupy.py -v\n")
    print("Key features demonstrated:")
    print("  1. Basic snapshot testing (Line 58)")
    print("  2. Snapshots with dataclasses (Line 69)")
    print("  3. List snapshots (Line 82)")
    print("  4. Multiple snapshots in one test (Lines 95-96)")
    print("  5. Nested data structures (Line 123)")
    print("  6. Parameterized tests (Line 145)")
    print("  7. Function output snapshots (Line 170)")
    print("  8. API response snapshots (Line 197)")
    print("  9. List comprehension results (Line 208)")
    print(" 10. Exception handling snapshots (Line 226)")
    print("\n" + "=" * 70)
    print("\nRunning pytest...\n")
    print("=" * 70 + "\n")

    # Run pytest with verbose output
    # Check if we should update snapshots
    import os

    args = [__file__, "-v", "--tb=short"]
    if os.environ.get("UPDATE_SNAPSHOTS") == "1" or "--snapshot-update" in sys.argv:
        args.append("--snapshot-update")

    sys.exit(pytest.main(args))
