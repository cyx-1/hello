# Visitor Design Pattern in Rust

The Visitor pattern is a behavioral design pattern that separates algorithms from the objects on which they operate. It allows adding new operations to existing object structures without modifying those structures. This implementation demonstrates the pattern using geometric shapes with multiple visitors that calculate areas, perimeters, and export data.

## Source Code

```rust
  1  // Visitor Design Pattern in Rust
  2  // Demonstrates separating algorithms from objects they operate on
  3
  4  use std::f64::consts::PI;
  5
  6  // Visitor trait - defines operations for each element type
  7  trait ShapeVisitor {
  8      fn visit_circle(&mut self, circle: &Circle);
  9      fn visit_rectangle(&mut self, rectangle: &Rectangle);
 10      fn visit_triangle(&mut self, triangle: &Triangle);
 11  }
 12
 13  // Element trait - shapes that can accept visitors
 14  trait Shape {
 15      fn accept(&self, visitor: &mut dyn ShapeVisitor);
 16      fn name(&self) -> &str;
 17  }
 18
 19  // Concrete Element: Circle
 20  struct Circle {
 21      radius: f64,
 22  }
 23
 24  impl Circle {
 25      fn new(radius: f64) -> Self {
 26          println!("  [Circle] Created with radius: {}", radius);
 27          Circle { radius }
 28      }
 29  }
 30
 31  impl Shape for Circle {
 32      fn accept(&self, visitor: &mut dyn ShapeVisitor) {
 33          println!("  [Circle] Accepting visitor...");
 34          visitor.visit_circle(self);
 35      }
 36
 37      fn name(&self) -> &str {
 38          "Circle"
 39      }
 40  }
 41
 42  // Concrete Element: Rectangle
 43  struct Rectangle {
 44      width: f64,
 45      height: f64,
 46  }
 47
 48  impl Rectangle {
 49      fn new(width: f64, height: f64) -> Self {
 50          println!("  [Rectangle] Created with width: {}, height: {}", width, height);
 51          Rectangle { width, height }
 52      }
 53  }
 54
 55  impl Shape for Rectangle {
 56      fn accept(&self, visitor: &mut dyn ShapeVisitor) {
 57          println!("  [Rectangle] Accepting visitor...");
 58          visitor.visit_rectangle(self);
 59      }
 60
 61      fn name(&self) -> &str {
 62          "Rectangle"
 63      }
 64  }
 65
 66  // Concrete Element: Triangle
 67  struct Triangle {
 68      base: f64,
 69      height: f64,
 70  }
 71
 72  impl Triangle {
 73      fn new(base: f64, height: f64) -> Self {
 74          println!("  [Triangle] Created with base: {}, height: {}", base, height);
 75          Triangle { base, height }
 76      }
 77  }
 78
 79  impl Shape for Triangle {
 80      fn accept(&self, visitor: &mut dyn ShapeVisitor) {
 81          println!("  [Triangle] Accepting visitor...");
 82          visitor.visit_triangle(self);
 83      }
 84
 85      fn name(&self) -> &str {
 86          "Triangle"
 87      }
 88  }
 89
 90  // Concrete Visitor: Area Calculator
 91  struct AreaCalculator {
 92      total_area: f64,
 93  }
 94
 95  impl AreaCalculator {
 96      fn new() -> Self {
 97          println!("  [AreaCalculator] Initialized with total_area: 0.0");
 98          AreaCalculator { total_area: 0.0 }
 99      }
100
101      fn get_total_area(&self) -> f64 {
102          self.total_area
103      }
104  }
105
106  impl ShapeVisitor for AreaCalculator {
107      fn visit_circle(&mut self, circle: &Circle) {
108          let area = PI * circle.radius * circle.radius;
109          self.total_area += area;
110          println!("    -> Calculated circle area: {:.2}", area);
111      }
112
113      fn visit_rectangle(&mut self, rectangle: &Rectangle) {
114          let area = rectangle.width * rectangle.height;
115          self.total_area += area;
116          println!("    -> Calculated rectangle area: {:.2}", area);
117      }
118
119      fn visit_triangle(&mut self, triangle: &Triangle) {
120          let area = 0.5 * triangle.base * triangle.height;
121          self.total_area += area;
122          println!("    -> Calculated triangle area: {:.2}", area);
123      }
124  }
125
126  // Concrete Visitor: Shape Exporter (exports to different formats)
127  struct ShapeExporter {
128      export_data: Vec<String>,
129  }
130
131  impl ShapeExporter {
132      fn new() -> Self {
133          println!("  [ShapeExporter] Initialized with empty export buffer");
134          ShapeExporter {
135              export_data: Vec::new(),
136          }
137      }
138
139      fn get_export(&self) -> String {
140          self.export_data.join("\n")
141      }
142  }
143
144  impl ShapeVisitor for ShapeExporter {
145      fn visit_circle(&mut self, circle: &Circle) {
146          let json = format!(
147              r#"{{ "type": "circle", "radius": {} }}"#,
148              circle.radius
149          );
150          self.export_data.push(json.clone());
151          println!("    -> Exported circle: {}", json);
152      }
153
154      fn visit_rectangle(&mut self, rectangle: &Rectangle) {
155          let json = format!(
156              r#"{{ "type": "rectangle", "width": {}, "height": {} }}"#,
157              rectangle.width, rectangle.height
158          );
159          self.export_data.push(json.clone());
160          println!("    -> Exported rectangle: {}", json);
161      }
162
163      fn visit_triangle(&mut self, triangle: &Triangle) {
164          let json = format!(
165              r#"{{ "type": "triangle", "base": {}, "height": {} }}"#,
166              triangle.base, triangle.height
167          );
168          self.export_data.push(json.clone());
169          println!("    -> Exported triangle: {}", json);
170      }
171  }
172
173  // Concrete Visitor: Perimeter Calculator
174  struct PerimeterCalculator {
175      total_perimeter: f64,
176  }
177
178  impl PerimeterCalculator {
179      fn new() -> Self {
180          println!("  [PerimeterCalculator] Initialized with total_perimeter: 0.0");
181          PerimeterCalculator { total_perimeter: 0.0 }
182      }
183
184      fn get_total_perimeter(&self) -> f64 {
185          self.total_perimeter
186      }
187  }
188
189  impl ShapeVisitor for PerimeterCalculator {
190      fn visit_circle(&mut self, circle: &Circle) {
191          let perimeter = 2.0 * PI * circle.radius;
192          self.total_perimeter += perimeter;
193          println!("    -> Calculated circle perimeter: {:.2}", perimeter);
194      }
195
196      fn visit_rectangle(&mut self, rectangle: &Rectangle) {
197          let perimeter = 2.0 * (rectangle.width + rectangle.height);
198          self.total_perimeter += perimeter;
199          println!("    -> Calculated rectangle perimeter: {:.2}", perimeter);
200      }
201
202      fn visit_triangle(&mut self, triangle: &Triangle) {
203          // Assuming isoceles triangle for simplicity
204          let side = (triangle.height.powi(2) + (triangle.base / 2.0).powi(2)).sqrt();
205          let perimeter = triangle.base + 2.0 * side;
206          self.total_perimeter += perimeter;
207          println!("    -> Calculated triangle perimeter: {:.2}", perimeter);
208      }
209  }
210
211  // Object structure that holds elements
212  struct ShapeCollection {
213      shapes: Vec<Box<dyn Shape>>,
214  }
215
216  impl ShapeCollection {
217      fn new() -> Self {
218          println!("  [ShapeCollection] Created empty collection");
219          ShapeCollection { shapes: Vec::new() }
220      }
221
222      fn add(&mut self, shape: Box<dyn Shape>) {
223          println!("  [ShapeCollection] Added {} to collection", shape.name());
224          self.shapes.push(shape);
225      }
226
227      fn accept(&self, visitor: &mut dyn ShapeVisitor) {
228          for shape in &self.shapes {
229              shape.accept(visitor);
230          }
231      }
232  }
233
234  fn main() {
235      println!("=== Visitor Design Pattern Demo ===\n");
236
237      // Create shapes
238      println!("1. Creating shapes:");
239      let circle = Box::new(Circle::new(5.0));
240      let rectangle = Box::new(Rectangle::new(4.0, 6.0));
241      let triangle = Box::new(Triangle::new(3.0, 4.0));
242
243      // Add shapes to collection
244      println!("\n2. Building shape collection:");
245      let mut collection = ShapeCollection::new();
246      collection.add(circle);
247      collection.add(rectangle);
248      collection.add(triangle);
249
250      // Use Area Calculator visitor
251      println!("\n3. Applying AreaCalculator visitor:");
252      let mut area_calc = AreaCalculator::new();
253      collection.accept(&mut area_calc);
254      println!("  [Result] Total area: {:.2}\n", area_calc.get_total_area());
255
256      // Use Shape Exporter visitor
257      println!("4. Applying ShapeExporter visitor:");
258      let mut exporter = ShapeExporter::new();
259      collection.accept(&mut exporter);
260      println!("  [Result] Export data:");
261      for line in exporter.get_export().lines() {
262          println!("    {}", line);
263      }
264
265      // Use Perimeter Calculator visitor
266      println!("\n5. Applying PerimeterCalculator visitor:");
267      let mut perimeter_calc = PerimeterCalculator::new();
268      collection.accept(&mut perimeter_calc);
269      println!("  [Result] Total perimeter: {:.2}\n", perimeter_calc.get_total_perimeter());
270
271      // Demonstrate adding new visitor without modifying shapes
272      println!("6. Key Pattern Benefits:");
273      println!("  - New operations added without modifying shape classes");
274      println!("  - Operations on shapes are centralized in visitors");
275      println!("  - Double dispatch achieved via accept/visit methods");
276      println!("  - Easy to add new visitors for different algorithms");
277
278      println!("\n=== Demo Complete ===");
279  }
```

