// Abstract Factory Design Pattern in Rust
// Demonstrates creating families of related GUI components for different OS themes

// ============================================================================
// Abstract Products - Traits defining the interface for product families
// ============================================================================

/// Abstract product for buttons
trait Button {
    fn render(&self);
    fn on_click(&self);
}

/// Abstract product for checkboxes
trait Checkbox {
    fn render(&self);
    fn toggle(&self);
}

// ============================================================================
// Concrete Products - Windows Theme
// ============================================================================

/// Concrete Windows button
struct WindowsButton {
    label: String,
}

impl WindowsButton {
    fn new(label: &str) -> Self {
        println!("  [WindowsButton] Creating button with label: '{}'", label);
        WindowsButton {
            label: label.to_string(),
        }
    }
}

impl Button for WindowsButton {
    fn render(&self) {
        println!("  [WindowsButton] Rendering Windows-style button: [{}]", self.label);
    }

    fn on_click(&self) {
        println!("  [WindowsButton] Windows click event triggered for '{}'", self.label);
    }
}

/// Concrete Windows checkbox
struct WindowsCheckbox {
    label: String,
    checked: bool,
}

impl WindowsCheckbox {
    fn new(label: &str) -> Self {
        println!("  [WindowsCheckbox] Creating checkbox with label: '{}'", label);
        WindowsCheckbox {
            label: label.to_string(),
            checked: false,
        }
    }
}

impl Checkbox for WindowsCheckbox {
    fn render(&self) {
        let state = if self.checked { "X" } else { " " };
        println!("  [WindowsCheckbox] Rendering Windows-style checkbox: [{}] {}", state, self.label);
    }

    fn toggle(&self) {
        println!("  [WindowsCheckbox] Windows checkbox '{}' toggled", self.label);
    }
}

// ============================================================================
// Concrete Products - macOS Theme
// ============================================================================

/// Concrete macOS button
struct MacOSButton {
    label: String,
}

impl MacOSButton {
    fn new(label: &str) -> Self {
        println!("  [MacOSButton] Creating button with label: '{}'", label);
        MacOSButton {
            label: label.to_string(),
        }
    }
}

impl Button for MacOSButton {
    fn render(&self) {
        println!("  [MacOSButton] Rendering macOS-style button: ({})", self.label);
    }

    fn on_click(&self) {
        println!("  [MacOSButton] macOS click event triggered for '{}'", self.label);
    }
}

/// Concrete macOS checkbox
struct MacOSCheckbox {
    label: String,
    checked: bool,
}

impl MacOSCheckbox {
    fn new(label: &str) -> Self {
        println!("  [MacOSCheckbox] Creating checkbox with label: '{}'", label);
        MacOSCheckbox {
            label: label.to_string(),
            checked: false,
        }
    }
}

impl Checkbox for MacOSCheckbox {
    fn render(&self) {
        let state = if self.checked { "●" } else { "○" };
        println!("  [MacOSCheckbox] Rendering macOS-style checkbox: {} {}", state, self.label);
    }

    fn toggle(&self) {
        println!("  [MacOSCheckbox] macOS checkbox '{}' toggled", self.label);
    }
}

// ============================================================================
// Abstract Factory - Trait defining the factory interface
// ============================================================================

/// Abstract factory trait for creating GUI component families
trait GUIFactory {
    fn create_button(&self, label: &str) -> Box<dyn Button>;
    fn create_checkbox(&self, label: &str) -> Box<dyn Checkbox>;
    fn get_theme_name(&self) -> &str;
}

// ============================================================================
// Concrete Factories
// ============================================================================

/// Concrete factory for Windows theme
struct WindowsFactory;

impl WindowsFactory {
    fn new() -> Self {
        println!("[WindowsFactory] Initializing Windows GUI Factory");
        WindowsFactory
    }
}

impl GUIFactory for WindowsFactory {
    fn create_button(&self, label: &str) -> Box<dyn Button> {
        Box::new(WindowsButton::new(label))
    }

    fn create_checkbox(&self, label: &str) -> Box<dyn Checkbox> {
        Box::new(WindowsCheckbox::new(label))
    }

    fn get_theme_name(&self) -> &str {
        "Windows"
    }
}

/// Concrete factory for macOS theme
struct MacOSFactory;

impl MacOSFactory {
    fn new() -> Self {
        println!("[MacOSFactory] Initializing macOS GUI Factory");
        MacOSFactory
    }
}

impl GUIFactory for MacOSFactory {
    fn create_button(&self, label: &str) -> Box<dyn Button> {
        Box::new(MacOSButton::new(label))
    }

    fn create_checkbox(&self, label: &str) -> Box<dyn Checkbox> {
        Box::new(MacOSCheckbox::new(label))
    }

    fn get_theme_name(&self) -> &str {
        "macOS"
    }
}

// ============================================================================
// Client Code - Works with factories through abstract interfaces
// ============================================================================

/// Application that uses the abstract factory to create GUI components
struct Application {
    button: Box<dyn Button>,
    checkbox: Box<dyn Checkbox>,
    theme: String,
}

impl Application {
    fn new(factory: &dyn GUIFactory) -> Self {
        println!("\n[Application] Building application with {} theme", factory.get_theme_name());

        let button = factory.create_button("Submit");
        let checkbox = factory.create_checkbox("Remember me");

        Application {
            button,
            checkbox,
            theme: factory.get_theme_name().to_string(),
        }
    }

    fn render(&self) {
        println!("\n[Application] Rendering {} themed components:", self.theme);
        self.button.render();
        self.checkbox.render();
    }

    fn interact(&self) {
        println!("\n[Application] Simulating user interaction:");
        self.button.on_click();
        self.checkbox.toggle();
    }
}

/// Factory selector based on configuration
fn get_factory(os_type: &str) -> Box<dyn GUIFactory> {
    println!("\n[FactorySelector] Selecting factory for OS: {}", os_type);
    match os_type.to_lowercase().as_str() {
        "windows" => Box::new(WindowsFactory::new()),
        "macos" | "mac" => Box::new(MacOSFactory::new()),
        _ => {
            println!("[FactorySelector] Unknown OS, defaulting to Windows");
            Box::new(WindowsFactory::new())
        }
    }
}

// ============================================================================
// Main - Demonstrates the Abstract Factory pattern
// ============================================================================

fn main() {
    println!("{}", "=".repeat(60));
    println!("Abstract Factory Design Pattern - GUI Component Example");
    println!("{}", "=".repeat(60));

    // Demonstrate Windows theme
    println!("\n--- Creating Windows Application ---");
    let windows_factory = get_factory("Windows");
    let windows_app = Application::new(windows_factory.as_ref());
    windows_app.render();
    windows_app.interact();

    // Demonstrate macOS theme
    println!("\n--- Creating macOS Application ---");
    let macos_factory = get_factory("macOS");
    let macos_app = Application::new(macos_factory.as_ref());
    macos_app.render();
    macos_app.interact();

    // Demonstrate runtime factory selection
    println!("\n--- Dynamic Factory Selection ---");
    let os_configs = vec!["Windows", "macOS", "Linux"];

    for os in os_configs {
        let factory = get_factory(os);
        let button = factory.create_button("OK");
        button.render();
    }

    println!("\n{}", "=".repeat(60));
    println!("Abstract Factory Pattern demonstration complete!");
    println!("{}", "=".repeat(60));
}
