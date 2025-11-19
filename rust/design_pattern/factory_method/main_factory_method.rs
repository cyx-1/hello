// Factory Method Design Pattern in Rust
// Demonstrates creating different types of transport for a logistics application

// Product trait - defines the interface for objects created by the factory method
trait Transport {
    fn deliver(&self) -> String;
    fn get_capacity(&self) -> u32;
}

// Concrete Product: Truck
struct Truck {
    cargo_weight: u32,
}

impl Transport for Truck {
    fn deliver(&self) -> String {
        format!("Delivering by land in a truck with {} tons of cargo", self.cargo_weight)
    }

    fn get_capacity(&self) -> u32 {
        self.cargo_weight
    }
}

// Concrete Product: Ship
struct Ship {
    container_count: u32,
}

impl Transport for Ship {
    fn deliver(&self) -> String {
        format!("Delivering by sea in a ship with {} containers", self.container_count)
    }

    fn get_capacity(&self) -> u32 {
        self.container_count * 20 // Each container holds ~20 tons
    }
}

// Concrete Product: Airplane
struct Airplane {
    cargo_volume: u32,
}

impl Transport for Airplane {
    fn deliver(&self) -> String {
        format!("Delivering by air in an airplane with {} cubic meters of cargo", self.cargo_volume)
    }

    fn get_capacity(&self) -> u32 {
        self.cargo_volume
    }
}

// Creator trait - declares the factory method
trait Logistics {
    // Factory method - subclasses override this to create specific products
    fn create_transport(&self) -> Box<dyn Transport>;

    // Business logic that uses the factory method
    fn plan_delivery(&self) {
        println!("Planning delivery logistics...");
        let transport = self.create_transport();
        println!("  -> Transport created with capacity: {} units", transport.get_capacity());
        println!("  -> {}", transport.deliver());
    }
}

// Concrete Creator: RoadLogistics
struct RoadLogistics {
    cargo_weight: u32,
}

impl Logistics for RoadLogistics {
    fn create_transport(&self) -> Box<dyn Transport> {
        println!("  [Factory] Creating Truck transport");
        Box::new(Truck { cargo_weight: self.cargo_weight })
    }
}

// Concrete Creator: SeaLogistics
struct SeaLogistics {
    container_count: u32,
}

impl Logistics for SeaLogistics {
    fn create_transport(&self) -> Box<dyn Transport> {
        println!("  [Factory] Creating Ship transport");
        Box::new(Ship { container_count: self.container_count })
    }
}

// Concrete Creator: AirLogistics
struct AirLogistics {
    cargo_volume: u32,
}

impl Logistics for AirLogistics {
    fn create_transport(&self) -> Box<dyn Transport> {
        println!("  [Factory] Creating Airplane transport");
        Box::new(Airplane { cargo_volume: self.cargo_volume })
    }
}

// Client code that works with creators through the base trait
fn execute_logistics(logistics: &dyn Logistics) {
    logistics.plan_delivery();
}

fn main() {
    println!("=== Factory Method Pattern Demo ===\n");

    // Create different logistics operations
    println!("1. Road Logistics (Truck):");
    let road = RoadLogistics { cargo_weight: 10 };
    execute_logistics(&road);

    println!("\n2. Sea Logistics (Ship):");
    let sea = SeaLogistics { container_count: 50 };
    execute_logistics(&sea);

    println!("\n3. Air Logistics (Airplane):");
    let air = AirLogistics { cargo_volume: 100 };
    execute_logistics(&air);

    println!("\n=== Demonstrating Polymorphism ===\n");

    // Store different logistics in a vector
    let logistics_list: Vec<Box<dyn Logistics>> = vec![
        Box::new(RoadLogistics { cargo_weight: 25 }),
        Box::new(SeaLogistics { container_count: 100 }),
        Box::new(AirLogistics { cargo_volume: 200 }),
    ];

    for (i, logistics) in logistics_list.iter().enumerate() {
        println!("Operation {}:", i + 1);
        logistics.plan_delivery();
        println!();
    }

    println!("=== Pattern Complete ===");
}
