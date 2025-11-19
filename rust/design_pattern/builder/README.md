# Builder Design Pattern in Rust

The Builder pattern is a creational design pattern that separates the construction of a complex object from its representation. It allows you to construct objects step-by-step and produce different types and representations of an object using the same construction code.

This example demonstrates building houses with different configurations using:
- A **Product** (`House`) - the complex object being built
- A **Builder Trait** (`HouseBuilder`) - defines the interface for construction steps
- **Concrete Builders** (`LuxuryHouseBuilder`, `SimpleHouseBuilder`) - provide specific implementations
- A **Director** (`ConstructionDirector`) - orchestrates the building process

## Source Code

```rust
  1  // Builder Design Pattern in Rust
  2  // Demonstrates: Builder Trait, Concrete Builder, Director, and Product
  3
  4  // The Product - what we're building
  5  #[derive(Debug, Clone)]
  6  struct House {
  7      foundation: String,
  8      walls: String,
  9      roof: String,
 10      windows: u32,
 11      doors: u32,
 12      garage: bool,
 13      swimming_pool: bool,
 14      garden: bool,
 15  }
 16
 17  impl House {
 18      fn describe(&self) {
 19          println!("\n=== House Description ===");
 20          println!("Foundation: {}", self.foundation);
 21          println!("Walls: {}", self.walls);
 22          println!("Roof: {}", self.roof);
 23          println!("Windows: {}", self.windows);
 24          println!("Doors: {}", self.doors);
 25          println!("Garage: {}", if self.garage { "Yes" } else { "No" });
 26          println!("Swimming Pool: {}", if self.swimming_pool { "Yes" } else { "No" });
 27          println!("Garden: {}", if self.garden { "Yes" } else { "No" });
 28      }
 29  }
 30
 31  // Builder Trait - defines the interface for building parts
 32  trait HouseBuilder {
 33      fn new() -> Self where Self: Sized;
 34      fn build_foundation(&mut self) -> &mut Self;
 35      fn build_walls(&mut self) -> &mut Self;
 36      fn build_roof(&mut self) -> &mut Self;
 37      fn build_windows(&mut self, count: u32) -> &mut Self;
 38      fn build_doors(&mut self, count: u32) -> &mut Self;
 39      fn build_garage(&mut self) -> &mut Self;
 40      fn build_swimming_pool(&mut self) -> &mut Self;
 41      fn build_garden(&mut self) -> &mut Self;
 42      fn get_result(&self) -> House;
 43  }
 44
 45  // Concrete Builder - builds a luxury house
 46  struct LuxuryHouseBuilder {
 47      house: House,
 48  }
 49
 50  impl HouseBuilder for LuxuryHouseBuilder {
 51      fn new() -> Self {
 52          println!("[LuxuryHouseBuilder] Initializing new luxury house builder");
 53          LuxuryHouseBuilder {
 54              house: House {
 55                  foundation: String::new(),
 56                  walls: String::new(),
 57                  roof: String::new(),
 58                  windows: 0,
 59                  doors: 0,
 60                  garage: false,
 61                  swimming_pool: false,
 62                  garden: false,
 63              },
 64          }
 65      }
 66
 67      fn build_foundation(&mut self) -> &mut Self {
 68          println!("[LuxuryHouseBuilder] Building reinforced concrete foundation");
 69          self.house.foundation = "Reinforced Concrete".to_string();
 70          self
 71      }
 72
 73      fn build_walls(&mut self) -> &mut Self {
 74          println!("[LuxuryHouseBuilder] Building brick walls with insulation");
 75          self.house.walls = "Brick with Premium Insulation".to_string();
 76          self
 77      }
 78
 79      fn build_roof(&mut self) -> &mut Self {
 80          println!("[LuxuryHouseBuilder] Building slate tile roof");
 81          self.house.roof = "Slate Tiles".to_string();
 82          self
 83      }
 84
 85      fn build_windows(&mut self, count: u32) -> &mut Self {
 86          println!("[LuxuryHouseBuilder] Installing {} double-glazed windows", count);
 87          self.house.windows = count;
 88          self
 89      }
 90
 91      fn build_doors(&mut self, count: u32) -> &mut Self {
 92          println!("[LuxuryHouseBuilder] Installing {} oak doors", count);
 93          self.house.doors = count;
 94          self
 95      }
 96
 97      fn build_garage(&mut self) -> &mut Self {
 98          println!("[LuxuryHouseBuilder] Building 3-car garage");
 99          self.house.garage = true;
100          self
101      }
102
103      fn build_swimming_pool(&mut self) -> &mut Self {
104          println!("[LuxuryHouseBuilder] Building heated swimming pool");
105          self.house.swimming_pool = true;
106          self
107      }
108
109      fn build_garden(&mut self) -> &mut Self {
110          println!("[LuxuryHouseBuilder] Creating landscaped garden");
111          self.house.garden = true;
112          self
113      }
114
115      fn get_result(&self) -> House {
116          println!("[LuxuryHouseBuilder] Luxury house construction complete!");
117          self.house.clone()
118      }
119  }
120
121  // Concrete Builder - builds a simple house
122  struct SimpleHouseBuilder {
123      house: House,
124  }
125
126  impl HouseBuilder for SimpleHouseBuilder {
127      fn new() -> Self {
128          println!("[SimpleHouseBuilder] Initializing new simple house builder");
129          SimpleHouseBuilder {
130              house: House {
131                  foundation: String::new(),
132                  walls: String::new(),
133                  roof: String::new(),
134                  windows: 0,
135                  doors: 0,
136                  garage: false,
137                  swimming_pool: false,
138                  garden: false,
139              },
140          }
141      }
142
143      fn build_foundation(&mut self) -> &mut Self {
144          println!("[SimpleHouseBuilder] Building concrete slab foundation");
145          self.house.foundation = "Concrete Slab".to_string();
146          self
147      }
148
149      fn build_walls(&mut self) -> &mut Self {
150          println!("[SimpleHouseBuilder] Building wood frame walls");
151          self.house.walls = "Wood Frame".to_string();
152          self
153      }
154
155      fn build_roof(&mut self) -> &mut Self {
156          println!("[SimpleHouseBuilder] Building asphalt shingle roof");
157          self.house.roof = "Asphalt Shingles".to_string();
158          self
159      }
160
161      fn build_windows(&mut self, count: u32) -> &mut Self {
162          println!("[SimpleHouseBuilder] Installing {} standard windows", count);
163          self.house.windows = count;
164          self
165      }
166
167      fn build_doors(&mut self, count: u32) -> &mut Self {
168          println!("[SimpleHouseBuilder] Installing {} standard doors", count);
169          self.house.doors = count;
170          self
171      }
172
173      fn build_garage(&mut self) -> &mut Self {
174          println!("[SimpleHouseBuilder] Building 1-car garage");
175          self.house.garage = true;
176          self
177      }
178
179      fn build_swimming_pool(&mut self) -> &mut Self {
180          println!("[SimpleHouseBuilder] Skipping swimming pool (not included)");
181          self.house.swimming_pool = false;
182          self
183      }
184
185      fn build_garden(&mut self) -> &mut Self {
186          println!("[SimpleHouseBuilder] Creating basic lawn");
187          self.house.garden = true;
188          self
189      }
190
191      fn get_result(&self) -> House {
192          println!("[SimpleHouseBuilder] Simple house construction complete!");
193          self.house.clone()
194      }
195  }
196
197  // Director - orchestrates the building process
198  struct ConstructionDirector;
199
200  impl ConstructionDirector {
201      fn construct_full_house<T: HouseBuilder>(builder: &mut T) -> House {
202          println!("\n>>> Director: Starting full house construction");
203          builder
204              .build_foundation()
205              .build_walls()
206              .build_roof()
207              .build_windows(8)
208              .build_doors(4)
209              .build_garage()
210              .build_swimming_pool()
211              .build_garden();
212          println!(">>> Director: Full house construction finished\n");
213          builder.get_result()
214      }
215
216      fn construct_minimal_house<T: HouseBuilder>(builder: &mut T) -> House {
217          println!("\n>>> Director: Starting minimal house construction");
218          builder
219              .build_foundation()
220              .build_walls()
221              .build_roof()
222              .build_windows(4)
223              .build_doors(2);
224          println!(">>> Director: Minimal house construction finished\n");
225          builder.get_result()
226      }
227  }
228
229  fn main() {
230      println!("==============================================");
231      println!("   Builder Design Pattern - House Example");
232      println!("==============================================");
233
234      // Build a luxury house using the director
235      println!("\n--- Building Luxury House with Director ---");
236      let mut luxury_builder = LuxuryHouseBuilder::new();
237      let luxury_house = ConstructionDirector::construct_full_house(&mut luxury_builder);
238      luxury_house.describe();
239
240      // Build a simple minimal house using the director
241      println!("\n\n--- Building Simple Minimal House with Director ---");
242      let mut simple_builder = SimpleHouseBuilder::new();
243      let simple_house = ConstructionDirector::construct_minimal_house(&mut simple_builder);
244      simple_house.describe();
245
246      // Direct builder usage with method chaining (without director)
247      println!("\n\n--- Custom House using Builder Directly ---");
248      let mut custom_builder = LuxuryHouseBuilder::new();
249      custom_builder
250          .build_foundation()
251          .build_walls()
252          .build_roof()
253          .build_windows(12)
254          .build_doors(6)
255          .build_swimming_pool();
256      let custom_house = custom_builder.get_result();
257      custom_house.describe();
258
259      println!("\n==============================================");
260      println!("   Builder Pattern Demonstration Complete");
261      println!("==============================================");
262  }
```

