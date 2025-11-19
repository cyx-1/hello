# State Pattern

The State pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

## Key Components

- **Context**: Maintains instance of ConcreteState subclass for current state
- **State**: Interface for encapsulating state-specific behavior
- **ConcreteState**: Implements behavior associated with a state

## Key Source Code

### State Interface and Concrete States

```python:main_state.py startLine=22 endLine=44
# State interface
class VendingMachineState(ABC):
    """Abstract state for vending machine."""

    @abstractmethod
    def insert_coin(self, machine: "VendingMachine", amount: float) -> str:
        pass

    @abstractmethod
    def select_product(self, machine: "VendingMachine", product: str) -> str:
        pass

    @abstractmethod
    def dispense(self, machine: "VendingMachine") -> str:
        pass

    @abstractmethod
    def cancel(self, machine: "VendingMachine") -> str:
        pass

    @abstractmethod
    def get_state_name(self) -> str:
        pass
```

### State Transition Logic (IdleState to HasMoneyState)

```python:main_state.py startLine=47 endLine=66
class IdleState(VendingMachineState):
    """Machine is idle, waiting for coins."""

    def insert_coin(self, machine: "VendingMachine", amount: float) -> str:
        machine.add_credit(amount)
        machine.set_state(HasMoneyState())
        return f"Inserted ${amount:.2f}. Credit: ${machine.credit:.2f}"

    def select_product(self, machine: "VendingMachine", product: str) -> str:
        return "Please insert coins first"

    def dispense(self, machine: "VendingMachine") -> str:
        return "Please insert coins and select a product"

    def cancel(self, machine: "VendingMachine") -> str:
        return "No transaction to cancel"

    def get_state_name(self) -> str:
        return "Idle"
```

### Context Class with State Delegation

```python:main_state.py startLine=164 endLine=192
# Context
class VendingMachine:
    """Context: Vending machine that changes behavior based on state."""

    def __init__(self):
        self._state: VendingMachineState = IdleState()
        self._credit = 0.0
        self._inventory: dict[str, dict] = {
            "Cola": {"price": 1.50, "stock": 5},
            "Chips": {"price": 1.25, "stock": 3},
            "Candy": {"price": 0.75, "stock": 10},
            "Water": {"price": 1.00, "stock": 8},
        }
        self.selected_product = ""

    @property
    def credit(self) -> float:
        return self._credit

    @property
    def inventory(self) -> dict[str, dict]:
        return self._inventory

    def set_state(self, state: VendingMachineState) -> None:
        old_state = self._state.get_state_name()
        self._state = state
        print(f"  [State] {old_state} -> {state.get_state_name()}")
```

## Program Output

```
============================================================
State Pattern - Vending Machine Demo
============================================================

--- Normal Operation ---

Available products:
  Cola: $1.50 (Stock: 5)
  Chips: $1.25 (Stock: 3)
  Candy: $0.75 (Stock: 10)
  Water: $1.00 (Stock: 8)

--- Transaction 1 ---
  [State] Idle -> HasMoney
Inserted $1.00. Credit: $1.00
Added $0.50. Total credit: $1.50
  [State] HasMoney -> Dispensing
Selected Cola ($1.50). Dispensing...
  [State] Dispensing -> Idle
Dispensed: Cola

--- Transaction 2 (Insufficient funds) ---
  [State] Idle -> HasMoney
Inserted $0.50. Credit: $0.50
Insufficient credit. Chips costs $1.25, you have $0.50

--- Transaction 2 (Add more money) ---
Added $1.00. Total credit: $1.50
  [State] HasMoney -> Dispensing
Selected Chips ($1.25). Dispensing...
  [State] Dispensing -> Idle
Dispensed: Chips
Change: $0.25

--- Transaction 3 (Cancel) ---
  [State] Idle -> HasMoney
Inserted $2.00. Credit: $2.00
  [State] HasMoney -> Idle
Transaction cancelled. Refund: $2.00

--- Invalid Operations ---
Please insert coins first
Please insert coins and select a product

============================================================
State Pattern - Document Workflow Demo
============================================================

--- Document Lifecycle ---
Initial state: Draft

Document edited
State: Draft

Document submitted for review
State: Review

Cannot edit during review

Document rejected. Returned to draft
State: Draft

Document edited
Document submitted for review
State: Review

Document approved
State: Approved

Document published!
State: Published

Cannot edit published document. Create new version

============================================================
Benefits of State Pattern:
============================================================
1. Localizes state-specific behavior
2. Makes state transitions explicit
3. State objects can be shared
4. Eliminates large conditional statements
5. Follows Single Responsibility Principle
```

## Output Annotations

- **Lines 1-12**: Initial setup showing available products and their prices/stock (lines 229-233 in source)
- **Lines 14-20**: Transaction 1 demonstrates state transitions from Idle -> HasMoney -> Dispensing -> Idle as coins are inserted (lines 50-53), product selected (lines 86-88), and dispensed (lines 128-132)
- **Lines 22-25**: Transaction 2 shows validation in HasMoneyState preventing purchase with insufficient funds (lines 79-81)
- **Lines 27-32**: Adding more money in HasMoneyState (lines 71-73) then completing purchase with change calculation (lines 121-126)
- **Lines 34-38**: Cancel operation in HasMoneyState returns refund and transitions back to Idle (lines 93-97)
- **Lines 40-42**: Invalid operations demonstrate state-specific behavior - IdleState rejects operations requiring money (lines 55-59)
- **Lines 46-75**: Document workflow demo shows different state pattern implementation with Draft -> Review -> Approved -> Published lifecycle
- **Lines 52, 55**: Shows that editing is blocked during Review state (line 289) and after Publishing (line 335)

## Requirements

- Python 3.10+ (uses union type syntax with `|` and type hints)

## Running the Example

```bash
uv run python main_state.py
```
