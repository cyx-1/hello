# Questionary - Interactive CLI Tool

This example demonstrates the **questionary** library for building interactive command-line interfaces (CLI) in Python.

## Overview

Questionary is a Python library that makes it easy to build beautiful command-line interfaces with interactive prompts. It provides various question types including text input, selections, confirmations, and more.

## Requirements

- **Python**: 3.8 or higher (uses inline script metadata)
- **Library**: questionary >= 2.0.0

## Running the Example

```bash
uv run main_questionary.py
```

The script uses inline script metadata (PEP 723), so `uv` will automatically install the required dependencies.

---

## Source Code Structure

### Main Entry Point (Lines 188-214)

```python
188: def main():
189:     """Run all demonstrations."""
190:     print("=" * 60)
191:     print("QUESTIONARY - Interactive CLI Tool Demonstrations")
192:     print("=" * 60)
193:     print("\nNote: Some demos require interactive input.")
194:     print("For automated demo, default values will be used.\n")
195:
196:     # Run demonstrations
197:     demo_text_input()           # Line 196
198:     demo_password()             # Line 197
199:     demo_confirm()              # Line 198
200:     demo_select()               # Line 199
201:     demo_checkbox()             # Line 200
202:     demo_rawselect()            # Line 201
203:     demo_autocomplete()         # Line 202
204:     demo_path()                 # Line 203
205:     demo_custom_style()         # Line 204
206:     demo_validation()           # Line 205
207:     demo_conditional_questions()  # Line 206
208:
209:     print("\n" + "=" * 60)
210:     print("Demo completed!")
211:     print("=" * 60)
```

**Annotation**: The main function (line 188) orchestrates all demonstrations, calling each demo function sequentially (lines 197-207).

---

## Feature Demonstrations

### 1. Text Input (Lines 17-24)

```python
17: def demo_text_input():
18:     """Demonstrate simple text input."""
19:     print("\n=== Text Input Demo ===")  # Line 19
20:     name = questionary.text(
21:         "What is your name?",
22:         default="John Doe"
23:     ).ask()
24:     print(f"Hello, {name}!")  # Line 24
```

**Output:**
```
=== Text Input Demo ===
? What is your name? Alice Smith
Hello, Alice Smith!
```

**Annotation**:
- Line 19: Prints the section header
- Lines 20-23: Creates a text input prompt with a default value
- Line 24: Displays the user's input

---

### 2. Password Input (Lines 27-32)

```python
27: def demo_password():
28:     """Demonstrate password input (hidden characters)."""
29:     print("\n=== Password Input Demo ===")  # Line 28
30:     password = questionary.password(
31:         "Enter your password:"
32:     ).ask()
33:     print(f"Password length: {len(password) if password else 0} characters")  # Line 32
```

**Output:**
```
=== Password Input Demo ===
? Enter your password: ***********
Password length: 11 characters
```

**Annotation**:
- Line 30-32: `questionary.password()` hides input with asterisks for security
- Line 33: Shows password length without revealing the actual password

---

### 3. Confirmation (Lines 35-41)

```python
35: def demo_confirm():
36:     """Demonstrate yes/no confirmation."""
37:     print("\n=== Confirmation Demo ===")  # Line 36
38:     confirm = questionary.confirm(
39:         "Do you want to continue?",
40:         default=True
41:     ).ask()
42:     print(f"User confirmed: {confirm}")  # Line 41
```

**Output:**
```
=== Confirmation Demo ===
? Do you want to continue? Yes
User confirmed: True
```

**Annotation**:
- Lines 38-41: `questionary.confirm()` provides a yes/no prompt
- Returns a boolean value (True/False)
- Line 40: Default value is True

---

### 4. Select (Single Choice) (Lines 44-58)

```python
44: def demo_select():
45:     """Demonstrate single selection from a list."""
46:     print("\n=== Select Demo ===")  # Line 45
47:     choice = questionary.select(
48:         "What's your favorite programming language?",
49:         choices=[
50:             "Python",
51:             "JavaScript",
52:             "Go",
53:             "Rust",
54:             "Java",
55:             "TypeScript"
56:         ]
57:     ).ask()
58:     print(f"Selected: {choice}")  # Line 58
```

**Output:**
```
=== Select Demo ===
? What's your favorite programming language?
  Python
❯ JavaScript
  Go
  Rust
  Java
  TypeScript

Selected: JavaScript
```

**Annotation**:
- Lines 47-57: Creates an interactive menu with arrow key navigation
- Line 58: Returns the selected choice as a string
- The `❯` symbol indicates the currently highlighted option

---

