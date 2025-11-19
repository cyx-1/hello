/**
 * Abstract Factory Design Pattern in TypeScript
 *
 * The Abstract Factory pattern provides an interface for creating families of
 * related or dependent objects without specifying their concrete classes.
 * It encapsulates a group of individual factories with a common theme.
 */

// ============================================================
// Abstract Product Interfaces
// ============================================================

// Abstract Product A - Button
interface Button {
    render(): void;
    onClick(callback: () => void): void;
}

// Abstract Product B - Checkbox
interface Checkbox {
    render(): void;
    toggle(): void;
    isChecked(): boolean;
}

// Abstract Product C - TextField
interface TextField {
    render(): void;
    setValue(value: string): void;
    getValue(): string;
}

// ============================================================
// Concrete Products - Light Theme
// ============================================================

class LightButton implements Button {
    private name: string;

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 38] LightButton: Created '${name}' with light theme styling`);
    }

    render(): void {
        console.log(`[Line 42] LightButton: Rendering '${this.name}' with white background and dark text`);
    }

    onClick(callback: () => void): void {
        console.log(`[Line 46] LightButton: '${this.name}' clicked - executing callback`);
        callback();
    }
}

class LightCheckbox implements Checkbox {
    private name: string;
    private checked: boolean = false;

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 56] LightCheckbox: Created '${name}' with light theme styling`);
    }

    render(): void {
        const state = this.checked ? "checked" : "unchecked";
        console.log(`[Line 61] LightCheckbox: Rendering '${this.name}' (${state}) with light gray border`);
    }

    toggle(): void {
        this.checked = !this.checked;
        console.log(`[Line 66] LightCheckbox: '${this.name}' toggled to ${this.checked}`);
    }

    isChecked(): boolean {
        return this.checked;
    }
}

class LightTextField implements TextField {
    private name: string;
    private value: string = "";

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 79] LightTextField: Created '${name}' with light theme styling`);
    }

    render(): void {
        console.log(`[Line 83] LightTextField: Rendering '${this.name}' with white background and dark border`);
    }

    setValue(value: string): void {
        this.value = value;
        console.log(`[Line 88] LightTextField: '${this.name}' value set to '${value}'`);
    }

    getValue(): string {
        return this.value;
    }
}

// ============================================================
// Concrete Products - Dark Theme
// ============================================================

class DarkButton implements Button {
    private name: string;

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 104] DarkButton: Created '${name}' with dark theme styling`);
    }

    render(): void {
        console.log(`[Line 108] DarkButton: Rendering '${this.name}' with dark background and light text`);
    }

    onClick(callback: () => void): void {
        console.log(`[Line 112] DarkButton: '${this.name}' clicked - executing callback`);
        callback();
    }
}

class DarkCheckbox implements Checkbox {
    private name: string;
    private checked: boolean = false;

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 122] DarkCheckbox: Created '${name}' with dark theme styling`);
    }

    render(): void {
        const state = this.checked ? "checked" : "unchecked";
        console.log(`[Line 127] DarkCheckbox: Rendering '${this.name}' (${state}) with light border on dark`);
    }

    toggle(): void {
        this.checked = !this.checked;
        console.log(`[Line 132] DarkCheckbox: '${this.name}' toggled to ${this.checked}`);
    }

    isChecked(): boolean {
        return this.checked;
    }
}

class DarkTextField implements TextField {
    private name: string;
    private value: string = "";

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 145] DarkTextField: Created '${name}' with dark theme styling`);
    }

    render(): void {
        console.log(`[Line 149] DarkTextField: Rendering '${this.name}' with dark background and light border`);
    }

    setValue(value: string): void {
        this.value = value;
        console.log(`[Line 154] DarkTextField: '${this.name}' value set to '${value}'`);
    }

    getValue(): string {
        return this.value;
    }
}

// ============================================================
// Abstract Factory Interface
// ============================================================

interface UIComponentFactory {
    createButton(name: string): Button;
    createCheckbox(name: string): Checkbox;
    createTextField(name: string): TextField;
    getThemeName(): string;
}

// ============================================================
// Concrete Factories
// ============================================================

class LightThemeFactory implements UIComponentFactory {
    constructor() {
        console.log("[Line 177] LightThemeFactory: Initialized - will create light-themed components");
    }

    createButton(name: string): Button {
        console.log(`[Line 181] LightThemeFactory: Creating light-themed button '${name}'`);
        return new LightButton(name);
    }

