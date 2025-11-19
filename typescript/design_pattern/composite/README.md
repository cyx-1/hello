# Composite Design Pattern - TypeScript Implementation

## Pattern Description

The **Composite Design Pattern** is a structural pattern that lets you compose objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects (leaves) and compositions of objects (composites) uniformly through a common interface.

### Key Characteristics

- **Tree Structure**: Objects are organized in a tree hierarchy
- **Uniform Interface**: Both leaf and composite nodes implement the same interface
- **Recursive Composition**: Composites can contain both leaves and other composites
- **Transparency**: Clients don't need to know whether they're working with a leaf or composite

### Use Cases

- File system structures (files and directories)
- UI component hierarchies
- Organization charts
- Menu systems with nested submenus
- Document structures (chapters, sections, paragraphs)

## Requirements

- **Node.js**: 18.0 or higher
- **TypeScript**: 5.3.0 or higher
- **npm**: 8.0 or higher

## How to Run

```bash
# Navigate to the composite directory
cd typescript/composite

# Install dependencies
npm install

# Build and run the application
npm run start
```

## Source Code

```typescript
     1→/**
     2→ * Composite Design Pattern Implementation
     3→ *
     4→ * This example demonstrates the Composite pattern using a file system hierarchy.
     5→ * Files are leaf nodes and Directories are composite nodes that can contain
     6→ * both files and other directories.
     7→ */
     8→
     9→// Component interface - declares common operations for both leaf and composite objects
    10→interface FileSystemComponent {
    11→    getName(): string;
    12→    getSize(): number;
    13→    display(indent?: string): void;
    14→    search(name: string): FileSystemComponent[];
    15→}
    16→
    17→// Leaf class - represents end objects that have no children
    18→class FileNode implements FileSystemComponent {
    19→    private name: string;
    20→    private size: number;
    21→
    22→    constructor(name: string, size: number) {
    23→        this.name = name;
    24→        this.size = size;
    25→    }
    26→
    27→    getName(): string {
    28→        return this.name;
    29→    }
    30→
    31→    getSize(): number {
    32→        return this.size;
    33→    }
    34→
    35→    display(indent: string = ""): void {
    36→        console.log(`${indent}[Line 36] File: ${this.name} (${this.size} KB)`);
    37→    }
    38→
    39→    search(name: string): FileSystemComponent[] {
    40→        if (this.name.toLowerCase().includes(name.toLowerCase())) {
    41→            return [this];
    42→        }
    43→        return [];
    44→    }
    45→}
    46→
    47→// Composite class - represents complex components that may have children
    48→class Directory implements FileSystemComponent {
    49→    private name: string;
    50→    private children: FileSystemComponent[] = [];
    51→
    52→    constructor(name: string) {
    53→        this.name = name;
    54→    }
    55→
    56→    getName(): string {
    57→        return this.name;
    58→    }
    59→
    60→    // Calculates total size by summing all children recursively
    61→    getSize(): number {
    62→        return this.children.reduce((total, child) => total + child.getSize(), 0);
    63→    }
    64→
    65→    add(component: FileSystemComponent): void {
    66→        this.children.push(component);
    67→    }
    68→
    69→    remove(component: FileSystemComponent): void {
    70→        const index = this.children.indexOf(component);
    71→        if (index > -1) {
    72→            this.children.splice(index, 1);
    73→        }
    74→    }
    75→
    76→    getChildren(): FileSystemComponent[] {
    77→        return this.children;
    78→    }
    79→
    80→    display(indent: string = ""): void {
    81→        console.log(`${indent}[Line 81] Directory: ${this.name}/ (${this.getSize()} KB total)`);
    82→        this.children.forEach(child => {
    83→            child.display(indent + "  ");
    84→        });
    85→    }
    86→
    87→    // Searches recursively through all children
    88→    search(name: string): FileSystemComponent[] {
    89→        let results: FileSystemComponent[] = [];
    90→
    91→        if (this.name.toLowerCase().includes(name.toLowerCase())) {
    92→            results.push(this);
    93→        }
    94→
    95→        this.children.forEach(child => {
    96→            results = results.concat(child.search(name));
    97→        });
    98→
    99→        return results;
   100→    }
   101→}
   102→
   103→// Client code that works with all components through the base interface
   104→function printSeparator(title: string): void {
   105→    console.log("\n" + "=".repeat(50));
   106→    console.log(`[Line 106] ${title}`);
   107→    console.log("=".repeat(50));
   108→}
   109→
   110→// Main demonstration
   111→function main(): void {
   112→    console.log("[Line 112] Creating file system structure...\n");
   113→
   114→    // Create leaf nodes (files)
   115→    const file1 = new FileNode("readme.md", 5);
   116→    const file2 = new FileNode("index.ts", 12);
   117→    const file3 = new FileNode("styles.css", 8);
   118→    const file4 = new FileNode("app.ts", 25);
   119→    const file5 = new FileNode("utils.ts", 15);
   120→    const file6 = new FileNode("config.json", 3);
   121→    const file7 = new FileNode("package.json", 2);
   122→    const file8 = new FileNode("test.spec.ts", 18);
   123→
   124→    // Create composite nodes (directories)
   125→    const root = new Directory("project");
   126→    const src = new Directory("src");
   127→    const components = new Directory("components");
   128→    const tests = new Directory("tests");
   129→    const config = new Directory("config");
   130→
   131→    // Build the tree structure
   132→    console.log("[Line 132] Building directory tree...");
   133→
   134→    // Add files to components directory
   135→    components.add(file3);
   136→    components.add(file4);
   137→
   138→    // Add files and subdirectory to src
   139→    src.add(file2);
   140→    src.add(file5);
   141→    src.add(components);
   142→
   143→    // Add test files
   144→    tests.add(file8);
   145→
   146→    // Add config files
   147→    config.add(file6);
   148→
   149→    // Build root directory
   150→    root.add(file1);
   151→    root.add(file7);
   152→    root.add(src);
   153→    root.add(tests);
   154→    root.add(config);
   155→
   156→    // Display the complete tree structure
   157→    printSeparator("Complete File System Structure");
   158→    root.display();
   159→
   160→    // Demonstrate uniform treatment - both files and directories respond to getSize()
   161→    printSeparator("Size Calculations (Uniform Treatment)");
   162→    console.log(`[Line 162] Root directory total size: ${root.getSize()} KB`);
   163→    console.log(`[Line 163] src directory size: ${src.getSize()} KB`);
   164→    console.log(`[Line 164] components directory size: ${components.getSize()} KB`);
   165→    console.log(`[Line 165] Single file (app.ts) size: ${file4.getSize()} KB`);
   166→
   167→    // Demonstrate search functionality
   168→    printSeparator("Search Functionality");
   169→
   170→    const tsFiles = root.search(".ts");
   171→    console.log(`[Line 171] Found ${tsFiles.length} items containing '.ts':`);
   172→    tsFiles.forEach(item => {
   173→        console.log(`  - ${item.getName()} (${item.getSize()} KB)`);
   174→    });
   175→
   176→    const configSearch = root.search("config");
   177→    console.log(`\n[Line 177] Found ${configSearch.length} items containing 'config':`);
   178→    configSearch.forEach(item => {
   179→        console.log(`  - ${item.getName()}`);
   180→    });
   181→
   182→    // Demonstrate adding and removing components
   183→    printSeparator("Dynamic Modifications");
   184→
   185→    const newFile = new FileNode("api.ts", 20);
   186→    src.add(newFile);
   187→    console.log(`[Line 187] Added new file 'api.ts' to src directory`);
   188→    console.log(`[Line 188] Updated src directory size: ${src.getSize()} KB`);
   189→    console.log(`[Line 189] Updated root directory size: ${root.getSize()} KB`);
   190→
   191→    // Remove a file
   192→    src.remove(newFile);
   193→    console.log(`[Line 193] Removed 'api.ts' from src directory`);
   194→    console.log(`[Line 194] Reverted src directory size: ${src.getSize()} KB`);
   195→
   196→    // Demonstrate that client code doesn't need to know whether it's
   197→    // working with a leaf or composite
   198→    printSeparator("Polymorphic Behavior");
   199→
   200→    const components_to_check: FileSystemComponent[] = [file1, src, components, file4];
   201→    console.log("[Line 201] Checking sizes of mixed components (files and directories):");
   202→    components_to_check.forEach(component => {
   203→        console.log(`  ${component.getName()}: ${component.getSize()} KB`);
   204→    });
   205→
   206→    // Display nested structure for clarity
   207→    printSeparator("Final Directory Structure");
   208→    root.display();
   209→
   210→    console.log("\n[Line 210] Composite pattern demonstration complete!");
   211→}
   212→
   213→// Run the demonstration
   214→main();
```

