# Flyweight Design Pattern in Rust

The Flyweight pattern is a structural design pattern that minimizes memory usage by sharing common state (intrinsic state) among multiple objects while keeping unique state (extrinsic state) external to the shared objects. This pattern is particularly useful when dealing with large numbers of similar objects.

In this example, we implement a forest rendering system where many trees share the same tree type data (name, color, texture) but each tree has a unique position.

## Source Code

```rust
  1  // Flyweight Design Pattern in Rust
  2  // Demonstrates memory sharing through intrinsic (shared) vs extrinsic (unique) state
  3
  4  use std::collections::HashMap;
  5  use std::rc::Rc;
  6
  7  // Flyweight: TreeType contains intrinsic state (shared data)
  8  // This data is the same for many trees and can be shared
  9  #[derive(Debug)]
 10  struct TreeType {
 11      name: String,
 12      color: String,
 13      texture: String,
 14  }
 15
 16  impl TreeType {
 17      fn new(name: &str, color: &str, texture: &str) -> Self {
 18          println!("  [CREATING] New TreeType: {} ({}, {})", name, color, texture);
 19          TreeType {
 20              name: name.to_string(),
 21              color: color.to_string(),
 22              texture: texture.to_string(),
 23          }
 24      }
 25
 26      fn render(&self, x: i32, y: i32) {
 27          println!(
 28              "    Rendering {} tree at ({}, {}) - Color: {}, Texture: {}",
 29              self.name, x, y, self.color, self.texture
 30          );
 31      }
 32  }
 33
 34  // Context: Tree contains extrinsic state (unique data per instance)
 35  // Each tree has unique position but shares TreeType
 36  struct Tree {
 37      x: i32,
 38      y: i32,
 39      tree_type: Rc<TreeType>, // Shared reference to flyweight
 40  }
 41
 42  impl Tree {
 43      fn new(x: i32, y: i32, tree_type: Rc<TreeType>) -> Self {
 44          Tree { x, y, tree_type }
 45      }
 46
 47      fn render(&self) {
 48          self.tree_type.render(self.x, self.y);
 49      }
 50  }
 51
 52  // Flyweight Factory: Manages and reuses TreeType instances
 53  struct TreeFactory {
 54      tree_types: HashMap<String, Rc<TreeType>>,
 55  }
 56
 57  impl TreeFactory {
 58      fn new() -> Self {
 59          println!("=== TreeFactory initialized ===\n");
 60          TreeFactory {
 61              tree_types: HashMap::new(),
 62          }
 63      }
 64
 65      fn get_tree_type(&mut self, name: &str, color: &str, texture: &str) -> Rc<TreeType> {
 66          let key = format!("{}_{}_{}",name, color, texture);
 67
 68          if let Some(tree_type) = self.tree_types.get(&key) {
 69              println!("  [REUSING] Existing TreeType: {} (memory saved!)", name);
 70              Rc::clone(tree_type)
 71          } else {
 72              let tree_type = Rc::new(TreeType::new(name, color, texture));
 73              self.tree_types.insert(key, Rc::clone(&tree_type));
 74              tree_type
 75          }
 76      }
 77
 78      fn get_flyweight_count(&self) -> usize {
 79          self.tree_types.len()
 80      }
 81  }
 82
 83  // Forest: Client that uses flyweights
 84  struct Forest {
 85      trees: Vec<Tree>,
 86      factory: TreeFactory,
 87  }
 88
 89  impl Forest {
 90      fn new() -> Self {
 91          Forest {
 92              trees: Vec::new(),
 93              factory: TreeFactory::new(),
 94          }
 95      }
 96
 97      fn plant_tree(&mut self, x: i32, y: i32, name: &str, color: &str, texture: &str) {
 98          println!("Planting tree at ({}, {}):", x, y);
 99          let tree_type = self.factory.get_tree_type(name, color, texture);
100          let tree = Tree::new(x, y, tree_type);
101          self.trees.push(tree);
102          println!();
103      }
104
105      fn render(&self) {
106          println!("=== Rendering Forest ===\n");
107          for tree in &self.trees {
108              tree.render();
109          }
110          println!();
111      }
112
113      fn get_stats(&self) {
114          let total_trees = self.trees.len();
115          let unique_types = self.factory.get_flyweight_count();
116
117          println!("=== Memory Statistics ===\n");
118          println!("Total trees planted: {}", total_trees);
119          println!("Unique tree types (flyweights): {}", unique_types);
120          println!("Memory optimization: {} trees share {} flyweight objects", total_trees, unique_types);
121
122          // Calculate theoretical memory savings
123          let tree_type_size = std::mem::size_of::<TreeType>();
124          let without_flyweight = total_trees * tree_type_size;
125          let with_flyweight = unique_types * tree_type_size;
126
127          println!("\nTheoretical memory for TreeType data:");
128          println!("  Without Flyweight: {} bytes ({} trees x {} bytes)",
129              without_flyweight, total_trees, tree_type_size);
130          println!("  With Flyweight: {} bytes ({} types x {} bytes)",
131              with_flyweight, unique_types, tree_type_size);
132          println!("  Memory saved: {} bytes ({:.1}% reduction)",
133              without_flyweight - with_flyweight,
134              (1.0 - (with_flyweight as f64 / without_flyweight as f64)) * 100.0);
135      }
136  }
137
138  fn main() {
139      println!("========================================");
140      println!("   Flyweight Pattern - Forest Example");
141      println!("========================================\n");
142
143      let mut forest = Forest::new();
144
145      // Plant multiple trees - many will share the same TreeType
146      println!("--- Planting Trees ---\n");
147
148      // First oak tree - creates new flyweight
149      forest.plant_tree(10, 20, "Oak", "Dark Green", "Rough Bark");
150
151      // Second oak tree - reuses existing flyweight
152      forest.plant_tree(50, 30, "Oak", "Dark Green", "Rough Bark");
153
154      // Pine tree - creates new flyweight
155      forest.plant_tree(100, 40, "Pine", "Green", "Scaly Bark");
156
157      // Third oak tree - reuses existing flyweight
158      forest.plant_tree(150, 50, "Oak", "Dark Green", "Rough Bark");
159
160      // Birch tree - creates new flyweight
161      forest.plant_tree(200, 60, "Birch", "Light Green", "White Bark");
162
163      // Second pine tree - reuses existing flyweight
164      forest.plant_tree(250, 70, "Pine", "Green", "Scaly Bark");
165
166      // Fourth oak tree - reuses existing flyweight
167      forest.plant_tree(300, 80, "Oak", "Dark Green", "Rough Bark");
168
169      // Second birch tree - reuses existing flyweight
170      forest.plant_tree(350, 90, "Birch", "Light Green", "White Bark");
171
172      // Render all trees
173      forest.render();
174
175      // Show memory statistics
176      forest.get_stats();
177
178      println!("\n========================================");
179      println!("   Flyweight Pattern Demo Complete");
180      println!("========================================");
181  }
```

