# Flyweight Design Pattern in TypeScript

The Flyweight pattern minimizes memory usage by sharing as much data as possible with similar objects. It separates **intrinsic state** (shared, immutable data) from **extrinsic state** (unique, context-dependent data). This pattern is particularly useful when dealing with large numbers of similar objects that would otherwise consume excessive memory.

## Requirements

- Node.js 18+
- TypeScript 5.3+

## How to Run

```bash
npm install
npm run start
```

## Source Code

```typescript
1   /**
2    * Flyweight Design Pattern in TypeScript
3    *
4    * The Flyweight pattern minimizes memory usage by sharing as much data
5    * as possible with similar objects. It separates intrinsic state (shared)
6    * from extrinsic state (unique to each context).
7    */
8
9   // Flyweight Interface - defines the interface for flyweight objects
10  interface TreeType {
11      name: string;
12      color: string;
13      texture: string;
14      draw(x: number, y: number, age: number): void;
15  }
16
17  // Concrete Flyweight - contains intrinsic state shared among all trees
18  class ConcreteTreeType implements TreeType {
19      // Intrinsic state - shared among all trees of this type
20      public readonly name: string;
21      public readonly color: string;
22      public readonly texture: string;
23
24      constructor(name: string, color: string, texture: string) {
25          this.name = name;
26          this.color = color;
27          this.texture = texture;
28          console.log(`[Line 27] ConcreteTreeType: Created flyweight for "${name}" (color: ${color}, texture: ${texture})`);
29      }
30
31      // Operation using both intrinsic and extrinsic state
32      draw(x: number, y: number, age: number): void {
33          console.log(`[Line 32] Drawing ${this.name} tree at (${x}, ${y}), age: ${age} years`);
34          console.log(`    -> Intrinsic: color=${this.color}, texture=${this.texture}`);
35          console.log(`    -> Extrinsic: position=(${x},${y}), age=${age}`);
36      }
37  }
38
39  // Flyweight Factory - creates and manages flyweight objects
40  class TreeFactory {
41      private static treeTypes: Map<string, TreeType> = new Map();
42      private static cacheHits: number = 0;
43      private static cacheMisses: number = 0;
44
45      static getTreeType(name: string, color: string, texture: string): TreeType {
46          const key = `${name}_${color}_${texture}`;
47
48          if (this.treeTypes.has(key)) {
49              this.cacheHits++;
50              console.log(`[Line 49] TreeFactory: Cache HIT for "${name}" (key: ${key})`);
51              return this.treeTypes.get(key)!;
52          }
53
54          this.cacheMisses++;
55          console.log(`[Line 54] TreeFactory: Cache MISS - Creating new flyweight for "${name}"`);
56          const treeType = new ConcreteTreeType(name, color, texture);
57          this.treeTypes.set(key, treeType);
58          return treeType;
59      }
60
61      static getStats(): { total: number; hits: number; misses: number } {
62          return {
63              total: this.treeTypes.size,
64              hits: this.cacheHits,
65              misses: this.cacheMisses
66          };
67      }
68
69      static clear(): void {
70          this.treeTypes.clear();
71          this.cacheHits = 0;
72          this.cacheMisses = 0;
73      }
74  }
75
76  // Context - stores extrinsic state and references flyweight
77  class Tree {
78      // Extrinsic state - unique to each tree instance
79      private x: number;
80      private y: number;
81      private age: number;
82
83      // Reference to flyweight (intrinsic state)
84      private type: TreeType;
85
86      constructor(x: number, y: number, age: number, type: TreeType) {
87          this.x = x;
88          this.y = y;
89          this.age = age;
90          this.type = type;
91      }
92
93      draw(): void {
94          this.type.draw(this.x, this.y, this.age);
95      }
96
97      getMemoryFootprint(): number {
98          // Extrinsic state only: 3 numbers (x, y, age) + 1 reference
99          // Each number = 8 bytes, reference = 8 bytes
100         return 32; // bytes
101     }
102 }
103
104 // Client - manages the collection of trees
105 class Forest {
106     private trees: Tree[] = [];
107
108     plantTree(x: number, y: number, age: number, name: string, color: string, texture: string): void {
109         // Get or create flyweight through factory
110         const type = TreeFactory.getTreeType(name, color, texture);
111         const tree = new Tree(x, y, age, type);
112         this.trees.push(tree);
113         console.log(`[Line 102] Forest: Planted ${name} at (${x}, ${y}), age ${age}`);
114     }
115
116     draw(): void {
117         console.log(`\n[Line 106] Forest: Drawing ${this.trees.length} trees...`);
118         this.trees.forEach((tree, index) => {
119             console.log(`\n  Tree #${index + 1}:`);
120             tree.draw();
121         });
122     }
123
124     getTreeCount(): number {
125         return this.trees.length;
126     }
127
128     calculateMemorySaved(): { withFlyweight: number; withoutFlyweight: number; saved: number } {
129         const stats = TreeFactory.getStats();
130
131         // With Flyweight: each tree stores only extrinsic state + reference
132         // Flyweight objects store intrinsic state once per type
133         const flyweightSize = 100; // Approximate bytes for intrinsic state per type
134         const withFlyweight = (this.trees.length * 32) + (stats.total * flyweightSize);
135
136         // Without Flyweight: each tree would store all state
137         const fullTreeSize = 132; // All data per tree
138         const withoutFlyweight = this.trees.length * fullTreeSize;
139
140         return {
141             withFlyweight,
142             withoutFlyweight,
143             saved: withoutFlyweight - withFlyweight
144         };
145     }
146 }
147
148 // ============================================================
149 // Second Example: Character Flyweight for Text Editor
150 // ============================================================
151
152 // Flyweight Interface for characters
153 interface CharacterFlyweight {
154     char: string;
155     fontFamily: string;
156     fontSize: number;
157     render(x: number, y: number, color: string, bold: boolean): void;
158 }
159
160 // Concrete Flyweight - character with shared formatting
161 class CharacterType implements CharacterFlyweight {
162     // Intrinsic state - character appearance
163     public readonly char: string;
164     public readonly fontFamily: string;
165     public readonly fontSize: number;
166
167     constructor(char: string, fontFamily: string, fontSize: number) {
168         this.char = char;
169         this.fontFamily = fontFamily;
170         this.fontSize = fontSize;
171         console.log(`[Line 152] CharacterType: Created flyweight for '${char}' (${fontFamily}, ${fontSize}px)`);
172     }
173
174     render(x: number, y: number, color: string, bold: boolean): void {
175         const style = bold ? "bold" : "normal";
176         console.log(`[Line 157] Rendering '${this.char}' at (${x},${y}) - ${this.fontFamily} ${this.fontSize}px ${style} ${color}`);
177     }
178 }
179
180 // Flyweight Factory for characters
181 class CharacterFactory {
182     private static characters: Map<string, CharacterFlyweight> = new Map();
183
184     static getCharacter(char: string, fontFamily: string, fontSize: number): CharacterFlyweight {
185         const key = `${char}_${fontFamily}_${fontSize}`;
186
187         if (!this.characters.has(key)) {
188             console.log(`[Line 169] CharacterFactory: Creating new character flyweight`);
189             this.characters.set(key, new CharacterType(char, fontFamily, fontSize));
190         } else {
191             console.log(`[Line 172] CharacterFactory: Reusing existing flyweight for '${char}'`);
192         }
193
194         return this.characters.get(key)!;
195     }
196
197     static getUniqueCount(): number {
198         return this.characters.size;
199     }
200
201     static clear(): void {
202         this.characters.clear();
203     }
204 }
205
206 // Context - represents a character in the document
207 class Character {
208     // Extrinsic state
209     private x: number;
210     private y: number;
211     private color: string;
212     private bold: boolean;
213
214     // Reference to flyweight
215     private type: CharacterFlyweight;
216
217     constructor(x: number, y: number, color: string, bold: boolean, type: CharacterFlyweight) {
218         this.x = x;
219         this.y = y;
220         this.color = color;
221         this.bold = bold;
222         this.type = type;
223     }
224
225     render(): void {
226         this.type.render(this.x, this.y, this.color, this.bold);
227     }
228 }
```

## Program Output

```
=== Flyweight Pattern Demonstration ===

