# PyQt6 Drag and Drop Shapes Example

This example demonstrates how to create an interactive canvas with draggable shapes using PyQt6. The application showcases three different shape types (rectangles, circles, and triangles) that can be freely dragged around the canvas.

## Running the Example

```bash
uv run python main_pyqt6_drag_drop.py
```

## Features

- **Multiple Shape Types**: Rectangles, circles (ellipses), and triangles
- **Drag and Drop**: Click and drag any shape to move it around the canvas
- **Z-Order Management**: Dragged shapes automatically come to the front
- **Visual Feedback**: Smooth anti-aliased rendering with colored shapes

## Source Code Highlights

### Shape Class Definition (Lines 21-53)

```python
21→class Shape:
22→    """Represents a draggable shape on the canvas"""
23→
24→    def __init__(self, x, y, width, height, color, shape_type):
25→        self.rect = QRect(x, y, width, height)
26→        self.color = color
27→        self.shape_type = shape_type  # 'rectangle', 'circle', 'triangle'
28→        self.dragging = False
29→        self.drag_offset = QPoint()
```

**Line 24-29**: Each shape stores its position (`QRect`), color, type, and dragging state. The `drag_offset` tracks where the user clicked relative to the shape's origin, ensuring smooth dragging without the shape "jumping" to the cursor position.

### Drawing Different Shape Types (Lines 35-53)

```python
35→    def draw(self, painter):
36→        """Draw the shape using the painter"""
37→        painter.setPen(QPen(Qt.GlobalColor.black, 2))
38→        painter.setBrush(QBrush(self.color))
39→
40→        if self.shape_type == "rectangle":
41→            # Draw a filled rectangle
42→            painter.drawRect(self.rect)
43→        elif self.shape_type == "circle":
44→            # Draw a filled ellipse (circle)
45→            painter.drawEllipse(self.rect)
46→        elif self.shape_type == "triangle":
47→            # Draw a filled triangle using a polygon
48→            points = [
49→                QPoint(self.rect.center().x(), self.rect.top()),
50→                QPoint(self.rect.left(), self.rect.bottom()),
51→                QPoint(self.rect.right(), self.rect.bottom()),
52→            ]
53→            painter.drawPolygon(points)
```

**Line 40-42**: Rectangles are drawn using `drawRect()` with the shape's bounding rectangle.

**Line 43-45**: Circles are drawn using `drawEllipse()`, which creates an ellipse inscribed in the rectangle.

**Line 46-53**: Triangles are drawn as polygons with three points: top center, bottom left, and bottom right of the bounding rectangle.

### Creating Initial Shapes (Lines 75-86)

```python
75→    def create_shapes(self):
76→        """Create initial shapes on the canvas"""
77→        # Create a red rectangle
78→        self.shapes.append(Shape(100, 100, 120, 80, QColor(255, 100, 100), "rectangle"))
79→        # Create a blue circle
80→        self.shapes.append(Shape(300, 150, 100, 100, QColor(100, 150, 255), "circle"))
81→        # Create a green triangle
82→        self.shapes.append(Shape(500, 120, 100, 100, QColor(100, 255, 150), "triangle"))
83→        # Create a yellow rectangle
84→        self.shapes.append(Shape(150, 300, 100, 60, QColor(255, 255, 100), "rectangle"))
85→        # Create a purple circle
86→        self.shapes.append(Shape(400, 350, 90, 90, QColor(200, 100, 255), "circle"))
```

**Lines 78-86**: Five shapes are created with different positions, sizes, colors, and types. Each shape is added to the shapes list, which determines the drawing order.

### Mouse Press Event - Starting the Drag (Lines 97-111)

```python
97→    def mousePressEvent(self, event):
98→        """Handle mouse press events to start dragging"""
99→        if event.button() == Qt.MouseButton.LeftButton:
100→            # Check shapes in reverse order (top to bottom)
101→            for shape in reversed(self.shapes):
102→                if shape.contains(event.pos()):
103→                    # Shape found - prepare for dragging
104→                    self.selected_shape = shape
105→                    shape.dragging = True
106→                    # Calculate offset between mouse and shape origin
107→                    shape.drag_offset = event.pos() - shape.rect.topLeft()
108→                    # Move shape to end of list (bring to front)
109→                    self.shapes.remove(shape)
110→                    self.shapes.append(shape)
111→                    break
```

