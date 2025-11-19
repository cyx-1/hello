# Composite Pattern

The Composite pattern composes objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

**Requires: Python 3.10+** (uses union types with `|` syntax)

## Key Components

- **Component**: Common interface for all objects in composition (`FileSystemComponent`)
- **Leaf**: Represents leaf objects with no children (`File`, `SymbolicLink`)
- **Composite**: Stores child components and implements child-related operations (`Directory`)

## Source Code

### Component Interface (Lines 22-63)

```python:main_composite.py startLine=22 endLine=63
class FileSystemComponent(ABC):
    """Abstract component for file system items."""

    def __init__(self, name: str):
        self.name = name
        self._parent: "FileSystemComponent | None" = None

    @property
    def parent(self) -> "FileSystemComponent | None":
        return self._parent

    @parent.setter
    def parent(self, value: "FileSystemComponent | None") -> None:
        self._parent = value

    @abstractmethod
    def get_size(self) -> int:
        """Get size in bytes."""
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display component with indentation."""
        pass

    @abstractmethod
    def get_path(self) -> str:
        """Get full path."""
        pass

    def is_composite(self) -> bool:
        """Check if this is a composite component."""
        return False

    def add(self, component: "FileSystemComponent") -> None:
        """Add a child component (only for composites)."""
        raise NotImplementedError("Cannot add to a leaf component")

    def remove(self, component: "FileSystemComponent") -> None:
        """Remove a child component (only for composites)."""
        raise NotImplementedError("Cannot remove from a leaf component")
```

### Leaf Component - File (Lines 66-92)

```python:main_composite.py startLine=66 endLine=92
class File(FileSystemComponent):
    """Leaf component representing a file."""

    def __init__(self, name: str, size: int, file_type: str = "txt"):
        super().__init__(name)
        self._size = size
        self.file_type = file_type

    def get_size(self) -> int:
        return self._size

    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        return f"{prefix} {self.name} ({self._format_size()})"

    def get_path(self) -> str:
        if self._parent:
            return f"{self._parent.get_path()}/{self.name}"
        return self.name

    def _format_size(self) -> str:
        if self._size < 1024:
            return f"{self._size} B"
        elif self._size < 1024 * 1024:
            return f"{self._size / 1024:.1f} KB"
        else:
            return f"{self._size / (1024 * 1024):.1f} MB"
```

### Composite Component - Directory (Lines 116-183)

```python:main_composite.py startLine=116 endLine=161
class Directory(FileSystemComponent):
    """Composite component representing a directory."""

    def __init__(self, name: str):
        super().__init__(name)
        self._children: list[FileSystemComponent] = []

    def is_composite(self) -> bool:
        return True

    def add(self, component: FileSystemComponent) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: FileSystemComponent) -> None:
        self._children.remove(component)
        component.parent = None

    def get_children(self) -> list[FileSystemComponent]:
        return self._children.copy()

    def get_size(self) -> int:
        """Calculate total size of directory and all contents."""
        return sum(child.get_size() for child in self._children)

    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        result = [f"{prefix} {self.name}/"]
        for child in self._children:
            result.append(child.display(indent + 1))
        return "\n".join(result)

    def get_path(self) -> str:
        if self._parent:
            return f"{self._parent.get_path()}/{self.name}"
        return self.name

    def count_files(self) -> int:
        """Count all files in directory and subdirectories."""
        count = 0
        for child in self._children:
            if isinstance(child, File):
                count += 1
            elif isinstance(child, Directory):
                count += child.count_files()
        return count
```

### Building the Tree Structure (Lines 201-244)

```python:main_composite.py startLine=201 endLine=244
    # Build file system structure
    root = Directory("project")

    # Source directory
    src = Directory("src")
    src.add(File("main.py", 2500, "py"))
    src.add(File("utils.py", 1200, "py"))
    src.add(File("config.py", 800, "py"))

    # Components subdirectory
    components = Directory("components")
    components.add(File("button.py", 1500, "py"))
    components.add(File("modal.py", 2000, "py"))
    components.add(File("form.py", 3000, "py"))
    src.add(components)

    # Tests directory
    tests = Directory("tests")
    tests.add(File("test_main.py", 1800, "py"))
    tests.add(File("test_utils.py", 1200, "py"))

    # Docs directory
    docs = Directory("docs")
    docs.add(File("README.md", 5000, "md"))
    docs.add(File("API.md", 12000, "md"))
    docs.add(File("CHANGELOG.md", 8000, "md"))

    # Assets directory
    assets = Directory("assets")
    assets.add(File("logo.png", 150000, "png"))
    assets.add(File("banner.jpg", 280000, "jpg"))
    assets.add(File("styles.css", 4500, "css"))

    # Add all to root
    root.add(src)
    root.add(tests)
    root.add(docs)
    root.add(assets)
    root.add(File("pyproject.toml", 600, "toml"))
    root.add(File(".gitignore", 200, "txt"))

    # Add symbolic link
    readme_link = SymbolicLink("README", docs.find_by_extension(".md")[0])
    root.add(readme_link)
```

