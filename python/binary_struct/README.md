# Binary Data Handling with Python struct Module

This example demonstrates how to handle binary data formats using Python's `struct` module, which is essential for working with binary files, network protocols, and low-level data structures.

## Overview

The `struct` module provides:
- **Packing**: Converting Python values to binary data (bytes)
- **Unpacking**: Converting binary data back to Python values
- **Format strings**: Specifying data types and byte order
- **Size calculation**: Computing binary structure sizes

## Requirements

- **Python version**: Python 3.6+ (standard library module, no external dependencies)
- **No external packages required**: `struct` is part of Python's standard library

## Running the Example

```bash
uv run python main_binary_struct.py
```

## Source Code with Annotations

### Example 1: Basic Integer Packing/Unpacking (Lines 20-35)

```python
# Pack integers into binary format (line 26-27)
value1, value2 = 42, 1000
packed = struct.pack('iI', value1, value2)  # 'i'=signed int, 'I'=unsigned int
```

**Output:**
```
Original values: 42, 1000
Packed binary (hex): 2a000000e8030000
Packed size: 8 bytes
Unpacked values: (42, 1000)
```

**Explanation:**
- Line 29: `struct.pack('iI', ...)` converts two integers to 8 bytes of binary data
- The hex output `2a000000e8030000` shows:
  - `2a000000` = 42 in little-endian 4-byte signed int
  - `e8030000` = 1000 in little-endian 4-byte unsigned int
- Line 33: `struct.unpack()` reverses the process, returning `(42, 1000)`

### Example 2: Byte Order - Endianness (Lines 38-58)

```python
# Little-endian (< prefix) vs Big-endian (> prefix)
value = 0x12345678
little = struct.pack('<I', value)  # Line 48
big = struct.pack('>I', value)     # Line 51
```

**Output:**
```
Original value: 0x12345678
Native byte order: 78563412
Little-endian:     78563412
Big-endian:        12345678
Network order:     12345678
```

**Explanation:**
- **Little-endian** (`78563412`): Least significant byte first (Intel x86 architecture)
  - Bytes stored as: 0x78, 0x56, 0x34, 0x12
- **Big-endian** (`12345678`): Most significant byte first (network protocols, some RISC)
  - Bytes stored as: 0x12, 0x34, 0x56, 0x78
- Line 54: Network order `!` is the same as big-endian, used in TCP/IP protocols

### Example 3: Mixed Data Types (Lines 61-88)

```python
# Pack different types: char, short, int, float, double (lines 64-68)
char_val = 65        # 1 byte
short_val = 1000     # 2 bytes
int_val = 100000     # 4 bytes
float_val = 3.14159  # 4 bytes
double_val = 2.71828 # 8 bytes

packed = struct.pack('Bhifd', ...)  # Line 78
```

**Output:**
```
Original values:
  char (B):   65 ('A')
  short (h):  1000
  int (i):    100000
  float (f):  3.14159
  double (d): 2.71828

Packed binary (hex): 4100e803a0860100d00f49400000000090f7aa9509bf0540
Total size: 24 bytes
```

**Explanation:**
- Line 78: Format `'Bhifd'` specifies the type sequence:
  - `B`: unsigned char (1 byte) → `41` (ASCII 'A')
  - `h`: short (2 bytes) → `00e8` (1000 in little-endian)
  - `i`: int (4 bytes) → `a0860100` (100000)
  - `f`: float (4 bytes) → `d00f4940` (3.14159)
  - `d`: double (8 bytes) → `0000000090f7aa9509bf0540` (2.71828)
- Total: 1+2+4+4+8 = 19 bytes + alignment padding = 24 bytes

### Example 4: Struct Sizes and Alignment (Lines 91-110)

```python
# Calculate size without packing (line 105)
size = struct.calcsize(fmt)
```

**Output:**
```
Format 'B       ' (unsigned char            ):  1 bytes
Format 'h       ' (short                    ):  2 bytes
Format 'i       ' (int                      ):  4 bytes
Format 'f       ' (float                    ):  4 bytes
Format 'd       ' (double                   ):  8 bytes
Format '4s      ' (4-byte string            ):  4 bytes
Format 'Bhi     ' (char+short+int           ):  8 bytes
Format '!Bhi    ' (network order: char+short+int):  7 bytes
```

**Explanation:**
- Line 105: `struct.calcsize()` returns the size in bytes without actually packing
- `'Bhi'` (8 bytes) vs `'!Bhi'` (7 bytes): Native order adds alignment padding
- Native order: 1 (B) + 1 (pad) + 2 (h) + 4 (i) = 8 bytes
- Network order: 1 (B) + 2 (h) + 4 (i) = 7 bytes (no padding)

### Example 5: Binary File Header (Lines 113-143)

```python
# Create a file header with magic number, version, size, flags (lines 116-120)
magic = b'BIN\x00'
version_major, version_minor = 1, 2
file_size = 4096
flags = 0x0F

header = struct.pack('4sBBIB', magic, version_major, version_minor,
                     file_size, flags)  # Line 130
```

**Output:**
```
Creating file header:
  Magic:   b'BIN\x00'
  Version: 1.2
  Size:    4096 bytes
  Flags:   0x0f

Packed header (hex): 42494e0001020000001000000f
Header size: 13 bytes
```

**Explanation:**
- Line 129: Format `'4sBBIB'` creates a typical binary file header:
  - `4s`: 4-byte string → `42494e00` ('BIN\x00')
  - `B`: unsigned char → `01` (major version)
  - `B`: unsigned char → `02` (minor version)
  - `I`: unsigned int → `00001000` (4096 in little-endian)
  - `B`: unsigned char → `0f` (flags)
