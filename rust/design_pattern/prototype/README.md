# Prototype Design Pattern in Rust

The Prototype pattern is a creational design pattern that allows objects to be cloned rather than created from scratch. In Rust, this pattern is idiomatically implemented using the `Clone` trait, which provides a standardized way to create deep copies of objects.

**When to use:** When creating new objects is expensive (e.g., database operations, complex initialization), or when you want to create variations of a base configuration without exposing the internal structure.

## Source Code

```rust
  1  // Prototype Design Pattern in Rust
  2  // Using Clone trait as Rust's built-in prototype mechanism
  3
  4  use std::fmt;
  5
  6  // Define a trait for shapes that can be cloned and displayed
  7  trait Shape: Clone + fmt::Display {
  8      fn area(&self) -> f64;
  9      fn shape_type(&self) -> &str;
 10  }
 11
 12  // Circle implementation
 13  #[derive(Clone)]
 14  struct Circle {
 15      id: u32,
 16      x: f64,
 17      y: f64,
 18      radius: f64,
 19      color: String,
 20  }
 21
 22  impl Circle {
 23      fn new(id: u32, x: f64, y: f64, radius: f64, color: &str) -> Self {
 24          println!("[Circle] Creating new Circle with id={}", id);
 25          Circle {
 26              id,
 27              x,
 28              y,
 29              radius,
 30              color: color.to_string(),
 31          }
 32      }
 33  }
 34
 35  impl Shape for Circle {
 36      fn area(&self) -> f64 {
 37          std::f64::consts::PI * self.radius * self.radius
 38      }
 39
 40      fn shape_type(&self) -> &str {
 41          "Circle"
 42      }
 43  }
 44
 45  impl fmt::Display for Circle {
 46      fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
 47          write!(
 48              f,
 49              "Circle[id={}, pos=({}, {}), radius={}, color={}, area={:.2}]",
 50              self.id, self.x, self.y, self.radius, self.color, self.area()
 51          )
 52      }
 53  }
 54
 55  // Rectangle implementation
 56  #[derive(Clone)]
 57  struct Rectangle {
 58      id: u32,
 59      x: f64,
 60      y: f64,
 61      width: f64,
 62      height: f64,
 63      color: String,
 64  }
 65
 66  impl Rectangle {
 67      fn new(id: u32, x: f64, y: f64, width: f64, height: f64, color: &str) -> Self {
 68          println!("[Rectangle] Creating new Rectangle with id={}", id);
 69          Rectangle {
 70              id,
 71              x,
 72              y,
 73              width,
 74              height,
 75              color: color.to_string(),
 76          }
 77      }
 78  }
 79
 80  impl Shape for Rectangle {
 81      fn area(&self) -> f64 {
 82          self.width * self.height
 83      }
 84
 85      fn shape_type(&self) -> &str {
 86          "Rectangle"
 87      }
 88  }
 89
 90  impl fmt::Display for Rectangle {
 91      fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
 92          write!(
 93              f,
 94              "Rectangle[id={}, pos=({}, {}), size={}x{}, color={}, area={:.2}]",
 95              self.id, self.x, self.y, self.width, self.height, self.color, self.area()
 96          )
 97      }
 98  }
 99
100  // Document with nested structure to demonstrate deep cloning
101  #[derive(Clone)]
102  struct Document {
103      title: String,
104      content: String,
105      metadata: Metadata,
106  }
107
108  #[derive(Clone)]
109  struct Metadata {
110      author: String,
111      version: u32,
112      tags: Vec<String>,
113  }
114
115  impl Document {
116      fn new(title: &str, content: &str, author: &str) -> Self {
117          println!("[Document] Creating new Document: '{}'", title);
118          Document {
119              title: title.to_string(),
120              content: content.to_string(),
121              metadata: Metadata {
122                  author: author.to_string(),
123                  version: 1,
124                  tags: Vec::new(),
125              },
126          }
127      }
128
129      fn add_tag(&mut self, tag: &str) {
130          self.metadata.tags.push(tag.to_string());
131      }
132  }
133
134  impl fmt::Display for Document {
135      fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
136          write!(
137              f,
138              "Document[title='{}', author='{}', version={}, tags={:?}]",
139              self.title, self.metadata.author, self.metadata.version, self.metadata.tags
140          )
141      }
142  }
143
144  // Prototype Registry to store and clone prototypes
145  struct ShapeRegistry {
146      circles: std::collections::HashMap<String, Circle>,
147      rectangles: std::collections::HashMap<String, Rectangle>,
148  }
149
150  impl ShapeRegistry {
151      fn new() -> Self {
152          println!("[Registry] Creating new ShapeRegistry");
153          ShapeRegistry {
154              circles: std::collections::HashMap::new(),
155              rectangles: std::collections::HashMap::new(),
156          }
157      }
158
159      fn register_circle(&mut self, name: &str, circle: Circle) {
160          println!("[Registry] Registering circle prototype: '{}'", name);
161          self.circles.insert(name.to_string(), circle);
162      }
163
164      fn register_rectangle(&mut self, name: &str, rectangle: Rectangle) {
165          println!("[Registry] Registering rectangle prototype: '{}'", name);
166          self.rectangles.insert(name.to_string(), rectangle);
167      }
168
169      fn clone_circle(&self, name: &str) -> Option<Circle> {
170          self.circles.get(name).map(|c| {
171              println!("[Registry] Cloning circle prototype: '{}'", name);
172              c.clone()
173          })
174      }
175
176      fn clone_rectangle(&self, name: &str) -> Option<Rectangle> {
177          self.rectangles.get(name).map(|r| {
178              println!("[Registry] Cloning rectangle prototype: '{}'", name);
179              r.clone()
180          })
181      }
182  }
183
184  fn main() {
185      println!("=== Prototype Design Pattern in Rust ===\n");
186
187      // Part 1: Basic Shape Cloning
188      println!("--- Part 1: Basic Shape Cloning ---");
189
190      let original_circle = Circle::new(1, 10.0, 20.0, 5.0, "Red");
191      println!("Original: {}", original_circle);
192
193      // Clone the circle using Rust's Clone trait
194      println!("\n[Clone] Cloning circle using .clone()");
195      let mut cloned_circle = original_circle.clone();
196      cloned_circle.id = 2;
197      cloned_circle.color = "Blue".to_string();
198      cloned_circle.x = 30.0;
199
200      println!("Original: {}", original_circle);
201      println!("Cloned:   {}", cloned_circle);
202
203      // Part 2: Rectangle Cloning
204      println!("\n--- Part 2: Rectangle Cloning ---");
205
206      let original_rect = Rectangle::new(100, 0.0, 0.0, 10.0, 5.0, "Green");
207      println!("Original: {}", original_rect);
208
209      println!("\n[Clone] Cloning rectangle using .clone()");
210      let mut cloned_rect = original_rect.clone();
211      cloned_rect.id = 101;
212      cloned_rect.width = 20.0;
213      cloned_rect.color = "Yellow".to_string();
214
215      println!("Original: {}", original_rect);
216      println!("Cloned:   {}", cloned_rect);
217
218      // Part 3: Deep Cloning with Document
219      println!("\n--- Part 3: Deep Cloning (Document with nested data) ---");
220
221      let mut original_doc = Document::new("Design Patterns", "Content about patterns...", "Alice");
222      original_doc.add_tag("programming");
223      original_doc.add_tag("rust");
224      println!("Original: {}", original_doc);
225
226      println!("\n[Clone] Deep cloning document using .clone()");
227      let mut cloned_doc = original_doc.clone();
228      cloned_doc.title = "Design Patterns - Copy".to_string();
229      cloned_doc.metadata.author = "Bob".to_string();
230      cloned_doc.metadata.version = 2;
231      cloned_doc.add_tag("copy");
232
233      println!("Original: {}", original_doc);
234      println!("Cloned:   {}", cloned_doc);
235
236      // Part 4: Prototype Registry Pattern
237      println!("\n--- Part 4: Prototype Registry ---");
238
239      let mut registry = ShapeRegistry::new();
240
241      // Register prototypes
242      let small_circle = Circle::new(0, 0.0, 0.0, 2.0, "Black");
243      let large_rect = Rectangle::new(0, 0.0, 0.0, 100.0, 50.0, "White");
244
245      registry.register_circle("small-circle", small_circle);
246      registry.register_rectangle("large-rect", large_rect);
247
248      // Clone from registry
249      println!("\n[Usage] Creating shapes from registry prototypes");
250
251      if let Some(mut circle1) = registry.clone_circle("small-circle") {
252          circle1.id = 1001;
253          circle1.x = 50.0;
254          circle1.y = 50.0;
255          circle1.color = "Purple".to_string();
256          println!("From registry: {}", circle1);
257      }
258
259      if let Some(mut circle2) = registry.clone_circle("small-circle") {
260          circle2.id = 1002;
261          circle2.x = 100.0;
262          circle2.y = 100.0;
263          circle2.color = "Orange".to_string();
264          println!("From registry: {}", circle2);
265      }
266
267      if let Some(mut rect1) = registry.clone_rectangle("large-rect") {
268          rect1.id = 2001;
269          rect1.x = 200.0;
270          rect1.color = "Cyan".to_string();
271          println!("From registry: {}", rect1);
272      }
273
274      // Part 5: Demonstrating independence of clones
275      println!("\n--- Part 5: Clone Independence Verification ---");
276
277      let proto = Circle::new(999, 0.0, 0.0, 10.0, "Proto");
278      let clone_a = proto.clone();
279      let clone_b = proto.clone();
280
281      println!("Prototype: {}", proto);
282      println!("Clone A:   {}", clone_a);
283      println!("Clone B:   {}", clone_b);
284
285      // Verify memory addresses are different
286      println!("\n[Memory] Verifying clones are separate objects:");
287      println!("  Prototype address: {:p}", &proto);
288      println!("  Clone A address:   {:p}", &clone_a);
289      println!("  Clone B address:   {:p}", &clone_b);
290
291      println!("\n=== Prototype Pattern Demo Complete ===");
292  }
```