**Line 101**: Shapes are checked in reverse order so that the topmost (most recently drawn) shape is selected first.

**Line 107**: The drag offset is calculated to maintain the relative position between the mouse cursor and the shape's top-left corner during dragging.

**Lines 109-110**: The selected shape is moved to the end of the list, which brings it to the front visually (drawn last = on top).

### Mouse Move Event - Dragging the Shape (Lines 113-121)

```python
113→    def mouseMoveEvent(self, event):
114→        """Handle mouse move events to drag the shape"""
115→        if self.selected_shape and self.selected_shape.dragging:
116→            # Calculate new position maintaining the drag offset
117→            new_pos = event.pos() - self.selected_shape.drag_offset
118→            # Update the shape's rectangle position
119→            self.selected_shape.rect.moveTopLeft(new_pos)
120→            # Trigger a repaint to show the shape at new position
121→            self.update()
```

**Line 117**: The new position is calculated by subtracting the drag offset from the current mouse position, ensuring the shape doesn't "jump" to the cursor.

**Line 119**: The shape's rectangle is moved to the new position.

**Line 121**: `update()` triggers a repaint of the canvas, causing `paintEvent` to be called and the shape to be redrawn at its new location.

### Mouse Release Event - Ending the Drag (Lines 123-129)

```python
123→    def mouseReleaseEvent(self, event):
124→        """Handle mouse release events to stop dragging"""
125→        if event.button() == Qt.MouseButton.LeftButton:
126→            if self.selected_shape:
127→                # Stop dragging the shape
128→                self.selected_shape.dragging = False
129→                self.selected_shape = None
```

**Lines 128-129**: When the mouse button is released, the dragging state is cleared and the shape is deselected.

### Paint Event - Rendering the Canvas (Lines 88-95)

```python
88→    def paintEvent(self, event):
89→        """Paint all shapes on the canvas"""
90→        painter = QPainter(self)
91→        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
92→
93→        # Draw all shapes in reverse order (last added = top layer)
94→        for shape in reversed(self.shapes):
95→            shape.draw(painter)
```

**Line 91**: Antialiasing is enabled for smoother shape edges.

**Line 94**: Shapes are drawn in reverse order. Since shapes at the end of the list should appear on top, reversing the list ensures correct z-ordering (shapes added last are drawn last and appear on top).

## Program Output

When you run the program, you'll see:

```
PyQt6 Drag and Drop Shapes Demo
========================================
Instructions:
  - Click and drag any shape to move it
  - Shapes can overlap
  - Dragged shapes are brought to the front
========================================
```

### Visual Output

The application window displays:

1. **Red rectangle** at position (100, 100) - size 120x80
2. **Blue circle** at position (300, 150) - size 100x100
3. **Green triangle** at position (500, 120) - size 100x100
4. **Yellow rectangle** at position (150, 300) - size 100x60
5. **Purple circle** at position (400, 350) - size 90x90

All shapes have a black 2-pixel border and are filled with their respective colors. The canvas has a white background and is 800x600 pixels.

### Interactive Behavior

- **Click any shape**: The shape becomes selected (brought to front)
- **Drag**: The shape follows your mouse cursor while maintaining the offset from where you clicked
- **Release**: The shape stays at its new position
- **Overlapping**: Shapes can overlap; the most recently dragged shape will be on top

## Key PyQt6 Concepts Demonstrated

1. **Custom Widget**: The `Canvas` class extends `QWidget` to create a custom drawing surface
2. **QPainter**: Used for all drawing operations with anti-aliasing
3. **Mouse Events**: Handling `mousePressEvent`, `mouseMoveEvent`, and `mouseReleaseEvent` for drag-and-drop
4. **Paint Event**: Overriding `paintEvent` to custom-render the widget
5. **Geometry**: Using `QRect`, `QPoint` for position and collision detection
6. **Drawing API**: Using `drawRect`, `drawEllipse`, and `drawPolygon` for different shapes

## Requirements

- **Python**: >= 3.10
- **PyQt6**: >= 6.6.0

The dependencies are specified inline in the script using PEP 723 metadata, so `uv` will automatically install them when you run the script.

## Version Requirements

This example requires **PyQt6 6.6.0 or higher** for the latest API features and stability.
