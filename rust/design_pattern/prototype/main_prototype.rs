// Prototype Design Pattern in Rust
// Using Clone trait as Rust's built-in prototype mechanism

use std::fmt;

// Define a trait for shapes that can be cloned and displayed
trait Shape: Clone + fmt::Display {
    fn area(&self) -> f64;
    fn shape_type(&self) -> &str;
}

// Circle implementation
#[derive(Clone)]
struct Circle {
    id: u32,
    x: f64,
    y: f64,
    radius: f64,
    color: String,
}

impl Circle {
    fn new(id: u32, x: f64, y: f64, radius: f64, color: &str) -> Self {
        println!("[Circle] Creating new Circle with id={}", id);
        Circle {
            id,
            x,
            y,
            radius,
            color: color.to_string(),
        }
    }
}

impl Shape for Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * self.radius * self.radius
    }

    fn shape_type(&self) -> &str {
        "Circle"
    }
}

impl fmt::Display for Circle {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "Circle[id={}, pos=({}, {}), radius={}, color={}, area={:.2}]",
            self.id, self.x, self.y, self.radius, self.color, self.area()
        )
    }
}

// Rectangle implementation
#[derive(Clone)]
struct Rectangle {
    id: u32,
    x: f64,
    y: f64,
    width: f64,
    height: f64,
    color: String,
}

impl Rectangle {
    fn new(id: u32, x: f64, y: f64, width: f64, height: f64, color: &str) -> Self {
        println!("[Rectangle] Creating new Rectangle with id={}", id);
        Rectangle {
            id,
            x,
            y,
            width,
            height,
            color: color.to_string(),
        }
    }
}

impl Shape for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn shape_type(&self) -> &str {
        "Rectangle"
    }
}

impl fmt::Display for Rectangle {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "Rectangle[id={}, pos=({}, {}), size={}x{}, color={}, area={:.2}]",
            self.id, self.x, self.y, self.width, self.height, self.color, self.area()
        )
    }
}

// Document with nested structure to demonstrate deep cloning
#[derive(Clone)]
struct Document {
    title: String,
    content: String,
    metadata: Metadata,
}

#[derive(Clone)]
struct Metadata {
    author: String,
    version: u32,
    tags: Vec<String>,
}

impl Document {
    fn new(title: &str, content: &str, author: &str) -> Self {
        println!("[Document] Creating new Document: '{}'", title);
        Document {
            title: title.to_string(),
            content: content.to_string(),
            metadata: Metadata {
                author: author.to_string(),
                version: 1,
                tags: Vec::new(),
            },
        }
    }

    fn add_tag(&mut self, tag: &str) {
        self.metadata.tags.push(tag.to_string());
    }
}

impl fmt::Display for Document {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "Document[title='{}', author='{}', version={}, tags={:?}]",
            self.title, self.metadata.author, self.metadata.version, self.metadata.tags
        )
    }
}

// Prototype Registry to store and clone prototypes
struct ShapeRegistry {
    circles: std::collections::HashMap<String, Circle>,
    rectangles: std::collections::HashMap<String, Rectangle>,
}

impl ShapeRegistry {
    fn new() -> Self {
        println!("[Registry] Creating new ShapeRegistry");
        ShapeRegistry {
            circles: std::collections::HashMap::new(),
            rectangles: std::collections::HashMap::new(),
        }
    }

    fn register_circle(&mut self, name: &str, circle: Circle) {
        println!("[Registry] Registering circle prototype: '{}'", name);
        self.circles.insert(name.to_string(), circle);
    }

    fn register_rectangle(&mut self, name: &str, rectangle: Rectangle) {
        println!("[Registry] Registering rectangle prototype: '{}'", name);
        self.rectangles.insert(name.to_string(), rectangle);
    }

    fn clone_circle(&self, name: &str) -> Option<Circle> {
        self.circles.get(name).map(|c| {
            println!("[Registry] Cloning circle prototype: '{}'", name);
            c.clone()
        })
    }

    fn clone_rectangle(&self, name: &str) -> Option<Rectangle> {
        self.rectangles.get(name).map(|r| {
            println!("[Registry] Cloning rectangle prototype: '{}'", name);
            r.clone()
        })
    }
}

