/**
 * Flyweight Design Pattern in TypeScript
 *
 * The Flyweight pattern minimizes memory usage by sharing as much data
 * as possible with similar objects. It separates intrinsic state (shared)
 * from extrinsic state (unique to each context).
 */

// Flyweight Interface - defines the interface for flyweight objects
interface TreeType {
    name: string;
    color: string;
    texture: string;
    draw(x: number, y: number, age: number): void;
}

// Concrete Flyweight - contains intrinsic state shared among all trees
class ConcreteTreeType implements TreeType {
    // Intrinsic state - shared among all trees of this type
    public readonly name: string;
    public readonly color: string;
    public readonly texture: string;

    constructor(name: string, color: string, texture: string) {
        this.name = name;
        this.color = color;
        this.texture = texture;
        console.log(`[Line 27] ConcreteTreeType: Created flyweight for "${name}" (color: ${color}, texture: ${texture})`);
    }

    // Operation using both intrinsic and extrinsic state
    draw(x: number, y: number, age: number): void {
        console.log(`[Line 32] Drawing ${this.name} tree at (${x}, ${y}), age: ${age} years`);
        console.log(`    -> Intrinsic: color=${this.color}, texture=${this.texture}`);
        console.log(`    -> Extrinsic: position=(${x},${y}), age=${age}`);
    }
}

// Flyweight Factory - creates and manages flyweight objects
class TreeFactory {
    private static treeTypes: Map<string, TreeType> = new Map();
    private static cacheHits: number = 0;
    private static cacheMisses: number = 0;

    static getTreeType(name: string, color: string, texture: string): TreeType {
        const key = `${name}_${color}_${texture}`;

        if (this.treeTypes.has(key)) {
            this.cacheHits++;
            console.log(`[Line 49] TreeFactory: Cache HIT for "${name}" (key: ${key})`);
            return this.treeTypes.get(key)!;
        }

        this.cacheMisses++;
        console.log(`[Line 54] TreeFactory: Cache MISS - Creating new flyweight for "${name}"`);
        const treeType = new ConcreteTreeType(name, color, texture);
        this.treeTypes.set(key, treeType);
        return treeType;
    }

    static getStats(): { total: number; hits: number; misses: number } {
        return {
            total: this.treeTypes.size,
            hits: this.cacheHits,
            misses: this.cacheMisses
        };
    }

    static clear(): void {
        this.treeTypes.clear();
        this.cacheHits = 0;
        this.cacheMisses = 0;
    }
}

// Context - stores extrinsic state and references flyweight
class Tree {
    // Extrinsic state - unique to each tree instance
    private x: number;
    private y: number;
    private age: number;

    // Reference to flyweight (intrinsic state)
    private type: TreeType;

    constructor(x: number, y: number, age: number, type: TreeType) {
        this.x = x;
        this.y = y;
        this.age = age;
        this.type = type;
    }

    draw(): void {
        this.type.draw(this.x, this.y, this.age);
    }

    getMemoryFootprint(): number {
        // Extrinsic state only: 3 numbers (x, y, age) + 1 reference
        // Each number = 8 bytes, reference = 8 bytes
        return 32; // bytes
    }
}

// Client - manages the collection of trees
class Forest {
    private trees: Tree[] = [];

    plantTree(x: number, y: number, age: number, name: string, color: string, texture: string): void {
        // Get or create flyweight through factory
        const type = TreeFactory.getTreeType(name, color, texture);
        const tree = new Tree(x, y, age, type);
        this.trees.push(tree);
        console.log(`[Line 102] Forest: Planted ${name} at (${x}, ${y}), age ${age}`);
    }

    draw(): void {
        console.log(`\n[Line 106] Forest: Drawing ${this.trees.length} trees...`);
        this.trees.forEach((tree, index) => {
            console.log(`\n  Tree #${index + 1}:`);
            tree.draw();
        });
    }

    getTreeCount(): number {
        return this.trees.length;
    }

    calculateMemorySaved(): { withFlyweight: number; withoutFlyweight: number; saved: number } {
        const stats = TreeFactory.getStats();

        // With Flyweight: each tree stores only extrinsic state + reference
        // Flyweight objects store intrinsic state once per type
        const flyweightSize = 100; // Approximate bytes for intrinsic state per type
        const withFlyweight = (this.trees.length * 32) + (stats.total * flyweightSize);

        // Without Flyweight: each tree would store all state
        const fullTreeSize = 132; // All data per tree
        const withoutFlyweight = this.trees.length * fullTreeSize;

        return {
            withFlyweight,
            withoutFlyweight,
            saved: withoutFlyweight - withFlyweight
        };
    }
}

// ============================================================
// Second Example: Character Flyweight for Text Editor
// ============================================================

// Flyweight Interface for characters
interface CharacterFlyweight {
    char: string;
    fontFamily: string;
    fontSize: number;
    render(x: number, y: number, color: string, bold: boolean): void;
}

// Concrete Flyweight - character with shared formatting
class CharacterType implements CharacterFlyweight {
    // Intrinsic state - character appearance
    public readonly char: string;
    public readonly fontFamily: string;
    public readonly fontSize: number;

    constructor(char: string, fontFamily: string, fontSize: number) {
        this.char = char;
        this.fontFamily = fontFamily;
        this.fontSize = fontSize;
        console.log(`[Line 152] CharacterType: Created flyweight for '${char}' (${fontFamily}, ${fontSize}px)`);
    }

    render(x: number, y: number, color: string, bold: boolean): void {
        const style = bold ? "bold" : "normal";
        console.log(`[Line 157] Rendering '${this.char}' at (${x},${y}) - ${this.fontFamily} ${this.fontSize}px ${style} ${color}`);
    }
}