## Program Output

```
==============================================
   Builder Design Pattern - House Example
==============================================

--- Building Luxury House with Director ---
[LuxuryHouseBuilder] Initializing new luxury house builder

>>> Director: Starting full house construction
[LuxuryHouseBuilder] Building reinforced concrete foundation
[LuxuryHouseBuilder] Building brick walls with insulation
[LuxuryHouseBuilder] Building slate tile roof
[LuxuryHouseBuilder] Installing 8 double-glazed windows
[LuxuryHouseBuilder] Installing 4 oak doors
[LuxuryHouseBuilder] Building 3-car garage
[LuxuryHouseBuilder] Building heated swimming pool
[LuxuryHouseBuilder] Creating landscaped garden
>>> Director: Full house construction finished

[LuxuryHouseBuilder] Luxury house construction complete!

=== House Description ===
Foundation: Reinforced Concrete
Walls: Brick with Premium Insulation
Roof: Slate Tiles
Windows: 8
Doors: 4
Garage: Yes
Swimming Pool: Yes
Garden: Yes


--- Building Simple Minimal House with Director ---
[SimpleHouseBuilder] Initializing new simple house builder

>>> Director: Starting minimal house construction
[SimpleHouseBuilder] Building concrete slab foundation
[SimpleHouseBuilder] Building wood frame walls
[SimpleHouseBuilder] Building asphalt shingle roof
[SimpleHouseBuilder] Installing 4 standard windows
[SimpleHouseBuilder] Installing 2 standard doors
>>> Director: Minimal house construction finished

[SimpleHouseBuilder] Simple house construction complete!

=== House Description ===
Foundation: Concrete Slab
Walls: Wood Frame
Roof: Asphalt Shingles
Windows: 4
Doors: 2
Garage: No
Swimming Pool: No
Garden: No


--- Custom House using Builder Directly ---
[LuxuryHouseBuilder] Initializing new luxury house builder
[LuxuryHouseBuilder] Building reinforced concrete foundation
[LuxuryHouseBuilder] Building brick walls with insulation
[LuxuryHouseBuilder] Building slate tile roof
[LuxuryHouseBuilder] Installing 12 double-glazed windows
[LuxuryHouseBuilder] Installing 6 oak doors
[LuxuryHouseBuilder] Building heated swimming pool
[LuxuryHouseBuilder] Luxury house construction complete!

=== House Description ===
Foundation: Reinforced Concrete
Walls: Brick with Premium Insulation
Roof: Slate Tiles
Windows: 12
Doors: 6
Garage: No
Swimming Pool: Yes
Garden: No

==============================================
   Builder Pattern Demonstration Complete
==============================================
```

