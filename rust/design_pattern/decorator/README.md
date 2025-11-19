# Decorator Design Pattern in Rust

## Description

The Decorator pattern attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality. In Rust, this pattern is implemented using trait objects (`Box<dyn Trait>`) to allow decorators to wrap any component that implements the base trait.

This example demonstrates a coffee shop ordering system where beverages can be decorated with various additions (milk, sugar, whipped cream, caramel), each adding to the cost and description.

## Source Code

```rust
  1  // Decorator Design Pattern in Rust
  2  // Demonstrates adding behaviors dynamically using trait objects
  3
  4  // Base trait that defines the component interface
  5  trait Beverage {
  6      fn cost(&self) -> f64;
  7      fn description(&self) -> String;
  8  }
  9
 10  // Concrete component: Simple Coffee
 11  struct SimpleCoffee;
 12
 13  impl Beverage for SimpleCoffee {
 14      fn cost(&self) -> f64 {
 15          println!("  [SimpleCoffee] Base cost: $2.00");
 16          2.00
 17      }
 18
 19      fn description(&self) -> String {
 20          String::from("Simple Coffee")
 21      }
 22  }
 23
 24  // Concrete component: Espresso
 25  struct Espresso;
 26
 27  impl Beverage for Espresso {
 28      fn cost(&self) -> f64 {
 29          println!("  [Espresso] Base cost: $3.00");
 30          3.00
 31      }
 32
 33      fn description(&self) -> String {
 34          String::from("Espresso")
 35      }
 36  }
 37
 38  // Decorator: Milk
 39  struct MilkDecorator {
 40      beverage: Box<dyn Beverage>,
 41  }
 42
 43  impl MilkDecorator {
 44      fn new(beverage: Box<dyn Beverage>) -> Self {
 45          MilkDecorator { beverage }
 46      }
 47  }
 48
 49  impl Beverage for MilkDecorator {
 50      fn cost(&self) -> f64 {
 51          let base_cost = self.beverage.cost();
 52          println!("  [MilkDecorator] Adding milk: +$0.50");
 53          base_cost + 0.50
 54      }
 55
 56      fn description(&self) -> String {
 57          format!("{}, Milk", self.beverage.description())
 58      }
 59  }
 60
 61  // Decorator: Sugar
 62  struct SugarDecorator {
 63      beverage: Box<dyn Beverage>,
 64  }
 65
 66  impl SugarDecorator {
 67      fn new(beverage: Box<dyn Beverage>) -> Self {
 68          SugarDecorator { beverage }
 69      }
 70  }
 71
 72  impl Beverage for SugarDecorator {
 73      fn cost(&self) -> f64 {
 74          let base_cost = self.beverage.cost();
 75          println!("  [SugarDecorator] Adding sugar: +$0.25");
 76          base_cost + 0.25
 77      }
 78
 79      fn description(&self) -> String {
 80          format!("{}, Sugar", self.beverage.description())
 81      }
 82  }
 83
 84  // Decorator: Whipped Cream
 85  struct WhipDecorator {
 86      beverage: Box<dyn Beverage>,
 87  }
 88
 89  impl WhipDecorator {
 90      fn new(beverage: Box<dyn Beverage>) -> Self {
 91          WhipDecorator { beverage }
 92      }
 93  }
 94
 95  impl Beverage for WhipDecorator {
 96      fn cost(&self) -> f64 {
 97          let base_cost = self.beverage.cost();
 98          println!("  [WhipDecorator] Adding whipped cream: +$0.75");
 99          base_cost + 0.75
100      }
101
102      fn description(&self) -> String {
103          format!("{}, Whip", self.beverage.description())
104      }
105  }
106
107  // Decorator: Caramel
108  struct CaramelDecorator {
109      beverage: Box<dyn Beverage>,
110  }
111
112  impl CaramelDecorator {
113      fn new(beverage: Box<dyn Beverage>) -> Self {
114          CaramelDecorator { beverage }
115      }
116  }
117
118  impl Beverage for CaramelDecorator {
119      fn cost(&self) -> f64 {
120          let base_cost = self.beverage.cost();
121          println!("  [CaramelDecorator] Adding caramel: +$0.60");
122          base_cost + 0.60
123      }
124
125      fn description(&self) -> String {
126          format!("{}, Caramel", self.beverage.description())
127      }
128  }
129
130  fn main() {
131      println!("=== Decorator Pattern: Coffee Shop Example ===\n");
132
133      // Example 1: Simple coffee with no decorations
134      println!("Order 1: Plain Simple Coffee");
135      println!("---------------------------------");
136      let coffee = SimpleCoffee;
137      println!("Description: {}", coffee.description());
138      print!("Calculating cost:\n");
139      let total = coffee.cost();
140      println!("Total: ${:.2}\n", total);
141
142      // Example 2: Coffee with milk
143      println!("Order 2: Coffee with Milk");
144      println!("---------------------------------");
145      let coffee_with_milk = MilkDecorator::new(Box::new(SimpleCoffee));
146      println!("Description: {}", coffee_with_milk.description());
147      print!("Calculating cost:\n");
148      let total = coffee_with_milk.cost();
149      println!("Total: ${:.2}\n", total);
150
151      // Example 3: Coffee with milk and sugar (stacked decorators)
152      println!("Order 3: Coffee with Milk and Sugar");
153      println!("---------------------------------");
154      let sweet_coffee = SugarDecorator::new(
155          Box::new(MilkDecorator::new(Box::new(SimpleCoffee)))
156      );
157      println!("Description: {}", sweet_coffee.description());
158      print!("Calculating cost:\n");
159      let total = sweet_coffee.cost();
160      println!("Total: ${:.2}\n", total);
161
162      // Example 4: Fully loaded espresso
163      println!("Order 4: Espresso with Milk, Sugar, Whip, and Caramel");
164      println!("---------------------------------");
165      let fancy_espresso = CaramelDecorator::new(
166          Box::new(WhipDecorator::new(
167              Box::new(SugarDecorator::new(
168                  Box::new(MilkDecorator::new(Box::new(Espresso)))
169              ))
170          ))
171      );
172      println!("Description: {}", fancy_espresso.description());
173      print!("Calculating cost:\n");
174      let total = fancy_espresso.cost();
175      println!("Total: ${:.2}\n", total);
176
177      // Example 5: Double milk coffee
178      println!("Order 5: Coffee with Double Milk");
179      println!("---------------------------------");
180      let double_milk = MilkDecorator::new(
181          Box::new(MilkDecorator::new(Box::new(SimpleCoffee)))
182      );
183      println!("Description: {}", double_milk.description());
184      print!("Calculating cost:\n");
185      let total = double_milk.cost();
186      println!("Total: ${:.2}\n", total);
187
188      println!("=== Pattern Demonstration Complete ===");
189  }
```

