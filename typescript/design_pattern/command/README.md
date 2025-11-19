# Command Design Pattern in TypeScript

The Command pattern encapsulates a request as an object, thereby allowing parameterization of clients with different requests, queuing of requests, logging of requests, and support for undoable operations. This pattern decouples the object that invokes the operation from the one that knows how to perform it.

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
2    * Command Design Pattern in TypeScript
3    *
4    * The Command pattern encapsulates a request as an object, thereby allowing
5    * parameterization of clients with different requests, queuing of requests,
6    * and support for undoable operations.
7    */
8
9   // Command Interface - declares the execution and undo methods
10  interface Command {
11      execute(): void;
12      undo(): void;
13      getDescription(): string;
14  }
15
16  // Receiver - the object that performs the actual work
17  class TextEditor {
18      private content: string = "";
19      private cursorPosition: number = 0;
20
21      getContent(): string {
22          return this.content;
23      }
24
25      getCursorPosition(): number {
26          return this.cursorPosition;
27      }
28
29      setCursorPosition(position: number): void {
30          this.cursorPosition = Math.max(0, Math.min(position, this.content.length));
31          console.log(`[Line 31] TextEditor: Cursor moved to position ${this.cursorPosition}`);
32      }
33
34      insertAt(position: number, text: string): void {
35          const before = this.content.substring(0, position);
36          const after = this.content.substring(position);
37          this.content = before + text + after;
38          this.cursorPosition = position + text.length;
39          console.log(`[Line 38] TextEditor: Inserted "${text}" at position ${position}`);
40          console.log(`[Line 39] TextEditor: Content is now "${this.content}"`);
41      }
42
43      deleteRange(start: number, length: number): string {
44          const deleted = this.content.substring(start, start + length);
45          const before = this.content.substring(0, start);
46          const after = this.content.substring(start + length);
47          this.content = before + after;
48          this.cursorPosition = start;
49          console.log(`[Line 47] TextEditor: Deleted "${deleted}" from position ${start}`);
50          console.log(`[Line 48] TextEditor: Content is now "${this.content}"`);
51          return deleted;
52      }
53
54      replaceRange(start: number, length: number, newText: string): string {
55          const replaced = this.content.substring(start, start + length);
56          const before = this.content.substring(0, start);
57          const after = this.content.substring(start + length);
58          this.content = before + newText + after;
59          this.cursorPosition = start + newText.length;
60          console.log(`[Line 57] TextEditor: Replaced "${replaced}" with "${newText}" at position ${start}`);
61          console.log(`[Line 58] TextEditor: Content is now "${this.content}"`);
62          return replaced;
63      }
64
65      selectAll(): void {
66          console.log(`[Line 63] TextEditor: Selected all text - "${this.content}"`);
67      }
68
69      clear(): void {
70          this.content = "";
71          this.cursorPosition = 0;
72          console.log(`[Line 69] TextEditor: Cleared all content`);
73      }
74  }
75
76  // Concrete Command 1: Insert Text
77  class InsertTextCommand implements Command {
78      private editor: TextEditor;
79      private text: string;
80      private position: number;
81
82      constructor(editor: TextEditor, text: string, position: number) {
83          this.editor = editor;
84          this.text = text;
85          this.position = position;
86          console.log(`[Line 82] InsertTextCommand: Created command to insert "${text}" at position ${position}`);
87      }
88
89      execute(): void {
90          console.log(`[Line 86] InsertTextCommand: Executing insert`);
91          this.editor.insertAt(this.position, this.text);
92      }
93
94      undo(): void {
95          console.log(`[Line 91] InsertTextCommand: Undoing insert`);
96          this.editor.deleteRange(this.position, this.text.length);
97      }
98
99      getDescription(): string {
100         return `Insert "${this.text}" at position ${this.position}`;
101     }
102 }
103
104 // Concrete Command 2: Delete Text
105 class DeleteTextCommand implements Command {
106     private editor: TextEditor;
107     private position: number;
108     private length: number;
109     private deletedText: string = "";
110
111     constructor(editor: TextEditor, position: number, length: number) {
112         this.editor = editor;
113         this.position = position;
114         this.length = length;
115         console.log(`[Line 110] DeleteTextCommand: Created command to delete ${length} chars at position ${position}`);
116     }
117
118     execute(): void {
119         console.log(`[Line 114] DeleteTextCommand: Executing delete`);
120         this.deletedText = this.editor.deleteRange(this.position, this.length);
121     }
122
123     undo(): void {
124         console.log(`[Line 119] DeleteTextCommand: Undoing delete - restoring "${this.deletedText}"`);
125         this.editor.insertAt(this.position, this.deletedText);
126     }
127
128     getDescription(): string {
129         return `Delete ${this.length} characters at position ${this.position}`;
130     }
131 }
132
133 // Concrete Command 3: Replace Text
134 class ReplaceTextCommand implements Command {
135     private editor: TextEditor;
136     private position: number;
137     private length: number;
138     private newText: string;
139     private oldText: string = "";
140
141     constructor(editor: TextEditor, position: number, length: number, newText: string) {
142         this.editor = editor;
143         this.position = position;
144         this.length = length;
145         this.newText = newText;
146         console.log(`[Line 140] ReplaceTextCommand: Created command to replace ${length} chars with "${newText}" at position ${position}`);
147     }
148
149     execute(): void {
150         console.log(`[Line 144] ReplaceTextCommand: Executing replace`);
151         this.oldText = this.editor.replaceRange(this.position, this.length, this.newText);
152     }
153
154     undo(): void {
155         console.log(`[Line 149] ReplaceTextCommand: Undoing replace - restoring "${this.oldText}"`);
156         this.editor.replaceRange(this.position, this.newText.length, this.oldText);
157     }
158
159     getDescription(): string {
160         return `Replace ${this.length} characters with "${this.newText}" at position ${this.position}`;
161     }
162 }
163
164 // Concrete Command 4: Composite/Macro Command
165 class MacroCommand implements Command {
166     private commands: Command[] = [];
167     private name: string;
168
169     constructor(name: string) {
170         this.name = name;
171         console.log(`[Line 165] MacroCommand: Created macro "${name}"`);
172     }
173
174     addCommand(command: Command): void {
175         this.commands.push(command);
176         console.log(`[Line 170] MacroCommand: Added command to "${this.name}" - ${command.getDescription()}`);
177     }
178
179     execute(): void {
180         console.log(`[Line 174] MacroCommand: Executing macro "${this.name}" with ${this.commands.length} commands`);
181         for (const command of this.commands) {
182             command.execute();
183         }
184     }
185
186     undo(): void {
187         console.log(`[Line 181] MacroCommand: Undoing macro "${this.name}" (${this.commands.length} commands in reverse)`);
188         // Undo in reverse order
189         for (let i = this.commands.length - 1; i >= 0; i--) {
190             this.commands[i].undo();
191         }
192     }
193
194     getDescription(): string {
195         return `Macro "${this.name}" (${this.commands.length} commands)`;
196     }
197 }
198
199 // Invoker - manages command execution, history, and undo/redo
200 class CommandManager {
201     private history: Command[] = [];
202     private redoStack: Command[] = [];
203     private commandQueue: Command[] = [];
204
205     executeCommand(command: Command): void {
206         console.log(`\n[Line 199] CommandManager: Executing command - ${command.getDescription()}`);
207         command.execute();
208         this.history.push(command);
209         // Clear redo stack when new command is executed
210         this.redoStack = [];
211         console.log(`[Line 204] CommandManager: History size is now ${this.history.length}`);
212     }
213
214     queueCommand(command: Command): void {
215         this.commandQueue.push(command);
216         console.log(`[Line 209] CommandManager: Queued command - ${command.getDescription()}`);
217         console.log(`[Line 210] CommandManager: Queue size is now ${this.commandQueue.length}`);
218     }
219
220     executeQueue(): void {
221         console.log(`\n[Line 214] CommandManager: Executing queue of ${this.commandQueue.length} commands`);
222         while (this.commandQueue.length > 0) {
223             const command = this.commandQueue.shift()!;
224             console.log(`\n[Line 217] CommandManager: Dequeuing and executing - ${command.getDescription()}`);
225             command.execute();
226             this.history.push(command);
227         }
228         this.redoStack = [];
229         console.log(`[Line 222] CommandManager: Queue executed. History size is now ${this.history.length}`);
230     }
231
232     undo(): boolean {
233         if (this.history.length === 0) {
234             console.log(`[Line 227] CommandManager: Nothing to undo`);
235             return false;
236         }
237
238         const command = this.history.pop()!;
239         console.log(`\n[Line 232] CommandManager: Undoing - ${command.getDescription()}`);
240         command.undo();
241         this.redoStack.push(command);
242         console.log(`[Line 235] CommandManager: History size is now ${this.history.length}, Redo stack size is ${this.redoStack.length}`);
243         return true;
244     }
245
246     redo(): boolean {
247         if (this.redoStack.length === 0) {
248             console.log(`[Line 241] CommandManager: Nothing to redo`);
249             return false;
250         }
251
252         const command = this.redoStack.pop()!;
253         console.log(`\n[Line 246] CommandManager: Redoing - ${command.getDescription()}`);
254         command.execute();
255         this.history.push(command);
256         console.log(`[Line 249] CommandManager: History size is now ${this.history.length}, Redo stack size is ${this.redoStack.length}`);
257         return true;
258     }
259
260     getHistorySize(): number {
261         return this.history.length;
262     }
263
264     getRedoStackSize(): number {
265         return this.redoStack.length;
266     }
267
268     printHistory(): void {
269         console.log(`\n[Line 262] CommandManager: Command History (${this.history.length} items):`);
270         this.history.forEach((cmd, index) => {
271             console.log(`  ${index + 1}. ${cmd.getDescription()}`);
272         });
273     }
274 }
```

## Program Output

```
=== Command Pattern Demonstration ===
Text Editor with Undo/Redo Functionality


