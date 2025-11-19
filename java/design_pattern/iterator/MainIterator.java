/**
 * Comprehensive demonstration of the Iterator Pattern in Java
 *
 * The Iterator pattern provides a way to access the elements of an aggregate
 * object sequentially without exposing its underlying representation.
 */

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

// Iterator interface
interface Iterator<T> {
    boolean hasNext();
    T next();
    void reset();
}

// Aggregate interface
interface IterableCollection<T> {
    Iterator<T> createIterator();
}

// Concrete collection - Book shelf
class Book {
    private String title;
    private String author;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    public String getTitle() { return title; }
    public String getAuthor() { return author; }

    @Override
    public String toString() {
        return "\"" + title + "\" by " + author;
    }
}

class BookShelf implements IterableCollection<Book> {
    private List<Book> books = new ArrayList<>();

    public void addBook(Book book) {
        books.add(book);
    }

    public int getLength() {
        return books.size();
    }

    public Book getBookAt(int index) {
        return books.get(index);
    }

    @Override
    public Iterator<Book> createIterator() {
        return new BookShelfIterator(this);
    }

    // Create reverse iterator
    public Iterator<Book> createReverseIterator() {
        return new ReverseBookShelfIterator(this);
    }
}

// Concrete Iterator
class BookShelfIterator implements Iterator<Book> {
    private BookShelf bookShelf;
    private int index;

    public BookShelfIterator(BookShelf bookShelf) {
        this.bookShelf = bookShelf;
        this.index = 0;
    }

    @Override
    public boolean hasNext() {
        return index < bookShelf.getLength();
    }

    @Override
    public Book next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        return bookShelf.getBookAt(index++);
    }

    @Override
    public void reset() {
        index = 0;
    }
}

// Reverse Iterator
class ReverseBookShelfIterator implements Iterator<Book> {
    private BookShelf bookShelf;
    private int index;

    public ReverseBookShelfIterator(BookShelf bookShelf) {
        this.bookShelf = bookShelf;
        this.index = bookShelf.getLength() - 1;
    }

    @Override
    public boolean hasNext() {
        return index >= 0;
    }

    @Override
    public Book next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        return bookShelf.getBookAt(index--);
    }

    @Override
    public void reset() {
        index = bookShelf.getLength() - 1;
    }
}

// Binary Tree example with different traversal iterators

class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    public TreeNode(int value) {
        this.value = value;
    }
}

class BinaryTree implements IterableCollection<Integer> {
    private TreeNode root;

    public BinaryTree() {}

    public void insert(int value) {
        root = insertRec(root, value);
    }

    private TreeNode insertRec(TreeNode node, int value) {
        if (node == null) {
            return new TreeNode(value);
        }
        if (value < node.value) {
            node.left = insertRec(node.left, value);
        } else {
            node.right = insertRec(node.right, value);
        }
        return node;
    }

    @Override
    public Iterator<Integer> createIterator() {
        return new InOrderIterator(root);
    }

    public Iterator<Integer> createPreOrderIterator() {
        return new PreOrderIterator(root);
    }

    public Iterator<Integer> createPostOrderIterator() {
        return new PostOrderIterator(root);
    }
}

// In-order traversal iterator
class InOrderIterator implements Iterator<Integer> {
    private List<Integer> values = new ArrayList<>();
    private int index = 0;

    public InOrderIterator(TreeNode root) {
        inOrder(root);
    }

    private void inOrder(TreeNode node) {
        if (node != null) {
            inOrder(node.left);
            values.add(node.value);
            inOrder(node.right);
        }
    }

    @Override
    public boolean hasNext() {
        return index < values.size();
    }

    @Override
    public Integer next() {
        return values.get(index++);
    }

    @Override
    public void reset() {
        index = 0;
    }
}

// Pre-order traversal iterator
class PreOrderIterator implements Iterator<Integer> {
    private List<Integer> values = new ArrayList<>();
    private int index = 0;

    public PreOrderIterator(TreeNode root) {
        preOrder(root);
    }

