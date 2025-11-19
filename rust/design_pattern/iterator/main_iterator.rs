// Iterator Design Pattern in Rust
// Demonstrates custom collection with idiomatic Iterator trait implementation

use std::slice::Iter;

// Book struct representing items in our collection
#[derive(Debug, Clone)]
struct Book {
    title: String,
    author: String,
    year: u32,
}

impl Book {
    fn new(title: &str, author: &str, year: u32) -> Self {
        Book {
            title: title.to_string(),
            author: author.to_string(),
            year,
        }
    }
}

// Custom collection: BookShelf
struct BookShelf {
    books: Vec<Book>,
}

impl BookShelf {
    fn new() -> Self {
        BookShelf { books: Vec::new() }
    }

    fn add_book(&mut self, book: Book) {
        self.books.push(book);
    }

    fn len(&self) -> usize {
        self.books.len()
    }

    // Return an iterator over borrowed books
    fn iter(&self) -> Iter<'_, Book> {
        self.books.iter()
    }

    // Custom iterator that filters by year range
    fn books_in_range(&self, start_year: u32, end_year: u32) -> BookRangeIterator<'_> {
        BookRangeIterator {
            books: &self.books,
            index: 0,
            start_year,
            end_year,
        }
    }
}

// Custom iterator for filtering books by year range
struct BookRangeIterator<'a> {
    books: &'a Vec<Book>,
    index: usize,
    start_year: u32,
    end_year: u32,
}

// Implement Iterator trait for our custom iterator
impl<'a> Iterator for BookRangeIterator<'a> {
    type Item = &'a Book;

    fn next(&mut self) -> Option<Self::Item> {
        while self.index < self.books.len() {
            let book = &self.books[self.index];
            self.index += 1;
            if book.year >= self.start_year && book.year <= self.end_year {
                return Some(book);
            }
        }
        None
    }
}

// Implement IntoIterator to enable for-loop syntax
impl<'a> IntoIterator for &'a BookShelf {
    type Item = &'a Book;
    type IntoIter = Iter<'a, Book>;

    fn into_iter(self) -> Self::IntoIter {
        self.books.iter()
    }
}

// Consuming iterator implementation
impl IntoIterator for BookShelf {
    type Item = Book;
    type IntoIter = std::vec::IntoIter<Book>;

    fn into_iter(self) -> Self::IntoIter {
        self.books.into_iter()
    }
}

fn main() {
    println!("=== Iterator Design Pattern in Rust ===\n");

    // Create and populate the bookshelf
    let mut shelf = BookShelf::new();

    shelf.add_book(Book::new("The Rust Programming Language", "Steve Klabnik", 2018));
    shelf.add_book(Book::new("Programming Rust", "Jim Blandy", 2021));
    shelf.add_book(Book::new("Rust in Action", "Tim McNamara", 2021));
    shelf.add_book(Book::new("Zero To Production", "Luca Palmieri", 2022));
    shelf.add_book(Book::new("Rust for Rustaceans", "Jon Gjengset", 2021));

    println!("BookShelf contains {} books\n", shelf.len());

    // Demonstration 1: Basic for-loop iteration (using IntoIterator)
    println!("--- Demo 1: Basic for-loop iteration ---");
    for book in &shelf {
        println!("  {} by {} ({})", book.title, book.author, book.year);
    }
    println!();

    // Demonstration 2: Using iter() method with enumerate
    println!("--- Demo 2: Using iter() with enumerate ---");
    for (index, book) in shelf.iter().enumerate() {
        println!("  [{}] {}", index, book.title);
    }
    println!();

    // Demonstration 3: Iterator adapters (map, filter, collect)
    println!("--- Demo 3: Iterator adapters ---");
    let titles: Vec<&str> = shelf
        .iter()
        .filter(|book| book.year >= 2021)
        .map(|book| book.title.as_str())
        .collect();
    println!("  Books from 2021 onwards:");
    for title in &titles {
        println!("    - {}", title);
    }
    println!();

    // Demonstration 4: Custom iterator with year range filter
    println!("--- Demo 4: Custom BookRangeIterator (2021-2022) ---");
    for book in shelf.books_in_range(2021, 2022) {
        println!("  {} ({})", book.title, book.year);
    }
    println!();

    // Demonstration 5: Iterator methods (fold, count, any)
    println!("--- Demo 5: Iterator methods ---");

    let total_years: u32 = shelf.iter().map(|book| book.year).sum();
    let avg_year = total_years as f64 / shelf.len() as f64;
    println!("  Average publication year: {:.1}", avg_year);

    let count_2021 = shelf.iter().filter(|book| book.year == 2021).count();
    println!("  Books published in 2021: {}", count_2021);

    let has_2022_book = shelf.iter().any(|book| book.year == 2022);
    println!("  Has book from 2022: {}", has_2022_book);

    let all_after_2000 = shelf.iter().all(|book| book.year > 2000);
    println!("  All books after 2000: {}", all_after_2000);
    println!();

    // Demonstration 6: find and position
    println!("--- Demo 6: find and position ---");
    if let Some(book) = shelf.iter().find(|book| book.author.contains("Jon")) {
        println!("  Found book by Jon: {}", book.title);
    }

    if let Some(pos) = shelf.iter().position(|book| book.title.contains("Action")) {
        println!("  'Rust in Action' is at position: {}", pos);
    }
    println!();

    // Demonstration 7: Consuming iterator (moves ownership)
    println!("--- Demo 7: Consuming iterator ---");
    let shelf_clone = BookShelf {
        books: shelf.books.clone(),
    };

    for book in shelf_clone {
        println!("  Consumed: {} ({})", book.title, book.year);
    }
    // shelf_clone is now moved and cannot be used

    println!("\n=== Iterator Pattern Complete ===");
}
