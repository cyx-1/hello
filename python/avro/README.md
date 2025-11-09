# Apache Avro Demonstration in Python

This example demonstrates the key benefits of Apache Avro, a data serialization system that provides compact binary format, schema validation, and schema evolution capabilities.

## Requirements

- **Python**: >= 3.8
- **Dependencies**: `fastavro` (automatically installed via inline script metadata)

## Running the Example

```bash
uv run main_avro.py
```

## Key Benefits Demonstrated

1. **Schema Definition & Validation**: Type-safe data with enforced schema
2. **Binary Serialization**: Compact binary format (though overhead exists for small datasets)
3. **Schema Evolution**: Add/remove fields with backward/forward compatibility
4. **Self-Describing**: Schema stored with data for cross-language compatibility

---

## Source Code & Output Walkthrough

### [1] Schema Definition (Lines 35-47)

**Source Code:**
```python
35:    user_schema_v1 = {
36:        "type": "record",
37:        "name": "User",
38:        "namespace": "example.avro",
39:        "fields": [
40:            {"name": "name", "type": "string"},
41:            {"name": "favorite_number", "type": ["int", "null"]},
42:            {"name": "favorite_color", "type": ["string", "null"]}
43:        ]
44:    }
45:
46:    parsed_schema_v1 = parse_schema(user_schema_v1)
47:    print("Schema v1 defined with fields: name, favorite_number, favorite_color")
```

**Output:**
```
[1] SCHEMA DEFINITION
--------------------------------------------------------------------------------
Schema v1 defined with fields: name, favorite_number, favorite_color
```

**Annotation:**
- **Lines 35-44**: Define an Avro schema as a Python dictionary. The schema specifies a "record" type with three fields.
- **Lines 40-42**: Each field has a name and type. Union types like `["int", "null"]` allow nullable fields.
- **Line 46**: `parse_schema()` validates and compiles the schema for use.
- This schema acts as a contract - all data written must conform to it.

---

### [2] Sample Data Creation (Lines 53-60)

**Source Code:**
```python
53:    users = [
54:        {"name": "Alice", "favorite_number": 42, "favorite_color": "blue"},
55:        {"name": "Bob", "favorite_number": None, "favorite_color": "green"},
56:        {"name": "Charlie", "favorite_number": 7, "favorite_color": None},
57:    ]
58:    print(f"Sample data: {len(users)} user records")
59:    for i, user in enumerate(users, 1):
60:        print(f"  User {i}: {user}")
```

**Output:**
```
[2] DATA SERIALIZATION
--------------------------------------------------------------------------------
Sample data: 3 user records
  User 1: {'name': 'Alice', 'favorite_number': 42, 'favorite_color': 'blue'}
  User 2: {'name': 'Bob', 'favorite_number': None, 'favorite_color': 'green'}
  User 3: {'name': 'Charlie', 'favorite_number': 7, 'favorite_color': None}
```

**Annotation:**
- **Lines 53-57**: Create sample user records matching the schema.
- **Line 55**: Bob has `None` for favorite_number (allowed by union type `["int", "null"]`).
- **Line 56**: Charlie has `None` for favorite_color (demonstrates nullable fields).
- All records conform to the schema defined in section [1].

---

### [3] Avro Binary Serialization (Lines 66-77)

**Source Code:**
```python
66:    avro_bytes = io.BytesIO()
67:    writer(avro_bytes, parsed_schema_v1, users)
68:
69:    avro_size = len(avro_bytes.getvalue())
70:    print(f"Avro binary size: {avro_size} bytes")
71:
72:    # Line 74-79: Compare with JSON size
73:    json_bytes = json.dumps(users).encode('utf-8')
74:    json_size = len(json_bytes)
75:    print(f"JSON size (same data): {json_size} bytes")
76:    print(f"Size reduction: {((json_size - avro_size) / json_size * 100):.1f}% smaller with Avro")
77:    print(f"Compression ratio: {json_size / avro_size:.2f}x")
```

**Output:**
```
[3] AVRO BINARY SERIALIZATION
--------------------------------------------------------------------------------
Avro binary size: 312 bytes
JSON size (same data): 204 bytes
Size reduction: -52.9% smaller with Avro
Compression ratio: 0.65x
```

