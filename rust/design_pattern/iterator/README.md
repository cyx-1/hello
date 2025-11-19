# Iterator Design Pattern in Rust

## Description

The **Iterator** design pattern provides a way to access elements of a collection sequentially without exposing its underlying representation. In Rust, this pattern is deeply integrated into the language through the `Iterator` trait, making it one of the most idiomatic and powerful patterns to use.

Rust's iterator pattern offers:
- **Zero-cost abstractions**: Iterators compile to efficient machine code
- **Lazy evaluation**: Elements are computed on-demand
- **Composability**: Iterator adapters can be chained together
- **Memory safety**: Rust's ownership system prevents iterator invalidation

This example demonstrates a custom `BookShelf` collection with multiple iterator implementations, including a custom range-filtered iterator.

---

## Source Code

**File: `main_iterator.rs`**

```rust
  1  // Iterator Design Pattern in Rust
  2  // Demonstrates custom collection with idiomatic Iterator trait implementation
  3
  4  use std::slice::Iter;
  5
  6  // Book struct representing items in our collection
  7  #[derive(Debug, Clone)]
  8  struct Book {
  9      title: String,
 10      author: String,
 11      year: u32,
 12  }
 13
 14  impl Book {
 15      fn new(title: &str, author: &str, year: u32) -> Self {
 16          Book {
 17              title: title.to_string(),
 18              author: author.to_string(),
 19              year,
 20          }
 21      }
 22  }
 23
 24  // Custom collection: BookShelf
 25  struct BookShelf {
 26      books: Vec<Book>,
 27  }
 28
 29  impl BookShelf {
 30      fn new() -> Self {
 31          BookShelf { books: Vec::new() }
 32      }
 33
 34      fn add_book(&mut self, book: Book) {
 35          self.books.push(book);
 36      }
 37
 38      fn len(&self) -> usize {
 39          self.books.len()
 40      }
 41
 42      // Return an iterator over borrowed books
 43      fn iter(&self) -> Iter<'_, Book> {
 44          self.books.iter()
 45      }
 46
 47      // Custom iterator that filters by year range
 48      fn books_in_range(&self, start_year: u32, end_year: u32) -> BookRangeIterator<'_> {
 49          BookRangeIterator {
 50              books: &self.books,
 51              index: 0,
 52              start_year,
 53              end_year,
 54          }
 55      }
 56  }
 57
 58  // Custom iterator for filtering books by year range
 59  struct BookRangeIterator<'a> {
 60      books: &'a Vec<Book>,
 61      index: usize,
 62      start_year: u32,
 63      end_year: u32,
 64  }
 65
 66  // Implement Iterator trait for our custom iterator
 67  impl<'a> Iterator for BookRangeIterator<'a> {
 68      type Item = &'a Book;
 69
 70      fn next(&mut self) -> Option<Self::Item> {
 71          while self.index < self.books.len() {
 72              let book = &self.books[self.index];
 73              self.index += 1;
 74              if book.year >= self.start_year && book.year <= self.end_year {
 75                  return Some(book);
 76              }
 77          }
 78          None
 79      }
 80  }
 81
 82  // Implement IntoIterator to enable for-loop syntax
 83  impl<'a> IntoIterator for &'a BookShelf {
 84      type Item = &'a Book;
 85      type IntoIter = Iter<'a, Book>;
 86
 87      fn into_iter(self) -> Self::IntoIter {
 88          self.books.iter()
 89      }
 90  }
 91
 92  // Consuming iterator implementation
 93  impl IntoIterator for BookShelf {
 94      type Item = Book;
 95      type IntoIter = std::vec::IntoIter<Book>;
 96
 97      fn into_iter(self) -> Self::IntoIter {
 98          self.books.into_iter()
 99      }
100  }
101
102  fn main() {
103      println!("=== Iterator Design Pattern in Rust ===\n");
104
105      // Create and populate the bookshelf
106      let mut shelf = BookShelf::new();
107
108      shelf.add_book(Book::new("The Rust Programming Language", "Steve Klabnik", 2018));
109      shelf.add_book(Book::new("Programming Rust", "Jim Blandy", 2021));
110      shelf.add_book(Book::new("Rust in Action", "Tim McNamara", 2021));
111      shelf.add_book(Book::new("Zero To Production", "Luca Palmieri", 2022));
112      shelf.add_book(Book::new("Rust for Rustaceans", "Jon Gjengset", 2021));
113
114      println!("BookShelf contains {} books\n", shelf.len());
115
116      // Demonstration 1: Basic for-loop iteration (using IntoIterator)
117      println!("--- Demo 1: Basic for-loop iteration ---");
118      for book in &shelf {
119          println!("  {} by {} ({})", book.title, book.author, book.year);
120      }
121      println!();
122
123      // Demonstration 2: Using iter() method with enumerate
124      println!("--- Demo 2: Using iter() with enumerate ---");
125      for (index, book) in shelf.iter().enumerate() {
126          println!("  [{}] {}", index, book.title);
127      }
128      println!();
129
130      // Demonstration 3: Iterator adapters (map, filter, collect)
131      println!("--- Demo 3: Iterator adapters ---");
132      let titles: Vec<&str> = shelf
133          .iter()
134          .filter(|book| book.year >= 2021)
135          .map(|book| book.title.as_str())
136          .collect();
137      println!("  Books from 2021 onwards:");
138      for title in &titles {
139          println!("    - {}", title);
140      }
141      println!();
142
143      // Demonstration 4: Custom iterator with year range filter
144      println!("--- Demo 4: Custom BookRangeIterator (2021-2022) ---");
145      for book in shelf.books_in_range(2021, 2022) {
146          println!("  {} ({})", book.title, book.year);
147      }
148      println!();
149
150      // Demonstration 5: Iterator methods (fold, count, any)
151      println!("--- Demo 5: Iterator methods ---");
152
153      let total_years: u32 = shelf.iter().map(|book| book.year).sum();
154      let avg_year = total_years as f64 / shelf.len() as f64;
155      println!("  Average publication year: {:.1}", avg_year);
156
157      let count_2021 = shelf.iter().filter(|book| book.year == 2021).count();
158      println!("  Books published in 2021: {}", count_2021);
159
160      let has_2022_book = shelf.iter().any(|book| book.year == 2022);
161      println!("  Has book from 2022: {}", has_2022_book);
162
163      let all_after_2000 = shelf.iter().all(|book| book.year > 2000);
164      println!("  All books after 2000: {}", all_after_2000);
165      println!();
166
167      // Demonstration 6: find and position
168      println!("--- Demo 6: find and position ---");
169      if let Some(book) = shelf.iter().find(|book| book.author.contains("Jon")) {
170          println!("  Found book by Jon: {}", book.title);
171      }
172
173      if let Some(pos) = shelf.iter().position(|book| book.title.contains("Action")) {
174          println!("  'Rust in Action' is at position: {}", pos);
175      }
176      println!();
177
178      // Demonstration 7: Consuming iterator (moves ownership)
179      println!("--- Demo 7: Consuming iterator ---");
180      let shelf_clone = BookShelf {
181          books: shelf.books.clone(),
182      };
183
184      for book in shelf_clone {
185          println!("  Consumed: {} ({})", book.title, book.year);
186      }
187      // shelf_clone is now moved and cannot be used
188
189      println!("\n=== Iterator Pattern Complete ===");
190  }
```

