# YAML Sorting Example: Managing and Organizing YAML Data

This example demonstrates how to sort elements in YAML files using Python's `PyYAML` library. Sorting YAML data helps maintain consistency, improves readability, and makes version control diffs cleaner.

## Key Concepts Illustrated

1. **Dictionary Key Sorting** - Sort keys alphabetically for consistent formatting
2. **Nested Structure Sorting** - Sort keys in deeply nested dictionaries
3. **List Sorting** - Sort list elements with various criteria
4. **Deep Sorting** - Recursively sort both dictionary keys and list contents
5. **File I/O with Sorting** - Read, sort, and write YAML files

## Requirements

- **Python Version**: 3.10 or higher
- **Library**: PyYAML 6.0.1 or higher

## Running the Example

```bash
uv run python main_yaml_sort.py
```

## Source Code and Output Analysis

### 1. Sorting Dictionary Keys

**Source Code (main_yaml_sort.py:38-50):**
```python
unsorted_config = {
    "zebra": "last animal",
    "apple": "first fruit",
    "mango": "tropical fruit",
    "banana": "yellow fruit",
}

print("\n📝 Original YAML (unsorted):")
print(yaml.dump(unsorted_config, sort_keys=False, default_flow_style=False))

print("📝 Sorted YAML (using yaml.dump with sort_keys=True):")
sorted_yaml = yaml.dump(unsorted_config, sort_keys=True, default_flow_style=False)  # Line 49
print(sorted_yaml)
```

**Output:**
```
📝 Original YAML (unsorted):
zebra: last animal          ← Keys in insertion order
apple: first fruit
mango: tropical fruit
banana: yellow fruit

📝 Sorted YAML (using yaml.dump with sort_keys=True):
apple: first fruit          ← Line 49: Keys sorted alphabetically
banana: yellow fruit        ← 'a' comes first
mango: tropical fruit       ← 'b', 'm', then 'z'
zebra: last animal
```

**💡 Key Insight:**
- **Line 49**: The `sort_keys=True` parameter in `yaml.dump()` automatically sorts dictionary keys alphabetically
- This creates consistent output regardless of insertion order
- Useful for version control to reduce meaningless diffs

---

### 2. Sorting Nested Structures

**Source Code (main_yaml_sort.py:55-74):**
```python
nested_data = {
    "database": {
        "port": 5432,              # Line 57: Nested keys unsorted
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
sorted_nested = yaml.dump(nested_data, sort_keys=True, default_flow_style=False)  # Line 73
print(sorted_nested)
```

**Output:**
```
📝 Original nested YAML (unsorted):
database:                   ← Parent keys in insertion order
  port: 5432               ← Line 57: Child keys unsorted
  host: localhost
  name: mydb
  user: admin
api:
  timeout: 30
  endpoint: /api/v1
  auth: true

📝 Sorted nested YAML:
api:                        ← Line 73: Parent keys sorted ('api' before 'database')
  auth: true               ← Child keys also sorted
  endpoint: /api/v1
  timeout: 30
database:
  host: localhost          ← All nested keys sorted alphabetically
  name: mydb
  port: 5432
  user: admin
```

**💡 Key Insight:**
- **Line 73**: `sort_keys=True` works recursively on all nested dictionaries
- Both top-level keys ('api', 'database') and nested keys are sorted
- Creates consistent structure at every level

---

### 3. Sorting Lists

**Source Code (main_yaml_sort.py:79-100):**
```python
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
    "fruits": sorted(data_with_lists["fruits"]),                          # Line 94: Simple list sort
    "numbers": sorted(data_with_lists["numbers"]),                        # Line 95: Numeric sort
    "mixed": sorted(data_with_lists["mixed"], key=lambda x: x["name"]),  # Line 96: Custom key sort
}

print("📝 YAML with sorted lists:")
print(yaml.dump(sorted_lists, sort_keys=True, default_flow_style=False))
```

**Output:**
```
📝 Original YAML with lists:
fruits:
- mango                     ← Unsorted list items
- apple
- banana
- cherry
numbers:
- 42                        ← Unsorted numbers
- 7
- 23
- 15
- 8
mixed:
- name: Charlie             ← Unsorted by name
  age: 35
- name: Alice
  age: 30
- name: Bob
  age: 25

📝 YAML with sorted lists:
fruits:
- apple                     ← Line 94: Alphabetically sorted
- banana
- cherry
- mango
mixed:
- age: 30                   ← Line 96: Sorted by 'name' field
  name: Alice               ← Alice, Bob, Charlie
- age: 25
  name: Bob
- age: 35
  name: Charlie
numbers:
- 7                         ← Line 95: Numerically sorted
- 8
- 15
- 23
- 42
```

**💡 Key Insight:**
- **Important**: `yaml.dump(sort_keys=True)` does NOT sort list contents, only dictionary keys
- **Line 94-95**: Use Python's `sorted()` function to sort simple lists
- **Line 96**: Use `key=lambda` for custom sorting of complex objects
- Must sort lists manually before dumping to YAML

---

### 4. Custom Deep Sorting

