# Decorator Pattern

The Decorator pattern attaches additional responsibilities to an object dynamically, providing a flexible alternative to subclassing.

## How to Run

```bash
cd java/decorator
mvn compile exec:java
```

## Key Source Code

### Component Interface (Lines 9-12)
```java
interface Coffee {
    String getDescription();
    double getCost();
}
```

### Base Decorator (Lines 35-48)
```java
abstract class CoffeeDecorator implements Coffee {
    protected Coffee decoratedCoffee;

    public CoffeeDecorator(Coffee coffee) {
        this.decoratedCoffee = coffee;
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription();
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost();
    }
}
```

### Concrete Decorator (Lines 51-63)
```java
class MilkDecorator extends CoffeeDecorator {
    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Milk";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.50;
    }
}
```

## Program Output

```
=== Decorator Pattern Demonstration ===

--- 1. Coffee Shop Orders ---
Simple Coffee = $2.00
Simple Coffee, Milk = $2.50
Espresso, Milk, Vanilla, Whipped Cream = $4.30
Espresso, Milk, Milk, Whipped Cream, Caramel = $4.85

--- 2. Text Formatting ---
Plain: Hello, World!
Bold: <b>Hello, World!</b>
Fancy: <span style="color:red"><u><i><b>Fancy Text!</b></i></u></span>

--- 3. Data Source with Encryption and Compression ---
Writing encrypted data:
  [EncryptionDecorator] Encrypting data
  [FileDataSource] Writing to encrypted.txt: Vhfuhw#Gdwd

Writing compressed and encrypted data:
  [CompressionDecorator] Compressing data (21 -> 33 chars)
  [EncryptionDecorator] Encrypting data
  [FileDataSource] Writing to secure.txt: FRPSUHVVHG^Yhu|#Lpsruwdqw#Vhfuhw`
```

## Pattern Benefits

1. **Flexible Extension**: Add behavior at runtime
2. **Combinable**: Stack decorators in any order
3. **Single Responsibility**: Divide behavior into small classes
4. **Open/Closed**: Extend without modifying existing code

## Requirements

- Java 17 or higher
- Maven 3.x
