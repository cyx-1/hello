/**
 * Comprehensive demonstration of the Abstract Factory Pattern in Java
 *
 * The Abstract Factory pattern provides an interface for creating families
 * of related or dependent objects without specifying their concrete classes.
 */

// Abstract Products
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

// Concrete Products - Windows Family
class WindowsButton implements Button {
    @Override
    public void render() {
        System.out.println("  [WindowsButton] Rendering a Windows-style button");
    }

    @Override
    public void onClick() {
        System.out.println("  [WindowsButton] Windows button clicked!");
    }
}

class WindowsCheckbox implements Checkbox {
    private boolean checked = false;

    @Override
    public void render() {
        System.out.println("  [WindowsCheckbox] Rendering a Windows-style checkbox");
    }

    @Override
    public void toggle() {
        checked = !checked;
        System.out.println("  [WindowsCheckbox] Checkbox is now: " + (checked ? "checked" : "unchecked"));
    }
}

class WindowsTextField implements TextField {
    @Override
    public void render() {
        System.out.println("  [WindowsTextField] Rendering a Windows-style text field");
    }

    @Override
    public void setText(String text) {
        System.out.println("  [WindowsTextField] Text set to: " + text);
    }
}

// Concrete Products - macOS Family
class MacOSButton implements Button {
    @Override
    public void render() {
        System.out.println("  [MacOSButton] Rendering a macOS-style button");
    }

    @Override
    public void onClick() {
        System.out.println("  [MacOSButton] macOS button clicked!");
    }
}

class MacOSCheckbox implements Checkbox {
    private boolean checked = false;

    @Override
    public void render() {
        System.out.println("  [MacOSCheckbox] Rendering a macOS-style checkbox");
    }

    @Override
    public void toggle() {
        checked = !checked;
        System.out.println("  [MacOSCheckbox] Checkbox is now: " + (checked ? "checked" : "unchecked"));
    }
}

class MacOSTextField implements TextField {
    @Override
    public void render() {
        System.out.println("  [MacOSTextField] Rendering a macOS-style text field");
    }

    @Override
    public void setText(String text) {
        System.out.println("  [MacOSTextField] Text set to: " + text);
    }
}

// Concrete Products - Linux Family
class LinuxButton implements Button {
    @Override
    public void render() {
        System.out.println("  [LinuxButton] Rendering a Linux GTK-style button");
    }

    @Override
    public void onClick() {
        System.out.println("  [LinuxButton] Linux button clicked!");
    }
}

class LinuxCheckbox implements Checkbox {
    private boolean checked = false;

    @Override
    public void render() {
        System.out.println("  [LinuxCheckbox] Rendering a Linux GTK-style checkbox");
    }

    @Override
    public void toggle() {
        checked = !checked;
        System.out.println("  [LinuxCheckbox] Checkbox is now: " + (checked ? "checked" : "unchecked"));
    }
}

class LinuxTextField implements TextField {
    @Override
    public void render() {
        System.out.println("  [LinuxTextField] Rendering a Linux GTK-style text field");
    }

    @Override
    public void setText(String text) {
        System.out.println("  [LinuxTextField] Text set to: " + text);
    }
}

// Abstract Factory
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
    TextField createTextField();
}

// Concrete Factories
class WindowsFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }

    @Override
    public TextField createTextField() {
        return new WindowsTextField();
    }
}

class MacOSFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new MacOSButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new MacOSCheckbox();
    }

    @Override
    public TextField createTextField() {
        return new MacOSTextField();
    }
}

class LinuxFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new LinuxButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new LinuxCheckbox();
    }

    @Override
    public TextField createTextField() {
        return new LinuxTextField();
    }
}

// Client class that uses the factory
class Application {
    private Button button;
    private Checkbox checkbox;
    private TextField textField;

    public Application(GUIFactory factory) {
        button = factory.createButton();
        checkbox = factory.createCheckbox();
        textField = factory.createTextField();
    }

    public void renderUI() {
        button.render();
        checkbox.render();
        textField.render();
    }

    public void interact() {
        button.onClick();
        checkbox.toggle();
        textField.setText("Hello, World!");
    }
}

public class MainAbstractFactory {
    public static void main(String[] args) {
        System.out.println("=== Abstract Factory Pattern Demonstration ===\n");

        // Demonstrate with Windows Factory
        System.out.println("--- Creating Windows UI Components ---");
        GUIFactory windowsFactory = new WindowsFactory();
        Application windowsApp = new Application(windowsFactory);
        System.out.println("Rendering Windows UI:");
        windowsApp.renderUI();
        System.out.println("\nInteracting with Windows UI:");
        windowsApp.interact();
        System.out.println();

        // Demonstrate with macOS Factory
        System.out.println("--- Creating macOS UI Components ---");
        GUIFactory macFactory = new MacOSFactory();
        Application macApp = new Application(macFactory);
        System.out.println("Rendering macOS UI:");
        macApp.renderUI();
        System.out.println("\nInteracting with macOS UI:");
        macApp.interact();
        System.out.println();

        // Demonstrate with Linux Factory
        System.out.println("--- Creating Linux UI Components ---");
        GUIFactory linuxFactory = new LinuxFactory();
        Application linuxApp = new Application(linuxFactory);
        System.out.println("Rendering Linux UI:");
        linuxApp.renderUI();
        System.out.println("\nInteracting with Linux UI:");
        linuxApp.interact();
        System.out.println();

        // Demonstrate factory selection based on configuration
        System.out.println("--- Dynamic Factory Selection ---");
        String osName = System.getProperty("os.name").toLowerCase();
        GUIFactory factory;

        if (osName.contains("windows")) {
            factory = new WindowsFactory();
            System.out.println("Detected Windows - using WindowsFactory");
        } else if (osName.contains("mac")) {
            factory = new MacOSFactory();
            System.out.println("Detected macOS - using MacOSFactory");
        } else {
            factory = new LinuxFactory();
            System.out.println("Detected Linux/Other - using LinuxFactory");
        }

        Application nativeApp = new Application(factory);
        System.out.println("\nRendering native UI for current OS:");
        nativeApp.renderUI();

        System.out.println("\n=== Summary ===");
        System.out.println("Abstract Factory pattern benefits:");
        System.out.println("  - Ensures product compatibility within a family");
        System.out.println("  - Isolates concrete classes from client code");
        System.out.println("  - Makes exchanging product families easy");
        System.out.println("  - Promotes consistency among products");
    }
}
