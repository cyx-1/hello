# Composite Design Pattern in Rust

## Description

The **Composite Design Pattern** is a structural pattern that allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects (leaves) and compositions of objects (composites) uniformly through a common interface.

This implementation demonstrates a file system hierarchy where:
- **Component**: `FileSystemComponent` trait defines the common interface
- **Leaf**: `File` struct represents individual files (no children)
- **Composite**: `Directory` struct can contain both files and other directories

## Source Code

```rust
  1  // Composite Design Pattern in Rust
  2  // Demonstrates a file system hierarchy with files (leaves) and directories (composites)
  3
  4  use std::cell::RefCell;
  5  use std::rc::Rc;
  6
  7  // Component trait - defines the interface for all objects in the composition
  8  trait FileSystemComponent {
  9      fn get_name(&self) -> &str;
 10      fn get_size(&self) -> u64;
 11      fn display(&self, indent: usize);
 12      fn is_composite(&self) -> bool {
 13          false
 14      }
 15  }
 16
 17  // Leaf - represents individual files that cannot contain other components
 18  struct File {
 19      name: String,
 20      size: u64,
 21  }
 22
 23  impl File {
 24      fn new(name: &str, size: u64) -> Self {
 25          println!("  [Created File] '{}' ({} bytes)", name, size);
 26          File {
 27              name: name.to_string(),
 28              size,
 29          }
 30      }
 31  }
 32
 33  impl FileSystemComponent for File {
 34      fn get_name(&self) -> &str {
 35          &self.name
 36      }
 37
 38      fn get_size(&self) -> u64 {
 39          self.size
 40      }
 41
 42      fn display(&self, indent: usize) {
 43          let prefix = "  ".repeat(indent);
 44          println!("{}|- File: {} ({} bytes)", prefix, self.name, self.size);
 45      }
 46  }
 47
 48  // Composite - represents directories that can contain other components
 49  struct Directory {
 50      name: String,
 51      children: RefCell<Vec<Rc<dyn FileSystemComponent>>>,
 52  }
 53
 54  impl Directory {
 55      fn new(name: &str) -> Self {
 56          println!("  [Created Directory] '{}'", name);
 57          Directory {
 58              name: name.to_string(),
 59              children: RefCell::new(Vec::new()),
 60          }
 61      }
 62
 63      fn add(&self, component: Rc<dyn FileSystemComponent>) {
 64          println!("  [Added] '{}' to '{}'", component.get_name(), self.name);
 65          self.children.borrow_mut().push(component);
 66      }
 67
 68      fn remove(&self, name: &str) {
 69          self.children.borrow_mut().retain(|c| c.get_name() != name);
 70          println!("  [Removed] '{}' from '{}'", name, self.name);
 71      }
 72  }
 73
 74  impl FileSystemComponent for Directory {
 75      fn get_name(&self) -> &str {
 76          &self.name
 77      }
 78
 79      fn get_size(&self) -> u64 {
 80          // Recursively calculate total size of all children
 81          self.children
 82              .borrow()
 83              .iter()
 84              .map(|child| child.get_size())
 85              .sum()
 86      }
 87
 88      fn display(&self, indent: usize) {
 89          let prefix = "  ".repeat(indent);
 90          println!("{}|+ Directory: {} (total: {} bytes)", prefix, self.name, self.get_size());
 91
 92          // Recursively display all children
 93          for child in self.children.borrow().iter() {
 94              child.display(indent + 1);
 95          }
 96      }
 97
 98      fn is_composite(&self) -> bool {
 99          true
100      }
101  }
102
103  fn main() {
104      println!("=== Composite Design Pattern Demo ===\n");
105
106      // Step 1: Create the root directory
107      println!("Step 1: Creating root directory structure");
108      let root = Rc::new(Directory::new("root"));
109
110      // Step 2: Create files for root directory
111      println!("\nStep 2: Creating files for root");
112      let readme = Rc::new(File::new("README.md", 1024));
113      let config = Rc::new(File::new("config.json", 512));
114
115      // Step 3: Add files to root
116      println!("\nStep 3: Adding files to root");
117      root.add(readme);
118      root.add(config);
119
120      // Step 4: Create subdirectories
121      println!("\nStep 4: Creating subdirectories");
122      let src_dir = Rc::new(Directory::new("src"));
123      let tests_dir = Rc::new(Directory::new("tests"));
124
125      // Step 5: Create files for src directory
126      println!("\nStep 5: Creating files for src directory");
127      let main_file = Rc::new(File::new("main.rs", 2048));
128      let lib_file = Rc::new(File::new("lib.rs", 4096));
129      let utils_file = Rc::new(File::new("utils.rs", 1536));
130
131      // Step 6: Add files to src directory
132      println!("\nStep 6: Adding files to src directory");
133      src_dir.add(main_file);
134      src_dir.add(lib_file);
135      src_dir.add(utils_file);
136
137      // Step 7: Create nested directory inside src
138      println!("\nStep 7: Creating nested directory (modules)");
139      let modules_dir = Rc::new(Directory::new("modules"));
140      let auth_file = Rc::new(File::new("auth.rs", 3072));
141      let db_file = Rc::new(File::new("database.rs", 2560));
142
143      println!("\nStep 8: Adding files to modules directory");
144      modules_dir.add(auth_file);
145      modules_dir.add(db_file);
146
147      // Step 9: Add modules directory to src
148      println!("\nStep 9: Adding modules to src directory");
149      src_dir.add(modules_dir);
150
151      // Step 10: Create test files
152      println!("\nStep 10: Creating test files");
153      let test_main = Rc::new(File::new("test_main.rs", 1024));
154      let test_utils = Rc::new(File::new("test_utils.rs", 768));
155
156      // Step 11: Add test files to tests directory
157      println!("\nStep 11: Adding test files to tests directory");
158      tests_dir.add(test_main);
159      tests_dir.add(test_utils);
160
161      // Step 12: Add subdirectories to root
162      println!("\nStep 12: Adding subdirectories to root");
163      root.add(src_dir);
164      root.add(tests_dir);
165
166      // Step 13: Display the complete tree structure
167      println!("\n=== Complete File System Tree ===\n");
168      root.display(0);
169
170      // Step 14: Demonstrate uniform treatment - get sizes
171      println!("\n=== Size Calculations (Uniform Treatment) ===\n");
172      println!("Total size of root: {} bytes", root.get_size());
173
174      // Step 15: Create a standalone file to show leaf behavior
175      println!("\n=== Demonstrating Leaf vs Composite ===\n");
176      let standalone = Rc::new(File::new("standalone.txt", 256));
177      println!("Standalone file size: {} bytes", standalone.get_size());
178      println!("Is standalone a composite? {}", standalone.is_composite());
179      println!("Is root a composite? {}", root.is_composite());
180
181      // Step 16: Demonstrate remove operation
182      println!("\n=== Demonstrating Remove Operation ===\n");
183      let temp_dir = Rc::new(Directory::new("temp"));
184      let temp_file = Rc::new(File::new("temp.txt", 100));
185      temp_dir.add(temp_file);
186      println!("Temp directory size before removal: {} bytes", temp_dir.get_size());
187      temp_dir.remove("temp.txt");
188      println!("Temp directory size after removal: {} bytes", temp_dir.get_size());
189
190      println!("\n=== End of Composite Pattern Demo ===");
191  }
```

