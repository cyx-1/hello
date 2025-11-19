# Abstract Factory Design Pattern in Rust

## Description

The **Abstract Factory** pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. This example demonstrates the pattern through a GUI component factory that creates themed buttons and checkboxes for different operating systems (Windows and macOS).

### Key Concepts

- **Abstract Factory**: A trait defining methods for creating abstract products
- **Concrete Factory**: Implementations that create concrete products for a specific theme
- **Abstract Product**: Traits defining interfaces for product types
- **Concrete Product**: Specific implementations of products for each theme
- **Client**: Code that uses factories through abstract interfaces

## Source Code

```rust
  1  // Abstract Factory Design Pattern in Rust
  2  // Demonstrates creating families of related GUI components for different OS themes
  3
  4  // ============================================================================
  5  // Abstract Products - Traits defining the interface for product families
  6  // ============================================================================
  7
  8  /// Abstract product for buttons
  9  trait Button {
 10      fn render(&self);
 11      fn on_click(&self);
 12  }
 13
 14  /// Abstract product for checkboxes
 15  trait Checkbox {
 16      fn render(&self);
 17      fn toggle(&self);
 18  }
 19
 20  // ============================================================================
 21  // Concrete Products - Windows Theme
 22  // ============================================================================
 23
 24  /// Concrete Windows button
 25  struct WindowsButton {
 26      label: String,
 27  }
 28
 29  impl WindowsButton {
 30      fn new(label: &str) -> Self {
 31          println!("  [WindowsButton] Creating button with label: '{}'", label);
 32          WindowsButton {
 33              label: label.to_string(),
 34          }
 35      }
 36  }
 37
 38  impl Button for WindowsButton {
 39      fn render(&self) {
 40          println!("  [WindowsButton] Rendering Windows-style button: [{}]", self.label);
 41      }
 42
 43      fn on_click(&self) {
 44          println!("  [WindowsButton] Windows click event triggered for '{}'", self.label);
 45      }
 46  }
 47
 48  /// Concrete Windows checkbox
 49  struct WindowsCheckbox {
 50      label: String,
 51      checked: bool,
 52  }
 53
 54  impl WindowsCheckbox {
 55      fn new(label: &str) -> Self {
 56          println!("  [WindowsCheckbox] Creating checkbox with label: '{}'", label);
 57          WindowsCheckbox {
 58              label: label.to_string(),
 59              checked: false,
 60          }
 61      }
 62  }
 63
 64  impl Checkbox for WindowsCheckbox {
 65      fn render(&self) {
 66          let state = if self.checked { "X" } else { " " };
 67          println!("  [WindowsCheckbox] Rendering Windows-style checkbox: [{}] {}", state, self.label);
 68      }
 69
 70      fn toggle(&self) {
 71          println!("  [WindowsCheckbox] Windows checkbox '{}' toggled", self.label);
 72      }
 73  }
 74
 75  // ============================================================================
 76  // Concrete Products - macOS Theme
 77  // ============================================================================
 78
 79  /// Concrete macOS button
 80  struct MacOSButton {
 81      label: String,
 82  }
 83
 84  impl MacOSButton {
 85      fn new(label: &str) -> Self {
 86          println!("  [MacOSButton] Creating button with label: '{}'", label);
 87          MacOSButton {
 88              label: label.to_string(),
 89          }
 90      }
 91  }
 92
 93  impl Button for MacOSButton {
 94      fn render(&self) {
 95          println!("  [MacOSButton] Rendering macOS-style button: ({})", self.label);
 96      }
 97
 98      fn on_click(&self) {
 99          println!("  [MacOSButton] macOS click event triggered for '{}'", self.label);
100      }
101  }
102
103  /// Concrete macOS checkbox
104  struct MacOSCheckbox {
105      label: String,
106      checked: bool,
107  }
108
109  impl MacOSCheckbox {
110      fn new(label: &str) -> Self {
111          println!("  [MacOSCheckbox] Creating checkbox with label: '{}'", label);
112          MacOSCheckbox {
113              label: label.to_string(),
114              checked: false,
115          }
116      }
117  }
118
119  impl Checkbox for MacOSCheckbox {
120      fn render(&self) {
121          let state = if self.checked { "●" } else { "○" };
122          println!("  [MacOSCheckbox] Rendering macOS-style checkbox: {} {}", state, self.label);
123      }
124
125      fn toggle(&self) {
126          println!("  [MacOSCheckbox] macOS checkbox '{}' toggled", self.label);
127      }
128  }
129
130  // ============================================================================
131  // Abstract Factory - Trait defining the factory interface
132  // ============================================================================
133
134  /// Abstract factory trait for creating GUI component families
135  trait GUIFactory {
136      fn create_button(&self, label: &str) -> Box<dyn Button>;
137      fn create_checkbox(&self, label: &str) -> Box<dyn Checkbox>;
138      fn get_theme_name(&self) -> &str;
139  }
140
141  // ============================================================================
142  // Concrete Factories
143  // ============================================================================
144
145  /// Concrete factory for Windows theme
146  struct WindowsFactory;
147
148  impl WindowsFactory {
149      fn new() -> Self {
150          println!("[WindowsFactory] Initializing Windows GUI Factory");
151          WindowsFactory
152      }
153  }
154
155  impl GUIFactory for WindowsFactory {
156      fn create_button(&self, label: &str) -> Box<dyn Button> {
157          Box::new(WindowsButton::new(label))
158      }
159
160      fn create_checkbox(&self, label: &str) -> Box<dyn Checkbox> {
161          Box::new(WindowsCheckbox::new(label))
162      }
163
164      fn get_theme_name(&self) -> &str {
165          "Windows"
166      }
167  }
168
169  /// Concrete factory for macOS theme
170  struct MacOSFactory;
171
172  impl MacOSFactory {
173      fn new() -> Self {
174          println!("[MacOSFactory] Initializing macOS GUI Factory");
175          MacOSFactory
176      }
177  }
178
179  impl GUIFactory for MacOSFactory {
180      fn create_button(&self, label: &str) -> Box<dyn Button> {
181          Box::new(MacOSButton::new(label))
182      }
183
184      fn create_checkbox(&self, label: &str) -> Box<dyn Checkbox> {
185          Box::new(MacOSCheckbox::new(label))
186      }
187
188      fn get_theme_name(&self) -> &str {
189          "macOS"
190      }
191  }
192
193  // ============================================================================
194  // Client Code - Works with factories through abstract interfaces
195  // ============================================================================
196
197  /// Application that uses the abstract factory to create GUI components
198  struct Application {
199      button: Box<dyn Button>,
200      checkbox: Box<dyn Checkbox>,
201      theme: String,
202  }
203
204  impl Application {
205      fn new(factory: &dyn GUIFactory) -> Self {
206          println!("\n[Application] Building application with {} theme", factory.get_theme_name());
207
208          let button = factory.create_button("Submit");
209          let checkbox = factory.create_checkbox("Remember me");
210
211          Application {
212              button,
213              checkbox,
214              theme: factory.get_theme_name().to_string(),
215          }
216      }
217
218      fn render(&self) {
219          println!("\n[Application] Rendering {} themed components:", self.theme);
220          self.button.render();
221          self.checkbox.render();
222      }
223
224      fn interact(&self) {
225          println!("\n[Application] Simulating user interaction:");
226          self.button.on_click();
227          self.checkbox.toggle();
228      }
229  }
230
231  /// Factory selector based on configuration
232  fn get_factory(os_type: &str) -> Box<dyn GUIFactory> {
233      println!("\n[FactorySelector] Selecting factory for OS: {}", os_type);
234      match os_type.to_lowercase().as_str() {
235          "windows" => Box::new(WindowsFactory::new()),
236          "macos" | "mac" => Box::new(MacOSFactory::new()),
237          _ => {
238              println!("[FactorySelector] Unknown OS, defaulting to Windows");
239              Box::new(WindowsFactory::new())
240          }
241      }
242  }
243
244  // ============================================================================
245  // Main - Demonstrates the Abstract Factory pattern
246  // ============================================================================
247
248  fn main() {
249      println!("{}", "=".repeat(60));
250      println!("Abstract Factory Design Pattern - GUI Component Example");
251      println!("{}", "=".repeat(60));
252
253      // Demonstrate Windows theme
254      println!("\n--- Creating Windows Application ---");
255      let windows_factory = get_factory("Windows");
256      let windows_app = Application::new(windows_factory.as_ref());
257      windows_app.render();
258      windows_app.interact();
259
260      // Demonstrate macOS theme
261      println!("\n--- Creating macOS Application ---");
262      let macos_factory = get_factory("macOS");
263      let macos_app = Application::new(macos_factory.as_ref());
264      macos_app.render();
265      macos_app.interact();
266
267      // Demonstrate runtime factory selection
268      println!("\n--- Dynamic Factory Selection ---");
269      let os_configs = vec!["Windows", "macOS", "Linux"];
270
271      for os in os_configs {
272          let factory = get_factory(os);
273          let button = factory.create_button("OK");
274          button.render();
275      }
276
277      println!("\n{}", "=".repeat(60));
278      println!("Abstract Factory Pattern demonstration complete!");
279      println!("{}", "=".repeat(60));
280  }
```

