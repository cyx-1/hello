/**
 * Prototype Design Pattern in TypeScript
 *
 * The Prototype pattern creates new objects by cloning existing instances
 * rather than creating them from scratch. This is useful when object creation
 * is expensive or when you need variations of complex objects.
 */

// Prototype Interface
interface Prototype<T> {
    clone(): T;
    deepClone(): T;
}

// ============================================================
// Example 1: Game Character Cloning
// ============================================================

// Inventory item (nested object to demonstrate shallow vs deep cloning)
interface InventoryItem {
    name: string;
    quantity: number;
    damage?: number;
}

// Character stats
interface CharacterStats {
    health: number;
    mana: number;
    strength: number;
    agility: number;
}

// Game Character - Prototype implementation
class GameCharacter implements Prototype<GameCharacter> {
    public name: string;
    public level: number;
    public stats: CharacterStats;
    public inventory: InventoryItem[];
    public skills: string[];

    constructor(
        name: string,
        level: number,
        stats: CharacterStats,
        inventory: InventoryItem[],
        skills: string[]
    ) {
        this.name = name;
        this.level = level;
        this.stats = stats;
        this.inventory = inventory;
        this.skills = skills;
        console.log(`[Line 47] GameCharacter: Created character "${name}" at level ${level}`);
    }

    // Shallow clone - references to nested objects are shared
    clone(): GameCharacter {
        console.log(`[Line 52] GameCharacter.clone(): Creating shallow clone of "${this.name}"`);
        const cloned = new GameCharacter(
            this.name + " (Clone)",
            this.level,
            this.stats,          // Shared reference
            this.inventory,      // Shared reference
            this.skills          // Shared reference
        );
        console.log(`[Line 60] GameCharacter.clone(): Shallow clone created - nested objects are SHARED`);
        return cloned;
    }

    // Deep clone - all nested objects are recursively copied
    deepClone(): GameCharacter {
        console.log(`[Line 66] GameCharacter.deepClone(): Creating deep clone of "${this.name}"`);
        const cloned = new GameCharacter(
            this.name + " (Deep Clone)",
            this.level,
            { ...this.stats },                                    // New object copy
            this.inventory.map(item => ({ ...item })),            // New array with new objects
            [...this.skills]                                       // New array copy
        );
        console.log(`[Line 74] GameCharacter.deepClone(): Deep clone created - all objects are INDEPENDENT`);
        return cloned;
    }

    display(): void {
        console.log(`  Character: ${this.name}`);
        console.log(`  Level: ${this.level}`);
        console.log(`  Stats: HP=${this.stats.health}, MP=${this.stats.mana}, STR=${this.stats.strength}, AGI=${this.stats.agility}`);
        console.log(`  Inventory: ${this.inventory.map(i => `${i.name}(${i.quantity})`).join(", ")}`);
        console.log(`  Skills: ${this.skills.join(", ")}`);
    }
}

// ============================================================
// Example 2: Document Template Cloning
// ============================================================

// Document metadata
interface DocumentMetadata {
    author: string;
    createdAt: Date;
    tags: string[];
}

// Document section
interface Section {
    title: string;
    content: string;
    pageNumber: number;
}

// Document Template - Prototype implementation
class DocumentTemplate implements Prototype<DocumentTemplate> {
    public title: string;
    public metadata: DocumentMetadata;
    public sections: Section[];
    public formatting: { [key: string]: string };

    constructor(
        title: string,
        metadata: DocumentMetadata,
        sections: Section[],
        formatting: { [key: string]: string }
    ) {
        this.title = title;
        this.metadata = metadata;
        this.sections = sections;
        this.formatting = formatting;
        console.log(`[Line 114] DocumentTemplate: Created template "${title}"`);
    }

    // Shallow clone
    clone(): DocumentTemplate {
        console.log(`[Line 119] DocumentTemplate.clone(): Creating shallow clone of "${this.title}"`);
        const cloned = new DocumentTemplate(
            this.title + " (Copy)",
            this.metadata,       // Shared reference
            this.sections,       // Shared reference
            this.formatting      // Shared reference
        );
        console.log(`[Line 126] DocumentTemplate.clone(): Shallow clone created`);
        return cloned;
    }