## Program Output

```
=== Composite Design Pattern Demo ===

Step 1: Creating root directory structure
  [Created Directory] 'root'

Step 2: Creating files for root
  [Created File] 'README.md' (1024 bytes)
  [Created File] 'config.json' (512 bytes)

Step 3: Adding files to root
  [Added] 'README.md' to 'root'
  [Added] 'config.json' to 'root'

Step 4: Creating subdirectories
  [Created Directory] 'src'
  [Created Directory] 'tests'

Step 5: Creating files for src directory
  [Created File] 'main.rs' (2048 bytes)
  [Created File] 'lib.rs' (4096 bytes)
  [Created File] 'utils.rs' (1536 bytes)

Step 6: Adding files to src directory
  [Added] 'main.rs' to 'src'
  [Added] 'lib.rs' to 'src'
  [Added] 'utils.rs' to 'src'

Step 7: Creating nested directory (modules)
  [Created Directory] 'modules'
  [Created File] 'auth.rs' (3072 bytes)
  [Created File] 'database.rs' (2560 bytes)

Step 8: Adding files to modules directory
  [Added] 'auth.rs' to 'modules'
  [Added] 'database.rs' to 'modules'

Step 9: Adding modules to src directory
  [Added] 'modules' to 'src'

Step 10: Creating test files
  [Created File] 'test_main.rs' (1024 bytes)
  [Created File] 'test_utils.rs' (768 bytes)

Step 11: Adding test files to tests directory
  [Added] 'test_main.rs' to 'tests'
  [Added] 'test_utils.rs' to 'tests'

Step 12: Adding subdirectories to root
  [Added] 'src' to 'root'
  [Added] 'tests' to 'root'

=== Complete File System Tree ===

|+ Directory: root (total: 16640 bytes)
  |- File: README.md (1024 bytes)
  |- File: config.json (512 bytes)
  |+ Directory: src (total: 13312 bytes)
    |- File: main.rs (2048 bytes)
    |- File: lib.rs (4096 bytes)
    |- File: utils.rs (1536 bytes)
    |+ Directory: modules (total: 5632 bytes)
      |- File: auth.rs (3072 bytes)
      |- File: database.rs (2560 bytes)
  |+ Directory: tests (total: 1792 bytes)
    |- File: test_main.rs (1024 bytes)
    |- File: test_utils.rs (768 bytes)

=== Size Calculations (Uniform Treatment) ===

Total size of root: 16640 bytes

=== Demonstrating Leaf vs Composite ===

  [Created File] 'standalone.txt' (256 bytes)
Standalone file size: 256 bytes
Is standalone a composite? false
Is root a composite? true

=== Demonstrating Remove Operation ===

  [Created Directory] 'temp'
  [Created File] 'temp.txt' (100 bytes)
  [Added] 'temp.txt' to 'temp'
Temp directory size before removal: 100 bytes
  [Removed] 'temp.txt' from 'temp'
Temp directory size after removal: 0 bytes

=== End of Composite Pattern Demo ===
```

