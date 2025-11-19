// Builder Design Pattern in Rust
// Demonstrates: Builder Trait, Concrete Builder, Director, and Product

// The Product - what we're building
#[derive(Debug, Clone)]
struct House {
    foundation: String,
    walls: String,
    roof: String,
    windows: u32,
    doors: u32,
    garage: bool,
    swimming_pool: bool,
    garden: bool,
}

impl House {
    fn describe(&self) {
        println!("\n=== House Description ===");
        println!("Foundation: {}", self.foundation);
        println!("Walls: {}", self.walls);
        println!("Roof: {}", self.roof);
        println!("Windows: {}", self.windows);
        println!("Doors: {}", self.doors);
        println!("Garage: {}", if self.garage { "Yes" } else { "No" });
        println!("Swimming Pool: {}", if self.swimming_pool { "Yes" } else { "No" });
        println!("Garden: {}", if self.garden { "Yes" } else { "No" });
    }
}

// Builder Trait - defines the interface for building parts
trait HouseBuilder {
    fn new() -> Self where Self: Sized;
    fn build_foundation(&mut self) -> &mut Self;
    fn build_walls(&mut self) -> &mut Self;
    fn build_roof(&mut self) -> &mut Self;
    fn build_windows(&mut self, count: u32) -> &mut Self;
    fn build_doors(&mut self, count: u32) -> &mut Self;
    fn build_garage(&mut self) -> &mut Self;
    fn build_swimming_pool(&mut self) -> &mut Self;
    fn build_garden(&mut self) -> &mut Self;
    fn get_result(&self) -> House;
}

// Concrete Builder - builds a luxury house
struct LuxuryHouseBuilder {
    house: House,
}

impl HouseBuilder for LuxuryHouseBuilder {
    fn new() -> Self {
        println!("[LuxuryHouseBuilder] Initializing new luxury house builder");
        LuxuryHouseBuilder {
            house: House {
                foundation: String::new(),
                walls: String::new(),
                roof: String::new(),
                windows: 0,
                doors: 0,
                garage: false,
                swimming_pool: false,
                garden: false,
            },
        }
    }

    fn build_foundation(&mut self) -> &mut Self {
        println!("[LuxuryHouseBuilder] Building reinforced concrete foundation");
        self.house.foundation = "Reinforced Concrete".to_string();
        self
    }

    fn build_walls(&mut self) -> &mut Self {
        println!("[LuxuryHouseBuilder] Building brick walls with insulation");
        self.house.walls = "Brick with Premium Insulation".to_string();
        self
    }

    fn build_roof(&mut self) -> &mut Self {
        println!("[LuxuryHouseBuilder] Building slate tile roof");
        self.house.roof = "Slate Tiles".to_string();
        self
    }

    fn build_windows(&mut self, count: u32) -> &mut Self {
        println!("[LuxuryHouseBuilder] Installing {} double-glazed windows", count);
        self.house.windows = count;
        self
    }

    fn build_doors(&mut self, count: u32) -> &mut Self {
        println!("[LuxuryHouseBuilder] Installing {} oak doors", count);
        self.house.doors = count;
        self
    }

    fn build_garage(&mut self) -> &mut Self {
        println!("[LuxuryHouseBuilder] Building 3-car garage");
        self.house.garage = true;
        self
    }

    fn build_swimming_pool(&mut self) -> &mut Self {
        println!("[LuxuryHouseBuilder] Building heated swimming pool");
        self.house.swimming_pool = true;
        self
    }

    fn build_garden(&mut self) -> &mut Self {
        println!("[LuxuryHouseBuilder] Creating landscaped garden");
        self.house.garden = true;
        self
    }

    fn get_result(&self) -> House {
        println!("[LuxuryHouseBuilder] Luxury house construction complete!");
        self.house.clone()
    }
}

// Concrete Builder - builds a simple house
struct SimpleHouseBuilder {
    house: House,
}

