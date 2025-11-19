# Iterator Pattern

Provides a way to access elements of a collection sequentially without exposing its underlying representation.

## How to Run
```bash
cd java/iterator
mvn compile exec:java
```

## Key Source Code

### Iterator Interface (Lines 13-17)
```java
interface Iterator<T> {
    boolean hasNext();
    T next();
    void reset();
}
```

### Concrete Iterator (Lines 58-79)
```java
class BookShelfIterator implements Iterator<Book> {
    private BookShelf bookShelf;
    private int index;

    @Override
    public boolean hasNext() {
        return index < bookShelf.getLength();
    }

    @Override
    public Book next() {
        return bookShelf.getBookAt(index++);
    }
}
```

## Program Output
```
--- 1. Book Shelf Iterator ---
Forward iteration:
  "Design Patterns" by Gang of Four
  "Clean Code" by Robert Martin
  "Refactoring" by Martin Fowler

Reverse iteration:
  "The Pragmatic Programmer" by Hunt & Thomas
  "Refactoring" by Martin Fowler
  "Clean Code" by Robert Martin

--- 2. Binary Tree Traversal Iterators ---
In-order (sorted): 20 30 40 50 60 70 80
Pre-order: 50 30 20 40 70 60 80
Post-order: 20 40 30 60 80 70 50
```

## Pattern Benefits
- Uniform interface for traversing collections
- Supports multiple simultaneous traversals
- Different iterators for different algorithms

## Requirements
- Java 17 or higher
- Maven 3.x
