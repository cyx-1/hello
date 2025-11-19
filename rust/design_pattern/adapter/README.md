# Adapter Pattern in Rust

The Adapter pattern allows incompatible interfaces to work together by wrapping an object with an incompatible interface in an adapter that implements the expected interface.

## Source Code

```rust
  1  //! Adapter Pattern in Rust
  2  //!
  3  //! The Adapter pattern allows incompatible interfaces to work together by
  4  //! wrapping an object with an incompatible interface in an adapter that
  5  //! implements the expected interface.
  6
  7  /// Target interface that the client expects
  8  trait PaymentProcessor {
  9      fn process_payment(&self, amount: f64, currency: &str) -> Result<String, String>;
 10      fn refund(&self, transaction_id: &str) -> Result<String, String>;
 11  }
 12
 13  /// Legacy payment system with incompatible interface
 14  struct LegacyPaymentGateway {
 15      gateway_name: String,
 16  }
 17
 18  impl LegacyPaymentGateway {
 19      fn new(name: &str) -> Self {
 20          println!("  [LegacyGateway] Initializing legacy gateway: {}", name);
 21          LegacyPaymentGateway {
 22              gateway_name: name.to_string(),
 23          }
 24      }
 25
 26      /// Legacy method with different signature - uses cents instead of dollars
 27      fn make_payment(&self, amount_cents: i64, currency_code: i32) -> i32 {
 28          let currency = match currency_code {
 29              1 => "USD",
 30              2 => "EUR",
 31              3 => "GBP",
 32              _ => "UNKNOWN",
 33          };
 34          println!("  [LegacyGateway] Processing {} cents in {} via {}",
 35                   amount_cents, currency, self.gateway_name);
 36          // Returns transaction ID as integer
 37          12345
 38      }
 39
 40      /// Legacy refund method with different return type
 41      fn cancel_transaction(&self, tx_id: i32) -> bool {
 42          println!("  [LegacyGateway] Canceling transaction #{} via {}",
 43                   tx_id, self.gateway_name);
 44          true
 45      }
 46  }
 47
 48  /// Modern third-party payment API with yet another interface
 49  struct ThirdPartyPaymentAPI {
 50      api_key: String,
 51  }
 52
 53  impl ThirdPartyPaymentAPI {
 54      fn new(api_key: &str) -> Self {
 55          println!("  [ThirdPartyAPI] Initializing with API key: {}...", &api_key[..8]);
 56          ThirdPartyPaymentAPI {
 57              api_key: api_key.to_string(),
 58          }
 59      }
 60
 61      /// Third-party method using JSON-like structure
 62      fn execute_transaction(&self, payload: &str) -> String {
 63          println!("  [ThirdPartyAPI] Executing transaction with payload: {}", payload);
 64          format!("TXN-{}-{}", &self.api_key[..4], "ABC123")
 65      }
 66
 67      /// Third-party refund with different naming
 68      fn reverse_transaction(&self, txn_ref: &str) -> String {
 69          println!("  [ThirdPartyAPI] Reversing transaction: {}", txn_ref);
 70          format!("REFUND-{}", txn_ref)
 71      }
 72  }
 73
 74  /// Adapter for LegacyPaymentGateway to implement PaymentProcessor
 75  struct LegacyGatewayAdapter {
 76      legacy_gateway: LegacyPaymentGateway,
 77  }
 78
 79  impl LegacyGatewayAdapter {
 80      fn new(gateway: LegacyPaymentGateway) -> Self {
 81          println!("  [Adapter] Wrapping LegacyPaymentGateway");
 82          LegacyGatewayAdapter {
 83              legacy_gateway: gateway,
 84          }
 85      }
 86
 87      fn currency_to_code(&self, currency: &str) -> i32 {
 88          match currency {
 89              "USD" => 1,
 90              "EUR" => 2,
 91              "GBP" => 3,
 92              _ => 0,
 93          }
 94      }
 95  }
 96
 97  impl PaymentProcessor for LegacyGatewayAdapter {
 98      fn process_payment(&self, amount: f64, currency: &str) -> Result<String, String> {
 99          // Convert dollars to cents
100          let amount_cents = (amount * 100.0) as i64;
101          let currency_code = self.currency_to_code(currency);
102
103          println!("  [Adapter] Converting ${:.2} to {} cents", amount, amount_cents);
104
105          let tx_id = self.legacy_gateway.make_payment(amount_cents, currency_code);
106          Ok(format!("LEGACY-{}", tx_id))
107      }
108
109      fn refund(&self, transaction_id: &str) -> Result<String, String> {
110          // Extract numeric ID from adapted format
111          let tx_id: i32 = transaction_id
112              .replace("LEGACY-", "")
113              .parse()
114              .map_err(|_| "Invalid transaction ID".to_string())?;
115
116          println!("  [Adapter] Converting transaction ID {} to legacy format {}",
117                   transaction_id, tx_id);
118
119          if self.legacy_gateway.cancel_transaction(tx_id) {
120              Ok(format!("Refund successful for {}", transaction_id))
121          } else {
122              Err("Refund failed".to_string())
123          }
124      }
125  }
126
127  /// Adapter for ThirdPartyPaymentAPI to implement PaymentProcessor
128  struct ThirdPartyAPIAdapter {
129      api: ThirdPartyPaymentAPI,
130  }
131
132  impl ThirdPartyAPIAdapter {
133      fn new(api: ThirdPartyPaymentAPI) -> Self {
134          println!("  [Adapter] Wrapping ThirdPartyPaymentAPI");
135          ThirdPartyAPIAdapter { api }
136      }
137  }
138
139  impl PaymentProcessor for ThirdPartyAPIAdapter {
140      fn process_payment(&self, amount: f64, currency: &str) -> Result<String, String> {
141          // Convert to JSON-like payload expected by third-party API
142          let payload = format!("{{\"amount\":{},\"currency\":\"{}\"}}", amount, currency);
143
144          println!("  [Adapter] Converting to JSON payload");
145
146          let txn_ref = self.api.execute_transaction(&payload);
147          Ok(txn_ref)
148      }
149
150      fn refund(&self, transaction_id: &str) -> Result<String, String> {
151          println!("  [Adapter] Passing transaction ID directly");
152
153          let refund_ref = self.api.reverse_transaction(transaction_id);
154          Ok(refund_ref)
155      }
156  }
157
158  /// Client code that works with any PaymentProcessor
159  fn process_order(processor: &dyn PaymentProcessor, amount: f64, currency: &str) {
160      println!("\n  Processing order for ${:.2} {}...", amount, currency);
161
162      match processor.process_payment(amount, currency) {
163          Ok(tx_id) => {
164              println!("  Payment successful! Transaction ID: {}", tx_id);
165
166              // Demonstrate refund
167              println!("\n  Initiating refund...");
168              match processor.refund(&tx_id) {
169                  Ok(result) => println!("  {}", result),
170                  Err(e) => println!("  Refund error: {}", e),
171              }
172          }
173          Err(e) => println!("  Payment failed: {}", e),
174      }
175  }
176
177  fn main() {
178      println!("=== Adapter Pattern Demo ===\n");
179
180      // Example 1: Adapt legacy payment gateway
181      println!("1. Setting up Legacy Gateway Adapter:");
182      let legacy = LegacyPaymentGateway::new("OldBankGateway");
183      let legacy_adapter = LegacyGatewayAdapter::new(legacy);
184
185      println!("\n2. Processing payment through Legacy Adapter:");
186      process_order(&legacy_adapter, 99.99, "USD");
187
188      println!("\n{}\n", "=".repeat(50));
189
190      // Example 2: Adapt third-party API
191      println!("3. Setting up Third-Party API Adapter:");
192      let third_party = ThirdPartyPaymentAPI::new("sk_live_abc123xyz789");
193      let third_party_adapter = ThirdPartyAPIAdapter::new(third_party);
194
195      println!("\n4. Processing payment through Third-Party Adapter:");
196      process_order(&third_party_adapter, 149.50, "EUR");
197
198      println!("\n{}\n", "=".repeat(50));
199
200      // Example 3: Polymorphic usage - same client code works with both
201      println!("5. Polymorphic usage with multiple processors:");
202      let processors: Vec<Box<dyn PaymentProcessor>> = vec![
203          Box::new(LegacyGatewayAdapter::new(LegacyPaymentGateway::new("BankA"))),
204          Box::new(ThirdPartyAPIAdapter::new(ThirdPartyPaymentAPI::new("sk_test_987654321"))),
205      ];
206
207      for (i, processor) in processors.iter().enumerate() {
208          println!("\n  --- Processor {} ---", i + 1);
209          match processor.process_payment(50.00, "GBP") {
210              Ok(tx_id) => println!("  Transaction: {}", tx_id),
211              Err(e) => println!("  Error: {}", e),
212          }
213      }
214
215      println!("\n=== Demo Complete ===");
216  }
```