## Program Output

```
=== Decorator Pattern: Coffee Shop Example ===

Order 1: Plain Simple Coffee
---------------------------------
Description: Simple Coffee
Calculating cost:
  [SimpleCoffee] Base cost: $2.00
Total: $2.00

Order 2: Coffee with Milk
---------------------------------
Description: Simple Coffee, Milk
Calculating cost:
  [SimpleCoffee] Base cost: $2.00
  [MilkDecorator] Adding milk: +$0.50
Total: $2.50

Order 3: Coffee with Milk and Sugar
---------------------------------
Description: Simple Coffee, Milk, Sugar
Calculating cost:
  [SimpleCoffee] Base cost: $2.00
  [MilkDecorator] Adding milk: +$0.50
  [SugarDecorator] Adding sugar: +$0.25
Total: $2.75

Order 4: Espresso with Milk, Sugar, Whip, and Caramel
---------------------------------
Description: Espresso, Milk, Sugar, Whip, Caramel
Calculating cost:
  [Espresso] Base cost: $3.00
  [MilkDecorator] Adding milk: +$0.50
  [SugarDecorator] Adding sugar: +$0.25
  [WhipDecorator] Adding whipped cream: +$0.75
  [CaramelDecorator] Adding caramel: +$0.60
Total: $5.10

Order 5: Coffee with Double Milk
---------------------------------
Description: Simple Coffee, Milk, Milk
Calculating cost:
  [SimpleCoffee] Base cost: $2.00
  [MilkDecorator] Adding milk: +$0.50
  [MilkDecorator] Adding milk: +$0.50
Total: $3.00

=== Pattern Demonstration Complete ===
```

## Code Annotations

### Key Sections Explained

