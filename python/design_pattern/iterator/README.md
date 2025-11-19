# Iterator Design Pattern

The Iterator pattern provides a way to access elements of a collection sequentially without exposing the underlying representation. This enables traversal of different data structures using a uniform interface.

## How to Run

```bash
uv run python main_iterator.py
```

## Key Source Code

### Book Data Class (lines 21-31)

Simple data class for collection items:

```python
21: @dataclass
22: class Book:
23:     """Data class representing a book."""
24:
25:     title: str
26:     author: str
27:     year: int
28:     isbn: str
29:
30:     def __str__(self) -> str:
31:         return f"'{self.title}' by {self.author} ({self.year})"
```

### Concrete Iterator (lines 34-57)

Implements the iterator protocol with forward/reverse support:

```python
34: class BookIterator(IteratorProtocol[Book]):
35:     """Concrete iterator for iterating over books."""
36:
37:     def __init__(self, books: list[Book], reverse: bool = False) -> None:
38:         self._books = books
39:         self._reverse = reverse
40:         self._index = len(books) - 1 if reverse else 0
41:
42:     def __next__(self) -> Book:
43:         """Return the next book in the iteration."""
44:         if self._reverse:
45:             if self._index < 0:
46:                 raise StopIteration
47:             book = self._books[self._index]
48:             self._index -= 1
49:         else:
50:             if self._index >= len(self._books):
51:                 raise StopIteration
52:             book = self._books[self._index]
53:             self._index += 1
54:         return book
```

### Aggregate Class (lines 60-79)

The collection that provides iterators:

```python
60: class BookCollection:
61:     """Aggregate class representing a collection of books."""
62:
63:     def __init__(self) -> None:
64:         self._books: list[Book] = []
65:
66:     def add_book(self, book: Book) -> None:
67:         """Add a book to the collection."""
68:         self._books.append(book)
69:
70:     def __iter__(self) -> BookIterator:
71:         """Return a forward iterator."""
72:         return BookIterator(self._books)
73:
74:     def reverse_iterator(self) -> BookIterator:
75:         """Return a reverse iterator."""
76:         return BookIterator(self._books, reverse=True)
```

### Filter Iterator (lines 82-102)

Iterator with predicate-based filtering:

```python
82: class FilterIterator(IteratorProtocol[Book]):
83:     """Iterator that filters books based on a predicate."""
84:
85:     def __init__(
86:         self, books: list[Book], predicate: callable[[Book], bool]
87:     ) -> None:
88:         self._books = books
89:         self._predicate = predicate
90:         self._index = 0
91:
92:     def __next__(self) -> Book:
93:         """Return the next book matching the predicate."""
94:         while self._index < len(self._books):
95:             book = self._books[self._index]
96:             self._index += 1
97:             if self._predicate(book):
98:                 return book
99:         raise StopIteration
```

### Tree Traversal Iterators (lines 133-199)

Multiple traversal strategies for binary trees:

```python
133: class InorderIterator(IteratorProtocol[T]):
134:     """Iterator for inorder tree traversal."""
135:
136:     def __init__(self, root: TreeNode[T] | None) -> None:
137:         self._stack: list[TreeNode[T]] = []
138:         self._current = root
139:
140:     def __next__(self) -> T:
141:         while self._stack or self._current:
142:             if self._current:
143:                 self._stack.append(self._current)
144:                 self._current = self._current.left
145:             else:
146:                 node = self._stack.pop()
147:                 value = node.value
148:                 self._current = node.right
149:                 return value
150:         raise StopIteration
```

### Generator-based Iterator (lines 290-293)

Pythonic approach using generators:

```python
290:    def paginate(items: list[Any], page_size: int) -> IteratorProtocol[list[Any]]:
291:        """Generator that yields items in pages."""
292:        for i in range(0, len(items), page_size):
293:            yield items[i : i + page_size]
```

## Program Output

