/**
 * Strategy Design Pattern in TypeScript
 *
 * The Strategy pattern defines a family of algorithms, encapsulates each one,
 * and makes them interchangeable. Strategy lets the algorithm vary independently
 * from clients that use it.
 */

// Strategy Interface - defines the contract for all payment strategies
interface PaymentStrategy {
    pay(amount: number): boolean;
    getName(): string;
    getTransactionFee(amount: number): number;
}

// Concrete Strategy 1: Credit Card Payment
class CreditCardPayment implements PaymentStrategy {
    private cardNumber: string;
    private cardHolder: string;
    private expiryDate: string;

    constructor(cardNumber: string, cardHolder: string, expiryDate: string) {
        this.cardNumber = cardNumber;
        this.cardHolder = cardHolder;
        this.expiryDate = expiryDate;
        console.log(`[Line 24] CreditCardPayment initialized for ${cardHolder}`);
    }

    pay(amount: number): boolean {
        const fee = this.getTransactionFee(amount);
        const total = amount + fee;
        const maskedCard = `****-****-****-${this.cardNumber.slice(-4)}`;
        console.log(`[Line 31] Processing Credit Card payment...`);
        console.log(`[Line 32]   Card: ${maskedCard}`);
        console.log(`[Line 33]   Holder: ${this.cardHolder}`);
        console.log(`[Line 34]   Amount: $${amount.toFixed(2)}`);
        console.log(`[Line 35]   Fee (2.9%): $${fee.toFixed(2)}`);
        console.log(`[Line 36]   Total charged: $${total.toFixed(2)}`);
        console.log(`[Line 37]   Status: APPROVED`);
        return true;
    }

    getName(): string {
        return "Credit Card";
    }

    getTransactionFee(amount: number): number {
        return amount * 0.029; // 2.9% fee
    }
}

// Concrete Strategy 2: PayPal Payment
class PayPalPayment implements PaymentStrategy {
    private email: string;

    constructor(email: string) {
        this.email = email;
        console.log(`[Line 54] PayPalPayment initialized for ${email}`);
    }

    pay(amount: number): boolean {
        const fee = this.getTransactionFee(amount);
        const total = amount + fee;
        console.log(`[Line 60] Processing PayPal payment...`);
        console.log(`[Line 61]   Account: ${this.email}`);
        console.log(`[Line 62]   Amount: $${amount.toFixed(2)}`);
        console.log(`[Line 63]   Fee (3.49% + $0.49): $${fee.toFixed(2)}`);
        console.log(`[Line 64]   Total charged: $${total.toFixed(2)}`);
        console.log(`[Line 65]   Status: COMPLETED`);
        return true;
    }

    getName(): string {
        return "PayPal";
    }

    getTransactionFee(amount: number): number {
        return amount * 0.0349 + 0.49; // 3.49% + $0.49 fixed fee
    }
}

// Concrete Strategy 3: Cryptocurrency Payment
class CryptoPayment implements PaymentStrategy {
    private walletAddress: string;
    private cryptoType: string;

    constructor(walletAddress: string, cryptoType: string = "BTC") {
        this.walletAddress = walletAddress;
        this.cryptoType = cryptoType;
        console.log(`[Line 84] CryptoPayment initialized for ${cryptoType} wallet`);
    }

    pay(amount: number): boolean {
        const fee = this.getTransactionFee(amount);
        const total = amount + fee;
        const maskedWallet = `${this.walletAddress.slice(0, 6)}...${this.walletAddress.slice(-4)}`;
        console.log(`[Line 90] Processing ${this.cryptoType} payment...`);
        console.log(`[Line 91]   Wallet: ${maskedWallet}`);
        console.log(`[Line 92]   Amount: $${amount.toFixed(2)}`);
        console.log(`[Line 93]   Network fee (1%): $${fee.toFixed(2)}`);
        console.log(`[Line 94]   Total in ${this.cryptoType}: $${total.toFixed(2)}`);
        console.log(`[Line 95]   Status: CONFIRMED (6 blocks)`);
        return true;
    }

    getName(): string {
        return `Cryptocurrency (${this.cryptoType})`;
    }

    getTransactionFee(amount: number): number {
        return amount * 0.01; // 1% network fee
    }
}

// Concrete Strategy 4: Bank Transfer Payment
class BankTransferPayment implements PaymentStrategy {
    private accountNumber: string;
    private routingNumber: string;
    private bankName: string;

    constructor(accountNumber: string, routingNumber: string, bankName: string) {
        this.accountNumber = accountNumber;
        this.routingNumber = routingNumber;
        this.bankName = bankName;
        console.log(`[Line 116] BankTransferPayment initialized for ${bankName}`);
    }

    pay(amount: number): boolean {
        const fee = this.getTransactionFee(amount);
        const total = amount + fee;
        const maskedAccount = `****${this.accountNumber.slice(-4)}`;
        console.log(`[Line 122] Processing Bank Transfer...`);
        console.log(`[Line 123]   Bank: ${this.bankName}`);
        console.log(`[Line 124]   Account: ${maskedAccount}`);
        console.log(`[Line 125]   Amount: $${amount.toFixed(2)}`);
        console.log(`[Line 126]   Fee (flat $0.25): $${fee.toFixed(2)}`);
        console.log(`[Line 127]   Total transferred: $${total.toFixed(2)}`);
        console.log(`[Line 128]   Status: PENDING (1-3 business days)`);
        return true;
    }