### 5. Checkbox (Multiple Choice) (Lines 61-74)

```python
61: def demo_checkbox():
62:     """Demonstrate multiple selection from a list."""
63:     print("\n=== Checkbox Demo ===")  # Line 62
64:     choices = questionary.checkbox(
65:         "Select your skills (use space to select, enter to confirm):",
66:         choices=[
67:             "Python",
68:             "JavaScript",
69:             "Docker",
70:             "Kubernetes",
71:             "AWS",
72:             "Git"
73:         ]
74:     ).ask()
75:     print(f"Selected skills: {', '.join(choices) if choices else 'None'}")  # Line 74
```

**Output:**
```
=== Checkbox Demo ===
? Select your skills (use space to select, enter to confirm): done (3 selections)
❯ ◉ Python
  ◯ JavaScript
  ◉ Docker
  ◉ Kubernetes
  ◯ AWS
  ◯ Git

Selected skills: Python, Docker, Kubernetes
```

**Annotation**:
- Lines 64-74: Allows multiple selections using spacebar
- `◉` indicates selected items, `◯` indicates unselected items
- Line 75: Returns a list of selected choices

---

### 6. Raw Select (Lines 77-88)

```python
77: def demo_rawselect():
78:     """Demonstrate selection with shortcuts."""
79:     print("\n=== Raw Select Demo ===")  # Line 78
80:     choice = questionary.rawselect(
81:         "Choose your deployment environment:",
82:         choices=[
83:             "Development",
84:             "Staging",
85:             "Production"
86:         ]
87:     ).ask()
88:     print(f"Selected environment: {choice}")  # Line 88
```

**Output:**
```
=== Raw Select Demo ===
? Choose your deployment environment?
  1) Development
❯ 2) Staging
  3) Production

Selected environment: Staging
```

**Annotation**:
- Lines 80-87: Similar to `select()` but with numbered shortcuts
- Users can type the number to select an option directly

---

### 7. Autocomplete (Lines 91-106)

```python
 91: def demo_autocomplete():
 92:     """Demonstrate autocomplete functionality."""
 93:     print("\n=== Autocomplete Demo ===")  # Line 92
 94:     frameworks = [
 95:         "Django",
 96:         "Flask",
 97:         "FastAPI",
 98:         "Tornado",
 99:         "Pyramid",
100:         "Bottle"
101:     ]
102:     choice = questionary.autocomplete(
103:         "Choose a Python web framework (start typing):",
104:         choices=frameworks
105:     ).ask()
106:     print(f"Selected framework: {choice}")  # Line 106
```

**Output:**
```
=== Autocomplete Demo ===
? Choose a Python web framework (start typing): Fa
  Django
❯ FastAPI
  Flask

Selected framework: FastAPI
```

**Annotation**:
- Lines 102-105: Filters choices as the user types
- Typing "Fa" shows only "FastAPI" and "Flask"
- Line 106: Returns the selected or typed value

---

### 8. Path Selection (Lines 109-115)

```python
109: def demo_path():
110:     """Demonstrate file path selection."""
111:     print("\n=== Path Demo ===")  # Line 110
112:     path = questionary.path(
113:         "Select a file or directory:",
114:         default="."
115:     ).ask()
116:     print(f"Selected path: {path}")  # Line 115
```

**Output:**
```
=== Path Demo ===
? Select a file or directory: ./python/questionary
Selected path: ./python/questionary
```

**Annotation**:
- Lines 112-115: Provides path autocomplete for filesystem navigation
- Line 114: Default starting path is current directory
- Supports tab completion for directories and files

---

### 9. Custom Styling (Lines 118-139)

```python
118: def demo_custom_style():
119:     """Demonstrate custom styling."""
120:     print("\n=== Custom Style Demo ===")  # Line 119
121:
122:     custom_style = Style([
123:         ('qmark', 'fg:#673ab7 bold'),       # Question mark color
124:         ('question', 'bold'),                # Question text
125:         ('answer', 'fg:#f44336 bold'),       # User's answer
126:         ('pointer', 'fg:#673ab7 bold'),      # Pointer in lists
127:         ('highlighted', 'fg:#673ab7 bold'),  # Highlighted choice
128:         ('selected', 'fg:#cc5454'),          # Selected checkbox items
129:         ('separator', 'fg:#cc5454'),         # Separator line
130:         ('instruction', ''),                 # Instruction text
131:         ('text', ''),                        # Plain text
132:     ])
133:
134:     choice = questionary.select(
135:         "Choose your favorite color (with custom styling):",
136:         choices=["Red", "Green", "Blue", "Purple"],
137:         style=custom_style
138:     ).ask()
139:     print(f"Favorite color: {choice}")  # Line 139
```

