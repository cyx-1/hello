# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Proxy Pattern

The Proxy pattern provides a surrogate or placeholder for another object to
control access to it. The proxy acts as an intermediary, adding functionality
like lazy loading, access control, logging, or caching.

Key Components:
- Subject: Interface for RealSubject and Proxy
- RealSubject: The actual object that proxy represents
- Proxy: Controls access to RealSubject
"""

from abc import ABC, abstractmethod
from datetime import datetime
import time


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


# Logging Proxy
class LoggingImageProxy(Image):
    """Logging proxy that records all access to the image."""

    def __init__(self, filename: str):
        self.filename = filename
        self._real_image: HighResolutionImage | None = None
        self._access_log: list[dict[str, str]] = []

    def _log(self, action: str) -> None:
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "filename": self.filename,
        }
        self._access_log.append(entry)
        print(f"  [LogProxy] {entry['timestamp']} - {action}")

    def _get_real_image(self) -> HighResolutionImage:
        if self._real_image is None:
            self._log("LOAD")
            self._real_image = HighResolutionImage(self.filename)
        return self._real_image

    def display(self) -> str:
        self._log("DISPLAY")
        return self._get_real_image().display()

    def get_info(self) -> dict[str, str]:
        self._log("GET_INFO")
        return self._get_real_image().get_info()

    def get_access_log(self) -> list[dict[str, str]]:
        return self._access_log.copy()


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


# Remote Proxy (simulated)
class RemoteImageProxy(Image):
    """Simulates remote proxy for accessing images on remote server."""

    def __init__(self, filename: str, server: str = "cdn.example.com"):
        self.filename = filename
        self.server = server
        self._cached_data: dict[str, str] | None = None

    def display(self) -> str:
        print(f"  [RemoteProxy] Fetching {self.filename} from {self.server}...")
        time.sleep(0.05)  # Simulate network latency
        return f"Displaying remote image: https://{self.server}/{self.filename}"

    def get_info(self) -> dict[str, str]:
        if self._cached_data is None:
            print(f"  [RemoteProxy] Requesting metadata from {self.server}...")
            time.sleep(0.05)
            self._cached_data = {
                "filename": self.filename,
                "server": self.server,
                "url": f"https://{self.server}/{self.filename}",
            }
        return self._cached_data


def main() -> None:
    print("=" * 60)
    print("Proxy Pattern - Image Loading Demo")
    print("=" * 60)

    # Demo 1: Virtual Proxy (Lazy Loading)
    print("\n--- Virtual Proxy (Lazy Loading) ---")
    print("Creating proxy (no loading yet):")
    proxy = ImageProxy("vacation_photo.jpg")
    print("Proxy created.\n")

    print("First display (triggers loading):")
    print(proxy.display())

    print("\nSecond display (already loaded):")
    print(proxy.display())

    # Demo 2: Protection Proxy
    print("\n\n--- Protection Proxy (Access Control) ---")
    secure_img = SecureImage("confidential.jpg", ["admin", "manager"])

    secure_img.set_user("admin")
    print(secure_img.display())

    print()
    secure_img.set_user("guest")
    print(secure_img.display())

    # Demo 3: Logging Proxy
    print("\n\n--- Logging Proxy ---")
    logging_img = LoggingImageProxy("tracked_image.jpg")

    logging_img.display()
    logging_img.get_info()
    logging_img.display()

    print("\nAccess log:")
    for entry in logging_img.get_access_log():
        print(f"  {entry}")

    # Demo 4: Caching Proxy
    print("\n\n--- Caching Proxy ---")
    CachingImageProxy.clear_cache()

    # Access same file multiple times
    for _ in range(3):
        img = CachingImageProxy("shared_resource.jpg")
        img.display()

    print(f"\nCache size: {CachingImageProxy.get_cache_size()} images")

    # Access different file
    img2 = CachingImageProxy("another_file.jpg")
    img2.display()

    print(f"Cache size: {CachingImageProxy.get_cache_size()} images")

    # Demo 5: Remote Proxy
    print("\n\n--- Remote Proxy ---")
    remote = RemoteImageProxy("banner.png", "images.cdn.com")
    print(remote.display())
    print(f"Info: {remote.get_info()}")

    # Demo 6: Compare proxy with direct access
    print("\n\n--- Comparison: Proxy vs Direct Access ---")

    print("\nWithout proxy (immediate loading):")
    start = time.time()
    direct = HighResolutionImage("direct.jpg")
    direct_time = time.time() - start
    print(f"Time: {direct_time:.3f}s")
    _ = direct.display()  # Use the variable

    print("\nWith proxy (deferred loading):")
    start = time.time()
    proxy = ImageProxy("proxied.jpg")
    proxy_create_time = time.time() - start
    print(f"Proxy creation time: {proxy_create_time:.3f}s")

    start = time.time()
    proxy.display()
    proxy_load_time = time.time() - start
    print(f"First access time: {proxy_load_time:.3f}s")

    print("\n" + "=" * 60)
    print("Types of Proxies:")
    print("=" * 60)
    print("1. Virtual Proxy: Delays expensive object creation")
    print("2. Protection Proxy: Controls access to object")
    print("3. Remote Proxy: Represents object in different address space")
    print("4. Logging Proxy: Adds logging when accessing object")
    print("5. Caching Proxy: Caches results of expensive operations")

    print("\n" + "=" * 60)
    print("Benefits of Proxy Pattern:")
    print("=" * 60)
    print("1. Control access without modifying original object")
    print("2. Manage lifecycle of service objects")
    print("3. Works even if service object isn't ready/available")
    print("4. Open/Closed: new proxies without changing service")


if __name__ == "__main__":
    main()
