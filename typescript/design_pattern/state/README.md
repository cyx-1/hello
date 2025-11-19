# State Design Pattern in TypeScript

The State pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class. This pattern encapsulates state-specific behavior into separate state classes, making the code more maintainable and adhering to the Open/Closed Principle.

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
2    * State Design Pattern in TypeScript
3    *
4    * The State pattern allows an object to alter its behavior when its internal
5    * state changes. The object will appear to change its class. This pattern
6    * encapsulates state-specific behavior into separate state classes.
7    */
8
9   // State Interface - defines the common interface for all concrete states
10  interface VendingMachineState {
11      insertMoney(amount: number): void;
12      selectProduct(product: string): void;
13      dispense(): void;
14      refund(): void;
15      getName(): string;
16  }
17
18  // Context - maintains an instance of a ConcreteState subclass
19  class VendingMachine {
20      private state: VendingMachineState;
21      private balance: number = 0;
22      private selectedProduct: string = "";
23      private inventory: Map<string, { price: number; quantity: number }>;
24
25      // States
26      private idleState: VendingMachineState;
27      private hasMoneyState: VendingMachineState;
28      private productSelectedState: VendingMachineState;
29      private dispensingState: VendingMachineState;
30      private soldOutState: VendingMachineState;
31
32      constructor() {
33          // Initialize states
34          this.idleState = new IdleState(this);
35          this.hasMoneyState = new HasMoneyState(this);
36          this.productSelectedState = new ProductSelectedState(this);
37          this.dispensingState = new DispensingState(this);
38          this.soldOutState = new SoldOutState(this);
39
40          // Initialize inventory
41          this.inventory = new Map([
42              ["Cola", { price: 150, quantity: 3 }],
43              ["Chips", { price: 100, quantity: 2 }],
44              ["Candy", { price: 75, quantity: 5 }],
45              ["Water", { price: 125, quantity: 0 }]  // Sold out item
46          ]);
47
48          // Start in idle state
49          this.state = this.idleState;
50          console.log("[Line 47] VendingMachine: Initialized in IdleState");
51          console.log("[Line 48] VendingMachine: Inventory loaded with 4 products");
52      }
53
54      // State setters
55      setState(state: VendingMachineState): void {
56          console.log(`[Line 52] VendingMachine: Transitioning from ${this.state.getName()} to ${state.getName()}`);
57          this.state = state;
58      }
59
60      // Getters for states
61      getIdleState(): VendingMachineState { return this.idleState; }
62      getHasMoneyState(): VendingMachineState { return this.hasMoneyState; }
63      getProductSelectedState(): VendingMachineState { return this.productSelectedState; }
64      getDispensingState(): VendingMachineState { return this.dispensingState; }
65      getSoldOutState(): VendingMachineState { return this.soldOutState; }
66
67      // Balance management
68      getBalance(): number { return this.balance; }
69      addBalance(amount: number): void {
70          this.balance += amount;
71          console.log(`[Line 66] VendingMachine: Balance updated to ${this.balance} cents`);
72      }
73      resetBalance(): void {
74          const previousBalance = this.balance;
75          this.balance = 0;
76          console.log(`[Line 70] VendingMachine: Balance reset from ${previousBalance} to 0 cents`);
77      }
78
79      // Product management
80      getSelectedProduct(): string { return this.selectedProduct; }
81      setSelectedProduct(product: string): void {
82          this.selectedProduct = product;
83          console.log(`[Line 77] VendingMachine: Selected product set to "${product}"`);
84      }
85
86      // Inventory management
87      getProductPrice(product: string): number {
88          const item = this.inventory.get(product);
89          return item ? item.price : 0;
90      }
91
92      getProductQuantity(product: string): number {
93          const item = this.inventory.get(product);
94          return item ? item.quantity : 0;
95      }
96
97      hasProduct(product: string): boolean {
98          return this.inventory.has(product);
99      }
100
101     decrementProduct(product: string): void {
102         const item = this.inventory.get(product);
103         if (item && item.quantity > 0) {
104             item.quantity--;
105             console.log(`[Line 98] VendingMachine: ${product} quantity decreased to ${item.quantity}`);
106         }
107     }
108
109     // Delegated methods to current state
110     insertMoney(amount: number): void {
111         console.log(`\n[Line 104] VendingMachine: insertMoney(${amount}) called in ${this.state.getName()}`);
112         this.state.insertMoney(amount);
113     }
114
115     selectProduct(product: string): void {
116         console.log(`\n[Line 109] VendingMachine: selectProduct("${product}") called in ${this.state.getName()}`);
117         this.state.selectProduct(product);
118     }
119
120     dispense(): void {
121         console.log(`\n[Line 114] VendingMachine: dispense() called in ${this.state.getName()}`);
122         this.state.dispense();
123     }
124
125     refund(): void {
126         console.log(`\n[Line 119] VendingMachine: refund() called in ${this.state.getName()}`);
127         this.state.refund();
128     }
129
130     // Display current state
131     displayStatus(): void {
132         console.log(`\n[Line 125] --- Machine Status ---`);
133         console.log(`[Line 126] Current State: ${this.state.getName()}`);
134         console.log(`[Line 127] Balance: ${this.balance} cents`);
135         console.log(`[Line 128] Selected Product: ${this.selectedProduct || "None"}`);
136     }
137 }
138
139 // Concrete State 1: Idle State
140 class IdleState implements VendingMachineState {
141     private machine: VendingMachine;
142
143     constructor(machine: VendingMachine) {
144         this.machine = machine;
145     }
146
147     getName(): string { return "IdleState"; }
148
149     insertMoney(amount: number): void {
150         console.log(`[Line 142] IdleState: Accepting ${amount} cents`);
151         this.machine.addBalance(amount);
152         this.machine.setState(this.machine.getHasMoneyState());
153     }
154
155     selectProduct(product: string): void {
156         console.log(`[Line 148] IdleState: Cannot select product - please insert money first`);
157     }
158
159     dispense(): void {
160         console.log(`[Line 152] IdleState: Cannot dispense - please insert money and select a product`);
161     }
162
163     refund(): void {
164         console.log(`[Line 156] IdleState: No money to refund`);
165     }
166 }
167
168 // Concrete State 2: Has Money State
169 class HasMoneyState implements VendingMachineState {
170     private machine: VendingMachine;
171
172     constructor(machine: VendingMachine) {
173         this.machine = machine;
174     }
175
176     getName(): string { return "HasMoneyState"; }
177
178     insertMoney(amount: number): void {
179         console.log(`[Line 171] HasMoneyState: Adding ${amount} cents to existing balance`);
180         this.machine.addBalance(amount);
181     }
182
183     selectProduct(product: string): void {
184         console.log(`[Line 176] HasMoneyState: Processing product selection "${product}"`);
185
186         if (!this.machine.hasProduct(product)) {
187             console.log(`[Line 179] HasMoneyState: Product "${product}" not found in inventory`);
188             return;
189         }
190
191         const quantity = this.machine.getProductQuantity(product);
192         if (quantity === 0) {
193             console.log(`[Line 185] HasMoneyState: "${product}" is sold out`);
194             this.machine.setState(this.machine.getSoldOutState());
195             return;
196         }
197
198         const price = this.machine.getProductPrice(product);
199         const balance = this.machine.getBalance();
200
201         console.log(`[Line 193] HasMoneyState: ${product} costs ${price} cents, balance is ${balance} cents`);
202
203         if (balance >= price) {
204             console.log(`[Line 196] HasMoneyState: Sufficient balance - proceeding to selection`);
205             this.machine.setSelectedProduct(product);
206             this.machine.setState(this.machine.getProductSelectedState());
207         } else {
208             console.log(`[Line 200] HasMoneyState: Insufficient balance - need ${price - balance} more cents`);
209         }
210     }
211
212     dispense(): void {
213         console.log(`[Line 205] HasMoneyState: Cannot dispense - please select a product first`);
214     }
215
216     refund(): void {
217         const balance = this.machine.getBalance();
218         console.log(`[Line 210] HasMoneyState: Refunding ${balance} cents`);
219         this.machine.resetBalance();
220         this.machine.setState(this.machine.getIdleState());
221     }
222 }
223
224 // Concrete State 3: Product Selected State
225 class ProductSelectedState implements VendingMachineState {
226     private machine: VendingMachine;
227
228     constructor(machine: VendingMachine) {
229         this.machine = machine;
230     }
231
232     getName(): string { return "ProductSelectedState"; }
233
234     insertMoney(amount: number): void {
235         console.log(`[Line 227] ProductSelectedState: Cannot accept money - product already selected`);
236     }
237
238     selectProduct(product: string): void {
239         console.log(`[Line 231] ProductSelectedState: Cannot change selection - please dispense or refund first`);
240     }
241
242     dispense(): void {
243         const product = this.machine.getSelectedProduct();
244         const price = this.machine.getProductPrice(product);
245
246         console.log(`[Line 238] ProductSelectedState: Dispensing ${product}...`);
247         this.machine.setState(this.machine.getDispensingState());
248
249         // Perform the dispensing action
250         this.machine.dispense();
251     }
252
253     refund(): void {
254         const balance = this.machine.getBalance();
255         console.log(`[Line 247] ProductSelectedState: Canceling transaction, refunding ${balance} cents`);
256         this.machine.setSelectedProduct("");
257         this.machine.resetBalance();
258         this.machine.setState(this.machine.getIdleState());
259     }
260 }
261
262 // Concrete State 4: Dispensing State
263 class DispensingState implements VendingMachineState {
264     private machine: VendingMachine;
265
266     constructor(machine: VendingMachine) {
267         this.machine = machine;
268     }
269
270     getName(): string { return "DispensingState"; }
271
272     insertMoney(amount: number): void {
273         console.log(`[Line 265] DispensingState: Please wait - dispensing in progress`);
274     }
275
276     selectProduct(product: string): void {
277         console.log(`[Line 269] DispensingState: Please wait - dispensing in progress`);
278     }
279
280     dispense(): void {
281         const product = this.machine.getSelectedProduct();
282         const price = this.machine.getProductPrice(product);
283         const balance = this.machine.getBalance();
284
285         console.log(`[Line 277] DispensingState: **** ${product} dispensed! ****`);
286
287         // Update inventory and balance
288         this.machine.decrementProduct(product);
289
290         // Calculate and return change
291         const change = balance - price;
292         if (change > 0) {
293             console.log(`[Line 285] DispensingState: Returning ${change} cents in change`);
294         } else {
295             console.log(`[Line 287] DispensingState: No change to return`);
296         }
297
298         // Reset machine
299         this.machine.resetBalance();
300         this.machine.setSelectedProduct("");
301         this.machine.setState(this.machine.getIdleState());
302
303         console.log(`[Line 295] DispensingState: Transaction complete`);
304     }
305
306     refund(): void {
307         console.log(`[Line 299] DispensingState: Cannot refund - dispensing in progress`);
308     }
309 }
310
311 // Concrete State 5: Sold Out State
312 class SoldOutState implements VendingMachineState {
313     private machine: VendingMachine;
314
315     constructor(machine: VendingMachine) {
316         this.machine = machine;
317     }
318
319     getName(): string { return "SoldOutState"; }
320
321     insertMoney(amount: number): void {
322         console.log(`[Line 314] SoldOutState: Cannot accept money - please select a different product`);
323     }
324
325     selectProduct(product: string): void {
326         console.log(`[Line 318] SoldOutState: Returning to HasMoneyState to try another product`);
327         this.machine.setState(this.machine.getHasMoneyState());
328         this.machine.selectProduct(product);
329     }
330
331     dispense(): void {
332         console.log(`[Line 324] SoldOutState: Cannot dispense - product is sold out`);
333     }
334
335     refund(): void {
336         const balance = this.machine.getBalance();
337         console.log(`[Line 329] SoldOutState: Refunding ${balance} cents due to sold out product`);
338         this.machine.resetBalance();
339         this.machine.setState(this.machine.getIdleState());
340     }
341 }
```

## Program Output

```
=== State Pattern Demonstration - Vending Machine ===