## Program Output

```
[Line 112] Creating file system structure...

[Line 132] Building directory tree...

==================================================
[Line 106] Complete File System Structure
==================================================
[Line 81] Directory: project/ (88 KB total)
  [Line 36] File: readme.md (5 KB)
  [Line 36] File: package.json (2 KB)
  [Line 81] Directory: src/ (60 KB total)
    [Line 36] File: index.ts (12 KB)
    [Line 36] File: utils.ts (15 KB)
    [Line 81] Directory: components/ (33 KB total)
      [Line 36] File: styles.css (8 KB)
      [Line 36] File: app.ts (25 KB)
  [Line 81] Directory: tests/ (18 KB total)
    [Line 36] File: test.spec.ts (18 KB)
  [Line 81] Directory: config/ (3 KB total)
    [Line 36] File: config.json (3 KB)

==================================================
[Line 106] Size Calculations (Uniform Treatment)
==================================================
[Line 162] Root directory total size: 88 KB
[Line 163] src directory size: 60 KB
[Line 164] components directory size: 33 KB
[Line 165] Single file (app.ts) size: 25 KB

==================================================
[Line 106] Search Functionality
==================================================
[Line 171] Found 4 items containing '.ts':
  - index.ts (12 KB)
  - utils.ts (15 KB)
  - app.ts (25 KB)
  - test.spec.ts (18 KB)

[Line 177] Found 2 items containing 'config':
  - config
  - config.json

==================================================
[Line 106] Dynamic Modifications
==================================================
[Line 187] Added new file 'api.ts' to src directory
[Line 188] Updated src directory size: 80 KB
[Line 189] Updated root directory size: 108 KB
[Line 193] Removed 'api.ts' from src directory
[Line 194] Reverted src directory size: 60 KB

==================================================
[Line 106] Polymorphic Behavior
==================================================
[Line 201] Checking sizes of mixed components (files and directories):
  readme.md: 5 KB
  src: 60 KB
  components: 33 KB
  app.ts: 25 KB

==================================================
[Line 106] Final Directory Structure
==================================================
[Line 81] Directory: project/ (88 KB total)
  [Line 36] File: readme.md (5 KB)
  [Line 36] File: package.json (2 KB)
  [Line 81] Directory: src/ (60 KB total)
    [Line 36] File: index.ts (12 KB)
    [Line 36] File: utils.ts (15 KB)
    [Line 81] Directory: components/ (33 KB total)
      [Line 36] File: styles.css (8 KB)
      [Line 36] File: app.ts (25 KB)
  [Line 81] Directory: tests/ (18 KB total)
    [Line 36] File: test.spec.ts (18 KB)
  [Line 81] Directory: config/ (3 KB total)
    [Line 36] File: config.json (3 KB)

[Line 210] Composite pattern demonstration complete!
```

