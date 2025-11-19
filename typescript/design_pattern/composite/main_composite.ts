/**
 * Composite Design Pattern Implementation
 *
 * This example demonstrates the Composite pattern using a file system hierarchy.
 * Files are leaf nodes and Directories are composite nodes that can contain
 * both files and other directories.
 */

// Component interface - declares common operations for both leaf and composite objects
interface FileSystemComponent {
    getName(): string;
    getSize(): number;
    display(indent?: string): void;
    search(name: string): FileSystemComponent[];
}

// Leaf class - represents end objects that have no children
class FileNode implements FileSystemComponent {
    private name: string;
    private size: number;

    constructor(name: string, size: number) {
        this.name = name;
        this.size = size;
    }

    getName(): string {
        return this.name;
    }

    getSize(): number {
        return this.size;
    }

    display(indent: string = ""): void {
        console.log(`${indent}[Line 36] File: ${this.name} (${this.size} KB)`);
    }

    search(name: string): FileSystemComponent[] {
        if (this.name.toLowerCase().includes(name.toLowerCase())) {
            return [this];
        }
        return [];
    }
}

// Composite class - represents complex components that may have children
class Directory implements FileSystemComponent {
    private name: string;
    private children: FileSystemComponent[] = [];

    constructor(name: string) {
        this.name = name;
    }

    getName(): string {
        return this.name;
    }

    // Calculates total size by summing all children recursively
    getSize(): number {
        return this.children.reduce((total, child) => total + child.getSize(), 0);
    }

    add(component: FileSystemComponent): void {
        this.children.push(component);
    }

    remove(component: FileSystemComponent): void {
        const index = this.children.indexOf(component);
        if (index > -1) {
            this.children.splice(index, 1);
        }
    }

    getChildren(): FileSystemComponent[] {
        return this.children;
    }

    display(indent: string = ""): void {
        console.log(`${indent}[Line 81] Directory: ${this.name}/ (${this.getSize()} KB total)`);
        this.children.forEach(child => {
            child.display(indent + "  ");
        });
    }

    // Searches recursively through all children
    search(name: string): FileSystemComponent[] {
        let results: FileSystemComponent[] = [];

        if (this.name.toLowerCase().includes(name.toLowerCase())) {
            results.push(this);
        }

        this.children.forEach(child => {
            results = results.concat(child.search(name));
        });

        return results;
    }
}

// Client code that works with all components through the base interface
function printSeparator(title: string): void {
    console.log("\n" + "=".repeat(50));
    console.log(`[Line 106] ${title}`);
    console.log("=".repeat(50));
}

// Main demonstration
function main(): void {
    console.log("[Line 112] Creating file system structure...\n");

    // Create leaf nodes (files)
    const file1 = new FileNode("readme.md", 5);
    const file2 = new FileNode("index.ts", 12);
    const file3 = new FileNode("styles.css", 8);
    const file4 = new FileNode("app.ts", 25);
    const file5 = new FileNode("utils.ts", 15);
    const file6 = new FileNode("config.json", 3);
    const file7 = new FileNode("package.json", 2);
    const file8 = new FileNode("test.spec.ts", 18);

    // Create composite nodes (directories)
    const root = new Directory("project");
    const src = new Directory("src");
    const components = new Directory("components");
    const tests = new Directory("tests");
    const config = new Directory("config");

    // Build the tree structure
    console.log("[Line 132] Building directory tree...");

    // Add files to components directory
    components.add(file3);
    components.add(file4);

    // Add files and subdirectory to src
    src.add(file2);
    src.add(file5);
    src.add(components);

    // Add test files
    tests.add(file8);

    // Add config files
    config.add(file6);

    // Build root directory
    root.add(file1);
    root.add(file7);
    root.add(src);
    root.add(tests);
    root.add(config);

    // Display the complete tree structure
    printSeparator("Complete File System Structure");
    root.display();

    // Demonstrate uniform treatment - both files and directories respond to getSize()
    printSeparator("Size Calculations (Uniform Treatment)");
    console.log(`[Line 162] Root directory total size: ${root.getSize()} KB`);
    console.log(`[Line 163] src directory size: ${src.getSize()} KB`);
    console.log(`[Line 164] components directory size: ${components.getSize()} KB`);
    console.log(`[Line 165] Single file (app.ts) size: ${file4.getSize()} KB`);

    // Demonstrate search functionality
    printSeparator("Search Functionality");

    const tsFiles = root.search(".ts");
    console.log(`[Line 171] Found ${tsFiles.length} items containing '.ts':`);
    tsFiles.forEach(item => {
        console.log(`  - ${item.getName()} (${item.getSize()} KB)`);
    });

    const configSearch = root.search("config");
    console.log(`\n[Line 177] Found ${configSearch.length} items containing 'config':`);
    configSearch.forEach(item => {
        console.log(`  - ${item.getName()}`);
    });

    // Demonstrate adding and removing components
    printSeparator("Dynamic Modifications");

    const newFile = new FileNode("api.ts", 20);
    src.add(newFile);
    console.log(`[Line 187] Added new file 'api.ts' to src directory`);
    console.log(`[Line 188] Updated src directory size: ${src.getSize()} KB`);
    console.log(`[Line 189] Updated root directory size: ${root.getSize()} KB`);

    // Remove a file
    src.remove(newFile);
    console.log(`[Line 193] Removed 'api.ts' from src directory`);
    console.log(`[Line 194] Reverted src directory size: ${src.getSize()} KB`);

    // Demonstrate that client code doesn't need to know whether it's
    // working with a leaf or composite
    printSeparator("Polymorphic Behavior");

    const components_to_check: FileSystemComponent[] = [file1, src, components, file4];
    console.log("[Line 201] Checking sizes of mixed components (files and directories):");
    components_to_check.forEach(component => {
        console.log(`  ${component.getName()}: ${component.getSize()} KB`);
    });

    // Display nested structure for clarity
    printSeparator("Final Directory Structure");
    root.display();

    console.log("\n[Line 210] Composite pattern demonstration complete!");
}

// Run the demonstration
main();
