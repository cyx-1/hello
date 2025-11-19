# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Flyweight Pattern

The Flyweight pattern uses sharing to support large numbers of fine-grained
objects efficiently. It reduces memory usage by sharing common parts of object
state among multiple objects.

Key Components:
- Flyweight: Interface for flyweight objects
- ConcreteFlyweight: Implements Flyweight with intrinsic state (shared)
- FlyweightFactory: Creates and manages flyweight objects
- Client: Maintains extrinsic state (unique per context)
"""

from typing import Any
import sys


# Flyweight interface and implementation
class TreeType:
    """
    Flyweight class storing intrinsic state (shared across all trees).
    Intrinsic state: name, color, texture (same for all trees of this type)
    """

    def __init__(self, name: str, color: str, texture: str):
        self._name = name
        self._color = color
        self._texture = texture

    @property
    def name(self) -> str:
        return self._name

    def draw(self, x: int, y: int) -> str:
        """
        Draw tree with extrinsic state (x, y) provided by client.
        Extrinsic state: position (unique for each tree instance)
        """
        return f"Drawing {self._name} tree at ({x}, {y}) with {self._color} leaves and {self._texture} bark"


# Flyweight Factory
class TreeFactory:
    """Factory that manages flyweight TreeType objects."""

    _tree_types: dict[str, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        """
        Return existing flyweight or create new one if doesn't exist.
        This ensures only one TreeType exists per unique combination.
        """
        key = f"{name}_{color}_{texture}"
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
            print(f"  [Factory] Created new TreeType: {name}")
        return cls._tree_types[key]

    @classmethod
    def get_type_count(cls) -> int:
        """Return number of unique tree types."""
        return len(cls._tree_types)

    @classmethod
    def list_types(cls) -> list[str]:
        """List all tree types."""
        return list(cls._tree_types.keys())


# Context class that uses flyweight
class Tree:
    """
    Context class containing extrinsic state (x, y) and reference to flyweight.
    Each Tree has a unique position but shares the TreeType flyweight.
    """

    def __init__(self, x: int, y: int, tree_type: TreeType):
        self._x = x
        self._y = y
        self._tree_type = tree_type  # Reference to shared flyweight

    def draw(self) -> str:
        """Draw tree using flyweight's intrinsic state and own extrinsic state."""
        return self._tree_type.draw(self._x, self._y)