[Line 47] VendingMachine: Initialized in IdleState
[Line 48] VendingMachine: Inventory loaded with 4 products


--- Demo 1: Successful Purchase ---

[Line 104] VendingMachine: insertMoney(100) called in IdleState
[Line 142] IdleState: Accepting 100 cents
[Line 66] VendingMachine: Balance updated to 100 cents
[Line 52] VendingMachine: Transitioning from IdleState to HasMoneyState

[Line 104] VendingMachine: insertMoney(100) called in HasMoneyState
[Line 171] HasMoneyState: Adding 100 cents to existing balance
[Line 66] VendingMachine: Balance updated to 200 cents

[Line 109] VendingMachine: selectProduct("Cola") called in HasMoneyState
[Line 176] HasMoneyState: Processing product selection "Cola"
[Line 193] HasMoneyState: Cola costs 150 cents, balance is 200 cents
[Line 196] HasMoneyState: Sufficient balance - proceeding to selection
[Line 77] VendingMachine: Selected product set to "Cola"
[Line 52] VendingMachine: Transitioning from HasMoneyState to ProductSelectedState

[Line 114] VendingMachine: dispense() called in ProductSelectedState
[Line 238] ProductSelectedState: Dispensing Cola...
[Line 52] VendingMachine: Transitioning from ProductSelectedState to DispensingState

