# Strategy Design Pattern in TypeScript

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This allows the algorithm to vary independently from the clients that use it. It's particularly useful when you have multiple ways of performing an action and want to select the appropriate algorithm at runtime.

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
2    * Strategy Design Pattern in TypeScript
3    *
4    * The Strategy pattern defines a family of algorithms, encapsulates each one,
5    * and makes them interchangeable. Strategy lets the algorithm vary independently
6    * from clients that use it.
7    */
8
9   // Strategy Interface - defines the contract for all payment strategies
10  interface PaymentStrategy {
11      pay(amount: number): boolean;
12      getName(): string;
13      getTransactionFee(amount: number): number;
14  }
15
16  // Concrete Strategy 1: Credit Card Payment
17  class CreditCardPayment implements PaymentStrategy {
18      private cardNumber: string;
19      private cardHolder: string;
20      private expiryDate: string;
21
22      constructor(cardNumber: string, cardHolder: string, expiryDate: string) {
23          this.cardNumber = cardNumber;
24          this.cardHolder = cardHolder;
25          this.expiryDate = expiryDate;
26          console.log(`[Line 24] CreditCardPayment initialized for ${cardHolder}`);
27      }
28
29      pay(amount: number): boolean {
30          const fee = this.getTransactionFee(amount);
31          const total = amount + fee;
32          const maskedCard = `****-****-****-${this.cardNumber.slice(-4)}`;
33          console.log(`[Line 31] Processing Credit Card payment...`);
34          console.log(`[Line 32]   Card: ${maskedCard}`);
35          console.log(`[Line 33]   Holder: ${this.cardHolder}`);
36          console.log(`[Line 34]   Amount: $${amount.toFixed(2)}`);
37          console.log(`[Line 35]   Fee (2.9%): $${fee.toFixed(2)}`);
38          console.log(`[Line 36]   Total charged: $${total.toFixed(2)}`);
39          console.log(`[Line 37]   Status: APPROVED`);
40          return true;
41      }
42
43      getName(): string {
44          return "Credit Card";
45      }
46
47      getTransactionFee(amount: number): number {
48          return amount * 0.029; // 2.9% fee
49      }
50  }
51
52  // Concrete Strategy 2: PayPal Payment
53  class PayPalPayment implements PaymentStrategy {
54      private email: string;
55
56      constructor(email: string) {
57          this.email = email;
58          console.log(`[Line 54] PayPalPayment initialized for ${email}`);
59      }
60
61      pay(amount: number): boolean {
62          const fee = this.getTransactionFee(amount);
63          const total = amount + fee;
64          console.log(`[Line 60] Processing PayPal payment...`);
65          console.log(`[Line 61]   Account: ${this.email}`);
66          console.log(`[Line 62]   Amount: $${amount.toFixed(2)}`);
67          console.log(`[Line 63]   Fee (3.49% + $0.49): $${fee.toFixed(2)}`);
68          console.log(`[Line 64]   Total charged: $${total.toFixed(2)}`);
69          console.log(`[Line 65]   Status: COMPLETED`);
70          return true;
71      }
72
73      getName(): string {
74          return "PayPal";
75      }
76
77      getTransactionFee(amount: number): number {
78          return amount * 0.0349 + 0.49; // 3.49% + $0.49 fixed fee
79      }
80  }
81
82  // Concrete Strategy 3: Cryptocurrency Payment
83  class CryptoPayment implements PaymentStrategy {
84      private walletAddress: string;
85      private cryptoType: string;
86
87      constructor(walletAddress: string, cryptoType: string = "BTC") {
88          this.walletAddress = walletAddress;
89          this.cryptoType = cryptoType;
90          console.log(`[Line 84] CryptoPayment initialized for ${cryptoType} wallet`);
91      }
92
93      pay(amount: number): boolean {
94          const fee = this.getTransactionFee(amount);
95          const total = amount + fee;
96          const maskedWallet = `${this.walletAddress.slice(0, 6)}...${this.walletAddress.slice(-4)}`;
97          console.log(`[Line 90] Processing ${this.cryptoType} payment...`);
98          console.log(`[Line 91]   Wallet: ${maskedWallet}`);
99          console.log(`[Line 92]   Amount: $${amount.toFixed(2)}`);
100         console.log(`[Line 93]   Network fee (1%): $${fee.toFixed(2)}`);
101         console.log(`[Line 94]   Total in ${this.cryptoType}: $${total.toFixed(2)}`);
102         console.log(`[Line 95]   Status: CONFIRMED (6 blocks)`);
103         return true;
104     }
105
106     getName(): string {
107         return `Cryptocurrency (${this.cryptoType})`;
108     }
109
110     getTransactionFee(amount: number): number {
111         return amount * 0.01; // 1% network fee
112     }
113 }
114
115 // Concrete Strategy 4: Bank Transfer Payment
116 class BankTransferPayment implements PaymentStrategy {
117     private accountNumber: string;
118     private routingNumber: string;
119     private bankName: string;
120
121     constructor(accountNumber: string, routingNumber: string, bankName: string) {
122         this.accountNumber = accountNumber;
123         this.routingNumber = routingNumber;
124         this.bankName = bankName;
125         console.log(`[Line 116] BankTransferPayment initialized for ${bankName}`);
126     }
127
128     pay(amount: number): boolean {
129         const fee = this.getTransactionFee(amount);
130         const total = amount + fee;
131         const maskedAccount = `****${this.accountNumber.slice(-4)}`;
132         console.log(`[Line 122] Processing Bank Transfer...`);
133         console.log(`[Line 123]   Bank: ${this.bankName}`);
134         console.log(`[Line 124]   Account: ${maskedAccount}`);
135         console.log(`[Line 125]   Amount: $${amount.toFixed(2)}`);
136         console.log(`[Line 126]   Fee (flat $0.25): $${fee.toFixed(2)}`);
137         console.log(`[Line 127]   Total transferred: $${total.toFixed(2)}`);
138         console.log(`[Line 128]   Status: PENDING (1-3 business days)`);
139         return true;
140     }
141
142     getName(): string {
143         return "Bank Transfer (ACH)";
144     }
145
146     getTransactionFee(amount: number): number {
147         return 0.25; // Flat fee
148     }
149 }
150
151 // Context: ShoppingCart that uses the payment strategy
152 class ShoppingCart {
153     private items: { name: string; price: number }[] = [];
154     private paymentStrategy: PaymentStrategy | null = null;
155
156     addItem(name: string, price: number): void {
157         this.items.push({ name, price });
158         console.log(`[Line 147] Added "${name}" ($${price.toFixed(2)}) to cart`);
159     }
160
161     setPaymentStrategy(strategy: PaymentStrategy): void {
162         this.paymentStrategy = strategy;
163         console.log(`[Line 152] Payment strategy set to: ${strategy.getName()}`);
164     }
165
166     getTotal(): number {
167         return this.items.reduce((sum, item) => sum + item.price, 0);
168     }
169
170     showCart(): void {
171         console.log(`[Line 159] Current cart contents:`);
172         this.items.forEach((item, index) => {
173             console.log(`[Line 161]   ${index + 1}. ${item.name}: $${item.price.toFixed(2)}`);
174         });
175         const subtotal = this.getTotal();
176         console.log(`[Line 164]   Subtotal: $${subtotal.toFixed(2)}`);
177     }
178
179     checkout(): boolean {
180         if (!this.paymentStrategy) {
181             console.log(`[Line 169] Error: No payment strategy selected!`);
182             return false;
183         }
184
185         const amount = this.getTotal();
186         if (amount <= 0) {
187             console.log(`[Line 175] Error: Cart is empty!`);
188             return false;
189         }
190
191         console.log(`[Line 179] Starting checkout with ${this.paymentStrategy.getName()}...`);
192         const success = this.paymentStrategy.pay(amount);
193
194         if (success) {
195             console.log(`[Line 183] Checkout completed successfully!`);
196             this.items = []; // Clear cart after successful payment
197         }
198
199         return success;
200     }
201
202     comparePaymentMethods(strategies: PaymentStrategy[]): void {
203         const amount = this.getTotal();
204         console.log(`\n[Line 191] Fee comparison for $${amount.toFixed(2)} purchase:`);
205         console.log(`[Line 192] ${"Method".padEnd(25)} | ${"Fee".padStart(10)} | ${"Total".padStart(10)}`);
206         console.log(`[Line 193] ${"-".repeat(50)}`);
207
208         strategies.forEach(strategy => {
209             const fee = strategy.getTransactionFee(amount);
210             const total = amount + fee;
211             console.log(`[Line 197] ${strategy.getName().padEnd(25)} | $${fee.toFixed(2).padStart(9)} | $${total.toFixed(2).padStart(9)}`);
212         });
213     }
214 }
215
216 // Demonstration
217 function main(): void {
218     console.log("=== Strategy Pattern Demonstration ===\n");
219
220     // Create shopping cart
221     const cart = new ShoppingCart();
222
223     // Add items to cart
224     console.log("--- Adding Items to Cart ---");
225     cart.addItem("Mechanical Keyboard", 149.99);
226     cart.addItem("Wireless Mouse", 79.99);
227     cart.addItem("USB-C Hub", 49.99);
228     cart.showCart();
229
230     // Create different payment strategies
231     console.log("\n--- Initializing Payment Strategies ---");
232     const creditCard = new CreditCardPayment("4111111111111234", "John Doe", "12/25");
233     const paypal = new PayPalPayment("john.doe@email.com");
234     const crypto = new CryptoPayment("bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh", "BTC");
235     const bankTransfer = new BankTransferPayment("123456789", "021000021", "Chase Bank");
236
237     // Compare fees for all payment methods
238     cart.comparePaymentMethods([creditCard, paypal, crypto, bankTransfer]);
239
240     // Demo 1: Pay with Credit Card
241     console.log("\n--- Demo 1: Checkout with Credit Card ---");
242     cart.addItem("Mechanical Keyboard", 149.99);
243     cart.addItem("Wireless Mouse", 79.99);
244     cart.addItem("USB-C Hub", 49.99);
245     cart.setPaymentStrategy(creditCard);
246     cart.checkout();
247
248     // Demo 2: Pay with PayPal
249     console.log("\n--- Demo 2: Checkout with PayPal ---");
250     cart.addItem("Monitor Stand", 89.99);
251     cart.addItem("Webcam HD", 129.99);
252     cart.setPaymentStrategy(paypal);
253     cart.checkout();
254
255     // Demo 3: Pay with Cryptocurrency
256     console.log("\n--- Demo 3: Checkout with Cryptocurrency ---");
257     cart.addItem("Gaming Headset", 199.99);
258     cart.setPaymentStrategy(crypto);
259     cart.checkout();
260
261     // Demo 4: Switch strategy at runtime
262     console.log("\n--- Demo 4: Dynamic Strategy Switching ---");
263     cart.addItem("Laptop Stand", 59.99);
264     cart.showCart();
265
266     console.log(`\n[Line 244] Switching from Crypto to Bank Transfer...`);
267     cart.setPaymentStrategy(bankTransfer);
268     cart.checkout();
269
270     // Demo 5: Error handling - no payment strategy
271     console.log("\n--- Demo 5: Error Handling ---");
272     const emptyCart = new ShoppingCart();
273     emptyCart.addItem("Test Item", 10.00);
274     console.log(`[Line 252] Attempting checkout without setting payment strategy...`);
275     emptyCart.checkout();
276
277     console.log("\n=== End of Demonstration ===");
278 }
279
280 main();
```

## Program Output

```
=== Strategy Pattern Demonstration ===