## Program Output

```
=== Prototype Design Pattern in Rust ===

--- Part 1: Basic Shape Cloning ---
[Circle] Creating new Circle with id=1
Original: Circle[id=1, pos=(10, 20), radius=5, color=Red, area=78.54]

[Clone] Cloning circle using .clone()
Original: Circle[id=1, pos=(10, 20), radius=5, color=Red, area=78.54]
Cloned:   Circle[id=2, pos=(30, 20), radius=5, color=Blue, area=78.54]

--- Part 2: Rectangle Cloning ---
[Rectangle] Creating new Rectangle with id=100
Original: Rectangle[id=100, pos=(0, 0), size=10x5, color=Green, area=50.00]

[Clone] Cloning rectangle using .clone()
Original: Rectangle[id=100, pos=(0, 0), size=10x5, color=Green, area=50.00]
Cloned:   Rectangle[id=101, pos=(0, 0), size=20x5, color=Yellow, area=100.00]

--- Part 3: Deep Cloning (Document with nested data) ---
[Document] Creating new Document: 'Design Patterns'
Original: Document[title='Design Patterns', author='Alice', version=1, tags=["programming", "rust"]]

[Clone] Deep cloning document using .clone()
Original: Document[title='Design Patterns', author='Alice', version=1, tags=["programming", "rust"]]
Cloned:   Document[title='Design Patterns - Copy', author='Bob', version=2, tags=["programming", "rust", "copy"]]

--- Part 4: Prototype Registry ---
[Registry] Creating new ShapeRegistry
[Circle] Creating new Circle with id=0
[Rectangle] Creating new Rectangle with id=0
[Registry] Registering circle prototype: 'small-circle'
[Registry] Registering rectangle prototype: 'large-rect'

[Usage] Creating shapes from registry prototypes
[Registry] Cloning circle prototype: 'small-circle'
From registry: Circle[id=1001, pos=(50, 50), radius=2, color=Purple, area=12.57]
[Registry] Cloning circle prototype: 'small-circle'
From registry: Circle[id=1002, pos=(100, 100), radius=2, color=Orange, area=12.57]
[Registry] Cloning rectangle prototype: 'large-rect'
From registry: Rectangle[id=2001, pos=(200, 0), size=100x50, color=Cyan, area=5000.00]

--- Part 5: Clone Independence Verification ---
[Circle] Creating new Circle with id=999
Prototype: Circle[id=999, pos=(0, 0), radius=10, color=Proto, area=314.16]
Clone A:   Circle[id=999, pos=(0, 0), radius=10, color=Proto, area=314.16]
Clone B:   Circle[id=999, pos=(0, 0), radius=10, color=Proto, area=314.16]

[Memory] Verifying clones are separate objects:
  Prototype address: 0x7edbbb9dbac8
  Clone A address:   0x7edbbb9dbb00
  Clone B address:   0x7edbbb9dbb38

=== Prototype Pattern Demo Complete ===
```

