#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "PyQt6>=6.6.0",
# ]
# ///
"""
PyQt6 Drag and Drop Shapes Example

This example demonstrates how to create draggable shapes on a canvas
using PyQt6. Users can drag different colored shapes around the canvas.
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush, QPalette


class Shape:
    """Represents a draggable shape on the canvas"""

    def __init__(self, x, y, width, height, color, shape_type):
        self.rect = QRect(x, y, width, height)
        self.color = color
        self.shape_type = shape_type  # 'rectangle', 'circle', 'triangle'
        self.dragging = False
        self.drag_offset = QPoint()

    def contains(self, point):
        """Check if a point is inside the shape"""
        return self.rect.contains(point)

    def draw(self, painter):
        """Draw the shape using the painter"""
        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.setBrush(QBrush(self.color))

        if self.shape_type == "rectangle":
            # Line 47: Draw a filled rectangle
            painter.drawRect(self.rect)
        elif self.shape_type == "circle":
            # Line 50: Draw a filled ellipse (circle)
            painter.drawEllipse(self.rect)
        elif self.shape_type == "triangle":
            # Line 53: Draw a filled triangle using a polygon
            points = [
                QPoint(self.rect.center().x(), self.rect.top()),
                QPoint(self.rect.left(), self.rect.bottom()),
                QPoint(self.rect.right(), self.rect.bottom()),
            ]
            painter.drawPolygon(points)


class Canvas(QWidget):
    """Canvas widget that holds and manages draggable shapes"""

    def __init__(self):
        super().__init__()
        self.shapes = []
        self.selected_shape = None
        self.init_ui()
        self.create_shapes()

    def init_ui(self):
        """Initialize the UI"""
        self.setMinimumSize(800, 600)
        # Line 77: Set white background for the canvas
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.white)
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def create_shapes(self):
        """Create initial shapes on the canvas"""
        # Line 85: Create a red rectangle
        self.shapes.append(Shape(100, 100, 120, 80, QColor(255, 100, 100), "rectangle"))
        # Line 89: Create a blue circle
        self.shapes.append(Shape(300, 150, 100, 100, QColor(100, 150, 255), "circle"))
        # Line 93: Create a green triangle
        self.shapes.append(Shape(500, 120, 100, 100, QColor(100, 255, 150), "triangle"))
        # Line 97: Create a yellow rectangle
        self.shapes.append(Shape(150, 300, 100, 60, QColor(255, 255, 100), "rectangle"))
        # Line 101: Create a purple circle
        self.shapes.append(Shape(400, 350, 90, 90, QColor(200, 100, 255), "circle"))

    def paintEvent(self, event):
        """Paint all shapes on the canvas"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Line 111: Draw all shapes in reverse order (last added = top layer)
        for shape in reversed(self.shapes):
            shape.draw(painter)

    def mousePressEvent(self, event):
        """Handle mouse press events to start dragging"""
        if event.button() == Qt.MouseButton.LeftButton:
            # Line 118: Check shapes in reverse order (top to bottom)
            for shape in reversed(self.shapes):
                if shape.contains(event.pos()):
                    # Line 121: Shape found - prepare for dragging
                    self.selected_shape = shape
                    shape.dragging = True
                    # Line 124: Calculate offset between mouse and shape origin
                    shape.drag_offset = event.pos() - shape.rect.topLeft()
                    # Line 126: Move shape to end of list (bring to front)
                    self.shapes.remove(shape)
                    self.shapes.append(shape)
                    break

    def mouseMoveEvent(self, event):
        """Handle mouse move events to drag the shape"""
        if self.selected_shape and self.selected_shape.dragging:
            # Line 134: Calculate new position maintaining the drag offset
            new_pos = event.pos() - self.selected_shape.drag_offset
            # Line 136: Update the shape's rectangle position
            self.selected_shape.rect.moveTopLeft(new_pos)
            # Line 138: Trigger a repaint to show the shape at new position
            self.update()

    def mouseReleaseEvent(self, event):
        """Handle mouse release events to stop dragging"""
        if event.button() == Qt.MouseButton.LeftButton:
            if self.selected_shape:
                # Line 145: Stop dragging the shape
                self.selected_shape.dragging = False
                self.selected_shape = None


class MainWindow(QMainWindow):
    """Main application window"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the main window UI"""
        # Line 160: Set window title
        self.setWindowTitle("PyQt6 Drag and Drop Shapes")
        self.setGeometry(100, 100, 800, 600)

        # Line 164: Create and set the canvas as central widget
        canvas = Canvas()
        self.setCentralWidget(canvas)


def main():
    """Main entry point"""
    # Line 171: Create the application instance
    app = QApplication(sys.argv)

    # Line 174: Create and show the main window
    window = MainWindow()
    window.show()

    # Line 178: Start the event loop
    print("PyQt6 Drag and Drop Shapes Demo")
    print("=" * 40)
    print("Instructions:")
    print("  - Click and drag any shape to move it")
    print("  - Shapes can overlap")
    print("  - Dragged shapes are brought to the front")
    print("=" * 40)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
