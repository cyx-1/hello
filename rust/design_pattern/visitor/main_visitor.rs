// Visitor Design Pattern in Rust
// Demonstrates separating algorithms from objects they operate on

use std::f64::consts::PI;

// Visitor trait - defines operations for each element type
trait ShapeVisitor {
    fn visit_circle(&mut self, circle: &Circle);
    fn visit_rectangle(&mut self, rectangle: &Rectangle);
    fn visit_triangle(&mut self, triangle: &Triangle);
}

// Element trait - shapes that can accept visitors
trait Shape {
    fn accept(&self, visitor: &mut dyn ShapeVisitor);
    fn name(&self) -> &str;
}

// Concrete Element: Circle
struct Circle {
    radius: f64,
}

impl Circle {
    fn new(radius: f64) -> Self {
        println!("  [Circle] Created with radius: {}", radius);
        Circle { radius }
    }
}

impl Shape for Circle {
    fn accept(&self, visitor: &mut dyn ShapeVisitor) {
        println!("  [Circle] Accepting visitor...");
        visitor.visit_circle(self);
    }

    fn name(&self) -> &str {
        "Circle"
    }
}

// Concrete Element: Rectangle
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    fn new(width: f64, height: f64) -> Self {
        println!("  [Rectangle] Created with width: {}, height: {}", width, height);
        Rectangle { width, height }
    }
}

impl Shape for Rectangle {
    fn accept(&self, visitor: &mut dyn ShapeVisitor) {
        println!("  [Rectangle] Accepting visitor...");
        visitor.visit_rectangle(self);
    }

    fn name(&self) -> &str {
        "Rectangle"
    }
}

// Concrete Element: Triangle
struct Triangle {
    base: f64,
    height: f64,
}

impl Triangle {
    fn new(base: f64, height: f64) -> Self {
        println!("  [Triangle] Created with base: {}, height: {}", base, height);
        Triangle { base, height }
    }
}

impl Shape for Triangle {
    fn accept(&self, visitor: &mut dyn ShapeVisitor) {
        println!("  [Triangle] Accepting visitor...");
        visitor.visit_triangle(self);
    }

    fn name(&self) -> &str {
        "Triangle"
    }
}

// Concrete Visitor: Area Calculator
struct AreaCalculator {
    total_area: f64,
}

impl AreaCalculator {
    fn new() -> Self {
        println!("  [AreaCalculator] Initialized with total_area: 0.0");
        AreaCalculator { total_area: 0.0 }
    }

    fn get_total_area(&self) -> f64 {
        self.total_area
    }
}

impl ShapeVisitor for AreaCalculator {
    fn visit_circle(&mut self, circle: &Circle) {
        let area = PI * circle.radius * circle.radius;
        self.total_area += area;
        println!("    -> Calculated circle area: {:.2}", area);
    }

    fn visit_rectangle(&mut self, rectangle: &Rectangle) {
        let area = rectangle.width * rectangle.height;
        self.total_area += area;
        println!("    -> Calculated rectangle area: {:.2}", area);
    }

    fn visit_triangle(&mut self, triangle: &Triangle) {
        let area = 0.5 * triangle.base * triangle.height;
        self.total_area += area;
        println!("    -> Calculated triangle area: {:.2}", area);
    }
}

// Concrete Visitor: Shape Exporter (exports to different formats)
struct ShapeExporter {
    export_data: Vec<String>,
}

impl ShapeExporter {
    fn new() -> Self {
        println!("  [ShapeExporter] Initialized with empty export buffer");
        ShapeExporter {
            export_data: Vec::new(),
        }
    }

    fn get_export(&self) -> String {
        self.export_data.join("\n")
    }
}

impl ShapeVisitor for ShapeExporter {
    fn visit_circle(&mut self, circle: &Circle) {
        let json = format!(
            r#"{{ "type": "circle", "radius": {} }}"#,
            circle.radius
        );
        self.export_data.push(json.clone());
        println!("    -> Exported circle: {}", json);
    }

    fn visit_rectangle(&mut self, rectangle: &Rectangle) {
        let json = format!(
            r#"{{ "type": "rectangle", "width": {}, "height": {} }}"#,
            rectangle.width, rectangle.height
        );
        self.export_data.push(json.clone());
        println!("    -> Exported rectangle: {}", json);
    }