## Code Annotations

### Key Section Explanations

**Lines 7-10: Shape Trait Definition**
- Defines a trait that requires both `Clone` and `Display` traits
- This establishes the contract that all shapes must be clonable (prototype pattern requirement)
- The trait bound `Clone + fmt::Display` combines multiple traits using Rust's trait composition

**Lines 13-20: Circle Struct with Derive Clone**
- `#[derive(Clone)]` automatically implements the Clone trait
- This is Rust's idiomatic way to enable the prototype pattern
- The compiler generates a deep clone implementation that copies all fields

**Lines 56-64: Rectangle Struct**
- Same pattern as Circle, demonstrating consistency across different shape types
- Each struct maintains its own set of properties while sharing the cloning mechanism

**Lines 101-113: Document with Nested Metadata**
- Demonstrates deep cloning with nested structures
- Both `Document` and `Metadata` derive Clone
- The `Vec<String>` in tags is also fully cloned (deep copy)

**Lines 144-181: ShapeRegistry (Prototype Manager)**
- Implements the classic Prototype Registry pattern
- Stores prototype objects in HashMaps for later cloning
- `clone_circle` and `clone_rectangle` methods create new instances from stored prototypes
- Returns `Option<T>` to handle cases where prototype doesn't exist

**Lines 195-198: Clone and Modify Pattern**
- Shows the typical workflow: clone then modify
- Original remains unchanged while clone is customized
- This is the core value proposition of the Prototype pattern