## Program Output

```
=== Visitor Design Pattern Demo ===

1. Creating shapes:
  [Circle] Created with radius: 5
  [Rectangle] Created with width: 4, height: 6
  [Triangle] Created with base: 3, height: 4

2. Building shape collection:
  [ShapeCollection] Created empty collection
  [ShapeCollection] Added Circle to collection
  [ShapeCollection] Added Rectangle to collection
  [ShapeCollection] Added Triangle to collection

3. Applying AreaCalculator visitor:
  [AreaCalculator] Initialized with total_area: 0.0
  [Circle] Accepting visitor...
    -> Calculated circle area: 78.54
  [Rectangle] Accepting visitor...
    -> Calculated rectangle area: 24.00
  [Triangle] Accepting visitor...
    -> Calculated triangle area: 6.00
  [Result] Total area: 108.54

4. Applying ShapeExporter visitor:
  [ShapeExporter] Initialized with empty export buffer
  [Circle] Accepting visitor...
    -> Exported circle: { "type": "circle", "radius": 5 }
  [Rectangle] Accepting visitor...
    -> Exported rectangle: { "type": "rectangle", "width": 4, "height": 6 }
  [Triangle] Accepting visitor...
    -> Exported triangle: { "type": "triangle", "base": 3, "height": 4 }
  [Result] Export data:
    { "type": "circle", "radius": 5 }
    { "type": "rectangle", "width": 4, "height": 6 }
    { "type": "triangle", "base": 3, "height": 4 }

5. Applying PerimeterCalculator visitor:
  [PerimeterCalculator] Initialized with total_perimeter: 0.0
  [Circle] Accepting visitor...
    -> Calculated circle perimeter: 31.42
  [Rectangle] Accepting visitor...
    -> Calculated rectangle perimeter: 20.00
  [Triangle] Accepting visitor...
    -> Calculated triangle perimeter: 11.54
  [Result] Total perimeter: 62.96

6. Key Pattern Benefits:
  - New operations added without modifying shape classes
  - Operations on shapes are centralized in visitors
  - Double dispatch achieved via accept/visit methods
  - Easy to add new visitors for different algorithms

=== Demo Complete ===
```