[Line 114] VendingMachine: dispense() called in DispensingState
[Line 277] DispensingState: **** Cola dispensed! ****
[Line 98] VendingMachine: Cola quantity decreased to 2
[Line 285] DispensingState: Returning 50 cents in change
[Line 70] VendingMachine: Balance reset from 200 to 0 cents
[Line 77] VendingMachine: Selected product set to ""
[Line 52] VendingMachine: Transitioning from DispensingState to IdleState
[Line 295] DispensingState: Transaction complete


--- Demo 2: Invalid Operations ---

[Line 109] VendingMachine: selectProduct("Chips") called in IdleState
[Line 148] IdleState: Cannot select product - please insert money first

[Line 114] VendingMachine: dispense() called in IdleState
[Line 152] IdleState: Cannot dispense - please insert money and select a product

[Line 119] VendingMachine: refund() called in IdleState
[Line 156] IdleState: No money to refund


--- Demo 3: Insufficient Balance ---

[Line 104] VendingMachine: insertMoney(50) called in IdleState
[Line 142] IdleState: Accepting 50 cents
[Line 66] VendingMachine: Balance updated to 50 cents
[Line 52] VendingMachine: Transitioning from IdleState to HasMoneyState

[Line 109] VendingMachine: selectProduct("Candy") called in HasMoneyState
[Line 176] HasMoneyState: Processing product selection "Candy"
[Line 193] HasMoneyState: Candy costs 75 cents, balance is 50 cents
[Line 200] HasMoneyState: Insufficient balance - need 25 more cents

