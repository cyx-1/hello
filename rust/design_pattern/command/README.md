# Command Design Pattern in Rust

The Command pattern encapsulates a request as an object, allowing you to parameterize clients with different requests, queue or log requests, and support undoable operations. This implementation demonstrates a text editor with full undo functionality using Rust's ownership system and smart pointers.

## Source Code

```rust
  1  // Command Design Pattern in Rust
  2  // Demonstrates a text editor with undo functionality
  3
  4  use std::cell::RefCell;
  5  use std::rc::Rc;
  6
  7  // Receiver: The object that performs the actual work
  8  struct TextEditor {
  9      content: String,
 10  }
 11
 12  impl TextEditor {
 13      fn new() -> Self {
 14          println!("[TextEditor] Created new text editor");
 15          TextEditor {
 16              content: String::new(),
 17          }
 18      }
 19
 20      fn insert(&mut self, text: &str, position: usize) {
 21          let pos = position.min(self.content.len());
 22          self.content.insert_str(pos, text);
 23          println!("[TextEditor] Inserted '{}' at position {}", text, pos);
 24      }
 25
 26      fn delete(&mut self, position: usize, length: usize) -> String {
 27          let pos = position.min(self.content.len());
 28          let end = (pos + length).min(self.content.len());
 29          let deleted: String = self.content.drain(pos..end).collect();
 30          println!("[TextEditor] Deleted '{}' from position {}", deleted, pos);
 31          deleted
 32      }
 33
 34      fn get_content(&self) -> &str {
 35          &self.content
 36      }
 37  }
 38
 39  // Command trait: The interface for all commands
 40  trait Command {
 41      fn execute(&mut self);
 42      fn undo(&mut self);
 43      fn description(&self) -> String;
 44  }
 45
 46  // Concrete Command: Insert text
 47  struct InsertCommand {
 48      editor: Rc<RefCell<TextEditor>>,
 49      text: String,
 50      position: usize,
 51  }
 52
 53  impl InsertCommand {
 54      fn new(editor: Rc<RefCell<TextEditor>>, text: String, position: usize) -> Self {
 55          InsertCommand {
 56              editor,
 57              text,
 58              position,
 59          }
 60      }
 61  }
 62
 63  impl Command for InsertCommand {
 64      fn execute(&mut self) {
 65          println!(">>> Executing InsertCommand: '{}' at {}", self.text, self.position);
 66          self.editor.borrow_mut().insert(&self.text, self.position);
 67      }
 68
 69      fn undo(&mut self) {
 70          println!("<<< Undoing InsertCommand: removing '{}' from {}", self.text, self.position);
 71          self.editor.borrow_mut().delete(self.position, self.text.len());
 72      }
 73
 74      fn description(&self) -> String {
 75          format!("Insert '{}' at position {}", self.text, self.position)
 76      }
 77  }
 78
 79  // Concrete Command: Delete text
 80  struct DeleteCommand {
 81      editor: Rc<RefCell<TextEditor>>,
 82      position: usize,
 83      length: usize,
 84      deleted_text: String, // Store for undo
 85  }
 86
 87  impl DeleteCommand {
 88      fn new(editor: Rc<RefCell<TextEditor>>, position: usize, length: usize) -> Self {
 89          DeleteCommand {
 90              editor,
 91              position,
 92              length,
 93              deleted_text: String::new(),
 94          }
 95      }
 96  }
 97
 98  impl Command for DeleteCommand {
 99      fn execute(&mut self) {
100          println!(">>> Executing DeleteCommand: {} chars at position {}", self.length, self.position);
101          self.deleted_text = self.editor.borrow_mut().delete(self.position, self.length);
102      }
103
104      fn undo(&mut self) {
105          println!("<<< Undoing DeleteCommand: restoring '{}' at {}", self.deleted_text, self.position);
106          self.editor.borrow_mut().insert(&self.deleted_text, self.position);
107      }
108
109      fn description(&self) -> String {
110          format!("Delete {} chars at position {}", self.length, self.position)
111      }
112  }
113
114  // Concrete Command: Replace text (combines delete + insert)
115  struct ReplaceCommand {
116      editor: Rc<RefCell<TextEditor>>,
117      position: usize,
118      old_length: usize,
119      new_text: String,
120      old_text: String, // Store for undo
121  }
122
123  impl ReplaceCommand {
124      fn new(editor: Rc<RefCell<TextEditor>>, position: usize, old_length: usize, new_text: String) -> Self {
125          ReplaceCommand {
126              editor,
127              position,
128              old_length,
129              new_text,
130              old_text: String::new(),
131          }
132      }
133  }
134
135  impl Command for ReplaceCommand {
136      fn execute(&mut self) {
137          println!(">>> Executing ReplaceCommand: {} chars with '{}' at {}", self.old_length, self.new_text, self.position);
138          self.old_text = self.editor.borrow_mut().delete(self.position, self.old_length);
139          self.editor.borrow_mut().insert(&self.new_text, self.position);
140      }
141
142      fn undo(&mut self) {
143          println!("<<< Undoing ReplaceCommand: restoring '{}' at {}", self.old_text, self.position);
144          self.editor.borrow_mut().delete(self.position, self.new_text.len());
145          self.editor.borrow_mut().insert(&self.old_text, self.position);
146      }
147
148      fn description(&self) -> String {
149          format!("Replace {} chars with '{}' at position {}", self.old_length, self.new_text, self.position)
150      }
151  }
152
153  // Invoker: Manages command execution and history
154  struct EditorController {
155      history: Vec<Box<dyn Command>>,
156      editor: Rc<RefCell<TextEditor>>,
157  }
158
159  impl EditorController {
160      fn new(editor: Rc<RefCell<TextEditor>>) -> Self {
161          println!("[EditorController] Created new controller");
162          EditorController {
163              history: Vec::new(),
164              editor,
165          }
166      }
167
168      fn execute_command(&mut self, mut command: Box<dyn Command>) {
169          println!("\n[EditorController] Executing: {}", command.description());
170          command.execute();
171          self.history.push(command);
172          self.print_content();
173      }
174
175      fn undo(&mut self) {
176          if let Some(mut command) = self.history.pop() {
177              println!("\n[EditorController] Undoing: {}", command.description());
178              command.undo();
179              self.print_content();
180          } else {
181              println!("\n[EditorController] Nothing to undo!");
182          }
183      }
184
185      fn print_content(&self) {
186          println!("[EditorController] Current content: \"{}\"", self.editor.borrow().get_content());
187      }
188
189      fn history_size(&self) -> usize {
190          self.history.len()
191      }
192  }
193
194  fn main() {
195      println!("=== Command Design Pattern Demo ===\n");
196
197      // Create the receiver
198      let editor = Rc::new(RefCell::new(TextEditor::new()));
199
200      // Create the invoker
201      let mut controller = EditorController::new(Rc::clone(&editor));
202
203      println!("\n--- Executing Commands ---");
204
205      // Create and execute commands
206      let cmd1 = Box::new(InsertCommand::new(Rc::clone(&editor), "Hello".to_string(), 0));
207      controller.execute_command(cmd1);
208
209      let cmd2 = Box::new(InsertCommand::new(Rc::clone(&editor), " World".to_string(), 5));
210      controller.execute_command(cmd2);
211
212      let cmd3 = Box::new(InsertCommand::new(Rc::clone(&editor), "!".to_string(), 11));
213      controller.execute_command(cmd3);
214
215      // Delete command
216      let cmd4 = Box::new(DeleteCommand::new(Rc::clone(&editor), 5, 6));
217      controller.execute_command(cmd4);
218
219      // Replace command
220      let cmd5 = Box::new(ReplaceCommand::new(Rc::clone(&editor), 0, 5, "Goodbye".to_string()));
221      controller.execute_command(cmd5);
222
223      println!("\n--- Command History ---");
224      println!("Total commands in history: {}", controller.history_size());
225
226      println!("\n--- Undoing Commands ---");
227
228      // Undo all commands
229      controller.undo(); // Undo Replace
230      controller.undo(); // Undo Delete
231      controller.undo(); // Undo Insert !
232      controller.undo(); // Undo Insert World
233      controller.undo(); // Undo Insert Hello
234
235      // Try to undo when history is empty
236      controller.undo();
237
238      println!("\n=== Demo Complete ===");
239  }
```