--- Adding Items to Cart ---
[Line 147] Added "Mechanical Keyboard" ($149.99) to cart
[Line 147] Added "Wireless Mouse" ($79.99) to cart
[Line 147] Added "USB-C Hub" ($49.99) to cart
[Line 159] Current cart contents:
[Line 161]   1. Mechanical Keyboard: $149.99
[Line 161]   2. Wireless Mouse: $79.99
[Line 161]   3. USB-C Hub: $49.99
[Line 164]   Subtotal: $279.97

--- Initializing Payment Strategies ---
[Line 24] CreditCardPayment initialized for John Doe
[Line 54] PayPalPayment initialized for john.doe@email.com
[Line 84] CryptoPayment initialized for BTC wallet
[Line 116] BankTransferPayment initialized for Chase Bank

[Line 191] Fee comparison for $279.97 purchase:
[Line 192] Method                    |        Fee |      Total
[Line 193] --------------------------------------------------
[Line 197] Credit Card               | $     8.12 | $   288.09
[Line 197] PayPal                    | $    10.26 | $   290.23
[Line 197] Cryptocurrency (BTC)      | $     2.80 | $   282.77
[Line 197] Bank Transfer (ACH)       | $     0.25 | $   280.22

--- Demo 1: Checkout with Credit Card ---
[Line 147] Added "Mechanical Keyboard" ($149.99) to cart
[Line 147] Added "Wireless Mouse" ($79.99) to cart
[Line 147] Added "USB-C Hub" ($49.99) to cart
[Line 152] Payment strategy set to: Credit Card
[Line 179] Starting checkout with Credit Card...
[Line 31] Processing Credit Card payment...
[Line 32]   Card: ****-****-****-1234
[Line 33]   Holder: John Doe
[Line 34]   Amount: $559.94
[Line 35]   Fee (2.9%): $16.24
[Line 36]   Total charged: $576.18
[Line 37]   Status: APPROVED
[Line 183] Checkout completed successfully!