--- Forest Tree Flyweight Demo ---

[Line 256] Planting Oak trees (should create 1 flyweight):
[Line 54] TreeFactory: Cache MISS - Creating new flyweight for "Oak"
[Line 27] ConcreteTreeType: Created flyweight for "Oak" (color: green, texture: rough_bark)
[Line 102] Forest: Planted Oak at (10, 20), age 5
[Line 49] TreeFactory: Cache HIT for "Oak" (key: Oak_green_rough_bark)
[Line 102] Forest: Planted Oak at (30, 45), age 8
[Line 49] TreeFactory: Cache HIT for "Oak" (key: Oak_green_rough_bark)
[Line 102] Forest: Planted Oak at (55, 15), age 3

[Line 261] Planting Pine trees (should create 1 flyweight):
[Line 54] TreeFactory: Cache MISS - Creating new flyweight for "Pine"
[Line 27] ConcreteTreeType: Created flyweight for "Pine" (color: dark_green, texture: pine_needles)
[Line 102] Forest: Planted Pine at (100, 50), age 12
[Line 49] TreeFactory: Cache HIT for "Pine" (key: Pine_dark_green_pine_needles)
[Line 102] Forest: Planted Pine at (120, 75), age 7

[Line 265] Planting Birch trees (should create 1 flyweight):
[Line 54] TreeFactory: Cache MISS - Creating new flyweight for "Birch"
[Line 27] ConcreteTreeType: Created flyweight for "Birch" (color: light_green, texture: white_bark)
[Line 102] Forest: Planted Birch at (200, 30), age 4
[Line 49] TreeFactory: Cache HIT for "Birch" (key: Birch_light_green_white_bark)
[Line 102] Forest: Planted Birch at (220, 55), age 6
[Line 49] TreeFactory: Cache HIT for "Birch" (key: Birch_light_green_white_bark)
[Line 102] Forest: Planted Birch at (240, 40), age 2
[Line 49] TreeFactory: Cache HIT for "Birch" (key: Birch_light_green_white_bark)
[Line 102] Forest: Planted Birch at (260, 80), age 9

