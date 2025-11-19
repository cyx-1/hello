# Memento Design Pattern in Rust

## Description

The Memento pattern is a behavioral design pattern that allows you to save and restore the previous state of an object without revealing the details of its implementation. It is commonly used for implementing undo mechanisms, checkpoints, and state history features.

The pattern consists of three main components:
- **Originator**: The object whose state needs to be saved (TextEditor)
- **Memento**: A snapshot object that stores the originator's state (EditorMemento)
- **Caretaker**: Manages the collection of mementos without modifying them (History)

This example demonstrates a text editor with undo functionality, showing how states can be saved and restored.

---

## Source Code

```rust
  1  // Memento Design Pattern - Text Editor Example
  2  // Demonstrates save/restore functionality using Originator, Memento, and Caretaker
  3
  4  use std::time::{SystemTime, UNIX_EPOCH};
  5
  6  // Memento: Stores the internal state of the Originator
  7  // In Rust, we keep this struct's fields private to maintain encapsulation
  8  #[derive(Clone)]
  9  struct EditorMemento {
 10      content: String,
 11      cursor_position: usize,
 12      timestamp: u64,
 13  }
 14
 15  impl EditorMemento {
 16      fn get_timestamp(&self) -> u64 {
 17          self.timestamp
 18      }
 19  }
 20
 21  // Originator: The object whose state needs to be saved and restored
 22  struct TextEditor {
 23      content: String,
 24      cursor_position: usize,
 25  }
 26
 27  impl TextEditor {
 28      fn new() -> Self {
 29          println!("[Editor] Creating new text editor");
 30          TextEditor {
 31              content: String::new(),
 32              cursor_position: 0,
 33          }
 34      }
 35
 36      fn write(&mut self, text: &str) {
 37          self.content.push_str(text);
 38          self.cursor_position = self.content.len();
 39          println!("[Editor] Writing: \"{}\"", text);
 40          println!("[Editor] Current content: \"{}\"", self.content);
 41      }
 42
 43      fn set_cursor(&mut self, position: usize) {
 44          self.cursor_position = position.min(self.content.len());
 45          println!("[Editor] Cursor moved to position: {}", self.cursor_position);
 46      }
 47
 48      fn get_content(&self) -> &str {
 49          &self.content
 50      }
 51
 52      fn get_cursor_position(&self) -> usize {
 53          self.cursor_position
 54      }
 55
 56      // Save current state to a memento
 57      fn save(&self) -> EditorMemento {
 58          let timestamp = SystemTime::now()
 59              .duration_since(UNIX_EPOCH)
 60              .unwrap()
 61              .as_secs();
 62
 63          println!("[Editor] Saving state - Content: \"{}\", Cursor: {}",
 64                   self.content, self.cursor_position);
 65
 66          EditorMemento {
 67              content: self.content.clone(),
 68              cursor_position: self.cursor_position,
 69              timestamp,
 70          }
 71      }
 72
 73      // Restore state from a memento
 74      fn restore(&mut self, memento: &EditorMemento) {
 75          self.content = memento.content.clone();
 76          self.cursor_position = memento.cursor_position;
 77          println!("[Editor] Restoring state - Content: \"{}\", Cursor: {}",
 78                   self.content, self.cursor_position);
 79      }
 80  }
 81
 82  // Caretaker: Manages the history of mementos
 83  struct History {
 84      snapshots: Vec<EditorMemento>,
 85  }
 86
 87  impl History {
 88      fn new() -> Self {
 89          println!("[History] Creating new history manager");
 90          History {
 91              snapshots: Vec::new(),
 92          }
 93      }
 94
 95      fn push(&mut self, memento: EditorMemento) {
 96          println!("[History] Saving snapshot #{} (timestamp: {})",
 97                   self.snapshots.len() + 1, memento.get_timestamp());
 98          self.snapshots.push(memento);
 99      }
100
101      fn pop(&mut self) -> Option<EditorMemento> {
102          if let Some(memento) = self.snapshots.pop() {
103              println!("[History] Retrieving snapshot (timestamp: {})",
104                       memento.get_timestamp());
105              Some(memento)
106          } else {
107              println!("[History] No snapshots available!");
108              None
109          }
110      }
111
112      fn len(&self) -> usize {
113          self.snapshots.len()
114      }
115
116      fn is_empty(&self) -> bool {
117          self.snapshots.is_empty()
118      }
119  }
120
121  fn main() {
122      println!("=== Memento Pattern: Text Editor Example ===\n");
123
124      // Create the originator (text editor) and caretaker (history)
125      let mut editor = TextEditor::new();
126      let mut history = History::new();
127
128      println!("\n--- Step 1: Initial writing ---");
129      editor.write("Hello");
130      history.push(editor.save());
131
132      println!("\n--- Step 2: Continue writing ---");
133      editor.write(", World");
134      history.push(editor.save());
135
136      println!("\n--- Step 3: Add more text ---");
137      editor.write("! Welcome to Rust.");
138      editor.set_cursor(5);
139      history.push(editor.save());
140
141      println!("\n--- Step 4: Make a mistake ---");
142      editor.write(" OOPS! This should not be here.");
143      println!("[Main] Current editor state: \"{}\"", editor.get_content());
144
145      println!("\n--- Step 5: Undo last action (restore previous state) ---");
146      if let Some(memento) = history.pop() {
147          editor.restore(&memento);
148      }
149      println!("[Main] After undo: \"{}\"", editor.get_content());
150      println!("[Main] Cursor at position: {}", editor.get_cursor_position());
151
152      println!("\n--- Step 6: Undo again ---");
153      if let Some(memento) = history.pop() {
154          editor.restore(&memento);
155      }
156      println!("[Main] After second undo: \"{}\"", editor.get_content());
157
158      println!("\n--- Step 7: Undo once more ---");
159      if let Some(memento) = history.pop() {
160          editor.restore(&memento);
161      }
162      println!("[Main] After third undo: \"{}\"", editor.get_content());
163
164      println!("\n--- Step 8: Try to undo when history is empty ---");
165      if history.is_empty() {
166          println!("[Main] Cannot undo: History is empty");
167      } else if let Some(memento) = history.pop() {
168          editor.restore(&memento);
169      }
170
171      println!("\n--- Final State ---");
172      println!("[Main] Editor content: \"{}\"", editor.get_content());
173      println!("[Main] Remaining snapshots in history: {}", history.len());
174
175      println!("\n=== Memento Pattern Demo Complete ===");
176  }
```