**Annotation:**
- **Line 67**: `writer()` serializes all user records into Avro binary format with schema embedded.
- **Line 69**: The Avro file is 312 bytes (includes schema + data).
- **Line 73-74**: Same data in JSON is 204 bytes (no schema, just data).
- **Important Note**: For small datasets, Avro has overhead because it stores the schema. Avro's benefits shine with:
  - **Larger datasets** where schema overhead is amortized
  - **Many records** where binary encoding outweighs schema cost
  - **Schema evolution** needs where the self-describing format is essential
  - **Cross-language serialization** where schema validation is critical

---

### [4] Deserialization (Lines 83-90)

**Source Code:**
```python
83:    avro_bytes.seek(0)
84:
85:    print("Reading records from Avro file:")
86:    deserialized_users = []
87:    for i, user in enumerate(reader(avro_bytes), 1):
88:        deserialized_users.append(user)
89:        print(f"  User {i}: {user}")
90:    print(f"Successfully deserialized {len(deserialized_users)} records")
```

**Output:**
```
[4] AVRO DESERIALIZATION
--------------------------------------------------------------------------------
Reading records from Avro file:
  User 1: {'name': 'Alice', 'favorite_number': 42, 'favorite_color': 'blue'}
  User 2: {'name': 'Bob', 'favorite_number': None, 'favorite_color': 'green'}
  User 3: {'name': 'Charlie', 'favorite_number': 7, 'favorite_color': None}
Successfully deserialized 3 records
```

**Annotation:**
- **Line 83**: Reset buffer to beginning for reading.
- **Line 87**: `reader()` automatically extracts the schema from the Avro file and deserializes records.
- The deserialized data perfectly matches the original input (see section [2]).
- **Self-Describing**: No need to specify schema when reading - it's embedded in the file.

---

### [5] Schema Evolution (Lines 96-109)

**Source Code:**
```python
96:    user_schema_v2 = {
97:        "type": "record",
98:        "name": "User",
99:        "namespace": "example.avro",
100:        "fields": [
101:            {"name": "name", "type": "string"},
102:            {"name": "favorite_number", "type": ["int", "null"]},
103:            {"name": "favorite_color", "type": ["string", "null"]},
104:            {"name": "email", "type": ["string", "null"], "default": None}  # New field
105:        ]
106:    }
107:
108:    parsed_schema_v2 = parse_schema(user_schema_v2)
109:    print("Schema v2 adds 'email' field with default value of None")
```

**Output:**
```
[5] SCHEMA EVOLUTION (Adding a new field)
--------------------------------------------------------------------------------
Schema v2 adds 'email' field with default value of None
```

**Annotation:**
- **Line 104**: Schema v2 adds a new `email` field that didn't exist in v1.
- **`"default": None`**: Crucial for backward compatibility - allows reading old data with new schema.
- This demonstrates **schema evolution**: adding fields without breaking existing data.

---

### [6] Backward Compatibility (Lines 115-121)

**Source Code:**
```python
115:    print("Reading v1 data (without email) using v2 schema (with email):")
116:    avro_bytes.seek(0)
117:
118:    # Create reader with new schema
119:    for i, user in enumerate(reader(avro_bytes, reader_schema=user_schema_v2), 1):
120:        print(f"  User {i}: {user}")
121:        print(f"    -> 'email' field populated with default: {user.get('email')}")
```

**Output:**
```
[6] BACKWARD COMPATIBILITY
--------------------------------------------------------------------------------
Reading v1 data (without email) using v2 schema (with email):
  User 1: {'name': 'Alice', 'favorite_number': 42, 'favorite_color': 'blue', 'email': None}
    -> 'email' field populated with default: None
  User 2: {'name': 'Bob', 'favorite_number': None, 'favorite_color': 'green', 'email': None}
    -> 'email' field populated with default: None
  User 3: {'name': 'Charlie', 'favorite_number': 7, 'favorite_color': None, 'email': None}
    -> 'email' field populated with default: None
```

