# Strategy Design Pattern in Rust

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from the clients that use it. This implementation demonstrates the pattern using a payment processing example where different payment methods (Credit Card, PayPal, Bitcoin) can be swapped at runtime.

## Source Code

```rust
  1  // Strategy Design Pattern in Rust
  2  // Demonstrates runtime algorithm selection using traits
  3
  4  // Strategy trait defining the payment interface
  5  trait PaymentStrategy {
  6      fn pay(&self, amount: f64) -> String;
  7      fn name(&self) -> &str;
  8  }
  9
 10  // Concrete Strategy: Credit Card Payment
 11  struct CreditCardPayment {
 12      card_number: String,
 13      card_holder: String,
 14  }
 15
 16  impl CreditCardPayment {
 17      fn new(card_number: &str, card_holder: &str) -> Self {
 18          CreditCardPayment {
 19              card_number: card_number.to_string(),
 20              card_holder: card_holder.to_string(),
 21          }
 22      }
 23  }
 24
 25  impl PaymentStrategy for CreditCardPayment {
 26      fn pay(&self, amount: f64) -> String {
 27          format!(
 28              "Paid ${:.2} using Credit Card ending in {} (Holder: {})",
 29              amount,
 30              &self.card_number[self.card_number.len() - 4..],
 31              self.card_holder
 32          )
 33      }
 34
 35      fn name(&self) -> &str {
 36          "Credit Card"
 37      }
 38  }
 39
 40  // Concrete Strategy: PayPal Payment
 41  struct PayPalPayment {
 42      email: String,
 43  }
 44
 45  impl PayPalPayment {
 46      fn new(email: &str) -> Self {
 47          PayPalPayment {
 48              email: email.to_string(),
 49          }
 50      }
 51  }
 52
 53  impl PaymentStrategy for PayPalPayment {
 54      fn pay(&self, amount: f64) -> String {
 55          format!("Paid ${:.2} using PayPal account: {}", amount, self.email)
 56      }
 57
 58      fn name(&self) -> &str {
 59          "PayPal"
 60      }
 61  }
 62
 63  // Concrete Strategy: Bitcoin Payment
 64  struct BitcoinPayment {
 65      wallet_address: String,
 66  }
 67
 68  impl BitcoinPayment {
 69      fn new(wallet_address: &str) -> Self {
 70          BitcoinPayment {
 71              wallet_address: wallet_address.to_string(),
 72          }
 73      }
 74  }
 75
 76  impl PaymentStrategy for BitcoinPayment {
 77      fn pay(&self, amount: f64) -> String {
 78          format!(
 79              "Paid ${:.2} in Bitcoin to wallet: {}...{}",
 80              amount,
 81              &self.wallet_address[..6],
 82              &self.wallet_address[self.wallet_address.len() - 4..]
 83          )
 84      }
 85
 86      fn name(&self) -> &str {
 87          "Bitcoin"
 88      }
 89  }
 90
 91  // Context: Shopping Cart that uses payment strategies
 92  struct ShoppingCart {
 93      items: Vec<(String, f64)>,
 94      payment_strategy: Box<dyn PaymentStrategy>,
 95  }
 96
 97  impl ShoppingCart {
 98      fn new(strategy: Box<dyn PaymentStrategy>) -> Self {
 99          println!("=== Shopping Cart Created ===");
100          println!("Initial payment method: {}", strategy.name());
101          ShoppingCart {
102              items: Vec::new(),
103              payment_strategy: strategy,
104          }
105      }
106
107      fn add_item(&mut self, name: &str, price: f64) {
108          println!("Added item: {} - ${:.2}", name, price);
109          self.items.push((name.to_string(), price));
110      }
111
112      fn set_payment_strategy(&mut self, strategy: Box<dyn PaymentStrategy>) {
113          println!("\n--- Switching Payment Strategy ---");
114          println!("From: {} -> To: {}", self.payment_strategy.name(), strategy.name());
115          self.payment_strategy = strategy;
116      }
117
118      fn calculate_total(&self) -> f64 {
119          self.items.iter().map(|(_, price)| price).sum()
120      }
121
122      fn checkout(&self) {
123          let total = self.calculate_total();
124          println!("\n=== Checkout ===");
125          println!("Items in cart: {}", self.items.len());
126          println!("Total amount: ${:.2}", total);
127          let result = self.payment_strategy.pay(total);
128          println!("Payment result: {}", result);
129          println!("Checkout complete!\n");
130      }
131  }
132
133  fn main() {
134      println!("========================================");
135      println!("  Strategy Pattern - Payment Example");
136      println!("========================================\n");
137
138      // Create cart with Credit Card strategy
139      let credit_card = CreditCardPayment::new("4532015112830366", "John Doe");
140      let mut cart = ShoppingCart::new(Box::new(credit_card));
141
142      // Add items to cart
143      println!("\n--- Adding Items ---");
144      cart.add_item("Laptop", 999.99);
145      cart.add_item("Mouse", 29.99);
146      cart.add_item("Keyboard", 79.99);
147
148      // Checkout with Credit Card
149      cart.checkout();
150
151      // Switch to PayPal strategy
152      let paypal = PayPalPayment::new("john.doe@email.com");
153      cart.set_payment_strategy(Box::new(paypal));
154
155      // Add more items
156      println!("\n--- Adding More Items ---");
157      cart.add_item("Monitor", 349.99);
158      cart.add_item("USB Hub", 24.99);
159
160      // Checkout with PayPal
161      cart.checkout();
162
163      // Switch to Bitcoin strategy
164      let bitcoin = BitcoinPayment::new("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa");
165      cart.set_payment_strategy(Box::new(bitcoin));
166
167      // Add final item
168      println!("\n--- Adding Final Item ---");
169      cart.add_item("Graphics Card", 599.99);
170
171      // Checkout with Bitcoin
172      cart.checkout();
173
174      println!("========================================");
175      println!("  Strategy Pattern Demo Complete!");
176      println!("========================================");
177  }
```