#### Lines 5-8: Component Trait Definition
The `Beverage` trait defines the interface that both concrete components and decorators must implement. This is the foundation of the pattern - all participants share this common interface.

#### Lines 10-22, 24-36: Concrete Components
`SimpleCoffee` and `Espresso` are the base objects that can be decorated. They implement the `Beverage` trait directly with their base costs ($2.00 and $3.00 respectively).

#### Lines 38-59: Decorator Structure (MilkDecorator)
Each decorator:
- Contains a `Box<dyn Beverage>` field (line 40) - this allows wrapping any Beverage implementation
- Has a `new()` constructor that takes ownership of the wrapped beverage (lines 43-46)
- Implements `Beverage` trait, delegating to the wrapped object and adding its behavior (lines 49-58)

#### Lines 50-54: Decorator Cost Calculation Pattern
The decorator first calls the wrapped beverage's `cost()` method (line 51), then adds its own contribution (line 53). This creates a chain of responsibility where each decorator adds to the total.

#### Lines 145, 154-156, 165-171: Decorator Stacking
Shows how decorators can be nested:
- Line 145: Single decorator wrapping a component
- Lines 154-156: Two decorators stacked
- Lines 165-171: Four decorators creating a complex decorated object

#### Lines 180-182: Same Decorator Multiple Times
Demonstrates that the same decorator type can be applied multiple times (double milk), showing the flexibility of the pattern.

### Output to Source Code Correlation

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| "Order 1: Plain Simple Coffee" | 134 | First example header |
| "Description: Simple Coffee" | 137, 19-20 | Calls `description()` on SimpleCoffee |
| "[SimpleCoffee] Base cost: $2.00" | 139, 14-16 | Calls `cost()` on base component |
| "Total: $2.00" | 140 | Final cost with no decorations |
| "Description: Simple Coffee, Milk" | 146, 56-58 | MilkDecorator builds description by prepending wrapped description |
| "[SimpleCoffee] Base cost: $2.00" then "[MilkDecorator] Adding milk" | 148, 50-53 | Decorator chain: first inner, then outer |
| "Total: $2.50" | 149 | $2.00 + $0.50 = $2.50 |
| "Description: Simple Coffee, Milk, Sugar" | 157, 79-81, 56-58 | Chain of descriptions built from inside out |
| Cost calculation chain for Order 3 | 159, 73-76, 50-53, 14-16 | Three-level chain: SimpleCoffee -> Milk -> Sugar |
| "Total: $2.75" | 160 | $2.00 + $0.50 + $0.25 = $2.75 |
| Five-level description in Order 4 | 172 | All decorators contribute to description |
| Five cost components | 174, 119-122, 96-99, 73-76, 50-53, 28-30 | Full decorator stack unwinding |
| "Total: $5.10" | 175 | $3.00 + $0.50 + $0.25 + $0.75 + $0.60 = $5.10 |
| "Description: Simple Coffee, Milk, Milk" | 183 | Same decorator applied twice |
| Double milk cost | 185 | MilkDecorator called twice in chain |

### Key Characteristics of the Decorator Pattern in Rust

1. **Trait Objects for Polymorphism**: Using `Box<dyn Beverage>` enables runtime polymorphism, allowing any `Beverage` implementor to be wrapped.

2. **Ownership Through Boxing**: Rust's ownership model requires decorators to own their wrapped components. `Box<dyn Trait>` provides heap allocation and ownership semantics.

3. **Composition Over Inheritance**: Rust doesn't have traditional inheritance. The Decorator pattern naturally fits Rust's composition-based approach using traits.

4. **Open/Closed Principle**: New decorators can be added without modifying existing code. Just create a new struct that wraps `Box<dyn Beverage>`.

5. **Runtime Flexibility**: Decorators can be stacked in any order and quantity at runtime, unlike compile-time generics.

6. **Chain of Responsibility**: Each decorator delegates to its wrapped component, creating a chain that processes requests from outside to inside.

7. **No Null Safety Issues**: Rust's type system ensures the wrapped beverage always exists - no null pointer concerns.

## Compilation and Execution

```bash
rustc main_decorator.rs -o main_decorator.exe && ./main_decorator.exe
```

This code is compatible with Rust stable (tested with rustc 1.70+). No external dependencies are required.
