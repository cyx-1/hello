"""
YAML Sorting Example: Demonstrating how to sort elements in YAML files

This example shows various YAML sorting techniques:
1. Sorting dictionary keys alphabetically
2. Sorting nested structures
3. Sorting lists by different criteria
4. Preserving structure while sorting
"""

import yaml
from typing import Any


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print("=" * 60)


def sort_dict_keys(data: dict[str, Any]) -> dict[str, Any]:
    """Recursively sort dictionary keys alphabetically."""
    if isinstance(data, dict):
        return {k: sort_dict_keys(v) for k, v in sorted(data.items())}
    elif isinstance(data, list):
        return [sort_dict_keys(item) for item in data]
    else:
        return data


def main() -> None:
    """Demonstrate YAML sorting capabilities."""

    # Example 1: Sorting dictionary keys
    print_section("Example 1: Sorting Dictionary Keys")

    unsorted_config = {
        "zebra": "last animal",
        "apple": "first fruit",
        "mango": "tropical fruit",
        "banana": "yellow fruit",
    }

    print("\n📝 Original YAML (unsorted):")
    print(yaml.dump(unsorted_config, sort_keys=False, default_flow_style=False))

    print("📝 Sorted YAML (using yaml.dump with sort_keys=True):")
    sorted_yaml = yaml.dump(unsorted_config, sort_keys=True, default_flow_style=False)
    print(sorted_yaml)

    # Example 2: Sorting nested structures
    print_section("Example 2: Sorting Nested Structures")

    nested_data = {
        "database": {
            "port": 5432,
            "host": "localhost",
            "name": "mydb",
            "user": "admin",
        },
        "api": {
            "timeout": 30,
            "endpoint": "/api/v1",
            "auth": True,
        },
    }

    print("\n📝 Original nested YAML (unsorted):")
    print(yaml.dump(nested_data, sort_keys=False, default_flow_style=False))

    print("📝 Sorted nested YAML:")
    sorted_nested = yaml.dump(nested_data, sort_keys=True, default_flow_style=False)
    print(sorted_nested)

    # Example 3: Sorting lists
    print_section("Example 3: Sorting Lists")

    data_with_lists = {
        "fruits": ["mango", "apple", "banana", "cherry"],
        "numbers": [42, 7, 23, 15, 8],
        "mixed": [
            {"name": "Charlie", "age": 35},
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
        ],
    }

    print("\n📝 Original YAML with lists:")
    print(yaml.dump(data_with_lists, sort_keys=False, default_flow_style=False))

    # Sort the lists
    sorted_lists = {
        "fruits": sorted(data_with_lists["fruits"]),
        "numbers": sorted(data_with_lists["numbers"]),
        "mixed": sorted(data_with_lists["mixed"], key=lambda x: x["name"]),
    }

    print("📝 YAML with sorted lists:")
    print(yaml.dump(sorted_lists, sort_keys=True, default_flow_style=False))

    # Example 4: Custom sorting with complex nested structures
    print_section("Example 4: Custom Deep Sorting")

    complex_data = {
        "users": [
            {
                "username": "john_doe",
                "email": "john@example.com",
                "roles": ["editor", "admin", "viewer"],
                "age": 30,
            },
            {
                "username": "alice_smith",
                "email": "alice@example.com",
                "roles": ["viewer", "contributor"],
                "age": 25,
            },
        ],
        "settings": {
            "theme": "dark",
            "notifications": True,
            "language": "en",
        },
    }

    print("\n📝 Original complex YAML:")
    print(yaml.dump(complex_data, sort_keys=False, default_flow_style=False))

    # Deep sort: sort dict keys AND list contents
    def deep_sort(data: Any) -> Any:
        """Recursively sort both dictionary keys and lists."""
        if isinstance(data, dict):
            return {k: deep_sort(v) for k, v in sorted(data.items())}
        elif isinstance(data, list):
            # Try to sort if all items are comparable
            try:
                if all(isinstance(item, (str, int, float)) for item in data):
                    return sorted(data)
                elif all(isinstance(item, dict) for item in data):
                    # Sort list of dicts by first key's value
                    return [deep_sort(item) for item in data]
                else:
                    return [deep_sort(item) for item in data]
            except (TypeError, KeyError):
                return [deep_sort(item) for item in data]
        else:
            return data

    deep_sorted = deep_sort(complex_data)
    print("📝 Deep sorted YAML (keys + lists):")
    print(yaml.dump(deep_sorted, sort_keys=False, default_flow_style=False))

    # Example 5: Reading, sorting, and writing YAML files
    print_section("Example 5: File Operations with Sorting")

    # Create a sample YAML file
    sample_data = {
        "version": "1.0",
        "services": {
            "web": {
                "port": 8080,
                "image": "nginx:latest",
                "depends_on": ["database", "cache"],
            },
            "database": {
                "port": 5432,
                "image": "postgres:13",
                "volumes": ["/data/db:/var/lib/postgresql/data"],
            },
            "cache": {
                "port": 6379,
                "image": "redis:alpine",
            },
        },
    }

    # Write unsorted
    with open("/tmp/unsorted.yaml", "w") as f:
        yaml.dump(sample_data, f, sort_keys=False, default_flow_style=False)

    print("\n📝 Written to /tmp/unsorted.yaml")

    # Read and sort
    with open("/tmp/unsorted.yaml") as f:
        loaded_data = yaml.safe_load(f)

    # Write sorted
    with open("/tmp/sorted.yaml", "w") as f:
        yaml.dump(loaded_data, f, sort_keys=True, default_flow_style=False)

    print("📝 Written sorted version to /tmp/sorted.yaml")

    # Display both
    print("\n📄 Content of sorted.yaml:")
    with open("/tmp/sorted.yaml") as f:
        sorted_content = f.read()
        print(sorted_content)

    # Summary
    print_section("Summary")
    print("""
    ✅ Key Points Demonstrated:

    1. yaml.dump(data, sort_keys=True) - Sorts dictionary keys alphabetically
    2. sorted() function - Sorts lists and sequences
    3. Custom key functions - Sort by specific criteria (e.g., lambda x: x['name'])
    4. Recursive sorting - Deep sort nested structures
    5. File I/O - Read, sort, and write YAML files

    💡 Note: The PyYAML library's sort_keys parameter only sorts dictionary
       keys, not list contents. For complete sorting, combine yaml.dump()
       with custom sorting functions.
    """)


if __name__ == "__main__":
    main()