// Flyweight Factory for characters
class CharacterFactory {
    private static characters: Map<string, CharacterFlyweight> = new Map();

    static getCharacter(char: string, fontFamily: string, fontSize: number): CharacterFlyweight {
        const key = `${char}_${fontFamily}_${fontSize}`;

        if (!this.characters.has(key)) {
            console.log(`[Line 169] CharacterFactory: Creating new character flyweight`);
            this.characters.set(key, new CharacterType(char, fontFamily, fontSize));
        } else {
            console.log(`[Line 172] CharacterFactory: Reusing existing flyweight for '${char}'`);
        }

        return this.characters.get(key)!;
    }

    static getUniqueCount(): number {
        return this.characters.size;
    }

    static clear(): void {
        this.characters.clear();
    }
}

// Context - represents a character in the document
class Character {
    // Extrinsic state
    private x: number;
    private y: number;
    private color: string;
    private bold: boolean;

    // Reference to flyweight
    private type: CharacterFlyweight;

    constructor(x: number, y: number, color: string, bold: boolean, type: CharacterFlyweight) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.bold = bold;
        this.type = type;
    }

    render(): void {
        this.type.render(this.x, this.y, this.color, this.bold);
    }
}

// Document class using character flyweights
class TextDocument {
    private characters: Character[] = [];
    private cursorX: number = 0;
    private cursorY: number = 0;
    private charWidth: number = 10;
    private lineHeight: number = 16;

    addText(text: string, fontFamily: string, fontSize: number, color: string, bold: boolean): void {
        console.log(`\n[Line 215] TextDocument: Adding "${text}"`);

        for (const char of text) {
            if (char === '\n') {
                this.cursorX = 0;
                this.cursorY += this.lineHeight;
                continue;
            }

            const charType = CharacterFactory.getCharacter(char, fontFamily, fontSize);
            const character = new Character(this.cursorX, this.cursorY, color, bold, charType);
            this.characters.push(character);
            this.cursorX += this.charWidth;
        }
    }

    render(): void {
        console.log(`\n[Line 231] TextDocument: Rendering ${this.characters.length} characters...`);
        this.characters.forEach((char, index) => {
            if (index < 5 || index >= this.characters.length - 2) {
                char.render();
            } else if (index === 5) {
                console.log(`    ... (${this.characters.length - 7} more characters)`);
            }
        });
    }

    getStats(): { totalChars: number; uniqueFlyweights: number } {
        return {
            totalChars: this.characters.length,
            uniqueFlyweights: CharacterFactory.getUniqueCount()
        };
    }
}

// Demonstration
function main(): void {
    console.log("=== Flyweight Pattern Demonstration ===");

    // Demo 1: Forest with Tree Flyweights
    console.log("\n--- Forest Tree Flyweight Demo ---\n");

    const forest = new Forest();

    // Plant multiple trees - notice how flyweights are reused
    console.log("[Line 256] Planting Oak trees (should create 1 flyweight):");
    forest.plantTree(10, 20, 5, "Oak", "green", "rough_bark");
    forest.plantTree(30, 45, 8, "Oak", "green", "rough_bark");
    forest.plantTree(55, 15, 3, "Oak", "green", "rough_bark");

    console.log("\n[Line 261] Planting Pine trees (should create 1 flyweight):");
    forest.plantTree(100, 50, 12, "Pine", "dark_green", "pine_needles");
    forest.plantTree(120, 75, 7, "Pine", "dark_green", "pine_needles");

    console.log("\n[Line 265] Planting Birch trees (should create 1 flyweight):");
    forest.plantTree(200, 30, 4, "Birch", "light_green", "white_bark");
    forest.plantTree(220, 55, 6, "Birch", "light_green", "white_bark");
    forest.plantTree(240, 40, 2, "Birch", "light_green", "white_bark");
    forest.plantTree(260, 80, 9, "Birch", "light_green", "white_bark");

    // Draw the forest
    forest.draw();

    // Show memory savings
    const memory = forest.calculateMemorySaved();
    const stats = TreeFactory.getStats();

    console.log("\n--- Memory Analysis ---");
    console.log(`[Line 278] Total trees planted: ${forest.getTreeCount()}`);
    console.log(`[Line 279] Unique flyweight objects: ${stats.total}`);
    console.log(`[Line 280] Cache hits: ${stats.hits}, Cache misses: ${stats.misses}`);
    console.log(`[Line 281] Memory with Flyweight: ${memory.withFlyweight} bytes`);
    console.log(`[Line 282] Memory without Flyweight: ${memory.withoutFlyweight} bytes`);
    console.log(`[Line 283] Memory saved: ${memory.saved} bytes (${((memory.saved / memory.withoutFlyweight) * 100).toFixed(1)}%)`);

    // Demo 2: Text Editor Character Flyweights
    console.log("\n\n--- Text Editor Character Flyweight Demo ---");

    // Clear factory for fresh demo
    CharacterFactory.clear();

    const document = new TextDocument();

    // Add text - characters will be shared
    document.addText("Hello", "Arial", 12, "black", false);
    document.addText("World", "Arial", 12, "blue", true);
    document.addText("Hello", "Arial", 12, "red", false);

    // Render document
    document.render();

    // Show stats
    const docStats = document.getStats();
    console.log("\n--- Document Statistics ---");
    console.log(`[Line 302] Total characters in document: ${docStats.totalChars}`);
    console.log(`[Line 303] Unique character flyweights: ${docStats.uniqueFlyweights}`);
    console.log(`[Line 304] Flyweight reuse ratio: ${(docStats.totalChars / docStats.uniqueFlyweights).toFixed(2)}x`);

    console.log("\n=== End of Demonstration ===");
}

main();
