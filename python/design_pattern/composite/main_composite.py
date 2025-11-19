# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Composite Pattern

The Composite pattern composes objects into tree structures to represent part-whole
hierarchies. It lets clients treat individual objects and compositions of objects
uniformly.

Key Components:
- Component: Common interface for all objects in composition
- Leaf: Represents leaf objects with no children
- Composite: Stores child components and implements child-related operations
"""

from abc import ABC, abstractmethod


# Component interface
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


# Leaf components
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
        return f"{prefix}📄 {self.name} ({self._format_size()})"

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


class SymbolicLink(FileSystemComponent):
    """Leaf component representing a symbolic link."""

    def __init__(self, name: str, target: FileSystemComponent):
        super().__init__(name)
        self.target = target

    def get_size(self) -> int:
        return 0  # Symlinks don't contribute to size

    def display(self, indent: int = 0) -> str:
        prefix = "  " * indent
        return f"{prefix}🔗 {self.name} -> {self.target.get_path()}"

    def get_path(self) -> str:
        if self._parent:
            return f"{self._parent.get_path()}/{self.name}"
        return self.name


# Composite component
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
        result = [f"{prefix}📁 {self.name}/"]
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

    def find_by_name(self, name: str) -> list[FileSystemComponent]:
        """Find all components matching name."""
        results = []
        if self.name == name:
            results.append(self)
        for child in self._children:
            if child.name == name:
                results.append(child)
            if isinstance(child, Directory):
                results.extend(child.find_by_name(name))
        return results

    def find_by_extension(self, ext: str) -> list[File]:
        """Find all files with given extension."""
        results = []
        for child in self._children:
            if isinstance(child, File) and child.name.endswith(ext):
                results.append(child)
            elif isinstance(child, Directory):
                results.extend(child.find_by_extension(ext))
        return results


def format_size(size: int) -> str:
    """Format size in human-readable format."""
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    else:
        return f"{size / (1024 * 1024):.1f} MB"


def main() -> None:
    print("=" * 60)
    print("Composite Pattern - File System Demo")
    print("=" * 60)

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

    # Display the entire structure
    print("\n--- File System Structure ---")
    print(root.display())

    # Calculate sizes uniformly (works for both files and directories)
    print("\n\n--- Size Calculations ---")
    print(f"Total project size: {format_size(root.get_size())}")
    print(f"Source code size: {format_size(src.get_size())}")
    print(f"Documentation size: {format_size(docs.get_size())}")
    print(f"Assets size: {format_size(assets.get_size())}")

    # Count files
    print("\n--- File Counts ---")
    print(f"Total files in project: {root.count_files()}")
    print(f"Source files: {src.count_files()}")
    print(f"Test files: {tests.count_files()}")

    # Search operations
    print("\n--- Search Operations ---")
    py_files = root.find_by_extension(".py")
    print(f"\nPython files ({len(py_files)}):")
    for f in py_files:
        print(f"  - {f.get_path()}")

    md_files = root.find_by_extension(".md")
    print(f"\nMarkdown files ({len(md_files)}):")
    for f in md_files:
        print(f"  - {f.get_path()}")

    # Demonstrate uniform treatment
    print("\n--- Uniform Treatment Demo ---")

    def print_info(component: FileSystemComponent) -> None:
        """Works with both files and directories."""
        print(f"Name: {component.name}")
        print(f"Path: {component.get_path()}")
        print(f"Size: {format_size(component.get_size())}")
        print(f"Is composite: {component.is_composite()}")
        print()

    print("\nFor a file:")
    print_info(src.get_children()[0])

    print("For a directory:")
    print_info(src)

    print("\n" + "=" * 60)
    print("Benefits of Composite Pattern:")
    print("=" * 60)
    print("1. Simplifies client code - treats all objects uniformly")
    print("2. Easy to add new component types")
    print("3. Natural representation of hierarchical structures")
    print("4. Recursive composition allows complex structures")


if __name__ == "__main__":
    main()