---

## Program Output

```
=== Iterator Design Pattern in Rust ===

BookShelf contains 5 books

--- Demo 1: Basic for-loop iteration ---
  The Rust Programming Language by Steve Klabnik (2018)
  Programming Rust by Jim Blandy (2021)
  Rust in Action by Tim McNamara (2021)
  Zero To Production by Luca Palmieri (2022)
  Rust for Rustaceans by Jon Gjengset (2021)

--- Demo 2: Using iter() with enumerate ---
  [0] The Rust Programming Language
  [1] Programming Rust
  [2] Rust in Action
  [3] Zero To Production
  [4] Rust for Rustaceans

--- Demo 3: Iterator adapters ---
  Books from 2021 onwards:
    - Programming Rust
    - Rust in Action
    - Zero To Production
    - Rust for Rustaceans

--- Demo 4: Custom BookRangeIterator (2021-2022) ---
  Programming Rust (2021)
  Rust in Action (2021)
  Zero To Production (2022)
  Rust for Rustaceans (2021)

--- Demo 5: Iterator methods ---
  Average publication year: 2020.6
  Books published in 2021: 3
  Has book from 2022: true
  All books after 2000: true

--- Demo 6: find and position ---
  Found book by Jon: Rust for Rustaceans
  'Rust in Action' is at position: 2

--- Demo 7: Consuming iterator ---
  Consumed: The Rust Programming Language (2018)
  Consumed: Programming Rust (2021)
  Consumed: Rust in Action (2021)
  Consumed: Zero To Production (2022)
  Consumed: Rust for Rustaceans (2021)

=== Iterator Pattern Complete ===
```

---

## Code Annotations

### Key Sections Explained

#### Lines 6-22: Data Structure Definition
The `Book` struct represents items in our collection. It derives `Debug` and `Clone` for debugging and cloning capabilities. The `new` constructor converts string slices to owned `String` types.

#### Lines 24-56: Custom Collection (BookShelf)
The `BookShelf` struct wraps a `Vec<Book>` and provides:
- `new()`: Creates an empty bookshelf
- `add_book()`: Adds a book to the collection
- `len()`: Returns the number of books
- `iter()`: Returns a borrowed iterator (line 43-45)
- `books_in_range()`: Returns a custom filtered iterator (lines 48-55)