## Code Annotations

### Key Sections Explained

#### Lines 5-15: Product Definition
The `House` struct represents the complex object being built. It uses `#[derive(Debug, Clone)]` to allow debugging output and cloning (needed when `get_result()` returns a copy of the built house).

#### Lines 32-43: Builder Trait
The `HouseBuilder` trait defines the interface that all concrete builders must implement. Each method returns `&mut Self` to enable method chaining (fluent interface). The `where Self: Sized` constraint on `new()` is required because trait objects cannot call methods that return `Self`.

#### Lines 50-119: LuxuryHouseBuilder
A concrete builder that creates high-end houses with premium materials. Each build method:
1. Prints a step-by-step message (lines 68, 74, 80, etc.)
2. Sets the corresponding house field
3. Returns `&mut Self` for chaining

#### Lines 126-195: SimpleHouseBuilder
Another concrete builder with different implementations. Note how `build_swimming_pool()` (line 179-183) explicitly sets `swimming_pool = false`, showing that builders can have different behaviors for the same interface.

#### Lines 198-227: Director
The `ConstructionDirector` contains construction algorithms. It uses generics (`<T: HouseBuilder>`) to work with any builder implementing the trait. This demonstrates:
- `construct_full_house`: Builds everything (lines 201-214)
- `construct_minimal_house`: Builds only essentials (lines 216-226)

