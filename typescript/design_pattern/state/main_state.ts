/**
 * State Design Pattern in TypeScript
 *
 * The State pattern allows an object to alter its behavior when its internal
 * state changes. The object will appear to change its class. This pattern
 * encapsulates state-specific behavior into separate state classes.
 */

// State Interface - defines the common interface for all concrete states
interface VendingMachineState {
    insertMoney(amount: number): void;
    selectProduct(product: string): void;
    dispense(): void;
    refund(): void;
    getName(): string;
}

// Context - maintains an instance of a ConcreteState subclass
class VendingMachine {
    private state: VendingMachineState;
    private balance: number = 0;
    private selectedProduct: string = "";
    private inventory: Map<string, { price: number; quantity: number }>;

    // States
    private idleState: VendingMachineState;
    private hasMoneyState: VendingMachineState;
    private productSelectedState: VendingMachineState;
    private dispensingState: VendingMachineState;
    private soldOutState: VendingMachineState;

    constructor() {
        // Initialize states
        this.idleState = new IdleState(this);
        this.hasMoneyState = new HasMoneyState(this);
        this.productSelectedState = new ProductSelectedState(this);
        this.dispensingState = new DispensingState(this);
        this.soldOutState = new SoldOutState(this);

        // Initialize inventory
        this.inventory = new Map([
            ["Cola", { price: 150, quantity: 3 }],
            ["Chips", { price: 100, quantity: 2 }],
            ["Candy", { price: 75, quantity: 5 }],
            ["Water", { price: 125, quantity: 0 }]  // Sold out item
        ]);

        // Start in idle state
        this.state = this.idleState;
        console.log("[Line 47] VendingMachine: Initialized in IdleState");
        console.log("[Line 48] VendingMachine: Inventory loaded with 4 products");
    }

    // State setters
    setState(state: VendingMachineState): void {
        console.log(`[Line 52] VendingMachine: Transitioning from ${this.state.getName()} to ${state.getName()}`);
        this.state = state;
    }

    // Getters for states
    getIdleState(): VendingMachineState { return this.idleState; }
    getHasMoneyState(): VendingMachineState { return this.hasMoneyState; }
    getProductSelectedState(): VendingMachineState { return this.productSelectedState; }
    getDispensingState(): VendingMachineState { return this.dispensingState; }
    getSoldOutState(): VendingMachineState { return this.soldOutState; }

    // Balance management
    getBalance(): number { return this.balance; }
    addBalance(amount: number): void {
        this.balance += amount;
        console.log(`[Line 66] VendingMachine: Balance updated to ${this.balance} cents`);
    }
    resetBalance(): void {
        const previousBalance = this.balance;
        this.balance = 0;
        console.log(`[Line 70] VendingMachine: Balance reset from ${previousBalance} to 0 cents`);
    }

    // Product management
    getSelectedProduct(): string { return this.selectedProduct; }
    setSelectedProduct(product: string): void {
        this.selectedProduct = product;
        console.log(`[Line 77] VendingMachine: Selected product set to "${product}"`);
    }

    // Inventory management
    getProductPrice(product: string): number {
        const item = this.inventory.get(product);
        return item ? item.price : 0;
    }

    getProductQuantity(product: string): number {
        const item = this.inventory.get(product);
        return item ? item.quantity : 0;
    }

    hasProduct(product: string): boolean {
        return this.inventory.has(product);
    }

    decrementProduct(product: string): void {
        const item = this.inventory.get(product);
        if (item && item.quantity > 0) {
            item.quantity--;
            console.log(`[Line 98] VendingMachine: ${product} quantity decreased to ${item.quantity}`);
        }
    }

    // Delegated methods to current state
    insertMoney(amount: number): void {
        console.log(`\n[Line 104] VendingMachine: insertMoney(${amount}) called in ${this.state.getName()}`);
        this.state.insertMoney(amount);
    }

    selectProduct(product: string): void {
        console.log(`\n[Line 109] VendingMachine: selectProduct("${product}") called in ${this.state.getName()}`);
        this.state.selectProduct(product);
    }

    dispense(): void {
        console.log(`\n[Line 114] VendingMachine: dispense() called in ${this.state.getName()}`);
        this.state.dispense();
    }

    refund(): void {
        console.log(`\n[Line 119] VendingMachine: refund() called in ${this.state.getName()}`);
        this.state.refund();
    }