#### Lines 58-80: Custom Iterator Implementation
`BookRangeIterator` is a custom iterator that filters books by year range:
- Lines 59-64: Struct holds a reference to books with lifetime `'a`, plus filter parameters
- Lines 67-80: Implements `Iterator` trait with `next()` method that skips books outside the year range

#### Lines 82-90: IntoIterator for Borrowed Collection
Implementing `IntoIterator` for `&BookShelf` enables the `for book in &shelf` syntax. This borrows the collection, allowing it to be used again after iteration.

#### Lines 92-100: IntoIterator for Owned Collection
Implementing `IntoIterator` for `BookShelf` (without reference) enables consuming iteration with `for book in shelf`. This moves ownership and the collection cannot be used afterward.

#### Lines 116-121: Basic For-Loop Iteration
Uses the `IntoIterator` implementation for `&BookShelf` (lines 82-90). The `&shelf` syntax triggers borrowing iteration.

#### Lines 123-128: Enumerate Adapter
The `enumerate()` adapter wraps each item with its index, returning `(usize, &Book)` tuples.

#### Lines 130-141: Chained Iterator Adapters
Demonstrates Rust's functional-style iterator chain:
- `filter()`: Keeps only books from 2021 onwards
- `map()`: Transforms books to their titles
- `collect()`: Gathers results into a `Vec`

#### Lines 143-148: Custom Iterator Usage
Uses `BookRangeIterator` to iterate only over books published between 2021-2022.

#### Lines 150-165: Iterator Methods
Demonstrates built-in iterator methods:
- `sum()`: Adds all values
- `count()`: Counts matching elements
- `any()`: Checks if any element matches
- `all()`: Checks if all elements match

#### Lines 167-176: Find and Position
- `find()`: Returns first matching element
- `position()`: Returns index of first match

#### Lines 178-187: Consuming Iterator
Clones the collection, then uses consuming `into_iter()` which moves ownership. After iteration, `shelf_clone` is no longer accessible.

---

### Output-to-Source Correlation Table

| Output Line | Source Lines | Description |
|------------|-------------|-------------|
| `BookShelf contains 5 books` | 114 | Displays collection size via `len()` method |
| Demo 1: Book list with details | 118-120 | For-loop using `IntoIterator` for `&BookShelf` (lines 82-90) |
| Demo 2: Indexed book titles | 125-127 | `iter().enumerate()` produces (index, book) pairs |
| Demo 3: Filtered book titles | 132-139 | Chain of `filter()`, `map()`, `collect()` adapters |
| Demo 4: Books in 2021-2022 | 145-147 | Custom `BookRangeIterator` (lines 67-80) filters by year |
| `Average publication year: 2020.6` | 153-155 | `map()` extracts years, `sum()` totals them |
| `Books published in 2021: 3` | 157-158 | `filter()` and `count()` combination |
| `Has book from 2022: true` | 160-161 | `any()` short-circuits on first match |
| `All books after 2000: true` | 163-164 | `all()` checks every element |
| `Found book by Jon: Rust for Rustaceans` | 169-171 | `find()` returns first match as `Option` |
| `'Rust in Action' is at position: 2` | 173-175 | `position()` returns index as `Option<usize>` |
| Demo 7: Consumed books | 184-186 | Consuming `IntoIterator` moves ownership (lines 92-100) |

---

### Key Characteristics of the Iterator Pattern in Rust

| Characteristic | Rust Implementation |
|---------------|---------------------|
| **Trait-based** | `Iterator` trait with required `next()` method and `Item` associated type |
| **Lazy evaluation** | Iterators don't execute until consumed (e.g., `collect()`, `for` loop) |
| **Zero-cost abstraction** | Compiler optimizes iterator chains to efficient loops |
| **Ownership awareness** | Three iterator types: `iter()` (borrow), `iter_mut()` (mutable borrow), `into_iter()` (consume) |
| **Composable** | Adapters like `map`, `filter`, `take`, `skip` can be chained |
| **Memory safe** | Lifetime parameters prevent dangling references |
| **Rich standard library** | Many built-in methods: `sum`, `count`, `any`, `all`, `find`, `fold`, etc. |

### Comparison with Traditional OOP Iterator

| Aspect | Traditional (Java/C++) | Rust |
|--------|----------------------|------|
| Interface | `hasNext()` / `next()` | Single `next()` returning `Option<Item>` |
| Null handling | Manual null checks | `Option` type enforces handling |
| Memory management | GC or manual | Ownership system |
| Invalidation | Runtime errors possible | Compile-time prevention |
| Adapters | Separate library needed | Built into standard library |

---

## Build Instructions

Compile and run:
```bash
rustc main_iterator.rs -o main_iterator && ./main_iterator
```

No external dependencies required. Works with Rust stable (tested with rustc 1.70+).