**Source Code (main_yaml_sort.py:131-152):**
```python
# Deep sort: sort dict keys AND list contents
def deep_sort(data: Any) -> Any:                                     # Line 131
    """Recursively sort both dictionary keys and lists."""
    if isinstance(data, dict):
        return {k: deep_sort(v) for k, v in sorted(data.items())}   # Line 134: Sort dict keys
    elif isinstance(data, list):
        # Try to sort if all items are comparable
        try:
            if all(isinstance(item, (str, int, float)) for item in data):
                return sorted(data)                                  # Line 139: Sort simple lists
            elif all(isinstance(item, dict) for item in data):
                return [deep_sort(item) for item in data]           # Line 141: Recurse into dicts
            else:
                return [deep_sort(item) for item in data]
        except (TypeError, KeyError):
            return [deep_sort(item) for item in data]
    else:
        return data

deep_sorted = deep_sort(complex_data)                               # Line 150
print("📝 Deep sorted YAML (keys + lists):")
print(yaml.dump(deep_sorted, sort_keys=False, default_flow_style=False))
```

**Output:**
```
📝 Original complex YAML:
users:
- username: john_doe
  email: john@example.com
  roles:
  - editor                  ← Roles list unsorted
  - admin
  - viewer
  age: 30
- username: alice_smith
  email: alice@example.com
  roles:
  - viewer
  - contributor
  age: 25
settings:
  theme: dark
  notifications: true
  language: en

📝 Deep sorted YAML (keys + lists):
settings:                   ← Line 150: Top-level keys sorted
  language: en             ← Nested keys sorted
  notifications: true
  theme: dark
users:
- age: 30                  ← Line 134: Dict keys sorted in each item
  email: john@example.com
  roles:
  - admin                  ← Line 139: List items sorted!
  - editor
  - viewer
  username: john_doe
- age: 25
  email: alice@example.com
  roles:
  - contributor            ← Lists sorted alphabetically
  - viewer
  username: alice_smith
```

**💡 Key Insight:**
- **Line 131**: Custom recursive function for complete sorting
- **Line 134**: Sorts dictionary keys using `sorted(data.items())`
- **Line 139**: Sorts simple lists (strings, numbers)
- **Line 141**: Recursively processes nested structures
- This achieves complete sorting at all levels, unlike `yaml.dump(sort_keys=True)` alone

---

### 5. File Operations with Sorting

**Source Code (main_yaml_sort.py:178-198):**
```python
# Write unsorted
with open("/tmp/unsorted.yaml", "w") as f:                            # Line 179
    yaml.dump(sample_data, f, sort_keys=False, default_flow_style=False)

print("\n📝 Written to /tmp/unsorted.yaml")

# Read and sort
with open("/tmp/unsorted.yaml") as f:                                 # Line 185
    loaded_data = yaml.safe_load(f)

# Write sorted
with open("/tmp/sorted.yaml", "w") as f:                              # Line 189
    yaml.dump(loaded_data, f, sort_keys=True, default_flow_style=False)

print("📝 Written sorted version to /tmp/sorted.yaml")

# Display both
print("\n📄 Content of sorted.yaml:")
with open("/tmp/sorted.yaml") as f:                                   # Line 196
    sorted_content = f.read()
    print(sorted_content)
```

**Output:**
```
📝 Written to /tmp/unsorted.yaml                  ← Line 179: File written

📝 Written sorted version to /tmp/sorted.yaml     ← Line 189: Sorted file written

📄 Content of sorted.yaml:                        ← Line 196: Display result
services:
  cache:                                          ← Services sorted: cache, database, web
    image: redis:alpine
    port: 6379
  database:
    image: postgres:13
    port: 5432
    volumes:
    - /data/db:/var/lib/postgresql/data
  web:
    depends_on:
    - database
    - cache
    image: nginx:latest
    port: 8080
version: '1.0'                                    ← Top-level keys sorted
```

**💡 Key Insight:**
- **Line 179**: Write YAML file with `yaml.dump()` to file object
- **Line 185**: Read with `yaml.safe_load()` (preferred for untrusted input)
- **Line 189**: Write sorted version with `sort_keys=True`
- Common workflow: Read → Process → Sort → Write back

---

## Summary of Sorting Techniques

| Technique | Code | What It Sorts |
|-----------|------|---------------|
| **Basic Key Sort** | `yaml.dump(data, sort_keys=True)` | Dictionary keys only (recursive) |
| **List Sort** | `sorted(list)` | List elements |
| **Custom List Sort** | `sorted(list, key=lambda x: x['field'])` | List by custom criteria |
| **Deep Sort** | Custom recursive function | Everything: dict keys + lists |

## Key Takeaways

1. **`yaml.dump(sort_keys=True)`** - Sorts dictionary keys at all levels, but NOT list contents
2. **`sorted()`** - Required to sort list elements; use `key=` parameter for custom sorting
3. **Deep sorting** - Requires custom recursive function to sort both dicts and lists
4. **File operations** - Use `yaml.safe_load()` to read and `yaml.dump()` to write
5. **Consistency** - Sorted YAML improves version control diffs and readability

## When to Sort YAML

✅ **Good for:**
- Configuration files in version control
- API responses that need consistency
- Documentation and examples
- Reducing merge conflicts

❌ **Avoid when:**
- Order has semantic meaning (e.g., execution order)
- Performance is critical (sorting adds overhead)
- Working with pre-formatted YAML that must preserve structure

## Version Requirements

This example requires:
- **Python 3.10+** for modern type hints (`dict[str, Any]`)
- **PyYAML 6.0.1+** for the latest YAML 1.1 support

For Python 3.9 and below, replace `dict[str, Any]` with `Dict[str, Any]` from the `typing` module.