## Program Output

```
============================================================
Abstract Factory Design Pattern - GUI Component Example
============================================================

--- Creating Windows Application ---

[FactorySelector] Selecting factory for OS: Windows
[WindowsFactory] Initializing Windows GUI Factory

[Application] Building application with Windows theme
  [WindowsButton] Creating button with label: 'Submit'
  [WindowsCheckbox] Creating checkbox with label: 'Remember me'

[Application] Rendering Windows themed components:
  [WindowsButton] Rendering Windows-style button: [Submit]
  [WindowsCheckbox] Rendering Windows-style checkbox: [ ] Remember me

[Application] Simulating user interaction:
  [WindowsButton] Windows click event triggered for 'Submit'
  [WindowsCheckbox] Windows checkbox 'Remember me' toggled

--- Creating macOS Application ---

[FactorySelector] Selecting factory for OS: macOS
[MacOSFactory] Initializing macOS GUI Factory

[Application] Building application with macOS theme
  [MacOSButton] Creating button with label: 'Submit'
  [MacOSCheckbox] Creating checkbox with label: 'Remember me'

[Application] Rendering macOS themed components:
  [MacOSButton] Rendering macOS-style button: (Submit)
  [MacOSCheckbox] Rendering macOS-style checkbox: ○ Remember me

[Application] Simulating user interaction:
  [MacOSButton] macOS click event triggered for 'Submit'
  [MacOSCheckbox] macOS checkbox 'Remember me' toggled

--- Dynamic Factory Selection ---

[FactorySelector] Selecting factory for OS: Windows
[WindowsFactory] Initializing Windows GUI Factory
  [WindowsButton] Creating button with label: 'OK'
  [WindowsButton] Rendering Windows-style button: [OK]

[FactorySelector] Selecting factory for OS: macOS
[MacOSFactory] Initializing macOS GUI Factory
  [MacOSButton] Creating button with label: 'OK'
  [MacOSButton] Rendering macOS-style button: (OK)

[FactorySelector] Selecting factory for OS: Linux
[FactorySelector] Unknown OS, defaulting to Windows
[WindowsFactory] Initializing Windows GUI Factory
  [WindowsButton] Creating button with label: 'OK'
  [WindowsButton] Rendering Windows-style button: [OK]

============================================================
Abstract Factory Pattern demonstration complete!
============================================================
```

