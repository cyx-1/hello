# Abstract Factory Pattern

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

## How to Run

```bash
cd java/abstract_factory
mvn compile exec:java
```

## Key Source Code

### Abstract Products (Lines 15-25)
```java
interface Button {
    void render();
    void onClick();
}

interface Checkbox {
    void render();
    void toggle();
}

interface TextField {
    void render();
    void setText(String text);
}
```

### Concrete Products - Windows Family (Lines 28-59)
```java
class WindowsButton implements Button {
    @Override
    public void render() {
        System.out.println("  [WindowsButton] Rendering a Windows-style button");
    }
    // ...
}
```

### Abstract Factory Interface (Lines 117-121)
```java
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
    TextField createTextField();
}
```

### Concrete Factory (Lines 124-139)
```java
class WindowsFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new WindowsButton();
    }
    // Creates family of Windows-style components
}
```

### Client Code (Lines 167-182)
```java
class Application {
    public Application(GUIFactory factory) {
        button = factory.createButton();
        checkbox = factory.createCheckbox();
        textField = factory.createTextField();
    }
}
```

## Program Output

```
=== Abstract Factory Pattern Demonstration ===

--- Creating Windows UI Components ---
Rendering Windows UI:
  [WindowsButton] Rendering a Windows-style button
  [WindowsCheckbox] Rendering a Windows-style checkbox
  [WindowsTextField] Rendering a Windows-style text field

Interacting with Windows UI:
  [WindowsButton] Windows button clicked!
  [WindowsCheckbox] Checkbox is now: checked
  [WindowsTextField] Text set to: Hello, World!

--- Creating macOS UI Components ---
Rendering macOS UI:
  [MacOSButton] Rendering a macOS-style button
  [MacOSCheckbox] Rendering a macOS-style checkbox
  [MacOSTextField] Rendering a macOS-style text field

Interacting with macOS UI:
  [MacOSButton] macOS button clicked!
  [MacOSCheckbox] Checkbox is now: checked
  [MacOSTextField] Text set to: Hello, World!

--- Creating Linux UI Components ---
Rendering Linux UI:
  [LinuxButton] Rendering a Linux GTK-style button
  [LinuxCheckbox] Rendering a Linux GTK-style checkbox
  [LinuxTextField] Rendering a Linux GTK-style text field

Interacting with Linux UI:
  [LinuxButton] Linux button clicked!
  [LinuxCheckbox] Checkbox is now: checked
  [LinuxTextField] Text set to: Hello, World!

--- Dynamic Factory Selection ---
Detected Linux/Other - using LinuxFactory

Rendering native UI for current OS:
  [LinuxButton] Rendering a Linux GTK-style button
  [LinuxCheckbox] Rendering a Linux GTK-style checkbox
  [LinuxTextField] Rendering a Linux GTK-style text field

=== Summary ===
Abstract Factory pattern benefits:
  - Ensures product compatibility within a family
  - Isolates concrete classes from client code
  - Makes exchanging product families easy
  - Promotes consistency among products
```

## Output Analysis

| Output Line | Source Code Reference | Explanation |
|-------------|----------------------|-------------|
| `[WindowsButton] Rendering...` | Line 30 | WindowsButton.render() creates Windows-style button |
| `[MacOSButton] macOS button clicked!` | Line 68 | MacOSButton.onClick() demonstrates family-specific behavior |
| `Detected Linux/Other...` | Lines 206-214 | Dynamic factory selection based on OS property |
| Button/Checkbox/TextField together | Lines 174-176 | Client uses abstract factory to create complete UI family |

## Pattern Benefits

1. **Product Family Consistency**: All UI components from one factory match each other
2. **Isolation**: Client code works with abstract interfaces, not concrete classes
3. **Easy Switching**: Change from Windows to macOS UI by switching the factory
4. **Open/Closed Principle**: Add new UI families without modifying existing code

## Requirements

- Java 17 or higher
- Maven 3.x
