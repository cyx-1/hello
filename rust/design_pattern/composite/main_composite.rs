// Composite Design Pattern in Rust
// Demonstrates a file system hierarchy with files (leaves) and directories (composites)

use std::cell::RefCell;
use std::rc::Rc;

// Component trait - defines the interface for all objects in the composition
trait FileSystemComponent {
    fn get_name(&self) -> &str;
    fn get_size(&self) -> u64;
    fn display(&self, indent: usize);
    fn is_composite(&self) -> bool {
        false
    }
}

// Leaf - represents individual files that cannot contain other components
struct File {
    name: String,
    size: u64,
}

impl File {
    fn new(name: &str, size: u64) -> Self {
        println!("  [Created File] '{}' ({} bytes)", name, size);
        File {
            name: name.to_string(),
            size,
        }
    }
}

impl FileSystemComponent for File {
    fn get_name(&self) -> &str {
        &self.name
    }

    fn get_size(&self) -> u64 {
        self.size
    }

    fn display(&self, indent: usize) {
        let prefix = "  ".repeat(indent);
        println!("{}|- File: {} ({} bytes)", prefix, self.name, self.size);
    }
}

// Composite - represents directories that can contain other components
struct Directory {
    name: String,
    children: RefCell<Vec<Rc<dyn FileSystemComponent>>>,
}

impl Directory {
    fn new(name: &str) -> Self {
        println!("  [Created Directory] '{}'", name);
        Directory {
            name: name.to_string(),
            children: RefCell::new(Vec::new()),
        }
    }

    fn add(&self, component: Rc<dyn FileSystemComponent>) {
        println!("  [Added] '{}' to '{}'", component.get_name(), self.name);
        self.children.borrow_mut().push(component);
    }

    fn remove(&self, name: &str) {
        self.children.borrow_mut().retain(|c| c.get_name() != name);
        println!("  [Removed] '{}' from '{}'", name, self.name);
    }
}

impl FileSystemComponent for Directory {
    fn get_name(&self) -> &str {
        &self.name
    }

    fn get_size(&self) -> u64 {
        // Recursively calculate total size of all children
        self.children
            .borrow()
            .iter()
            .map(|child| child.get_size())
            .sum()
    }

    fn display(&self, indent: usize) {
        let prefix = "  ".repeat(indent);
        println!("{}|+ Directory: {} (total: {} bytes)", prefix, self.name, self.get_size());

        // Recursively display all children
        for child in self.children.borrow().iter() {
            child.display(indent + 1);
        }
    }

    fn is_composite(&self) -> bool {
        true
    }
}

fn main() {
    println!("=== Composite Design Pattern Demo ===\n");

    // Step 1: Create the root directory
    println!("Step 1: Creating root directory structure");
    let root = Rc::new(Directory::new("root"));

    // Step 2: Create files for root directory
    println!("\nStep 2: Creating files for root");
    let readme = Rc::new(File::new("README.md", 1024));
    let config = Rc::new(File::new("config.json", 512));

    // Step 3: Add files to root
    println!("\nStep 3: Adding files to root");
    root.add(readme);
    root.add(config);

    // Step 4: Create subdirectories
    println!("\nStep 4: Creating subdirectories");
    let src_dir = Rc::new(Directory::new("src"));
    let tests_dir = Rc::new(Directory::new("tests"));

    // Step 5: Create files for src directory
    println!("\nStep 5: Creating files for src directory");
    let main_file = Rc::new(File::new("main.rs", 2048));
    let lib_file = Rc::new(File::new("lib.rs", 4096));
    let utils_file = Rc::new(File::new("utils.rs", 1536));

    // Step 6: Add files to src directory
    println!("\nStep 6: Adding files to src directory");
    src_dir.add(main_file);
    src_dir.add(lib_file);
    src_dir.add(utils_file);

    // Step 7: Create nested directory inside src
    println!("\nStep 7: Creating nested directory (modules)");
    let modules_dir = Rc::new(Directory::new("modules"));
    let auth_file = Rc::new(File::new("auth.rs", 3072));
    let db_file = Rc::new(File::new("database.rs", 2560));

    println!("\nStep 8: Adding files to modules directory");
    modules_dir.add(auth_file);
    modules_dir.add(db_file);

    // Step 9: Add modules directory to src
    println!("\nStep 9: Adding modules to src directory");
    src_dir.add(modules_dir);

    // Step 10: Create test files
    println!("\nStep 10: Creating test files");
    let test_main = Rc::new(File::new("test_main.rs", 1024));
    let test_utils = Rc::new(File::new("test_utils.rs", 768));

    // Step 11: Add test files to tests directory
    println!("\nStep 11: Adding test files to tests directory");
    tests_dir.add(test_main);
    tests_dir.add(test_utils);

    // Step 12: Add subdirectories to root
    println!("\nStep 12: Adding subdirectories to root");
    root.add(src_dir);
    root.add(tests_dir);

    // Step 13: Display the complete tree structure
    println!("\n=== Complete File System Tree ===\n");
    root.display(0);

    // Step 14: Demonstrate uniform treatment - get sizes
    println!("\n=== Size Calculations (Uniform Treatment) ===\n");
    println!("Total size of root: {} bytes", root.get_size());

    // Step 15: Create a standalone file to show leaf behavior
    println!("\n=== Demonstrating Leaf vs Composite ===\n");
    let standalone = Rc::new(File::new("standalone.txt", 256));
    println!("Standalone file size: {} bytes", standalone.get_size());
    println!("Is standalone a composite? {}", standalone.is_composite());
    println!("Is root a composite? {}", root.is_composite());

    // Step 16: Demonstrate remove operation
    println!("\n=== Demonstrating Remove Operation ===\n");
    let temp_dir = Rc::new(Directory::new("temp"));
    let temp_file = Rc::new(File::new("temp.txt", 100));
    temp_dir.add(temp_file);
    println!("Temp directory size before removal: {} bytes", temp_dir.get_size());
    temp_dir.remove("temp.txt");
    println!("Temp directory size after removal: {} bytes", temp_dir.get_size());

    println!("\n=== End of Composite Pattern Demo ===");
}
