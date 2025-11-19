/**
 * Decorator Design Pattern - Coffee Shop Example
 *
 * The Decorator pattern allows behavior to be added to individual objects,
 * dynamically, without affecting the behavior of other objects from the same class.
 */

// Component Interface - defines the interface for objects that can have responsibilities added
interface Beverage {
  getDescription(): string;
  getCost(): number;
}

// Concrete Component - Espresso
class Espresso implements Beverage {
  getDescription(): string {
    return "Espresso";
  }

  getCost(): number {
    return 1.99;
  }
}

// Concrete Component - House Blend Coffee
class HouseBlend implements Beverage {
  getDescription(): string {
    return "House Blend Coffee";
  }

  getCost(): number {
    return 0.89;
  }
}

// Concrete Component - Decaf Coffee
class Decaf implements Beverage {
  getDescription(): string {
    return "Decaf Coffee";
  }

  getCost(): number {
    return 1.05;
  }
}

// Decorator Abstract Class - maintains a reference to a Component object
abstract class CondimentDecorator implements Beverage {
  protected beverage: Beverage;

  constructor(beverage: Beverage) {
    this.beverage = beverage;
  }

  abstract getDescription(): string;
  abstract getCost(): number;
}

// Concrete Decorator - Milk
class Milk extends CondimentDecorator {
  constructor(beverage: Beverage) {
    super(beverage);
  }

  getDescription(): string {
    return this.beverage.getDescription() + ", Milk";
  }

  getCost(): number {
    return this.beverage.getCost() + 0.10;
  }
}

// Concrete Decorator - Mocha
class Mocha extends CondimentDecorator {
  constructor(beverage: Beverage) {
    super(beverage);
  }

  getDescription(): string {
    return this.beverage.getDescription() + ", Mocha";
  }

  getCost(): number {
    return this.beverage.getCost() + 0.20;
  }
}

// Concrete Decorator - Soy
class Soy extends CondimentDecorator {
  constructor(beverage: Beverage) {
    super(beverage);
  }

  getDescription(): string {
    return this.beverage.getDescription() + ", Soy";
  }

  getCost(): number {
    return this.beverage.getCost() + 0.15;
  }
}

// Concrete Decorator - Whip
class Whip extends CondimentDecorator {
  constructor(beverage: Beverage) {
    super(beverage);
  }

  getDescription(): string {
    return this.beverage.getDescription() + ", Whip";
  }

  getCost(): number {
    return this.beverage.getCost() + 0.10;
  }
}

// Concrete Decorator - Caramel
class Caramel extends CondimentDecorator {
  constructor(beverage: Beverage) {
    super(beverage);
  }

  getDescription(): string {
    return this.beverage.getDescription() + ", Caramel";
  }

  getCost(): number {
    return this.beverage.getCost() + 0.25;
  }
}

// Helper function to format currency
function formatCurrency(amount: number): string {
  return `$${amount.toFixed(2)}`;
}

// Main execution
console.log("=== Decorator Pattern: Coffee Shop ===\n");                          // [Line 1]

// Example 1: Simple Espresso (no decorators)
console.log("--- Order 1: Plain Espresso ---");                                    // [Line 2]
const espresso: Beverage = new Espresso();
console.log(`[Line 3] Description: ${espresso.getDescription()}`);                 // [Line 3]
console.log(`[Line 4] Cost: ${formatCurrency(espresso.getCost())}\n`);             // [Line 4]

// Example 2: House Blend with Milk (single decorator)
console.log("--- Order 2: House Blend with Milk ---");                             // [Line 5]
let houseBlend: Beverage = new HouseBlend();
console.log(`[Line 6] Base: ${houseBlend.getDescription()} - ${formatCurrency(houseBlend.getCost())}`);  // [Line 6]
houseBlend = new Milk(houseBlend);
console.log(`[Line 7] After Milk: ${houseBlend.getDescription()}`);                // [Line 7]
console.log(`[Line 8] Cost: ${formatCurrency(houseBlend.getCost())}\n`);           // [Line 8]