---

## Program Output

```
=== Memento Pattern: Text Editor Example ===

[Editor] Creating new text editor
[History] Creating new history manager

--- Step 1: Initial writing ---
[Editor] Writing: "Hello"
[Editor] Current content: "Hello"
[Editor] Saving state - Content: "Hello", Cursor: 5
[History] Saving snapshot #1 (timestamp: 1763513953)

--- Step 2: Continue writing ---
[Editor] Writing: ", World"
[Editor] Current content: "Hello, World"
[Editor] Saving state - Content: "Hello, World", Cursor: 12
[History] Saving snapshot #2 (timestamp: 1763513953)

--- Step 3: Add more text ---
[Editor] Writing: "! Welcome to Rust."
[Editor] Current content: "Hello, World! Welcome to Rust."
[Editor] Cursor moved to position: 5
[Editor] Saving state - Content: "Hello, World! Welcome to Rust.", Cursor: 5
[History] Saving snapshot #3 (timestamp: 1763513953)

--- Step 4: Make a mistake ---
[Editor] Writing: " OOPS! This should not be here."
[Editor] Current content: "Hello, World! Welcome to Rust. OOPS! This should not be here."
[Main] Current editor state: "Hello, World! Welcome to Rust. OOPS! This should not be here."

--- Step 5: Undo last action (restore previous state) ---
[History] Retrieving snapshot (timestamp: 1763513953)
[Editor] Restoring state - Content: "Hello, World! Welcome to Rust.", Cursor: 5
[Main] After undo: "Hello, World! Welcome to Rust."
[Main] Cursor at position: 5

--- Step 6: Undo again ---
[History] Retrieving snapshot (timestamp: 1763513953)
[Editor] Restoring state - Content: "Hello, World", Cursor: 12
[Main] After second undo: "Hello, World"

--- Step 7: Undo once more ---
[History] Retrieving snapshot (timestamp: 1763513953)
[Editor] Restoring state - Content: "Hello", Cursor: 5
[Main] After third undo: "Hello"

--- Step 8: Try to undo when history is empty ---
[Main] Cannot undo: History is empty

--- Final State ---
[Main] Editor content: "Hello"
[Main] Remaining snapshots in history: 0

=== Memento Pattern Demo Complete ===
```

---

## Code Annotations

### Key Sections Explained

