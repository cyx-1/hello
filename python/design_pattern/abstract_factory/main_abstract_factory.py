# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Abstract Factory Pattern

The Abstract Factory pattern provides an interface for creating families of related
or dependent objects without specifying their concrete classes. This pattern is
particularly useful when a system needs to be independent of how its products are
created, composed, and represented.

Key Components:
- AbstractFactory: Declares interface for creating abstract products
- ConcreteFactory: Implements operations to create concrete products
- AbstractProduct: Declares interface for a type of product
- ConcreteProduct: Defines a product to be created by corresponding factory
"""

from abc import ABC, abstractmethod


# Abstract Products
class Button(ABC):
    """Abstract product for buttons."""

    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def on_click(self) -> str:
        pass


class Checkbox(ABC):
    """Abstract product for checkboxes."""

    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def toggle(self) -> str:
        pass


class TextInput(ABC):
    """Abstract product for text inputs."""

    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def get_value(self) -> str:
        pass


# Concrete Products - Windows Theme
class WindowsButton(Button):
    """Windows-styled button."""

    def render(self) -> str:
        return "[Windows Button]"

    def on_click(self) -> str:
        return "Windows button clicked with Win32 API"


class WindowsCheckbox(Checkbox):
    """Windows-styled checkbox."""

    def render(self) -> str:
        return "[Windows Checkbox ☐]"

    def toggle(self) -> str:
        return "Windows checkbox toggled with Win32 API"


class WindowsTextInput(TextInput):
    """Windows-styled text input."""

    def render(self) -> str:
        return "[Windows TextInput |_____]"

    def get_value(self) -> str:
        return "Getting value via Win32 API"


# Concrete Products - macOS Theme
class MacOSButton(Button):
    """macOS-styled button."""

    def render(self) -> str:
        return "( macOS Button )"

    def on_click(self) -> str:
        return "macOS button clicked with Cocoa framework"


class MacOSCheckbox(Checkbox):
    """macOS-styled checkbox."""

    def render(self) -> str:
        return "( macOS Checkbox ○ )"

    def toggle(self) -> str:
        return "macOS checkbox toggled with Cocoa framework"


class MacOSTextInput(TextInput):
    """macOS-styled text input."""

    def render(self) -> str:
        return "( macOS TextInput _____ )"

    def get_value(self) -> str:
        return "Getting value via Cocoa framework"


# Concrete Products - Linux Theme
class LinuxButton(Button):
    """Linux/GTK-styled button."""

    def render(self) -> str:
        return "<Linux Button>"

    def on_click(self) -> str:
        return "Linux button clicked with GTK"


class LinuxCheckbox(Checkbox):
    """Linux/GTK-styled checkbox."""

    def render(self) -> str:
        return "<Linux Checkbox □>"

    def toggle(self) -> str:
        return "Linux checkbox toggled with GTK"


class LinuxTextInput(TextInput):
    """Linux/GTK-styled text input."""

    def render(self) -> str:
        return "<Linux TextInput [___]>"

    def get_value(self) -> str:
        return "Getting value via GTK"


# Abstract Factory
class GUIFactory(ABC):
    """Abstract factory for creating GUI components."""

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

    @abstractmethod
    def create_text_input(self) -> TextInput:
        pass


# Concrete Factories
class WindowsFactory(GUIFactory):
    """Factory for creating Windows-styled GUI components."""

    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

    def create_text_input(self) -> TextInput:
        return WindowsTextInput()


class MacOSFactory(GUIFactory):
    """Factory for creating macOS-styled GUI components."""

    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

    def create_text_input(self) -> TextInput:
        return MacOSTextInput()


class LinuxFactory(GUIFactory):
    """Factory for creating Linux/GTK-styled GUI components."""

    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()

    def create_text_input(self) -> TextInput:
        return LinuxTextInput()


# Client code
class Application:
    """Application that uses GUI components without knowing their concrete types."""

    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()
        self.text_input = factory.create_text_input()

    def render_ui(self) -> None:
        print("Rendering UI components:")
        print(f"  Button: {self.button.render()}")
        print(f"  Checkbox: {self.checkbox.render()}")
        print(f"  TextInput: {self.text_input.render()}")

    def interact(self) -> None:
        print("Interacting with components:")
        print(f"  {self.button.on_click()}")
        print(f"  {self.checkbox.toggle()}")
        print(f"  {self.text_input.get_value()}")


def get_factory(os_type: str) -> GUIFactory:
    """Factory method to get the appropriate GUI factory based on OS type."""
    factories = {
        "windows": WindowsFactory,
        "macos": MacOSFactory,
        "linux": LinuxFactory,
    }
    factory_class = factories.get(os_type.lower())
    if factory_class is None:
        raise ValueError(f"Unknown OS type: {os_type}")
    return factory_class()


def main() -> None:
    print("=" * 60)
    print("Abstract Factory Pattern - Cross-Platform GUI Demo")
    print("=" * 60)

    # Demonstrate each platform
    for os_type in ["Windows", "macOS", "Linux"]:
        print(f"\n--- {os_type} Platform ---")
        factory = get_factory(os_type)
        app = Application(factory)
        app.render_ui()
        print()
        app.interact()

    print("\n" + "=" * 60)
    print("Benefits of Abstract Factory Pattern:")
    print("=" * 60)
    print("1. Ensures compatibility among products in the same family")
    print("2. Isolates concrete classes from the client code")
    print("3. Makes exchanging product families easy")
    print("4. Promotes consistency among products")


if __name__ == "__main__":
    main()
