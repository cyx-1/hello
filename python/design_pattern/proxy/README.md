# Proxy Pattern

The Proxy pattern provides a surrogate or placeholder for another object to control access to it. The proxy acts as an intermediary, adding functionality like lazy loading, access control, logging, or caching without modifying the original object.

**Requires Python 3.10+** (uses union types with `|` syntax)

## Key Components

- **Subject** (`Image`): Interface for RealSubject and Proxy
- **RealSubject** (`HighResolutionImage`): The actual object that proxy represents
- **Proxy Types**: Various proxies that control access (Virtual, Protection, Logging, Caching, Remote)

## Source Code

### Subject Interface and Real Subject

```python:main_proxy.py startLine=23 endLine=61
# Subject interface
class Image(ABC):
    """Abstract interface for images."""

    @abstractmethod
    def display(self) -> str:
        pass

    @abstractmethod
    def get_info(self) -> dict[str, str]:
        pass


# Real Subject
class HighResolutionImage(Image):
    """Real subject: expensive-to-load high resolution image."""

    def __init__(self, filename: str):
        self.filename = filename
        self._load_image()

    def _load_image(self) -> None:
        """Simulate expensive image loading."""
        print(f"  [RealImage] Loading '{self.filename}' from disk...")
        time.sleep(0.1)  # Simulate loading time
        self._data = f"[Image data for {self.filename}]"
        self._width = 3840
        self._height = 2160
        print(f"  [RealImage] Loaded {self._width}x{self._height} image")

    def display(self) -> str:
        return f"Displaying {self.filename} ({self._width}x{self._height})"

    def get_info(self) -> dict[str, str]:
        return {
            "filename": self.filename,
            "resolution": f"{self._width}x{self._height}",
            "size": f"{len(self._data)} bytes",
        }
```

### Virtual Proxy (Lazy Loading)

```python:main_proxy.py startLine=64 endLine=84
# Virtual Proxy (Lazy Loading)
class ImageProxy(Image):
    """Virtual proxy that delays loading until actually needed."""

    def __init__(self, filename: str):
        self.filename = filename
        self._real_image: HighResolutionImage | None = None

    def _get_real_image(self) -> HighResolutionImage:
        """Lazy load the real image."""
        if self._real_image is None:
            print("  [Proxy] First access - loading image")
            self._real_image = HighResolutionImage(self.filename)
        return self._real_image

    def display(self) -> str:
        return self._get_real_image().display()

    def get_info(self) -> dict[str, str]:
        return self._get_real_image().get_info()
```

### Protection Proxy (Access Control)

```python:main_proxy.py startLine=86 endLine=124
# Protection Proxy (Access Control)
class SecureImage(Image):
    """Protection proxy that controls access based on permissions."""

    def __init__(self, filename: str, allowed_users: list[str]):
        self.filename = filename
        self._allowed_users = allowed_users
        self._real_image: HighResolutionImage | None = None
        self._current_user: str = ""

    def set_user(self, username: str) -> None:
        """Set current user for access control."""
        self._current_user = username

    def _check_access(self) -> bool:
        """Check if current user has access."""
        if self._current_user in self._allowed_users:
            print(f"  [SecureProxy] Access granted to {self._current_user}")
            return True
        else:
            print(f"  [SecureProxy] Access DENIED to {self._current_user}")
            return False

    def _get_real_image(self) -> HighResolutionImage | None:
        if self._real_image is None:
            self._real_image = HighResolutionImage(self.filename)
        return self._real_image

    def display(self) -> str:
        if not self._check_access():
            return f"ACCESS DENIED: User '{self._current_user}' cannot view {self.filename}"
        img = self._get_real_image()
        return img.display() if img else "Error loading image"

    def get_info(self) -> dict[str, str]:
        if not self._check_access():
            return {"error": "Access denied"}
        img = self._get_real_image()
        return img.get_info() if img else {}
```

### Caching Proxy

```python:main_proxy.py startLine=163 endLine=193
# Caching Proxy
class CachingImageProxy(Image):
    """Caching proxy that caches expensive operation results."""

    _cache: dict[str, HighResolutionImage] = {}

    def __init__(self, filename: str):
        self.filename = filename

    def _get_real_image(self) -> HighResolutionImage:
        if self.filename not in self._cache:
            print(f"  [CacheProxy] Cache MISS for {self.filename}")
            self._cache[self.filename] = HighResolutionImage(self.filename)
        else:
            print(f"  [CacheProxy] Cache HIT for {self.filename}")
        return self._cache[self.filename]

    def display(self) -> str:
        return self._get_real_image().display()

    def get_info(self) -> dict[str, str]:
        return self._get_real_image().get_info()

    @classmethod
    def get_cache_size(cls) -> int:
        return len(cls._cache)

    @classmethod
    def clear_cache(cls) -> None:
        cls._cache.clear()
```

## Program Output

