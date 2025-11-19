# Proxy Design Pattern in Rust

## Description

The Proxy design pattern provides a surrogate or placeholder for another object to control access to it. This implementation demonstrates a **Protection Proxy** that controls access to a document based on user roles and permissions.

### Types of Proxy Patterns:
- **Virtual Proxy**: Delays creation/initialization of expensive objects
- **Protection Proxy**: Controls access based on permissions (demonstrated here)
- **Remote Proxy**: Represents objects in different address spaces
- **Smart Proxy**: Adds additional behavior when accessing objects

## Source Code

```rust
  1  // Proxy Design Pattern - Protection Proxy Example
  2  // Demonstrates access control to sensitive documents based on user roles
  3
  4  /// Subject trait that defines the common interface for RealSubject and Proxy
  5  trait Document {
  6      fn read(&self, user: &User) -> String;
  7      fn write(&self, user: &User, content: &str) -> String;
  8      fn delete(&self, user: &User) -> String;
  9  }
 10
 11  /// User roles for access control
 12  #[derive(Debug, Clone, PartialEq)]
 13  enum Role {
 14      Admin,
 15      Editor,
 16      Viewer,
 17  }
 18
 19  /// User struct containing identity and role information
 20  #[derive(Debug, Clone)]
 21  struct User {
 22      name: String,
 23      role: Role,
 24  }
 25
 26  impl User {
 27      fn new(name: &str, role: Role) -> Self {
 28          println!("[User] Creating user '{}' with role {:?}", name, role);
 29          User {
 30              name: name.to_string(),
 31              role,
 32          }
 33      }
 34  }
 35
 36  /// RealSubject - The actual document that performs real operations
 37  struct RealDocument {
 38      title: String,
 39      content: String,
 40  }
 41
 42  impl RealDocument {
 43      fn new(title: &str, content: &str) -> Self {
 44          println!("[RealDocument] Creating document '{}'", title);
 45          RealDocument {
 46              title: title.to_string(),
 47              content: content.to_string(),
 48          }
 49      }
 50  }
 51
 52  impl Document for RealDocument {
 53      fn read(&self, user: &User) -> String {
 54          println!("[RealDocument] Reading document '{}' for user '{}'", self.title, user.name);
 55          format!("Content: {}", self.content)
 56      }
 57
 58      fn write(&self, user: &User, content: &str) -> String {
 59          println!("[RealDocument] Writing to document '{}' by user '{}'", self.title, user.name);
 60          format!("Successfully wrote: '{}'", content)
 61      }
 62
 63      fn delete(&self, user: &User) -> String {
 64          println!("[RealDocument] Deleting document '{}' by user '{}'", self.title, user.name);
 65          format!("Document '{}' deleted", self.title)
 66      }
 67  }
 68
 69  /// Proxy - Controls access to the RealDocument based on user permissions
 70  #[allow(dead_code)]
 71  struct DocumentProxy {
 72      real_document: RealDocument,
 73      access_log: Vec<String>,
 74  }
 75
 76  // ... DocumentProxy implementation omitted for brevity ...
 77
136  /// Enhanced proxy with mutable access logging
137  struct SecureDocumentProxy {
138      real_document: RealDocument,
139      access_log: std::cell::RefCell<Vec<String>>,
140  }
141
142  impl SecureDocumentProxy {
143      fn new(title: &str, content: &str) -> Self {
144          println!("\n[SecureDocumentProxy] Initializing secure proxy for document '{}'", title);
145          SecureDocumentProxy {
146              real_document: RealDocument::new(title, content),
147              access_log: std::cell::RefCell::new(Vec::new()),
148          }
149      }
150
151      fn log_access(&self, user: &User, operation: &str, granted: bool) {
152          let status = if granted { "GRANTED" } else { "DENIED" };
153          let entry = format!("{}: {} - {} [{}]", user.name, operation, status,
154              match user.role {
155                  Role::Admin => "Admin",
156                  Role::Editor => "Editor",
157                  Role::Viewer => "Viewer",
158              });
159          println!("[SecureDocumentProxy] Access log: {}", entry);
160          self.access_log.borrow_mut().push(entry);
161      }
162
163      fn print_access_log(&self) {
164          println!("\n--- Access Log Summary ---");
165          for (i, entry) in self.access_log.borrow().iter().enumerate() {
166              println!("  {}. {}", i + 1, entry);
167          }
168          println!("-------------------------");
169      }
170  }
171
172  impl Document for SecureDocumentProxy {
173      fn read(&self, user: &User) -> String {
174          println!("[SecureDocumentProxy] Checking read permission for user '{}'", user.name);
175          let granted = matches!(user.role, Role::Admin | Role::Editor | Role::Viewer);
176          self.log_access(user, "READ", granted);
177
178          if granted {
179              self.real_document.read(user)
180          } else {
181              format!("ACCESS DENIED: User '{}' cannot read this document", user.name)
182          }
183      }
184
185      fn write(&self, user: &User, content: &str) -> String {
186          println!("[SecureDocumentProxy] Checking write permission for user '{}'", user.name);
187          let granted = matches!(user.role, Role::Admin | Role::Editor);
188          self.log_access(user, "WRITE", granted);
189
190          if granted {
191              self.real_document.write(user, content)
192          } else {
193              format!("ACCESS DENIED: User '{}' ({:?}) cannot write to this document",
194                  user.name, user.role)
195          }
196      }
197
198      fn delete(&self, user: &User) -> String {
199          println!("[SecureDocumentProxy] Checking delete permission for user '{}'", user.name);
200          let granted = matches!(user.role, Role::Admin);
201          self.log_access(user, "DELETE", granted);
202
203          if granted {
204              self.real_document.delete(user)
205          } else {
206              format!("ACCESS DENIED: User '{}' ({:?}) cannot delete this document",
207                  user.name, user.role)
208          }
209      }
210  }
211
212  fn main() {
213      println!("=== Proxy Design Pattern - Protection Proxy Demo ===\n");
214
215      // Create users with different roles
216      let admin = User::new("Alice", Role::Admin);
217      let editor = User::new("Bob", Role::Editor);
218      let viewer = User::new("Charlie", Role::Viewer);
219
220      println!("\n--- Creating Secure Document Proxy ---");
221      let secure_doc = SecureDocumentProxy::new("Confidential Report", "Top secret information here.");
222
223      // Test READ operations
224      println!("\n--- Testing READ Operations ---");
225      println!("Result: {}\n", secure_doc.read(&admin));
226      println!("Result: {}\n", secure_doc.read(&editor));
227      println!("Result: {}\n", secure_doc.read(&viewer));
228
229      // Test WRITE operations
230      println!("--- Testing WRITE Operations ---");
231      println!("Result: {}\n", secure_doc.write(&admin, "Admin's update"));
232      println!("Result: {}\n", secure_doc.write(&editor, "Editor's update"));
233      println!("Result: {}\n", secure_doc.write(&viewer, "Viewer's update"));
234
235      // Test DELETE operations
236      println!("--- Testing DELETE Operations ---");
237      println!("Result: {}\n", secure_doc.delete(&viewer));
238      println!("Result: {}\n", secure_doc.delete(&editor));
239      println!("Result: {}\n", secure_doc.delete(&admin));
240
241      // Display access log
242      secure_doc.print_access_log();
243
244      println!("\n=== Proxy Pattern Demo Complete ===");
245  }
```

