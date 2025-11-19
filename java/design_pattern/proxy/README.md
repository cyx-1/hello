# Proxy Pattern

The Proxy pattern provides a surrogate or placeholder for another object to control access to it.

## How to Run

```bash
cd java/proxy
mvn compile exec:java
```

## Key Source Code

### Virtual Proxy - Lazy Loading (Lines 35-52)
```java
class ProxyImage implements Image {
    private RealImage realImage;
    private String filename;

    @Override
    public void display() {
        if (realImage == null) {
            realImage = new RealImage(filename);  // Load on demand
        }
        realImage.display();
    }
}
```

### Protection Proxy - Access Control (Lines 75-106)
```java
class ProtectedDocumentProxy implements Document {
    private String userRole;

    @Override
    public void write(String content) {
        if (!userRole.equals("admin") && !userRole.equals("editor")) {
            System.out.println("Access denied! " + userRole + " cannot write.");
            return;
        }
        realDocument.write(content);
    }

    @Override
    public void delete() {
        if (!userRole.equals("admin")) {
            System.out.println("Access denied! Only admin can delete.");
            return;
        }
        realDocument.delete();
    }
}
```

### Caching Proxy (Lines 119-142)
```java
class CachingProxy implements DataService {
    private Map<String, String> cache = new HashMap<>();

    @Override
    public String fetchData(String key) {
        if (cache.containsKey(key)) {
            return cache.get(key);  // Return cached
        }
        String data = realService.fetchData(key);
        cache.put(key, data);
        return data;
    }
}
```

## Program Output

```
=== Proxy Pattern Demonstration ===

--- 1. Virtual Proxy (Lazy Loading) ---
Creating image proxies (no loading yet):

  [ProxyImage] Created proxy for: photo1.jpg
  [ProxyImage] Created proxy for: photo2.jpg
  [ProxyImage] Created proxy for: photo3.jpg

First access to image1 (loads from disk):
  [RealImage] Loading image from disk: photo1.jpg
  [RealImage] Displaying: photo1.jpg

Second access to image1 (already loaded):
  [RealImage] Displaying: photo1.jpg

image3 never accessed - never loaded!

--- 2. Protection Proxy (Access Control) ---

Editor user operations:
  [RealDocument] Reading: Original content
  [RealDocument] Content updated to: Editor's content
  [ProtectionProxy] Access denied! Only admin can delete.

--- 3. Caching Proxy ---

First fetch (cache miss):
  [RealDataService] Fetching data from database for key: user_123
  [CachingProxy] Data cached for: user_123

Second fetch same key (cache hit):
  [CachingProxy] Returning cached data for: user_123

--- 4. Logging Proxy ---
  [Log] add(10, 5) = 15
  [Log] subtract(10, 5) = 5
  [Log] multiply(10, 5) = 50
  [Log] divide(10, 5) = 2
```

## Proxy Types

| Type | Purpose |
|------|---------|
| Virtual | Lazy initialization, load on demand |
| Protection | Access control based on permissions |
| Caching | Cache expensive operation results |
| Logging | Log method calls and parameters |
| Remote | Represent remote objects locally |

## Requirements

- Java 17 or higher
- Maven 3.x