## Program Output

```
============================================================
Composite Pattern - File System Demo
============================================================

--- File System Structure ---
 project/
   src/
     main.py (2.4 KB)
     utils.py (1.2 KB)
     config.py (800 B)
     components/
       button.py (1.5 KB)
       modal.py (2.0 KB)
       form.py (2.9 KB)
   tests/
     test_main.py (1.8 KB)
     test_utils.py (1.2 KB)
   docs/
     README.md (4.9 KB)
     API.md (11.7 KB)
     CHANGELOG.md (7.8 KB)
   assets/
     logo.png (146.5 KB)
     banner.jpg (273.4 KB)
     styles.css (4.4 KB)
   pyproject.toml (600 B)
   .gitignore (200 B)
   README -> project/docs/README.md


--- Size Calculations ---
Total project size: 463.2 KB
Source code size: 10.7 KB
Documentation size: 24.4 KB
Assets size: 424.3 KB

--- File Counts ---
Total files in project: 16
Source files: 6
Test files: 2

--- Search Operations ---

Python files (8):
  - project/src/main.py
  - project/src/utils.py
  - project/src/config.py
  - project/src/components/button.py
  - project/src/components/modal.py
  - project/src/components/form.py
  - project/tests/test_main.py
  - project/tests/test_utils.py

Markdown files (3):
  - project/docs/README.md
  - project/docs/API.md
  - project/docs/CHANGELOG.md

--- Uniform Treatment Demo ---

For a file:
Name: main.py
Path: project/src/main.py
Size: 2.4 KB
Is composite: False

For a directory:
Name: src
Path: project/src
Size: 10.7 KB
Is composite: True


============================================================
Benefits of Composite Pattern:
============================================================
1. Simplifies client code - treats all objects uniformly
2. Easy to add new component types
3. Natural representation of hierarchical structures
4. Recursive composition allows complex structures
```

## Annotations

### How It Works

1. **Component Interface (Lines 22-63)**: The `FileSystemComponent` abstract class defines the common interface with `get_size()`, `display()`, and `get_path()`. It also provides default implementations for `add()` and `remove()` that raise errors for leaf nodes.

2. **Leaf Components (Lines 66-112)**:
   - `File` returns its own size directly (Line 74: `return self._size`)
   - `SymbolicLink` returns 0 for size since it doesn't contribute to total

3. **Composite Component (Lines 116-183)**:
   - `Directory.get_size()` (Line 137-139) recursively sums sizes of all children
   - `Directory.display()` (Lines 141-146) recursively displays all children with increasing indentation
   - `Directory.count_files()` (Lines 153-161) recursively counts files in subdirectories

### Output Analysis

**Tree Structure Display**:
The `display()` method recursively traverses the tree, incrementing indent for each level. The `src/components/` subdirectory shows 3 levels of nesting, demonstrating how the composite pattern naturally represents hierarchies.

**Size Calculations**:
- `root.get_size()` returns 463.2 KB (total of all children)
- `src.get_size()` returns 10.7 KB (main.py + utils.py + config.py + components/)
- The same `get_size()` method works for both files (returns stored value) and directories (sums children)

**File Counts**:
- `root.count_files()` = 16 (counts recursively through all subdirectories)
- `src.count_files()` = 6 (3 direct files + 3 in components/)

**Uniform Treatment Demo (Lines 276-290)**:
The `print_info()` function accepts any `FileSystemComponent` and calls the same methods on both:
- For `File`: size is 2.4 KB, `is_composite()` returns False
- For `Directory`: size is 10.7 KB (computed), `is_composite()` returns True

### Key Insight

The power of the Composite pattern is that clients don't need to know whether they're working with a single file or an entire directory tree. The same `get_size()` call works uniformly - a file returns its size, while a directory recursively computes the sum of all its contents. This allows complex operations (like calculating total project size) to be expressed with simple, uniform code.
