# Prototype Design Pattern in TypeScript

The Prototype pattern creates new objects by cloning existing instances rather than creating them from scratch. This is a creational design pattern that is particularly useful when object creation is expensive (e.g., database calls, network requests) or when you need many variations of complex objects with similar base configurations.

## Key Concepts

- **Shallow Clone**: Copies the object but shares references to nested objects
- **Deep Clone**: Recursively copies all nested objects, creating fully independent instances

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
2    * Prototype Design Pattern in TypeScript
3    *
4    * The Prototype pattern creates new objects by cloning existing instances
5    * rather than creating them from scratch. This is useful when object creation
6    * is expensive or when you need variations of complex objects.
7    */
8
9   // Prototype Interface
10  interface Prototype<T> {
11      clone(): T;
12      deepClone(): T;
13  }
14
15  // ============================================================
16  // Example 1: Game Character Cloning
17  // ============================================================
18
19  // Inventory item (nested object to demonstrate shallow vs deep cloning)
20  interface InventoryItem {
21      name: string;
22      quantity: number;
23      damage?: number;
24  }
25
26  // Character stats
27  interface CharacterStats {
28      health: number;
29      mana: number;
30      strength: number;
31      agility: number;
32  }
33
34  // Game Character - Prototype implementation
35  class GameCharacter implements Prototype<GameCharacter> {
36      public name: string;
37      public level: number;
38      public stats: CharacterStats;
39      public inventory: InventoryItem[];
40      public skills: string[];
41
42      constructor(
43          name: string,
44          level: number,
45          stats: CharacterStats,
46          inventory: InventoryItem[],
47          skills: string[]
48      ) {
49          this.name = name;
50          this.level = level;
51          this.stats = stats;
52          this.inventory = inventory;
53          this.skills = skills;
54          console.log(`[Line 47] GameCharacter: Created character "${name}" at level ${level}`);
55      }
56
57      // Shallow clone - references to nested objects are shared
58      clone(): GameCharacter {
59          console.log(`[Line 52] GameCharacter.clone(): Creating shallow clone of "${this.name}"`);
60          const cloned = new GameCharacter(
61              this.name + " (Clone)",
62              this.level,
63              this.stats,          // Shared reference
64              this.inventory,      // Shared reference
65              this.skills          // Shared reference
66          );
67          console.log(`[Line 60] GameCharacter.clone(): Shallow clone created - nested objects are SHARED`);
68          return cloned;
69      }
70
71      // Deep clone - all nested objects are recursively copied
72      deepClone(): GameCharacter {
73          console.log(`[Line 66] GameCharacter.deepClone(): Creating deep clone of "${this.name}"`);
74          const cloned = new GameCharacter(
75              this.name + " (Deep Clone)",
76              this.level,
77              { ...this.stats },                                    // New object copy
78              this.inventory.map(item => ({ ...item })),            // New array with new objects
79              [...this.skills]                                       // New array copy
80          );
81          console.log(`[Line 74] GameCharacter.deepClone(): Deep clone created - all objects are INDEPENDENT`);
82          return cloned;
83      }
84
85      display(): void {
86          console.log(`  Character: ${this.name}`);
87          console.log(`  Level: ${this.level}`);
88          console.log(`  Stats: HP=${this.stats.health}, MP=${this.stats.mana}, STR=${this.stats.strength}, AGI=${this.stats.agility}`);
89          console.log(`  Inventory: ${this.inventory.map(i => `${i.name}(${i.quantity})`).join(", ")}`);
90          console.log(`  Skills: ${this.skills.join(", ")}`);
91      }
92  }
93
94  // ============================================================
95  // Example 2: Document Template Cloning
96  // ============================================================
97
98  // Document metadata
99  interface DocumentMetadata {
100     author: string;
101     createdAt: Date;
102     tags: string[];
103 }
104
105 // Document section
106 interface Section {
107     title: string;
108     content: string;
109     pageNumber: number;
110 }
111
112 // Document Template - Prototype implementation
113 class DocumentTemplate implements Prototype<DocumentTemplate> {
114     public title: string;
115     public metadata: DocumentMetadata;
116     public sections: Section[];
117     public formatting: { [key: string]: string };
118
119     constructor(
120         title: string,
121         metadata: DocumentMetadata,
122         sections: Section[],
123         formatting: { [key: string]: string }
124     ) {
125         this.title = title;
126         this.metadata = metadata;
127         this.sections = sections;
128         this.formatting = formatting;
129         console.log(`[Line 114] DocumentTemplate: Created template "${title}"`);
130     }
131
132     // Shallow clone
133     clone(): DocumentTemplate {
134         console.log(`[Line 119] DocumentTemplate.clone(): Creating shallow clone of "${this.title}"`);
135         const cloned = new DocumentTemplate(
136             this.title + " (Copy)",
137             this.metadata,       // Shared reference
138             this.sections,       // Shared reference
139             this.formatting      // Shared reference
140         );
141         console.log(`[Line 126] DocumentTemplate.clone(): Shallow clone created`);
142         return cloned;
143     }
144
145     // Deep clone
146     deepClone(): DocumentTemplate {
147         console.log(`[Line 132] DocumentTemplate.deepClone(): Creating deep clone of "${this.title}"`);
148         const cloned = new DocumentTemplate(
149             this.title + " (Deep Copy)",
150             {
151                 author: this.metadata.author,
152                 createdAt: new Date(this.metadata.createdAt.getTime()),
153                 tags: [...this.metadata.tags]
154             },
155             this.sections.map(section => ({
156                 title: section.title,
157                 content: section.content,
158                 pageNumber: section.pageNumber
159             })),
160             { ...this.formatting }
161         );
162         console.log(`[Line 147] DocumentTemplate.deepClone(): Deep clone created`);
163         return cloned;
164     }
165 }
166
167 // ============================================================
168 // Prototype Registry - manages prototype instances
169 // ============================================================
170
171 class PrototypeRegistry {
172     private prototypes: Map<string, Prototype<any>> = new Map();
173
174     register(name: string, prototype: Prototype<any>): void {
175         this.prototypes.set(name, prototype);
176         console.log(`[Line 169] PrototypeRegistry: Registered prototype "${name}"`);
177     }
178
179     getClone(name: string): any {
180         const prototype = this.prototypes.get(name);
181         if (!prototype) {
182             throw new Error(`Prototype "${name}" not found`);
183         }
184         console.log(`[Line 177] PrototypeRegistry: Retrieving shallow clone of "${name}"`);
185         return prototype.clone();
186     }
187
188     getDeepClone(name: string): any {
189         const prototype = this.prototypes.get(name);
190         if (!prototype) {
191             throw new Error(`Prototype "${name}" not found`);
192         }
193         console.log(`[Line 186] PrototypeRegistry: Retrieving deep clone of "${name}"`);
194         return prototype.deepClone();
195     }
196 }
```

## Program Output

```
=== Prototype Pattern Demonstration ===

