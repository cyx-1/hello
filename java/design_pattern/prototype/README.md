# Prototype Pattern

The Prototype pattern specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype.

## How to Run

```bash
cd java/prototype
mvn compile exec:java
```

## Key Source Code

### Prototype Interface (Lines 12-14)
```java
interface Prototype extends Cloneable {
    Prototype clone();
}
```

### Deep Copy Constructor (Lines 17-41)
```java
class DocumentPrototype implements Prototype {
    // Copy constructor for deep copy
    public DocumentPrototype(DocumentPrototype source) {
        this.title = source.title;
        this.content = source.content;
        this.author = source.author;
        this.comments = new ArrayList<>(source.comments);      // Deep copy
        this.metadata = new HashMap<>(source.metadata);        // Deep copy
    }

    @Override
    public Prototype clone() {
        return new DocumentPrototype(this);
    }
}
```

### Shape Hierarchy with Clone (Lines 62-128)
```java
abstract class Shape implements Prototype {
    public Shape(Shape source) {
        this.x = source.x;
        this.y = source.y;
        this.color = source.color;
    }

    @Override
    public abstract Prototype clone();
}

class Circle extends Shape {
    public Circle(Circle source) {
        super(source);
        this.radius = source.radius;
    }

    @Override
    public Prototype clone() {
        return new Circle(this);
    }
}
```

### Prototype Registry (Lines 143-174)
```java
class ShapeRegistry {
    private Map<String, Shape> shapes = new HashMap<>();

    public Shape getShape(String key) {
        Shape shape = shapes.get(key);
        if (shape != null) {
            return (Shape) shape.clone();  // Return clone, not original
        }
        return null;
    }

    public void loadDefaults() {
        Circle redCircle = new Circle();
        redCircle.setColor("Red");
        redCircle.setRadius(50);
        addShape("red-circle", redCircle);
        // ...
    }
}
```

### Deep vs Shallow Copy (Lines 222-254)
```java
class Employee implements Prototype {
    // Deep copy constructor
    public Employee(Employee source) {
        this.name = source.name;
        this.department = source.department;
        // Deep copy of nested object
        this.address = source.address != null ? source.address.clone() : null;
        // Deep copy of collection
        this.skills = new ArrayList<>(source.skills);
    }
}
```

## Program Output

```
=== Prototype Pattern Demonstration ===

--- 1. Basic Document Prototype ---
Original: Document[title=Design Patterns Guide, author=John Doe, content=This is a comprehen..., comments=1, metadata={category=Programming, version=1.0}]
Clone: Document[title=Design Patterns Guide - Copy, author=John Doe, content=This is a comprehen..., comments=2, metadata={category=Programming, version=1.1}]
Original unchanged: Document[title=Design Patterns Guide, author=John Doe, content=This is a comprehen..., comments=1, metadata={category=Programming, version=1.0}]

--- 2. Shape Prototypes ---
Original circle:
  Drawing Circle at (10, 20) with radius 25, color: Red
Cloned circle:
  Drawing Circle at (100, 200) with radius 25, color: Blue
Original circle unchanged:
  Drawing Circle at (10, 20) with radius 25, color: Red

--- 3. Using Prototype Registry ---
  Drawing Circle at (50, 50) with radius 50, color: Red
  Drawing Rectangle at (200, 100) with size 100x50, color: Green
  Drawing Triangle at (300, 150) with base 80, height 60, color: Yellow

Multiple clones from blue-circle:
  Drawing Circle at (0, 0) with radius 30, color: Blue
  Drawing Circle at (100, 50) with radius 30, color: Blue
  Drawing Circle at (200, 100) with radius 30, color: Blue

--- 4. Deep Copy with Nested Objects ---
Original Employee: Employee[name=Alice, dept=Engineering, address=123 Main St, New York, USA, skills=[Java, Python]]
Cloned Employee: Employee[name=Bob, dept=Engineering, address=456 Oak Ave, New York, USA, skills=[Java, Python, JavaScript]]
Original unchanged: Employee[name=Alice, dept=Engineering, address=123 Main St, New York, USA, skills=[Java, Python]]

--- 5. Performance Benefit Example ---
Creating complex object from scratch vs cloning:
  Time to clone 1000 objects: 2.5 ms

=== Summary ===
Prototype pattern benefits:
  - Reduces subclassing by cloning
  - Hides complexities of creating new instances
  - Lets you add/remove objects at runtime
  - Specifies new objects by varying values
  - Can be faster than creating new objects

Key considerations:
  - Must implement deep copy for complex objects
  - Cloning objects with circular references is tricky
```

## Output Analysis

| Output Section | Source Code Reference | Explanation |
|----------------|----------------------|-------------|
| Basic Document Clone | Lines 280-293 | Deep copy ensures original unchanged after clone modification |
| Shape Prototypes | Lines 296-310 | Clone inherits all properties, can be modified independently |
| Registry Usage | Lines 314-330 | Get pre-configured prototypes from cache |
| Multiple clones | Lines 332-337 | Same prototype creates multiple instances |
| Deep Copy with Nested | Lines 340-350 | Address object also cloned, not shared |
| Performance | Lines 353-364 | Cloning can be faster than complex construction |

## Pattern Benefits

1. **Reduced Subclassing**: Clone instead of creating subclass for each variation
2. **Dynamic Configuration**: Add/remove prototypes at runtime
3. **Performance**: Cloning can be faster than new object construction
4. **Hidden Complexity**: Client doesn't need to know how to construct objects

## Deep Copy vs Shallow Copy

| Type | Behavior | Use When |
|------|----------|----------|
| Shallow Copy | Copies references to nested objects | Simple objects, immutable fields |
| Deep Copy | Creates new copies of nested objects | Objects with mutable nested references |

## Requirements

- Java 17 or higher
- Maven 3.x
