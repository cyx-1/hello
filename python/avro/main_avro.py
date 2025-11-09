#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "fastavro",
# ]
# ///

"""
Apache Avro Demonstration in Python

This script demonstrates the key benefits of Apache Avro:
1. Compact binary serialization format
2. Schema-based data validation
3. Schema evolution support
4. Language-agnostic serialization
"""

import io
import json
from fastavro import writer, reader, parse_schema


def demonstrate_avro_benefits():
    """Demonstrate key benefits of Apache Avro format."""

    # Line 26-35: Define Avro schema for User records
    print("=" * 80)
    print("AVRO DEMONSTRATION: Benefits of Apache Avro")
    print("=" * 80)
    print()

    print("[1] SCHEMA DEFINITION")
    print("-" * 80)
    user_schema_v1 = {
        "type": "record",
        "name": "User",
        "namespace": "example.avro",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "favorite_number", "type": ["int", "null"]},
            {"name": "favorite_color", "type": ["string", "null"]}
        ]
    }

    parsed_schema_v1 = parse_schema(user_schema_v1)
    print("Schema v1 defined with fields: name, favorite_number, favorite_color")
    print()

    # Line 49-56: Create sample data
    print("[2] DATA SERIALIZATION")
    print("-" * 80)
    users = [
        {"name": "Alice", "favorite_number": 42, "favorite_color": "blue"},
        {"name": "Bob", "favorite_number": None, "favorite_color": "green"},
        {"name": "Charlie", "favorite_number": 7, "favorite_color": None},
    ]
    print(f"Sample data: {len(users)} user records")
    for i, user in enumerate(users, 1):
        print(f"  User {i}: {user}")
    print()

    # Line 61-71: Serialize to Avro format
    print("[3] AVRO BINARY SERIALIZATION")
    print("-" * 80)
    avro_bytes = io.BytesIO()
    writer(avro_bytes, parsed_schema_v1, users)

    avro_size = len(avro_bytes.getvalue())
    print(f"Avro binary size: {avro_size} bytes")

    # Line 74-79: Compare with JSON size
    json_bytes = json.dumps(users).encode('utf-8')
    json_size = len(json_bytes)
    print(f"JSON size (same data): {json_size} bytes")
    print(f"Size reduction: {((json_size - avro_size) / json_size * 100):.1f}% smaller with Avro")
    print(f"Compression ratio: {json_size / avro_size:.2f}x")
    print()

    # Line 83-93: Deserialize and verify data
    print("[4] AVRO DESERIALIZATION")
    print("-" * 80)
    avro_bytes.seek(0)

    print("Reading records from Avro file:")
    deserialized_users = []
    for i, user in enumerate(reader(avro_bytes), 1):
        deserialized_users.append(user)
        print(f"  User {i}: {user}")
    print(f"Successfully deserialized {len(deserialized_users)} records")
    print()

    # Line 97-112: Demonstrate schema evolution
    print("[5] SCHEMA EVOLUTION (Adding a new field)")
    print("-" * 80)
    user_schema_v2 = {
        "type": "record",
        "name": "User",
        "namespace": "example.avro",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "favorite_number", "type": ["int", "null"]},
            {"name": "favorite_color", "type": ["string", "null"]},
            {"name": "email", "type": ["string", "null"], "default": None}  # New field
        ]
    }

    parsed_schema_v2 = parse_schema(user_schema_v2)
    print("Schema v2 adds 'email' field with default value of None")
    print()

    # Line 116-128: Read old data with new schema
    print("[6] BACKWARD COMPATIBILITY")
    print("-" * 80)
    print("Reading v1 data (without email) using v2 schema (with email):")
    avro_bytes.seek(0)

    # Create reader with new schema
    for i, user in enumerate(reader(avro_bytes, reader_schema=user_schema_v2), 1):
        print(f"  User {i}: {user}")
        print(f"    -> 'email' field populated with default: {user.get('email')}")
    print()

    # Line 133-143: Write new data with evolved schema
    print("[7] FORWARD COMPATIBILITY")
    print("-" * 80)
    print("Writing new data with v2 schema (including email):")
    avro_bytes_v2 = io.BytesIO()

    new_users = [
        {"name": "Diana", "favorite_number": 99, "favorite_color": "red", "email": "diana@example.com"},
        {"name": "Eve", "favorite_number": 13, "favorite_color": "purple", "email": None},
    ]

    writer(avro_bytes_v2, parsed_schema_v2, new_users)

    for i, user in enumerate(new_users, 1):
        print(f"  User {i}: {user}")
    print()

    # Line 153-160: Key benefits summary
    print("[8] KEY BENEFITS SUMMARY")
    print("-" * 80)
    print("✓ COMPACT: Binary format is more space-efficient than JSON")
    print("✓ FAST: Binary serialization/deserialization is faster than text parsing")
    print("✓ SCHEMA VALIDATION: Data is validated against schema during write")
    print("✓ SCHEMA EVOLUTION: Supports adding/removing fields with defaults")
    print("✓ SELF-DESCRIBING: Schema is stored with the data")
    print("✓ LANGUAGE-AGNOSTIC: Works across different programming languages")
    print("✓ SPLITTABLE: Avro files can be split for parallel processing")
    print()

    print("=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_avro_benefits()
