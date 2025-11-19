// Proxy Design Pattern - Protection Proxy Example
// Demonstrates access control to sensitive documents based on user roles

/// Subject trait that defines the common interface for RealSubject and Proxy
trait Document {
    fn read(&self, user: &User) -> String;
    fn write(&self, user: &User, content: &str) -> String;
    fn delete(&self, user: &User) -> String;
}

/// User roles for access control
#[derive(Debug, Clone, PartialEq)]
enum Role {
    Admin,
    Editor,
    Viewer,
}

/// User struct containing identity and role information
#[derive(Debug, Clone)]
struct User {
    name: String,
    role: Role,
}

impl User {
    fn new(name: &str, role: Role) -> Self {
        println!("[User] Creating user '{}' with role {:?}", name, role);
        User {
            name: name.to_string(),
            role,
        }
    }
}

/// RealSubject - The actual document that performs real operations
struct RealDocument {
    title: String,
    content: String,
}

impl RealDocument {
    fn new(title: &str, content: &str) -> Self {
        println!("[RealDocument] Creating document '{}'", title);
        RealDocument {
            title: title.to_string(),
            content: content.to_string(),
        }
    }
}

impl Document for RealDocument {
    fn read(&self, user: &User) -> String {
        println!("[RealDocument] Reading document '{}' for user '{}'", self.title, user.name);
        format!("Content: {}", self.content)
    }

    fn write(&self, user: &User, content: &str) -> String {
        println!("[RealDocument] Writing to document '{}' by user '{}'", self.title, user.name);
        format!("Successfully wrote: '{}'", content)
    }

    fn delete(&self, user: &User) -> String {
        println!("[RealDocument] Deleting document '{}' by user '{}'", self.title, user.name);
        format!("Document '{}' deleted", self.title)
    }
}

/// Proxy - Controls access to the RealDocument based on user permissions
#[allow(dead_code)]
struct DocumentProxy {
    real_document: RealDocument,
    access_log: Vec<String>,
}

#[allow(dead_code)]
impl DocumentProxy {
    fn new(title: &str, content: &str) -> Self {
        println!("[DocumentProxy] Initializing proxy for document '{}'", title);
        DocumentProxy {
            real_document: RealDocument::new(title, content),
            access_log: Vec::new(),
        }
    }

    fn log_access(&mut self, user: &User, operation: &str, granted: bool) {
        let status = if granted { "GRANTED" } else { "DENIED" };
        let entry = format!("{}: {} - {} [{}]", user.name, operation, status,
            match user.role {
                Role::Admin => "Admin",
                Role::Editor => "Editor",
                Role::Viewer => "Viewer",
            });
        println!("[DocumentProxy] Access log: {}", entry);
        self.access_log.push(entry);
    }

    fn check_read_permission(&self, user: &User) -> bool {
        // All roles can read
        matches!(user.role, Role::Admin | Role::Editor | Role::Viewer)
    }

    fn check_write_permission(&self, user: &User) -> bool {
        // Only Admin and Editor can write
        matches!(user.role, Role::Admin | Role::Editor)
    }

    fn check_delete_permission(&self, user: &User) -> bool {
        // Only Admin can delete
        matches!(user.role, Role::Admin)
    }

    fn get_access_log(&self) -> &Vec<String> {
        &self.access_log
    }
}

impl Document for DocumentProxy {
    fn read(&self, user: &User) -> String {
        println!("[DocumentProxy] Checking read permission for user '{}'", user.name);
        if self.check_read_permission(user) {
            // Note: We need mutable access for logging, but trait requires &self
            // In a real implementation, you'd use RefCell or similar
            self.real_document.read(user)
        } else {
            format!("ACCESS DENIED: User '{}' cannot read this document", user.name)
        }
    }

    fn write(&self, user: &User, content: &str) -> String {
        println!("[DocumentProxy] Checking write permission for user '{}'", user.name);
        if self.check_write_permission(user) {
            self.real_document.write(user, content)
        } else {
            format!("ACCESS DENIED: User '{}' ({:?}) cannot write to this document",
                user.name, user.role)
        }
    }

