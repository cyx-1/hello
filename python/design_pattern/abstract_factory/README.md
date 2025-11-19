# Abstract Factory Pattern

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. This is particularly useful when a system needs to support multiple platforms or themes where all components must be consistent within each family.

**Requires: Python 3.10+** (for type hints with `|` union syntax and modern ABC features)

## Key Components

- **AbstractFactory** (`GUIFactory`): Declares interface for creating abstract products
- **ConcreteFactory** (`WindowsFactory`, `MacOSFactory`, `LinuxFactory`): Implements operations to create concrete products
- **AbstractProduct** (`Button`, `Checkbox`, `TextInput`): Declares interface for a type of product
- **ConcreteProduct**: Platform-specific implementations of each product

## Source Code Highlights

### Abstract Products - Define the Interface

```python:main_abstract_factory.py startLine=24 endLine=57
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
```

### Concrete Products - Platform-Specific Implementations

```python:main_abstract_factory.py startLine=60 endLine=89
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
```

### Abstract Factory - Declares Creation Interface

```python:main_abstract_factory.py startLine=153 endLine=167
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
```

### Concrete Factory - Creates Family of Products

```python:main_abstract_factory.py startLine=170 endLine=182
# Concrete Factories
class WindowsFactory(GUIFactory):
    """Factory for creating Windows-styled GUI components."""

    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

    def create_text_input(self) -> TextInput:
        return WindowsTextInput()
```

### Client Code - Uses Factory Without Knowing Concrete Types

```python:main_abstract_factory.py startLine=210 endLine=230
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
```

## Program Output

```
============================================================
Abstract Factory Pattern - Cross-Platform GUI Demo
============================================================

--- Windows Platform ---
Rendering UI components:
  Button: [Windows Button]
  Checkbox: [Windows Checkbox ☐]
  TextInput: [Windows TextInput |_____]

Interacting with components:
  Windows button clicked with Win32 API
  Windows checkbox toggled with Win32 API
  Getting value via Win32 API

--- macOS Platform ---
Rendering UI components:
  Button: ( macOS Button )
  Checkbox: ( macOS Checkbox ○ )
  TextInput: ( macOS TextInput _____ )

Interacting with components:
  macOS button clicked with Cocoa framework
  macOS checkbox toggled with Cocoa framework
  Getting value via Cocoa framework

--- Linux Platform ---
Rendering UI components:
  Button: <Linux Button>
  Checkbox: <Linux Checkbox □>
  TextInput: <Linux TextInput [___]>

Interacting with components:
  Linux button clicked with GTK
  Linux checkbox toggled with GTK
  Getting value via GTK

============================================================
Benefits of Abstract Factory Pattern:
============================================================
1. Ensures compatibility among products in the same family
2. Isolates concrete classes from the client code
3. Makes exchanging product families easy
4. Promotes consistency among products
```

## Output Annotations

1. **Lines 214-218** - The `Application.__init__` method receives a factory and creates all three components. This is why each platform section shows a Button, Checkbox, and TextInput rendered together.

2. **Lines 220-224** - The `render_ui()` method calls `render()` on each component, producing the visual representation (e.g., `[Windows Button]` from line 65, `( macOS Button )` from line 96).

3. **Lines 226-230** - The `interact()` method calls the action methods (`on_click()`, `toggle()`, `get_value()`), producing the interaction messages that reference the underlying platform API (e.g., "Win32 API", "Cocoa framework", "GTK").

4. **Lines 252-258** - The main loop iterates through each platform, demonstrating that the same `Application` class works identically with any factory - the only difference is which concrete factory is passed in.

5. **Visual consistency** - Notice how all Windows components use `[brackets]`, macOS uses `(parentheses)`, and Linux uses `<angle brackets>`. This consistency within each family is a key benefit of the pattern.

## Running the Code

```bash
uv run python main_abstract_factory.py
```
