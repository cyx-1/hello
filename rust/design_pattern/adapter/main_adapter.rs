//! Adapter Pattern in Rust
//!
//! The Adapter pattern allows incompatible interfaces to work together by
//! wrapping an object with an incompatible interface in an adapter that
//! implements the expected interface.

/// Target interface that the client expects
trait PaymentProcessor {
    fn process_payment(&self, amount: f64, currency: &str) -> Result<String, String>;
    fn refund(&self, transaction_id: &str) -> Result<String, String>;
}

/// Legacy payment system with incompatible interface
struct LegacyPaymentGateway {
    gateway_name: String,
}

impl LegacyPaymentGateway {
    fn new(name: &str) -> Self {
        println!("  [LegacyGateway] Initializing legacy gateway: {}", name);
        LegacyPaymentGateway {
            gateway_name: name.to_string(),
        }
    }

    /// Legacy method with different signature - uses cents instead of dollars
    fn make_payment(&self, amount_cents: i64, currency_code: i32) -> i32 {
        let currency = match currency_code {
            1 => "USD",
            2 => "EUR",
            3 => "GBP",
            _ => "UNKNOWN",
        };
        println!("  [LegacyGateway] Processing {} cents in {} via {}",
                 amount_cents, currency, self.gateway_name);
        // Returns transaction ID as integer
        12345
    }

    /// Legacy refund method with different return type
    fn cancel_transaction(&self, tx_id: i32) -> bool {
        println!("  [LegacyGateway] Canceling transaction #{} via {}",
                 tx_id, self.gateway_name);
        true
    }
}

/// Modern third-party payment API with yet another interface
struct ThirdPartyPaymentAPI {
    api_key: String,
}

impl ThirdPartyPaymentAPI {
    fn new(api_key: &str) -> Self {
        println!("  [ThirdPartyAPI] Initializing with API key: {}...", &api_key[..8]);
        ThirdPartyPaymentAPI {
            api_key: api_key.to_string(),
        }
    }

    /// Third-party method using JSON-like structure
    fn execute_transaction(&self, payload: &str) -> String {
        println!("  [ThirdPartyAPI] Executing transaction with payload: {}", payload);
        format!("TXN-{}-{}", &self.api_key[..4], "ABC123")
    }

    /// Third-party refund with different naming
    fn reverse_transaction(&self, txn_ref: &str) -> String {
        println!("  [ThirdPartyAPI] Reversing transaction: {}", txn_ref);
        format!("REFUND-{}", txn_ref)
    }
}

/// Adapter for LegacyPaymentGateway to implement PaymentProcessor
struct LegacyGatewayAdapter {
    legacy_gateway: LegacyPaymentGateway,
}

impl LegacyGatewayAdapter {
    fn new(gateway: LegacyPaymentGateway) -> Self {
        println!("  [Adapter] Wrapping LegacyPaymentGateway");
        LegacyGatewayAdapter {
            legacy_gateway: gateway,
        }
    }

    fn currency_to_code(&self, currency: &str) -> i32 {
        match currency {
            "USD" => 1,
            "EUR" => 2,
            "GBP" => 3,
            _ => 0,
        }
    }
}

impl PaymentProcessor for LegacyGatewayAdapter {
    fn process_payment(&self, amount: f64, currency: &str) -> Result<String, String> {
        // Convert dollars to cents
        let amount_cents = (amount * 100.0) as i64;
        let currency_code = self.currency_to_code(currency);

        println!("  [Adapter] Converting ${:.2} to {} cents", amount, amount_cents);

        let tx_id = self.legacy_gateway.make_payment(amount_cents, currency_code);
        Ok(format!("LEGACY-{}", tx_id))
    }

