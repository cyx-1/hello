# Decorator Design Pattern - TypeScript Implementation

## Pattern Description

The **Decorator Pattern** is a structural design pattern that allows behavior to be added to individual objects, dynamically, without affecting the behavior of other objects from the same class. It provides a flexible alternative to subclassing for extending functionality.

### Key Concepts

- **Component**: Defines the interface for objects that can have responsibilities added to them
- **Concrete Component**: The original object to which additional responsibilities can be attached
- **Decorator**: Maintains a reference to a Component object and defines an interface that conforms to Component's interface
- **Concrete Decorator**: Adds responsibilities to the component

### Use Cases

- When you need to add responsibilities to objects dynamically and transparently
- When extension by subclassing is impractical due to a large number of independent extensions
- When you want to add functionality that can be withdrawn later

## Requirements

- **Node.js**: 18.0 or higher
- **TypeScript**: 5.3.0 or higher
- **npm**: 8.0 or higher

## How to Run

```bash
# Navigate to the project directory
cd typescript/decorator

# Install dependencies
npm install

# Build and run the application
npm run start
```

## Source Code

```typescript
     1	/**
     2	 * Decorator Design Pattern - Coffee Shop Example
     3	 *
     4	 * The Decorator pattern allows behavior to be added to individual objects,
     5	 * dynamically, without affecting the behavior of other objects from the same class.
     6	 */
     7
     8	// Component Interface - defines the interface for objects that can have responsibilities added
     9	interface Beverage {
    10	  getDescription(): string;
    11	  getCost(): number;
    12	}
    13
    14	// Concrete Component - Espresso
    15	class Espresso implements Beverage {
    16	  getDescription(): string {
    17	    return "Espresso";
    18	  }
    19
    20	  getCost(): number {
    21	    return 1.99;
    22	  }
    23	}
    24
    25	// Concrete Component - House Blend Coffee
    26	class HouseBlend implements Beverage {
    27	  getDescription(): string {
    28	    return "House Blend Coffee";
    29	  }
    30
    31	  getCost(): number {
    32	    return 0.89;
    33	  }
    34	}
    35
    36	// Concrete Component - Decaf Coffee
    37	class Decaf implements Beverage {
    38	  getDescription(): string {
    39	    return "Decaf Coffee";
    40	  }
    41
    42	  getCost(): number {
    43	    return 1.05;
    44	  }
    45	}
    46
    47	// Decorator Abstract Class - maintains a reference to a Component object
    48	abstract class CondimentDecorator implements Beverage {
    49	  protected beverage: Beverage;
    50
    51	  constructor(beverage: Beverage) {
    52	    this.beverage = beverage;
    53	  }
    54
    55	  abstract getDescription(): string;
    56	  abstract getCost(): number;
    57	}
    58
    59	// Concrete Decorator - Milk
    60	class Milk extends CondimentDecorator {
    61	  constructor(beverage: Beverage) {
    62	    super(beverage);
    63	  }
    64
    65	  getDescription(): string {
    66	    return this.beverage.getDescription() + ", Milk";
    67	  }
    68
    69	  getCost(): number {
    70	    return this.beverage.getCost() + 0.10;
    71	  }
    72	}
    73
    74	// Concrete Decorator - Mocha
    75	class Mocha extends CondimentDecorator {
    76	  constructor(beverage: Beverage) {
    77	    super(beverage);
    78	  }
    79
    80	  getDescription(): string {
    81	    return this.beverage.getDescription() + ", Mocha";
    82	  }
    83
    84	  getCost(): number {
    85	    return this.beverage.getCost() + 0.20;
    86	  }
    87	}
    88
    89	// Concrete Decorator - Soy
    90	class Soy extends CondimentDecorator {
    91	  constructor(beverage: Beverage) {
    92	    super(beverage);
    93	  }
    94
    95	  getDescription(): string {
    96	    return this.beverage.getDescription() + ", Soy";
    97	  }
    98
    99	  getCost(): number {
   100	    return this.beverage.getCost() + 0.15;
   101	  }
   102	}
   103
   104	// Concrete Decorator - Whip
   105	class Whip extends CondimentDecorator {
   106	  constructor(beverage: Beverage) {
   107	    super(beverage);
   108	  }
   109
   110	  getDescription(): string {
   111	    return this.beverage.getDescription() + ", Whip";
   112	  }
   113
   114	  getCost(): number {
   115	    return this.beverage.getCost() + 0.10;
   116	  }
   117	}
   118
   119	// Concrete Decorator - Caramel
   120	class Caramel extends CondimentDecorator {
   121	  constructor(beverage: Beverage) {
   122	    super(beverage);
   123	  }
   124
   125	  getDescription(): string {
   126	    return this.beverage.getDescription() + ", Caramel";
   127	  }
   128
   129	  getCost(): number {
   130	    return this.beverage.getCost() + 0.25;
   131	  }
   132	}
   133
   134	// Helper function to format currency
   135	function formatCurrency(amount: number): string {
   136	  return `$${amount.toFixed(2)}`;
   137	}
   138
   139	// Main execution
   140	console.log("=== Decorator Pattern: Coffee Shop ===\n");                          // [Line 1]
   141
   142	// Example 1: Simple Espresso (no decorators)
   143	console.log("--- Order 1: Plain Espresso ---");                                    // [Line 2]
   144	const espresso: Beverage = new Espresso();
   145	console.log(`[Line 3] Description: ${espresso.getDescription()}`);                 // [Line 3]
   146	console.log(`[Line 4] Cost: ${formatCurrency(espresso.getCost())}\n`);             // [Line 4]
   147
   148	// Example 2: House Blend with Milk (single decorator)
   149	console.log("--- Order 2: House Blend with Milk ---");                             // [Line 5]
   150	let houseBlend: Beverage = new HouseBlend();
   151	console.log(`[Line 6] Base: ${houseBlend.getDescription()} - ${formatCurrency(houseBlend.getCost())}`);  // [Line 6]
   152	houseBlend = new Milk(houseBlend);
   153	console.log(`[Line 7] After Milk: ${houseBlend.getDescription()}`);                // [Line 7]
   154	console.log(`[Line 8] Cost: ${formatCurrency(houseBlend.getCost())}\n`);           // [Line 8]
   155
   156	// Example 3: Espresso with double Mocha and Whip (multiple decorators)
   157	console.log("--- Order 3: Double Mocha Espresso with Whip ---");                   // [Line 9]
   158	let doubleMocha: Beverage = new Espresso();
   159	console.log(`[Line 10] Base: ${doubleMocha.getDescription()} - ${formatCurrency(doubleMocha.getCost())}`);  // [Line 10]
   160	doubleMocha = new Mocha(doubleMocha);
   161	console.log(`[Line 11] After 1st Mocha: ${doubleMocha.getDescription()} - ${formatCurrency(doubleMocha.getCost())}`);  // [Line 11]
   162	doubleMocha = new Mocha(doubleMocha);
   163	console.log(`[Line 12] After 2nd Mocha: ${doubleMocha.getDescription()} - ${formatCurrency(doubleMocha.getCost())}`);  // [Line 12]
   164	doubleMocha = new Whip(doubleMocha);
   165	console.log(`[Line 13] Final: ${doubleMocha.getDescription()}`);                   // [Line 13]
   166	console.log(`[Line 14] Cost: ${formatCurrency(doubleMocha.getCost())}\n`);         // [Line 14]
   167
   168	// Example 4: Decaf with Soy, Mocha, and Whip (stacking multiple different decorators)
   169	console.log("--- Order 4: Decaf with Soy, Mocha, and Whip ---");                   // [Line 15]
   170	let decafSpecial: Beverage = new Decaf();
   171	console.log(`[Line 16] Base: ${decafSpecial.getDescription()} - ${formatCurrency(decafSpecial.getCost())}`);  // [Line 16]
   172	decafSpecial = new Soy(decafSpecial);
   173	console.log(`[Line 17] After Soy: ${decafSpecial.getDescription()} - ${formatCurrency(decafSpecial.getCost())}`);  // [Line 17]
   174	decafSpecial = new Mocha(decafSpecial);
   175	console.log(`[Line 18] After Mocha: ${decafSpecial.getDescription()} - ${formatCurrency(decafSpecial.getCost())}`);  // [Line 18]
   176	decafSpecial = new Whip(decafSpecial);
   177	console.log(`[Line 19] Final: ${decafSpecial.getDescription()}`);                  // [Line 19]
   178	console.log(`[Line 20] Cost: ${formatCurrency(decafSpecial.getCost())}\n`);        // [Line 20]
   179
   180	// Example 5: Fancy Espresso with all condiments
   181	console.log("--- Order 5: Loaded Espresso (all condiments) ---");                  // [Line 21]
   182	let loadedEspresso: Beverage = new Espresso();
   183	console.log(`[Line 22] Base: ${loadedEspresso.getDescription()} - ${formatCurrency(loadedEspresso.getCost())}`);  // [Line 22]
   184	loadedEspresso = new Milk(loadedEspresso);
   185	loadedEspresso = new Mocha(loadedEspresso);
   186	loadedEspresso = new Soy(loadedEspresso);
   187	loadedEspresso = new Whip(loadedEspresso);
   188	loadedEspresso = new Caramel(loadedEspresso);
   189	console.log(`[Line 23] Final: ${loadedEspresso.getDescription()}`);                // [Line 23]
   190	console.log(`[Line 24] Cost: ${formatCurrency(loadedEspresso.getCost())}\n`);      // [Line 24]
   191
   192	// Summary
   193	console.log("=== Order Summary ===");                                              // [Line 25]
   194	console.log(`[Line 26] Order 1: ${espresso.getDescription()} = ${formatCurrency(espresso.getCost())}`);  // [Line 26]
   195	console.log(`[Line 27] Order 2: ${houseBlend.getDescription()} = ${formatCurrency(houseBlend.getCost())}`);  // [Line 27]
   196	console.log(`[Line 28] Order 3: ${doubleMocha.getDescription()} = ${formatCurrency(doubleMocha.getCost())}`);  // [Line 28]
   197	console.log(`[Line 29] Order 4: ${decafSpecial.getDescription()} = ${formatCurrency(decafSpecial.getCost())}`);  // [Line 29]
   198	console.log(`[Line 30] Order 5: ${loadedEspresso.getDescription()} = ${formatCurrency(loadedEspresso.getCost())}`);  // [Line 30]
```