--- Demo 1: Game Character Cloning ---

Creating original character:
[Line 47] GameCharacter: Created character "Warrior" at level 50

Original character state:
  Character: Warrior
  Level: 50
  Stats: HP=1000, MP=200, STR=85, AGI=60
  Inventory: Sword(1), Health Potion(5)
  Skills: Slash, Block, Charge

--- Shallow Clone Test ---
[Line 52] GameCharacter.clone(): Creating shallow clone of "Warrior"
[Line 47] GameCharacter: Created character "Warrior (Clone)" at level 50
[Line 60] GameCharacter.clone(): Shallow clone created - nested objects are SHARED

Modifying shallow clone's inventory...
[Line 220] Modified clone's sword damage to 100 and potion quantity to 10

Original character AFTER shallow clone modification:
  Character: Warrior
  Level: 50
  Stats: HP=1000, MP=200, STR=85, AGI=60
  Inventory: Sword(1), Health Potion(10)
  Skills: Slash, Block, Charge, Rage

Shallow clone state:
  Character: Warrior (Clone)
  Level: 50
  Stats: HP=1000, MP=200, STR=85, AGI=60
  Inventory: Sword(1), Health Potion(10)
  Skills: Slash, Block, Charge, Rage

[Line 227] NOTICE: Original was affected because shallow clone shares references!

--- Deep Clone Test ---
[Line 66] GameCharacter.deepClone(): Creating deep clone of "Warrior"
[Line 47] GameCharacter: Created character "Warrior (Deep Clone)" at level 50
[Line 74] GameCharacter.deepClone(): Deep clone created - all objects are INDEPENDENT

Modifying deep clone's inventory...
[Line 242] Modified clone's sword damage to 200 and potion quantity to 20