```
============================================================
ITERATOR DESIGN PATTERN DEMONSTRATION
============================================================

[1] Basic Book Collection Iterator:
----------------------------------------
Forward iteration:
  1. 'Design Patterns' by Gang of Four (1994)
  2. 'Clean Code' by Robert Martin (2008)
  3. 'The Pragmatic Programmer' by Hunt & Thomas (1999)
  4. 'Refactoring' by Martin Fowler (2018)

[2] Reverse Iterator:
----------------------------------------
Reverse iteration:
  1. 'Refactoring' by Martin Fowler (2018)
  2. 'The Pragmatic Programmer' by Hunt & Thomas (1999)
  3. 'Clean Code' by Robert Martin (2008)
  4. 'Design Patterns' by Gang of Four (1994)

[3] Filter Iterator (books after 2000):
----------------------------------------
Books published after 2000:
  1. 'Clean Code' by Robert Martin (2008)
  2. 'Refactoring' by Martin Fowler (2018)

[4] Filter Iterator (author contains 'Martin'):
----------------------------------------
Books by authors named Martin:
  1. 'Clean Code' by Robert Martin (2008)
  2. 'Refactoring' by Martin Fowler (2018)

[5] Binary Tree Traversal Iterators:
----------------------------------------
Tree structure:
       10
      /  \
     5    15
    / \   / \
   3   7 12  20

Inorder traversal (left-root-right):
  [3, 5, 7, 10, 12, 15, 20]

Preorder traversal (root-left-right):
  [10, 5, 3, 7, 15, 12, 20]

Postorder traversal (left-right-root):
  [3, 7, 5, 12, 20, 15, 10]

[6] Generator-based Iterator (Pythonic):
----------------------------------------
Paginating 4 books (page size: 2):
  Page 1:
    - 'Design Patterns' by Gang of Four (1994)
    - 'Clean Code' by Robert Martin (2008)
  Page 2:
    - 'The Pragmatic Programmer' by Hunt & Thomas (1999)
    - 'Refactoring' by Martin Fowler (2018)

============================================================
Key Benefits of Iterator Pattern:
============================================================
• Provides uniform interface to traverse different collections
• Hides internal structure of aggregates from clients
• Supports multiple simultaneous traversals
• Enables different traversal algorithms (forward, reverse, filtered)
• Python's iterator protocol (__iter__, __next__) is built-in
============================================================
```

## Output Analysis

### Output Correlation with Source Code

| Output Section | Source Lines | Description |
|----------------|--------------|-------------|
| Forward iteration | 70-72, 49-53 | `__iter__()` returns BookIterator, `__next__()` increments index |
| Reverse iteration | 74-76, 44-48 | `reverse=True` starts at end, decrements index |
| Filter (year > 2000) | 234, 94-98 | Lambda predicate filters in `__next__()` |
| Filter (Martin) | 243, 94-98 | String predicate checks author name |
| Inorder traversal | 140-149 | Stack-based left-root-right traversal |
| Preorder traversal | 164-172 | Stack-based root-left-right traversal |
| Postorder traversal | 186-196 | Stack with visited flag for left-right-root |
| Pagination | 290-293 | Generator yields slices of items |

### Key Observations

1. **Iterator Protocol (lines 42-54, 56-57)**:
   - `__next__()` returns next item or raises `StopIteration`
   - `__iter__()` returns self, making iterator iterable
   - Python's `for` loop automatically calls these methods

2. **Bidirectional Traversal (lines 37-54)**:
   - Line 40: Index initialized based on direction
   - Forward: starts at 0, increments (line 53)
   - Reverse: starts at end, decrements (line 48)

3. **Filter Iterator (lines 92-98)**:
   - Skips non-matching items in `__next__()` loop
   - Only returns items where `predicate(book)` is True
   - Output shows only 2 of 4 books match year > 2000

4. **Tree Traversals (lines 133-196)**:
   - Inorder [3,5,7,10,12,15,20]: sorted order for BST
   - Preorder [10,5,3,7,15,12,20]: root first, useful for copying
   - Postorder [3,7,5,12,20,15,10]: children first, useful for deletion

5. **Generator Simplicity (lines 290-293)**:
   - `yield` automatically implements iterator protocol
   - No need for separate class with `__next__`
   - Pythonic way to create simple iterators

## Requirements

- Python >= 3.10 (uses modern type hints with `list[T]`, union syntax `|`, and `Generic[T]`)