#### Memento Struct (Lines 8-19)
The `EditorMemento` struct stores the complete state of the text editor:
- **Line 8**: `#[derive(Clone)]` enables cloning of memento objects for safe state transfer
- **Lines 10-12**: Private fields ensure encapsulation - only the originator can access the full state
- **Lines 15-18**: Only a timestamp getter is exposed publicly; the actual state remains hidden

#### Originator - TextEditor (Lines 22-80)
The TextEditor is the object whose state we want to save and restore:
- **Lines 28-34**: Constructor initializes empty editor state
- **Lines 36-41**: `write()` method modifies the editor state and updates cursor position
- **Lines 43-46**: `set_cursor()` demonstrates additional state that gets preserved
- **Lines 57-71**: `save()` creates a memento containing the current state snapshot
- **Lines 74-79**: `restore()` replaces the current state with a memento's saved state

#### Caretaker - History (Lines 83-119)
The History manager maintains a stack of mementos:
- **Lines 83-85**: Uses `Vec<EditorMemento>` as a stack for LIFO (last-in-first-out) undo
- **Lines 95-99**: `push()` adds a new snapshot without inspecting its contents
- **Lines 101-110**: `pop()` retrieves and removes the most recent snapshot
- **Lines 116-118**: `is_empty()` prevents attempting undo with no history

#### Main Demonstration (Lines 121-176)
The main function demonstrates the complete workflow:
- **Lines 125-126**: Create originator and caretaker instances
- **Lines 129-130, 133-134, 137-139**: Write content and save snapshots
- **Lines 142-143**: Make a "mistake" that we'll want to undo
- **Lines 146-148, 153-155, 159-161**: Perform multiple undo operations
- **Lines 165-169**: Handle edge case when history is empty

---

### Output to Source Code Correlation

| Output Line | Source Lines | Description |
|-------------|--------------|-------------|
| `[Editor] Creating new text editor` | 29 | TextEditor::new() constructor message |
| `[History] Creating new history manager` | 89 | History::new() constructor message |
| `[Editor] Writing: "Hello"` | 39 | write() method showing text being added |
| `[Editor] Current content: "Hello"` | 40 | write() method showing full content |
| `[Editor] Saving state - Content: "Hello", Cursor: 5` | 63-64 | save() method creating memento |
| `[History] Saving snapshot #1` | 96-97 | History::push() storing memento |
| `[Editor] Cursor moved to position: 5` | 45 | set_cursor() method adjusting position |
| `[Main] Current editor state: "..."` | 143 | Main showing state before undo |
| `[History] Retrieving snapshot` | 103-104 | History::pop() returning memento |
| `[Editor] Restoring state - Content: "...", Cursor: ...` | 77-78 | restore() method applying memento |
| `[Main] After undo: "..."` | 149 | Main confirming successful restore |
| `[Main] Cannot undo: History is empty` | 166 | Empty history check in main |

---

## Key Characteristics of the Memento Pattern in Rust

### 1. Encapsulation Through Ownership
Rust's ownership model naturally enforces memento encapsulation. The `EditorMemento` struct has private fields that only the `TextEditor` can access, preventing external modification of saved states.

### 2. Safe State Transfer
Using `Clone` trait and explicit cloning (`content.clone()`) ensures that mementos contain independent copies of state, preventing unintended mutations. This is safer than reference-based approaches in other languages.

### 3. Memory Safety Without Garbage Collection
The `Vec<EditorMemento>` in History automatically manages memory. When mementos are popped and go out of scope, Rust automatically deallocates them.

### 4. Option Type for Safe Retrieval
The `pop()` method returns `Option<EditorMemento>`, forcing the caller to handle the case when no snapshots are available. This eliminates null pointer exceptions common in other languages.

### 5. Immutable Memento Access
By passing `&EditorMemento` to the `restore()` method, we ensure the memento cannot be modified during restoration. This maintains the integrity of saved states.

### 6. Compile-Time Guarantees
Rust's type system ensures:
- Mementos can only be created by the originator's `save()` method
- The caretaker cannot modify memento contents
- Memory is properly managed without manual intervention

### 7. Practical Applications
This pattern is ideal for:
- Text editors with undo/redo functionality
- Game save/load systems
- Database transaction rollbacks
- Form state preservation in web applications
- Configuration snapshots for system rollback

---

## Compilation

This code can be compiled with standard rustc:

```bash
rustc main_memento.rs -o main_memento && ./main_memento
```

No external dependencies are required beyond the Rust standard library.