## Program Output

```
=== Proxy Design Pattern - Protection Proxy Demo ===

[User] Creating user 'Alice' with role Admin
[User] Creating user 'Bob' with role Editor
[User] Creating user 'Charlie' with role Viewer

--- Creating Secure Document Proxy ---

[SecureDocumentProxy] Initializing secure proxy for document 'Confidential Report'
[RealDocument] Creating document 'Confidential Report'

--- Testing READ Operations ---
[SecureDocumentProxy] Checking read permission for user 'Alice'
[SecureDocumentProxy] Access log: Alice: READ - GRANTED [Admin]
[RealDocument] Reading document 'Confidential Report' for user 'Alice'
Result: Content: Top secret information here.

[SecureDocumentProxy] Checking read permission for user 'Bob'
[SecureDocumentProxy] Access log: Bob: READ - GRANTED [Editor]
[RealDocument] Reading document 'Confidential Report' for user 'Bob'
Result: Content: Top secret information here.

[SecureDocumentProxy] Checking read permission for user 'Charlie'
[SecureDocumentProxy] Access log: Charlie: READ - GRANTED [Viewer]
[RealDocument] Reading document 'Confidential Report' for user 'Charlie'
Result: Content: Top secret information here.

--- Testing WRITE Operations ---
[SecureDocumentProxy] Checking write permission for user 'Alice'
[SecureDocumentProxy] Access log: Alice: WRITE - GRANTED [Admin]
[RealDocument] Writing to document 'Confidential Report' by user 'Alice'
Result: Successfully wrote: 'Admin's update'

[SecureDocumentProxy] Checking write permission for user 'Bob'
[SecureDocumentProxy] Access log: Bob: WRITE - GRANTED [Editor]
[RealDocument] Writing to document 'Confidential Report' by user 'Bob'
Result: Successfully wrote: 'Editor's update'

[SecureDocumentProxy] Checking write permission for user 'Charlie'
[SecureDocumentProxy] Access log: Charlie: WRITE - DENIED [Viewer]
Result: ACCESS DENIED: User 'Charlie' (Viewer) cannot write to this document

--- Testing DELETE Operations ---
[SecureDocumentProxy] Checking delete permission for user 'Charlie'
[SecureDocumentProxy] Access log: Charlie: DELETE - DENIED [Viewer]
Result: ACCESS DENIED: User 'Charlie' (Viewer) cannot delete this document

[SecureDocumentProxy] Checking delete permission for user 'Bob'
[SecureDocumentProxy] Access log: Bob: DELETE - DENIED [Editor]
Result: ACCESS DENIED: User 'Bob' (Editor) cannot delete this document

[SecureDocumentProxy] Checking delete permission for user 'Alice'
[SecureDocumentProxy] Access log: Alice: DELETE - GRANTED [Admin]
[RealDocument] Deleting document 'Confidential Report' by user 'Alice'
Result: Document 'Confidential Report' deleted


--- Access Log Summary ---
  1. Alice: READ - GRANTED [Admin]
  2. Bob: READ - GRANTED [Editor]
  3. Charlie: READ - GRANTED [Viewer]
  4. Alice: WRITE - GRANTED [Admin]
  5. Bob: WRITE - GRANTED [Editor]
  6. Charlie: WRITE - DENIED [Viewer]
  7. Charlie: DELETE - DENIED [Viewer]
  8. Bob: DELETE - DENIED [Editor]
  9. Alice: DELETE - GRANTED [Admin]
-------------------------

=== Proxy Pattern Demo Complete ===
```