# Client: Forest that manages many trees
class Forest:
    """Client that creates and manages many Tree objects."""

    def __init__(self):
        self._trees: list[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        """Plant a tree, reusing TreeType flyweights."""
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self._trees.append(tree)

    def draw(self) -> list[str]:
        """Draw all trees in forest."""
        return [tree.draw() for tree in self._trees]

    def get_tree_count(self) -> int:
        """Return total number of trees."""
        return len(self._trees)


# Character flyweight example (text editor)
class CharacterStyle:
    """Flyweight for text character styling."""

    def __init__(self, font: str, size: int, bold: bool, italic: bool):
        self.font = font
        self.size = size
        self.bold = bold
        self.italic = italic

    def render(self, char: str, position: int) -> str:
        style = []
        if self.bold:
            style.append("B")
        if self.italic:
            style.append("I")
        style_str = "+".join(style) if style else "normal"
        return f"'{char}' at {position}: {self.font} {self.size}pt ({style_str})"


class StyleFactory:
    """Factory for character style flyweights."""

    _styles: dict[str, CharacterStyle] = {}

    @classmethod
    def get_style(cls, font: str, size: int, bold: bool, italic: bool) -> CharacterStyle:
        key = f"{font}_{size}_{bold}_{italic}"
        if key not in cls._styles:
            cls._styles[key] = CharacterStyle(font, size, bold, italic)
        return cls._styles[key]

    @classmethod
    def get_style_count(cls) -> int:
        return len(cls._styles)


class Character:
    """A character with extrinsic state (char, position) and shared style."""

    def __init__(self, char: str, position: int, style: CharacterStyle):
        self.char = char
        self.position = position
        self.style = style

    def render(self) -> str:
        return self.style.render(self.char, self.position)


class TextDocument:
    """Document that stores characters efficiently using flyweight."""

    def __init__(self):
        self._characters: list[Character] = []

    def add_character(
        self, char: str, font: str, size: int, bold: bool = False, italic: bool = False
    ) -> None:
        position = len(self._characters)
        style = StyleFactory.get_style(font, size, bold, italic)
        self._characters.append(Character(char, position, style))

    def render(self) -> list[str]:
        return [char.render() for char in self._characters]

    def get_char_count(self) -> int:
        return len(self._characters)


def estimate_memory_usage(obj: Any, seen: set | None = None) -> int:
    """Roughly estimate memory usage of an object."""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum(
            estimate_memory_usage(v, seen) for v in obj.values()
        )
        size += sum(
            estimate_memory_usage(k, seen) for k in obj.keys()
        )
    elif hasattr(obj, "__dict__"):
        size += estimate_memory_usage(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(estimate_memory_usage(i, seen) for i in obj)

    return size


def main() -> None:
    print("=" * 60)
    print("Flyweight Pattern - Forest Simulation Demo")
    print("=" * 60)

    # Demo 1: Forest with many trees
    print("\n--- Planting Forest ---")
    forest = Forest()

    # Plant many trees of different types
    tree_configs = [
        ("Oak", "Green", "Rough"),
        ("Pine", "Dark Green", "Scaly"),
        ("Maple", "Red", "Smooth"),
        ("Birch", "Yellow", "White"),
    ]

    # Plant 100 trees but only use 4 tree types
    import random

    random.seed(42)

    for i in range(100):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        config = random.choice(tree_configs)
        forest.plant_tree(x, y, *config)

    print(f"\nTotal trees planted: {forest.get_tree_count()}")
    print(f"Unique tree types (flyweights): {TreeFactory.get_type_count()}")

    # Show first few trees
    print("\nFirst 5 trees:")
    for line in forest.draw()[:5]:
        print(f"  {line}")

    # Demo 2: Memory savings illustration
    print("\n--- Memory Savings ---")
    print(f"Without flyweight: {forest.get_tree_count()} tree type objects")
    print(f"With flyweight: {TreeFactory.get_type_count()} tree type objects")
    print(f"Memory reduction: {100 * (1 - TreeFactory.get_type_count() / forest.get_tree_count()):.1f}%")

    # Demo 3: Text document with character flyweights
    print("\n--- Text Document Demo ---")
    doc = TextDocument()

    # Add characters with different styles
    text = "Hello World"
    for i, char in enumerate(text):
        if i < 5:  # "Hello" in bold
            doc.add_character(char, "Arial", 12, bold=True)
        elif char == " ":
            doc.add_character(char, "Arial", 12)
        else:  # "World" in italic
            doc.add_character(char, "Arial", 12, italic=True)

    print(f"\nTotal characters: {doc.get_char_count()}")
    print(f"Unique styles (flyweights): {StyleFactory.get_style_count()}")

    print("\nRendered characters:")
    for line in doc.render():
        print(f"  {line}")

    # Demo 4: Show flyweight reuse
    print("\n--- Flyweight Reuse Demo ---")

    # Add more characters with existing styles
    for char in "!!!":
        doc.add_character(char, "Arial", 12, bold=True)  # Reuses existing style

    print(f"Characters after adding '!!!': {doc.get_char_count()}")
    print(f"Styles still: {StyleFactory.get_style_count()} (reused existing)")

    # Demo 5: Large scale demonstration
    print("\n--- Large Scale Demo ---")
    large_forest = Forest()

    # Plant 1000 trees with only 4 types
    for _ in range(1000):
        x = random.randint(0, 10000)
        y = random.randint(0, 10000)
        config = random.choice(tree_configs)
        large_forest.plant_tree(x, y, *config)

    print(f"Trees in large forest: {large_forest.get_tree_count()}")
    print(f"Tree types used: {TreeFactory.get_type_count()}")
    print(f"Objects saved: {large_forest.get_tree_count() - TreeFactory.get_type_count()}")

    print("\n" + "=" * 60)
    print("Benefits of Flyweight Pattern:")
    print("=" * 60)
    print("1. Reduces memory usage by sharing common state")
    print("2. Improves performance with many similar objects")
    print("3. Separates intrinsic (shared) from extrinsic (unique) state")
    print("4. Flyweight objects must be immutable")
    print("5. Factory ensures proper sharing and object management")


if __name__ == "__main__":
    main()
