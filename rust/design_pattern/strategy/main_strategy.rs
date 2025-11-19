// Strategy Design Pattern in Rust
// Demonstrates runtime algorithm selection using traits

// Strategy trait defining the payment interface
trait PaymentStrategy {
    fn pay(&self, amount: f64) -> String;
    fn name(&self) -> &str;
}

// Concrete Strategy: Credit Card Payment
struct CreditCardPayment {
    card_number: String,
    card_holder: String,
}

impl CreditCardPayment {
    fn new(card_number: &str, card_holder: &str) -> Self {
        CreditCardPayment {
            card_number: card_number.to_string(),
            card_holder: card_holder.to_string(),
        }
    }
}

impl PaymentStrategy for CreditCardPayment {
    fn pay(&self, amount: f64) -> String {
        format!(
            "Paid ${:.2} using Credit Card ending in {} (Holder: {})",
            amount,
            &self.card_number[self.card_number.len() - 4..],
            self.card_holder
        )
    }

    fn name(&self) -> &str {
        "Credit Card"
    }
}

// Concrete Strategy: PayPal Payment
struct PayPalPayment {
    email: String,
}

impl PayPalPayment {
    fn new(email: &str) -> Self {
        PayPalPayment {
            email: email.to_string(),
        }
    }
}

impl PaymentStrategy for PayPalPayment {
    fn pay(&self, amount: f64) -> String {
        format!("Paid ${:.2} using PayPal account: {}", amount, self.email)
    }

    fn name(&self) -> &str {
        "PayPal"
    }
}

// Concrete Strategy: Bitcoin Payment
struct BitcoinPayment {
    wallet_address: String,
}

impl BitcoinPayment {
    fn new(wallet_address: &str) -> Self {
        BitcoinPayment {
            wallet_address: wallet_address.to_string(),
        }
    }
}

impl PaymentStrategy for BitcoinPayment {
    fn pay(&self, amount: f64) -> String {
        format!(
            "Paid ${:.2} in Bitcoin to wallet: {}...{}",
            amount,
            &self.wallet_address[..6],
            &self.wallet_address[self.wallet_address.len() - 4..]
        )
    }

    fn name(&self) -> &str {
        "Bitcoin"
    }
}

// Context: Shopping Cart that uses payment strategies
struct ShoppingCart {
    items: Vec<(String, f64)>,
    payment_strategy: Box<dyn PaymentStrategy>,
}

impl ShoppingCart {
    fn new(strategy: Box<dyn PaymentStrategy>) -> Self {
        println!("=== Shopping Cart Created ===");
        println!("Initial payment method: {}", strategy.name());
        ShoppingCart {
            items: Vec::new(),
            payment_strategy: strategy,
        }
    }

    fn add_item(&mut self, name: &str, price: f64) {
        println!("Added item: {} - ${:.2}", name, price);
        self.items.push((name.to_string(), price));
    }

    fn set_payment_strategy(&mut self, strategy: Box<dyn PaymentStrategy>) {
        println!("\n--- Switching Payment Strategy ---");
        println!("From: {} -> To: {}", self.payment_strategy.name(), strategy.name());
        self.payment_strategy = strategy;
    }

    fn calculate_total(&self) -> f64 {
        self.items.iter().map(|(_, price)| price).sum()
    }

    fn checkout(&self) {
        let total = self.calculate_total();
        println!("\n=== Checkout ===");
        println!("Items in cart: {}", self.items.len());
        println!("Total amount: ${:.2}", total);
        let result = self.payment_strategy.pay(total);
        println!("Payment result: {}", result);
        println!("Checkout complete!\n");
    }
}

fn main() {
    println!("========================================");
    println!("  Strategy Pattern - Payment Example");
    println!("========================================\n");

    // Create cart with Credit Card strategy
    let credit_card = CreditCardPayment::new("4532015112830366", "John Doe");
    let mut cart = ShoppingCart::new(Box::new(credit_card));

    // Add items to cart
    println!("\n--- Adding Items ---");
    cart.add_item("Laptop", 999.99);
    cart.add_item("Mouse", 29.99);
    cart.add_item("Keyboard", 79.99);

    // Checkout with Credit Card
    cart.checkout();

    // Switch to PayPal strategy
    let paypal = PayPalPayment::new("john.doe@email.com");
    cart.set_payment_strategy(Box::new(paypal));

    // Add more items
    println!("\n--- Adding More Items ---");
    cart.add_item("Monitor", 349.99);
    cart.add_item("USB Hub", 24.99);

    // Checkout with PayPal
    cart.checkout();

    // Switch to Bitcoin strategy
    let bitcoin = BitcoinPayment::new("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa");
    cart.set_payment_strategy(Box::new(bitcoin));

    // Add final item
    println!("\n--- Adding Final Item ---");
    cart.add_item("Graphics Card", 599.99);

    // Checkout with Bitcoin
    cart.checkout();

    println!("========================================");
    println!("  Strategy Pattern Demo Complete!");
    println!("========================================");
}
