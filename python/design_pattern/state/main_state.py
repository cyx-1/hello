# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
State Pattern

The State pattern allows an object to alter its behavior when its internal
state changes. The object will appear to change its class.

Key Components:
- Context: Maintains instance of ConcreteState subclass for current state
- State: Interface for encapsulating state-specific behavior
- ConcreteState: Implements behavior associated with a state
"""

from abc import ABC, abstractmethod
from datetime import datetime


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


# Concrete States
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


class HasMoneyState(VendingMachineState):
    """Machine has money, waiting for product selection."""

    def insert_coin(self, machine: "VendingMachine", amount: float) -> str:
        machine.add_credit(amount)
        return f"Added ${amount:.2f}. Total credit: ${machine.credit:.2f}"

    def select_product(self, machine: "VendingMachine", product: str) -> str:
        if product not in machine.inventory:
            return f"Product '{product}' not available"

        price = machine.get_price(product)
        if machine.credit < price:
            return f"Insufficient credit. {product} costs ${price:.2f}, you have ${machine.credit:.2f}"

        if machine.get_stock(product) <= 0:
            return f"{product} is out of stock"

        machine.selected_product = product
        machine.set_state(DispensingState())
        return f"Selected {product} (${price:.2f}). Dispensing..."

    def dispense(self, machine: "VendingMachine") -> str:
        return "Please select a product first"

    def cancel(self, machine: "VendingMachine") -> str:
        refund = machine.credit
        machine.reset_credit()
        machine.set_state(IdleState())
        return f"Transaction cancelled. Refund: ${refund:.2f}"

    def get_state_name(self) -> str:
        return "HasMoney"


class DispensingState(VendingMachineState):
    """Machine is dispensing selected product."""

    def insert_coin(self, machine: "VendingMachine", amount: float) -> str:
        return "Please wait, dispensing in progress"

    def select_product(self, machine: "VendingMachine", product: str) -> str:
        return "Please wait, dispensing in progress"

    def dispense(self, machine: "VendingMachine") -> str:
        product = machine.selected_product
        price = machine.get_price(product)

        # Dispense product
        machine.reduce_stock(product)
        machine.deduct_credit(price)

        # Calculate change
        change = machine.credit
        message = f"Dispensed: {product}"

        if change > 0:
            message += f"\nChange: ${change:.2f}"
            machine.reset_credit()

        # Transition to appropriate state
        if machine.credit > 0:
            machine.set_state(HasMoneyState())
        else:
            machine.set_state(IdleState())

        machine.selected_product = ""
        return message

    def cancel(self, machine: "VendingMachine") -> str:
        return "Cannot cancel during dispensing"

    def get_state_name(self) -> str:
        return "Dispensing"


class OutOfStockState(VendingMachineState):
    """Machine is out of all products."""

    def insert_coin(self, machine: "VendingMachine", amount: float) -> str:
        return f"Machine is out of stock. Returning ${amount:.2f}"

    def select_product(self, machine: "VendingMachine", product: str) -> str:
        return "Machine is out of stock"

    def dispense(self, machine: "VendingMachine") -> str:
        return "Machine is out of stock"

    def cancel(self, machine: "VendingMachine") -> str:
        return "No transaction to cancel"

    def get_state_name(self) -> str:
        return "OutOfStock"


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

    def get_state_name(self) -> str:
        return self._state.get_state_name()

    def add_credit(self, amount: float) -> None:
        self._credit += amount

    def deduct_credit(self, amount: float) -> None:
        self._credit -= amount

    def reset_credit(self) -> None:
        self._credit = 0.0

    def get_price(self, product: str) -> float:
        return self._inventory[product]["price"]

    def get_stock(self, product: str) -> int:
        return self._inventory[product]["stock"]

    def reduce_stock(self, product: str) -> None:
        self._inventory[product]["stock"] -= 1
        # Check if machine is out of stock
        total_stock = sum(p["stock"] for p in self._inventory.values())
        if total_stock == 0:
            self.set_state(OutOfStockState())

    # Delegated methods
    def insert_coin(self, amount: float) -> str:
        return self._state.insert_coin(self, amount)

    def select_product(self, product: str) -> str:
        return self._state.select_product(self, product)

    def dispense(self) -> str:
        return self._state.dispense(self)

    def cancel(self) -> str:
        return self._state.cancel(self)

    def show_products(self) -> None:
        print("\nAvailable products:")
        for name, info in self._inventory.items():
            status = f"Stock: {info['stock']}" if info["stock"] > 0 else "OUT OF STOCK"
            print(f"  {name}: ${info['price']:.2f} ({status})")


# Document example
class DocumentState(ABC):
    """State for document workflow."""

    @abstractmethod
    def edit(self, doc: "Document") -> str:
        pass

    @abstractmethod
    def review(self, doc: "Document") -> str:
        pass

    @abstractmethod
    def approve(self, doc: "Document") -> str:
        pass

    @abstractmethod
    def reject(self, doc: "Document") -> str:
        pass

    @abstractmethod
    def publish(self, doc: "Document") -> str:
        pass

    @abstractmethod
    def get_state_name(self) -> str:
        pass


class DraftState(DocumentState):
    def edit(self, doc: "Document") -> str:
        doc.modified_at = datetime.now()
        return "Document edited"

    def review(self, doc: "Document") -> str:
        doc.set_state(ReviewState())
        return "Document submitted for review"

    def approve(self, doc: "Document") -> str:
        return "Cannot approve draft. Submit for review first"

    def reject(self, doc: "Document") -> str:
        return "Cannot reject draft"

    def publish(self, doc: "Document") -> str:
        return "Cannot publish draft. Must be approved first"

    def get_state_name(self) -> str:
        return "Draft"


class ReviewState(DocumentState):
    def edit(self, doc: "Document") -> str:
        return "Cannot edit during review"

    def review(self, doc: "Document") -> str:
        return "Already in review"

    def approve(self, doc: "Document") -> str:
        doc.set_state(ApprovedState())
        return "Document approved"

    def reject(self, doc: "Document") -> str:
        doc.set_state(DraftState())
        return "Document rejected. Returned to draft"

    def publish(self, doc: "Document") -> str:
        return "Cannot publish. Must be approved first"

    def get_state_name(self) -> str:
        return "Review"


class ApprovedState(DocumentState):
    def edit(self, doc: "Document") -> str:
        doc.set_state(DraftState())
        return "Document moved back to draft for editing"

    def review(self, doc: "Document") -> str:
        return "Already approved"

    def approve(self, doc: "Document") -> str:
        return "Already approved"

    def reject(self, doc: "Document") -> str:
        doc.set_state(DraftState())
        return "Approval revoked. Returned to draft"

    def publish(self, doc: "Document") -> str:
        doc.set_state(PublishedState())
        doc.published_at = datetime.now()
        return "Document published!"

    def get_state_name(self) -> str:
        return "Approved"


class PublishedState(DocumentState):
    def edit(self, doc: "Document") -> str:
        return "Cannot edit published document. Create new version"

    def review(self, doc: "Document") -> str:
        return "Cannot review published document"

    def approve(self, doc: "Document") -> str:
        return "Cannot approve published document"

    def reject(self, doc: "Document") -> str:
        return "Cannot reject published document"

    def publish(self, doc: "Document") -> str:
        return "Already published"

    def get_state_name(self) -> str:
        return "Published"


class Document:
    """Context for document workflow."""

    def __init__(self, title: str):
        self.title = title
        self._state: DocumentState = DraftState()
        self.created_at = datetime.now()
        self.modified_at = datetime.now()
        self.published_at: datetime | None = None

    def set_state(self, state: DocumentState) -> None:
        self._state = state

    def get_state_name(self) -> str:
        return self._state.get_state_name()

    def edit(self) -> str:
        return self._state.edit(self)

    def review(self) -> str:
        return self._state.review(self)

    def approve(self) -> str:
        return self._state.approve(self)

    def reject(self) -> str:
        return self._state.reject(self)

    def publish(self) -> str:
        return self._state.publish(self)


def main() -> None:
    print("=" * 60)
    print("State Pattern - Vending Machine Demo")
    print("=" * 60)

    # Demo 1: Normal vending machine operation
    print("\n--- Normal Operation ---")
    machine = VendingMachine()
    machine.show_products()

    print("\n--- Transaction 1 ---")
    print(machine.insert_coin(1.00))
    print(machine.insert_coin(0.50))
    print(machine.select_product("Cola"))
    print(machine.dispense())

    print("\n--- Transaction 2 (Insufficient funds) ---")
    print(machine.insert_coin(0.50))
    print(machine.select_product("Chips"))

    print("\n--- Transaction 2 (Add more money) ---")
    print(machine.insert_coin(1.00))
    print(machine.select_product("Chips"))
    print(machine.dispense())

    print("\n--- Transaction 3 (Cancel) ---")
    print(machine.insert_coin(2.00))
    print(machine.cancel())

    print("\n--- Invalid Operations ---")
    print(machine.select_product("Cola"))  # No money
    print(machine.dispense())  # Nothing selected

    # Demo 2: Document workflow
    print("\n" + "=" * 60)
    print("State Pattern - Document Workflow Demo")
    print("=" * 60)

    doc = Document("Design Proposal")

    print("\n--- Document Lifecycle ---")
    print(f"Initial state: {doc.get_state_name()}")

    print(f"\n{doc.edit()}")
    print(f"State: {doc.get_state_name()}")

    print(f"\n{doc.review()}")
    print(f"State: {doc.get_state_name()}")

    print(f"\n{doc.edit()}")  # Cannot edit during review

    print(f"\n{doc.reject()}")
    print(f"State: {doc.get_state_name()}")

    print(f"\n{doc.edit()}")
    print(f"{doc.review()}")
    print(f"State: {doc.get_state_name()}")

    print(f"\n{doc.approve()}")
    print(f"State: {doc.get_state_name()}")

    print(f"\n{doc.publish()}")
    print(f"State: {doc.get_state_name()}")

    print(f"\n{doc.edit()}")  # Cannot edit published

    print("\n" + "=" * 60)
    print("Benefits of State Pattern:")
    print("=" * 60)
    print("1. Localizes state-specific behavior")
    print("2. Makes state transitions explicit")
    print("3. State objects can be shared")
    print("4. Eliminates large conditional statements")
    print("5. Follows Single Responsibility Principle")


if __name__ == "__main__":
    main()