[Line 106] Forest: Drawing 9 trees...

  Tree #1:
[Line 32] Drawing Oak tree at (10, 20), age: 5 years
    -> Intrinsic: color=green, texture=rough_bark
    -> Extrinsic: position=(10,20), age=5

  Tree #2:
[Line 32] Drawing Oak tree at (30, 45), age: 8 years
    -> Intrinsic: color=green, texture=rough_bark
    -> Extrinsic: position=(30,45), age=8

  Tree #3:
[Line 32] Drawing Oak tree at (55, 15), age: 3 years
    -> Intrinsic: color=green, texture=rough_bark
    -> Extrinsic: position=(55,15), age=3

  Tree #4:
[Line 32] Drawing Pine tree at (100, 50), age: 12 years
    -> Intrinsic: color=dark_green, texture=pine_needles
    -> Extrinsic: position=(100,50), age=12

  Tree #5:
[Line 32] Drawing Pine tree at (120, 75), age: 7 years
    -> Intrinsic: color=dark_green, texture=pine_needles
    -> Extrinsic: position=(120,75), age=7

  Tree #6:
[Line 32] Drawing Birch tree at (200, 30), age: 4 years
    -> Intrinsic: color=light_green, texture=white_bark
    -> Extrinsic: position=(200,30), age=4

  Tree #7:
[Line 32] Drawing Birch tree at (220, 55), age: 6 years
    -> Intrinsic: color=light_green, texture=white_bark
    -> Extrinsic: position=(220,55), age=6

  Tree #8:
[Line 32] Drawing Birch tree at (240, 40), age: 2 years
    -> Intrinsic: color=light_green, texture=white_bark
    -> Extrinsic: position=(240,40), age=2

  Tree #9:
[Line 32] Drawing Birch tree at (260, 80), age: 9 years
    -> Intrinsic: color=light_green, texture=white_bark
    -> Extrinsic: position=(260,80), age=9

--- Memory Analysis ---
[Line 278] Total trees planted: 9
[Line 279] Unique flyweight objects: 3
[Line 280] Cache hits: 6, Cache misses: 3
[Line 281] Memory with Flyweight: 588 bytes
[Line 282] Memory without Flyweight: 1188 bytes
[Line 283] Memory saved: 600 bytes (50.5%)


--- Text Editor Character Flyweight Demo ---

[Line 215] TextDocument: Adding "Hello"
[Line 169] CharacterFactory: Creating new character flyweight
[Line 152] CharacterType: Created flyweight for 'H' (Arial, 12px)
[Line 169] CharacterFactory: Creating new character flyweight
[Line 152] CharacterType: Created flyweight for 'e' (Arial, 12px)
[Line 169] CharacterFactory: Creating new character flyweight
[Line 152] CharacterType: Created flyweight for 'l' (Arial, 12px)
[Line 172] CharacterFactory: Reusing existing flyweight for 'l'
[Line 169] CharacterFactory: Creating new character flyweight
[Line 152] CharacterType: Created flyweight for 'o' (Arial, 12px)

[Line 215] TextDocument: Adding "World"
[Line 169] CharacterFactory: Creating new character flyweight
[Line 152] CharacterType: Created flyweight for 'W' (Arial, 12px)
[Line 172] CharacterFactory: Reusing existing flyweight for 'o'
[Line 169] CharacterFactory: Creating new character flyweight
[Line 152] CharacterType: Created flyweight for 'r' (Arial, 12px)
[Line 172] CharacterFactory: Reusing existing flyweight for 'l'
[Line 169] CharacterFactory: Creating new character flyweight
[Line 152] CharacterType: Created flyweight for 'd' (Arial, 12px)

[Line 215] TextDocument: Adding "Hello"
[Line 172] CharacterFactory: Reusing existing flyweight for 'H'
[Line 172] CharacterFactory: Reusing existing flyweight for 'e'
[Line 172] CharacterFactory: Reusing existing flyweight for 'l'
[Line 172] CharacterFactory: Reusing existing flyweight for 'l'
[Line 172] CharacterFactory: Reusing existing flyweight for 'o'

[Line 231] TextDocument: Rendering 15 characters...
[Line 157] Rendering 'H' at (0,0) - Arial 12px normal black
[Line 157] Rendering 'e' at (10,0) - Arial 12px normal black
[Line 157] Rendering 'l' at (20,0) - Arial 12px normal black
[Line 157] Rendering 'l' at (30,0) - Arial 12px normal black
[Line 157] Rendering 'o' at (40,0) - Arial 12px normal black
    ... (8 more characters)
[Line 157] Rendering 'l' at (130,0) - Arial 12px normal red
[Line 157] Rendering 'o' at (140,0) - Arial 12px normal red

--- Document Statistics ---
[Line 302] Total characters in document: 15
[Line 303] Unique character flyweights: 7
[Line 304] Flyweight reuse ratio: 2.14x

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Pattern Components

#### Flyweight Interface (Lines 10-15, 153-158)
- Defines the interface that both concrete flyweights implement
- `TreeType` declares the shared properties (name, color, texture) and operation (draw)
- `CharacterFlyweight` declares character properties and render operation

#### Concrete Flyweight (Lines 18-37, 161-178)
- Contains **intrinsic state** - data shared among all instances
- `ConcreteTreeType` stores tree appearance data (name, color, texture)
- `CharacterType` stores character and font information
- Operations receive **extrinsic state** as parameters

#### Flyweight Factory (Lines 40-74, 181-204)
- Creates and manages flyweight objects
- Uses a cache (Map) to store and reuse flyweight instances
- Returns existing flyweight if available (cache hit)
- Creates new flyweight only when necessary (cache miss)

