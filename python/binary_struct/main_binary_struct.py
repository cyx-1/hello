#!/usr/bin/env python3
"""
Demonstrate handling of binary data format using struct module.

The struct module provides format strings for packing/unpacking binary data.
This is essential for reading/writing binary files, network protocols, and more.
"""

import struct
import sys


def print_section(title: str) -> None:
    """Print a section header."""
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print("=" * 60)


def example_basic_packing() -> None:
    """Example 1: Basic packing and unpacking of integers."""
    print_section("Example 1: Basic Integer Packing/Unpacking")

    # Pack integers into binary format
    value1, value2 = 42, 1000
    print(f"Original values: {value1}, {value2}")

    # 'i' = signed int (4 bytes), 'I' = unsigned int (4 bytes)
    packed = struct.pack("iI", value1, value2)
    print(f"Packed binary (hex): {packed.hex()}")
    print(f"Packed size: {len(packed)} bytes")

    # Unpack the binary data
    unpacked = struct.unpack("iI", packed)
    print(f"Unpacked values: {unpacked}")


def example_byte_order() -> None:
    """Example 2: Byte order (endianness) demonstration."""
    print_section("Example 2: Byte Order (Endianness)")

    value = 0x12345678
    print(f"Original value: 0x{value:08x}")

    # Native byte order (depends on system)
    native = struct.pack("I", value)
    print(f"Native byte order: {native.hex()}")

    # Little-endian (< prefix)
    little = struct.pack("<I", value)
    print(f"Little-endian:     {little.hex()}")

    # Big-endian (> prefix)
    big = struct.pack(">I", value)
    print(f"Big-endian:        {big.hex()}")

    # Network byte order (! prefix, same as big-endian)
    network = struct.pack("!I", value)
    print(f"Network order:     {network.hex()}")


def example_mixed_types() -> None:
    """Example 3: Packing mixed data types."""
    print_section("Example 3: Mixed Data Types")

    # Pack: unsigned char, short, int, float, double
    char_val = 65  # ASCII 'A'
    short_val = 1000
    int_val = 100000
    float_val = 3.14159
    double_val = 2.71828

    print("Original values:")
    print(f"  char (B):   {char_val} ('{chr(char_val)}')")
    print(f"  short (h):  {short_val}")
    print(f"  int (i):    {int_val}")
    print(f"  float (f):  {float_val}")
    print(f"  double (d): {double_val}")

    # Format: B=unsigned char, h=short, i=int, f=float, d=double
    packed = struct.pack("Bhifd", char_val, short_val, int_val, float_val, double_val)
    print(f"\nPacked binary (hex): {packed.hex()}")
    print(f"Total size: {len(packed)} bytes")

    # Unpack
    unpacked = struct.unpack("Bhifd", packed)
    print(f"\nUnpacked values: {unpacked}")


def example_struct_size() -> None:
    """Example 4: Calculate struct sizes and alignment."""
    print_section("Example 4: Struct Sizes and Alignment")

    formats = [
        ("B", "unsigned char"),
        ("h", "short"),
        ("i", "int"),
        ("f", "float"),
        ("d", "double"),
        ("4s", "4-byte string"),
        ("Bhi", "char+short+int"),
        ("!Bhi", "network order: char+short+int"),
    ]

    for fmt, description in formats:
        size = struct.calcsize(fmt)
        print(f"Format '{fmt:8s}' ({description:25s}): {size:2d} bytes")


def example_file_header() -> None:
    """Example 5: Simulating a binary file header."""
    print_section("Example 5: Binary File Header")

    # Create a mock file header with magic number, version, size, and flags
    magic = b"BIN\x00"  # 4-byte magic number
    version_major = 1
    version_minor = 2
    file_size = 4096
    flags = 0x0F

    print("Creating file header:")
    print(f"  Magic:   {magic}")
    print(f"  Version: {version_major}.{version_minor}")
    print(f"  Size:    {file_size} bytes")
    print(f"  Flags:   0x{flags:02x}")

    # Pack header: 4s=4-byte string, BB=2 unsigned chars, I=unsigned int, B=unsigned char
    header_fmt = "4sBBIB"
    header = struct.pack(
        header_fmt, magic, version_major, version_minor, file_size, flags
    )

    print(f"\nPacked header (hex): {header.hex()}")
    print(f"Header size: {len(header)} bytes")

    # Unpack and verify
    unpacked = struct.unpack(header_fmt, header)
    print("\nUnpacked header:")
    print(f"  Magic:   {unpacked[0]}")
    print(f"  Version: {unpacked[1]}.{unpacked[2]}")
    print(f"  Size:    {unpacked[3]} bytes")
    print(f"  Flags:   0x{unpacked[4]:02x}")