fn main() {
    println!("=== Prototype Design Pattern in Rust ===\n");

    // Part 1: Basic Shape Cloning
    println!("--- Part 1: Basic Shape Cloning ---");

    let original_circle = Circle::new(1, 10.0, 20.0, 5.0, "Red");
    println!("Original: {}", original_circle);

    // Clone the circle using Rust's Clone trait
    println!("\n[Clone] Cloning circle using .clone()");
    let mut cloned_circle = original_circle.clone();
    cloned_circle.id = 2;
    cloned_circle.color = "Blue".to_string();
    cloned_circle.x = 30.0;

    println!("Original: {}", original_circle);
    println!("Cloned:   {}", cloned_circle);

    // Part 2: Rectangle Cloning
    println!("\n--- Part 2: Rectangle Cloning ---");

    let original_rect = Rectangle::new(100, 0.0, 0.0, 10.0, 5.0, "Green");
    println!("Original: {}", original_rect);

    println!("\n[Clone] Cloning rectangle using .clone()");
    let mut cloned_rect = original_rect.clone();
    cloned_rect.id = 101;
    cloned_rect.width = 20.0;
    cloned_rect.color = "Yellow".to_string();

    println!("Original: {}", original_rect);
    println!("Cloned:   {}", cloned_rect);

    // Part 3: Deep Cloning with Document
    println!("\n--- Part 3: Deep Cloning (Document with nested data) ---");

    let mut original_doc = Document::new("Design Patterns", "Content about patterns...", "Alice");
    original_doc.add_tag("programming");
    original_doc.add_tag("rust");
    println!("Original: {}", original_doc);

    println!("\n[Clone] Deep cloning document using .clone()");
    let mut cloned_doc = original_doc.clone();
    cloned_doc.title = "Design Patterns - Copy".to_string();
    cloned_doc.metadata.author = "Bob".to_string();
    cloned_doc.metadata.version = 2;
    cloned_doc.add_tag("copy");

    println!("Original: {}", original_doc);
    println!("Cloned:   {}", cloned_doc);

    // Part 4: Prototype Registry Pattern
    println!("\n--- Part 4: Prototype Registry ---");

    let mut registry = ShapeRegistry::new();

    // Register prototypes
    let small_circle = Circle::new(0, 0.0, 0.0, 2.0, "Black");
    let large_rect = Rectangle::new(0, 0.0, 0.0, 100.0, 50.0, "White");

    registry.register_circle("small-circle", small_circle);
    registry.register_rectangle("large-rect", large_rect);

    // Clone from registry
    println!("\n[Usage] Creating shapes from registry prototypes");

    if let Some(mut circle1) = registry.clone_circle("small-circle") {
        circle1.id = 1001;
        circle1.x = 50.0;
        circle1.y = 50.0;
        circle1.color = "Purple".to_string();
        println!("From registry: {}", circle1);
    }

    if let Some(mut circle2) = registry.clone_circle("small-circle") {
        circle2.id = 1002;
        circle2.x = 100.0;
        circle2.y = 100.0;
        circle2.color = "Orange".to_string();
        println!("From registry: {}", circle2);
    }

    if let Some(mut rect1) = registry.clone_rectangle("large-rect") {
        rect1.id = 2001;
        rect1.x = 200.0;
        rect1.color = "Cyan".to_string();
        println!("From registry: {}", rect1);
    }

    // Part 5: Demonstrating independence of clones
    println!("\n--- Part 5: Clone Independence Verification ---");

    let proto = Circle::new(999, 0.0, 0.0, 10.0, "Proto");
    let clone_a = proto.clone();
    let clone_b = proto.clone();

    println!("Prototype: {}", proto);
    println!("Clone A:   {}", clone_a);
    println!("Clone B:   {}", clone_b);

    // Verify memory addresses are different
    println!("\n[Memory] Verifying clones are separate objects:");
    println!("  Prototype address: {:p}", &proto);
    println!("  Clone A address:   {:p}", &clone_a);
    println!("  Clone B address:   {:p}", &clone_b);

    println!("\n=== Prototype Pattern Demo Complete ===");
}