    // Deep clone
    deepClone(): DocumentTemplate {
        console.log(`[Line 132] DocumentTemplate.deepClone(): Creating deep clone of "${this.title}"`);
        const cloned = new DocumentTemplate(
            this.title + " (Deep Copy)",
            {
                author: this.metadata.author,
                createdAt: new Date(this.metadata.createdAt.getTime()),
                tags: [...this.metadata.tags]
            },
            this.sections.map(section => ({
                title: section.title,
                content: section.content,
                pageNumber: section.pageNumber
            })),
            { ...this.formatting }
        );
        console.log(`[Line 147] DocumentTemplate.deepClone(): Deep clone created`);
        return cloned;
    }

    display(): void {
        console.log(`  Title: ${this.title}`);
        console.log(`  Author: ${this.metadata.author}`);
        console.log(`  Tags: ${this.metadata.tags.join(", ")}`);
        console.log(`  Sections: ${this.sections.map(s => s.title).join(", ")}`);
        console.log(`  Font: ${this.formatting.font}, Size: ${this.formatting.fontSize}`);
    }
}

// ============================================================
// Prototype Registry - manages prototype instances
// ============================================================

class PrototypeRegistry {
    private prototypes: Map<string, Prototype<any>> = new Map();

    register(name: string, prototype: Prototype<any>): void {
        this.prototypes.set(name, prototype);
        console.log(`[Line 169] PrototypeRegistry: Registered prototype "${name}"`);
    }

    getClone(name: string): any {
        const prototype = this.prototypes.get(name);
        if (!prototype) {
            throw new Error(`Prototype "${name}" not found`);
        }
        console.log(`[Line 177] PrototypeRegistry: Retrieving shallow clone of "${name}"`);
        return prototype.clone();
    }

    getDeepClone(name: string): any {
        const prototype = this.prototypes.get(name);
        if (!prototype) {
            throw new Error(`Prototype "${name}" not found`);
        }
        console.log(`[Line 186] PrototypeRegistry: Retrieving deep clone of "${name}"`);
        return prototype.deepClone();
    }
}

// ============================================================
// Demonstration
// ============================================================

