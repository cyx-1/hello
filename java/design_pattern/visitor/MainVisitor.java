/**
 * Comprehensive demonstration of the Visitor Pattern in Java
 *
 * The Visitor pattern represents an operation to be performed on elements of
 * an object structure. It lets you define a new operation without changing
 * the classes of the elements on which it operates.
 */

import java.util.ArrayList;
import java.util.List;

// Element interface
interface Shape {
    void accept(ShapeVisitor visitor);
}

// Concrete Elements
class Circle implements Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() { return radius; }

    @Override
    public void accept(ShapeVisitor visitor) {
        visitor.visitCircle(this);
    }
}

class Rectangle implements Shape {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double getWidth() { return width; }
    public double getHeight() { return height; }

    @Override
    public void accept(ShapeVisitor visitor) {
        visitor.visitRectangle(this);
    }
}

class Triangle implements Shape {
    private double base;
    private double height;

    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }

    public double getBase() { return base; }
    public double getHeight() { return height; }

    @Override
    public void accept(ShapeVisitor visitor) {
        visitor.visitTriangle(this);
    }
}

// Visitor interface
interface ShapeVisitor {
    void visitCircle(Circle circle);
    void visitRectangle(Rectangle rectangle);
    void visitTriangle(Triangle triangle);
}

// Concrete Visitors
class AreaCalculator implements ShapeVisitor {
    private double totalArea = 0;

    @Override
    public void visitCircle(Circle circle) {
        double area = Math.PI * circle.getRadius() * circle.getRadius();
        totalArea += area;
        System.out.println("  [Area] Circle: " + String.format("%.2f", area));
    }

    @Override
    public void visitRectangle(Rectangle rectangle) {
        double area = rectangle.getWidth() * rectangle.getHeight();
        totalArea += area;
        System.out.println("  [Area] Rectangle: " + String.format("%.2f", area));
    }

    @Override
    public void visitTriangle(Triangle triangle) {
        double area = 0.5 * triangle.getBase() * triangle.getHeight();
        totalArea += area;
        System.out.println("  [Area] Triangle: " + String.format("%.2f", area));
    }

    public double getTotalArea() { return totalArea; }
}

class PerimeterCalculator implements ShapeVisitor {
    private double totalPerimeter = 0;

    @Override
    public void visitCircle(Circle circle) {
        double perimeter = 2 * Math.PI * circle.getRadius();
        totalPerimeter += perimeter;
        System.out.println("  [Perimeter] Circle: " + String.format("%.2f", perimeter));
    }

    @Override
    public void visitRectangle(Rectangle rectangle) {
        double perimeter = 2 * (rectangle.getWidth() + rectangle.getHeight());
        totalPerimeter += perimeter;
        System.out.println("  [Perimeter] Rectangle: " + String.format("%.2f", perimeter));
    }

    @Override
    public void visitTriangle(Triangle triangle) {
        // Simplified: assuming isosceles triangle
        double side = Math.sqrt(Math.pow(triangle.getBase()/2, 2) + Math.pow(triangle.getHeight(), 2));
        double perimeter = triangle.getBase() + 2 * side;
        totalPerimeter += perimeter;
        System.out.println("  [Perimeter] Triangle: " + String.format("%.2f", perimeter));
    }

    public double getTotalPerimeter() { return totalPerimeter; }
}

class DrawingVisitor implements ShapeVisitor {
    @Override
    public void visitCircle(Circle circle) {
        System.out.println("  [Draw] Drawing circle with radius " + circle.getRadius());
    }

    @Override
    public void visitRectangle(Rectangle rectangle) {
        System.out.println("  [Draw] Drawing rectangle " + rectangle.getWidth() + "x" + rectangle.getHeight());
    }

    @Override
    public void visitTriangle(Triangle triangle) {
        System.out.println("  [Draw] Drawing triangle with base " + triangle.getBase());
    }
}

// Document element example

interface DocumentElement {
    void accept(DocumentVisitor visitor);
}

class TextElement implements DocumentElement {
    private String text;

    public TextElement(String text) {
        this.text = text;
    }

    public String getText() { return text; }

    @Override
    public void accept(DocumentVisitor visitor) {
        visitor.visitText(this);
    }
}

class ImageElement implements DocumentElement {
    private String filename;
    private int width;
    private int height;

    public ImageElement(String filename, int width, int height) {
        this.filename = filename;
        this.width = width;
        this.height = height;
    }

    public String getFilename() { return filename; }
    public int getWidth() { return width; }
    public int getHeight() { return height; }

    @Override
    public void accept(DocumentVisitor visitor) {
        visitor.visitImage(this);
    }
}

class TableElement implements DocumentElement {
    private int rows;
    private int cols;

    public TableElement(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
    }

    public int getRows() { return rows; }
    public int getCols() { return cols; }

    @Override
    public void accept(DocumentVisitor visitor) {
        visitor.visitTable(this);
    }
}

interface DocumentVisitor {
    void visitText(TextElement text);
    void visitImage(ImageElement image);
    void visitTable(TableElement table);
}