**Output:**
```
=== Custom Style Demo ===
? Choose your favorite color (with custom styling)?
  Red
  Green
  Blue
❯ Purple

Favorite color: Purple
```

**Annotation**:
- Lines 122-132: Defines custom colors and formatting using Style object
- Line 123: `fg:#673ab7` sets foreground color to purple
- Line 125: `fg:#f44336` sets answer text to red
- Lines 134-138: Applies the custom style to the select prompt
- Custom styles allow complete visual customization of prompts

---

### 10. Input Validation (Lines 142-162)

```python
142: def demo_validation():
143:     """Demonstrate input validation."""
144:     print("\n=== Validation Demo ===")  # Line 143
145:
146:     def validate_age(text):
147:         """Validate that input is a number between 1 and 120."""
148:         if not text:
149:             return "Please enter a value"
150:         try:
151:             age = int(text)
152:             if age < 1 or age > 120:
153:                 return "Age must be between 1 and 120"
154:             return True
155:         except ValueError:
156:             return "Please enter a valid number"
157:
158:     age = questionary.text(
159:         "What is your age?",
160:         validate=validate_age
161:     ).ask()
162:     print(f"Age entered: {age}")  # Line 162
```

**Output:**
```
=== Validation Demo ===
? What is your age? abc
Please enter a valid number
? What is your age? 150
Age must be between 1 and 120
? What is your age? 28
Age entered: 28
```

**Annotation**:
- Lines 146-156: Custom validation function checks if input is valid
- Line 149: Returns error message for empty input
- Lines 151-153: Validates numeric range (1-120)
- Line 155-156: Returns error message for non-numeric input
- Line 154: Returns `True` when validation passes
- The prompt repeats until valid input is provided

---

### 11. Conditional Questions (Lines 165-185)

```python
165: def demo_conditional_questions():
166:     """Demonstrate conditional questions based on previous answers."""
167:     print("\n=== Conditional Questions Demo ===")  # Line 166
168:
169:     is_developer = questionary.confirm(
170:         "Are you a developer?",
171:         default=True
172:     ).ask()
173:
174:     if is_developer:
175:         experience = questionary.select(
176:             "How many years of experience?",
177:             choices=[
178:                 "0-2 years",
179:                 "3-5 years",
180:                 "6-10 years",
181:                 "10+ years"
182:             ]
183:         ).ask()
184:         print(f"Developer with {experience} of experience")  # Line 183
185:     else:
186:         print("Not a developer")  # Line 185
```

**Output:**
```
=== Conditional Questions Demo ===
? Are you a developer? Yes
? How many years of experience?
  0-2 years
❯ 3-5 years
  6-10 years
  10+ years

Developer with 3-5 years of experience
```

**Annotation**:
- Lines 169-172: First question determines the workflow
- Lines 174-183: Follow-up question only appears if user is a developer
- Line 185: Alternative output if user is not a developer
- This demonstrates building dynamic, branching CLI workflows

---

## Key Features Demonstrated

1. **Text Input**: Simple string input with optional defaults
2. **Password**: Secure password input with hidden characters
3. **Confirm**: Yes/No boolean prompts
4. **Select**: Single selection from a list with arrow key navigation
5. **Checkbox**: Multiple selections using spacebar
6. **Raw Select**: Numbered selection shortcuts
7. **Autocomplete**: Type-ahead filtering of choices
8. **Path**: Filesystem path selection with autocomplete
9. **Custom Styling**: Complete visual customization
10. **Validation**: Custom input validation with error messages
11. **Conditional Logic**: Dynamic question flows based on previous answers

## Best Practices

1. **Provide defaults**: Use `default` parameter for common values
2. **Clear instructions**: Include helpful text in prompts (e.g., "use space to select")
3. **Validate inputs**: Use validation functions to ensure data quality
4. **Custom styles**: Match your brand or terminal theme
5. **Conditional logic**: Create smart, adaptive CLI experiences

## Additional Notes

- **Interactive Requirements**: Questionary requires a TTY (terminal) environment
- **Non-interactive Mode**: Automated/piped input has limitations
- **Error Handling**: All `.ask()` methods return `None` if user cancels (Ctrl+C)
- **Async Support**: Questionary also provides async versions of all prompts

## References

- **Library Documentation**: https://questionary.readthedocs.io/
- **GitHub Repository**: https://github.com/tmbo/questionary
- **Python Version**: Requires Python 3.8+ for inline script metadata (PEP 723)