## Program Output

```
=== Adapter Pattern Demo ===

1. Setting up Legacy Gateway Adapter:
  [LegacyGateway] Initializing legacy gateway: OldBankGateway
  [Adapter] Wrapping LegacyPaymentGateway

2. Processing payment through Legacy Adapter:

  Processing order for $99.99 USD...
  [Adapter] Converting $99.99 to 9999 cents
  [LegacyGateway] Processing 9999 cents in USD via OldBankGateway
  Payment successful! Transaction ID: LEGACY-12345

  Initiating refund...
  [Adapter] Converting transaction ID LEGACY-12345 to legacy format 12345
  [LegacyGateway] Canceling transaction #12345 via OldBankGateway
  Refund successful for LEGACY-12345

==================================================

3. Setting up Third-Party API Adapter:
  [ThirdPartyAPI] Initializing with API key: sk_live_...
  [Adapter] Wrapping ThirdPartyPaymentAPI

4. Processing payment through Third-Party Adapter:

  Processing order for $149.50 EUR...
  [Adapter] Converting to JSON payload
  [ThirdPartyAPI] Executing transaction with payload: {"amount":149.5,"currency":"EUR"}
  Payment successful! Transaction ID: TXN-sk_l-ABC123

  Initiating refund...
  [Adapter] Passing transaction ID directly
  [ThirdPartyAPI] Reversing transaction: TXN-sk_l-ABC123
  REFUND-TXN-sk_l-ABC123

==================================================

5. Polymorphic usage with multiple processors:
  [LegacyGateway] Initializing legacy gateway: BankA
  [Adapter] Wrapping LegacyPaymentGateway
  [ThirdPartyAPI] Initializing with API key: sk_test_...
  [Adapter] Wrapping ThirdPartyPaymentAPI

  --- Processor 1 ---
  [Adapter] Converting $50.00 to 5000 cents
  [LegacyGateway] Processing 5000 cents in GBP via BankA
  Transaction: LEGACY-12345

  --- Processor 2 ---
  [Adapter] Converting to JSON payload
  [ThirdPartyAPI] Executing transaction with payload: {"amount":50,"currency":"GBP"}
  Transaction: TXN-sk_t-ABC123

=== Demo Complete ===
```