class HTMLExportVisitor implements DocumentVisitor {
    private StringBuilder html = new StringBuilder();

    @Override
    public void visitText(TextElement text) {
        html.append("  <p>").append(text.getText()).append("</p>\n");
        System.out.println("  [HTML] Exported text paragraph");
    }

    @Override
    public void visitImage(ImageElement image) {
        html.append("  <img src=\"").append(image.getFilename())
            .append("\" width=\"").append(image.getWidth())
            .append("\" height=\"").append(image.getHeight()).append("\" />\n");
        System.out.println("  [HTML] Exported image: " + image.getFilename());
    }

    @Override
    public void visitTable(TableElement table) {
        html.append("  <table><!-- ").append(table.getRows())
            .append("x").append(table.getCols()).append(" --></table>\n");
        System.out.println("  [HTML] Exported table: " + table.getRows() + "x" + table.getCols());
    }

    public String getHTML() { return html.toString(); }
}

class MarkdownExportVisitor implements DocumentVisitor {
    private StringBuilder md = new StringBuilder();

    @Override
    public void visitText(TextElement text) {
        md.append(text.getText()).append("\n\n");
        System.out.println("  [Markdown] Exported text paragraph");
    }

    @Override
    public void visitImage(ImageElement image) {
        md.append("![").append(image.getFilename()).append("](")
          .append(image.getFilename()).append(")\n\n");
        System.out.println("  [Markdown] Exported image: " + image.getFilename());
    }

    @Override
    public void visitTable(TableElement table) {
        md.append("| Table ").append(table.getRows()).append("x")
          .append(table.getCols()).append(" |\n");
        System.out.println("  [Markdown] Exported table: " + table.getRows() + "x" + table.getCols());
    }

    public String getMarkdown() { return md.toString(); }
}

class WordCountVisitor implements DocumentVisitor {
    private int wordCount = 0;

    @Override
    public void visitText(TextElement text) {
        int words = text.getText().split("\\s+").length;
        wordCount += words;
        System.out.println("  [WordCount] Text: " + words + " words");
    }

    @Override
    public void visitImage(ImageElement image) {
        System.out.println("  [WordCount] Image: 0 words");
    }

    @Override
    public void visitTable(TableElement table) {
        System.out.println("  [WordCount] Table: 0 words");
    }

    public int getWordCount() { return wordCount; }
}

public class MainVisitor {
    public static void main(String[] args) {
        System.out.println("=== Visitor Pattern Demonstration ===\n");

        // Shape example
        System.out.println("--- 1. Shape Calculations ---");

        List<Shape> shapes = new ArrayList<>();
        shapes.add(new Circle(5));
        shapes.add(new Rectangle(4, 6));
        shapes.add(new Triangle(3, 4));

        System.out.println("\nCalculating areas:");
        AreaCalculator areaCalc = new AreaCalculator();
        for (Shape shape : shapes) {
            shape.accept(areaCalc);
        }
        System.out.println("  Total area: " + String.format("%.2f", areaCalc.getTotalArea()));

        System.out.println("\nCalculating perimeters:");
        PerimeterCalculator perimCalc = new PerimeterCalculator();
        for (Shape shape : shapes) {
            shape.accept(perimCalc);
        }
        System.out.println("  Total perimeter: " + String.format("%.2f", perimCalc.getTotalPerimeter()));

        System.out.println("\nDrawing shapes:");
        DrawingVisitor drawer = new DrawingVisitor();
        for (Shape shape : shapes) {
            shape.accept(drawer);
        }
        System.out.println();

        // Document export example
        System.out.println("--- 2. Document Export ---");

        List<DocumentElement> document = new ArrayList<>();
        document.add(new TextElement("Welcome to our annual report"));
        document.add(new ImageElement("chart.png", 800, 600));
        document.add(new TableElement(5, 3));
        document.add(new TextElement("Thank you for reading this comprehensive overview"));

        System.out.println("\nExporting to HTML:");
        HTMLExportVisitor htmlExporter = new HTMLExportVisitor();
        for (DocumentElement element : document) {
            element.accept(htmlExporter);
        }

        System.out.println("\nExporting to Markdown:");
        MarkdownExportVisitor mdExporter = new MarkdownExportVisitor();
        for (DocumentElement element : document) {
            element.accept(mdExporter);
        }

        System.out.println("\nCounting words:");
        WordCountVisitor wordCounter = new WordCountVisitor();
        for (DocumentElement element : document) {
            element.accept(wordCounter);
        }
        System.out.println("  Total words: " + wordCounter.getWordCount());

        System.out.println("\n=== Summary ===");
        System.out.println("Visitor pattern benefits:");
        System.out.println("  - Add new operations without changing element classes");
        System.out.println("  - Gather related operations in one class");
        System.out.println("  - Accumulate state while traversing");
        System.out.println("\nConsiderations:");
        System.out.println("  - Adding new element types requires updating all visitors");
        System.out.println("  - May break encapsulation (elements expose internals)");
    }
}
