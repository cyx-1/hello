# Strategy Pattern

Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime.

## How to Run
```bash
cd java/strategy
mvn compile exec:java
```

## Key Source Code

### Strategy Interface (Lines 13-16)
```java
interface PaymentStrategy {
    void pay(double amount);
    String getName();
}
```

### Concrete Strategies (Lines 19-50)
```java
class CreditCardPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " using card ending in " +
                          cardNumber.substring(cardNumber.length() - 4));
    }
}

class PayPalPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " from account: " + email);
    }
}
```

### Context (Lines 64-78)
```java
class ShoppingCart {
    private PaymentStrategy paymentStrategy;

    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.paymentStrategy = strategy;
    }

    public void checkout() {
        paymentStrategy.pay(getTotal());
    }
}
```

## Program Output
```
--- 1. Payment Strategy ---
Payment with Credit Card:
  Total: $99.97
  [CreditCard] Paid $99.97 using card ending in 3456

Payment with PayPal:
  Total: $99.97
  [PayPal] Paid $99.97 from account: john.doe@email.com

--- 2. Sorting Strategy ---
Original array: [64, 34, 25, 12, 22, 11, 90]
  [BubbleSort] Array sorted using bubble sort
  [QuickSort] Array sorted using quick sort
  [MergeSort] Array sorted using merge sort
Sorted result: [11, 12, 22, 25, 34, 64, 90]
```

## Pattern Benefits
- Defines family of algorithms
- Makes algorithms interchangeable
- Eliminates conditional statements
- Isolates algorithm implementation

## Requirements
- Java 17 or higher
- Maven 3.x