**Lines 277-289: Memory Address Verification**
- Uses `{:p}` format specifier to print memory addresses
- Proves that clones are independent objects in separate memory locations
- Each clone can be modified without affecting others

### Output to Source Line Correlation

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Circle] Creating new Circle with id=1` | 24 | Constructor prints creation message |
| `Original: Circle[...Red...]` | 191 | Display trait formats Circle (lines 45-52) |
| `[Clone] Cloning circle using .clone()` | 194 | Explicit message before clone operation |
| `Cloned: Circle[...Blue...]` | 201 | Modified clone displayed (lines 196-198 modify it) |
| `[Rectangle] Creating new Rectangle with id=100` | 68 | Rectangle constructor message |
| `[Document] Creating new Document: 'Design Patterns'` | 117 | Document constructor message |
| `[Registry] Creating new ShapeRegistry` | 152 | Registry constructor message |
| `[Registry] Registering circle prototype: 'small-circle'` | 160 | Registration method message |
| `[Registry] Cloning circle prototype: 'small-circle'` | 171 | Clone method prints before cloning |
| `From registry: Circle[id=1001...]` | 256 | Cloned and modified shape from registry |
| `Prototype address: 0x...` | 287 | Memory address printed with `:p` format |

### Key Characteristics of Prototype Pattern in Rust

| Characteristic | Rust Implementation |
|----------------|---------------------|
| **Clone Mechanism** | Built-in `Clone` trait with `#[derive(Clone)]` |
| **Deep vs Shallow** | Derive Clone creates deep copies by default |
| **Type Safety** | Compiler ensures cloned types match original |
| **Memory Safety** | Ownership system prevents aliasing issues |
| **Performance** | Zero-cost abstraction; compiler optimizes clone calls |
| **Customization** | Can implement Clone manually for custom behavior |

### Rust-Specific Advantages

1. **Derive Macro**: `#[derive(Clone)]` eliminates boilerplate code
2. **Trait Bounds**: Can require Clone in trait definitions (`trait Shape: Clone`)
3. **Ownership Model**: Cloning creates independent data with clear ownership
4. **No Runtime Overhead**: Clone is resolved at compile time
5. **Safe by Default**: Deep cloning prevents shared mutable state issues

### When to Manually Implement Clone

```rust
impl Clone for MyStruct {
    fn clone(&self) -> Self {
        // Custom cloning logic here
        // Useful for:
        // - Skipping certain fields
        // - Incrementing counters
        // - Resetting transient state
    }
}
```

## Compilation

```bash
rustc main_prototype.rs -o main_prototype.exe && ./main_prototype.exe
```

**Note**: This code uses only Rust standard library features and compiles with any stable Rust version (1.0+).