## Program Output

```
========================================
   Flyweight Pattern - Forest Example
========================================

=== TreeFactory initialized ===

--- Planting Trees ---

Planting tree at (10, 20):
  [CREATING] New TreeType: Oak (Dark Green, Rough Bark)

Planting tree at (50, 30):
  [REUSING] Existing TreeType: Oak (memory saved!)

Planting tree at (100, 40):
  [CREATING] New TreeType: Pine (Green, Scaly Bark)

Planting tree at (150, 50):
  [REUSING] Existing TreeType: Oak (memory saved!)

Planting tree at (200, 60):
  [CREATING] New TreeType: Birch (Light Green, White Bark)

Planting tree at (250, 70):
  [REUSING] Existing TreeType: Pine (memory saved!)

Planting tree at (300, 80):
  [REUSING] Existing TreeType: Oak (memory saved!)

Planting tree at (350, 90):
  [REUSING] Existing TreeType: Birch (memory saved!)

=== Rendering Forest ===

    Rendering Oak tree at (10, 20) - Color: Dark Green, Texture: Rough Bark
    Rendering Oak tree at (50, 30) - Color: Dark Green, Texture: Rough Bark
    Rendering Pine tree at (100, 40) - Color: Green, Texture: Scaly Bark
    Rendering Oak tree at (150, 50) - Color: Dark Green, Texture: Rough Bark
    Rendering Birch tree at (200, 60) - Color: Light Green, Texture: White Bark
    Rendering Pine tree at (250, 70) - Color: Green, Texture: Scaly Bark
    Rendering Oak tree at (300, 80) - Color: Dark Green, Texture: Rough Bark
    Rendering Birch tree at (350, 90) - Color: Light Green, Texture: White Bark

=== Memory Statistics ===

Total trees planted: 8
Unique tree types (flyweights): 3
Memory optimization: 8 trees share 3 flyweight objects

Theoretical memory for TreeType data:
  Without Flyweight: 576 bytes (8 trees x 72 bytes)
  With Flyweight: 216 bytes (3 types x 72 bytes)
  Memory saved: 360 bytes (62.5% reduction)

========================================
   Flyweight Pattern Demo Complete
========================================
```