## Program Output

```
=== Decorator Pattern: Coffee Shop ===

--- Order 1: Plain Espresso ---
[Line 3] Description: Espresso
[Line 4] Cost: $1.99

--- Order 2: House Blend with Milk ---
[Line 6] Base: House Blend Coffee - $0.89
[Line 7] After Milk: House Blend Coffee, Milk
[Line 8] Cost: $0.99

--- Order 3: Double Mocha Espresso with Whip ---
[Line 10] Base: Espresso - $1.99
[Line 11] After 1st Mocha: Espresso, Mocha - $2.19
[Line 12] After 2nd Mocha: Espresso, Mocha, Mocha - $2.39
[Line 13] Final: Espresso, Mocha, Mocha, Whip
[Line 14] Cost: $2.49

--- Order 4: Decaf with Soy, Mocha, and Whip ---
[Line 16] Base: Decaf Coffee - $1.05
[Line 17] After Soy: Decaf Coffee, Soy - $1.20
[Line 18] After Mocha: Decaf Coffee, Soy, Mocha - $1.40
[Line 19] Final: Decaf Coffee, Soy, Mocha, Whip
[Line 20] Cost: $1.50

--- Order 5: Loaded Espresso (all condiments) ---
[Line 22] Base: Espresso - $1.99
[Line 23] Final: Espresso, Milk, Mocha, Soy, Whip, Caramel
[Line 24] Cost: $2.79

=== Order Summary ===
[Line 26] Order 1: Espresso = $1.99
[Line 27] Order 2: House Blend Coffee, Milk = $0.99
[Line 28] Order 3: Espresso, Mocha, Mocha, Whip = $2.49
[Line 29] Order 4: Decaf Coffee, Soy, Mocha, Whip = $1.50
[Line 30] Order 5: Espresso, Milk, Mocha, Soy, Whip, Caramel = $2.79
```