    // Display current state
    displayStatus(): void {
        console.log(`\n[Line 125] --- Machine Status ---`);
        console.log(`[Line 126] Current State: ${this.state.getName()}`);
        console.log(`[Line 127] Balance: ${this.balance} cents`);
        console.log(`[Line 128] Selected Product: ${this.selectedProduct || "None"}`);
    }
}

// Concrete State 1: Idle State
class IdleState implements VendingMachineState {
    private machine: VendingMachine;

    constructor(machine: VendingMachine) {
        this.machine = machine;
    }

    getName(): string { return "IdleState"; }

    insertMoney(amount: number): void {
        console.log(`[Line 142] IdleState: Accepting ${amount} cents`);
        this.machine.addBalance(amount);
        this.machine.setState(this.machine.getHasMoneyState());
    }

    selectProduct(product: string): void {
        console.log(`[Line 148] IdleState: Cannot select product - please insert money first`);
    }

    dispense(): void {
        console.log(`[Line 152] IdleState: Cannot dispense - please insert money and select a product`);
    }

    refund(): void {
        console.log(`[Line 156] IdleState: No money to refund`);
    }
}

// Concrete State 2: Has Money State
class HasMoneyState implements VendingMachineState {
    private machine: VendingMachine;

    constructor(machine: VendingMachine) {
        this.machine = machine;
    }

    getName(): string { return "HasMoneyState"; }

    insertMoney(amount: number): void {
        console.log(`[Line 171] HasMoneyState: Adding ${amount} cents to existing balance`);
        this.machine.addBalance(amount);
    }

    selectProduct(product: string): void {
        console.log(`[Line 176] HasMoneyState: Processing product selection "${product}"`);

        if (!this.machine.hasProduct(product)) {
            console.log(`[Line 179] HasMoneyState: Product "${product}" not found in inventory`);
            return;
        }

        const quantity = this.machine.getProductQuantity(product);
        if (quantity === 0) {
            console.log(`[Line 185] HasMoneyState: "${product}" is sold out`);
            this.machine.setState(this.machine.getSoldOutState());
            return;
        }

        const price = this.machine.getProductPrice(product);
        const balance = this.machine.getBalance();

        console.log(`[Line 193] HasMoneyState: ${product} costs ${price} cents, balance is ${balance} cents`);

        if (balance >= price) {
            console.log(`[Line 196] HasMoneyState: Sufficient balance - proceeding to selection`);
            this.machine.setSelectedProduct(product);
            this.machine.setState(this.machine.getProductSelectedState());
        } else {
            console.log(`[Line 200] HasMoneyState: Insufficient balance - need ${price - balance} more cents`);
        }
    }

    dispense(): void {
        console.log(`[Line 205] HasMoneyState: Cannot dispense - please select a product first`);
    }

    refund(): void {
        const balance = this.machine.getBalance();
        console.log(`[Line 210] HasMoneyState: Refunding ${balance} cents`);
        this.machine.resetBalance();
        this.machine.setState(this.machine.getIdleState());
    }
}

// Concrete State 3: Product Selected State
class ProductSelectedState implements VendingMachineState {
    private machine: VendingMachine;

    constructor(machine: VendingMachine) {
        this.machine = machine;
    }

    getName(): string { return "ProductSelectedState"; }

    insertMoney(amount: number): void {
        console.log(`[Line 227] ProductSelectedState: Cannot accept money - product already selected`);
    }

    selectProduct(product: string): void {
        console.log(`[Line 231] ProductSelectedState: Cannot change selection - please dispense or refund first`);
    }

    dispense(): void {
        const product = this.machine.getSelectedProduct();
        const price = this.machine.getProductPrice(product);

        console.log(`[Line 238] ProductSelectedState: Dispensing ${product}...`);
        this.machine.setState(this.machine.getDispensingState());

        // Perform the dispensing action
        this.machine.dispense();
    }

    refund(): void {
        const balance = this.machine.getBalance();
        console.log(`[Line 247] ProductSelectedState: Canceling transaction, refunding ${balance} cents`);
        this.machine.setSelectedProduct("");
        this.machine.resetBalance();
        this.machine.setState(this.machine.getIdleState());
    }
}

// Concrete State 4: Dispensing State
class DispensingState implements VendingMachineState {
    private machine: VendingMachine;

    constructor(machine: VendingMachine) {
        this.machine = machine;
    }

    getName(): string { return "DispensingState"; }

    insertMoney(amount: number): void {
        console.log(`[Line 265] DispensingState: Please wait - dispensing in progress`);
    }

    selectProduct(product: string): void {
        console.log(`[Line 269] DispensingState: Please wait - dispensing in progress`);
    }