--- Demo 2: Checkout with PayPal ---
[Line 147] Added "Monitor Stand" ($89.99) to cart
[Line 147] Added "Webcam HD" ($129.99) to cart
[Line 152] Payment strategy set to: PayPal
[Line 179] Starting checkout with PayPal...
[Line 60] Processing PayPal payment...
[Line 61]   Account: john.doe@email.com
[Line 62]   Amount: $219.98
[Line 63]   Fee (3.49% + $0.49): $8.17
[Line 64]   Total charged: $228.15
[Line 65]   Status: COMPLETED
[Line 183] Checkout completed successfully!

--- Demo 3: Checkout with Cryptocurrency ---
[Line 147] Added "Gaming Headset" ($199.99) to cart
[Line 152] Payment strategy set to: Cryptocurrency (BTC)
[Line 179] Starting checkout with Cryptocurrency (BTC)...
[Line 90] Processing BTC payment...
[Line 91]   Wallet: bc1qxy...0wlh
[Line 92]   Amount: $199.99
[Line 93]   Network fee (1%): $2.00
[Line 94]   Total in BTC: $201.99
[Line 95]   Status: CONFIRMED (6 blocks)
[Line 183] Checkout completed successfully!

--- Demo 4: Dynamic Strategy Switching ---
[Line 147] Added "Laptop Stand" ($59.99) to cart
[Line 159] Current cart contents:
[Line 161]   1. Laptop Stand: $59.99
[Line 164]   Subtotal: $59.99

