// Decorator Design Pattern in Rust
// Demonstrates adding behaviors dynamically using trait objects

// Base trait that defines the component interface
trait Beverage {
    fn cost(&self) -> f64;
    fn description(&self) -> String;
}

// Concrete component: Simple Coffee
struct SimpleCoffee;

impl Beverage for SimpleCoffee {
    fn cost(&self) -> f64 {
        println!("  [SimpleCoffee] Base cost: $2.00");
        2.00
    }

    fn description(&self) -> String {
        String::from("Simple Coffee")
    }
}

// Concrete component: Espresso
struct Espresso;

impl Beverage for Espresso {
    fn cost(&self) -> f64 {
        println!("  [Espresso] Base cost: $3.00");
        3.00
    }

    fn description(&self) -> String {
        String::from("Espresso")
    }
}

// Decorator: Milk
struct MilkDecorator {
    beverage: Box<dyn Beverage>,
}

impl MilkDecorator {
    fn new(beverage: Box<dyn Beverage>) -> Self {
        MilkDecorator { beverage }
    }
}

impl Beverage for MilkDecorator {
    fn cost(&self) -> f64 {
        let base_cost = self.beverage.cost();
        println!("  [MilkDecorator] Adding milk: +$0.50");
        base_cost + 0.50
    }

    fn description(&self) -> String {
        format!("{}, Milk", self.beverage.description())
    }
}

// Decorator: Sugar
struct SugarDecorator {
    beverage: Box<dyn Beverage>,
}

impl SugarDecorator {
    fn new(beverage: Box<dyn Beverage>) -> Self {
        SugarDecorator { beverage }
    }
}

impl Beverage for SugarDecorator {
    fn cost(&self) -> f64 {
        let base_cost = self.beverage.cost();
        println!("  [SugarDecorator] Adding sugar: +$0.25");
        base_cost + 0.25
    }

    fn description(&self) -> String {
        format!("{}, Sugar", self.beverage.description())
    }
}

// Decorator: Whipped Cream
struct WhipDecorator {
    beverage: Box<dyn Beverage>,
}

impl WhipDecorator {
    fn new(beverage: Box<dyn Beverage>) -> Self {
        WhipDecorator { beverage }
    }
}

impl Beverage for WhipDecorator {
    fn cost(&self) -> f64 {
        let base_cost = self.beverage.cost();
        println!("  [WhipDecorator] Adding whipped cream: +$0.75");
        base_cost + 0.75
    }

    fn description(&self) -> String {
        format!("{}, Whip", self.beverage.description())
    }
}

// Decorator: Caramel
struct CaramelDecorator {
    beverage: Box<dyn Beverage>,
}

impl CaramelDecorator {
    fn new(beverage: Box<dyn Beverage>) -> Self {
        CaramelDecorator { beverage }
    }
}

impl Beverage for CaramelDecorator {
    fn cost(&self) -> f64 {
        let base_cost = self.beverage.cost();
        println!("  [CaramelDecorator] Adding caramel: +$0.60");
        base_cost + 0.60
    }

    fn description(&self) -> String {
        format!("{}, Caramel", self.beverage.description())
    }
}

fn main() {
    println!("=== Decorator Pattern: Coffee Shop Example ===\n");

    // Example 1: Simple coffee with no decorations
    println!("Order 1: Plain Simple Coffee");
    println!("---------------------------------");
    let coffee = SimpleCoffee;
    println!("Description: {}", coffee.description());
    print!("Calculating cost:\n");
    let total = coffee.cost();
    println!("Total: ${:.2}\n", total);

    // Example 2: Coffee with milk
    println!("Order 2: Coffee with Milk");
    println!("---------------------------------");
    let coffee_with_milk = MilkDecorator::new(Box::new(SimpleCoffee));
    println!("Description: {}", coffee_with_milk.description());
    print!("Calculating cost:\n");
    let total = coffee_with_milk.cost();
    println!("Total: ${:.2}\n", total);

    // Example 3: Coffee with milk and sugar (stacked decorators)
    println!("Order 3: Coffee with Milk and Sugar");
    println!("---------------------------------");
    let sweet_coffee = SugarDecorator::new(
        Box::new(MilkDecorator::new(Box::new(SimpleCoffee)))
    );
    println!("Description: {}", sweet_coffee.description());
    print!("Calculating cost:\n");
    let total = sweet_coffee.cost();
    println!("Total: ${:.2}\n", total);

    // Example 4: Fully loaded espresso
    println!("Order 4: Espresso with Milk, Sugar, Whip, and Caramel");
    println!("---------------------------------");
    let fancy_espresso = CaramelDecorator::new(
        Box::new(WhipDecorator::new(
            Box::new(SugarDecorator::new(
                Box::new(MilkDecorator::new(Box::new(Espresso)))
            ))
        ))
    );
    println!("Description: {}", fancy_espresso.description());
    print!("Calculating cost:\n");
    let total = fancy_espresso.cost();
    println!("Total: ${:.2}\n", total);

    // Example 5: Double milk coffee
    println!("Order 5: Coffee with Double Milk");
    println!("---------------------------------");
    let double_milk = MilkDecorator::new(
        Box::new(MilkDecorator::new(Box::new(SimpleCoffee)))
    );
    println!("Description: {}", double_milk.description());
    print!("Calculating cost:\n");
    let total = double_milk.cost();
    println!("Total: ${:.2}\n", total);

    println!("=== Pattern Demonstration Complete ===");
}
