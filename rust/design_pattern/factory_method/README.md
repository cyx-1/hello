# Factory Method Design Pattern in Rust

The Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. Instead of calling a constructor directly, a factory method is called to create the object.

This implementation demonstrates a logistics application where different types of transport (Truck, Ship, Airplane) are created by their respective logistics handlers (RoadLogistics, SeaLogistics, AirLogistics).

## Source Code

```rust
  1  // Factory Method Design Pattern in Rust
  2  // Demonstrates creating different types of transport for a logistics application
  3
  4  // Product trait - defines the interface for objects created by the factory method
  5  trait Transport {
  6      fn deliver(&self) -> String;
  7      fn get_capacity(&self) -> u32;
  8  }
  9
 10  // Concrete Product: Truck
 11  struct Truck {
 12      cargo_weight: u32,
 13  }
 14
 15  impl Transport for Truck {
 16      fn deliver(&self) -> String {
 17          format!("Delivering by land in a truck with {} tons of cargo", self.cargo_weight)
 18      }
 19
 20      fn get_capacity(&self) -> u32 {
 21          self.cargo_weight
 22      }
 23  }
 24
 25  // Concrete Product: Ship
 26  struct Ship {
 27      container_count: u32,
 28  }
 29
 30  impl Transport for Ship {
 31      fn deliver(&self) -> String {
 32          format!("Delivering by sea in a ship with {} containers", self.container_count)
 33      }
 34
 35      fn get_capacity(&self) -> u32 {
 36          self.container_count * 20 // Each container holds ~20 tons
 37      }
 38  }
 39
 40  // Concrete Product: Airplane
 41  struct Airplane {
 42      cargo_volume: u32,
 43  }
 44
 45  impl Transport for Airplane {
 46      fn deliver(&self) -> String {
 47          format!("Delivering by air in an airplane with {} cubic meters of cargo", self.cargo_volume)
 48      }
 49
 50      fn get_capacity(&self) -> u32 {
 51          self.cargo_volume
 52      }
 53  }
 54
 55  // Creator trait - declares the factory method
 56  trait Logistics {
 57      // Factory method - subclasses override this to create specific products
 58      fn create_transport(&self) -> Box<dyn Transport>;
 59
 60      // Business logic that uses the factory method
 61      fn plan_delivery(&self) {
 62          println!("Planning delivery logistics...");
 63          let transport = self.create_transport();
 64          println!("  -> Transport created with capacity: {} units", transport.get_capacity());
 65          println!("  -> {}", transport.deliver());
 66      }
 67  }
 68
 69  // Concrete Creator: RoadLogistics
 70  struct RoadLogistics {
 71      cargo_weight: u32,
 72  }
 73
 74  impl Logistics for RoadLogistics {
 75      fn create_transport(&self) -> Box<dyn Transport> {
 76          println!("  [Factory] Creating Truck transport");
 77          Box::new(Truck { cargo_weight: self.cargo_weight })
 78      }
 79  }
 80
 81  // Concrete Creator: SeaLogistics
 82  struct SeaLogistics {
 83      container_count: u32,
 84  }
 85
 86  impl Logistics for SeaLogistics {
 87      fn create_transport(&self) -> Box<dyn Transport> {
 88          println!("  [Factory] Creating Ship transport");
 89          Box::new(Ship { container_count: self.container_count })
 90      }
 91  }
 92
 93  // Concrete Creator: AirLogistics
 94  struct AirLogistics {
 95      cargo_volume: u32,
 96  }
 97
 98  impl Logistics for AirLogistics {
 99      fn create_transport(&self) -> Box<dyn Transport> {
100          println!("  [Factory] Creating Airplane transport");
101          Box::new(Airplane { cargo_volume: self.cargo_volume })
102      }
103  }
104
105  // Client code that works with creators through the base trait
106  fn execute_logistics(logistics: &dyn Logistics) {
107      logistics.plan_delivery();
108  }
109
110  fn main() {
111      println!("=== Factory Method Pattern Demo ===\n");
112
113      // Create different logistics operations
114      println!("1. Road Logistics (Truck):");
115      let road = RoadLogistics { cargo_weight: 10 };
116      execute_logistics(&road);
117
118      println!("\n2. Sea Logistics (Ship):");
119      let sea = SeaLogistics { container_count: 50 };
120      execute_logistics(&sea);
121
122      println!("\n3. Air Logistics (Airplane):");
123      let air = AirLogistics { cargo_volume: 100 };
124      execute_logistics(&air);
125
126      println!("\n=== Demonstrating Polymorphism ===\n");
127
128      // Store different logistics in a vector
129      let logistics_list: Vec<Box<dyn Logistics>> = vec![
130          Box::new(RoadLogistics { cargo_weight: 25 }),
131          Box::new(SeaLogistics { container_count: 100 }),
132          Box::new(AirLogistics { cargo_volume: 200 }),
133      ];
134
135      for (i, logistics) in logistics_list.iter().enumerate() {
136          println!("Operation {}:", i + 1);
137          logistics.plan_delivery();
138          println!();
139      }
140
141      println!("=== Pattern Complete ===");
142  }
```

## Program Output