[Line 244] Switching from Crypto to Bank Transfer...
[Line 152] Payment strategy set to: Bank Transfer (ACH)
[Line 179] Starting checkout with Bank Transfer (ACH)...
[Line 122] Processing Bank Transfer...
[Line 123]   Bank: Chase Bank
[Line 124]   Account: ****6789
[Line 125]   Amount: $59.99
[Line 126]   Fee (flat $0.25): $0.25
[Line 127]   Total transferred: $60.24
[Line 128]   Status: PENDING (1-3 business days)
[Line 183] Checkout completed successfully!

--- Demo 5: Error Handling ---
[Line 147] Added "Test Item" ($10.00) to cart
[Line 252] Attempting checkout without setting payment strategy...
[Line 169] Error: No payment strategy selected!

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Key Implementation Details

#### Strategy Interface (Lines 10-14)
- `PaymentStrategy` defines the contract that all payment methods must implement
- Three methods: `pay()`, `getName()`, and `getTransactionFee()`
- This interface enables polymorphism - the context can use any strategy interchangeably

#### Concrete Strategies (Lines 17-149)
Each payment strategy implements the interface differently:

| Strategy | Class | Fee Calculation | Lines |
|----------|-------|-----------------|-------|
| Credit Card | `CreditCardPayment` | 2.9% of amount | 17-50 |
| PayPal | `PayPalPayment` | 3.49% + $0.49 flat | 53-80 |
| Cryptocurrency | `CryptoPayment` | 1% network fee | 83-113 |
| Bank Transfer | `BankTransferPayment` | $0.25 flat fee | 116-149 |