[Line 104] VendingMachine: insertMoney(25) called in HasMoneyState
[Line 171] HasMoneyState: Adding 25 cents to existing balance
[Line 66] VendingMachine: Balance updated to 75 cents

[Line 109] VendingMachine: selectProduct("Candy") called in HasMoneyState
[Line 176] HasMoneyState: Processing product selection "Candy"
[Line 193] HasMoneyState: Candy costs 75 cents, balance is 75 cents
[Line 196] HasMoneyState: Sufficient balance - proceeding to selection
[Line 77] VendingMachine: Selected product set to "Candy"
[Line 52] VendingMachine: Transitioning from HasMoneyState to ProductSelectedState

[Line 114] VendingMachine: dispense() called in ProductSelectedState
[Line 238] ProductSelectedState: Dispensing Candy...
[Line 52] VendingMachine: Transitioning from ProductSelectedState to DispensingState

[Line 114] VendingMachine: dispense() called in DispensingState
[Line 277] DispensingState: **** Candy dispensed! ****
[Line 98] VendingMachine: Candy quantity decreased to 4
[Line 287] DispensingState: No change to return
[Line 70] VendingMachine: Balance reset from 75 to 0 cents
[Line 77] VendingMachine: Selected product set to ""
[Line 52] VendingMachine: Transitioning from DispensingState to IdleState
[Line 295] DispensingState: Transaction complete


--- Demo 4: Sold Out Product ---

[Line 104] VendingMachine: insertMoney(200) called in IdleState
[Line 142] IdleState: Accepting 200 cents
[Line 66] VendingMachine: Balance updated to 200 cents
[Line 52] VendingMachine: Transitioning from IdleState to HasMoneyState