## Code Annotations

### Key Sections Explained

#### Lines 5-9: Subject Trait (Interface)
The `Document` trait defines the common interface that both the real subject and proxy must implement. This ensures clients can work with either the proxy or real object interchangeably.

#### Lines 11-17: Role Enumeration
Defines three access levels (`Admin`, `Editor`, `Viewer`) used by the protection proxy to determine permissions. The `#[derive]` attributes enable debugging, cloning, and comparison.

#### Lines 37-67: RealDocument (RealSubject)
The actual object that performs real document operations. It implements the `Document` trait and contains the business logic for reading, writing, and deleting documents.

#### Lines 137-140: SecureDocumentProxy Structure
The proxy uses `RefCell<Vec<String>>` for the access log to enable interior mutability. This allows logging even when the proxy is accessed through a shared reference (`&self`).

#### Lines 151-161: Access Logging
The `log_access` method records all access attempts with user, operation, result, and role information. Uses `borrow_mut()` to get mutable access to the RefCell.

#### Lines 172-210: Proxy's Document Implementation
Each method follows the same pattern:
1. Log the permission check (line 174, 186, 199)
2. Determine if access is granted using `matches!` macro
3. Log the access attempt (line 176, 188, 201)
4. Either delegate to RealDocument or return access denied message

#### Lines 216-218: User Creation
Creates three users with different roles to demonstrate the access control behavior.

