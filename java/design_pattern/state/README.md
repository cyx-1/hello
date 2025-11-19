# State Pattern

Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

## How to Run
```bash
cd java/state
mvn compile exec:java
```

## Key Source Code

### State Interface (Lines 9-14)
```java
interface VendingMachineState {
    void insertCoin();
    void ejectCoin();
    void selectProduct();
    void dispense();
}
```

### Context (Lines 17-42)
```java
class VendingMachine {
    private VendingMachineState currentState;

    public void insertCoin() { currentState.insertCoin(); }
    public void setState(VendingMachineState state) {
        currentState = state;
    }
}
```

### Concrete State (Lines 45-67)
```java
class NoCoinState implements VendingMachineState {
    @Override
    public void insertCoin() {
        System.out.println("Coin inserted");
        machine.setState(machine.getHasCoinState());
    }
}
```

## Program Output
```
--- 1. Vending Machine ---
Attempt without coin:
  [NoCoin] Please insert a coin first

Normal purchase:
  [NoCoin] Coin inserted
  [HasCoin] Product selected
  [Machine] Product dispensed. Remaining: 1

Sold out:
  [SoldOut] Machine is sold out, returning coin

--- 2. Document Workflow ---
Draft phase:
  [Draft] Editing document: Annual Report
  [Draft] Cannot publish from draft state

Approve and publish:
  [Review] Document approved: Annual Report
  [Approved] Publishing document: Annual Report
```

## Pattern Benefits
- Localizes state-specific behavior
- Makes state transitions explicit
- Eliminates conditional statements

## Requirements
- Java 17 or higher
- Maven 3.x