## Program Output

```
=== Command Design Pattern Demo ===

[TextEditor] Created new text editor
[EditorController] Created new controller

--- Executing Commands ---

[EditorController] Executing: Insert 'Hello' at position 0
>>> Executing InsertCommand: 'Hello' at 0
[TextEditor] Inserted 'Hello' at position 0
[EditorController] Current content: "Hello"

[EditorController] Executing: Insert ' World' at position 5
>>> Executing InsertCommand: ' World' at 5
[TextEditor] Inserted ' World' at position 5
[EditorController] Current content: "Hello World"

[EditorController] Executing: Insert '!' at position 11
>>> Executing InsertCommand: '!' at 11
[TextEditor] Inserted '!' at position 11
[EditorController] Current content: "Hello World!"

[EditorController] Executing: Delete 6 chars at position 5
>>> Executing DeleteCommand: 6 chars at position 5
[TextEditor] Deleted ' World' from position 5
[EditorController] Current content: "Hello!"

[EditorController] Executing: Replace 5 chars with 'Goodbye' at position 0
>>> Executing ReplaceCommand: 5 chars with 'Goodbye' at 0
[TextEditor] Deleted 'Hello' from position 0
[TextEditor] Inserted 'Goodbye' at position 0
[EditorController] Current content: "Goodbye!"

--- Command History ---
Total commands in history: 5

--- Undoing Commands ---

[EditorController] Undoing: Replace 5 chars with 'Goodbye' at position 0
<<< Undoing ReplaceCommand: restoring 'Hello' at 0
[TextEditor] Deleted 'Goodbye' from position 0
[TextEditor] Inserted 'Hello' at position 0
[EditorController] Current content: "Hello!"

[EditorController] Undoing: Delete 6 chars at position 5
<<< Undoing DeleteCommand: restoring ' World' at 5
[TextEditor] Inserted ' World' at position 5
[EditorController] Current content: "Hello World!"

[EditorController] Undoing: Insert '!' at position 11
<<< Undoing InsertCommand: removing '!' from 11
[TextEditor] Deleted '!' from position 11
[EditorController] Current content: "Hello World"

[EditorController] Undoing: Insert ' World' at position 5
<<< Undoing InsertCommand: removing ' World' from 5
[TextEditor] Deleted ' World' from position 5
[EditorController] Current content: "Hello"

[EditorController] Undoing: Insert 'Hello' at position 0
<<< Undoing InsertCommand: removing 'Hello' from 0
[TextEditor] Deleted 'Hello' from position 0
[EditorController] Current content: ""

[EditorController] Nothing to undo!

=== Demo Complete ===
```

