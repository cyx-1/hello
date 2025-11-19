# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Iterator Design Pattern Implementation

The Iterator pattern provides a way to access elements of a collection
sequentially without exposing the underlying representation. This enables
traversal of different data structures using a uniform interface.
"""

from __future__ import annotations
from collections.abc import Iterator as IteratorProtocol
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass
class Book:
    """Data class representing a book."""

    title: str
    author: str
    year: int
    isbn: str

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year})"


class BookIterator(IteratorProtocol[Book]):
    """Concrete iterator for iterating over books."""

    def __init__(self, books: list[Book], reverse: bool = False) -> None:
        self._books = books
        self._reverse = reverse
        self._index = len(books) - 1 if reverse else 0

    def __next__(self) -> Book:
        """Return the next book in the iteration."""
        if self._reverse:
            if self._index < 0:
                raise StopIteration
            book = self._books[self._index]
            self._index -= 1
        else:
            if self._index >= len(self._books):
                raise StopIteration
            book = self._books[self._index]
            self._index += 1
        return book

    def __iter__(self) -> BookIterator:
        return self


class BookCollection:
    """Aggregate class representing a collection of books."""

    def __init__(self) -> None:
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a book to the collection."""
        self._books.append(book)

    def __iter__(self) -> BookIterator:
        """Return a forward iterator."""
        return BookIterator(self._books)

    def reverse_iterator(self) -> BookIterator:
        """Return a reverse iterator."""
        return BookIterator(self._books, reverse=True)

    def __len__(self) -> int:
        return len(self._books)


class FilterIterator(IteratorProtocol[Book]):
    """Iterator that filters books based on a predicate."""

    def __init__(
        self, books: list[Book], predicate: callable[[Book], bool]
    ) -> None:
        self._books = books
        self._predicate = predicate
        self._index = 0

    def __next__(self) -> Book:
        """Return the next book matching the predicate."""
        while self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            if self._predicate(book):
                return book
        raise StopIteration

    def __iter__(self) -> FilterIterator:
        return self


class TreeNode(Generic[T]):
    """Node class for binary tree."""

    def __init__(self, value: T) -> None:
        self.value = value
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None


class BinaryTree(Generic[T]):
    """Binary tree with multiple iteration strategies."""

    def __init__(self) -> None:
        self.root: TreeNode[T] | None = None

    def inorder(self) -> IteratorProtocol[T]:
        """Return an inorder (left-root-right) iterator."""
        return InorderIterator(self.root)

    def preorder(self) -> IteratorProtocol[T]:
        """Return a preorder (root-left-right) iterator."""
        return PreorderIterator(self.root)

    def postorder(self) -> IteratorProtocol[T]:
        """Return a postorder (left-right-root) iterator."""
        return PostorderIterator(self.root)


class InorderIterator(IteratorProtocol[T]):
    """Iterator for inorder tree traversal."""

    def __init__(self, root: TreeNode[T] | None) -> None:
        self._stack: list[TreeNode[T]] = []
        self._current = root

    def __next__(self) -> T:
        while self._stack or self._current:
            if self._current:
                self._stack.append(self._current)
                self._current = self._current.left
            else:
                node = self._stack.pop()
                value = node.value
                self._current = node.right
                return value
        raise StopIteration

    def __iter__(self) -> InorderIterator[T]:
        return self


class PreorderIterator(IteratorProtocol[T]):
    """Iterator for preorder tree traversal."""

    def __init__(self, root: TreeNode[T] | None) -> None:
        self._stack: list[TreeNode[T]] = []
        if root:
            self._stack.append(root)

    def __next__(self) -> T:
        if not self._stack:
            raise StopIteration
        node = self._stack.pop()
        if node.right:
            self._stack.append(node.right)
        if node.left:
            self._stack.append(node.left)
        return node.value

    def __iter__(self) -> PreorderIterator[T]:
        return self


class PostorderIterator(IteratorProtocol[T]):
    """Iterator for postorder tree traversal."""

    def __init__(self, root: TreeNode[T] | None) -> None:
        self._stack: list[tuple[TreeNode[T], bool]] = []
        if root:
            self._stack.append((root, False))

    def __next__(self) -> T:
        while self._stack:
            node, visited = self._stack.pop()
            if visited:
                return node.value
            self._stack.append((node, True))
            if node.right:
                self._stack.append((node.right, False))
            if node.left:
                self._stack.append((node.left, False))
        raise StopIteration

    def __iter__(self) -> PostorderIterator[T]:
        return self