#### Context (Lines 77-102, 207-228)
- Stores **extrinsic state** - data unique to each instance
- `Tree` stores position (x, y) and age
- `Character` stores position, color, and bold state
- Contains a reference to the shared flyweight

#### Client (Lines 105-146)
- `Forest` manages multiple trees and coordinates with factory
- Demonstrates memory savings calculation

### State Separation

| State Type | Description | Example (Forest) | Example (Text Editor) |
|------------|-------------|------------------|----------------------|
| **Intrinsic** | Shared, immutable | Tree type, color, texture | Character, font family, font size |
| **Extrinsic** | Unique, context-dependent | Position (x, y), age | Position (x, y), color, bold |

### Output Correlation Table

| Output | Source Line | Explanation |
|--------|-------------|-------------|
| `Cache MISS - Creating new flyweight for "Oak"` | Line 54-55 | First Oak tree triggers flyweight creation |
| `Created flyweight for "Oak" (color: green...)` | Line 27-28 | ConcreteTreeType constructor executes |
| `Cache HIT for "Oak" (key: Oak_green_rough_bark)` | Line 49-50 | Subsequent Oak trees reuse existing flyweight |
| `Drawing Oak tree at (10, 20), age: 5 years` | Line 32-33 | Draw operation with extrinsic state |
| `-> Intrinsic: color=green, texture=rough_bark` | Line 34 | Shared state from flyweight |
| `-> Extrinsic: position=(10,20), age=5` | Line 35 | Unique state passed as parameters |
| `Creating new character flyweight` | Line 169 | New character type needed |
| `Reusing existing flyweight for 'l'` | Line 172 | Same character reused |
| `Memory saved: 600 bytes (50.5%)` | Line 283 | Demonstrates memory efficiency |

### Memory Savings Analysis

The output shows concrete memory benefits:

| Metric | Value | Explanation |
|--------|-------|-------------|
| Total trees | 9 | All individual tree instances |
| Unique flyweights | 3 | Only Oak, Pine, Birch types created |
| Cache hits | 6 | Times flyweight was reused |
| Cache misses | 3 | Times new flyweight was created |
| Memory with Flyweight | 588 bytes | Extrinsic state + 3 flyweights |
| Memory without Flyweight | 1188 bytes | Full state for all 9 trees |
| Memory saved | 600 bytes (50.5%) | Significant reduction |

### Character Flyweight Statistics

| Metric | Value | Explanation |
|--------|-------|-------------|
| Total characters | 15 | "Hello" + "World" + "Hello" |
| Unique flyweights | 7 | H, e, l, o, W, r, d |
| Reuse ratio | 2.14x | Each flyweight used ~2 times |

### Key Implementation Details

#### Factory Caching Strategy (Lines 45-58)
```typescript
const key = `${name}_${color}_${texture}`;
if (this.treeTypes.has(key)) {
    return this.treeTypes.get(key)!;
}
// Create new only if not found
```

#### State Separation in Draw Operation (Lines 32-35)
```typescript
draw(x: number, y: number, age: number): void {
    // Uses intrinsic state (this.name, this.color, this.texture)
    // Combined with extrinsic state (x, y, age parameters)
}
```

### When to Use Flyweight Pattern

1. **Large Number of Similar Objects**: When your application creates thousands of similar objects
2. **Memory Constraints**: When memory usage is a critical concern
3. **Shared Immutable State**: When objects can share a significant portion of their state
4. **Performance**: When object creation overhead is significant

### Real-World Use Cases

- **Game Development**: Rendering thousands of trees, particles, or sprites
- **Text Editors**: Managing characters in a document with shared fonts
- **Data Visualization**: Plotting millions of data points with shared styles
- **Caching Systems**: Managing cached objects with common metadata
- **GUI Frameworks**: Sharing graphical resources among UI components

### Trade-offs

| Advantage | Disadvantage |
|-----------|--------------|
| Significant memory savings | Increased code complexity |
| Reduced object creation overhead | Runtime overhead for state separation |
| Better CPU cache utilization | Factory management overhead |
| Scalable for large datasets | Thread safety considerations |