## Code Annotations

### Key Sections Explained

#### Lines 4-5: Smart Pointer Imports
```rust
use std::cell::RefCell;
use std::rc::Rc;
```
- `Rc` (Reference Counted) enables shared ownership of components
- `RefCell` provides interior mutability for the children vector, allowing modification through shared references

#### Lines 8-15: Component Trait
```rust
trait FileSystemComponent {
    fn get_name(&self) -> &str;
    fn get_size(&self) -> u64;
    fn display(&self, indent: usize);
    fn is_composite(&self) -> bool { false }
}
```
- Defines the common interface for both leaves and composites
- Default implementation for `is_composite()` returns false (suitable for leaves)
- This trait enables uniform treatment of all components

#### Lines 18-46: Leaf Implementation (File)
- The `File` struct stores only name and size
- `get_size()` returns the file's own size directly (line 39)
- `display()` prints only itself with proper indentation (lines 42-45)

#### Lines 49-101: Composite Implementation (Directory)
- Stores children as `Vec<Rc<dyn FileSystemComponent>>` (line 51)
- `add()` and `remove()` methods for child management (lines 63-71)
- `get_size()` recursively sums all children's sizes (lines 79-86)
- `display()` recursively traverses and displays all children (lines 88-96)
- Overrides `is_composite()` to return true (lines 98-100)

#### Lines 79-86: Recursive Size Calculation
```rust
self.children
    .borrow()
    .iter()
    .map(|child| child.get_size())
    .sum()
```
- Demonstrates the power of the Composite pattern
- Same method call works uniformly on files (returns size) and directories (recurses)

### Output to Source Line Correlation

| Output | Source Lines | Description |
|--------|--------------|-------------|
| `[Created Directory] 'root'` | 56, 108 | Directory::new prints creation message |
| `[Created File] 'README.md' (1024 bytes)` | 25, 112 | File::new prints creation message |
| `[Added] 'README.md' to 'root'` | 64, 117 | Directory::add logs the addition |
| Tree output `\|+ Directory: root (total: 16640 bytes)` | 90, 168 | Directory::display with recursive size |
| Tree output `\|- File: README.md (1024 bytes)` | 44, via 94 | File::display called during tree traversal |
| `Total size of root: 16640 bytes` | 172, 79-86 | Recursive get_size calculation |
| `Is standalone a composite? false` | 12-14, 178 | Default trait implementation |
| `Is root a composite? true` | 98-100, 179 | Directory overrides to true |
| `Temp directory size after removal: 0 bytes` | 69, 188 | After remove(), size recalculates to 0 |

### Size Calculation Breakdown

The recursive size calculation demonstrates the Composite pattern's elegance:

| Component | Calculation | Total |
|-----------|-------------|-------|
| root | README.md + config.json + src + tests | 16640 bytes |
| src | main.rs + lib.rs + utils.rs + modules | 13312 bytes |
| modules | auth.rs + database.rs | 5632 bytes |
| tests | test_main.rs + test_utils.rs | 1792 bytes |

## Key Characteristics of Composite Pattern in Rust

### 1. Trait Objects for Polymorphism
```rust
children: RefCell<Vec<Rc<dyn FileSystemComponent>>>
```
- Uses `dyn` trait objects to store heterogeneous collections
- Enables storing both `File` and `Directory` in the same vector

### 2. Smart Pointers for Ownership
- `Rc<T>` enables shared ownership (multiple directories could reference same file)
- `RefCell<T>` provides interior mutability within `Rc`
- Combined as `Rc<RefCell<T>>` or `RefCell<Vec<Rc<T>>>` pattern

### 3. Recursive Operations
- Both `get_size()` and `display()` naturally recurse through the tree
- The pattern elegantly handles arbitrary nesting depth

### 4. Uniform Treatment
- Client code calls the same methods on both leaves and composites
- The implementation handles the difference transparently

### 5. Memory Safety
- Rust's ownership system prevents:
  - Dangling references
  - Memory leaks (with `Rc`)
  - Data races (single-threaded; use `Arc` for multi-threaded)

### 6. No Runtime Exceptions
- Rust's type system catches most errors at compile time
- `borrow()` and `borrow_mut()` can panic if borrow rules are violated

## When to Use This Pattern

- Representing part-whole hierarchies (file systems, GUI components, organization charts)
- When clients should treat individual objects and compositions uniformly
- When you want to add new component types without changing existing code

## Rust-Specific Considerations

- **Thread Safety**: Replace `Rc<RefCell<T>>` with `Arc<Mutex<T>>` for multi-threaded use
- **Compile with**: `rustc main_composite.rs -o main_composite`
- **Rust Version**: Compatible with Rust 1.0+ (stable)
