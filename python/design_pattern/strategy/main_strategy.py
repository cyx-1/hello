# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Strategy Pattern

The Strategy pattern defines a family of algorithms, encapsulates each one,
and makes them interchangeable. Strategy lets the algorithm vary independently
from clients that use it.

Key Components:
- Strategy: Interface common to all supported algorithms
- ConcreteStrategy: Implements algorithm using Strategy interface
- Context: Configured with ConcreteStrategy, maintains reference to Strategy
"""

from abc import ABC, abstractmethod
from typing import Any


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


# Concrete Strategies
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


class PayPalPayment(PaymentStrategy):
    """Strategy for PayPal payments."""

    def __init__(self, email: str):
        self._email = email

    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using PayPal ({self._email})"

    def validate(self) -> bool:
        return "@" in self._email and "." in self._email

    def get_name(self) -> str:
        return "PayPal"


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


class BankTransferPayment(PaymentStrategy):
    """Strategy for bank transfer payments."""

    def __init__(self, account_number: str, routing_number: str):
        self._account = account_number
        self._routing = routing_number

    def pay(self, amount: float) -> str:
        masked = "*" * (len(self._account) - 4) + self._account[-4:]
        return f"Initiated bank transfer of ${amount:.2f} to account {masked}"

    def validate(self) -> bool:
        return len(self._account) >= 8 and len(self._routing) == 9

    def get_name(self) -> str:
        return "Bank Transfer"


# Context
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

    def show_cart(self) -> None:
        if not self._items:
            print("Cart is empty")
            return

        print("\nShopping Cart:")
        for item in self._items:
            subtotal = item["price"] * item["quantity"]
            print(f"  {item['name']} x{item['quantity']}: ${subtotal:.2f}")
        print(f"  Total: ${self.get_total():.2f}")


# Sorting Strategy example
class SortStrategy(ABC):
    """Abstract strategy for sorting."""

    @abstractmethod
    def sort(self, data: list[Any]) -> list[Any]:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class BubbleSort(SortStrategy):
    """Bubble sort strategy - O(n²)."""

    def sort(self, data: list[Any]) -> list[Any]:
        result = data.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result

    def get_name(self) -> str:
        return "Bubble Sort"


class QuickSort(SortStrategy):
    """Quick sort strategy - O(n log n)."""

    def sort(self, data: list[Any]) -> list[Any]:
        if len(data) <= 1:
            return data.copy()

        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]

        return self.sort(left) + middle + self.sort(right)

    def get_name(self) -> str:
        return "Quick Sort"


class MergeSort(SortStrategy):
    """Merge sort strategy - O(n log n)."""

    def sort(self, data: list[Any]) -> list[Any]:
        if len(data) <= 1:
            return data.copy()

        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])

        return self._merge(left, right)

    def _merge(self, left: list[Any], right: list[Any]) -> list[Any]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def get_name(self) -> str:
        return "Merge Sort"


class Sorter:
    """Context for sorting strategies."""

    def __init__(self, strategy: SortStrategy | None = None):
        self._strategy = strategy or QuickSort()

    def set_strategy(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def sort(self, data: list[Any]) -> list[Any]:
        print(f"Sorting with {self._strategy.get_name()}...")
        return self._strategy.sort(data)


# Compression Strategy example
class CompressionStrategy(ABC):
    """Abstract strategy for compression."""

    @abstractmethod
    def compress(self, data: str) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class RunLengthCompression(CompressionStrategy):
    """Run-length encoding compression."""

    def compress(self, data: str) -> str:
        if not data:
            return ""

        result = []
        count = 1
        prev = data[0]

        for char in data[1:]:
            if char == prev:
                count += 1
            else:
                result.append(f"{prev}{count}" if count > 1 else prev)
                prev = char
                count = 1

        result.append(f"{prev}{count}" if count > 1 else prev)
        return "".join(result)

    def get_name(self) -> str:
        return "Run-Length Encoding"


class HuffmanCompression(CompressionStrategy):
    """Simplified Huffman-like compression (demonstration)."""

    def compress(self, data: str) -> str:
        # Simple frequency-based replacement
        freq: dict[str, int] = {}
        for char in data:
            freq[char] = freq.get(char, 0) + 1

        # Sort by frequency
        sorted_chars = sorted(freq.items(), key=lambda x: -x[1])

        # Replace common chars with shorter codes
        mapping = {}
        for i, (char, _) in enumerate(sorted_chars):
            if i < 10:
                mapping[char] = f"${i}"
            else:
                mapping[char] = char

        result = "".join(mapping.get(c, c) for c in data)
        return f"[{len(mapping)}]" + result

    def get_name(self) -> str:
        return "Huffman-like"


class FileCompressor:
    """Context for compression strategies."""

    def __init__(self, strategy: CompressionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: CompressionStrategy) -> None:
        self._strategy = strategy

    def compress(self, data: str) -> str:
        compressed = self._strategy.compress(data)
        ratio = len(compressed) / len(data) * 100 if data else 0
        print(
            f"{self._strategy.get_name()}: "
            f"{len(data)} -> {len(compressed)} chars ({ratio:.1f}%)"
        )
        return compressed


def main() -> None:
    print("=" * 60)
    print("Strategy Pattern - Payment Processing Demo")
    print("=" * 60)

    # Demo 1: Shopping cart with different payment methods
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99)
    cart.add_item("Mouse", 29.99, 2)
    cart.add_item("Keyboard", 79.99)

    cart.show_cart()

    # Try different payment strategies
    print("\n--- Payment with Credit Card ---")
    credit_card = CreditCardPayment("1234567890123456", "123", "12/25")
    cart.set_payment_strategy(credit_card)
    print(cart.checkout())

    # Refill cart
    cart.add_item("Monitor", 349.99)
    cart.add_item("Webcam", 89.99)
    cart.show_cart()

    print("\n--- Payment with PayPal ---")
    paypal = PayPalPayment("user@example.com")
    cart.set_payment_strategy(paypal)
    print(cart.checkout())

    # Refill cart
    cart.add_item("Headphones", 199.99)
    cart.show_cart()

    print("\n--- Payment with Crypto ---")
    crypto = CryptoPayment("bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh", "BTC")
    cart.set_payment_strategy(crypto)
    print(cart.checkout())

    # Demo 2: Sorting strategies
    print("\n" + "=" * 60)
    print("Strategy Pattern - Sorting Demo")
    print("=" * 60)

    data = [64, 34, 25, 12, 22, 11, 90, 45]
    print(f"\nOriginal data: {data}")

    sorter = Sorter()

    # Quick Sort (default)
    result = sorter.sort(data)
    print(f"Result: {result}")

    # Bubble Sort
    sorter.set_strategy(BubbleSort())
    result = sorter.sort(data)
    print(f"Result: {result}")

    # Merge Sort
    sorter.set_strategy(MergeSort())
    result = sorter.sort(data)
    print(f"Result: {result}")

    # Demo 3: Compression strategies
    print("\n" + "=" * 60)
    print("Strategy Pattern - Compression Demo")
    print("=" * 60)

    text = "AAABBBCCCCDDDDDEEEEE"
    print(f"\nOriginal: {text}")

    compressor = FileCompressor(RunLengthCompression())
    compressed = compressor.compress(text)
    print(f"Compressed: {compressed}")

    compressor.set_strategy(HuffmanCompression())
    compressed = compressor.compress(text)
    print(f"Compressed: {compressed}")

    print("\n" + "=" * 60)
    print("Benefits of Strategy Pattern:")
    print("=" * 60)
    print("1. Family of algorithms are interchangeable")
    print("2. Alternative to subclassing for extending behavior")
    print("3. Eliminates conditional statements")
    print("4. Easy to add new strategies")
    print("5. Follows Open/Closed Principle")


if __name__ == "__main__":
    main()