def main() -> None:
    """Demonstrate the Iterator pattern with various collections."""
    print("=" * 60)
    print("ITERATOR DESIGN PATTERN DEMONSTRATION")
    print("=" * 60)

    # Example 1: Basic Book Collection Iterator
    print("\n[1] Basic Book Collection Iterator:")
    print("-" * 40)

    library = BookCollection()
    library.add_book(Book("Design Patterns", "Gang of Four", 1994, "978-0201633610"))
    library.add_book(Book("Clean Code", "Robert Martin", 2008, "978-0132350884"))
    library.add_book(Book("The Pragmatic Programmer", "Hunt & Thomas", 1999, "978-0201616224"))
    library.add_book(Book("Refactoring", "Martin Fowler", 2018, "978-0134757599"))

    print("Forward iteration:")
    for i, book in enumerate(library, 1):
        print(f"  {i}. {book}")

    # Example 2: Reverse Iterator
    print("\n[2] Reverse Iterator:")
    print("-" * 40)

    print("Reverse iteration:")
    for i, book in enumerate(library.reverse_iterator(), 1):
        print(f"  {i}. {book}")

    # Example 3: Filter Iterator
    print("\n[3] Filter Iterator (books after 2000):")
    print("-" * 40)

    modern_books = FilterIterator(library._books, lambda b: b.year > 2000)
    print("Books published after 2000:")
    for i, book in enumerate(modern_books, 1):
        print(f"  {i}. {book}")

    # Example 4: Filter by author
    print("\n[4] Filter Iterator (author contains 'Martin'):")
    print("-" * 40)

    martin_books = FilterIterator(library._books, lambda b: "Martin" in b.author)
    print("Books by authors named Martin:")
    for i, book in enumerate(martin_books, 1):
        print(f"  {i}. {book}")

    # Example 5: Binary Tree with Multiple Traversal Strategies
    print("\n[5] Binary Tree Traversal Iterators:")
    print("-" * 40)

    #       10
    #      /  \
    #     5    15
    #    / \   / \
    #   3   7 12  20

    tree: BinaryTree[int] = BinaryTree()
    tree.root = TreeNode(10)
    tree.root.left = TreeNode(5)
    tree.root.right = TreeNode(15)
    tree.root.left.left = TreeNode(3)
    tree.root.left.right = TreeNode(7)
    tree.root.right.left = TreeNode(12)
    tree.root.right.right = TreeNode(20)

    print("Tree structure:")
    print("       10")
    print("      /  \\")
    print("     5    15")
    print("    / \\   / \\")
    print("   3   7 12  20")

    print("\nInorder traversal (left-root-right):")
    inorder_result = list(tree.inorder())
    print(f"  {inorder_result}")

    print("\nPreorder traversal (root-left-right):")
    preorder_result = list(tree.preorder())
    print(f"  {preorder_result}")

    print("\nPostorder traversal (left-right-root):")
    postorder_result = list(tree.postorder())
    print(f"  {postorder_result}")

    # Example 6: Generator-based Iterator (Pythonic approach)
    print("\n[6] Generator-based Iterator (Pythonic):")
    print("-" * 40)

    def paginate(items: list[Any], page_size: int) -> IteratorProtocol[list[Any]]:
        """Generator that yields items in pages."""
        for i in range(0, len(items), page_size):
            yield items[i : i + page_size]

    all_books = list(library)
    print(f"Paginating {len(all_books)} books (page size: 2):")
    for page_num, page in enumerate(paginate(all_books, 2), 1):
        print(f"  Page {page_num}:")
        for book in page:
            print(f"    - {book}")

    print("\n" + "=" * 60)
    print("Key Benefits of Iterator Pattern:")
    print("=" * 60)
    print("• Provides uniform interface to traverse different collections")
    print("• Hides internal structure of aggregates from clients")
    print("• Supports multiple simultaneous traversals")
    print("• Enables different traversal algorithms (forward, reverse, filtered)")
    print("• Python's iterator protocol (__iter__, __next__) is built-in")
    print("=" * 60)


if __name__ == "__main__":
    main()
