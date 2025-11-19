# Strategy Pattern

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

## Key Components

- **Strategy**: Interface common to all supported algorithms
- **ConcreteStrategy**: Implements algorithm using Strategy interface
- **Context**: Configured with ConcreteStrategy, maintains reference to Strategy

## Key Source Code

### Strategy Interface

```python:main_strategy.py startLine=22 endLine=37
# Strategy interface
class PaymentStrategy(ABC):
    """Abstract strategy for payment processing."""

    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
```

### Concrete Strategies (Payment Methods)

```python:main_strategy.py startLine=40 endLine=62
class CreditCardPayment(PaymentStrategy):
    """Strategy for credit card payments."""

    def __init__(self, card_number: str, cvv: str, expiry: str):
        self._card_number = card_number
        self._cvv = cvv
        self._expiry = expiry

    def pay(self, amount: float) -> str:
        masked = "*" * 12 + self._card_number[-4:]
        return f"Paid ${amount:.2f} using Credit Card {masked}"

    def validate(self) -> bool:
        # Simple validation
        return (
            len(self._card_number) == 16
            and len(self._cvv) == 3
            and len(self._expiry) == 5
        )

    def get_name(self) -> str:
        return "Credit Card"
```

```python:main_strategy.py startLine=80 endLine=106
class CryptoPayment(PaymentStrategy):
    """Strategy for cryptocurrency payments."""

    def __init__(self, wallet_address: str, currency: str = "BTC"):
        self._wallet = wallet_address
        self._currency = currency

    def pay(self, amount: float) -> str:
        # Simulate conversion
        if self._currency == "BTC":
            crypto_amount = amount / 45000
        elif self._currency == "ETH":
            crypto_amount = amount / 3000
        else:
            crypto_amount = amount

        return (
            f"Paid {crypto_amount:.6f} {self._currency} "
            f"(${amount:.2f}) to {self._wallet[:8]}..."
        )

    def validate(self) -> bool:
        return len(self._wallet) >= 26

    def get_name(self) -> str:
        return f"Crypto ({self._currency})"
```

### Context Class with Strategy Selection

```python:main_strategy.py startLine=127 endLine=164
class ShoppingCart:
    """Context that uses payment strategies."""

    def __init__(self):
        self._items: list[dict[str, Any]] = []
        self._payment_strategy: PaymentStrategy | None = None

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        self._items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name: str) -> bool:
        for i, item in enumerate(self._items):
            if item["name"] == name:
                self._items.pop(i)
                return True
        return False

    def get_total(self) -> float:
        return sum(item["price"] * item["quantity"] for item in self._items)

    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self._payment_strategy = strategy

    def checkout(self) -> str:
        if not self._items:
            return "Cart is empty"

        if not self._payment_strategy:
            return "Please select a payment method"

        if not self._payment_strategy.validate():
            return f"Invalid {self._payment_strategy.get_name()} details"

        total = self.get_total()
        result = self._payment_strategy.pay(total)
        self._items.clear()
        return result
```

## Program Output

```
============================================================
Strategy Pattern - Payment Processing Demo
============================================================

Shopping Cart:
  Laptop x1: $999.99
  Mouse x2: $59.98
  Keyboard x1: $79.99
  Total: $1139.96

--- Payment with Credit Card ---
Paid $1139.96 using Credit Card ************3456

Shopping Cart:
  Monitor x1: $349.99
  Webcam x1: $89.99
  Total: $439.98

--- Payment with PayPal ---
Paid $439.98 using PayPal (user@example.com)

Shopping Cart:
  Headphones x1: $199.99
  Total: $199.99

--- Payment with Crypto ---
Paid 0.004444 BTC ($199.99) to bc1qxy2k...

============================================================
Strategy Pattern - Sorting Demo
============================================================

Original data: [64, 34, 25, 12, 22, 11, 90, 45]
Sorting with Quick Sort...
Result: [11, 12, 22, 25, 34, 45, 64, 90]
Sorting with Bubble Sort...
Result: [11, 12, 22, 25, 34, 45, 64, 90]
Sorting with Merge Sort...
Result: [11, 12, 22, 25, 34, 45, 64, 90]

============================================================
Strategy Pattern - Compression Demo
============================================================

Original: AAABBBCCCCDDDDDEEEEE
Run-Length Encoding: 20 -> 10 chars (50.0%)
Compressed: A3B3C4D5E5
Huffman-like: 20 -> 43 chars (215.0%)
Compressed: [5]$3$3$3$4$4$4$2$2$2$2$0$0$0$0$0$1$1$1$1$1

============================================================
Benefits of Strategy Pattern:
============================================================
1. Family of algorithms are interchangeable
2. Alternative to subclassing for extending behavior
3. Eliminates conditional statements
4. Easy to add new strategies
5. Follows Open/Closed Principle
```

## Output Annotations

- **Lines 5-9**: Shopping cart displays items added via `add_item()` method (lines 134-135), with total calculated by `get_total()` (lines 144-145)
- **Lines 11-12**: Credit card payment uses `CreditCardPayment.pay()` (lines 48-50) which masks the card number, showing only last 4 digits
- **Lines 14-18**: Same cart context with different strategy - PayPal payment via `set_payment_strategy()` (lines 147-148)
- **Lines 20-24**: Crypto strategy demonstrates algorithm-specific logic (lines 88-98) - converts USD to BTC using exchange rate
- **Lines 28-34**: Sorting demo shows three different sorting strategies (QuickSort, BubbleSort, MergeSort) producing same results but with different algorithms (lines 190-254)
- **Lines 38-43**: Compression strategies show different approaches - Run-Length Encoding (lines 284-304) achieves 50% compression, while simplified Huffman-like (lines 310-331) uses frequency-based encoding

## Requirements

- Python 3.10+ (uses union type syntax with `|`)

## Running the Example

```bash
uv run python main_strategy.py
```
