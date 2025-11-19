# Flyweight Pattern

The Flyweight pattern uses sharing to support large numbers of fine-grained objects efficiently by separating intrinsic (shared) and extrinsic (unique) state.

## How to Run

```bash
cd java/flyweight
mvn compile exec:java
```

## Key Source Code

### Flyweight with Intrinsic State (Lines 16-31)
```java
class TreeTypeImpl implements TreeType {
    private String name;    // Intrinsic - shared
    private String color;   // Intrinsic - shared
    private String texture; // Intrinsic - shared

    @Override
    public void draw(int x, int y) {  // x, y are extrinsic
        System.out.println("Drawing " + name + " at (" + x + ", " + y + ")");
    }
}
```

### Flyweight Factory (Lines 34-49)
```java
class TreeFactory {
    private static Map<String, TreeType> treeTypes = new HashMap<>();

    public static TreeType getTreeType(String name, String color, String texture) {
        String key = name + "_" + color + "_" + texture;
        TreeType result = treeTypes.get(key);

        if (result == null) {
            result = new TreeTypeImpl(name, color, texture);
            treeTypes.put(key, result);
        }
        return result;
    }
}
```

### Context with Extrinsic State (Lines 52-65)
```java
class Tree {
    private int x;           // Extrinsic - unique
    private int y;           // Extrinsic - unique
    private TreeType type;   // Reference to flyweight

    public void draw() {
        type.draw(x, y);
    }
}
```

## Program Output

```
=== Flyweight Pattern Demonstration ===

--- 1. Forest with Shared Tree Types ---
Creating tree types (flyweights):

  Creating TreeType: Oak (this is shared)
  Creating TreeType: Pine (this is shared)
  Creating TreeType: Birch (this is shared)

Drawing forest:

    Drawing Oak tree at (10, 20) with color Green
    Drawing Pine tree at (50, 30) with color Dark Green
    Drawing Oak tree at (100, 40) with color Green
    Drawing Birch tree at (150, 50) with color Light Green
    Drawing Pine tree at (200, 60) with color Dark Green
    Drawing Oak tree at (250, 70) with color Green

Statistics:
  Total trees: 6
  Unique tree types (flyweights): 3
  Memory saved: 3 objects

--- 3. Game Particle System ---
Loading particle types:

  Loading particle sprite: spark (yellow)
  Loading particle sprite: spark (orange)
  Loading particle sprite: smoke (gray)

Statistics:
  Total particles: 5
  Unique particle types: 3
```

## Pattern Benefits

1. **Memory Efficiency**: Share common state among objects
2. **Performance**: Reduce object creation overhead
3. **Scalability**: Support large numbers of objects

## Key Concepts

- **Intrinsic State**: Shared, immutable (stored in flyweight)
- **Extrinsic State**: Unique, varies (passed to methods)

## Requirements

- Java 17 or higher
- Maven 3.x