## Code Analysis and Annotations

### Pattern Structure

| Component | Type | Description | Source Lines |
|-----------|------|-------------|--------------|
| `FileSystemComponent` | Interface | Common interface for all components | 10-15 |
| `FileNode` | Leaf | Represents individual files with no children | 18-45 |
| `Directory` | Composite | Container that can hold files and other directories | 48-101 |

### Key Method Implementations

| Method | FileNode (Leaf) | Directory (Composite) | Purpose |
|--------|-----------------|----------------------|---------|
| `getSize()` | Returns stored size (Line 31-33) | Recursively sums children sizes (Line 61-63) | Demonstrates uniform interface with different implementations |
| `display()` | Prints file info (Line 35-37) | Prints directory and recursively displays children (Line 80-85) | Tree traversal visualization |
| `search()` | Checks if name matches (Line 39-44) | Recursively searches all children (Line 88-100) | Demonstrates recursive operations across tree |

### Output-to-Source Correlation

#### Tree Structure Display

| Output | Source Line | Explanation |
|--------|-------------|-------------|
| `[Line 81] Directory: project/ (88 KB total)` | 81 | Root directory display - size calculated by summing all nested children |
| `[Line 36] File: readme.md (5 KB)` | 36 | Leaf node display - shows individual file with its direct size |
| `[Line 81] Directory: src/ (60 KB total)` | 81 | Nested composite - contains files (12+15 KB) + components directory (33 KB) |
| `[Line 81] Directory: components/ (33 KB total)` | 81 | Deeply nested composite - contains styles.css (8 KB) + app.ts (25 KB) |