## Code Annotations

### Key Sections Explained

#### Lines 4-5: Smart Pointer Imports
`Rc<RefCell<T>>` is the idiomatic Rust pattern for shared mutable state. `Rc` provides reference counting for multiple ownership, while `RefCell` enables interior mutability with runtime borrow checking.

#### Lines 8-37: Receiver (TextEditor)
The `TextEditor` struct is the receiver that performs the actual text manipulation operations. It contains:
- `insert()` (lines 20-24): Inserts text at a position, bounds-checked
- `delete()` (lines 26-32): Removes text and returns the deleted content for undo support
- `get_content()` (lines 34-36): Accessor for current content

#### Lines 39-44: Command Trait
The `Command` trait defines the interface for all commands with three methods:
- `execute(&mut self)`: Performs the command action
- `undo(&mut self)`: Reverses the command action
- `description(&self)`: Returns a human-readable description

#### Lines 46-77: InsertCommand
Stores the text and position for insertion. The undo operation (lines 69-72) simply deletes the same text that was inserted.

#### Lines 79-112: DeleteCommand
Uses `deleted_text` field (line 84) to store the removed text during execution (line 101), enabling restoration during undo (line 106).

#### Lines 114-151: ReplaceCommand
A composite command that combines delete and insert operations. Stores `old_text` (line 120) during execution for complete undo capability.

#### Lines 153-192: Invoker (EditorController)
The invoker manages command execution and maintains history:
- `history: Vec<Box<dyn Command>>` (line 155): Stores executed commands as trait objects
- `execute_command()` (lines 168-173): Executes and stores command in history
- `undo()` (lines 175-183): Pops last command from history and calls its undo method

#### Lines 194-239: Main Function
Demonstrates the complete workflow:
- Creates shared editor using `Rc::new(RefCell::new(...))` (line 198)
- Executes five commands building "Hello World!" then modifying to "Goodbye!"
- Undoes all commands in reverse order, returning to empty string

### Output to Source Code Correlation

| Output Line | Source Lines | Description |
|-------------|--------------|-------------|
| `[TextEditor] Created new text editor` | 14 | Constructor prints creation message |
| `[EditorController] Created new controller` | 161 | Controller initialization |
| `[EditorController] Executing: Insert 'Hello'...` | 169 | Invoker logs command execution |
| `>>> Executing InsertCommand: 'Hello' at 0` | 65 | InsertCommand.execute() entry |
| `[TextEditor] Inserted 'Hello' at position 0` | 23 | Receiver performs insertion |
| `[EditorController] Current content: "Hello"` | 186 | Invoker displays current state |
| `>>> Executing DeleteCommand: 6 chars...` | 100 | DeleteCommand.execute() entry |
| `[TextEditor] Deleted ' World' from position 5` | 30 | Receiver performs deletion |
| `>>> Executing ReplaceCommand...` | 137 | ReplaceCommand.execute() entry |
| `Total commands in history: 5` | 224 | History size after all executions |
| `[EditorController] Undoing: Replace...` | 177 | Invoker logs undo operation |
| `<<< Undoing ReplaceCommand: restoring 'Hello'` | 143 | ReplaceCommand.undo() entry |
| `[EditorController] Nothing to undo!` | 181 | Empty history condition |

### Key Characteristics of the Command Pattern in Rust

1. **Trait Objects for Polymorphism**: Using `Box<dyn Command>` allows storing different command types in the same collection while maintaining dynamic dispatch.

2. **Interior Mutability Pattern**: `Rc<RefCell<TextEditor>>` enables multiple commands to share and mutate the same receiver while satisfying Rust's ownership rules.

3. **State Preservation for Undo**: Each command stores the data needed to reverse its operation (e.g., `deleted_text` in DeleteCommand), following the memento-like pattern within commands.

4. **Separation of Concerns**:
   - Commands encapsulate actions and their inverse
   - Invoker manages execution flow and history
   - Receiver handles actual business logic

5. **Type Safety**: Rust's type system ensures commands properly implement all required methods, preventing runtime errors from missing undo implementations.

6. **Memory Safety**: The combination of `Rc` for shared ownership and `RefCell` for interior mutability provides memory-safe shared mutable state with runtime borrow checking.

## Running the Code

Compile and run with:
```bash
rustc main_command.rs -o main_command.exe && ./main_command.exe
```

No external dependencies are required. The code uses only Rust standard library components.