- This pattern is common in file formats like PNG, JPEG, ELF binaries

### Example 6: Network Packet Structure (Lines 146-177)

```python
# Network packets use big-endian (! prefix) (line 162)
packet_fmt = '!BIHH'  # Type, Sequence, Length, Checksum
packet_header = struct.pack(packet_fmt, packet_type, sequence_num,
                            payload_length, checksum)  # Lines 163-164
```

**Output:**
```
Creating network packet header:
  Type:     1
  Sequence: 12345
  Length:   256 bytes
  Checksum: 0xabcd

Packed packet header (hex): 01000030390100abcd
Header size: 9 bytes
```

**Explanation:**
- Line 162: Network byte order `!` ensures consistent interpretation across systems
- Format breakdown:
  - `B`: Type → `01` (1 byte)
  - `I`: Sequence → `00003039` (12345 in big-endian)
  - `H`: Length → `0100` (256 in big-endian)
  - `H`: Checksum → `abcd` (0xABCD in big-endian)
- Used in protocols like TCP/IP, UDP, custom network protocols

### Example 7: Struct Class for Reusability (Lines 180-208)

```python
# Pre-compile format for efficiency (line 185)
point_struct = struct.Struct('!3f')  # 3 floats in network order

# Reuse for multiple pack operations (line 197)
packed = point_struct.pack(*point)
```

**Output:**
```
Struct format: !3f
Struct size:   12 bytes

Packing 3D points:
  Point 0: (1.0, 2.0, 3.0) -> 3f8000004000000040400000
  Point 1: (4.5, 5.5, 6.5) -> 4090000040b0000040d00000
  Point 2: (7.8, 8.9, 9.1) -> 40f9999a410e66664111999a
```

**Explanation:**
- Line 185: `struct.Struct()` pre-compiles the format string for better performance
- Format `!3f` = 3 floats (4 bytes each) in big-endian = 12 bytes total
- Line 197: Reusing `point_struct.pack()` is faster than calling `struct.pack()` repeatedly
- Use this when packing/unpacking many values with the same format

### Example 8: Padding and Alignment (Lines 211-234)

```python
# Compare formats with and without padding (lines 215, 219)
fmt_no_pad = '=BIB'       # 6 bytes
fmt_with_pad = '=Bx3xIBx3x'  # 14 bytes with explicit padding
```

**Output:**
```
Format '=BIB' (native, standard sizes):
  Size: 6 bytes

Format '=Bx3xIBx3x' (with padding):
  Size: 14 bytes

Packed '=BIB': 01e803000002
```

**Explanation:**
- Line 215: `=BIB` uses standard sizes without padding: 1 + 4 + 1 = 6 bytes
- Line 219: `=Bx3xIBx3x` explicitly adds padding bytes (`x`):
  - 1 byte (B) + 3 pad bytes + 4 bytes (I) + 1 byte (B) + 3 pad bytes = 14 bytes
- Padding is used to align data to memory boundaries in C structures

## Format Characters Reference

### Data Types

| Character | C Type | Python Type | Size (bytes) |
|-----------|--------|-------------|--------------|
| `x` | pad byte | no value | 1 |
| `c` | char | bytes (length 1) | 1 |
| `b` | signed char | integer | 1 |
| `B` | unsigned char | integer | 1 |
| `h` | short | integer | 2 |
| `H` | unsigned short | integer | 2 |
| `i` | int | integer | 4 |
| `I` | unsigned int | integer | 4 |
| `l` | long | integer | 4 |
| `L` | unsigned long | integer | 4 |
| `q` | long long | integer | 8 |
| `Q` | unsigned long long | integer | 8 |
| `f` | float | float | 4 |
| `d` | double | float | 8 |
| `s` | char[] | bytes | variable |

### Byte Order Prefixes

| Character | Byte Order | Size | Alignment |
|-----------|-----------|------|-----------|
| `@` | native | native | native (default) |
| `=` | native | standard | none |
| `<` | little-endian | standard | none |
| `>` | big-endian | standard | none |
| `!` | network (big-endian) | standard | none |

## Common Use Cases

1. **Binary File I/O**: Reading/writing file headers (PNG, JPEG, WAV, etc.)
2. **Network Protocols**: Packing/unpacking TCP/IP, UDP packets
3. **Interfacing with C Libraries**: Matching C struct layouts
4. **Embedded Systems**: Communicating with hardware devices
5. **Data Serialization**: Efficient storage of numerical data
6. **Memory-Mapped Files**: Direct binary data access

## Key Takeaways

1. **Use format strings** to specify data types: `'iHf'` = int, unsigned short, float
2. **Control byte order** with prefixes: `<` (little), `>` (big), `!` (network)
3. **Pre-compile formats** with `struct.Struct()` for repeated operations
4. **Calculate sizes** with `struct.calcsize()` before allocating buffers
5. **Mind the padding**: Native alignment may add extra bytes
6. **Network protocols** typically use big-endian (`!` prefix)
7. **Binary data** is displayed as hex strings for readability

## Performance Tips

- Use `struct.Struct()` class for repeated pack/unpack operations (Example 7, line 185)
- Pre-calculate sizes with `calcsize()` to avoid runtime overhead
- Choose appropriate byte order prefix to avoid unnecessary conversions
- For large datasets, consider using `array` or `numpy` modules instead

## Further Reading

- [Python struct documentation](https://docs.python.org/3/library/struct.html)
- [Understanding Endianness](https://en.wikipedia.org/wiki/Endianness)
- [Binary file formats](https://en.wikipedia.org/wiki/Binary_file)