function main(): void {
    console.log("=== Prototype Pattern Demonstration ===\n");

    // Demo 1: Game Character Cloning
    console.log("--- Demo 1: Game Character Cloning ---\n");

    // Create original character
    console.log("Creating original character:");
    const warrior = new GameCharacter(
        "Warrior",
        50,
        { health: 1000, mana: 200, strength: 85, agility: 60 },
        [
            { name: "Sword", quantity: 1, damage: 50 },
            { name: "Health Potion", quantity: 5 }
        ],
        ["Slash", "Block", "Charge"]
    );
    console.log("\nOriginal character state:");
    warrior.display();

    // Shallow clone demonstration
    console.log("\n--- Shallow Clone Test ---");
    const shallowClone = warrior.clone();

    console.log("\nModifying shallow clone's inventory...");
    shallowClone.inventory[0].damage = 100;  // This affects original!
    shallowClone.inventory[1].quantity = 10;  // This affects original!
    shallowClone.skills.push("Rage");  // This affects original!
    console.log(`[Line 220] Modified clone's sword damage to 100 and potion quantity to 10`);

    console.log("\nOriginal character AFTER shallow clone modification:");
    warrior.display();
    console.log("\nShallow clone state:");
    shallowClone.display();
    console.log("\n[Line 227] NOTICE: Original was affected because shallow clone shares references!");

    // Reset for deep clone test
    warrior.inventory[0].damage = 50;
    warrior.inventory[1].quantity = 5;
    warrior.skills.pop();

    // Deep clone demonstration
    console.log("\n--- Deep Clone Test ---");
    const deepClone = warrior.deepClone();

    console.log("\nModifying deep clone's inventory...");
    deepClone.inventory[0].damage = 200;  // Original NOT affected
    deepClone.inventory[1].quantity = 20;  // Original NOT affected
    deepClone.skills.push("Berserk");  // Original NOT affected
    console.log(`[Line 242] Modified clone's sword damage to 200 and potion quantity to 20`);

    console.log("\nOriginal character AFTER deep clone modification:");
    warrior.display();
    console.log("\nDeep clone state:");
    deepClone.display();
    console.log("\n[Line 249] NOTICE: Original was NOT affected - deep clone is fully independent!");

    // Demo 2: Document Template Cloning
    console.log("\n\n--- Demo 2: Document Template Cloning ---\n");

    // Create original template
    console.log("Creating original document template:");
    const reportTemplate = new DocumentTemplate(
        "Annual Report",
        {
            author: "John Smith",
            createdAt: new Date("2024-01-15"),
            tags: ["finance", "quarterly", "2024"]
        },
        [
            { title: "Executive Summary", content: "Overview...", pageNumber: 1 },
            { title: "Financial Analysis", content: "Details...", pageNumber: 5 },
            { title: "Conclusions", content: "Summary...", pageNumber: 20 }
        ],
        { font: "Arial", fontSize: "12pt", margin: "1in" }
    );
    console.log("\nOriginal template state:");
    reportTemplate.display();

    // Deep clone for customization
    console.log("\n--- Creating Customized Version via Deep Clone ---");
    const q2Report = reportTemplate.deepClone();

    console.log("\nCustomizing deep clone for Q2...");
    q2Report.title = "Q2 Report";
    q2Report.metadata.tags.push("Q2");
    q2Report.sections[0].content = "Q2 Overview...";
    console.log(`[Line 280] Customized clone title, tags, and content`);

    console.log("\nOriginal template AFTER deep clone customization:");
    reportTemplate.display();
    console.log("\nCustomized Q2 report:");
    q2Report.display();
    console.log("\n[Line 287] Original template preserved - safe for future cloning!");

    // Demo 3: Prototype Registry
    console.log("\n\n--- Demo 3: Prototype Registry ---\n");

    const registry = new PrototypeRegistry();

    // Register prototypes
    const mageTemplate = new GameCharacter(
        "Mage",
        30,
        { health: 500, mana: 800, strength: 30, agility: 50 },
        [{ name: "Staff", quantity: 1, damage: 30 }],
        ["Fireball", "Ice Bolt", "Teleport"]
    );

    const invoiceTemplate = new DocumentTemplate(
        "Invoice Template",
        {
            author: "Accounting Dept",
            createdAt: new Date("2024-03-01"),
            tags: ["billing", "template"]
        },
        [
            { title: "Header", content: "Company Info", pageNumber: 1 },
            { title: "Items", content: "Line items...", pageNumber: 1 },
            { title: "Total", content: "Sum", pageNumber: 1 }
        ],
        { font: "Helvetica", fontSize: "10pt", margin: "0.5in" }
    );

    registry.register("mage", mageTemplate);
    registry.register("invoice", invoiceTemplate);

    // Create instances from registry
    console.log("\nCreating characters from registry:");
    const player1Mage = registry.getDeepClone("mage") as GameCharacter;
    player1Mage.name = "Gandalf";
    player1Mage.level = 99;

    const player2Mage = registry.getDeepClone("mage") as GameCharacter;
    player2Mage.name = "Merlin";
    player2Mage.level = 75;

    console.log("\nPlayer 1 mage:");
    player1Mage.display();
    console.log("\nPlayer 2 mage:");
    player2Mage.display();

    console.log("\nCreating invoices from registry:");
    const invoice1 = registry.getDeepClone("invoice") as DocumentTemplate;
    invoice1.title = "Invoice #001";

    const invoice2 = registry.getDeepClone("invoice") as DocumentTemplate;
    invoice2.title = "Invoice #002";

    console.log("\nInvoice 1:");
    invoice1.display();
    console.log("\nInvoice 2:");
    invoice2.display();

    console.log("\n=== End of Demonstration ===");
}

main();