    dispense(): void {
        const product = this.machine.getSelectedProduct();
        const price = this.machine.getProductPrice(product);
        const balance = this.machine.getBalance();

        console.log(`[Line 277] DispensingState: **** ${product} dispensed! ****`);

        // Update inventory and balance
        this.machine.decrementProduct(product);

        // Calculate and return change
        const change = balance - price;
        if (change > 0) {
            console.log(`[Line 285] DispensingState: Returning ${change} cents in change`);
        } else {
            console.log(`[Line 287] DispensingState: No change to return`);
        }

        // Reset machine
        this.machine.resetBalance();
        this.machine.setSelectedProduct("");
        this.machine.setState(this.machine.getIdleState());

        console.log(`[Line 295] DispensingState: Transaction complete`);
    }

    refund(): void {
        console.log(`[Line 299] DispensingState: Cannot refund - dispensing in progress`);
    }
}

// Concrete State 5: Sold Out State
class SoldOutState implements VendingMachineState {
    private machine: VendingMachine;

    constructor(machine: VendingMachine) {
        this.machine = machine;
    }

    getName(): string { return "SoldOutState"; }

    insertMoney(amount: number): void {
        console.log(`[Line 314] SoldOutState: Cannot accept money - please select a different product`);
    }

    selectProduct(product: string): void {
        console.log(`[Line 318] SoldOutState: Returning to HasMoneyState to try another product`);
        this.machine.setState(this.machine.getHasMoneyState());
        this.machine.selectProduct(product);
    }

    dispense(): void {
        console.log(`[Line 324] SoldOutState: Cannot dispense - product is sold out`);
    }

    refund(): void {
        const balance = this.machine.getBalance();
        console.log(`[Line 329] SoldOutState: Refunding ${balance} cents due to sold out product`);
        this.machine.resetBalance();
        this.machine.setState(this.machine.getIdleState());
    }
}

// Demonstration
function main(): void {
    console.log("=== State Pattern Demonstration - Vending Machine ===\n");

    const vendingMachine = new VendingMachine();

    // Demo 1: Successful purchase
    console.log("\n\n--- Demo 1: Successful Purchase ---");
    vendingMachine.insertMoney(100);
    vendingMachine.insertMoney(100);  // Total: 200 cents
    vendingMachine.selectProduct("Cola");  // Costs 150 cents
    vendingMachine.dispense();  // Should get 50 cents change

    // Demo 2: Attempt actions in wrong state
    console.log("\n\n--- Demo 2: Invalid Operations ---");
    vendingMachine.selectProduct("Chips");  // Should fail - no money
    vendingMachine.dispense();  // Should fail - no money/product
    vendingMachine.refund();  // Should fail - nothing to refund

    // Demo 3: Insufficient balance
    console.log("\n\n--- Demo 3: Insufficient Balance ---");
    vendingMachine.insertMoney(50);
    vendingMachine.selectProduct("Candy");  // Costs 75 cents - not enough
    vendingMachine.insertMoney(25);  // Now have 75 cents
    vendingMachine.selectProduct("Candy");  // Should work now
    vendingMachine.dispense();

    // Demo 4: Sold out product
    console.log("\n\n--- Demo 4: Sold Out Product ---");
    vendingMachine.insertMoney(200);
    vendingMachine.selectProduct("Water");  // Sold out
    vendingMachine.selectProduct("Chips");  // Switch to available product
    vendingMachine.dispense();

    // Demo 5: Refund from different states
    console.log("\n\n--- Demo 5: Refund Operations ---");
    vendingMachine.insertMoney(150);
    vendingMachine.displayStatus();
    vendingMachine.refund();  // Refund from HasMoneyState

    // Demo 6: Cancel after product selection
    console.log("\n\n--- Demo 6: Cancel After Selection ---");
    vendingMachine.insertMoney(200);
    vendingMachine.selectProduct("Chips");
    vendingMachine.displayStatus();
    vendingMachine.refund();  // Refund from ProductSelectedState

    // Demo 7: Multiple products in sequence
    console.log("\n\n--- Demo 7: Multiple Purchases ---");
    for (let i = 0; i < 2; i++) {
        console.log(`\n[Line 383] === Purchase ${i + 1} ===`);
        vendingMachine.insertMoney(100);
        vendingMachine.selectProduct("Candy");
        vendingMachine.dispense();
    }

    // Final status
    vendingMachine.displayStatus();

    console.log("\n\n=== End of Demonstration ===");
}

main();