## Code Annotations

### Key Sections Explained

#### Visitor Trait Definition (Lines 7-11)
The `ShapeVisitor` trait defines the visitor interface with separate visit methods for each concrete element type. This is the core of the Visitor pattern - each method handles a specific shape type. Using `&mut self` allows visitors to accumulate state (like totals).

#### Element Trait Definition (Lines 14-17)
The `Shape` trait defines the element interface that all visitable objects must implement. The `accept` method is crucial - it takes a mutable reference to any type implementing `ShapeVisitor`, enabling double dispatch.

#### Concrete Elements (Lines 19-88)
Three concrete shapes implement the `Shape` trait:
- **Circle** (lines 20-40): Stores radius, delegates to `visit_circle`
- **Rectangle** (lines 43-64): Stores width/height, delegates to `visit_rectangle`
- **Triangle** (lines 67-88): Stores base/height, delegates to `visit_triangle`

Each shape's `accept` method calls the appropriate visitor method, achieving the second dispatch in double dispatch.

#### Area Calculator Visitor (Lines 90-124)
Implements `ShapeVisitor` to calculate areas. Each visit method computes the shape-specific area formula and accumulates results in `total_area`. This demonstrates how algorithms are separated from shape definitions.

#### Shape Exporter Visitor (Lines 126-171)
A different visitor that exports shapes to JSON format. This shows how you can add completely different operations without modifying the shape classes - the core benefit of the Visitor pattern.

