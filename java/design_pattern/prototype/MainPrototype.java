/**
 * Comprehensive demonstration of the Prototype Pattern in Java
 *
 * The Prototype pattern specifies the kinds of objects to create using a
 * prototypical instance, and creates new objects by copying this prototype.
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// Prototype interface
interface Prototype extends Cloneable {
    Prototype clone();
}

// Concrete Prototype - Document
class DocumentPrototype implements Prototype {
    private String title;
    private String content;
    private String author;
    private List<String> comments;
    private Map<String, String> metadata;

    public DocumentPrototype() {
        this.comments = new ArrayList<>();
        this.metadata = new HashMap<>();
    }

    // Copy constructor for deep copy
    public DocumentPrototype(DocumentPrototype source) {
        this.title = source.title;
        this.content = source.content;
        this.author = source.author;
        this.comments = new ArrayList<>(source.comments);
        this.metadata = new HashMap<>(source.metadata);
    }

    @Override
    public Prototype clone() {
        return new DocumentPrototype(this);
    }

    // Setters
    public void setTitle(String title) { this.title = title; }
    public void setContent(String content) { this.content = content; }
    public void setAuthor(String author) { this.author = author; }
    public void addComment(String comment) { this.comments.add(comment); }
    public void addMetadata(String key, String value) { this.metadata.put(key, value); }

    @Override
    public String toString() {
        return String.format("Document[title=%s, author=%s, content=%s, comments=%d, metadata=%s]",
            title, author, content != null ? content.substring(0, Math.min(20, content.length())) + "..." : "null",
            comments.size(), metadata);
    }
}

// Concrete Prototype - Shape
abstract class Shape implements Prototype {
    protected int x;
    protected int y;
    protected String color;

    public Shape() {}

    public Shape(Shape source) {
        this.x = source.x;
        this.y = source.y;
        this.color = source.color;
    }

    public void setPosition(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public abstract Prototype clone();

    public abstract void draw();
}

class Circle extends Shape {
    private int radius;

    public Circle() {}

    public Circle(Circle source) {
        super(source);
        this.radius = source.radius;
    }

    public void setRadius(int radius) {
        this.radius = radius;
    }

    @Override
    public Prototype clone() {
        return new Circle(this);
    }

    @Override
    public void draw() {
        System.out.println("  Drawing Circle at (" + x + ", " + y + ") with radius " + radius + ", color: " + color);
    }
}

class Rectangle extends Shape {
    private int width;
    private int height;

    public Rectangle() {}

    public Rectangle(Rectangle source) {
        super(source);
        this.width = source.width;
        this.height = source.height;
    }

    public void setDimensions(int width, int height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public Prototype clone() {
        return new Rectangle(this);
    }

    @Override
    public void draw() {
        System.out.println("  Drawing Rectangle at (" + x + ", " + y + ") with size " + width + "x" + height + ", color: " + color);
    }
}

class Triangle extends Shape {
    private int base;
    private int height;

    public Triangle() {}

    public Triangle(Triangle source) {
        super(source);
        this.base = source.base;
        this.height = source.height;
    }

    public void setDimensions(int base, int height) {
        this.base = base;
        this.height = height;
    }

    @Override
    public Prototype clone() {
        return new Triangle(this);
    }

    @Override
    public void draw() {
        System.out.println("  Drawing Triangle at (" + x + ", " + y + ") with base " + base + ", height " + height + ", color: " + color);
    }
}

// Prototype Registry/Cache
class ShapeRegistry {
    private Map<String, Shape> shapes = new HashMap<>();

    public void addShape(String key, Shape shape) {
        shapes.put(key, shape);
    }

    public Shape getShape(String key) {
        Shape shape = shapes.get(key);
        if (shape != null) {
            return (Shape) shape.clone();
        }
        return null;
    }

    public void loadDefaults() {
        Circle redCircle = new Circle();
        redCircle.setPosition(0, 0);
        redCircle.setColor("Red");
        redCircle.setRadius(50);
        addShape("red-circle", redCircle);

        Circle blueCircle = new Circle();
        blueCircle.setPosition(0, 0);
        blueCircle.setColor("Blue");
        blueCircle.setRadius(30);
        addShape("blue-circle", blueCircle);

        Rectangle greenRect = new Rectangle();
        greenRect.setPosition(0, 0);
        greenRect.setColor("Green");
        greenRect.setDimensions(100, 50);
        addShape("green-rectangle", greenRect);

        Triangle yellowTriangle = new Triangle();
        yellowTriangle.setPosition(0, 0);
        yellowTriangle.setColor("Yellow");
        yellowTriangle.setDimensions(80, 60);
        addShape("yellow-triangle", yellowTriangle);
    }
}

// Example with nested objects - demonstrating deep vs shallow copy
class Address implements Cloneable {
    private String street;
    private String city;
    private String country;

    public Address(String street, String city, String country) {
        this.street = street;
        this.city = city;
        this.country = country;
    }

    public Address(Address source) {
        this.street = source.street;
        this.city = source.city;
        this.country = source.country;
    }

    public void setStreet(String street) { this.street = street; }
    public String getStreet() { return street; }

    @Override
    public String toString() {
        return street + ", " + city + ", " + country;
    }

    @Override
    protected Address clone() {
        return new Address(this);
    }
}

class Employee implements Prototype {
    private String name;
    private String department;
    private Address address;
    private List<String> skills;

    public Employee(String name, String department) {
        this.name = name;
        this.department = department;
        this.skills = new ArrayList<>();
    }

    // Deep copy constructor
    public Employee(Employee source) {
        this.name = source.name;
        this.department = source.department;
        // Deep copy of nested object
        this.address = source.address != null ? source.address.clone() : null;
        // Deep copy of collection
        this.skills = new ArrayList<>(source.skills);
    }

    public void setAddress(Address address) { this.address = address; }
    public Address getAddress() { return address; }
    public void addSkill(String skill) { this.skills.add(skill); }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    @Override
    public Prototype clone() {
        return new Employee(this);
    }

    @Override
    public String toString() {
        return String.format("Employee[name=%s, dept=%s, address=%s, skills=%s]",
            name, department, address, skills);
    }
}

public class MainPrototype {
    public static void main(String[] args) {
        System.out.println("=== Prototype Pattern Demonstration ===\n");

        // Basic prototype usage
        System.out.println("--- 1. Basic Document Prototype ---");
        DocumentPrototype original = new DocumentPrototype();
        original.setTitle("Design Patterns Guide");
        original.setContent("This is a comprehensive guide to design patterns...");
        original.setAuthor("John Doe");
        original.addComment("Great article!");
        original.addMetadata("version", "1.0");
        original.addMetadata("category", "Programming");

        System.out.println("Original: " + original);

        // Clone the document
        DocumentPrototype clone = (DocumentPrototype) original.clone();
        clone.setTitle("Design Patterns Guide - Copy");
        clone.addComment("Cloned version");
        clone.addMetadata("version", "1.1");

        System.out.println("Clone: " + clone);
        System.out.println("Original unchanged: " + original);
        System.out.println();

        // Shape prototypes
        System.out.println("--- 2. Shape Prototypes ---");
        Circle circlePrototype = new Circle();
        circlePrototype.setPosition(10, 20);
        circlePrototype.setColor("Red");
        circlePrototype.setRadius(25);

        System.out.println("Original circle:");
        circlePrototype.draw();

        // Clone and modify
        Circle clonedCircle = (Circle) circlePrototype.clone();
        clonedCircle.setPosition(100, 200);
        clonedCircle.setColor("Blue");

        System.out.println("Cloned circle:");
        clonedCircle.draw();

        System.out.println("Original circle unchanged:");
        circlePrototype.draw();
        System.out.println();

        // Using prototype registry
        System.out.println("--- 3. Using Prototype Registry ---");
        ShapeRegistry registry = new ShapeRegistry();
        registry.loadDefaults();

        // Get shapes from registry (cloned)
        Shape shape1 = registry.getShape("red-circle");
        shape1.setPosition(50, 50);
        shape1.draw();

        Shape shape2 = registry.getShape("green-rectangle");
        shape2.setPosition(200, 100);
        shape2.draw();

        Shape shape3 = registry.getShape("yellow-triangle");
        shape3.setPosition(300, 150);
        shape3.draw();

        // Multiple clones from same prototype
        System.out.println("\nMultiple clones from blue-circle:");
        for (int i = 0; i < 3; i++) {
            Shape circle = registry.getShape("blue-circle");
            circle.setPosition(i * 100, i * 50);
            circle.draw();
        }
        System.out.println();

        // Deep copy demonstration
        System.out.println("--- 4. Deep Copy with Nested Objects ---");
        Employee emp1 = new Employee("Alice", "Engineering");
        emp1.setAddress(new Address("123 Main St", "New York", "USA"));
        emp1.addSkill("Java");
        emp1.addSkill("Python");

        System.out.println("Original Employee: " + emp1);

        // Clone employee
        Employee emp2 = (Employee) emp1.clone();
        emp2.setName("Bob");
        emp2.getAddress().setStreet("456 Oak Ave");  // Modify nested object
        emp2.addSkill("JavaScript");

        System.out.println("Cloned Employee: " + emp2);
        System.out.println("Original unchanged: " + emp1);
        System.out.println();

        // Performance comparison
        System.out.println("--- 5. Performance Benefit Example ---");
        System.out.println("Creating complex object from scratch vs cloning:");

        // Simulating expensive object creation
        DocumentPrototype heavyDoc = new DocumentPrototype();
        heavyDoc.setTitle("Heavy Document");
        heavyDoc.setContent("Lots of content...");
        for (int i = 0; i < 100; i++) {
            heavyDoc.addMetadata("key" + i, "value" + i);
        }

        long startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            DocumentPrototype clonedDoc = (DocumentPrototype) heavyDoc.clone();
        }
        long cloneTime = System.nanoTime() - startTime;
        System.out.println("  Time to clone 1000 objects: " + cloneTime / 1_000_000.0 + " ms");

        System.out.println("\n=== Summary ===");
        System.out.println("Prototype pattern benefits:");
        System.out.println("  - Reduces subclassing by cloning");
        System.out.println("  - Hides complexities of creating new instances");
        System.out.println("  - Lets you add/remove objects at runtime");
        System.out.println("  - Specifies new objects by varying values");
        System.out.println("  - Can be faster than creating new objects");
        System.out.println("\nKey considerations:");
        System.out.println("  - Must implement deep copy for complex objects");
        System.out.println("  - Cloning objects with circular references is tricky");
    }
}
