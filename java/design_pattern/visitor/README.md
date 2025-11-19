# Visitor Pattern

Defines a new operation on elements without changing their classes, separating algorithm from object structure.

## How to Run
```bash
cd java/visitor
mvn compile exec:java
```

## Key Source Code

### Element Interface (Lines 12-14)
```java
interface Shape {
    void accept(ShapeVisitor visitor);
}
```

### Concrete Element (Lines 17-28)
```java
class Circle implements Shape {
    private double radius;

    @Override
    public void accept(ShapeVisitor visitor) {
        visitor.visitCircle(this);
    }
}
```

### Visitor Interface (Lines 52-56)
```java
interface ShapeVisitor {
    void visitCircle(Circle circle);
    void visitRectangle(Rectangle rectangle);
    void visitTriangle(Triangle triangle);
}
```

### Concrete Visitor (Lines 59-73)
```java
class AreaCalculator implements ShapeVisitor {
    private double totalArea = 0;

    @Override
    public void visitCircle(Circle circle) {
        double area = Math.PI * circle.getRadius() * circle.getRadius();
        totalArea += area;
    }
}
```

## Program Output
```
--- 1. Shape Calculations ---
Calculating areas:
  [Area] Circle: 78.54
  [Area] Rectangle: 24.00
  [Area] Triangle: 6.00
  Total area: 108.54

Calculating perimeters:
  [Perimeter] Circle: 31.42
  [Perimeter] Rectangle: 20.00
  [Perimeter] Triangle: 11.00
  Total perimeter: 62.42

--- 2. Document Export ---
Exporting to HTML:
  [HTML] Exported text paragraph
  [HTML] Exported image: chart.png
  [HTML] Exported table: 5x3

Exporting to Markdown:
  [Markdown] Exported text paragraph
  [Markdown] Exported image: chart.png
```

## Pattern Benefits
- Add operations without changing elements
- Gather related operations in one class
- Accumulate state while traversing

## Requirements
- Java 17 or higher
- Maven 3.x
