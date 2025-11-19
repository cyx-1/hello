# Decorator Pattern

The Decorator pattern attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality by wrapping objects with decorator classes.

**Requires Python 3.10+** (uses union types with `|` syntax)

## Key Components

- **Component** (`DataSource`): Interface for objects that can have responsibilities added
- **ConcreteComponent** (`FileDataSource`): Object to which responsibilities can be added
- **Decorator** (`DataSourceDecorator`): Maintains reference to Component and conforms to its interface
- **ConcreteDecorators**: Add specific responsibilities (encryption, compression, logging, caching, validation)

## Source Code

### Component Interface and Base Decorator

```python:main_decorator.py startLine=23 endLine=64
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
```

### Encryption Decorator Example

```python:main_decorator.py startLine=67 endLine=106
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
```

### Stacking Multiple Decorators

```python:main_decorator.py startLine=263 endLine=269
    # Demo 3: Stack multiple decorators
    print("\n--- Stacked Decorators (Logging + Compression + Encryption) ---")
    stacked_source = LoggingDecorator(
        CompressionDecorator(EncryptionDecorator(FileDataSource("secure.txt")))
    )
    test_data = "AAABBBCCCDDDEEEFFFGGG"  # Good for compression demo
    stacked_source.write_data(test_data)
```

## Program Output

```
============================================================
Decorator Pattern - Data Processing Demo
============================================================

--- Basic FileDataSource ---
  [FileDataSource] Written 13 chars to data.txt
  [FileDataSource] Read 13 chars from data.txt
Read: Hello, World!

--- With Encryption ---
  [EncryptionDecorator] Encrypted data (Caesar cipher, shift=3)
  [FileDataSource] Written 14 chars to encrypted.txt
  [FileDataSource] Read 14 chars from encrypted.txt
  [EncryptionDecorator] Decrypted data
Read: Secret Message

--- Stacked Decorators (Logging + Compression + Encryption) ---
  [LoggingDecorator] [LOG][2025-11-18 23:52:13] WRITE: 21 chars
  [CompressionDecorator] Compressed: 21 -> 14 chars
  [EncryptionDecorator] Encrypted data (Caesar cipher, shift=3)
  [FileDataSource] Written 14 chars to secure.txt
  [FileDataSource] Read 14 chars from secure.txt
  [EncryptionDecorator] Decrypted data
  [CompressionDecorator] Decompressed: 14 -> 21 chars
  [LoggingDecorator] [LOG][2025-11-18 23:52:13] READ: 21 chars
Read: AAABBBCCCDDDEEEFFFGGG

--- Caching Decorator ---
  [CachingDecorator] Cache invalidated
  [FileDataSource] Written 14 chars to cached.txt
  [CachingDecorator] Cache MISS (misses: 1)
  [FileDataSource] Read 14 chars from cached.txt
  [CachingDecorator] Cache HIT (hits: 1)
  [CachingDecorator] Cache HIT (hits: 2)
Cache stats: {'hits': 2, 'misses': 1}

--- Validation Decorator ---
  [ValidationDecorator] Validation passed
  [FileDataSource] Written 16 chars to validated.txt
  [ValidationDecorator] Validation error: Data exceeds maximum length of 50

--- Different Combinations ---

Compression -> Encryption:
  [EncryptionDecorator] Encrypted data (Caesar cipher, shift=3)
  [CompressionDecorator] Compressed: 9 -> 6 chars
  [FileDataSource] Written 6 chars to combo1.txt
  [FileDataSource] Read 6 chars from combo1.txt
  [CompressionDecorator] Decompressed: 6 -> 9 chars
  [EncryptionDecorator] Decrypted data
Read: AAABBBCCC

Encryption -> Compression:
  [CompressionDecorator] Compressed: 9 -> 6 chars
  [EncryptionDecorator] Encrypted data (Caesar cipher, shift=3)
  [FileDataSource] Written 6 chars to combo2.txt
  [FileDataSource] Read 6 chars from combo2.txt
  [EncryptionDecorator] Decrypted data
  [CompressionDecorator] Decompressed: 6 -> 9 chars
Read: AAABBBCCC

--- Full Stack (All Decorators) ---
  [LoggingDecorator] [FULL][2025-11-18 23:52:13] WRITE: 29 chars
  [CachingDecorator] Cache invalidated
  [ValidationDecorator] Validation passed
  [CompressionDecorator] Compressed: 29 -> 29 chars
  [EncryptionDecorator] Encrypted data (Caesar cipher, shift=3)
  [FileDataSource] Written 29 chars to fullstack.txt
  [CachingDecorator] Cache MISS (misses: 1)
  [FileDataSource] Read 29 chars from fullstack.txt
  [EncryptionDecorator] Decrypted data
  [CompressionDecorator] Decompressed: 29 -> 29 chars
  [LoggingDecorator] [FULL][2025-11-18 23:52:13] READ: 29 chars
  [CachingDecorator] Cache HIT (hits: 1)
  [LoggingDecorator] [FULL][2025-11-18 23:52:13] READ: 29 chars

============================================================
Benefits of Decorator Pattern:
============================================================
1. More flexibility than static inheritance
2. Add/remove responsibilities at runtime
3. Combine behaviors by wrapping multiple decorators
4. Single Responsibility: each decorator one concern
5. Open/Closed: extend without modifying existing code
```

## Annotations

### Basic Usage (Lines 251-254)
The `FileDataSource` (line 37) is the concrete component that stores data. Output shows direct write/read operations without any decoration.

### Encryption Decorator (Lines 257-260)
The `EncryptionDecorator` (line 68) wraps the file source. On write, it encrypts first then delegates to wrapped object. On read, it reads from wrapped object then decrypts. Output shows the encryption/decryption messages surrounding the file operations.

### Stacked Decorators (Lines 263-269)
Decorators are nested: `LoggingDecorator(CompressionDecorator(EncryptionDecorator(FileDataSource)))`.
- **Write flow** (outside-in): Logging -> Compression -> Encryption -> File
- **Read flow** (inside-out): File -> Encryption -> Compression -> Logging

The output clearly shows this chain where logging happens first on write, then compression reduces 21 to 14 chars, then encryption, then file storage.

### Caching Decorator (Lines 272-283)
The `CachingDecorator` (line 192) demonstrates cache invalidation on write and cache hits on subsequent reads. Output shows 1 miss followed by 2 hits.

### Validation Decorator (Lines 286-297)
The `ValidationDecorator` (line 226) checks data constraints before passing to wrapped object. Output shows validation passing for short data but failing for data exceeding 50 chars.

### Decorator Order Matters (Lines 299-312)
Two different orderings produce same result but process differently:
- Compression->Encryption: encrypts first, then compresses encrypted text
- Encryption->Compression: compresses first, then encrypts compressed text

## Running the Code

```bash
uv run python main_decorator.py
```
