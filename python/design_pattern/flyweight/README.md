# Flyweight Pattern

The Flyweight pattern uses sharing to support large numbers of fine-grained objects efficiently. It reduces memory usage by sharing common parts of object state (intrinsic state) among multiple objects, while keeping unique state (extrinsic state) external.

**Requires Python 3.10+** (uses union types with `|` syntax)

## Key Components

- **Flyweight** (`TreeType`, `CharacterStyle`): Stores intrinsic state that can be shared
- **FlyweightFactory** (`TreeFactory`, `StyleFactory`): Creates and manages flyweight objects
- **Context** (`Tree`, `Character`): Maintains extrinsic state unique to each instance
- **Client** (`Forest`, `TextDocument`): Uses flyweights through the factory

## Source Code

### Flyweight Class (Intrinsic State)

```python:main_flyweight.py startLine=23 endLine=45
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
```

### Flyweight Factory

```python:main_flyweight.py startLine=47 endLine=73
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
```

### Context Class (Extrinsic State)

```python:main_flyweight.py startLine=76 endLine=91
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
```

### Client Usage

```python:main_flyweight.py startLine=226 endLine=238
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
```

## Program Output

```
============================================================
Flyweight Pattern - Forest Simulation Demo
============================================================

--- Planting Forest ---
  [Factory] Created new TreeType: Oak
  [Factory] Created new TreeType: Pine
  [Factory] Created new TreeType: Birch
  [Factory] Created new TreeType: Maple

Total trees planted: 100
Unique tree types (flyweights): 4

First 5 trees:
  Drawing Oak tree at (654, 114) with Green leaves and Rough bark
  Drawing Pine tree at (759, 281) with Dark Green leaves and Scaly bark
  Drawing Oak tree at (228, 142) with Green leaves and Rough bark
  Drawing Oak tree at (692, 758) with Green leaves and Rough bark
  Drawing Oak tree at (604, 432) with Green leaves and Rough bark

--- Memory Savings ---
Without flyweight: 100 tree type objects
With flyweight: 4 tree type objects
Memory reduction: 96.0%

--- Text Document Demo ---

Total characters: 11
Unique styles (flyweights): 3

Rendered characters:
  'H' at 0: Arial 12pt (B)
  'e' at 1: Arial 12pt (B)
  'l' at 2: Arial 12pt (B)
  'l' at 3: Arial 12pt (B)
  'o' at 4: Arial 12pt (B)
  ' ' at 5: Arial 12pt (normal)
  'W' at 6: Arial 12pt (I)
  'o' at 7: Arial 12pt (I)
  'r' at 8: Arial 12pt (I)
  'l' at 9: Arial 12pt (I)
  'd' at 10: Arial 12pt (I)

--- Flyweight Reuse Demo ---
Characters after adding '!!!': 14
Styles still: 3 (reused existing)

--- Large Scale Demo ---
Trees in large forest: 1000
Tree types used: 4
Objects saved: 996

============================================================
Benefits of Flyweight Pattern:
============================================================
1. Reduces memory usage by sharing common state
2. Improves performance with many similar objects
3. Separates intrinsic (shared) from extrinsic (unique) state
4. Flyweight objects must be immutable
5. Factory ensures proper sharing and object management
```

## Annotations

### Factory Creation (Lines 54-63)
The `get_tree_type()` method checks if a TreeType with the given properties already exists. Output shows only 4 tree types being created despite planting 100 trees. The factory ensures each unique combination is created only once.

### Memory Savings (Lines 246-249)
The output demonstrates the core benefit:
- Without flyweight: 100 separate TreeType objects
- With flyweight: Only 4 shared TreeType objects
- **96% memory reduction**

Each Tree object stores only its unique position (x, y) plus a reference to the shared TreeType.

### Drawing Trees (Lines 39-44)
The `draw()` method combines intrinsic state (name, color, texture from flyweight) with extrinsic state (x, y passed as parameters). Output shows 5 different tree positions but only 4 unique tree types, with multiple Oak trees sharing the same TreeType.

### Text Document Example (Lines 251-270)
The `CharacterStyle` flyweight demonstrates another use case:
- 11 characters created
- Only 3 styles needed (Bold, Normal, Italic)
- Each character stores its own char and position (extrinsic) but shares the style (intrinsic)

### Flyweight Reuse (Lines 276-280)
Adding "!!!" characters reuses the existing Bold style. Output confirms styles remain at 3 despite total characters increasing to 14.

### Large Scale (Lines 283-295)
With 1000 trees but only 4 types, we save 996 TreeType objects. This demonstrates the pattern's scalability - the more objects you have, the greater the memory savings.

## Running the Code

```bash
uv run python main_flyweight.py
```
