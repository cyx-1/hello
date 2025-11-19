# Composite Pattern

The Composite pattern composes objects into tree structures to represent part-whole hierarchies, allowing clients to treat individual objects and compositions uniformly.

## How to Run

```bash
cd java/composite
mvn compile exec:java
```

## Key Source Code

### Component Interface (Lines 12-19)
```java
interface FileSystemComponent {
    String getName();
    int getSize();
    void display(String indent);
    void add(FileSystemComponent component);
    void remove(FileSystemComponent component);
}
```

### Leaf (Lines 22-50)
```java
class File implements FileSystemComponent {
    @Override
    public int getSize() { return size; }

    @Override
    public void display(String indent) {
        System.out.println(indent + "📄 " + name + " (" + size + " KB)");
    }

    @Override
    public void add(FileSystemComponent component) {
        throw new UnsupportedOperationException("Cannot add to a file");
    }
}
```

### Composite (Lines 53-82)
```java
class Directory implements FileSystemComponent {
    private List<FileSystemComponent> children = new ArrayList<>();

    @Override
    public int getSize() {
        int totalSize = 0;
        for (FileSystemComponent child : children) {
            totalSize += child.getSize();
        }
        return totalSize;
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + "📁 " + name + " (" + getSize() + " KB)");
        for (FileSystemComponent child : children) {
            child.display(indent + "  ");
        }
    }
}
```

## Program Output

```
=== Composite Pattern Demonstration ===

--- 1. File System Structure ---
📁 root (6745 KB)
  📁 Documents (200 KB)
    📄 resume.pdf (150 KB)
    📄 cover_letter.docx (50 KB)
  📁 Photos (6500 KB)
    📁 Vacation (5700 KB)
      📄 beach.jpg (2500 KB)
      📄 mountain.jpg (3200 KB)
    📄 profile.png (800 KB)
  📁 Code (40 KB)
    📄 main.java (25 KB)
    📄 utils.java (15 KB)
  📄 readme.txt (5 KB)

Total size: 6745 KB

--- 2. Organization Hierarchy ---
🏢 TechCorp - Total: $885000
  🏢 Engineering - Total: $655000
    👤 Alice (CTO) - $250000
    👤 Bob (Senior Developer) - $120000
    👤 Charlie (Developer) - $90000
    🏢 Backend Team - Total: $195000
      👤 Dave (Lead) - $110000
      👤 Eve (Developer) - $85000
  🏢 Sales - Total: $230000
    👤 Frank (Sales Director) - $150000
    👤 Grace (Account Manager) - $80000
```

## Pattern Benefits

1. **Uniformity**: Treat individual objects and compositions the same way
2. **Recursive Composition**: Build complex tree structures
3. **Easy to Add**: New component types integrate easily

## Requirements

- Java 17 or higher
- Maven 3.x
