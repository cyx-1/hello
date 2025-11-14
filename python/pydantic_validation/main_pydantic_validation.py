#!/usr/bin/env python3
# /// script
# dependencies = [
#   "pydantic>=2.0",
#   "pydantic[email]>=2.0",
# ]
# ///

"""
Comprehensive Pydantic Validation Example
This script demonstrates various validation features in Pydantic v2
"""

from datetime import datetime
from typing import Optional
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ValidationError,
    field_validator,
    model_validator,
    ConfigDict,
)


# Example 1: Basic Model with Type Validation
class BasicUser(BaseModel):
    """Simple user model with basic type validation"""

    name: str
    age: int
    email: str


def demo_basic_validation():
    """Demonstrate basic type validation"""
    print("=" * 60)
    print("1. BASIC TYPE VALIDATION")
    print("=" * 60)

    # Valid data
    user = BasicUser(name="Alice", age=30, email="alice@example.com")
    print(f"✓ Valid user created: {user}")
    print(f"  Name: {user.name}, Age: {user.age}, Email: {user.email}")

    # Type coercion - string to int
    user2 = BasicUser(name="Bob", age="25", email="bob@example.com")
    print(f"\n✓ Type coercion works - age='25' (str) → {user2.age} (int)")

    # Validation error - invalid type
    try:
        BasicUser(name="Charlie", age="invalid", email="charlie@example.com")
    except ValidationError as e:
        print("\n✗ Validation failed for age='invalid':")
        print(f"  Error count: {e.error_count()}")
        print(f"  Error: {e.errors()[0]['msg']}")

    print()


# Example 2: Field Constraints
class ConstrainedUser(BaseModel):
    """User model with field constraints"""

    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=0, le=150)  # ge: greater than or equal, le: less than or equal
    email: EmailStr  # Built-in email validation
    score: float = Field(gt=0.0, lt=100.0)  # gt: greater than, lt: less than
    username: str = Field(pattern=r"^[a-zA-Z0-9_]+$")  # Regex pattern


def demo_field_constraints():
    """Demonstrate field-level constraints"""
    print("=" * 60)
    print("2. FIELD CONSTRAINTS")
    print("=" * 60)

    # Valid data
    user = ConstrainedUser(
        name="Alice Johnson",
        age=30,
        email="alice@example.com",
        score=85.5,
        username="alice_123",
    )
    print(f"✓ Valid user: {user.name}, score={user.score}")

    # Test min_length constraint
    try:
        user = ConstrainedUser(
            name="A", age=30, email="alice@example.com", score=85.5, username="alice"
        )
    except ValidationError as e:
        print("\n✗ Name too short ('A'):")
        print(f"  {e.errors()[0]['msg']}")

    # Test age constraint
    try:
        user = ConstrainedUser(
            name="Alice",
            age=200,
            email="alice@example.com",
            score=85.5,
            username="alice",
        )
    except ValidationError as e:
        print("\n✗ Age too high (200):")
        print(f"  {e.errors()[0]['msg']}")

    # Test email validation
    try:
        user = ConstrainedUser(
            name="Alice", age=30, email="invalid-email", score=85.5, username="alice"
        )
    except ValidationError as e:
        print("\n✗ Invalid email format ('invalid-email'):")
        print(f"  {e.errors()[0]['msg']}")

    # Test pattern validation
    try:
        user = ConstrainedUser(
            name="Alice",
            age=30,
            email="alice@example.com",
            score=85.5,
            username="alice-invalid!",
        )
    except ValidationError as e:
        print("\n✗ Username contains invalid characters ('alice-invalid!'):")
        print(f"  {e.errors()[0]['msg']}")

    print()


# Example 3: Field Validators
class Product(BaseModel):
    """Product model with custom field validators"""

    name: str
    price: float
    quantity: int
    sku: str

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        """Validate that name is not just whitespace"""
        if not v.strip():
            raise ValueError("Name cannot be empty or just whitespace")
        return v.strip().title()  # Clean and capitalize

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        """Validate that price is positive"""
        if v <= 0:
            raise ValueError("Price must be positive")
        return round(v, 2)  # Round to 2 decimal places

    @field_validator("sku")
    @classmethod
    def sku_must_be_uppercase(cls, v: str) -> str:
        """Convert SKU to uppercase"""
        return v.upper()


