# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Visitor Pattern

The Visitor pattern lets you define a new operation without changing the
classes of the elements on which it operates. It separates algorithms from
the object structure they operate on.

Key Components:
- Visitor: Declares visit operations for each ConcreteElement
- ConcreteVisitor: Implements operations for each element type
- Element: Declares accept method that takes a Visitor
- ConcreteElement: Implements accept to call appropriate visit method
- ObjectStructure: Collection of elements that can be iterated
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


# Visitor interface
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


class Triangle(Shape):
    """Concrete element: Triangle."""

    def __init__(
        self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
    ):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def accept(self, visitor: ShapeVisitor) -> str:
        return visitor.visit_triangle(self)


class CompoundShape(Shape):
    """Composite element containing multiple shapes."""

    def __init__(self, name: str):
        self.name = name
        self._shapes: list[Shape] = []

    def add(self, shape: Shape) -> None:
        self._shapes.append(shape)

    def get_shapes(self) -> list[Shape]:
        return self._shapes.copy()

    def accept(self, visitor: ShapeVisitor) -> str:
        return visitor.visit_compound(self)


# Concrete Visitors
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


class PerimeterCalculator(ShapeVisitor):
    """Visitor that calculates perimeter of shapes."""

    def visit_circle(self, circle: Circle) -> str:
        import math

        perimeter = 2 * math.pi * circle.radius
        return f"Circle perimeter: {perimeter:.2f}"

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        perimeter = 2 * (rectangle.width + rectangle.height)
        return f"Rectangle perimeter: {perimeter:.2f}"

    def visit_triangle(self, triangle: Triangle) -> str:
        import math

        side1 = math.sqrt(
            (triangle.x2 - triangle.x1) ** 2 + (triangle.y2 - triangle.y1) ** 2
        )
        side2 = math.sqrt(
            (triangle.x3 - triangle.x2) ** 2 + (triangle.y3 - triangle.y2) ** 2
        )
        side3 = math.sqrt(
            (triangle.x1 - triangle.x3) ** 2 + (triangle.y1 - triangle.y3) ** 2
        )
        perimeter = side1 + side2 + side3
        return f"Triangle perimeter: {perimeter:.2f}"

    def visit_compound(self, compound: CompoundShape) -> str:
        total = 0.0
        for shape in compound.get_shapes():
            result = shape.accept(self)
            value = float(result.split(": ")[1])
            total += value
        return f"Compound '{compound.name}' total perimeter: {total:.2f}"


class DrawingVisitor(ShapeVisitor):
    """Visitor that generates drawing commands."""

    def visit_circle(self, circle: Circle) -> str:
        return f"Draw circle at ({circle.x}, {circle.y}) with radius {circle.radius}"

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return (
            f"Draw rectangle at ({rectangle.x}, {rectangle.y}) "
            f"with size {rectangle.width}x{rectangle.height}"
        )

    def visit_triangle(self, triangle: Triangle) -> str:
        return (
            f"Draw triangle: ({triangle.x1}, {triangle.y1}) -> "
            f"({triangle.x2}, {triangle.y2}) -> ({triangle.x3}, {triangle.y3})"
        )

    def visit_compound(self, compound: CompoundShape) -> str:
        commands = [f"Begin compound '{compound.name}'"]
        for shape in compound.get_shapes():
            commands.append(f"  {shape.accept(self)}")
        commands.append(f"End compound '{compound.name}'")
        return "\n".join(commands)


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


class JSONExporter(ShapeVisitor):
    """Visitor that exports shapes to JSON."""

    def visit_circle(self, circle: Circle) -> str:
        return (
            f'{{"type": "circle", "x": {circle.x}, '
            f'"y": {circle.y}, "radius": {circle.radius}}}'
        )

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return (
            f'{{"type": "rectangle", "x": {rectangle.x}, '
            f'"y": {rectangle.y}, "width": {rectangle.width}, '
            f'"height": {rectangle.height}}}'
        )

    def visit_triangle(self, triangle: Triangle) -> str:
        return (
            f'{{"type": "triangle", "points": ['
            f'[{triangle.x1}, {triangle.y1}], '
            f'[{triangle.x2}, {triangle.y2}], '
            f'[{triangle.x3}, {triangle.y3}]]}}'
        )

    def visit_compound(self, compound: CompoundShape) -> str:
        shapes_json = [shape.accept(self) for shape in compound.get_shapes()]
        return (
            f'{{"type": "compound", "name": "{compound.name}", '
            f'"shapes": [{", ".join(shapes_json)}]}}'
        )


# Object Structure
class Drawing:
    """Collection of shapes that can be visited."""

    def __init__(self):
        self._shapes: list[Shape] = []

    def add(self, shape: Shape) -> None:
        self._shapes.append(shape)

    def apply(self, visitor: ShapeVisitor) -> list[str]:
        """Apply visitor to all shapes."""
        return [shape.accept(visitor) for shape in self._shapes]


def main() -> None:
    print("=" * 60)
    print("Visitor Pattern - Shape Operations Demo")
    print("=" * 60)

    # Create shapes
    circle = Circle(10, 10, 5)
    rectangle = Rectangle(0, 0, 10, 20)
    triangle = Triangle(0, 0, 10, 0, 5, 8)

    # Create compound shape
    compound = CompoundShape("House")
    compound.add(Rectangle(10, 0, 20, 15))  # Body
    compound.add(Triangle(10, 15, 30, 15, 20, 25))  # Roof
    compound.add(Circle(20, 8, 2))  # Window

    # Create drawing
    drawing = Drawing()
    drawing.add(circle)
    drawing.add(rectangle)
    drawing.add(triangle)
    drawing.add(compound)

    # Demo 1: Area calculation
    print("\n--- Area Calculator Visitor ---")
    area_calc = AreaCalculator()
    for result in drawing.apply(area_calc):
        print(f"  {result}")

    # Demo 2: Perimeter calculation
    print("\n--- Perimeter Calculator Visitor ---")
    perimeter_calc = PerimeterCalculator()
    for result in drawing.apply(perimeter_calc):
        print(f"  {result}")

    # Demo 3: Drawing commands
    print("\n--- Drawing Visitor ---")
    draw_visitor = DrawingVisitor()
    for result in drawing.apply(draw_visitor):
        print(f"  {result}")

    # Demo 4: XML export
    print("\n--- XML Export Visitor ---")
    xml_exporter = XMLExporter()
    print("<shapes>")
    for result in drawing.apply(xml_exporter):
        for line in result.split("\n"):
            print(f"  {line}")
    print("</shapes>")

    # Demo 5: JSON export
    print("\n--- JSON Export Visitor ---")
    json_exporter = JSONExporter()
    print("[")
    results = drawing.apply(json_exporter)
    for i, result in enumerate(results):
        comma = "," if i < len(results) - 1 else ""
        print(f"  {result}{comma}")
    print("]")

    # Demo 6: Single shape with multiple visitors
    print("\n--- Multiple Visitors on Single Shape ---")
    shape = Rectangle(0, 0, 15, 10)
    print("Rectangle (15x10):")
    print(f"  {shape.accept(area_calc)}")
    print(f"  {shape.accept(perimeter_calc)}")
    print(f"  {shape.accept(draw_visitor)}")

    print("\n" + "=" * 60)
    print("Benefits of Visitor Pattern:")
    print("=" * 60)
    print("1. Adds operations without modifying element classes")
    print("2. Related operations grouped in visitor class")
    print("3. Can accumulate state while visiting elements")
    print("4. Works well with Composite pattern")
    print("5. Follows Single Responsibility Principle")


if __name__ == "__main__":
    main()