## Code Annotations

### Key Sections Explained

#### Abstract Products (Lines 8-18)
The `Button` and `Checkbox` traits define the abstract product interfaces. These traits declare the methods that all concrete products must implement, enabling polymorphic behavior through Rust's trait system.

#### Concrete Products - Windows Theme (Lines 24-73)
- **WindowsButton** (lines 25-46): Implements the Button trait with Windows-specific styling using square brackets `[Submit]`
- **WindowsCheckbox** (lines 49-73): Implements the Checkbox trait with Windows-style rendering using `[X]` or `[ ]`

#### Concrete Products - macOS Theme (Lines 80-128)
- **MacOSButton** (lines 80-101): Implements the Button trait with macOS-specific styling using parentheses `(Submit)`
- **MacOSCheckbox** (lines 104-128): Implements the Checkbox trait with macOS-style rendering using `●` or `○`

#### Abstract Factory Trait (Lines 135-139)
The `GUIFactory` trait defines the abstract factory interface with methods to create buttons and checkboxes. This is the core of the pattern - it declares methods for creating each product type without specifying concrete classes.

#### Concrete Factories (Lines 146-191)
- **WindowsFactory** (lines 146-167): Creates WindowsButton and WindowsCheckbox instances
- **MacOSFactory** (lines 170-191): Creates MacOSButton and MacOSCheckbox instances