#### Perimeter Calculator Visitor (Lines 173-209)
A third visitor demonstrating extensibility. Adding new operations is as simple as implementing a new `ShapeVisitor` - no changes to existing code required.

#### Object Structure (Lines 211-232)
`ShapeCollection` holds a vector of boxed trait objects (`Box<dyn Shape>`). The `accept` method iterates through all shapes and applies the visitor to each. This uses Rust's dynamic dispatch through trait objects.

#### Main Execution (Lines 234-279)
Demonstrates creating shapes, building a collection, and applying three different visitors. Each visitor processes the same shapes but performs different operations.

### Output-to-Source Correlation Table

| Output Line | Source Lines | Description |
|-------------|--------------|-------------|
| `[Circle] Created with radius: 5` | 26, 239 | Circle constructor called via `Circle::new(5.0)` |
| `[Rectangle] Created with width: 4, height: 6` | 50, 240 | Rectangle constructor called |
| `[Triangle] Created with base: 3, height: 4` | 74, 241 | Triangle constructor called |
| `[ShapeCollection] Created empty collection` | 218, 245 | Collection initialized |
| `[ShapeCollection] Added Circle to collection` | 223, 246 | Circle added to collection |
| `[AreaCalculator] Initialized with total_area: 0.0` | 97, 252 | Area calculator visitor created |
| `[Circle] Accepting visitor...` | 33, 229 | Circle's accept method called during iteration |
| `-> Calculated circle area: 78.54` | 110, 107-109 | AreaCalculator's visit_circle computes PI*5*5 |
| `-> Calculated rectangle area: 24.00` | 116, 113-115 | AreaCalculator's visit_rectangle computes 4*6 |
| `-> Calculated triangle area: 6.00` | 122, 119-121 | AreaCalculator's visit_triangle computes 0.5*3*4 |
| `[Result] Total area: 108.54` | 254, 101-103 | Sum of all areas retrieved |
| `[ShapeExporter] Initialized with empty export buffer` | 133, 258 | Exporter visitor created |
| `-> Exported circle: { "type": "circle"...}` | 151, 145-150 | ShapeExporter formats circle as JSON |
| `[PerimeterCalculator] Initialized...` | 180, 267 | Perimeter calculator visitor created |
| `-> Calculated circle perimeter: 31.42` | 193, 190-192 | Computes 2*PI*5 |
| `-> Calculated rectangle perimeter: 20.00` | 199, 196-198 | Computes 2*(4+6) |
| `-> Calculated triangle perimeter: 11.54` | 207, 202-206 | Computes perimeter using Pythagorean theorem |

### Key Characteristics of Visitor Pattern in Rust

1. **Trait-based Double Dispatch**: Rust achieves double dispatch through the combination of the `accept` method (first dispatch on the element type) and the specific `visit_*` method call (second dispatch on the visitor type). This replaces traditional OOP virtual method dispatch.

2. **Ownership and Borrowing**: Visitors take `&mut self` to accumulate state, while shapes are borrowed as `&self` in visit methods. This ensures safe concurrent access patterns and prevents data races.

3. **Dynamic Dispatch with Trait Objects**: The `ShapeCollection` uses `Box<dyn Shape>` for runtime polymorphism. The visitor parameter `&mut dyn ShapeVisitor` also uses dynamic dispatch, enabling flexible visitor application.

4. **Open/Closed Principle**:
   - **Open for extension**: New visitors can be added without modifying shapes
   - **Closed for modification**: Existing shape code remains unchanged
   - Trade-off: Adding new shape types requires updating all visitors

5. **Type Safety**: Rust's type system ensures all visitor implementations handle all shape types. Missing a visit method results in a compile-time error.

6. **No Inheritance Hierarchy**: Unlike traditional OOP implementations, Rust uses traits instead of abstract classes. Each visitor struct independently implements `ShapeVisitor`.

7. **Memory Safety**: Rust's ownership system prevents common visitor pattern pitfalls like dangling references or use-after-free when visitors store references to visited elements.

8. **Compile with rustc**: This code compiles with standard `rustc` without any external dependencies, using only the standard library (`std::f64::consts::PI`).