```
============================================================
Proxy Pattern - Image Loading Demo
============================================================

--- Virtual Proxy (Lazy Loading) ---
Creating proxy (no loading yet):
Proxy created.

First display (triggers loading):
  [Proxy] First access - loading image
  [RealImage] Loading 'vacation_photo.jpg' from disk...
  [RealImage] Loaded 3840x2160 image
Displaying vacation_photo.jpg (3840x2160)

Second display (already loaded):
Displaying vacation_photo.jpg (3840x2160)


--- Protection Proxy (Access Control) ---
  [SecureProxy] Access granted to admin
  [RealImage] Loading 'confidential.jpg' from disk...
  [RealImage] Loaded 3840x2160 image
Displaying confidential.jpg (3840x2160)

  [SecureProxy] Access DENIED to guest
ACCESS DENIED: User 'guest' cannot view confidential.jpg


--- Logging Proxy ---
  [LogProxy] 2025-11-18 23:52:32 - DISPLAY
  [LogProxy] 2025-11-18 23:52:32 - LOAD
  [RealImage] Loading 'tracked_image.jpg' from disk...
  [RealImage] Loaded 3840x2160 image
  [LogProxy] 2025-11-18 23:52:32 - GET_INFO
  [LogProxy] 2025-11-18 23:52:32 - DISPLAY

Access log:
  {'timestamp': '2025-11-18 23:52:32', 'action': 'DISPLAY', 'filename': 'tracked_image.jpg'}
  {'timestamp': '2025-11-18 23:52:32', 'action': 'LOAD', 'filename': 'tracked_image.jpg'}
  {'timestamp': '2025-11-18 23:52:32', 'action': 'GET_INFO', 'filename': 'tracked_image.jpg'}
  {'timestamp': '2025-11-18 23:52:32', 'action': 'DISPLAY', 'filename': 'tracked_image.jpg'}


--- Caching Proxy ---
  [CacheProxy] Cache MISS for shared_resource.jpg
  [RealImage] Loading 'shared_resource.jpg' from disk...
  [RealImage] Loaded 3840x2160 image
  [CacheProxy] Cache HIT for shared_resource.jpg
  [CacheProxy] Cache HIT for shared_resource.jpg

Cache size: 1 images
  [CacheProxy] Cache MISS for another_file.jpg
  [RealImage] Loading 'another_file.jpg' from disk...
  [RealImage] Loaded 3840x2160 image
Cache size: 2 images


--- Remote Proxy ---
  [RemoteProxy] Fetching banner.png from images.cdn.com...
Displaying remote image: https://images.cdn.com/banner.png
  [RemoteProxy] Requesting metadata from images.cdn.com...
Info: {'filename': 'banner.png', 'server': 'images.cdn.com', 'url': 'https://images.cdn.com/banner.png'}


--- Comparison: Proxy vs Direct Access ---

Without proxy (immediate loading):
  [RealImage] Loading 'direct.jpg' from disk...
  [RealImage] Loaded 3840x2160 image
Time: 0.101s

With proxy (deferred loading):
Proxy creation time: 0.000s
  [Proxy] First access - loading image
  [RealImage] Loading 'proxied.jpg' from disk...
  [RealImage] Loaded 3840x2160 image
First access time: 0.101s

============================================================
Types of Proxies:
============================================================
1. Virtual Proxy: Delays expensive object creation
2. Protection Proxy: Controls access to object
3. Remote Proxy: Represents object in different address space
4. Logging Proxy: Adds logging when accessing object
5. Caching Proxy: Caches results of expensive operations

============================================================
Benefits of Proxy Pattern:
============================================================
1. Control access without modifying original object
2. Manage lifecycle of service objects
3. Works even if service object isn't ready/available
4. Open/Closed: new proxies without changing service
```

## Annotations

### Virtual Proxy - Lazy Loading (Lines 64-84)
The `ImageProxy` (line 65) delays the expensive image loading until first access. Output shows:
- "Proxy created" - instant, no loading
- First `display()` - triggers "[Proxy] First access - loading image" then actual loading
- Second `display()` - no loading message, uses cached real image

### Protection Proxy - Access Control (Lines 86-124)
The `SecureImage` (line 87) checks user permissions before allowing access. Output shows:
- "admin" user: Access granted, image loads and displays
- "guest" user: Access denied, returns error message without loading image

Note: The image is only loaded once (for admin), then the guest denial doesn't trigger another load.

### Logging Proxy (Lines 127-160)
The `LoggingImageProxy` (line 128) records all access operations. Output shows:
- Each operation (DISPLAY, LOAD, GET_INFO) is timestamped
- The access log maintains a complete audit trail
- Second DISPLAY doesn't trigger LOAD (already loaded)

### Caching Proxy (Lines 163-193)
The `CachingImageProxy` (line 164) uses a class-level cache. Output shows:
- First access to "shared_resource.jpg": Cache MISS, loads image
- Second and third access: Cache HIT, no loading
- Different file "another_file.jpg": New Cache MISS
- Cache grows to 2 images

### Remote Proxy (Lines 195-218)
The `RemoteImageProxy` (line 196) simulates accessing remote resources. Output shows network operations with simulated latency for both display and metadata retrieval.

### Performance Comparison (Lines 285-303)
The output demonstrates the key benefit of virtual proxy:
- Direct access: Loading happens immediately at construction (0.101s)
- Proxy: Creation is instant (0.000s), loading deferred to first use

This is critical when you might not use the object, or need to defer expensive initialization.

## Running the Code

```bash
uv run python main_proxy.py
```