[Line 109] VendingMachine: selectProduct("Water") called in HasMoneyState
[Line 176] HasMoneyState: Processing product selection "Water"
[Line 185] HasMoneyState: "Water" is sold out
[Line 52] VendingMachine: Transitioning from HasMoneyState to SoldOutState

[Line 109] VendingMachine: selectProduct("Chips") called in SoldOutState
[Line 318] SoldOutState: Returning to HasMoneyState to try another product
[Line 52] VendingMachine: Transitioning from SoldOutState to HasMoneyState

[Line 109] VendingMachine: selectProduct("Chips") called in HasMoneyState
[Line 176] HasMoneyState: Processing product selection "Chips"
[Line 193] HasMoneyState: Chips costs 100 cents, balance is 200 cents
[Line 196] HasMoneyState: Sufficient balance - proceeding to selection
[Line 77] VendingMachine: Selected product set to "Chips"
[Line 52] VendingMachine: Transitioning from HasMoneyState to ProductSelectedState

[Line 114] VendingMachine: dispense() called in ProductSelectedState
[Line 238] ProductSelectedState: Dispensing Chips...
[Line 52] VendingMachine: Transitioning from ProductSelectedState to DispensingState

[Line 114] VendingMachine: dispense() called in DispensingState
[Line 277] DispensingState: **** Chips dispensed! ****
[Line 98] VendingMachine: Chips quantity decreased to 1
[Line 285] DispensingState: Returning 100 cents in change
[Line 70] VendingMachine: Balance reset from 200 to 0 cents
[Line 77] VendingMachine: Selected product set to ""
[Line 52] VendingMachine: Transitioning from DispensingState to IdleState
[Line 295] DispensingState: Transaction complete


--- Demo 5: Refund Operations ---

[Line 104] VendingMachine: insertMoney(150) called in IdleState
[Line 142] IdleState: Accepting 150 cents
[Line 66] VendingMachine: Balance updated to 150 cents
[Line 52] VendingMachine: Transitioning from IdleState to HasMoneyState

[Line 125] --- Machine Status ---
[Line 126] Current State: HasMoneyState
[Line 127] Balance: 150 cents
[Line 128] Selected Product: None

[Line 119] VendingMachine: refund() called in HasMoneyState
[Line 210] HasMoneyState: Refunding 150 cents
[Line 70] VendingMachine: Balance reset from 150 to 0 cents
[Line 52] VendingMachine: Transitioning from HasMoneyState to IdleState


--- Demo 6: Cancel After Selection ---

[Line 104] VendingMachine: insertMoney(200) called in IdleState
[Line 142] IdleState: Accepting 200 cents
[Line 66] VendingMachine: Balance updated to 200 cents
[Line 52] VendingMachine: Transitioning from IdleState to HasMoneyState

[Line 109] VendingMachine: selectProduct("Chips") called in HasMoneyState
[Line 176] HasMoneyState: Processing product selection "Chips"
[Line 193] HasMoneyState: Chips costs 100 cents, balance is 200 cents
[Line 196] HasMoneyState: Sufficient balance - proceeding to selection
[Line 77] VendingMachine: Selected product set to "Chips"
[Line 52] VendingMachine: Transitioning from HasMoneyState to ProductSelectedState

[Line 125] --- Machine Status ---
[Line 126] Current State: ProductSelectedState
[Line 127] Balance: 200 cents
[Line 128] Selected Product: Chips

[Line 119] VendingMachine: refund() called in ProductSelectedState
[Line 247] ProductSelectedState: Canceling transaction, refunding 200 cents
[Line 77] VendingMachine: Selected product set to ""
[Line 70] VendingMachine: Balance reset from 200 to 0 cents
[Line 52] VendingMachine: Transitioning from ProductSelectedState to IdleState


--- Demo 7: Multiple Purchases ---

[Line 383] === Purchase 1 ===

[Line 104] VendingMachine: insertMoney(100) called in IdleState
[Line 142] IdleState: Accepting 100 cents
[Line 66] VendingMachine: Balance updated to 100 cents
[Line 52] VendingMachine: Transitioning from IdleState to HasMoneyState