    getName(): string {
        return "Bank Transfer (ACH)";
    }

    getTransactionFee(amount: number): number {
        return 0.25; // Flat fee
    }
}

// Context: ShoppingCart that uses the payment strategy
class ShoppingCart {
    private items: { name: string; price: number }[] = [];
    private paymentStrategy: PaymentStrategy | null = null;

    addItem(name: string, price: number): void {
        this.items.push({ name, price });
        console.log(`[Line 147] Added "${name}" ($${price.toFixed(2)}) to cart`);
    }

    setPaymentStrategy(strategy: PaymentStrategy): void {
        this.paymentStrategy = strategy;
        console.log(`[Line 152] Payment strategy set to: ${strategy.getName()}`);
    }

    getTotal(): number {
        return this.items.reduce((sum, item) => sum + item.price, 0);
    }

    showCart(): void {
        console.log(`[Line 159] Current cart contents:`);
        this.items.forEach((item, index) => {
            console.log(`[Line 161]   ${index + 1}. ${item.name}: $${item.price.toFixed(2)}`);
        });
        const subtotal = this.getTotal();
        console.log(`[Line 164]   Subtotal: $${subtotal.toFixed(2)}`);
    }

    checkout(): boolean {
        if (!this.paymentStrategy) {
            console.log(`[Line 169] Error: No payment strategy selected!`);
            return false;
        }

        const amount = this.getTotal();
        if (amount <= 0) {
            console.log(`[Line 175] Error: Cart is empty!`);
            return false;
        }

        console.log(`[Line 179] Starting checkout with ${this.paymentStrategy.getName()}...`);
        const success = this.paymentStrategy.pay(amount);

        if (success) {
            console.log(`[Line 183] Checkout completed successfully!`);
            this.items = []; // Clear cart after successful payment
        }

        return success;
    }

    comparePaymentMethods(strategies: PaymentStrategy[]): void {
        const amount = this.getTotal();
        console.log(`\n[Line 191] Fee comparison for $${amount.toFixed(2)} purchase:`);
        console.log(`[Line 192] ${"Method".padEnd(25)} | ${"Fee".padStart(10)} | ${"Total".padStart(10)}`);
        console.log(`[Line 193] ${"-".repeat(50)}`);

        strategies.forEach(strategy => {
            const fee = strategy.getTransactionFee(amount);
            const total = amount + fee;
            console.log(`[Line 197] ${strategy.getName().padEnd(25)} | $${fee.toFixed(2).padStart(9)} | $${total.toFixed(2).padStart(9)}`);
        });
    }
}

// Demonstration
function main(): void {
    console.log("=== Strategy Pattern Demonstration ===\n");

    // Create shopping cart
    const cart = new ShoppingCart();

    // Add items to cart
    console.log("--- Adding Items to Cart ---");
    cart.addItem("Mechanical Keyboard", 149.99);
    cart.addItem("Wireless Mouse", 79.99);
    cart.addItem("USB-C Hub", 49.99);
    cart.showCart();

    // Create different payment strategies
    console.log("\n--- Initializing Payment Strategies ---");
    const creditCard = new CreditCardPayment("4111111111111234", "John Doe", "12/25");
    const paypal = new PayPalPayment("john.doe@email.com");
    const crypto = new CryptoPayment("bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh", "BTC");
    const bankTransfer = new BankTransferPayment("123456789", "021000021", "Chase Bank");

    // Compare fees for all payment methods
    cart.comparePaymentMethods([creditCard, paypal, crypto, bankTransfer]);

    // Demo 1: Pay with Credit Card
    console.log("\n--- Demo 1: Checkout with Credit Card ---");
    cart.addItem("Mechanical Keyboard", 149.99);
    cart.addItem("Wireless Mouse", 79.99);
    cart.addItem("USB-C Hub", 49.99);
    cart.setPaymentStrategy(creditCard);
    cart.checkout();

    // Demo 2: Pay with PayPal
    console.log("\n--- Demo 2: Checkout with PayPal ---");
    cart.addItem("Monitor Stand", 89.99);
    cart.addItem("Webcam HD", 129.99);
    cart.setPaymentStrategy(paypal);
    cart.checkout();

    // Demo 3: Pay with Cryptocurrency
    console.log("\n--- Demo 3: Checkout with Cryptocurrency ---");
    cart.addItem("Gaming Headset", 199.99);
    cart.setPaymentStrategy(crypto);
    cart.checkout();

    // Demo 4: Switch strategy at runtime
    console.log("\n--- Demo 4: Dynamic Strategy Switching ---");
    cart.addItem("Laptop Stand", 59.99);
    cart.showCart();

    console.log(`\n[Line 244] Switching from Crypto to Bank Transfer...`);
    cart.setPaymentStrategy(bankTransfer);
    cart.checkout();

    // Demo 5: Error handling - no payment strategy
    console.log("\n--- Demo 5: Error Handling ---");
    const emptyCart = new ShoppingCart();
    emptyCart.addItem("Test Item", 10.00);
    console.log(`[Line 252] Attempting checkout without setting payment strategy...`);
    emptyCart.checkout();

    console.log("\n=== End of Demonstration ===");
}

main();