    private void preOrder(TreeNode node) {
        if (node != null) {
            values.add(node.value);
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    @Override
    public boolean hasNext() {
        return index < values.size();
    }

    @Override
    public Integer next() {
        return values.get(index++);
    }

    @Override
    public void reset() {
        index = 0;
    }
}

// Post-order traversal iterator
class PostOrderIterator implements Iterator<Integer> {
    private List<Integer> values = new ArrayList<>();
    private int index = 0;

    public PostOrderIterator(TreeNode root) {
        postOrder(root);
    }

    private void postOrder(TreeNode node) {
        if (node != null) {
            postOrder(node.left);
            postOrder(node.right);
            values.add(node.value);
        }
    }

    @Override
    public boolean hasNext() {
        return index < values.size();
    }

    @Override
    public Integer next() {
        return values.get(index++);
    }

    @Override
    public void reset() {
        index = 0;
    }
}

// Filtering Iterator example

class FilteringIterator<T> implements Iterator<T> {
    private Iterator<T> innerIterator;
    private java.util.function.Predicate<T> predicate;
    private T nextItem;
    private boolean hasNextItem;

    public FilteringIterator(Iterator<T> iterator, java.util.function.Predicate<T> predicate) {
        this.innerIterator = iterator;
        this.predicate = predicate;
        findNext();
    }

    private void findNext() {
        hasNextItem = false;
        while (innerIterator.hasNext()) {
            T item = innerIterator.next();
            if (predicate.test(item)) {
                nextItem = item;
                hasNextItem = true;
                break;
            }
        }
    }

    @Override
    public boolean hasNext() {
        return hasNextItem;
    }

    @Override
    public T next() {
        if (!hasNextItem) {
            throw new NoSuchElementException();
        }
        T item = nextItem;
        findNext();
        return item;
    }

    @Override
    public void reset() {
        innerIterator.reset();
        findNext();
    }
}

public class MainIterator {
    public static void main(String[] args) {
        System.out.println("=== Iterator Pattern Demonstration ===\n");

        // Book shelf example
        System.out.println("--- 1. Book Shelf Iterator ---");

        BookShelf shelf = new BookShelf();
        shelf.addBook(new Book("Design Patterns", "Gang of Four"));
        shelf.addBook(new Book("Clean Code", "Robert Martin"));
        shelf.addBook(new Book("Refactoring", "Martin Fowler"));
        shelf.addBook(new Book("The Pragmatic Programmer", "Hunt & Thomas"));

        System.out.println("\nForward iteration:");
        Iterator<Book> iterator = shelf.createIterator();
        while (iterator.hasNext()) {
            System.out.println("  " + iterator.next());
        }

        System.out.println("\nReverse iteration:");
        Iterator<Book> reverseIterator = shelf.createReverseIterator();
        while (reverseIterator.hasNext()) {
            System.out.println("  " + reverseIterator.next());
        }
        System.out.println();

        // Binary tree example
        System.out.println("--- 2. Binary Tree Traversal Iterators ---");

        BinaryTree tree = new BinaryTree();
        tree.insert(50);
        tree.insert(30);
        tree.insert(70);
        tree.insert(20);
        tree.insert(40);
        tree.insert(60);
        tree.insert(80);

        System.out.println("\nTree structure:");
        System.out.println("       50");
        System.out.println("      /  \\");
        System.out.println("    30    70");
        System.out.println("   /  \\  /  \\");
        System.out.println("  20  40 60  80");

        System.out.print("\nIn-order (sorted): ");
        Iterator<Integer> inOrder = tree.createIterator();
        while (inOrder.hasNext()) {
            System.out.print(inOrder.next() + " ");
        }

        System.out.print("\nPre-order: ");
        Iterator<Integer> preOrder = tree.createPreOrderIterator();
        while (preOrder.hasNext()) {
            System.out.print(preOrder.next() + " ");
        }

        System.out.print("\nPost-order: ");
        Iterator<Integer> postOrder = tree.createPostOrderIterator();
        while (postOrder.hasNext()) {
            System.out.print(postOrder.next() + " ");
        }
        System.out.println("\n");

        // Filtering iterator example
        System.out.println("--- 3. Filtering Iterator ---");

        BookShelf techShelf = new BookShelf();
        techShelf.addBook(new Book("Java Concurrency", "Brian Goetz"));
        techShelf.addBook(new Book("Effective Java", "Joshua Bloch"));
        techShelf.addBook(new Book("Python Crash Course", "Eric Matthes"));
        techShelf.addBook(new Book("JavaScript: The Good Parts", "Douglas Crockford"));
        techShelf.addBook(new Book("Learning Java", "Patrick Niemeyer"));

        System.out.println("\nAll books:");
        Iterator<Book> allBooks = techShelf.createIterator();
        while (allBooks.hasNext()) {
            System.out.println("  " + allBooks.next());
        }

        System.out.println("\nFiltered (Java books only):");
        allBooks.reset();
        FilteringIterator<Book> javaBooks = new FilteringIterator<>(
            allBooks,
            book -> book.getTitle().toLowerCase().contains("java")
        );
        while (javaBooks.hasNext()) {
            System.out.println("  " + javaBooks.next());
        }

        System.out.println("\n=== Summary ===");
        System.out.println("Iterator pattern benefits:");
        System.out.println("  - Provides uniform interface for traversing collections");
        System.out.println("  - Supports multiple simultaneous traversals");
        System.out.println("  - Simplifies collection interface");
        System.out.println("  - Different iterators for different traversal algorithms");
        System.out.println("\nNote: Java's java.util.Iterator is a built-in implementation");
    }
}
