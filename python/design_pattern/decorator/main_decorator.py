# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Decorator Pattern

The Decorator pattern attaches additional responsibilities to an object dynamically.
It provides a flexible alternative to subclassing for extending functionality.

Key Components:
- Component: Interface for objects that can have responsibilities added
- ConcreteComponent: Object to which responsibilities can be added
- Decorator: Maintains reference to Component and conforms to its interface
- ConcreteDecorator: Adds responsibilities to the component
"""

from abc import ABC, abstractmethod
from datetime import datetime
import time


# Component interface
class DataSource(ABC):
    """Interface for reading and writing data."""

    @abstractmethod
    def write_data(self, data: str) -> None:
        pass

    @abstractmethod
    def read_data(self) -> str:
        pass


# Concrete Component
class FileDataSource(DataSource):
    """Simple data source that stores data in memory (simulating file)."""

    def __init__(self, filename: str):
        self.filename = filename
        self._data = ""

    def write_data(self, data: str) -> None:
        self._data = data
        print(f"  [FileDataSource] Written {len(data)} chars to {self.filename}")

    def read_data(self) -> str:
        print(f"  [FileDataSource] Read {len(self._data)} chars from {self.filename}")
        return self._data


# Base Decorator
class DataSourceDecorator(DataSource):
    """Base decorator that wraps a DataSource."""

    def __init__(self, source: DataSource):
        self._wrapped = source

    def write_data(self, data: str) -> None:
        self._wrapped.write_data(data)

    def read_data(self) -> str:
        return self._wrapped.read_data()


# Concrete Decorators
class EncryptionDecorator(DataSourceDecorator):
    """Decorator that adds encryption functionality."""

    def __init__(self, source: DataSource, shift: int = 3):
        super().__init__(source)
        self._shift = shift

    def write_data(self, data: str) -> None:
        encrypted = self._encrypt(data)
        print(f"  [EncryptionDecorator] Encrypted data (Caesar cipher, shift={self._shift})")
        self._wrapped.write_data(encrypted)

    def read_data(self) -> str:
        data = self._wrapped.read_data()
        decrypted = self._decrypt(data)
        print("  [EncryptionDecorator] Decrypted data")
        return decrypted

    def _encrypt(self, data: str) -> str:
        """Simple Caesar cipher encryption."""
        result = []
        for char in data:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                result.append(chr((ord(char) - base + self._shift) % 26 + base))
            else:
                result.append(char)
        return "".join(result)

    def _decrypt(self, data: str) -> str:
        """Decrypt Caesar cipher."""
        result = []
        for char in data:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                result.append(chr((ord(char) - base - self._shift) % 26 + base))
            else:
                result.append(char)
        return "".join(result)


class CompressionDecorator(DataSourceDecorator):
    """Decorator that adds compression functionality."""

    def write_data(self, data: str) -> None:
        compressed = self._compress(data)
        print(f"  [CompressionDecorator] Compressed: {len(data)} -> {len(compressed)} chars")
        self._wrapped.write_data(compressed)

    def read_data(self) -> str:
        data = self._wrapped.read_data()
        decompressed = self._decompress(data)
        print(f"  [CompressionDecorator] Decompressed: {len(data)} -> {len(decompressed)} chars")
        return decompressed

    def _compress(self, data: str) -> str:
        """Simple run-length encoding compression."""
        if not data:
            return ""
        result = []
        count = 1
        prev = data[0]
        for char in data[1:]:
            if char == prev and count < 9:
                count += 1
            else:
                if count > 1:
                    result.append(f"{count}{prev}")
                else:
                    result.append(prev)
                prev = char
                count = 1
        if count > 1:
            result.append(f"{count}{prev}")
        else:
            result.append(prev)
        return "".join(result)

    def _decompress(self, data: str) -> str:
        """Decompress run-length encoded data."""
        result = []
        i = 0
        while i < len(data):
            if data[i].isdigit():
                count = int(data[i])
                if i + 1 < len(data):
                    result.append(data[i + 1] * count)
                    i += 2
                else:
                    result.append(data[i])
                    i += 1
            else:
                result.append(data[i])
                i += 1
        return "".join(result)


class LoggingDecorator(DataSourceDecorator):
    """Decorator that adds logging functionality."""

    def __init__(self, source: DataSource, log_prefix: str = "LOG"):
        super().__init__(source)
        self._prefix = log_prefix
        self._logs: list[str] = []

    def write_data(self, data: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{self._prefix}][{timestamp}] WRITE: {len(data)} chars"
        self._logs.append(log_entry)
        print(f"  [LoggingDecorator] {log_entry}")
        self._wrapped.write_data(data)

    def read_data(self) -> str:
        data = self._wrapped.read_data()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{self._prefix}][{timestamp}] READ: {len(data)} chars"
        self._logs.append(log_entry)
        print(f"  [LoggingDecorator] {log_entry}")
        return data

    def get_logs(self) -> list[str]:
        return self._logs.copy()


class CachingDecorator(DataSourceDecorator):
    """Decorator that adds caching functionality."""

    def __init__(self, source: DataSource, cache_ttl: float = 5.0):
        super().__init__(source)
        self._cache: str | None = None
        self._cache_time: float = 0
        self._ttl = cache_ttl
        self._cache_hits = 0
        self._cache_misses = 0

    def write_data(self, data: str) -> None:
        self._cache = None  # Invalidate cache on write
        print("  [CachingDecorator] Cache invalidated")
        self._wrapped.write_data(data)

    def read_data(self) -> str:
        current_time = time.time()
        if self._cache is not None and (current_time - self._cache_time) < self._ttl:
            self._cache_hits += 1
            print(f"  [CachingDecorator] Cache HIT (hits: {self._cache_hits})")
            return self._cache
        else:
            self._cache_misses += 1
            print(f"  [CachingDecorator] Cache MISS (misses: {self._cache_misses})")
            data = self._wrapped.read_data()
            self._cache = data
            self._cache_time = current_time
            return data

    def get_stats(self) -> dict[str, int]:
        return {"hits": self._cache_hits, "misses": self._cache_misses}


class ValidationDecorator(DataSourceDecorator):
    """Decorator that adds data validation."""

    def __init__(self, source: DataSource, max_length: int = 1000):
        super().__init__(source)
        self._max_length = max_length

    def write_data(self, data: str) -> None:
        if len(data) > self._max_length:
            raise ValueError(f"Data exceeds maximum length of {self._max_length}")
        if not data.strip():
            raise ValueError("Data cannot be empty or whitespace only")
        print("  [ValidationDecorator] Validation passed")
        self._wrapped.write_data(data)

    def read_data(self) -> str:
        return self._wrapped.read_data()


def main() -> None:
    print("=" * 60)
    print("Decorator Pattern - Data Processing Demo")
    print("=" * 60)

    # Demo 1: Simple usage without decorators
    print("\n--- Basic FileDataSource ---")
    simple_source = FileDataSource("data.txt")
    simple_source.write_data("Hello, World!")
    print(f"Read: {simple_source.read_data()}")

    # Demo 2: Add encryption
    print("\n--- With Encryption ---")
    encrypted_source = EncryptionDecorator(FileDataSource("encrypted.txt"))
    encrypted_source.write_data("Secret Message")
    print(f"Read: {encrypted_source.read_data()}")

    # Demo 3: Stack multiple decorators
    print("\n--- Stacked Decorators (Logging + Compression + Encryption) ---")
    stacked_source = LoggingDecorator(
        CompressionDecorator(EncryptionDecorator(FileDataSource("secure.txt")))
    )
    test_data = "AAABBBCCCDDDEEEFFFGGG"  # Good for compression demo
    stacked_source.write_data(test_data)
    print(f"Read: {stacked_source.read_data()}")

    # Demo 4: Caching decorator
    print("\n--- Caching Decorator ---")
    cached_source = CachingDecorator(FileDataSource("cached.txt"), cache_ttl=10.0)
    cached_source.write_data("Cached content")

    # First read - cache miss
    cached_source.read_data()
    # Second read - cache hit
    cached_source.read_data()
    # Third read - still cache hit
    cached_source.read_data()

    print(f"Cache stats: {cached_source.get_stats()}")

    # Demo 5: Validation decorator
    print("\n--- Validation Decorator ---")
    validated_source = ValidationDecorator(FileDataSource("validated.txt"), max_length=50)

    try:
        validated_source.write_data("Valid short data")
    except ValueError as e:
        print(f"Validation error: {e}")

    try:
        validated_source.write_data("X" * 100)  # Too long
    except ValueError as e:
        print(f"  [ValidationDecorator] Validation error: {e}")

    # Demo 6: Different decorator combinations
    print("\n--- Different Combinations ---")

    # Compression then encryption
    print("\nCompression -> Encryption:")
    combo1 = EncryptionDecorator(CompressionDecorator(FileDataSource("combo1.txt")))
    combo1.write_data("AAABBBCCC")
    print(f"Read: {combo1.read_data()}")

    # Encryption then compression
    print("\nEncryption -> Compression:")
    combo2 = CompressionDecorator(EncryptionDecorator(FileDataSource("combo2.txt")))
    combo2.write_data("AAABBBCCC")
    print(f"Read: {combo2.read_data()}")

    # Demo 7: All decorators combined
    print("\n--- Full Stack (All Decorators) ---")
    full_stack = LoggingDecorator(
        CachingDecorator(
            ValidationDecorator(
                CompressionDecorator(
                    EncryptionDecorator(FileDataSource("fullstack.txt"))
                ),
                max_length=500,
            ),
            cache_ttl=5.0,
        ),
        log_prefix="FULL",
    )
    full_stack.write_data("Complete decorator stack test")
    full_stack.read_data()  # Cache miss
    full_stack.read_data()  # Cache hit

    print("\n" + "=" * 60)
    print("Benefits of Decorator Pattern:")
    print("=" * 60)
    print("1. More flexibility than static inheritance")
    print("2. Add/remove responsibilities at runtime")
    print("3. Combine behaviors by wrapping multiple decorators")
    print("4. Single Responsibility: each decorator one concern")
    print("5. Open/Closed: extend without modifying existing code")


if __name__ == "__main__":
    main()
