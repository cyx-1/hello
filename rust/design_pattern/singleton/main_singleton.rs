//! Singleton Pattern in Rust
//!
//! The Singleton pattern ensures a class has only one instance and provides
//! a global point of access to it. In Rust, this is achieved using OnceLock
//! for thread-safe lazy initialization.

use std::sync::{OnceLock, Mutex};

// Global singleton instance using OnceLock for thread-safe lazy initialization
static DATABASE_CONNECTION: OnceLock<DatabaseConnection> = OnceLock::new();

/// Represents a database connection singleton
struct DatabaseConnection {
    connection_string: String,
    query_count: Mutex<u32>,
}

impl DatabaseConnection {
    /// Creates a new DatabaseConnection instance
    fn new(connection_string: &str) -> Self {
        println!("  [DatabaseConnection] Creating new instance...");
        println!("  [DatabaseConnection] Connecting to: {}", connection_string);
        DatabaseConnection {
            connection_string: connection_string.to_string(),
            query_count: Mutex::new(0),
        }
    }

    /// Gets or creates the singleton instance
    fn get_instance() -> &'static DatabaseConnection {
        DATABASE_CONNECTION.get_or_init(|| {
            DatabaseConnection::new("postgres://localhost:5432/mydb")
        })
    }

    /// Executes a query and increments the query counter
    fn execute_query(&self, query: &str) -> String {
        let mut count = self.query_count.lock().unwrap();
        *count += 1;
        let current_count = *count;
        drop(count); // Release the lock early

        println!("  [Query #{}] Executing: {}", current_count, query);
        format!("Result for query #{}: {}", current_count, query)
    }

    /// Returns the total number of queries executed
    fn get_query_count(&self) -> u32 {
        *self.query_count.lock().unwrap()
    }

    /// Returns the connection string
    fn get_connection_string(&self) -> &str {
        &self.connection_string
    }
}

fn main() {
    println!("=== Singleton Pattern Demo ===\n");

    // Demonstrate singleton behavior
    println!("1. First access to singleton:");
    let db1 = DatabaseConnection::get_instance();
    println!("   Connection: {}\n", db1.get_connection_string());

    // Second access returns the same instance
    println!("2. Second access to singleton:");
    let db2 = DatabaseConnection::get_instance();
    println!("   Connection: {}\n", db2.get_connection_string());

    // Verify both references point to the same instance
    println!("3. Verifying singleton identity:");
    let ptr1 = db1 as *const DatabaseConnection;
    let ptr2 = db2 as *const DatabaseConnection;
    println!("   db1 address: {:p}", ptr1);
    println!("   db2 address: {:p}", ptr2);
    println!("   Same instance: {}\n", ptr1 == ptr2);

    // Execute queries through the singleton
    println!("4. Executing queries through singleton:");
    let result1 = db1.execute_query("SELECT * FROM users");
    println!("   {}\n", result1);

    let result2 = db2.execute_query("SELECT * FROM orders");
    println!("   {}\n", result2);

    // Show shared state
    println!("5. Shared state verification:");
    println!("   Total queries executed: {}\n", db1.get_query_count());

    // Thread safety demonstration
    println!("6. Thread safety demonstration:");
    use std::thread;

    let handles: Vec<_> = (0..3).map(|i| {
        thread::spawn(move || {
            let db = DatabaseConnection::get_instance();
            let query = format!("SELECT * FROM table_{}", i);
            db.execute_query(&query);
        })
    }).collect();

    for handle in handles {
        handle.join().unwrap();
    }

    println!("\n   Final query count: {}", DatabaseConnection::get_instance().get_query_count());

    println!("\n=== Demo Complete ===");
}