    fn visit_triangle(&mut self, triangle: &Triangle) {
        let json = format!(
            r#"{{ "type": "triangle", "base": {}, "height": {} }}"#,
            triangle.base, triangle.height
        );
        self.export_data.push(json.clone());
        println!("    -> Exported triangle: {}", json);
    }
}

// Concrete Visitor: Perimeter Calculator
struct PerimeterCalculator {
    total_perimeter: f64,
}

impl PerimeterCalculator {
    fn new() -> Self {
        println!("  [PerimeterCalculator] Initialized with total_perimeter: 0.0");
        PerimeterCalculator { total_perimeter: 0.0 }
    }

    fn get_total_perimeter(&self) -> f64 {
        self.total_perimeter
    }
}

impl ShapeVisitor for PerimeterCalculator {
    fn visit_circle(&mut self, circle: &Circle) {
        let perimeter = 2.0 * PI * circle.radius;
        self.total_perimeter += perimeter;
        println!("    -> Calculated circle perimeter: {:.2}", perimeter);
    }

    fn visit_rectangle(&mut self, rectangle: &Rectangle) {
        let perimeter = 2.0 * (rectangle.width + rectangle.height);
        self.total_perimeter += perimeter;
        println!("    -> Calculated rectangle perimeter: {:.2}", perimeter);
    }

    fn visit_triangle(&mut self, triangle: &Triangle) {
        // Assuming isoceles triangle for simplicity
        let side = (triangle.height.powi(2) + (triangle.base / 2.0).powi(2)).sqrt();
        let perimeter = triangle.base + 2.0 * side;
        self.total_perimeter += perimeter;
        println!("    -> Calculated triangle perimeter: {:.2}", perimeter);
    }
}

// Object structure that holds elements
struct ShapeCollection {
    shapes: Vec<Box<dyn Shape>>,
}

impl ShapeCollection {
    fn new() -> Self {
        println!("  [ShapeCollection] Created empty collection");
        ShapeCollection { shapes: Vec::new() }
    }

    fn add(&mut self, shape: Box<dyn Shape>) {
        println!("  [ShapeCollection] Added {} to collection", shape.name());
        self.shapes.push(shape);
    }

    fn accept(&self, visitor: &mut dyn ShapeVisitor) {
        for shape in &self.shapes {
            shape.accept(visitor);
        }
    }
}

fn main() {
    println!("=== Visitor Design Pattern Demo ===\n");

    // Create shapes
    println!("1. Creating shapes:");
    let circle = Box::new(Circle::new(5.0));
    let rectangle = Box::new(Rectangle::new(4.0, 6.0));
    let triangle = Box::new(Triangle::new(3.0, 4.0));

    // Add shapes to collection
    println!("\n2. Building shape collection:");
    let mut collection = ShapeCollection::new();
    collection.add(circle);
    collection.add(rectangle);
    collection.add(triangle);

    // Use Area Calculator visitor
    println!("\n3. Applying AreaCalculator visitor:");
    let mut area_calc = AreaCalculator::new();
    collection.accept(&mut area_calc);
    println!("  [Result] Total area: {:.2}\n", area_calc.get_total_area());

    // Use Shape Exporter visitor
    println!("4. Applying ShapeExporter visitor:");
    let mut exporter = ShapeExporter::new();
    collection.accept(&mut exporter);
    println!("  [Result] Export data:");
    for line in exporter.get_export().lines() {
        println!("    {}", line);
    }

    // Use Perimeter Calculator visitor
    println!("\n5. Applying PerimeterCalculator visitor:");
    let mut perimeter_calc = PerimeterCalculator::new();
    collection.accept(&mut perimeter_calc);
    println!("  [Result] Total perimeter: {:.2}\n", perimeter_calc.get_total_perimeter());

    // Demonstrate adding new visitor without modifying shapes
    println!("6. Key Pattern Benefits:");
    println!("  - New operations added without modifying shape classes");
    println!("  - Operations on shapes are centralized in visitors");
    println!("  - Double dispatch achieved via accept/visit methods");
    println!("  - Easy to add new visitors for different algorithms");

    println!("\n=== Demo Complete ===");
}