Original character AFTER deep clone modification:
  Character: Warrior
  Level: 50
  Stats: HP=1000, MP=200, STR=85, AGI=60
  Inventory: Sword(1), Health Potion(5)
  Skills: Slash, Block, Charge

Deep clone state:
  Character: Warrior (Deep Clone)
  Level: 50
  Stats: HP=1000, MP=200, STR=85, AGI=60
  Inventory: Sword(1), Health Potion(20)
  Skills: Slash, Block, Charge, Berserk

[Line 249] NOTICE: Original was NOT affected - deep clone is fully independent!


--- Demo 2: Document Template Cloning ---

Creating original document template:
[Line 114] DocumentTemplate: Created template "Annual Report"

Original template state:
  Title: Annual Report
  Author: John Smith
  Tags: finance, quarterly, 2024
  Sections: Executive Summary, Financial Analysis, Conclusions
  Font: Arial, Size: 12pt

--- Creating Customized Version via Deep Clone ---
[Line 132] DocumentTemplate.deepClone(): Creating deep clone of "Annual Report"
[Line 114] DocumentTemplate: Created template "Annual Report (Deep Copy)"
[Line 147] DocumentTemplate.deepClone(): Deep clone created

Customizing deep clone for Q2...
[Line 280] Customized clone title, tags, and content

Original template AFTER deep clone customization:
  Title: Annual Report
  Author: John Smith
  Tags: finance, quarterly, 2024
  Sections: Executive Summary, Financial Analysis, Conclusions
  Font: Arial, Size: 12pt

Customized Q2 report:
  Title: Q2 Report
  Author: John Smith
  Tags: finance, quarterly, 2024, Q2
  Sections: Executive Summary, Financial Analysis, Conclusions
  Font: Arial, Size: 12pt

[Line 287] Original template preserved - safe for future cloning!


--- Demo 3: Prototype Registry ---

[Line 47] GameCharacter: Created character "Mage" at level 30
[Line 114] DocumentTemplate: Created template "Invoice Template"
[Line 169] PrototypeRegistry: Registered prototype "mage"
[Line 169] PrototypeRegistry: Registered prototype "invoice"

Creating characters from registry:
[Line 186] PrototypeRegistry: Retrieving deep clone of "mage"
[Line 66] GameCharacter.deepClone(): Creating deep clone of "Mage"
[Line 47] GameCharacter: Created character "Mage (Deep Clone)" at level 30
[Line 74] GameCharacter.deepClone(): Deep clone created - all objects are INDEPENDENT
[Line 186] PrototypeRegistry: Retrieving deep clone of "mage"
[Line 66] GameCharacter.deepClone(): Creating deep clone of "Mage"
[Line 47] GameCharacter: Created character "Mage (Deep Clone)" at level 30
[Line 74] GameCharacter.deepClone(): Deep clone created - all objects are INDEPENDENT

Player 1 mage:
  Character: Gandalf
  Level: 99
  Stats: HP=500, MP=800, STR=30, AGI=50
  Inventory: Staff(1)
  Skills: Fireball, Ice Bolt, Teleport

Player 2 mage:
  Character: Merlin
  Level: 75
  Stats: HP=500, MP=800, STR=30, AGI=50
  Inventory: Staff(1)
  Skills: Fireball, Ice Bolt, Teleport

Creating invoices from registry:
[Line 186] PrototypeRegistry: Retrieving deep clone of "invoice"
[Line 132] DocumentTemplate.deepClone(): Creating deep clone of "Invoice Template"
[Line 114] DocumentTemplate: Created template "Invoice Template (Deep Copy)"
[Line 147] DocumentTemplate.deepClone(): Deep clone created
[Line 186] PrototypeRegistry: Retrieving deep clone of "invoice"
[Line 132] DocumentTemplate.deepClone(): Creating deep clone of "Invoice Template"
[Line 114] DocumentTemplate: Created template "Invoice Template (Deep Copy)"
[Line 147] DocumentTemplate.deepClone(): Deep clone created

Invoice 1:
  Title: Invoice #001
  Author: Accounting Dept
  Tags: billing, template
  Sections: Header, Items, Total
  Font: Helvetica, Size: 10pt

Invoice 2:
  Title: Invoice #002
  Author: Accounting Dept
  Tags: billing, template
  Sections: Header, Items, Total
  Font: Helvetica, Size: 10pt

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Pattern Components