def demo_field_validators():
    """Demonstrate custom field validators"""
    print("=" * 60)
    print("3. CUSTOM FIELD VALIDATORS")
    print("=" * 60)

    # Valid product with transformations
    product = Product(
        name="  laptop computer  ", price=999.999, quantity=10, sku="prod-123"
    )
    print("✓ Product created with transformations:")
    print(f"  Name: '{product.name}' (trimmed and titled)")
    print(f"  Price: ${product.price} (rounded to 2 decimals)")
    print(f"  SKU: '{product.sku}' (uppercase)")

    # Test empty name
    try:
        product = Product(name="   ", price=100, quantity=5, sku="SKU-001")
    except ValidationError as e:
        print("\n✗ Empty name validation:")
        print(f"  {e.errors()[0]['msg']}")

    # Test negative price
    try:
        product = Product(name="Mouse", price=-10, quantity=5, sku="SKU-002")
    except ValidationError as e:
        print("\n✗ Negative price validation:")
        print(f"  {e.errors()[0]['msg']}")

    print()


# Example 4: Model Validators
class Order(BaseModel):
    """Order model with model-level validation"""

    order_id: str
    items_count: int
    total_price: float
    discount: float = 0.0
    final_price: Optional[float] = None

    @model_validator(mode="after")
    def calculate_final_price(self) -> "Order":
        """Calculate final price after discount"""
        if self.discount > self.total_price:
            raise ValueError("Discount cannot exceed total price")

        if self.discount < 0:
            raise ValueError("Discount cannot be negative")

        # Calculate final price
        self.final_price = self.total_price - self.discount
        return self

    @model_validator(mode="after")
    def validate_items_and_price(self) -> "Order":
        """Ensure items count matches price logic"""
        if self.items_count <= 0:
            raise ValueError("Order must have at least one item")

        if self.total_price <= 0:
            raise ValueError("Total price must be positive")

        return self


def demo_model_validators():
    """Demonstrate model-level validators"""
    print("=" * 60)
    print("4. MODEL VALIDATORS")
    print("=" * 60)

    # Valid order
    order = Order(order_id="ORD-001", items_count=3, total_price=150.0, discount=15.0)
    print("✓ Order created:")
    print(f"  Order ID: {order.order_id}")
    print(f"  Total: ${order.total_price}, Discount: ${order.discount}")
    print(f"  Final Price: ${order.final_price} (calculated automatically)")

    # Test discount exceeds total
    try:
        order = Order(
            order_id="ORD-002", items_count=2, total_price=100.0, discount=150.0
        )
    except ValidationError as e:
        print("\n✗ Discount exceeds total price:")
        print(f"  {e.errors()[0]['msg']}")

    # Test negative items count
    try:
        order = Order(
            order_id="ORD-003", items_count=0, total_price=100.0, discount=10.0
        )
    except ValidationError as e:
        print("\n✗ Invalid items count (0):")
        print(f"  {e.errors()[0]['msg']}")

    print()


# Example 5: Optional Fields and Defaults
class UserProfile(BaseModel):
    """User profile with optional fields and defaults"""

    username: str
    email: EmailStr
    full_name: Optional[str] = None
    age: Optional[int] = None
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    tags: list[str] = Field(default_factory=list)
    metadata: dict[str, str] = Field(default_factory=dict)


def demo_optional_and_defaults():
    """Demonstrate optional fields and default values"""
    print("=" * 60)
    print("5. OPTIONAL FIELDS AND DEFAULTS")
    print("=" * 60)

    # Minimal profile
    profile1 = UserProfile(username="alice", email="alice@example.com")
    print("✓ Minimal profile:")
    print(f"  Username: {profile1.username}")
    print(f"  Full name: {profile1.full_name} (optional, not provided)")
    print(f"  Is active: {profile1.is_active} (default=True)")
    print(f"  Tags: {profile1.tags} (default empty list)")

    # Full profile
    profile2 = UserProfile(
        username="bob",
        email="bob@example.com",
        full_name="Bob Smith",
        age=35,
        is_active=False,
        tags=["admin", "developer"],
        metadata={"department": "Engineering"},
    )
    print("\n✓ Full profile:")
    print(f"  Username: {profile2.username}")
    print(f"  Full name: {profile2.full_name}")
    print(f"  Age: {profile2.age}")
    print(f"  Is active: {profile2.is_active}")
    print(f"  Tags: {profile2.tags}")
    print(f"  Metadata: {profile2.metadata}")

    print()