#### Context Class (Lines 152-214)
- `ShoppingCart` is the context that uses the payment strategy
- It maintains a reference to a `PaymentStrategy` (Line 154)
- `setPaymentStrategy()` allows changing the algorithm at runtime (Lines 161-164)
- `checkout()` delegates the payment to the current strategy (Lines 179-200)
- `comparePaymentMethods()` demonstrates strategy comparison (Lines 202-213)

### Output Correlation

| Output Line | Source Line | Explanation |
|-------------|-------------|-------------|
| `[Line 147] Added "Mechanical Keyboard"...` | Line 225 | Items added via `addItem()` method |
| `[Line 24] CreditCardPayment initialized...` | Line 232 | Constructor creates concrete strategy |
| `[Line 54] PayPalPayment initialized...` | Line 233 | Different strategy with different initialization |
| `[Line 191] Fee comparison...` | Line 238 | Context uses all strategies to compare fees |
| `[Line 197] Credit Card... $8.12... $288.09` | Lines 208-211 | Each strategy calculates its own fee |
| `[Line 152] Payment strategy set to: Credit Card` | Line 245 | Runtime strategy selection |
| `[Line 179] Starting checkout with Credit Card...` | Line 246 | Context delegates to strategy |
| `[Line 31-37] Processing Credit Card payment...` | Line 246 | Credit card's specific `pay()` implementation |
| `[Line 60-65] Processing PayPal payment...` | Line 253 | PayPal's different `pay()` implementation |
| `[Line 90-95] Processing BTC payment...` | Line 259 | Crypto's unique payment flow |
| `[Line 244] Switching from Crypto to Bank Transfer...` | Line 267 | Dynamic strategy change at runtime |
| `[Line 169] Error: No payment strategy selected!` | Line 275 | Validation when no strategy is set |

### Why Strategy Pattern Works

1. **Open/Closed Principle**: New payment methods can be added without modifying existing code - just create a new class implementing `PaymentStrategy`

2. **Single Responsibility**: Each strategy class handles only its own payment logic

3. **Runtime Flexibility**: The cart can switch between payment methods dynamically (Demo 4 shows switching from Crypto to Bank Transfer)

4. **Fee Comparison**: Different algorithms can be compared side-by-side (see fee comparison table in output)

5. **Encapsulation**: Implementation details (card numbers, wallet addresses) are hidden within each strategy

### Strategy Pattern vs. Other Patterns

| Aspect | Strategy | State | Template Method |
|--------|----------|-------|-----------------|
| Intent | Interchangeable algorithms | State-dependent behavior | Algorithm skeleton |
| Changed by | Client explicitly | Internal state changes | Subclass overrides |
| Focus | Family of algorithms | Object state transitions | Step customization |

### Use Cases for Strategy Pattern

- **Payment Processing**: Different payment gateways (as demonstrated)
- **Sorting Algorithms**: QuickSort, MergeSort, HeapSort
- **Compression**: ZIP, GZIP, RAR
- **Validation**: Different validation rules for form fields
- **Authentication**: OAuth, JWT, API Keys
- **Shipping Calculation**: Standard, Express, Overnight rates
- **Discount Strategies**: Percentage off, fixed amount, buy-one-get-one