```
=== Factory Method Pattern Demo ===

1. Road Logistics (Truck):
Planning delivery logistics...
  [Factory] Creating Truck transport
  -> Transport created with capacity: 10 units
  -> Delivering by land in a truck with 10 tons of cargo

2. Sea Logistics (Ship):
Planning delivery logistics...
  [Factory] Creating Ship transport
  -> Transport created with capacity: 1000 units
  -> Delivering by sea in a ship with 50 containers

3. Air Logistics (Airplane):
Planning delivery logistics...
  [Factory] Creating Airplane transport
  -> Transport created with capacity: 100 units
  -> Delivering by air in an airplane with 100 cubic meters of cargo

=== Demonstrating Polymorphism ===

Operation 1:
Planning delivery logistics...
  [Factory] Creating Truck transport
  -> Transport created with capacity: 25 units
  -> Delivering by land in a truck with 25 tons of cargo

Operation 2:
Planning delivery logistics...
  [Factory] Creating Ship transport
  -> Transport created with capacity: 2000 units
  -> Delivering by sea in a ship with 100 containers

Operation 3:
Planning delivery logistics...
  [Factory] Creating Airplane transport
  -> Transport created with capacity: 200 units
  -> Delivering by air in an airplane with 200 cubic meters of cargo

=== Pattern Complete ===
```

## Code Annotations

### Key Sections Explained

**Lines 5-8: Product Trait**
The `Transport` trait defines the interface that all concrete products must implement. This is the abstraction that allows the factory method to return different types while maintaining a consistent interface.

**Lines 10-53: Concrete Products**
Three concrete products (`Truck`, `Ship`, `Airplane`) implement the `Transport` trait. Each provides its own implementation of `deliver()` and `get_capacity()`, demonstrating how different products can have unique behavior while sharing a common interface.

**Lines 55-67: Creator Trait**
The `Logistics` trait is the core of the Factory Method pattern. It declares:
- `create_transport()` (line 58): The factory method that concrete creators must implement
- `plan_delivery()` (lines 61-66): Business logic that uses the factory method, demonstrating how the creator can work with products without knowing their concrete types

**Lines 69-103: Concrete Creators**
Each concrete creator (`RoadLogistics`, `SeaLogistics`, `AirLogistics`) implements the `create_transport()` factory method to return its specific product type. The key insight is that the `plan_delivery()` method remains unchanged across all creators.

**Lines 105-108: Client Code**
The `execute_logistics()` function demonstrates how client code can work with any logistics type through the trait object `&dyn Logistics`, without knowing which specific creator or product will be used.

**Lines 129-133: Polymorphic Collection**
This section demonstrates Rust's dynamic dispatch by storing different concrete creators in a single vector of trait objects, then iterating over them polymorphically.

### Output to Source Code Correlation

| Output Line | Source Lines | Description |
|-------------|--------------|-------------|
| `=== Factory Method Pattern Demo ===` | 111 | Main function header |
| `1. Road Logistics (Truck):` | 114 | First logistics type label |
| `Planning delivery logistics...` | 62 | plan_delivery() starts execution |
| `[Factory] Creating Truck transport` | 76 | RoadLogistics factory method called |
| `-> Transport created with capacity: 10 units` | 64 | Calls get_capacity() on Truck (line 20-22) |
| `-> Delivering by land in a truck with 10 tons of cargo` | 65 | Calls deliver() on Truck (line 16-18) |
| `2. Sea Logistics (Ship):` | 118 | Second logistics type label |
| `[Factory] Creating Ship transport` | 88 | SeaLogistics factory method called |
| `-> Transport created with capacity: 1000 units` | 64 | Calls get_capacity() on Ship (line 35-37), calculates 50 * 20 |
| `-> Delivering by sea in a ship with 50 containers` | 65 | Calls deliver() on Ship (line 31-33) |
| `3. Air Logistics (Airplane):` | 122 | Third logistics type label |
| `[Factory] Creating Airplane transport` | 100 | AirLogistics factory method called |
| `-> Transport created with capacity: 100 units` | 64 | Calls get_capacity() on Airplane (line 50-52) |
| `=== Demonstrating Polymorphism ===` | 126 | Polymorphism section header |
| `Operation 1:` through `Operation 3:` | 136 | Loop iteration output |

### Key Characteristics of Factory Method in Rust

1. **Trait-based Abstraction**: Rust uses traits instead of abstract classes. The `Transport` trait (lines 5-8) and `Logistics` trait (lines 56-67) define the contracts for products and creators.

2. **Dynamic Dispatch with Box<dyn Trait>**: The factory method returns `Box<dyn Transport>` (line 58) to enable runtime polymorphism, allowing different concrete types to be returned from the same method signature.

3. **Ownership Semantics**: The factory method transfers ownership of the created object to the caller via `Box`, ensuring clear memory management without garbage collection.

4. **Default Method Implementations**: Rust traits can have default implementations (lines 61-66), allowing the business logic to be shared across all concrete creators while only the factory method needs to be overridden.

5. **No Inheritance Required**: Unlike OOP languages, Rust achieves the Factory Method pattern through trait composition rather than class inheritance, making it more flexible and avoiding inheritance hierarchies.

6. **Compile-time Safety**: The Rust compiler ensures that all concrete creators properly implement the factory method, preventing runtime errors from missing implementations.

## Compilation

This code can be compiled with standard rustc:

```bash
rustc main_factory_method.rs -o main_factory_method && ./main_factory_method
```

No external dependencies are required.