# Example 6: Nested Models
class Address(BaseModel):
    """Address model"""

    street: str
    city: str
    state: str = Field(pattern=r"^[A-Z]{2}$")
    zip_code: str = Field(pattern=r"^\d{5}$")


class Company(BaseModel):
    """Company with nested address"""

    name: str
    address: Address
    employees: list[str] = Field(min_length=1)


def demo_nested_models():
    """Demonstrate nested model validation"""
    print("=" * 60)
    print("6. NESTED MODELS")
    print("=" * 60)

    # Valid nested model
    company = Company(
        name="Tech Corp",
        address=Address(
            street="123 Main St", city="San Francisco", state="CA", zip_code="94105"
        ),
        employees=["Alice", "Bob", "Charlie"],
    )
    print("✓ Company created:")
    print(f"  Name: {company.name}")
    print(
        f"  Address: {company.address.street}, {company.address.city}, {company.address.state}"
    )
    print(f"  Employees: {company.employees}")

    # Invalid nested address
    try:
        company = Company(
            name="Tech Corp",
            address=Address(
                street="123 Main St",
                city="San Francisco",
                state="California",  # Should be 2 letters
                zip_code="94105",
            ),
            employees=["Alice"],
        )
    except ValidationError as e:
        print("\n✗ Invalid state format ('California'):")
        print(f"  {e.errors()[0]['msg']}")
        print(f"  Location: {' -> '.join(str(x) for x in e.errors()[0]['loc'])}")

    # Invalid zip code
    try:
        company = Company(
            name="Tech Corp",
            address=Address(
                street="123 Main St",
                city="San Francisco",
                state="CA",
                zip_code="9410",  # Should be 5 digits
            ),
            employees=["Alice"],
        )
    except ValidationError as e:
        print("\n✗ Invalid zip code format ('9410'):")
        print(f"  {e.errors()[0]['msg']}")
        print(f"  Location: {' -> '.join(str(x) for x in e.errors()[0]['loc'])}")

    print()


# Example 7: Complex Validation Error Handling
class ComplexModel(BaseModel):
    """Model to demonstrate comprehensive error handling"""

    model_config = ConfigDict(str_strip_whitespace=True)

    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(ge=18, le=100)
    tags: list[str] = Field(min_length=1, max_length=5)


def demo_error_handling():
    """Demonstrate comprehensive error handling"""
    print("=" * 60)
    print("7. COMPREHENSIVE ERROR HANDLING")
    print("=" * 60)

    # Multiple validation errors
    try:
        ComplexModel(id=-1, name="AB", email="invalid-email", age=15, tags=[])
    except ValidationError as e:
        print("✗ Multiple validation errors detected:")
        print(f"  Total errors: {e.error_count()}")
        print()
        for i, error in enumerate(e.errors(), 1):
            field = error["loc"][0]
            msg = error["msg"]
            input_val = error.get("input")
            print(f"  Error {i} - Field '{field}':")
            print(f"    Input: {input_val}")
            print(f"    Message: {msg}")

        # Show JSON representation
        print("\n  JSON representation:")
        import json

        print(f"  {json.dumps(e.errors(), indent=4)}")

    print()


def main():
    """Run all demonstrations"""
    print("\n" + "=" * 60)
    print("PYDANTIC VALIDATION COMPREHENSIVE EXAMPLES")
    print("=" * 60 + "\n")

    demo_basic_validation()
    demo_field_constraints()
    demo_field_validators()
    demo_model_validators()
    demo_optional_and_defaults()
    demo_nested_models()
    demo_error_handling()

    print("=" * 60)
    print("ALL DEMONSTRATIONS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