#### Size Calculations (Uniform Treatment)

| Output | Source Line | Calculation |
|--------|-------------|-------------|
| `[Line 162] Root directory total size: 88 KB` | 162 | 5 + 2 + 60 + 18 + 3 = 88 KB (all files in tree) |
| `[Line 163] src directory size: 60 KB` | 163 | 12 + 15 + 33 = 60 KB (index.ts + utils.ts + components/) |
| `[Line 164] components directory size: 33 KB` | 164 | 8 + 25 = 33 KB (styles.css + app.ts) |
| `[Line 165] Single file (app.ts) size: 25 KB` | 165 | Direct file size - no recursion needed |

#### Search Functionality

| Output | Source Line | Behavior |
|--------|-------------|----------|
| `[Line 171] Found 4 items containing '.ts'` | 171 | Recursive search finds all TypeScript files in tree |
| `[Line 177] Found 2 items containing 'config'` | 177 | Finds both directory (config/) and file (config.json) |

#### Dynamic Modifications

| Output | Source Line | Key Concept |
|--------|-------------|-------------|
| `[Line 187] Added new file 'api.ts'` | 187 | Demonstrates runtime composition modification |
| `[Line 188] Updated src directory size: 80 KB` | 188 | Size auto-recalculates: 60 + 20 = 80 KB |
| `[Line 189] Updated root directory size: 108 KB` | 189 | Change propagates up the tree: 88 + 20 = 108 KB |
| `[Line 193] Removed 'api.ts'` | 193 | Component removal from tree |
| `[Line 194] Reverted src directory size: 60 KB` | 194 | Size correctly reverts after removal |

#### Polymorphic Behavior

| Output | Source Line | Component Type | Size |
|--------|-------------|----------------|------|
| `readme.md: 5 KB` | 201-203 | FileNode (Leaf) | Direct size |
| `src: 60 KB` | 201-203 | Directory (Composite) | Calculated recursively |
| `components: 33 KB` | 201-203 | Directory (Composite) | Calculated recursively |
| `app.ts: 25 KB` | 201-203 | FileNode (Leaf) | Direct size |

### Design Pattern Benefits Demonstrated

1. **Uniform Treatment** (Lines 200-204): Client code iterates over mixed array of files and directories, calling `getSize()` on each without type checking.

2. **Recursive Operations** (Lines 61-63, 88-100): Size calculation and search automatically traverse the entire tree structure.

3. **Dynamic Composition** (Lines 185-194): Components can be added/removed at runtime, and calculations automatically update.

4. **Encapsulation** (Lines 82-84): Each component knows how to display itself and its children, hiding implementation details from clients.

### Tree Structure Visualization

```
project/ (88 KB)
├── readme.md (5 KB)
├── package.json (2 KB)
├── src/ (60 KB)
│   ├── index.ts (12 KB)
│   ├── utils.ts (15 KB)
│   └── components/ (33 KB)
│       ├── styles.css (8 KB)
│       └── app.ts (25 KB)
├── tests/ (18 KB)
│   └── test.spec.ts (18 KB)
└── config/ (3 KB)
    └── config.json (3 KB)
```