[Line 109] VendingMachine: selectProduct("Candy") called in HasMoneyState
[Line 176] HasMoneyState: Processing product selection "Candy"
[Line 193] HasMoneyState: Candy costs 75 cents, balance is 100 cents
[Line 196] HasMoneyState: Sufficient balance - proceeding to selection
[Line 77] VendingMachine: Selected product set to "Candy"
[Line 52] VendingMachine: Transitioning from HasMoneyState to ProductSelectedState

[Line 114] VendingMachine: dispense() called in ProductSelectedState
[Line 238] ProductSelectedState: Dispensing Candy...
[Line 52] VendingMachine: Transitioning from ProductSelectedState to DispensingState

[Line 114] VendingMachine: dispense() called in DispensingState
[Line 277] DispensingState: **** Candy dispensed! ****
[Line 98] VendingMachine: Candy quantity decreased to 3
[Line 285] DispensingState: Returning 25 cents in change
[Line 70] VendingMachine: Balance reset from 100 to 0 cents
[Line 77] VendingMachine: Selected product set to ""
[Line 52] VendingMachine: Transitioning from DispensingState to IdleState
[Line 295] DispensingState: Transaction complete

[Line 383] === Purchase 2 ===

[Line 104] VendingMachine: insertMoney(100) called in IdleState
[Line 142] IdleState: Accepting 100 cents
[Line 66] VendingMachine: Balance updated to 100 cents
[Line 52] VendingMachine: Transitioning from IdleState to HasMoneyState

[Line 109] VendingMachine: selectProduct("Candy") called in HasMoneyState
[Line 176] HasMoneyState: Processing product selection "Candy"
[Line 193] HasMoneyState: Candy costs 75 cents, balance is 100 cents
[Line 196] HasMoneyState: Sufficient balance - proceeding to selection
[Line 77] VendingMachine: Selected product set to "Candy"
[Line 52] VendingMachine: Transitioning from HasMoneyState to ProductSelectedState

[Line 114] VendingMachine: dispense() called in ProductSelectedState
[Line 238] ProductSelectedState: Dispensing Candy...
[Line 52] VendingMachine: Transitioning from ProductSelectedState to DispensingState

[Line 114] VendingMachine: dispense() called in DispensingState
[Line 277] DispensingState: **** Candy dispensed! ****
[Line 98] VendingMachine: Candy quantity decreased to 2
[Line 285] DispensingState: Returning 25 cents in change
[Line 70] VendingMachine: Balance reset from 100 to 0 cents
[Line 77] VendingMachine: Selected product set to ""
[Line 52] VendingMachine: Transitioning from DispensingState to IdleState
[Line 295] DispensingState: Transaction complete

[Line 125] --- Machine Status ---
[Line 126] Current State: IdleState
[Line 127] Balance: 0 cents
[Line 128] Selected Product: None


=== End of Demonstration ===
```

## Code Analysis and Annotations

### Pattern Components

#### State Interface (Lines 10-16)
- Defines the common interface for all concrete states
- All states must implement: `insertMoney()`, `selectProduct()`, `dispense()`, `refund()`, and `getName()`
- Ensures consistent behavior across all state transitions

#### Context - VendingMachine (Lines 19-137)
- Maintains the current state and delegates behavior to it
- Stores shared data: balance, selected product, and inventory
- Provides state transition method `setState()` (Line 55)
- Contains getters for all states to enable transitions

#### Concrete States (Lines 139-341)
- **IdleState**: Machine waiting for money insertion
- **HasMoneyState**: Money inserted, waiting for product selection
- **ProductSelectedState**: Product selected, ready to dispense
- **DispensingState**: Actively dispensing product
- **SoldOutState**: Selected product is out of stock

### State Transition Diagram

```
                    insertMoney()
    [IdleState] ────────────────────> [HasMoneyState]
         ^                                   │
         │                                   │ selectProduct()
         │                                   │ (sufficient balance)
         │                                   v
         │                           [ProductSelectedState]
         │                                   │
         │                                   │ dispense()
         │                                   v
         │                           [DispensingState]
         │                                   │
         └───────────────────────────────────┘
              (transaction complete)

    [HasMoneyState] ──selectProduct()--> [SoldOutState]
                     (quantity = 0)            │
                                              │ selectProduct()
                                              v
                                       [HasMoneyState]