    fn refund(&self, transaction_id: &str) -> Result<String, String> {
        // Extract numeric ID from adapted format
        let tx_id: i32 = transaction_id
            .replace("LEGACY-", "")
            .parse()
            .map_err(|_| "Invalid transaction ID".to_string())?;

        println!("  [Adapter] Converting transaction ID {} to legacy format {}",
                 transaction_id, tx_id);

        if self.legacy_gateway.cancel_transaction(tx_id) {
            Ok(format!("Refund successful for {}", transaction_id))
        } else {
            Err("Refund failed".to_string())
        }
    }
}

/// Adapter for ThirdPartyPaymentAPI to implement PaymentProcessor
struct ThirdPartyAPIAdapter {
    api: ThirdPartyPaymentAPI,
}

impl ThirdPartyAPIAdapter {
    fn new(api: ThirdPartyPaymentAPI) -> Self {
        println!("  [Adapter] Wrapping ThirdPartyPaymentAPI");
        ThirdPartyAPIAdapter { api }
    }
}

impl PaymentProcessor for ThirdPartyAPIAdapter {
    fn process_payment(&self, amount: f64, currency: &str) -> Result<String, String> {
        // Convert to JSON-like payload expected by third-party API
        let payload = format!("{{\"amount\":{},\"currency\":\"{}\"}}", amount, currency);

        println!("  [Adapter] Converting to JSON payload");

        let txn_ref = self.api.execute_transaction(&payload);
        Ok(txn_ref)
    }

    fn refund(&self, transaction_id: &str) -> Result<String, String> {
        println!("  [Adapter] Passing transaction ID directly");

        let refund_ref = self.api.reverse_transaction(transaction_id);
        Ok(refund_ref)
    }
}

/// Client code that works with any PaymentProcessor
fn process_order(processor: &dyn PaymentProcessor, amount: f64, currency: &str) {
    println!("\n  Processing order for ${:.2} {}...", amount, currency);

    match processor.process_payment(amount, currency) {
        Ok(tx_id) => {
            println!("  Payment successful! Transaction ID: {}", tx_id);

            // Demonstrate refund
            println!("\n  Initiating refund...");
            match processor.refund(&tx_id) {
                Ok(result) => println!("  {}", result),
                Err(e) => println!("  Refund error: {}", e),
            }
        }
        Err(e) => println!("  Payment failed: {}", e),
    }
}

fn main() {
    println!("=== Adapter Pattern Demo ===\n");

    // Example 1: Adapt legacy payment gateway
    println!("1. Setting up Legacy Gateway Adapter:");
    let legacy = LegacyPaymentGateway::new("OldBankGateway");
    let legacy_adapter = LegacyGatewayAdapter::new(legacy);

    println!("\n2. Processing payment through Legacy Adapter:");
    process_order(&legacy_adapter, 99.99, "USD");

    println!("\n{}\n", "=".repeat(50));

    // Example 2: Adapt third-party API
    println!("3. Setting up Third-Party API Adapter:");
    let third_party = ThirdPartyPaymentAPI::new("sk_live_abc123xyz789");
    let third_party_adapter = ThirdPartyAPIAdapter::new(third_party);

    println!("\n4. Processing payment through Third-Party Adapter:");
    process_order(&third_party_adapter, 149.50, "EUR");

    println!("\n{}\n", "=".repeat(50));

    // Example 3: Polymorphic usage - same client code works with both
    println!("5. Polymorphic usage with multiple processors:");
    let processors: Vec<Box<dyn PaymentProcessor>> = vec![
        Box::new(LegacyGatewayAdapter::new(LegacyPaymentGateway::new("BankA"))),
        Box::new(ThirdPartyAPIAdapter::new(ThirdPartyPaymentAPI::new("sk_test_987654321"))),
    ];

    for (i, processor) in processors.iter().enumerate() {
        println!("\n  --- Processor {} ---", i + 1);
        match processor.process_payment(50.00, "GBP") {
            Ok(tx_id) => println!("  Transaction: {}", tx_id),
            Err(e) => println!("  Error: {}", e),
        }
    }

    println!("\n=== Demo Complete ===");
}