## Code Analysis and Annotations

### Pattern Components

| Component | Source Lines | Description |
|-----------|-------------|-------------|
| Beverage (Component Interface) | 9-12 | Defines the interface that all beverages and decorators must implement |
| Espresso (Concrete Component) | 15-23 | Base beverage with fixed description and cost ($1.99) |
| HouseBlend (Concrete Component) | 26-34 | Base beverage with fixed description and cost ($0.89) |
| Decaf (Concrete Component) | 37-45 | Base beverage with fixed description and cost ($1.05) |
| CondimentDecorator (Abstract Decorator) | 48-57 | Base decorator class that holds reference to wrapped beverage |
| Milk, Mocha, Soy, Whip, Caramel (Concrete Decorators) | 60-132 | Add specific functionality and cost to wrapped beverages |

### Output to Source Code Correlation

| Output Line | Source Line | Explanation |
|-------------|-------------|-------------|
| [Line 3] | 145 | Creates Espresso and calls `getDescription()` returning "Espresso" from line 17 |
| [Line 4] | 146 | Calls `getCost()` returning 1.99 from line 21 |
| [Line 6] | 151 | Creates HouseBlend, shows base cost $0.89 from line 32 |
| [Line 7] | 153 | After wrapping with Milk decorator (line 152), description becomes "House Blend Coffee, Milk" via line 66 |
| [Line 8] | 154 | Cost becomes $0.99 ($0.89 + $0.10 milk) via recursive call in line 70 |
| [Line 10] | 159 | Creates Espresso base for double mocha order |
| [Line 11] | 161 | First Mocha decorator adds ", Mocha" and $0.20 via lines 81, 85 |
| [Line 12] | 163 | Second Mocha decorator wraps the first, adding another ", Mocha" and $0.20 |
| [Line 13] | 165 | Whip decorator adds ", Whip" via line 111 |
| [Line 14] | 166 | Final cost: $1.99 + $0.20 + $0.20 + $0.10 = $2.49 |
| [Line 16] | 171 | Creates Decaf base at $1.05 from line 43 |
| [Line 17] | 173 | Soy adds $0.15 via line 100, total $1.20 |
| [Line 18] | 175 | Mocha adds $0.20 via line 85, total $1.40 |
| [Line 19] | 177 | Whip adds $0.10 via line 115, description complete |
| [Line 20] | 178 | Final cost: $1.05 + $0.15 + $0.20 + $0.10 = $1.50 |
| [Line 22] | 183 | Creates Espresso base for fully loaded order |
| [Line 23] | 189 | After 5 decorators (lines 184-188), shows complete description |
| [Line 24] | 190 | Final cost: $1.99 + $0.10 + $0.20 + $0.15 + $0.10 + $0.25 = $2.79 |