```

### Output Correlation Tables

#### Demo 1: Successful Purchase Flow

| Output Message | Source Line | Explanation |
|----------------|-------------|-------------|
| `IdleState: Accepting 100 cents` | Line 150 | First money insertion transitions to HasMoneyState |
| `Transitioning from IdleState to HasMoneyState` | Line 56 | State transition is logged |
| `HasMoneyState: Adding 100 cents to existing balance` | Line 179 | Second insertion stays in same state |
| `Cola costs 150 cents, balance is 200 cents` | Line 201 | Price check before selection |
| `Sufficient balance - proceeding to selection` | Line 204 | Balance check passes |
| `Transitioning from HasMoneyState to ProductSelectedState` | Line 56 | Ready to dispense |
| `ProductSelectedState: Dispensing Cola...` | Line 246 | Initiates dispensing |
| `**** Cola dispensed! ****` | Line 285 | Product delivered |
| `Returning 50 cents in change` | Line 293 | Change returned (200 - 150 = 50) |
| `Transaction complete` | Line 303 | Returns to IdleState |

#### Demo 2: Invalid Operations

| Output Message | Source Line | Explanation |
|----------------|-------------|-------------|
| `Cannot select product - please insert money first` | Line 156 | IdleState rejects product selection |
| `Cannot dispense - please insert money and select a product` | Line 160 | IdleState rejects dispense |
| `No money to refund` | Line 164 | IdleState handles refund with no balance |

#### Demo 3: Insufficient Balance

| Output Message | Source Line | Explanation |
|----------------|-------------|-------------|
| `Candy costs 75 cents, balance is 50 cents` | Line 201 | Balance check shows shortage |
| `Insufficient balance - need 25 more cents` | Line 208 | User informed of shortage |
| `Adding 25 cents to existing balance` | Line 179 | Additional money accepted |
| `No change to return` | Line 295 | Exact payment (75 - 75 = 0) |

#### Demo 4: Sold Out Handling

| Output Message | Source Line | Explanation |
|----------------|-------------|-------------|
| `"Water" is sold out` | Line 193 | Inventory check fails |
| `Transitioning from HasMoneyState to SoldOutState` | Line 56 | Special sold out state |
| `Returning to HasMoneyState to try another product` | Line 326 | SoldOutState allows retry |
| `Chips costs 100 cents, balance is 200 cents` | Line 201 | New product selected |
| `Returning 100 cents in change` | Line 293 | Change returned (200 - 100 = 100) |

### Key Behaviors by State

| State | insertMoney | selectProduct | dispense | refund |
|-------|-------------|---------------|----------|--------|
| IdleState | Accept, transition to HasMoneyState | Reject | Reject | No money to refund |
| HasMoneyState | Add to balance | Check inventory/balance, transition if valid | Reject | Refund and return to Idle |
| ProductSelectedState | Reject | Reject | Transition to Dispensing | Cancel and refund |
| DispensingState | Wait message | Wait message | Complete transaction | Cannot refund |
| SoldOutState | Reject | Transition to HasMoneyState and retry | Reject | Refund |

### Why the State Pattern Works Here

1. **Encapsulation of State-Specific Behavior** (Lines 139-341)
   - Each state class handles only its own logic
   - No complex if-else chains to determine current state
   - Adding new states doesn't affect existing code

2. **Clean State Transitions** (Line 55-57)
   - Transitions are explicit and logged
   - States control their own transitions
   - Easy to trace state flow in output

3. **Consistent Interface** (Lines 10-16)
   - All states implement the same interface
   - VendingMachine delegates to current state
   - Client code doesn't know which state is active

4. **Open/Closed Principle**
   - Easy to add new states (e.g., MaintenanceState, OutOfServiceState)
   - Existing states don't need modification
   - Each state is self-contained

### Use Cases for State Pattern

- **Vending Machines**: Multiple states based on money and selection
- **Document Workflows**: Draft, Review, Approved, Published states
- **TCP Connections**: Listen, Established, Closed states
- **Game Characters**: Idle, Walking, Running, Jumping states
- **Order Processing**: Pending, Processing, Shipped, Delivered states
- **Traffic Lights**: Red, Yellow, Green states
