# Visitor Pattern

The Visitor pattern lets you define a new operation without changing the classes of the elements on which it operates. It separates algorithms from the object structure they operate on.

## Key Components

- **Visitor**: Declares visit operations for each ConcreteElement
- **ConcreteVisitor**: Implements operations for each element type
- **Element**: Declares accept method that takes a Visitor
- **ConcreteElement**: Implements accept to call appropriate visit method
- **ObjectStructure**: Collection of elements that can be iterated

## Key Source Code

### Visitor Interface

```python:main_visitor.py startLine=28 endLine=46
class ShapeVisitor(ABC):
    """Abstract visitor for shape operations."""

    @abstractmethod
    def visit_circle(self, circle: "Circle") -> str:
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle") -> str:
        pass

    @abstractmethod
    def visit_triangle(self, triangle: "Triangle") -> str:
        pass

    @abstractmethod
    def visit_compound(self, compound: "CompoundShape") -> str:
        pass
```

### Element Interface and Concrete Elements

```python:main_visitor.py startLine=48 endLine=81
# Element interface
class Shape(ABC):
    """Abstract element that can accept a visitor."""

    @abstractmethod
    def accept(self, visitor: ShapeVisitor) -> str:
        pass


# Concrete Elements
class Circle(Shape):
    """Concrete element: Circle."""

    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.radius = radius

    def accept(self, visitor: ShapeVisitor) -> str:
        return visitor.visit_circle(self)


class Rectangle(Shape):
    """Concrete element: Rectangle."""

    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def accept(self, visitor: ShapeVisitor) -> str:
        return visitor.visit_rectangle(self)
```

### Concrete Visitors (Different Operations)

```python:main_visitor.py startLine=115 endLine=145
class AreaCalculator(ShapeVisitor):
    """Visitor that calculates area of shapes."""

    def visit_circle(self, circle: Circle) -> str:
        import math

        area = math.pi * circle.radius**2
        return f"Circle area: {area:.2f}"

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        area = rectangle.width * rectangle.height
        return f"Rectangle area: {area:.2f}"

    def visit_triangle(self, triangle: Triangle) -> str:
        # Using shoelace formula
        area = abs(
            (triangle.x1 * (triangle.y2 - triangle.y3))
            + (triangle.x2 * (triangle.y3 - triangle.y1))
            + (triangle.x3 * (triangle.y1 - triangle.y2))
        ) / 2
        return f"Triangle area: {area:.2f}"

    def visit_compound(self, compound: CompoundShape) -> str:
        total = 0.0
        for shape in compound.get_shapes():
            result = shape.accept(self)
            # Extract number from result string
            value = float(result.split(": ")[1])
            total += value
        return f"Compound '{compound.name}' total area: {total:.2f}"
```

```python:main_visitor.py startLine=210 endLine=237
class XMLExporter(ShapeVisitor):
    """Visitor that exports shapes to XML."""

    def visit_circle(self, circle: Circle) -> str:
        return (
            f'<circle x="{circle.x}" y="{circle.y}" radius="{circle.radius}"/>'
        )

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return (
            f'<rectangle x="{rectangle.x}" y="{rectangle.y}" '
            f'width="{rectangle.width}" height="{rectangle.height}"/>'
        )

    def visit_triangle(self, triangle: Triangle) -> str:
        return (
            f'<triangle x1="{triangle.x1}" y1="{triangle.y1}" '
            f'x2="{triangle.x2}" y2="{triangle.y2}" '
            f'x3="{triangle.x3}" y3="{triangle.y3}"/>'
        )

    def visit_compound(self, compound: CompoundShape) -> str:
        lines = [f'<compound name="{compound.name}">']
        for shape in compound.get_shapes():
            lines.append(f"  {shape.accept(self)}")
        lines.append("</compound>")
        return "\n".join(lines)
```

### Object Structure

