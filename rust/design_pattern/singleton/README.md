# Singleton Pattern in Rust

The Singleton pattern ensures a class has only one instance and provides a global point of access to it. In Rust, this is achieved using `OnceLock` for thread-safe lazy initialization.

**Note**: This example requires Rust 1.70+ for `std::sync::OnceLock`.

## Source Code

```rust
 1  //! Singleton Pattern in Rust
 2  //!
 3  //! The Singleton pattern ensures a class has only one instance and provides
 4  //! a global point of access to it. In Rust, this is achieved using OnceLock
 5  //! for thread-safe lazy initialization.
 6
 7  use std::sync::{OnceLock, Mutex};
 8
 9  // Global singleton instance using OnceLock for thread-safe lazy initialization
10  static DATABASE_CONNECTION: OnceLock<DatabaseConnection> = OnceLock::new();
11
12  /// Represents a database connection singleton
13  struct DatabaseConnection {
14      connection_string: String,
15      query_count: Mutex<u32>,
16  }
17
18  impl DatabaseConnection {
19      /// Creates a new DatabaseConnection instance
20      fn new(connection_string: &str) -> Self {
21          println!("  [DatabaseConnection] Creating new instance...");
22          println!("  [DatabaseConnection] Connecting to: {}", connection_string);
23          DatabaseConnection {
24              connection_string: connection_string.to_string(),
25              query_count: Mutex::new(0),
26          }
27      }
28
29      /// Gets or creates the singleton instance
30      fn get_instance() -> &'static DatabaseConnection {
31          DATABASE_CONNECTION.get_or_init(|| {
32              DatabaseConnection::new("postgres://localhost:5432/mydb")
33          })
34      }
35
36      /// Executes a query and increments the query counter
37      fn execute_query(&self, query: &str) -> String {
38          let mut count = self.query_count.lock().unwrap();
39          *count += 1;
40          let current_count = *count;
41          drop(count); // Release the lock early
42
43          println!("  [Query #{}] Executing: {}", current_count, query);
44          format!("Result for query #{}: {}", current_count, query)
45      }
46
47      /// Returns the total number of queries executed
48      fn get_query_count(&self) -> u32 {
49          *self.query_count.lock().unwrap()
50      }
51
52      /// Returns the connection string
53      fn get_connection_string(&self) -> &str {
54          &self.connection_string
55      }
56  }
57
58  fn main() {
59      println!("=== Singleton Pattern Demo ===\n");
60
61      // Demonstrate singleton behavior
62      println!("1. First access to singleton:");
63      let db1 = DatabaseConnection::get_instance();
64      println!("   Connection: {}\n", db1.get_connection_string());
65
66      // Second access returns the same instance
67      println!("2. Second access to singleton:");
68      let db2 = DatabaseConnection::get_instance();
69      println!("   Connection: {}\n", db2.get_connection_string());
70
71      // Verify both references point to the same instance
72      println!("3. Verifying singleton identity:");
73      let ptr1 = db1 as *const DatabaseConnection;
74      let ptr2 = db2 as *const DatabaseConnection;
75      println!("   db1 address: {:p}", ptr1);
76      println!("   db2 address: {:p}", ptr2);
77      println!("   Same instance: {}\n", ptr1 == ptr2);
78
79      // Execute queries through the singleton
80      println!("4. Executing queries through singleton:");
81      let result1 = db1.execute_query("SELECT * FROM users");
82      println!("   {}\n", result1);
83
84      let result2 = db2.execute_query("SELECT * FROM orders");
85      println!("   {}\n", result2);
86
87      // Show shared state
88      println!("5. Shared state verification:");
89      println!("   Total queries executed: {}\n", db1.get_query_count());
90
91      // Thread safety demonstration
92      println!("6. Thread safety demonstration:");
93      use std::thread;
94
95      let handles: Vec<_> = (0..3).map(|i| {
96          thread::spawn(move || {
97              let db = DatabaseConnection::get_instance();
98              let query = format!("SELECT * FROM table_{}", i);
99              db.execute_query(&query);
100         })
101     }).collect();
102
103     for handle in handles {
104         handle.join().unwrap();
105     }
106
107     println!("\n   Final query count: {}", DatabaseConnection::get_instance().get_query_count());
108
109     println!("\n=== Demo Complete ===");
110 }
```

## Program Output

```
=== Singleton Pattern Demo ===

1. First access to singleton:
  [DatabaseConnection] Creating new instance...
  [DatabaseConnection] Connecting to: postgres://localhost:5432/mydb
   Connection: postgres://localhost:5432/mydb

2. Second access to singleton:
   Connection: postgres://localhost:5432/mydb

3. Verifying singleton identity:
   db1 address: 0x55fec3d098a0
   db2 address: 0x55fec3d098a0
   Same instance: true

4. Executing queries through singleton:
  [Query #1] Executing: SELECT * FROM users
   Result for query #1: SELECT * FROM users

  [Query #2] Executing: SELECT * FROM orders
   Result for query #2: SELECT * FROM orders

5. Shared state verification:
   Total queries executed: 2

6. Thread safety demonstration:
  [Query #3] Executing: SELECT * FROM table_0
  [Query #4] Executing: SELECT * FROM table_2
  [Query #5] Executing: SELECT * FROM table_1

   Final query count: 5

=== Demo Complete ===
```

## Code Annotations

### Singleton Infrastructure (Lines 7-16)

- **Line 7**: Import `OnceLock` for thread-safe one-time initialization and `Mutex` for interior mutability
- **Line 10**: Declare global static `DATABASE_CONNECTION` using `OnceLock` - this is the singleton storage
- **Lines 13-16**: Define the `DatabaseConnection` struct with mutable state protected by `Mutex`

### Singleton Implementation (Lines 18-56)

- **Lines 20-27**: Private constructor that prints creation messages - note this only prints once in the output (after "1. First access")
- **Lines 30-34**: The `get_instance()` method is the key singleton accessor - `get_or_init()` ensures the initialization closure only runs once
- **Lines 37-45**: `execute_query()` demonstrates thread-safe mutable state using `Mutex`
- **Lines 48-50**: `get_query_count()` shows how multiple references share the same state

### Output Correlation

| Output Section | Source Lines | Explanation |
|----------------|--------------|-------------|
| "Creating new instance..." | 21-22 | Only appears on first access (line 63), proving singleton is created once |
| "2. Second access..." shows no creation | 68 | Second call to `get_instance()` returns existing instance |
| Same memory address for db1 and db2 | 73-77 | Pointer comparison proves both variables reference the identical instance |
| Query count increments across both references | 81-89 | db1 and db2 share state - queries through either increment the same counter |
| Thread safety demo shows queries 3-5 | 95-101 | Three threads safely access and modify the singleton concurrently |
| Final count is 5 | 107 | All 5 queries (2 manual + 3 threaded) are tracked in the shared state |

### Key Rust Singleton Characteristics

1. **Thread Safety**: `OnceLock` guarantees the initialization runs exactly once, even with concurrent access
2. **Lazy Initialization**: The singleton is only created on first access (line 63)
3. **Interior Mutability**: `Mutex<u32>` allows safe mutation of query_count through shared references
4. **Static Lifetime**: The singleton lives for the entire program duration (`&'static` return type)

## How to Run

```bash
rustc main_singleton.rs -o main_singleton
./main_singleton
```

Or with Cargo in a project:
```bash
cargo run
```
