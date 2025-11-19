# Abstract Factory Design Pattern in TypeScript

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It encapsulates a group of individual factories with a common theme, allowing the creation of entire product families that are designed to work together.

This example demonstrates the pattern using a UI component theming system where different factories create families of themed components (Button, Checkbox, TextField) that are visually consistent within their theme.

## Requirements

- Node.js 18+
- TypeScript 5.3+

## How to Run

```bash
npm install
npm run start
```

## Source Code

```typescript
1   /**
2    * Abstract Factory Design Pattern in TypeScript
3    *
4    * The Abstract Factory pattern provides an interface for creating families of
5    * related or dependent objects without specifying their concrete classes.
6    * It encapsulates a group of individual factories with a common theme.
7    */
8
9   // ============================================================
10  // Abstract Product Interfaces
11  // ============================================================
12
13  // Abstract Product A - Button
14  interface Button {
15      render(): void;
16      onClick(callback: () => void): void;
17  }
18
19  // Abstract Product B - Checkbox
20  interface Checkbox {
21      render(): void;
22      toggle(): void;
23      isChecked(): boolean;
24  }
25
26  // Abstract Product C - TextField
27  interface TextField {
28      render(): void;
29      setValue(value: string): void;
30      getValue(): string;
31  }
32
33  // ============================================================
34  // Concrete Products - Light Theme
35  // ============================================================
36
37  class LightButton implements Button {
38      private name: string;
39
40      constructor(name: string) {
41          this.name = name;
42          console.log(`[Line 38] LightButton: Created '${name}' with light theme styling`);
43      }
44
45      render(): void {
46          console.log(`[Line 42] LightButton: Rendering '${this.name}' with white background and dark text`);
47      }
48
49      onClick(callback: () => void): void {
50          console.log(`[Line 46] LightButton: '${this.name}' clicked - executing callback`);
51          callback();
52      }
53  }
54
55  class LightCheckbox implements Checkbox {
56      private name: string;
57      private checked: boolean = false;
58
59      constructor(name: string) {
60          this.name = name;
61          console.log(`[Line 56] LightCheckbox: Created '${name}' with light theme styling`);
62      }
63
64      render(): void {
65          const state = this.checked ? "checked" : "unchecked";
66          console.log(`[Line 61] LightCheckbox: Rendering '${this.name}' (${state}) with light gray border`);
67      }
68
69      toggle(): void {
70          this.checked = !this.checked;
71          console.log(`[Line 66] LightCheckbox: '${this.name}' toggled to ${this.checked}`);
72      }
73
74      isChecked(): boolean {
75          return this.checked;
76      }
77  }
78
79  class LightTextField implements TextField {
80      private name: string;
81      private value: string = "";
82
83      constructor(name: string) {
84          this.name = name;
85          console.log(`[Line 79] LightTextField: Created '${name}' with light theme styling`);
86      }
87
88      render(): void {
89          console.log(`[Line 83] LightTextField: Rendering '${this.name}' with white background and dark border`);
90      }
91
92      setValue(value: string): void {
93          this.value = value;
94          console.log(`[Line 88] LightTextField: '${this.name}' value set to '${value}'`);
95      }
96
97      getValue(): string {
98          return this.value;
99      }
100 }
101
102 // ============================================================
103 // Concrete Products - Dark Theme
104 // ============================================================
105
106 class DarkButton implements Button {
107     private name: string;
108
109     constructor(name: string) {
110         this.name = name;
111         console.log(`[Line 104] DarkButton: Created '${name}' with dark theme styling`);
112     }
113
114     render(): void {
115         console.log(`[Line 108] DarkButton: Rendering '${this.name}' with dark background and light text`);
116     }
117
118     onClick(callback: () => void): void {
119         console.log(`[Line 112] DarkButton: '${this.name}' clicked - executing callback`);
120         callback();
121     }
122 }
123
124 class DarkCheckbox implements Checkbox {
125     private name: string;
126     private checked: boolean = false;
127
128     constructor(name: string) {
129         this.name = name;
130         console.log(`[Line 122] DarkCheckbox: Created '${name}' with dark theme styling`);
131     }
132
133     render(): void {
134         const state = this.checked ? "checked" : "unchecked";
135         console.log(`[Line 127] DarkCheckbox: Rendering '${this.name}' (${state}) with light border on dark`);
136     }
137
138     toggle(): void {
139         this.checked = !this.checked;
140         console.log(`[Line 132] DarkCheckbox: '${this.name}' toggled to ${this.checked}`);
141     }
142
143     isChecked(): boolean {
144         return this.checked;
145     }
146 }
147
148 class DarkTextField implements TextField {
149     private name: string;
150     private value: string = "";
151
152     constructor(name: string) {
153         this.name = name;
154         console.log(`[Line 145] DarkTextField: Created '${name}' with dark theme styling`);
155     }
156
157     render(): void {
158         console.log(`[Line 149] DarkTextField: Rendering '${this.name}' with dark background and light border`);
159     }
160
161     setValue(value: string): void {
162         this.value = value;
163         console.log(`[Line 154] DarkTextField: '${this.name}' value set to '${value}'`);
164     }
165
166     getValue(): string {
167         return this.value;
168     }
169 }
170
171 // ============================================================
172 // Abstract Factory Interface
173 // ============================================================
174
175 interface UIComponentFactory {
176     createButton(name: string): Button;
177     createCheckbox(name: string): Checkbox;
178     createTextField(name: string): TextField;
179     getThemeName(): string;
180 }
181
182 // ============================================================
183 // Concrete Factories
184 // ============================================================
185
186 class LightThemeFactory implements UIComponentFactory {
187     constructor() {
188         console.log("[Line 177] LightThemeFactory: Initialized - will create light-themed components");
189     }
190
191     createButton(name: string): Button {
192         console.log(`[Line 181] LightThemeFactory: Creating light-themed button '${name}'`);
193         return new LightButton(name);
194     }
195
196     createCheckbox(name: string): Checkbox {
197         console.log(`[Line 186] LightThemeFactory: Creating light-themed checkbox '${name}'`);
198         return new LightCheckbox(name);
199     }
200
201     createTextField(name: string): TextField {
202         console.log(`[Line 191] LightThemeFactory: Creating light-themed text field '${name}'`);
203         return new LightTextField(name);
204     }
205
206     getThemeName(): string {
207         return "Light Theme";
208     }
209 }
210
211 class DarkThemeFactory implements UIComponentFactory {
212     constructor() {
213         console.log("[Line 202] DarkThemeFactory: Initialized - will create dark-themed components");
214     }
215
216     createButton(name: string): Button {
217         console.log(`[Line 206] DarkThemeFactory: Creating dark-themed button '${name}'`);
218         return new DarkButton(name);
219     }
220
221     createCheckbox(name: string): Checkbox {
222         console.log(`[Line 211] DarkThemeFactory: Creating dark-themed checkbox '${name}'`);
223         return new DarkCheckbox(name);
224     }
225
226     createTextField(name: string): TextField {
227         console.log(`[Line 216] DarkThemeFactory: Creating dark-themed text field '${name}'`);
228         return new DarkTextField(name);
229     }
230
231     getThemeName(): string {
232         return "Dark Theme";
233     }
234 }
```