def example_network_packet() -> None:
    """Example 6: Network packet structure."""
    print_section("Example 6: Network Packet (Big-Endian)")

    # Simulate a simple network packet with header
    packet_type = 1  # Data packet
    sequence_num = 12345
    payload_length = 256
    checksum = 0xABCD

    print("Creating network packet header:")
    print(f"  Type:     {packet_type}")
    print(f"  Sequence: {sequence_num}")
    print(f"  Length:   {payload_length} bytes")
    print(f"  Checksum: 0x{checksum:04x}")

    # Use network byte order (big-endian) with ! prefix
    # Format: B=unsigned char, I=unsigned int, H=unsigned short, H=unsigned short
    packet_fmt = "!BIHH"
    packet_header = struct.pack(
        packet_fmt, packet_type, sequence_num, payload_length, checksum
    )

    print(f"\nPacked packet header (hex): {packet_header.hex()}")
    print(f"Header size: {len(packet_header)} bytes")

    # Unpack
    unpacked = struct.unpack(packet_fmt, packet_header)
    print("\nUnpacked packet header:")
    print(f"  Type:     {unpacked[0]}")
    print(f"  Sequence: {unpacked[1]}")
    print(f"  Length:   {unpacked[2]} bytes")
    print(f"  Checksum: 0x{unpacked[3]:04x}")


def example_struct_class() -> None:
    """Example 7: Using Struct class for efficiency."""
    print_section("Example 7: Struct Class for Reusability")

    # Pre-compile the format string for better performance
    # This is useful when packing/unpacking multiple times
    point_struct = struct.Struct("!3f")  # 3 floats in network order

    print(f"Struct format: {point_struct.format}")
    print(f"Struct size:   {point_struct.size} bytes")

    # Pack multiple 3D points
    points = [
        (1.0, 2.0, 3.0),
        (4.5, 5.5, 6.5),
        (7.8, 8.9, 9.1),
    ]

    print("\nPacking 3D points:")
    packed_points = []
    for i, point in enumerate(points):
        packed = point_struct.pack(*point)
        packed_points.append(packed)
        print(f"  Point {i}: {point} -> {packed.hex()}")

    # Unpack
    print("\nUnpacking 3D points:")
    for i, packed in enumerate(packed_points):
        point = point_struct.unpack(packed)
        print(f"  Point {i}: {point}")


def example_padding() -> None:
    """Example 8: Struct padding and alignment."""
    print_section("Example 8: Padding and Alignment")

    # Without padding (using '=' for native alignment but standard sizes)
    fmt_no_pad = "=BIB"
    size_no_pad = struct.calcsize(fmt_no_pad)
    print("Format '=BIB' (native, standard sizes):")
    print(f"  Size: {size_no_pad} bytes")

    # With explicit padding using 'x' (pad byte)
    fmt_with_pad = "=Bx3xIBx3x"
    size_with_pad = struct.calcsize(fmt_with_pad)
    print("\nFormat '=Bx3xIBx3x' (with padding):")
    print(f"  Size: {size_with_pad} bytes")

    # Pack data
    data = struct.pack("=BIB", 1, 1000, 2)
    print(f"\nPacked '=BIB': {data.hex()}")
    print(f"Length: {len(data)} bytes")


def main() -> int:
    """Run all struct examples."""
    print("Python struct Module - Binary Data Handling Examples")
    print(f"Python version: {sys.version}")

    example_basic_packing()
    example_byte_order()
    example_mixed_types()
    example_struct_size()
    example_file_header()
    example_network_packet()
    example_struct_class()
    example_padding()

    print_section("Format Characters Reference")
    print("""
Common struct format characters:
  x   : pad byte (no value)
  c   : char (bytes of length 1)
  b/B : signed/unsigned char (1 byte)
  h/H : signed/unsigned short (2 bytes)
  i/I : signed/unsigned int (4 bytes)
  l/L : signed/unsigned long (4 bytes)
  q/Q : signed/unsigned long long (8 bytes)
  f   : float (4 bytes)
  d   : double (8 bytes)
  s   : char[] (string, e.g., '10s' for 10 bytes)

Byte order prefixes:
  @   : native order, native size, native alignment (default)
  =   : native order, standard size, no alignment
  <   : little-endian, standard size, no alignment
  >   : big-endian, standard size, no alignment
  !   : network (big-endian), standard size, no alignment
    """)

    return 0


if __name__ == "__main__":
    sys.exit(main())