--- Demo 1: Basic Command Execution ---

[Line 82] InsertTextCommand: Created command to insert "Hello" at position 0

[Line 199] CommandManager: Executing command - Insert "Hello" at position 0
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted "Hello" at position 0
[Line 39] TextEditor: Content is now "Hello"
[Line 204] CommandManager: History size is now 1
[Line 82] InsertTextCommand: Created command to insert " World" at position 5

[Line 199] CommandManager: Executing command - Insert " World" at position 5
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted " World" at position 5
[Line 39] TextEditor: Content is now "Hello World"
[Line 204] CommandManager: History size is now 2
[Line 82] InsertTextCommand: Created command to insert "!" at position 11

[Line 199] CommandManager: Executing command - Insert "!" at position 11
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted "!" at position 11
[Line 39] TextEditor: Content is now "Hello World!"
[Line 204] CommandManager: History size is now 3

[Line 293] Current content: "Hello World!"

--- Demo 2: Undo Functionality ---

[Line 232] CommandManager: Undoing - Insert "!" at position 11
[Line 91] InsertTextCommand: Undoing insert
[Line 47] TextEditor: Deleted "!" from position 11
[Line 48] TextEditor: Content is now "Hello World"
[Line 235] CommandManager: History size is now 2, Redo stack size is 1
[Line 301] After undo: "Hello World"