## Program Output

```
=== Abstract Factory Pattern Demonstration ===
Creating UI components with different themes

--- Demo 1: Light Theme Application ---
[Line 268] getFactory: Requested theme 'light'
[Line 177] LightThemeFactory: Initialized - will create light-themed components

[Line 235] Application: Initializing with Light Theme
[Line 181] LightThemeFactory: Creating light-themed button 'Submit'
[Line 38] LightButton: Created 'Submit' with light theme styling
[Line 186] LightThemeFactory: Creating light-themed checkbox 'Remember Me'
[Line 56] LightCheckbox: Created 'Remember Me' with light theme styling
[Line 191] LightThemeFactory: Creating light-themed text field 'Username'
[Line 79] LightTextField: Created 'Username' with light theme styling

[Line 244] Application: Rendering all components
[Line 42] LightButton: Rendering 'Submit' with white background and dark text
[Line 61] LightCheckbox: Rendering 'Remember Me' (unchecked) with light gray border
[Line 83] LightTextField: Rendering 'Username' with white background and dark border

[Line 251] Application: Simulating user interaction
[Line 88] LightTextField: 'Username' value set to 'john_doe'
[Line 66] LightCheckbox: 'Remember Me' toggled to true
[Line 46] LightButton: 'Submit' clicked - executing callback
[Line 261] Application: Form submitted with username 'john_doe', remember: true


--- Demo 2: Dark Theme Application ---
[Line 268] getFactory: Requested theme 'dark'
[Line 202] DarkThemeFactory: Initialized - will create dark-themed components

[Line 235] Application: Initializing with Dark Theme
[Line 206] DarkThemeFactory: Creating dark-themed button 'Submit'
[Line 104] DarkButton: Created 'Submit' with dark theme styling
[Line 211] DarkThemeFactory: Creating dark-themed checkbox 'Remember Me'
[Line 122] DarkCheckbox: Created 'Remember Me' with dark theme styling
[Line 216] DarkThemeFactory: Creating dark-themed text field 'Username'
[Line 145] DarkTextField: Created 'Username' with dark theme styling

[Line 244] Application: Rendering all components
[Line 108] DarkButton: Rendering 'Submit' with dark background and light text
[Line 127] DarkCheckbox: Rendering 'Remember Me' (unchecked) with light border on dark
[Line 149] DarkTextField: Rendering 'Username' with dark background and light border

[Line 251] Application: Simulating user interaction
[Line 154] DarkTextField: 'Username' value set to 'john_doe'
[Line 132] DarkCheckbox: 'Remember Me' toggled to true
[Line 112] DarkButton: 'Submit' clicked - executing callback
[Line 261] Application: Form submitted with username 'john_doe', remember: true


--- Demo 3: Direct Factory Usage ---
[Line 177] LightThemeFactory: Initialized - will create light-themed components
[Line 202] DarkThemeFactory: Initialized - will create dark-themed components

[Line 307] Creating components with factory 1 (Light Theme)
[Line 181] LightThemeFactory: Creating light-themed button 'Action'
[Line 38] LightButton: Created 'Action' with light theme styling
[Line 186] LightThemeFactory: Creating light-themed checkbox 'Option'
[Line 56] LightCheckbox: Created 'Option' with light theme styling
[Line 42] LightButton: Rendering 'Action' with white background and dark text
[Line 61] LightCheckbox: Rendering 'Option' (unchecked) with light gray border
[Line 66] LightCheckbox: 'Option' toggled to true

[Line 307] Creating components with factory 2 (Dark Theme)
[Line 206] DarkThemeFactory: Creating dark-themed button 'Action'
[Line 104] DarkButton: Created 'Action' with dark theme styling
[Line 211] DarkThemeFactory: Creating dark-themed checkbox 'Option'
[Line 122] DarkCheckbox: Created 'Option' with dark theme styling
[Line 108] DarkButton: Rendering 'Action' with dark background and light text
[Line 127] DarkCheckbox: Rendering 'Option' (unchecked) with light border on dark
[Line 132] DarkCheckbox: 'Option' toggled to true


--- Demo 4: Runtime Theme Selection ---
[Line 318] User preference: 'dark'
[Line 268] getFactory: Requested theme 'dark'
[Line 202] DarkThemeFactory: Initialized - will create dark-themed components
[Line 206] DarkThemeFactory: Creating dark-themed button 'Custom Action'
[Line 104] DarkButton: Created 'Custom Action' with dark theme styling
[Line 108] DarkButton: Rendering 'Custom Action' with dark background and light text
[Line 112] DarkButton: 'Custom Action' clicked - executing callback
[Line 323] Custom action executed!

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Pattern Components

#### Abstract Product Interfaces (Lines 14-31)
- Define the common interfaces for product families
- `Button`: Methods for rendering and handling clicks
- `Checkbox`: Methods for rendering, toggling, and checking state
- `TextField`: Methods for rendering and managing text values

#### Concrete Products - Light Theme (Lines 37-100)
- `LightButton`: White background, dark text styling
- `LightCheckbox`: Light gray border styling
- `LightTextField`: White background with dark border
- All implement their respective abstract product interfaces

#### Concrete Products - Dark Theme (Lines 106-169)
- `DarkButton`: Dark background, light text styling
- `DarkCheckbox`: Light border on dark background
- `DarkTextField`: Dark background with light border
- Mirror the light theme products but with inverted color schemes

#### Abstract Factory Interface (Lines 175-180)
- `UIComponentFactory`: Declares creation methods for each product type
- Each factory must implement methods for creating all product types
- Ensures product families are created consistently

#### Concrete Factories (Lines 186-234)
- `LightThemeFactory`: Creates light-themed components
- `DarkThemeFactory`: Creates dark-themed components
- Each factory creates products that are visually consistent

### Output Correlation

| Output Line Reference | Source Line | Explanation |
|----------------------|-------------|-------------|
| `getFactory: Requested theme 'light'` | Line 268 | Factory selector receives theme request |
| `LightThemeFactory: Initialized` | Line 177 | Light factory constructor executes |
| `Application: Initializing with Light Theme` | Line 235 | Application receives factory and begins creation |
| `LightThemeFactory: Creating light-themed button` | Line 181 | Factory method called to create button |
| `LightButton: Created 'Submit'` | Line 38 | Concrete product constructor executes |
| `Application: Rendering all components` | Line 244 | Application triggers render on all products |
| `LightButton: Rendering 'Submit'` | Line 42 | Product's render method displays theme-specific styling |
| `Application: Simulating user interaction` | Line 251 | User interaction simulation begins |
| `LightTextField: value set to 'john_doe'` | Line 88 | Text field stores user input |
| `LightCheckbox: toggled to true` | Line 66 | Checkbox state changes |
| `LightButton: clicked - executing callback` | Line 46 | Button executes provided callback |
| `Application: Form submitted` | Line 261 | Callback confirms form submission |

### Factory vs Product Creation Flow

| Step | Action | Class | Source Line |
|------|--------|-------|-------------|
| 1 | Request theme | `getFactory()` | 268 |
| 2 | Initialize factory | `LightThemeFactory` | 177 |
| 3 | Request button | `Application` | 235-237 |
| 4 | Factory creates | `LightThemeFactory.createButton()` | 181 |
| 5 | Product instantiated | `LightButton` | 38 |
| 6 | Use product | `button.render()` | 42 |

### Why Abstract Factory Works

1. **Product Family Consistency**: All components from one factory share the same theme
   - `LightThemeFactory` only creates light-themed components
   - No mixing of themes within a product family

2. **Open/Closed Principle**: Add new themes without modifying existing code
   - Create `HighContrastFactory` without changing `Application`
   - New products can be added by extending interfaces

3. **Dependency Inversion**: Client depends on abstractions, not concrete classes
   - `Application` uses `UIComponentFactory` interface
   - Doesn't know about `LightButton` or `DarkButton` directly

4. **Polymorphism**: Factories and products are interchangeable
   - Lines 302-312 show factories in an array
   - Same code works with any factory implementation

### Difference from Factory Method

| Aspect | Factory Method | Abstract Factory |
|--------|---------------|------------------|
| Products | Single product type | Family of related products |
| Factories | One factory per product | One factory per family |
| Abstraction | Method-level | Object-level |
| Use case | Create one object | Create consistent sets |

### Use Cases

- **Cross-platform UI**: Windows, macOS, Linux component factories
- **Theme Systems**: Light, dark, high-contrast themes
- **Database Access**: MySQL, PostgreSQL, SQLite connection factories
- **Document Generation**: PDF, HTML, Word document element factories
- **Game Development**: Different art style factories (realistic, cartoon, pixel art)

### Runtime Theme Switching (Demo 4)

The pattern enables dynamic factory selection at runtime:
```typescript
const userPreference = "dark";  // Could come from user settings
const selectedFactory = getFactory(userPreference);
const customButton = selectedFactory.createButton("Custom Action");
```

This demonstrates how the Abstract Factory pattern supports configuration-driven product creation without conditional logic scattered throughout the application.