#### Lines 229-262: Main Function
Demonstrates three usage patterns:
1. **Director with LuxuryHouseBuilder** (lines 236-238): Full house construction
2. **Director with SimpleHouseBuilder** (lines 242-244): Minimal house construction
3. **Direct builder usage** (lines 248-257): Custom configuration without director

### Output to Source Code Correlation

| Output Line | Source Line(s) | Description |
|-------------|----------------|-------------|
| `[LuxuryHouseBuilder] Initializing new luxury house builder` | 52 | Builder initialization in `new()` |
| `>>> Director: Starting full house construction` | 202 | Director begins orchestration |
| `[LuxuryHouseBuilder] Building reinforced concrete foundation` | 68 | Foundation step executed |
| `[LuxuryHouseBuilder] Building brick walls with insulation` | 74 | Walls step executed |
| `[LuxuryHouseBuilder] Building slate tile roof` | 80 | Roof step executed |
| `[LuxuryHouseBuilder] Installing 8 double-glazed windows` | 86 | Windows with count parameter |
| `[LuxuryHouseBuilder] Installing 4 oak doors` | 92 | Doors with count parameter |
| `[LuxuryHouseBuilder] Building 3-car garage` | 98 | Garage step executed |
| `[LuxuryHouseBuilder] Building heated swimming pool` | 104 | Pool step executed |
| `[LuxuryHouseBuilder] Creating landscaped garden` | 110 | Garden step executed |
| `>>> Director: Full house construction finished` | 212 | Director completes orchestration |
| `[LuxuryHouseBuilder] Luxury house construction complete!` | 116 | `get_result()` called |
| `=== House Description ===` | 19 | `describe()` method output |
| `Foundation: Reinforced Concrete` | 20 | House field display |
| `[SimpleHouseBuilder] Initializing new simple house builder` | 128 | Different builder initialization |
| `[SimpleHouseBuilder] Building concrete slab foundation` | 144 | Different foundation type |
| `[SimpleHouseBuilder] Building wood frame walls` | 150 | Different wall material |
| `[SimpleHouseBuilder] Installing 4 standard windows` | 162 | Minimal house configuration (4 windows) |
| `Garage: No` | 25 | Minimal house doesn't include garage |

### Key Characteristics of Builder Pattern in Rust

1. **Trait-based Interface**: Rust uses traits to define the builder interface, allowing for static dispatch when using generics or dynamic dispatch with trait objects.

2. **Method Chaining with `&mut Self`**: Returning `&mut Self` from builder methods enables the fluent interface pattern, allowing calls like `builder.build_foundation().build_walls().build_roof()`.

3. **Ownership and Borrowing**: The director takes `&mut T` (mutable reference) to the builder, allowing it to modify the builder without taking ownership. This lets the caller retain ownership and access the result.

4. **Generic Director**: Using `<T: HouseBuilder>` makes the director work with any type implementing the trait, promoting code reuse and flexibility.

5. **Clone for Result**: The `get_result()` method clones the house, which is a common pattern when the builder needs to be reusable. Alternatively, you could use `std::mem::take()` or consume the builder.

6. **No Inheritance**: Unlike object-oriented languages, Rust doesn't use inheritance. Instead, it uses composition (builder holds the product) and traits (defining the interface).

7. **Type Safety**: The compiler ensures all trait methods are implemented correctly, and the pattern provides compile-time guarantees about the construction process.

8. **Optional Director**: The pattern works with or without a director. Direct builder usage (lines 248-257) allows custom configurations not covered by predefined director methods.