[Line 232] CommandManager: Undoing - Insert " World" at position 5
[Line 91] InsertTextCommand: Undoing insert
[Line 47] TextEditor: Deleted " World" from position 5
[Line 48] TextEditor: Content is now "Hello"
[Line 235] CommandManager: History size is now 1, Redo stack size is 2
[Line 304] After undo: "Hello"

--- Demo 3: Redo Functionality ---

[Line 246] CommandManager: Redoing - Insert " World" at position 5
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted " World" at position 5
[Line 39] TextEditor: Content is now "Hello World"
[Line 249] CommandManager: History size is now 2, Redo stack size is 1
[Line 312] After redo: "Hello World"

--- Demo 4: Delete and Replace Commands ---

[Line 110] DeleteTextCommand: Created command to delete 5 chars at position 6

[Line 199] CommandManager: Executing command - Delete 5 characters at position 6
[Line 114] DeleteTextCommand: Executing delete
[Line 47] TextEditor: Deleted "World" from position 6
[Line 48] TextEditor: Content is now "Hello "
[Line 204] CommandManager: History size is now 3
[Line 140] ReplaceTextCommand: Created command to replace 6 chars with "Hi " at position 0

[Line 199] CommandManager: Executing command - Replace 6 characters with "Hi " at position 0
[Line 144] ReplaceTextCommand: Executing replace
[Line 57] TextEditor: Replaced "Hello " with "Hi " at position 0
[Line 58] TextEditor: Content is now "Hi "
[Line 204] CommandManager: History size is now 4
[Line 82] InsertTextCommand: Created command to insert "TypeScript" at position 3

[Line 199] CommandManager: Executing command - Insert "TypeScript" at position 3
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted "TypeScript" at position 3
[Line 39] TextEditor: Content is now "Hi TypeScript"
[Line 204] CommandManager: History size is now 5

[Line 330] Current content: "Hi TypeScript"

--- Demo 5: Command Queue ---

[Line 82] InsertTextCommand: Created command to insert " is" at position 13
[Line 209] CommandManager: Queued command - Insert " is" at position 13
[Line 210] CommandManager: Queue size is now 1
[Line 82] InsertTextCommand: Created command to insert " awesome" at position 16
[Line 209] CommandManager: Queued command - Insert " awesome" at position 16
[Line 210] CommandManager: Queue size is now 2
[Line 82] InsertTextCommand: Created command to insert "!" at position 24
[Line 209] CommandManager: Queued command - Insert "!" at position 24
[Line 210] CommandManager: Queue size is now 3

