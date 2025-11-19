# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Prototype Design Pattern Implementation

The Prototype pattern creates new objects by cloning existing instances rather
than creating new instances from scratch. This is useful when object creation
is expensive or when objects have many shared configurations.
"""

from __future__ import annotations
import copy
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Prototype(ABC):
    """Abstract base class for prototypes."""

    @abstractmethod
    def clone(self) -> Prototype:
        """Create a copy of the object."""
        pass


@dataclass
class Address:
    """Nested object to demonstrate deep cloning."""

    street: str
    city: str
    country: str

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.country}"


@dataclass
class Document(Prototype):
    """Concrete prototype representing a document."""

    title: str
    content: str
    author: str
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)

    def clone(self) -> Document:
        """Create a deep copy of the document."""
        return copy.deepcopy(self)

    def shallow_clone(self) -> Document:
        """Create a shallow copy of the document."""
        return copy.copy(self)

    def __str__(self) -> str:
        return (
            f"Document(title='{self.title}', author='{self.author}', "
            f"tags={self.tags}, metadata={self.metadata})"
        )


@dataclass
class Employee(Prototype):
    """Concrete prototype representing an employee."""

    name: str
    position: str
    department: str
    salary: float
    address: Address
    skills: list[str] = field(default_factory=list)

    def clone(self) -> Employee:
        """Create a deep copy of the employee."""
        return copy.deepcopy(self)

    def __str__(self) -> str:
        skills_str = ", ".join(self.skills) if self.skills else "None"
        return (
            f"Employee:\n"
            f"    Name: {self.name}\n"
            f"    Position: {self.position}\n"
            f"    Department: {self.department}\n"
            f"    Salary: ${self.salary:,.2f}\n"
            f"    Address: {self.address}\n"
            f"    Skills: {skills_str}"
        )


class PrototypeRegistry:
    """Registry to store and retrieve prototype instances."""

    def __init__(self) -> None:
        self._prototypes: dict[str, Prototype] = {}

    def register(self, name: str, prototype: Prototype) -> None:
        """Register a prototype with a given name."""
        self._prototypes[name] = prototype

    def unregister(self, name: str) -> None:
        """Remove a prototype from the registry."""
        del self._prototypes[name]

    def clone(self, name: str) -> Prototype:
        """Clone a registered prototype by name."""
        prototype = self._prototypes.get(name)
        if prototype is None:
            raise ValueError(f"Prototype '{name}' not found in registry")
        return prototype.clone()

    def list_prototypes(self) -> list[str]:
        """List all registered prototype names."""
        return list(self._prototypes.keys())


def main() -> None:
    """Demonstrate the Prototype pattern with documents and employees."""
    print("=" * 60)
    print("PROTOTYPE DESIGN PATTERN DEMONSTRATION")
    print("=" * 60)

    # Example 1: Document cloning
    print("\n[1] Document Cloning Example:")
    print("-" * 40)

    # Create original document
    original_doc = Document(
        title="Design Patterns Guide",
        content="This is a comprehensive guide...",
        author="John Doe",
        tags=["programming", "design", "patterns"],
        metadata={"version": "1.0", "status": "draft"},
    )
    print(f"Original: {original_doc}")
    print(f"Original ID: {id(original_doc)}")

    # Clone the document (deep copy)
    cloned_doc = original_doc.clone()
    cloned_doc.title = "Design Patterns Guide (Copy)"
    cloned_doc.tags.append("cloned")
    cloned_doc.metadata["status"] = "review"

    print(f"\nCloned:   {cloned_doc}")
    print(f"Cloned ID: {id(cloned_doc)}")
    print(f"\nOriginal after clone modification: {original_doc}")
    print("→ Note: Original remains unchanged (deep copy)")

    # Example 2: Shallow vs Deep Clone
    print("\n[2] Shallow vs Deep Clone Comparison:")
    print("-" * 40)

    base_doc = Document(
        title="Base Document",
        content="Content here",
        author="Jane Smith",
        tags=["base"],
        metadata={"type": "template"},
    )

    shallow = base_doc.shallow_clone()
    deep = base_doc.clone()

    # Modify the shallow clone's mutable attributes
    shallow.tags.append("shallow-modified")

    print(f"Base tags after shallow clone modification: {base_doc.tags}")
    print(f"Shallow clone tags: {shallow.tags}")
    print(f"Deep clone tags: {deep.tags}")
    print("→ Shallow clone shares mutable objects with original!")

    # Example 3: Employee cloning with nested objects
    print("\n[3] Employee Cloning with Nested Objects:")
    print("-" * 40)

    # Create original employee
    original_emp = Employee(
        name="Alice Johnson",
        position="Senior Developer",
        department="Engineering",
        salary=120000.00,
        address=Address("123 Tech Street", "San Francisco", "USA"),
        skills=["Python", "Java", "Kubernetes"],
    )
    print("Original Employee:")
    print(original_emp)

    # Clone and modify for a new employee
    cloned_emp = original_emp.clone()
    cloned_emp.name = "Bob Wilson"
    cloned_emp.position = "Developer"
    cloned_emp.salary = 95000.00
    cloned_emp.address.street = "456 Code Avenue"
    cloned_emp.skills.append("Docker")

    print("\nCloned Employee (modified):")
    print(cloned_emp)

    print("\nOriginal Employee (unchanged):")
    print(original_emp)
    print("→ Nested Address object was also deep copied")

    # Example 4: Prototype Registry
    print("\n[4] Prototype Registry Pattern:")
    print("-" * 40)

    registry = PrototypeRegistry()

    # Register template employees
    registry.register(
        "junior-dev",
        Employee(
            name="Template",
            position="Junior Developer",
            department="Engineering",
            salary=70000.00,
            address=Address("Office", "New York", "USA"),
            skills=["Git", "Python"],
        ),
    )

    registry.register(
        "senior-dev",
        Employee(
            name="Template",
            position="Senior Developer",
            department="Engineering",
            salary=130000.00,
            address=Address("Office", "New York", "USA"),
            skills=["Python", "Architecture", "Leadership"],
        ),
    )

    print(f"Registered prototypes: {registry.list_prototypes()}")

    # Clone from registry
    new_junior = registry.clone("junior-dev")
    if isinstance(new_junior, Employee):
        new_junior.name = "Charlie Brown"
        new_junior.address.city = "Boston"
        print("\nNew hire from 'junior-dev' template:")
        print(new_junior)

    new_senior = registry.clone("senior-dev")
    if isinstance(new_senior, Employee):
        new_senior.name = "Diana Prince"
        new_senior.skills.append("Cloud Architecture")
        print("\nNew hire from 'senior-dev' template:")
        print(new_senior)

    print("\n" + "=" * 60)
    print("Key Benefits of Prototype Pattern:")
    print("=" * 60)
    print("• Avoids expensive object creation from scratch")
    print("• Enables runtime object creation without knowing exact class")
    print("• Reduces subclassing by cloning configured instances")
    print("• Deep copy ensures complete independence of cloned objects")
    print("• Registry pattern provides convenient prototype management")
    print("=" * 60)


if __name__ == "__main__":
    main()