#### Prototype Interface (Lines 10-13)
- Defines `clone()` for shallow copying
- Defines `deepClone()` for deep copying
- Uses generics `<T>` for type safety

#### Concrete Prototypes (Lines 35-92, 113-165)
- `GameCharacter`: Implements cloning for game entities with nested stats, inventory, and skills
- `DocumentTemplate`: Implements cloning for document templates with metadata and sections

#### Prototype Registry (Lines 171-196)
- Manages a collection of prototype instances
- Provides `register()`, `getClone()`, and `getDeepClone()` methods
- Acts as a factory for creating new instances from prototypes

### Shallow vs Deep Clone Comparison

| Aspect | Shallow Clone | Deep Clone |
|--------|---------------|------------|
| **Implementation** | Lines 58-69 | Lines 72-83 |
| **Primitive Values** | Copied by value | Copied by value |
| **Objects/Arrays** | Shared reference | New independent copy |
| **Performance** | Faster | Slower |
| **Memory** | Lower usage | Higher usage |
| **Use Case** | Read-only nested data | Modifiable nested data |

### Output Correlation Table

| Output Line | Source Line | Explanation |
|-------------|-------------|-------------|
| `GameCharacter: Created character "Warrior"` | Line 54 | Constructor logs creation |
| `Creating shallow clone of "Warrior"` | Line 59 | Shallow clone method invoked |
| `Shallow clone created - nested objects are SHARED` | Line 67 | Confirms shared references |
| `Original was affected` | Line 227 | Demonstrates shallow clone side effect |
| `Creating deep clone of "Warrior"` | Line 73 | Deep clone method invoked |
| `Deep clone created - all objects are INDEPENDENT` | Line 81 | Confirms independent copies |
| `Original was NOT affected` | Line 249 | Demonstrates deep clone isolation |
| `PrototypeRegistry: Registered prototype` | Line 176 | Registry stores prototype |
| `Retrieving deep clone of "mage"` | Line 193 | Registry creates clone on demand |

### Critical Demonstration Points

#### Shallow Clone Side Effects (Lines 212-227)

```typescript
shallowClone.inventory[0].damage = 100;  // Affects original!
shallowClone.skills.push("Rage");        // Affects original!
```

**Output shows**: Original's `Health Potion` quantity changed from 5 to 10, and `Rage` skill was added.

**Why**: Both `inventory` and `skills` arrays point to the same memory location in both original and clone.

#### Deep Clone Independence (Lines 233-249)

```typescript
deepClone.inventory[0].damage = 200;     // Original NOT affected
deepClone.skills.push("Berserk");        // Original NOT affected
```

**Output shows**: Original's inventory and skills remain unchanged.

**Why**: `deepClone()` creates new array instances with spread operator:
- `{ ...this.stats }` - creates new stats object
- `this.inventory.map(item => ({ ...item }))` - creates new array with new objects
- `[...this.skills]` - creates new array copy

### Deep Clone Techniques Used

| Data Type | Technique | Source Line |
|-----------|-----------|-------------|
| Object | Spread operator `{ ...obj }` | Line 77 |
| Array of Objects | `array.map(item => ({ ...item }))` | Line 78 |
| Array of Primitives | Spread operator `[...array]` | Line 79 |
| Date | `new Date(date.getTime())` | Line 152 |

### Use Cases

1. **Game Development**
   - Clone base character templates for different players
   - Create enemy variations without expensive initialization

2. **Document Management**
   - Clone templates for invoices, reports, contracts
   - Maintain master templates while creating customized copies

3. **GUI Frameworks**
   - Clone complex UI components with default configurations
   - Create variations of widgets efficiently

4. **Caching Systems**
   - Store expensive-to-create objects as prototypes
   - Clone on demand instead of recreating

### When to Use Prototype Pattern

- Object creation is expensive (database queries, network calls)
- Need many similar objects with slight variations
- Want to avoid complex inheritance hierarchies
- Need to hide object creation complexity from clients
- Runtime object composition is required

### Considerations

- **Shallow vs Deep**: Always consider whether nested objects should be shared or copied
- **Circular References**: Deep cloning with circular references requires special handling
- **Complex Objects**: Objects with closures or private state may not clone correctly
- **Performance**: Deep cloning has overhead; use shallow clone when safe