[Line 214] CommandManager: Executing queue of 3 commands

[Line 217] CommandManager: Dequeuing and executing - Insert " is" at position 13
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted " is" at position 13
[Line 39] TextEditor: Content is now "Hi TypeScript is"

[Line 217] CommandManager: Dequeuing and executing - Insert " awesome" at position 16
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted " awesome" at position 16
[Line 39] TextEditor: Content is now "Hi TypeScript is awesome"

[Line 217] CommandManager: Dequeuing and executing - Insert "!" at position 24
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted "!" at position 24
[Line 39] TextEditor: Content is now "Hi TypeScript is awesome!"
[Line 222] CommandManager: Queue executed. History size is now 8

[Line 345] After queue execution: "Hi TypeScript is awesome!"

--- Demo 6: Macro Command (Composite) ---

[Line 352] Undoing all commands to start fresh...

[Line 232] CommandManager: Undoing - Insert "!" at position 24
[Line 91] InsertTextCommand: Undoing insert
[Line 47] TextEditor: Deleted "!" from position 24
[Line 48] TextEditor: Content is now "Hi TypeScript is awesome"
[Line 235] CommandManager: History size is now 7, Redo stack size is 1

... (continues undoing all 8 commands) ...

[Line 232] CommandManager: Undoing - Insert "Hello" at position 0
[Line 91] InsertTextCommand: Undoing insert
[Line 47] TextEditor: Deleted "Hello" from position 0
[Line 48] TextEditor: Content is now ""
[Line 235] CommandManager: History size is now 0, Redo stack size is 8
[Line 356] Content after undoing all: ""
[Line 165] MacroCommand: Created macro "Format Greeting"
[Line 82] InsertTextCommand: Created command to insert ">>> " at position 0
[Line 170] MacroCommand: Added command to "Format Greeting" - Insert ">>> " at position 0
[Line 82] InsertTextCommand: Created command to insert "Welcome" at position 4
[Line 170] MacroCommand: Added command to "Format Greeting" - Insert "Welcome" at position 4
[Line 82] InsertTextCommand: Created command to insert " <<<" at position 11
[Line 170] MacroCommand: Added command to "Format Greeting" - Insert " <<<" at position 11

[Line 199] CommandManager: Executing command - Macro "Format Greeting" (3 commands)
[Line 174] MacroCommand: Executing macro "Format Greeting" with 3 commands
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted ">>> " at position 0
[Line 39] TextEditor: Content is now ">>> "
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted "Welcome" at position 4
[Line 39] TextEditor: Content is now ">>> Welcome"
[Line 86] InsertTextCommand: Executing insert
[Line 38] TextEditor: Inserted " <<<" at position 11
[Line 39] TextEditor: Content is now ">>> Welcome <<<"
[Line 204] CommandManager: History size is now 1

[Line 367] After macro execution: ">>> Welcome <<<"

[Line 232] CommandManager: Undoing - Macro "Format Greeting" (3 commands)
[Line 181] MacroCommand: Undoing macro "Format Greeting" (3 commands in reverse)
[Line 91] InsertTextCommand: Undoing insert
[Line 47] TextEditor: Deleted " <<<" from position 11
[Line 48] TextEditor: Content is now ">>> Welcome"
[Line 91] InsertTextCommand: Undoing insert
[Line 47] TextEditor: Deleted "Welcome" from position 4
[Line 48] TextEditor: Content is now ">>> "
[Line 91] InsertTextCommand: Undoing insert
[Line 47] TextEditor: Deleted ">>> " from position 0
[Line 48] TextEditor: Content is now ""
[Line 235] CommandManager: History size is now 0, Redo stack size is 1
[Line 371] After undoing macro: ""

[Line 246] CommandManager: Redoing - Macro "Format Greeting" (3 commands)
[Line 174] MacroCommand: Executing macro "Format Greeting" with 3 commands
... (re-executes all 3 commands) ...
[Line 39] TextEditor: Content is now ">>> Welcome <<<"
[Line 249] CommandManager: History size is now 1, Redo stack size is 0
[Line 375] After redoing macro: ">>> Welcome <<<"

--- Demo 7: Command History ---

[Line 262] CommandManager: Command History (1 items):
  1. Macro "Format Greeting" (3 commands)

--- Demo 8: Edge Cases ---

... (undoing the macro) ...
[Line 227] CommandManager: Nothing to undo

... (redoing the macro) ...

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Pattern Components

#### Command Interface (Lines 10-14)
- Defines the contract for all command objects
- `execute()` - performs the action
- `undo()` - reverses the action
- `getDescription()` - provides human-readable command info