    createCheckbox(name: string): Checkbox {
        console.log(`[Line 186] LightThemeFactory: Creating light-themed checkbox '${name}'`);
        return new LightCheckbox(name);
    }

    createTextField(name: string): TextField {
        console.log(`[Line 191] LightThemeFactory: Creating light-themed text field '${name}'`);
        return new LightTextField(name);
    }

    getThemeName(): string {
        return "Light Theme";
    }
}

class DarkThemeFactory implements UIComponentFactory {
    constructor() {
        console.log("[Line 202] DarkThemeFactory: Initialized - will create dark-themed components");
    }

    createButton(name: string): Button {
        console.log(`[Line 206] DarkThemeFactory: Creating dark-themed button '${name}'`);
        return new DarkButton(name);
    }

    createCheckbox(name: string): Checkbox {
        console.log(`[Line 211] DarkThemeFactory: Creating dark-themed checkbox '${name}'`);
        return new DarkCheckbox(name);
    }

    createTextField(name: string): TextField {
        console.log(`[Line 216] DarkThemeFactory: Creating dark-themed text field '${name}'`);
        return new DarkTextField(name);
    }

    getThemeName(): string {
        return "Dark Theme";
    }
}

// ============================================================
// Client Code
// ============================================================

// Application class that uses the abstract factory
class Application {
    private factory: UIComponentFactory;
    private button: Button;
    private checkbox: Checkbox;
    private textField: TextField;

    constructor(factory: UIComponentFactory) {
        console.log(`\n[Line 235] Application: Initializing with ${factory.getThemeName()}`);
        this.factory = factory;

        // Create UI components using the factory
        this.button = this.factory.createButton("Submit");
        this.checkbox = this.factory.createCheckbox("Remember Me");
        this.textField = this.factory.createTextField("Username");
    }

    render(): void {
        console.log(`\n[Line 244] Application: Rendering all components`);
        this.button.render();
        this.checkbox.render();
        this.textField.render();
    }

    simulateUserInteraction(): void {
        console.log(`\n[Line 251] Application: Simulating user interaction`);

        // Set text field value
        this.textField.setValue("john_doe");

        // Toggle checkbox
        this.checkbox.toggle();

        // Click button with callback
        this.button.onClick(() => {
            console.log(`[Line 261] Application: Form submitted with username '${this.textField.getValue()}', remember: ${this.checkbox.isChecked()}`);
        });
    }
}

// Factory selector - determines which factory to use based on configuration
function getFactory(theme: string): UIComponentFactory {
    console.log(`[Line 268] getFactory: Requested theme '${theme}'`);

    switch (theme.toLowerCase()) {
        case "light":
            return new LightThemeFactory();
        case "dark":
            return new DarkThemeFactory();
        default:
            console.log(`[Line 276] getFactory: Unknown theme '${theme}', defaulting to light`);
            return new LightThemeFactory();
    }
}

// ============================================================
// Demonstration
// ============================================================

function main(): void {
    console.log("=== Abstract Factory Pattern Demonstration ===");
    console.log("Creating UI components with different themes");

    // Demo 1: Light Theme
    console.log("\n--- Demo 1: Light Theme Application ---");
    const lightFactory = getFactory("light");
    const lightApp = new Application(lightFactory);
    lightApp.render();
    lightApp.simulateUserInteraction();

    // Demo 2: Dark Theme
    console.log("\n\n--- Demo 2: Dark Theme Application ---");
    const darkFactory = getFactory("dark");
    const darkApp = new Application(darkFactory);
    darkApp.render();
    darkApp.simulateUserInteraction();

    // Demo 3: Using factories directly
    console.log("\n\n--- Demo 3: Direct Factory Usage ---");
    const factories: UIComponentFactory[] = [
        new LightThemeFactory(),
        new DarkThemeFactory()
    ];

    factories.forEach((factory, index) => {
        console.log(`\n[Line 307] Creating components with factory ${index + 1} (${factory.getThemeName()})`);
        const btn = factory.createButton("Action");
        const chk = factory.createCheckbox("Option");
        btn.render();
        chk.render();
        chk.toggle();
    });

    // Demo 4: Runtime theme switching
    console.log("\n\n--- Demo 4: Runtime Theme Selection ---");
    const userPreference = "dark";
    console.log(`[Line 318] User preference: '${userPreference}'`);
    const selectedFactory = getFactory(userPreference);
    const customButton = selectedFactory.createButton("Custom Action");
    customButton.render();
    customButton.onClick(() => {
        console.log("[Line 323] Custom action executed!");
    });

    console.log("\n=== End of Demonstration ===");
}

main();
