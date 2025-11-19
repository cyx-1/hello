// Flyweight Design Pattern in Rust
// Demonstrates memory sharing through intrinsic (shared) vs extrinsic (unique) state

use std::collections::HashMap;
use std::rc::Rc;

// Flyweight: TreeType contains intrinsic state (shared data)
// This data is the same for many trees and can be shared
#[derive(Debug)]
struct TreeType {
    name: String,
    color: String,
    texture: String,
}

impl TreeType {
    fn new(name: &str, color: &str, texture: &str) -> Self {
        println!("  [CREATING] New TreeType: {} ({}, {})", name, color, texture);
        TreeType {
            name: name.to_string(),
            color: color.to_string(),
            texture: texture.to_string(),
        }
    }

    fn render(&self, x: i32, y: i32) {
        println!(
            "    Rendering {} tree at ({}, {}) - Color: {}, Texture: {}",
            self.name, x, y, self.color, self.texture
        );
    }
}

// Context: Tree contains extrinsic state (unique data per instance)
// Each tree has unique position but shares TreeType
struct Tree {
    x: i32,
    y: i32,
    tree_type: Rc<TreeType>, // Shared reference to flyweight
}

impl Tree {
    fn new(x: i32, y: i32, tree_type: Rc<TreeType>) -> Self {
        Tree { x, y, tree_type }
    }

    fn render(&self) {
        self.tree_type.render(self.x, self.y);
    }
}

// Flyweight Factory: Manages and reuses TreeType instances
struct TreeFactory {
    tree_types: HashMap<String, Rc<TreeType>>,
}

impl TreeFactory {
    fn new() -> Self {
        println!("=== TreeFactory initialized ===\n");
        TreeFactory {
            tree_types: HashMap::new(),
        }
    }

    fn get_tree_type(&mut self, name: &str, color: &str, texture: &str) -> Rc<TreeType> {
        let key = format!("{}_{}_{}",name, color, texture);

        if let Some(tree_type) = self.tree_types.get(&key) {
            println!("  [REUSING] Existing TreeType: {} (memory saved!)", name);
            Rc::clone(tree_type)
        } else {
            let tree_type = Rc::new(TreeType::new(name, color, texture));
            self.tree_types.insert(key, Rc::clone(&tree_type));
            tree_type
        }
    }

    fn get_flyweight_count(&self) -> usize {
        self.tree_types.len()
    }
}

// Forest: Client that uses flyweights
struct Forest {
    trees: Vec<Tree>,
    factory: TreeFactory,
}

impl Forest {
    fn new() -> Self {
        Forest {
            trees: Vec::new(),
            factory: TreeFactory::new(),
        }
    }

    fn plant_tree(&mut self, x: i32, y: i32, name: &str, color: &str, texture: &str) {
        println!("Planting tree at ({}, {}):", x, y);
        let tree_type = self.factory.get_tree_type(name, color, texture);
        let tree = Tree::new(x, y, tree_type);
        self.trees.push(tree);
        println!();
    }

    fn render(&self) {
        println!("=== Rendering Forest ===\n");
        for tree in &self.trees {
            tree.render();
        }
        println!();
    }

    fn get_stats(&self) {
        let total_trees = self.trees.len();
        let unique_types = self.factory.get_flyweight_count();

        println!("=== Memory Statistics ===\n");
        println!("Total trees planted: {}", total_trees);
        println!("Unique tree types (flyweights): {}", unique_types);
        println!("Memory optimization: {} trees share {} flyweight objects", total_trees, unique_types);

        // Calculate theoretical memory savings
        let tree_type_size = std::mem::size_of::<TreeType>();
        let without_flyweight = total_trees * tree_type_size;
        let with_flyweight = unique_types * tree_type_size;

        println!("\nTheoretical memory for TreeType data:");
        println!("  Without Flyweight: {} bytes ({} trees x {} bytes)",
            without_flyweight, total_trees, tree_type_size);
        println!("  With Flyweight: {} bytes ({} types x {} bytes)",
            with_flyweight, unique_types, tree_type_size);
        println!("  Memory saved: {} bytes ({:.1}% reduction)",
            without_flyweight - with_flyweight,
            (1.0 - (with_flyweight as f64 / without_flyweight as f64)) * 100.0);
    }
}

fn main() {
    println!("========================================");
    println!("   Flyweight Pattern - Forest Example");
    println!("========================================\n");

    let mut forest = Forest::new();

    // Plant multiple trees - many will share the same TreeType
    println!("--- Planting Trees ---\n");

    // First oak tree - creates new flyweight
    forest.plant_tree(10, 20, "Oak", "Dark Green", "Rough Bark");

    // Second oak tree - reuses existing flyweight
    forest.plant_tree(50, 30, "Oak", "Dark Green", "Rough Bark");

    // Pine tree - creates new flyweight
    forest.plant_tree(100, 40, "Pine", "Green", "Scaly Bark");

    // Third oak tree - reuses existing flyweight
    forest.plant_tree(150, 50, "Oak", "Dark Green", "Rough Bark");

    // Birch tree - creates new flyweight
    forest.plant_tree(200, 60, "Birch", "Light Green", "White Bark");

    // Second pine tree - reuses existing flyweight
    forest.plant_tree(250, 70, "Pine", "Green", "Scaly Bark");

    // Fourth oak tree - reuses existing flyweight
    forest.plant_tree(300, 80, "Oak", "Dark Green", "Rough Bark");

    // Second birch tree - reuses existing flyweight
    forest.plant_tree(350, 90, "Birch", "Light Green", "White Bark");

    // Render all trees
    forest.render();

    // Show memory statistics
    forest.get_stats();

    println!("\n========================================");
    println!("   Flyweight Pattern Demo Complete");
    println!("========================================");
}