#### Receiver (Lines 17-74)
- `TextEditor` - the object that performs actual text operations
- Methods: `insertAt()`, `deleteRange()`, `replaceRange()`
- Stores state that commands will modify

#### Concrete Commands (Lines 77-197)
- `InsertTextCommand` - inserts text at a position
- `DeleteTextCommand` - deletes text (stores deleted text for undo)
- `ReplaceTextCommand` - replaces text (stores old text for undo)
- `MacroCommand` - composite command that groups multiple commands

#### Invoker (Lines 200-274)
- `CommandManager` - manages command execution and history
- Maintains `history` stack for undo
- Maintains `redoStack` for redo
- Supports command queuing for batch execution

### Output Correlation

| Output Line | Source Line | Explanation |
|-------------|-------------|-------------|
| `InsertTextCommand: Created command` | Line 86 | Command object instantiated with parameters |
| `CommandManager: Executing command` | Line 206 | Invoker delegates to command's execute() |
| `InsertTextCommand: Executing insert` | Line 90 | Command invokes receiver's method |
| `TextEditor: Inserted` | Line 39 | Receiver performs actual operation |
| `CommandManager: History size is now 1` | Line 211 | Command added to undo history |
| `CommandManager: Undoing` | Line 239 | Invoker pops command and calls undo() |
| `InsertTextCommand: Undoing insert` | Line 95 | Command's undo implementation |
| `TextEditor: Deleted` | Line 49 | Receiver reverses the operation |
| `Redo stack size is 1` | Line 242 | Undone command moved to redo stack |
| `CommandManager: Redoing` | Line 253 | Invoker pops from redo stack, re-executes |

### Key Operations Flow

#### Insert and Undo Flow
1. Client creates `InsertTextCommand("Hello", 0)` - Line 82
2. Invoker calls `executeCommand()` - Line 206
3. Command calls `editor.insertAt()` - Line 91
4. On undo, command calls `editor.deleteRange()` - Line 96
5. Deleted text matches inserted text exactly

#### Delete and Undo Flow
1. Client creates `DeleteTextCommand(6, 5)` - Line 115
2. Command stores deleted text during `execute()` - Line 120
3. On undo, command restores text with `insertAt()` - Line 125
4. Original text is perfectly restored

#### Macro Command Flow
1. Create `MacroCommand("Format Greeting")` - Line 171
2. Add multiple commands - Line 176
3. Execute runs all commands in sequence - Lines 180-183
4. Undo runs all commands in reverse order - Lines 188-191
5. Single undo/redo handles entire macro

### Why Command Pattern Works

1. **Encapsulation**: Each operation is a self-contained object
   - Insert command knows how to insert AND delete
   - Replace command knows how to replace AND restore

2. **Undo/Redo Support**: Commands store state for reversal
   - `DeleteTextCommand` stores `deletedText`
   - `ReplaceTextCommand` stores `oldText`

3. **Command Queuing**: Commands can be stored and executed later
   - Queue commands without immediate execution (Lines 214-217)
   - Execute all at once (Line 221)

4. **Composite Commands**: Macros group multiple commands
   - Single undo undoes entire macro
   - Commands are reusable building blocks

5. **Decoupling**: Invoker doesn't know command implementation
   - `CommandManager` only knows `Command` interface
   - New commands can be added without changing invoker

### State Transformations

| Demo | Operation | Before | After |
|------|-----------|--------|-------|
| 1 | Insert "Hello" | "" | "Hello" |
| 1 | Insert " World" | "Hello" | "Hello World" |
| 1 | Insert "!" | "Hello World" | "Hello World!" |
| 2 | Undo "!" | "Hello World!" | "Hello World" |
| 2 | Undo " World" | "Hello World" | "Hello" |
| 3 | Redo " World" | "Hello" | "Hello World" |
| 4 | Delete "World" | "Hello World" | "Hello " |
| 4 | Replace "Hello " | "Hello " | "Hi " |
| 4 | Insert "TypeScript" | "Hi " | "Hi TypeScript" |
| 5 | Queue + Execute | "Hi TypeScript" | "Hi TypeScript is awesome!" |
| 6 | Macro execute | "" | ">>> Welcome <<<" |

### Use Cases

- **Text Editors**: Undo/redo functionality for text operations
- **Graphics Applications**: Drawing operations with history
- **Database Transactions**: Rollback support for operations
- **Game Development**: Replay systems and action queues
- **Workflow Systems**: Task scheduling and execution
- **Remote Control**: Button actions as command objects
- **Menu Systems**: Menu items as executable commands