### Output to Source Code Correlation

| Output Line | Source Lines | Description |
|-------------|--------------|-------------|
| `[User] Creating user 'Alice' with role Admin` | 216, 28 | User::new() called for admin user |
| `[User] Creating user 'Bob' with role Editor` | 217, 28 | User::new() called for editor user |
| `[User] Creating user 'Charlie' with role Viewer` | 218, 28 | User::new() called for viewer user |
| `[SecureDocumentProxy] Initializing secure proxy...` | 221, 144 | SecureDocumentProxy::new() called |
| `[RealDocument] Creating document...` | 146, 44 | RealDocument created inside proxy |
| `[SecureDocumentProxy] Checking read permission...` | 225-227, 174 | Proxy checks permission before delegating |
| `[SecureDocumentProxy] Access log: ... READ - GRANTED` | 225-227, 159 | Permission granted, logged to access log |
| `[RealDocument] Reading document...` | 225-227, 179, 54 | Proxy delegates to RealDocument |
| `[SecureDocumentProxy] Checking write permission...` | 231-233, 186 | Write permission check in proxy |
| `ACCESS DENIED: User 'Charlie'...cannot write` | 233, 193-194 | Viewer denied write access |
| `[SecureDocumentProxy] Checking delete permission...` | 237-239, 199 | Delete permission check in proxy |
| `ACCESS DENIED: User 'Bob'...cannot delete` | 238, 206-207 | Editor denied delete access |
| `--- Access Log Summary ---` | 242, 164 | print_access_log() displays all entries |

### Permission Matrix

| Role | READ | WRITE | DELETE |
|------|------|-------|--------|
| Admin | GRANTED | GRANTED | GRANTED |
| Editor | GRANTED | GRANTED | DENIED |
| Viewer | GRANTED | DENIED | DENIED |

## Key Characteristics of Proxy Pattern in Rust

### 1. Trait-Based Polymorphism
Rust uses traits instead of interfaces. Both `RealDocument` and `SecureDocumentProxy` implement the `Document` trait, allowing them to be used interchangeably.

### 2. Interior Mutability with RefCell
The proxy uses `RefCell<Vec<String>>` to maintain an access log while still implementing the trait methods with `&self`. This is a common Rust pattern when you need mutability behind an immutable reference.

### 3. Pattern Matching for Permission Checks
The `matches!` macro provides concise, readable permission checking:
```rust
let granted = matches!(user.role, Role::Admin | Role::Editor);
```

### 4. Ownership and Composition
The proxy owns the `RealDocument` (composition over inheritance), which is the idiomatic Rust approach for the proxy pattern.

### 5. No Runtime Overhead
Rust's zero-cost abstractions mean the proxy pattern adds minimal runtime overhead compared to direct access.

### 6. Compile-Time Safety
The type system ensures that:
- All trait methods are implemented correctly
- Permission checks cannot be bypassed
- Access logging is always performed

## Use Cases for Protection Proxy

1. **Access Control Systems**: Restrict operations based on user roles
2. **Audit Logging**: Track all access attempts for compliance
3. **Rate Limiting**: Control frequency of operations
4. **Lazy Initialization**: Defer expensive object creation
5. **Caching**: Cache results of expensive operations

## Compilation

This code can be compiled with standard rustc:

```bash
rustc main_proxy.rs -o main_proxy.exe && ./main_proxy.exe
```

No external dependencies or specific Rust version required (tested with Rust stable).