// Example 3: Espresso with double Mocha and Whip (multiple decorators)
console.log("--- Order 3: Double Mocha Espresso with Whip ---");                   // [Line 9]
let doubleMocha: Beverage = new Espresso();
console.log(`[Line 10] Base: ${doubleMocha.getDescription()} - ${formatCurrency(doubleMocha.getCost())}`);  // [Line 10]
doubleMocha = new Mocha(doubleMocha);
console.log(`[Line 11] After 1st Mocha: ${doubleMocha.getDescription()} - ${formatCurrency(doubleMocha.getCost())}`);  // [Line 11]
doubleMocha = new Mocha(doubleMocha);
console.log(`[Line 12] After 2nd Mocha: ${doubleMocha.getDescription()} - ${formatCurrency(doubleMocha.getCost())}`);  // [Line 12]
doubleMocha = new Whip(doubleMocha);
console.log(`[Line 13] Final: ${doubleMocha.getDescription()}`);                   // [Line 13]
console.log(`[Line 14] Cost: ${formatCurrency(doubleMocha.getCost())}\n`);         // [Line 14]

// Example 4: Decaf with Soy, Mocha, and Whip (stacking multiple different decorators)
console.log("--- Order 4: Decaf with Soy, Mocha, and Whip ---");                   // [Line 15]
let decafSpecial: Beverage = new Decaf();
console.log(`[Line 16] Base: ${decafSpecial.getDescription()} - ${formatCurrency(decafSpecial.getCost())}`);  // [Line 16]
decafSpecial = new Soy(decafSpecial);
console.log(`[Line 17] After Soy: ${decafSpecial.getDescription()} - ${formatCurrency(decafSpecial.getCost())}`);  // [Line 17]
decafSpecial = new Mocha(decafSpecial);
console.log(`[Line 18] After Mocha: ${decafSpecial.getDescription()} - ${formatCurrency(decafSpecial.getCost())}`);  // [Line 18]
decafSpecial = new Whip(decafSpecial);
console.log(`[Line 19] Final: ${decafSpecial.getDescription()}`);                  // [Line 19]
console.log(`[Line 20] Cost: ${formatCurrency(decafSpecial.getCost())}\n`);        // [Line 20]

// Example 5: Fancy Espresso with all condiments
console.log("--- Order 5: Loaded Espresso (all condiments) ---");                  // [Line 21]
let loadedEspresso: Beverage = new Espresso();
console.log(`[Line 22] Base: ${loadedEspresso.getDescription()} - ${formatCurrency(loadedEspresso.getCost())}`);  // [Line 22]
loadedEspresso = new Milk(loadedEspresso);
loadedEspresso = new Mocha(loadedEspresso);
loadedEspresso = new Soy(loadedEspresso);
loadedEspresso = new Whip(loadedEspresso);
loadedEspresso = new Caramel(loadedEspresso);
console.log(`[Line 23] Final: ${loadedEspresso.getDescription()}`);                // [Line 23]
console.log(`[Line 24] Cost: ${formatCurrency(loadedEspresso.getCost())}\n`);      // [Line 24]

// Summary
console.log("=== Order Summary ===");                                              // [Line 25]
console.log(`[Line 26] Order 1: ${espresso.getDescription()} = ${formatCurrency(espresso.getCost())}`);  // [Line 26]
console.log(`[Line 27] Order 2: ${houseBlend.getDescription()} = ${formatCurrency(houseBlend.getCost())}`);  // [Line 27]
console.log(`[Line 28] Order 3: ${doubleMocha.getDescription()} = ${formatCurrency(doubleMocha.getCost())}`);  // [Line 28]
console.log(`[Line 29] Order 4: ${decafSpecial.getDescription()} = ${formatCurrency(decafSpecial.getCost())}`);  // [Line 29]
console.log(`[Line 30] Order 5: ${loadedEspresso.getDescription()} = ${formatCurrency(loadedEspresso.getCost())}`);  // [Line 30]