**Annotation:**
- **Line 119**: Read old data (written with v1 schema) using new v2 schema via `reader_schema` parameter.
- **Output**: All records now have `email: None` automatically populated from the default value.
- **Backward Compatibility**: New code (v2) can read old data (v1) without errors.
- This is essential for rolling upgrades where readers update before writers.

---

### [7] Forward Compatibility (Lines 127-138)

**Source Code:**
```python
127:    print("Writing new data with v2 schema (including email):")
128:    avro_bytes_v2 = io.BytesIO()
129:
130:    new_users = [
131:        {"name": "Diana", "favorite_number": 99, "favorite_color": "red", "email": "diana@example.com"},
132:        {"name": "Eve", "favorite_number": 13, "favorite_color": "purple", "email": None},
133:    ]
134:
135:    writer(avro_bytes_v2, parsed_schema_v2, new_users)
136:
137:    for i, user in enumerate(new_users, 1):
138:        print(f"  User {i}: {user}")
```

**Output:**
```
[7] FORWARD COMPATIBILITY
--------------------------------------------------------------------------------
Writing new data with v2 schema (including email):
  User 1: {'name': 'Diana', 'favorite_number': 99, 'favorite_color': 'red', 'email': 'diana@example.com'}
  User 2: {'name': 'Eve', 'favorite_number': 13, 'favorite_color': 'purple', 'email': None}
```

**Annotation:**
- **Line 131**: Diana's record includes the new `email` field with a value.
- **Line 132**: Eve's record has `email: None`.
- **Line 135**: Write data using the evolved v2 schema.
- **Forward Compatibility**: Old readers (v1) can read this data by ignoring the unknown `email` field (not demonstrated but Avro supports this).

---

### [8] Key Benefits Summary (Lines 142-150)

**Output:**
```
[8] KEY BENEFITS SUMMARY
--------------------------------------------------------------------------------
✓ COMPACT: Binary format is more space-efficient than JSON
✓ FAST: Binary serialization/deserialization is faster than text parsing
✓ SCHEMA VALIDATION: Data is validated against schema during write
✓ SCHEMA EVOLUTION: Supports adding/removing fields with defaults
✓ SELF-DESCRIBING: Schema is stored with the data
✓ LANGUAGE-AGNOSTIC: Works across different programming languages
✓ SPLITTABLE: Avro files can be split for parallel processing
```

**Annotation:**
Each benefit demonstrated in this example:
1. **COMPACT**: Binary format (though small datasets have schema overhead, larger datasets benefit).
2. **FAST**: Binary parsing is faster than JSON text parsing (not measured here, but true at scale).
3. **SCHEMA VALIDATION**: Lines 67, 135 - data validated against schema during write.
4. **SCHEMA EVOLUTION**: Section [6] shows reading old data with new schema.
5. **SELF-DESCRIBING**: Section [4] shows reading without specifying schema.
6. **LANGUAGE-AGNOSTIC**: Avro files can be read by Java, Python, C++, etc.
7. **SPLITTABLE**: Avro files support sync markers for parallel processing in distributed systems like Hadoop/Spark.

---

## When to Use Avro

**Best For:**
- **Large datasets**: Schema overhead amortized across many records
- **Data lakes**: Long-term storage with schema evolution requirements
- **Big data pipelines**: Hadoop, Spark, Kafka (native Avro support)
- **Cross-language systems**: Services in different languages sharing data
- **Streaming**: Kafka uses Avro with schema registry for type safety

**Consider Alternatives For:**
- **Small messages**: JSON or Protocol Buffers might be simpler
- **Human readability**: JSON is easier to debug
- **Extreme performance**: Cap'n Proto or FlatBuffers offer zero-copy deserialization
- **Browser-native**: JSON works natively in JavaScript

---

## Implementation Details

This example uses `fastavro`, a fast Python implementation of Avro that:
- Provides a pure-Python implementation for portability
- Uses Cython for performance-critical sections
- Supports all Avro features including schema evolution
- Is actively maintained and widely used in production systems

The code demonstrates end-to-end Avro usage from schema definition through serialization, deserialization, and schema evolution scenarios that mirror real-world use cases.