```python:main_visitor.py startLine=272 endLine=284
class Drawing:
    """Collection of shapes that can be visited."""

    def __init__(self):
        self._shapes: list[Shape] = []

    def add(self, shape: Shape) -> None:
        self._shapes.append(shape)

    def apply(self, visitor: ShapeVisitor) -> list[str]:
        """Apply visitor to all shapes."""
        return [shape.accept(visitor) for shape in self._shapes]
```

## Program Output

```
============================================================
Visitor Pattern - Shape Operations Demo
============================================================

--- Area Calculator Visitor ---
  Circle area: 78.54
  Rectangle area: 200.00
  Triangle area: 40.00
  Compound 'House' total area: 412.57

--- Perimeter Calculator Visitor ---
  Circle perimeter: 31.42
  Rectangle perimeter: 60.00
  Triangle perimeter: 28.87
  Compound 'House' total perimeter: 130.85

--- Drawing Visitor ---
  Draw circle at (10, 10) with radius 5
  Draw rectangle at (0, 0) with size 10x20
  Draw triangle: (0, 0) -> (10, 0) -> (5, 8)
  Begin compound 'House'
  Draw rectangle at (10, 0) with size 20x15
  Draw triangle: (10, 15) -> (30, 15) -> (20, 25)
  Draw circle at (20, 8) with radius 2
End compound 'House'

--- XML Export Visitor ---
<shapes>
  <circle x="10" y="10" radius="5"/>
  <rectangle x="0" y="0" width="10" height="20"/>
  <triangle x1="0" y1="0" x2="10" y2="0" x3="5" y3="8"/>
  <compound name="House">
    <rectangle x="10" y="0" width="20" height="15"/>
    <triangle x1="10" y1="15" x2="30" y2="15" x3="20" y3="25"/>
    <circle x="20" y="8" radius="2"/>
  </compound>
</shapes>

--- JSON Export Visitor ---
[
  {"type": "circle", "x": 10, "y": 10, "radius": 5},
  {"type": "rectangle", "x": 0, "y": 0, "width": 10, "height": 20},
  {"type": "triangle", "points": [[0, 0], [10, 0], [5, 8]]},
  {"type": "compound", "name": "House", "shapes": [{"type": "rectangle", "x": 10, "y": 0, "width": 20, "height": 15}, {"type": "triangle", "points": [[10, 15], [30, 15], [20, 25]]}, {"type": "circle", "x": 20, "y": 8, "radius": 2}]}
]

--- Multiple Visitors on Single Shape ---
Rectangle (15x10):
  Rectangle area: 150.00
  Rectangle perimeter: 50.00
  Draw rectangle at (0, 0) with size 15x10

============================================================
Benefits of Visitor Pattern:
============================================================
1. Adds operations without modifying element classes
2. Related operations grouped in visitor class
3. Can accumulate state while visiting elements
4. Works well with Composite pattern
5. Follows Single Responsibility Principle
```

## Output Annotations

- **Lines 5-9**: AreaCalculator visitor calculates area for each shape type - circle uses pi*r^2 (lines 118-122), rectangle uses w*h (lines 124-126), compound aggregates child areas (lines 137-144)
- **Lines 11-15**: PerimeterCalculator demonstrates another visitor with different logic - circle uses 2*pi*r (lines 150-154), triangle calculates all three sides (lines 160-173)
- **Lines 17-24**: DrawingVisitor generates drawing commands - shows how same element structure produces completely different output with different visitor (lines 184-207)
- **Lines 26-35**: XMLExporter outputs XML format - each visit method produces appropriate XML tag (lines 210-237), compound shapes nest child elements
- **Lines 37-43**: JSONExporter produces JSON format - demonstrates how easy it is to add new operations without modifying Shape classes (lines 239-268)
- **Lines 45-49**: Single shape with multiple visitors shows the pattern's flexibility - same Rectangle accepts three different visitors producing area, perimeter, and draw commands

## Requirements

- Python 3.10+ (uses type hints with `list[Shape]`)

## Running the Example

```bash
uv run python main_visitor.py
```