## Code Annotations

### Key Sections Explained

#### Flyweight Object (Lines 10-32)
The `TreeType` struct represents the **intrinsic state** - data that is shared among multiple objects. It contains:
- `name`: The type of tree (Oak, Pine, Birch)
- `color`: The foliage color
- `texture`: The bark texture

The `new()` method on line 17 prints a creation message to demonstrate when new flyweights are allocated. The `render()` method on line 26 takes extrinsic state (x, y coordinates) as parameters.

#### Context Object (Lines 36-50)
The `Tree` struct contains:
- **Extrinsic state**: `x` and `y` coordinates (unique per tree)
- **Shared reference**: `Rc<TreeType>` pointing to the flyweight

`Rc` (Reference Counted) on line 39 enables multiple trees to share ownership of the same `TreeType` without copying data.

#### Flyweight Factory (Lines 53-81)
The `TreeFactory` manages flyweight creation and reuse:
- Line 54: Uses `HashMap` to cache created flyweights
- Lines 65-76: The `get_tree_type()` method either returns an existing flyweight or creates a new one
- Line 66: Creates a composite key from all intrinsic properties
- Lines 68-70: Returns existing flyweight if found (prints reuse message)
- Lines 72-74: Creates new flyweight if not found

#### Client Code (Lines 84-136)
The `Forest` struct demonstrates client usage:
- Line 97: `plant_tree()` delegates to factory for flyweight management
- Lines 113-135: `get_stats()` calculates and displays memory savings

### Output to Source Code Correlation

| Output Line | Source Line(s) | Description |
|-------------|----------------|-------------|
| `=== TreeFactory initialized ===` | 59 | Factory constructor initialization message |
| `Planting tree at (10, 20):` | 98 | `plant_tree()` announces new tree location |
| `[CREATING] New TreeType: Oak` | 18 | First Oak - `TreeType::new()` creates flyweight |
| `[REUSING] Existing TreeType: Oak` | 69 | Second Oak - factory returns cached flyweight |
| `[CREATING] New TreeType: Pine` | 18 | First Pine - new flyweight type created |
| `[CREATING] New TreeType: Birch` | 18 | First Birch - new flyweight type created |
| `Rendering Oak tree at (10, 20)...` | 27-30 | `TreeType::render()` with extrinsic coords |
| `Total trees planted: 8` | 118 | Count from `self.trees.len()` |
| `Unique tree types: 3` | 119 | Count from factory's HashMap |
| `Without Flyweight: 576 bytes` | 128-129 | 8 trees x 72 bytes per TreeType |
| `With Flyweight: 216 bytes` | 130-131 | 3 types x 72 bytes per TreeType |
| `Memory saved: 360 bytes (62.5%)` | 132-134 | Calculated reduction |

### Memory Sharing Demonstration

The output clearly shows the Flyweight pattern in action:

1. **8 trees planted** but only **3 flyweight objects created**
2. Oak: Created once (line 149), reused 3 times (lines 152, 158, 167)
3. Pine: Created once (line 155), reused once (line 164)
4. Birch: Created once (line 161), reused once (line 170)

## Key Characteristics of Flyweight Pattern in Rust

### 1. Reference Counting with `Rc<T>`
Rust's `Rc` (Reference Counted) smart pointer is ideal for flyweight sharing:
- Multiple owners can hold references to the same data
- Data is automatically deallocated when the last reference is dropped
- Zero-cost abstraction at runtime for read-only sharing

### 2. HashMap for Flyweight Caching
The factory uses `HashMap<String, Rc<TreeType>>` to:
- Provide O(1) lookup for existing flyweights
- Use composite keys for complex intrinsic state combinations
- Automatically manage memory through Rust's ownership system

### 3. Separation of State
- **Intrinsic (Shared)**: `TreeType` - immutable data shared via `Rc`
- **Extrinsic (Unique)**: Position coordinates passed to `render()`

### 4. Compile-Time Safety
Rust ensures:
- No data races (single-threaded `Rc`, use `Arc` for multi-threaded)
- No memory leaks through automatic reference counting
- No null pointer exceptions

### 5. When to Use Flyweight in Rust
- Large numbers of similar objects (game sprites, UI elements, characters)
- Significant memory overhead from duplicated state
- Intrinsic state is immutable and can be safely shared
- Consider `Arc<T>` instead of `Rc<T>` for multi-threaded applications