impl HouseBuilder for SimpleHouseBuilder {
    fn new() -> Self {
        println!("[SimpleHouseBuilder] Initializing new simple house builder");
        SimpleHouseBuilder {
            house: House {
                foundation: String::new(),
                walls: String::new(),
                roof: String::new(),
                windows: 0,
                doors: 0,
                garage: false,
                swimming_pool: false,
                garden: false,
            },
        }
    }

    fn build_foundation(&mut self) -> &mut Self {
        println!("[SimpleHouseBuilder] Building concrete slab foundation");
        self.house.foundation = "Concrete Slab".to_string();
        self
    }

    fn build_walls(&mut self) -> &mut Self {
        println!("[SimpleHouseBuilder] Building wood frame walls");
        self.house.walls = "Wood Frame".to_string();
        self
    }

    fn build_roof(&mut self) -> &mut Self {
        println!("[SimpleHouseBuilder] Building asphalt shingle roof");
        self.house.roof = "Asphalt Shingles".to_string();
        self
    }

    fn build_windows(&mut self, count: u32) -> &mut Self {
        println!("[SimpleHouseBuilder] Installing {} standard windows", count);
        self.house.windows = count;
        self
    }

    fn build_doors(&mut self, count: u32) -> &mut Self {
        println!("[SimpleHouseBuilder] Installing {} standard doors", count);
        self.house.doors = count;
        self
    }

    fn build_garage(&mut self) -> &mut Self {
        println!("[SimpleHouseBuilder] Building 1-car garage");
        self.house.garage = true;
        self
    }

    fn build_swimming_pool(&mut self) -> &mut Self {
        println!("[SimpleHouseBuilder] Skipping swimming pool (not included)");
        self.house.swimming_pool = false;
        self
    }

    fn build_garden(&mut self) -> &mut Self {
        println!("[SimpleHouseBuilder] Creating basic lawn");
        self.house.garden = true;
        self
    }

    fn get_result(&self) -> House {
        println!("[SimpleHouseBuilder] Simple house construction complete!");
        self.house.clone()
    }
}

// Director - orchestrates the building process
struct ConstructionDirector;

impl ConstructionDirector {
    fn construct_full_house<T: HouseBuilder>(builder: &mut T) -> House {
        println!("\n>>> Director: Starting full house construction");
        builder
            .build_foundation()
            .build_walls()
            .build_roof()
            .build_windows(8)
            .build_doors(4)
            .build_garage()
            .build_swimming_pool()
            .build_garden();
        println!(">>> Director: Full house construction finished\n");
        builder.get_result()
    }

    fn construct_minimal_house<T: HouseBuilder>(builder: &mut T) -> House {
        println!("\n>>> Director: Starting minimal house construction");
        builder
            .build_foundation()
            .build_walls()
            .build_roof()
            .build_windows(4)
            .build_doors(2);
        println!(">>> Director: Minimal house construction finished\n");
        builder.get_result()
    }
}

fn main() {
    println!("==============================================");
    println!("   Builder Design Pattern - House Example");
    println!("==============================================");

    // Build a luxury house using the director
    println!("\n--- Building Luxury House with Director ---");
    let mut luxury_builder = LuxuryHouseBuilder::new();
    let luxury_house = ConstructionDirector::construct_full_house(&mut luxury_builder);
    luxury_house.describe();

    // Build a simple minimal house using the director
    println!("\n\n--- Building Simple Minimal House with Director ---");
    let mut simple_builder = SimpleHouseBuilder::new();
    let simple_house = ConstructionDirector::construct_minimal_house(&mut simple_builder);
    simple_house.describe();

    // Direct builder usage with method chaining (without director)
    println!("\n\n--- Custom House using Builder Directly ---");
    let mut custom_builder = LuxuryHouseBuilder::new();
    custom_builder
        .build_foundation()
        .build_walls()
        .build_roof()
        .build_windows(12)
        .build_doors(6)
        .build_swimming_pool();
    let custom_house = custom_builder.get_result();
    custom_house.describe();

    println!("\n==============================================");
    println!("   Builder Pattern Demonstration Complete");
    println!("==============================================");
}