#### Client Code (Lines 198-229)
The `Application` struct demonstrates client code that works with factories through abstract interfaces. It receives a `&dyn GUIFactory` and uses it to create components without knowing their concrete types.

#### Factory Selector (Lines 232-242)
A helper function that demonstrates runtime factory selection using pattern matching. This shows how the pattern supports configuration-based object creation.

### Output to Source Code Correlation

| Output Line | Source Line(s) | Description |
|-------------|---------------|-------------|
| `[FactorySelector] Selecting factory for OS: Windows` | 233 | Factory selector logging OS type |
| `[WindowsFactory] Initializing Windows GUI Factory` | 150 | WindowsFactory::new() constructor output |
| `[Application] Building application with Windows theme` | 206 | Application::new() logging theme |
| `[WindowsButton] Creating button with label: 'Submit'` | 31 | WindowsButton::new() constructor output |
| `[WindowsCheckbox] Creating checkbox with label: 'Remember me'` | 56 | WindowsCheckbox::new() constructor output |
| `[WindowsButton] Rendering Windows-style button: [Submit]` | 40 | Button::render() implementation |
| `[WindowsCheckbox] Rendering Windows-style checkbox: [ ] Remember me` | 67 | Checkbox::render() implementation |
| `[WindowsButton] Windows click event triggered for 'Submit'` | 44 | Button::on_click() implementation |
| `[WindowsCheckbox] Windows checkbox 'Remember me' toggled` | 71 | Checkbox::toggle() implementation |
| `[MacOSFactory] Initializing macOS GUI Factory` | 174 | MacOSFactory::new() constructor output |
| `[MacOSButton] Rendering macOS-style button: (Submit)` | 95 | macOS Button::render() - uses parentheses |
| `[MacOSCheckbox] Rendering macOS-style checkbox: ○ Remember me` | 122 | macOS Checkbox::render() - uses circle symbols |
| `[FactorySelector] Unknown OS, defaulting to Windows` | 238 | Default case in factory selector |

## Key Characteristics in Rust

### 1. Trait Objects for Polymorphism
Rust uses `Box<dyn Trait>` to achieve runtime polymorphism. The factory methods return `Box<dyn Button>` and `Box<dyn Checkbox>`, allowing different concrete types to be used interchangeably.

### 2. Zero-Cost Abstractions
When the concrete type is known at compile time, Rust can optimize away the dynamic dispatch. The pattern uses dynamic dispatch only where truly needed.

### 3. Memory Safety
Rust's ownership system ensures that all created objects are properly managed:
- `Box` provides heap allocation with automatic cleanup
- No null pointer issues due to Rust's Option type (not shown but implied)
- Clear ownership transfer when factories create products

### 4. Pattern Matching for Factory Selection
The `get_factory` function uses Rust's powerful pattern matching to select the appropriate factory based on configuration, demonstrating idiomatic Rust patterns.

### 5. No Inheritance Required
Unlike traditional OOP languages, Rust implements the Abstract Factory pattern using traits and composition rather than class inheritance. This leads to more flexible and composable code.

### Compilation and Execution

```bash
rustc main_abstract_factory.rs -o main_abstract_factory && ./main_abstract_factory
```

**Requirements**: Rust 1.0+ (uses stable features only)