## Code Annotations

### Target Interface (Lines 7-11)

- **Lines 8-11**: The `PaymentProcessor` trait defines the target interface that clients expect
- This is a consistent API with `process_payment()` taking `f64` amount and string currency, returning `Result<String, String>`

### Adaptee 1: Legacy System (Lines 13-46)

- **Lines 14-16**: `LegacyPaymentGateway` has an incompatible interface
- **Line 27**: `make_payment()` uses `i64` cents instead of `f64` dollars, and `i32` currency codes instead of strings
- **Line 37**: Returns transaction ID as `i32` instead of `String`
- **Line 41**: `cancel_transaction()` returns `bool` instead of `Result`

### Adaptee 2: Third-Party API (Lines 48-72)

- **Lines 49-51**: `ThirdPartyPaymentAPI` has yet another incompatible interface
- **Line 62**: `execute_transaction()` expects JSON payload string
- **Line 68**: Uses `reverse_transaction()` instead of `refund()`

### Adapter 1: LegacyGatewayAdapter (Lines 74-125)

- **Lines 75-77**: Wraps the `LegacyPaymentGateway` (composition)
- **Lines 87-94**: Helper method to convert string currency to integer codes
- **Lines 97-107**: Implements `PaymentProcessor::process_payment()`:
  - **Line 100**: Converts dollars to cents
  - **Line 101**: Converts currency string to code
  - **Line 105**: Calls legacy `make_payment()`
  - **Line 106**: Formats integer ID to string format
- **Lines 109-124**: Implements `PaymentProcessor::refund()`:
  - **Lines 111-114**: Parses string ID back to integer
  - **Line 119**: Calls legacy `cancel_transaction()`
  - **Lines 120-122**: Converts boolean to Result

### Adapter 2: ThirdPartyAPIAdapter (Lines 127-156)

- **Lines 128-130**: Wraps the `ThirdPartyPaymentAPI`
- **Lines 139-148**: Converts amount/currency to JSON payload format
- **Lines 150-155**: Passes through to `reverse_transaction()`

### Client Code (Lines 158-175)

- **Line 159**: `process_order()` accepts any `&dyn PaymentProcessor`
- The client code is completely decoupled from specific implementations

### Output Correlation

| Output Section | Source Lines | Adapter Action |
|----------------|--------------|----------------|
| "Converting $99.99 to 9999 cents" | 100, 103 | LegacyAdapter converts f64 to i64 cents |
| "Processing 9999 cents in USD" | 27-35 | Legacy gateway receives its expected format |
| "Converting transaction ID LEGACY-12345 to legacy format 12345" | 111-117 | Adapter parses string back to integer for refund |
| "Converting to JSON payload" | 142-144 | ThirdPartyAdapter creates JSON structure |
| "Executing transaction with payload: {\"amount\":149.5...}" | 62-64 | Third-party API receives its expected JSON format |
| Polymorphic processors in Vec | 202-205 | Both adapters stored as trait objects, used interchangeably |

### Key Adapter Pattern Characteristics in Rust

1. **Composition over Inheritance**: Adapters wrap adaptees rather than inheriting from them
2. **Trait-based Target**: The target interface is defined as a trait, enabling polymorphism
3. **Interface Translation**: Each adapter method translates between incompatible interfaces
4. **Transparent Usage**: Client code (`process_order`) works with any `PaymentProcessor` implementation
5. **Dynamic Dispatch**: `&dyn PaymentProcessor` enables runtime polymorphism (line 159)

## How to Run

```bash
rustc main_adapter.rs -o main_adapter
./main_adapter
```

Or with Cargo in a project:
```bash
cargo run
```