## Program Output

```
========================================
  Strategy Pattern - Payment Example
========================================

=== Shopping Cart Created ===
Initial payment method: Credit Card

--- Adding Items ---
Added item: Laptop - $999.99
Added item: Mouse - $29.99
Added item: Keyboard - $79.99

=== Checkout ===
Items in cart: 3
Total amount: $1109.97
Payment result: Paid $1109.97 using Credit Card ending in 0366 (Holder: John Doe)
Checkout complete!


--- Switching Payment Strategy ---
From: Credit Card -> To: PayPal

--- Adding More Items ---
Added item: Monitor - $349.99
Added item: USB Hub - $24.99

=== Checkout ===
Items in cart: 5
Total amount: $1484.95
Payment result: Paid $1484.95 using PayPal account: john.doe@email.com
Checkout complete!


--- Switching Payment Strategy ---
From: PayPal -> To: Bitcoin

--- Adding Final Item ---
Added item: Graphics Card - $599.99

=== Checkout ===
Items in cart: 6
Total amount: $2084.94
Payment result: Paid $2084.94 in Bitcoin to wallet: 1A1zP1...vfNa
Checkout complete!

========================================
  Strategy Pattern Demo Complete!
========================================
```

## Code Annotations

### Key Sections Explained

#### Strategy Trait (Lines 5-8)
The `PaymentStrategy` trait defines the interface that all concrete strategies must implement. It includes:
- `pay(&self, amount: f64) -> String`: The core algorithm that processes payment
- `name(&self) -> &str`: Helper method to identify the strategy

#### Concrete Strategies (Lines 10-89)
Three concrete payment strategies implement the trait:

1. **CreditCardPayment (Lines 10-38)**: Processes credit card payments, masking the card number for security
2. **PayPalPayment (Lines 40-61)**: Handles PayPal payments using email identification
3. **BitcoinPayment (Lines 63-89)**: Manages cryptocurrency payments with wallet address truncation

#### Context Class (Lines 91-131)
The `ShoppingCart` struct serves as the context that uses strategies:
- **Line 94**: Uses `Box<dyn PaymentStrategy>` for dynamic dispatch (trait object)
- **Lines 97-105**: Constructor accepts any strategy implementing the trait
- **Lines 112-116**: `set_payment_strategy` allows runtime strategy switching
- **Lines 122-130**: `checkout` delegates payment to the current strategy

#### Client Code (Lines 133-177)
Demonstrates strategy switching during runtime without modifying the context class.

### Output to Source Code Correlation

| Output Line | Source Lines | Description |
|-------------|--------------|-------------|
| "Strategy Pattern - Payment Example" | 134-136 | Main function banner |
| "=== Shopping Cart Created ===" | 99 | ShoppingCart::new() initialization |
| "Initial payment method: Credit Card" | 100 | Displays initial strategy name |
| "Added item: Laptop - $999.99" | 108, 144 | add_item() prints and stores item |
| "=== Checkout ===" | 124 | checkout() method header |
| "Items in cart: 3" | 125 | Count of items in vector |
| "Total amount: $1109.97" | 126, 118-120 | calculate_total() sums prices |
| "Payment result: Paid $1109.97 using Credit Card..." | 127-128, 26-32 | CreditCardPayment::pay() execution |
| "--- Switching Payment Strategy ---" | 113 | set_payment_strategy() notification |
| "From: Credit Card -> To: PayPal" | 114 | Shows old and new strategy names |
| "Payment result: Paid $1484.95 using PayPal..." | 127-128, 54-55 | PayPalPayment::pay() execution |
| "Payment result: Paid $2084.94 in Bitcoin..." | 127-128, 77-83 | BitcoinPayment::pay() execution |

### Key Characteristics of Strategy Pattern in Rust

1. **Trait-Based Polymorphism**: Uses Rust traits to define the strategy interface (line 5), providing compile-time safety while allowing runtime flexibility.

2. **Dynamic Dispatch with Box<dyn Trait>**: The context holds `Box<dyn PaymentStrategy>` (line 94), enabling heterogeneous strategy storage and runtime switching.

3. **Ownership Semantics**: Strategies are moved into Box containers, ensuring single ownership and preventing data races.

4. **Zero-Cost Abstractions**: While using dynamic dispatch for flexibility, the pattern could be adapted to use generics for static dispatch when strategy switching isn't needed.

5. **Open/Closed Principle**: New payment methods can be added by implementing `PaymentStrategy` without modifying existing code.

6. **Encapsulation**: Each strategy encapsulates its own algorithm and data (e.g., card numbers, email, wallet addresses).

7. **Runtime Flexibility**: The `set_payment_strategy` method (line 112) allows changing algorithms during execution without conditional statements.

### Compilation

This code compiles with standard rustc without any external dependencies:

```bash
rustc main_strategy.rs -o main_strategy.exe && ./main_strategy.exe
```

No specific Rust version is required beyond Rust 1.0, as it uses only stable language features.