    fn delete(&self, user: &User) -> String {
        println!("[DocumentProxy] Checking delete permission for user '{}'", user.name);
        if self.check_delete_permission(user) {
            self.real_document.delete(user)
        } else {
            format!("ACCESS DENIED: User '{}' ({:?}) cannot delete this document",
                user.name, user.role)
        }
    }
}

/// Enhanced proxy with mutable access logging
struct SecureDocumentProxy {
    real_document: RealDocument,
    access_log: std::cell::RefCell<Vec<String>>,
}

impl SecureDocumentProxy {
    fn new(title: &str, content: &str) -> Self {
        println!("\n[SecureDocumentProxy] Initializing secure proxy for document '{}'", title);
        SecureDocumentProxy {
            real_document: RealDocument::new(title, content),
            access_log: std::cell::RefCell::new(Vec::new()),
        }
    }

    fn log_access(&self, user: &User, operation: &str, granted: bool) {
        let status = if granted { "GRANTED" } else { "DENIED" };
        let entry = format!("{}: {} - {} [{}]", user.name, operation, status,
            match user.role {
                Role::Admin => "Admin",
                Role::Editor => "Editor",
                Role::Viewer => "Viewer",
            });
        println!("[SecureDocumentProxy] Access log: {}", entry);
        self.access_log.borrow_mut().push(entry);
    }

    fn print_access_log(&self) {
        println!("\n--- Access Log Summary ---");
        for (i, entry) in self.access_log.borrow().iter().enumerate() {
            println!("  {}. {}", i + 1, entry);
        }
        println!("-------------------------");
    }
}

impl Document for SecureDocumentProxy {
    fn read(&self, user: &User) -> String {
        println!("[SecureDocumentProxy] Checking read permission for user '{}'", user.name);
        let granted = matches!(user.role, Role::Admin | Role::Editor | Role::Viewer);
        self.log_access(user, "READ", granted);

        if granted {
            self.real_document.read(user)
        } else {
            format!("ACCESS DENIED: User '{}' cannot read this document", user.name)
        }
    }

    fn write(&self, user: &User, content: &str) -> String {
        println!("[SecureDocumentProxy] Checking write permission for user '{}'", user.name);
        let granted = matches!(user.role, Role::Admin | Role::Editor);
        self.log_access(user, "WRITE", granted);

        if granted {
            self.real_document.write(user, content)
        } else {
            format!("ACCESS DENIED: User '{}' ({:?}) cannot write to this document",
                user.name, user.role)
        }
    }

    fn delete(&self, user: &User) -> String {
        println!("[SecureDocumentProxy] Checking delete permission for user '{}'", user.name);
        let granted = matches!(user.role, Role::Admin);
        self.log_access(user, "DELETE", granted);

        if granted {
            self.real_document.delete(user)
        } else {
            format!("ACCESS DENIED: User '{}' ({:?}) cannot delete this document",
                user.name, user.role)
        }
    }
}

fn main() {
    println!("=== Proxy Design Pattern - Protection Proxy Demo ===\n");

    // Create users with different roles
    let admin = User::new("Alice", Role::Admin);
    let editor = User::new("Bob", Role::Editor);
    let viewer = User::new("Charlie", Role::Viewer);

    println!("\n--- Creating Secure Document Proxy ---");
    let secure_doc = SecureDocumentProxy::new("Confidential Report", "Top secret information here.");

    // Test READ operations
    println!("\n--- Testing READ Operations ---");
    println!("Result: {}\n", secure_doc.read(&admin));
    println!("Result: {}\n", secure_doc.read(&editor));
    println!("Result: {}\n", secure_doc.read(&viewer));

    // Test WRITE operations
    println!("--- Testing WRITE Operations ---");
    println!("Result: {}\n", secure_doc.write(&admin, "Admin's update"));
    println!("Result: {}\n", secure_doc.write(&editor, "Editor's update"));
    println!("Result: {}\n", secure_doc.write(&viewer, "Viewer's update"));

    // Test DELETE operations
    println!("--- Testing DELETE Operations ---");
    println!("Result: {}\n", secure_doc.delete(&viewer));
    println!("Result: {}\n", secure_doc.delete(&editor));
    println!("Result: {}\n", secure_doc.delete(&admin));

    // Display access log
    secure_doc.print_access_log();

    println!("\n=== Proxy Pattern Demo Complete ===");
}