### Decorator Cost Breakdown

| Decorator | Cost Addition | Source Line |
|-----------|--------------|-------------|
| Milk | $0.10 | 70 |
| Mocha | $0.20 | 85 |
| Soy | $0.15 | 100 |
| Whip | $0.10 | 115 |
| Caramel | $0.25 | 130 |

### Key Implementation Details

1. **Recursive Description Building** (Lines 65-67, 80-82, etc.)
   - Each decorator calls `this.beverage.getDescription()` first, then appends its own description
   - This creates a chain: Espresso -> Espresso, Mocha -> Espresso, Mocha, Mocha -> ...

2. **Recursive Cost Calculation** (Lines 69-71, 84-86, etc.)
   - Each decorator calls `this.beverage.getCost()` and adds its own cost
   - The recursion unwinds from the innermost component to the outermost decorator

3. **Same Decorator Multiple Times** (Lines 160-162)
   - Demonstrates that decorators can be applied multiple times (double Mocha)
   - Each application adds both description and cost independently

4. **Type Safety** (Lines 144, 150, 158, etc.)
   - All variables are typed as `Beverage` interface
   - Decorators and concrete components are interchangeable due to interface conformance

### Benefits Demonstrated

- **Open/Closed Principle**: New condiments can be added without modifying existing classes
- **Single Responsibility**: Each decorator handles only its specific functionality
- **Composition over Inheritance**: Behavior is composed at runtime rather than compile time
- **Flexible Combinations**: Any number of decorators can be stacked in any order
