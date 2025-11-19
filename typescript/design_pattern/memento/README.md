# Memento Design Pattern in TypeScript

## Pattern Description

The **Memento Design Pattern** is a behavioral design pattern that allows capturing and externalizing an object's internal state without violating encapsulation, so the object can be restored to this state later. This pattern is particularly useful for implementing **undo/redo functionality**, **checkpoints**, and **state snapshots**.

### Key Components

| Component | Role | Description |
|-----------|------|-------------|
| **Originator** | State owner | The object whose state needs to be saved and restored |
| **Memento** | State snapshot | Stores the internal state of the Originator at a given time |
| **Caretaker** | History manager | Responsible for keeping track of multiple mementos |

### Use Cases

- Text editor undo/redo operations
- Game save/load functionality
- Transaction rollback systems
- State history in form wizards
- Version control systems

## Requirements

- **Node.js**: 18.0.0 or higher
- **TypeScript**: 5.3.0 or higher
- **tsx**: 4.7.0 or higher (for running TypeScript directly)

## How to Run

```bash
# Navigate to the memento directory
cd typescript/memento

# Install dependencies
npm install

# Run the demonstration
npm run start
```

## Source Code

```typescript
     1  /**
     2   * Memento Design Pattern in TypeScript
     3   *
     4   * The Memento pattern allows capturing and externalizing an object's internal
     5   * state so that it can be restored later, without violating encapsulation.
     6   * This is commonly used for implementing undo/redo functionality.
     7   *
     8   * Components:
     9   * - Originator: The object whose state needs to be saved
    10   * - Memento: Stores the internal state of the Originator
    11   * - Caretaker: Manages the mementos (history)
    12   */
    13
    14  // ============================================================
    15  // Memento - Stores the state of the Originator
    16  // ============================================================
    17  class EditorMemento {
    18      private readonly content: string;
    19      private readonly cursorPosition: number;
    20      private readonly selectionStart: number;
    21      private readonly selectionEnd: number;
    22      private readonly timestamp: Date;
    23
    24      constructor(
    25          content: string,
    26          cursorPosition: number,
    27          selectionStart: number,
    28          selectionEnd: number
    29      ) {
    30          this.content = content;
    31          this.cursorPosition = cursorPosition;
    32          this.selectionStart = selectionStart;
    33          this.selectionEnd = selectionEnd;
    34          this.timestamp = new Date();
    35          console.log(`[Line 32] EditorMemento: Created snapshot at ${this.timestamp.toISOString()}`);
    36      }
    37
    38      // Getters for the Originator to restore state
    39      getContent(): string {
    40          return this.content;
    41      }
    42
    43      getCursorPosition(): number {
    44          return this.cursorPosition;
    45      }
    46
    47      getSelectionStart(): number {
    48          return this.selectionStart;
    49      }
    50
    51      getSelectionEnd(): number {
    52          return this.selectionEnd;
    53      }
    54
    55      getTimestamp(): Date {
    56          return this.timestamp;
    57      }
    58
    59      // For display purposes
    60      getDescription(): string {
    61          const preview = this.content.length > 30
    62              ? this.content.substring(0, 30) + "..."
    63              : this.content;
    64          return `"${preview}" (cursor: ${this.cursorPosition})`;
    65      }
    66  }
    67
    68  // ============================================================
    69  // Originator - The object whose state we want to save
    70  // ============================================================
    71  class TextEditor {
    72      private content: string = "";
    73      private cursorPosition: number = 0;
    74      private selectionStart: number = 0;
    75      private selectionEnd: number = 0;
    76
    77      // Create a memento (save state)
    78      save(): EditorMemento {
    79          console.log(`[Line 72] TextEditor: Saving current state...`);
    80          return new EditorMemento(
    81              this.content,
    82              this.cursorPosition,
    83              this.selectionStart,
    84              this.selectionEnd
    85          );
    86      }
    87
    88      // Restore from memento
    89      restore(memento: EditorMemento): void {
    90          this.content = memento.getContent();
    91          this.cursorPosition = memento.getCursorPosition();
    92          this.selectionStart = memento.getSelectionStart();
    93          this.selectionEnd = memento.getSelectionEnd();
    94          console.log(`[Line 87] TextEditor: Restored state from ${memento.getTimestamp().toISOString()}`);
    95      }
    96
    97      // Editor operations
    98      type(text: string): void {
    99          const before = this.content.substring(0, this.cursorPosition);
   100          const after = this.content.substring(this.cursorPosition);
   101          this.content = before + text + after;
   102          this.cursorPosition += text.length;
   103          this.selectionStart = this.cursorPosition;
   104          this.selectionEnd = this.cursorPosition;
   105          console.log(`[Line 98] TextEditor: Typed "${text}" at position ${this.cursorPosition - text.length}`);
   106      }
   107
   108      delete(count: number): void {
   109          if (this.cursorPosition > 0 && count > 0) {
   110              const deleteStart = Math.max(0, this.cursorPosition - count);
   111              const deleted = this.content.substring(deleteStart, this.cursorPosition);
   112              const before = this.content.substring(0, deleteStart);
   113              const after = this.content.substring(this.cursorPosition);
   114              this.content = before + after;
   115              this.cursorPosition = deleteStart;
   116              console.log(`[Line 109] TextEditor: Deleted "${deleted}"`);
   117          }
   118      }
   119
   120      moveCursor(position: number): void {
   121          this.cursorPosition = Math.max(0, Math.min(position, this.content.length));
   122          this.selectionStart = this.cursorPosition;
   123          this.selectionEnd = this.cursorPosition;
   124          console.log(`[Line 117] TextEditor: Moved cursor to position ${this.cursorPosition}`);
   125      }
   126
   127      select(start: number, end: number): void {
   128          this.selectionStart = Math.max(0, Math.min(start, this.content.length));
   129          this.selectionEnd = Math.max(0, Math.min(end, this.content.length));
   130          this.cursorPosition = this.selectionEnd;
   131          const selected = this.content.substring(this.selectionStart, this.selectionEnd);
   132          console.log(`[Line 125] TextEditor: Selected "${selected}" (${this.selectionStart}-${this.selectionEnd})`);
   133      }
   134
   135      replaceSelection(text: string): void {
   136          if (this.selectionStart !== this.selectionEnd) {
   137              const before = this.content.substring(0, this.selectionStart);
   138              const after = this.content.substring(this.selectionEnd);
   139              const replaced = this.content.substring(this.selectionStart, this.selectionEnd);
   140              this.content = before + text + after;
   141              this.cursorPosition = this.selectionStart + text.length;
   142              this.selectionStart = this.cursorPosition;
   143              this.selectionEnd = this.cursorPosition;
   144              console.log(`[Line 137] TextEditor: Replaced "${replaced}" with "${text}"`);
   145          }
   146      }
   147
   148      getContent(): string {
   149          return this.content;
   150      }
   151
   152      getCursorPosition(): number {
   153          return this.cursorPosition;
   154      }
   155
   156      display(): void {
   157          console.log(`[Line 150] TextEditor Display:`);
   158          console.log(`  Content: "${this.content}"`);
   159          console.log(`  Cursor Position: ${this.cursorPosition}`);
   160          if (this.selectionStart !== this.selectionEnd) {
   161              console.log(`  Selection: ${this.selectionStart}-${this.selectionEnd}`);
   162          }
   163      }
   164  }
   165
   166  // ============================================================
   167  // Caretaker - Manages the history of mementos
   168  // ============================================================
   169  class History {
   170      private undoStack: EditorMemento[] = [];
   171      private redoStack: EditorMemento[] = [];
   172      private maxHistory: number;
   173
   174      constructor(maxHistory: number = 50) {
   175          this.maxHistory = maxHistory;
   176          console.log(`[Line 168] History: Initialized with max ${maxHistory} snapshots`);
   177      }
   178
   179      // Push a new state to history
   180      push(memento: EditorMemento): void {
   181          // Clear redo stack when new action is performed
   182          if (this.redoStack.length > 0) {
   183              console.log(`[Line 175] History: Clearing ${this.redoStack.length} redo states`);
   184              this.redoStack = [];
   185          }
   186
   187          this.undoStack.push(memento);
   188          console.log(`[Line 180] History: Pushed state - ${memento.getDescription()}`);
   189
   190          // Limit history size
   191          if (this.undoStack.length > this.maxHistory) {
   192              this.undoStack.shift();
   193              console.log(`[Line 185] History: Removed oldest state (exceeded max history)`);
   194          }
   195      }
   196
   197      // Get the previous state for undo
   198      undo(currentState: EditorMemento): EditorMemento | null {
   199          if (this.undoStack.length === 0) {
   200              console.log(`[Line 192] History: Nothing to undo`);
   201              return null;
   202          }
   203
   204          const previousState = this.undoStack.pop()!;
   205          this.redoStack.push(currentState);
   206          console.log(`[Line 198] History: Undo - moving to ${previousState.getDescription()}`);
   207          return previousState;
   208      }
   209
   210      // Get the next state for redo
   211      redo(): EditorMemento | null {
   212          if (this.redoStack.length === 0) {
   213              console.log(`[Line 205] History: Nothing to redo`);
   214              return null;
   215          }
   216
   217          const nextState = this.redoStack.pop()!;
   218          this.undoStack.push(nextState);
   219          console.log(`[Line 211] History: Redo - moving to ${nextState.getDescription()}`);
   220          return nextState;
   221      }
   222
   223      // Get history info
   224      getUndoCount(): number {
   225          return this.undoStack.length;
   226      }
   227
   228      getRedoCount(): number {
   229          return this.redoStack.length;
   230      }
   231
   232      displayHistory(): void {
   233          console.log(`[Line 225] History Status:`);
   234          console.log(`  Undo stack: ${this.undoStack.length} states`);
   235          console.log(`  Redo stack: ${this.redoStack.length} states`);
   236          if (this.undoStack.length > 0) {
   237              console.log(`  Latest undo: ${this.undoStack[this.undoStack.length - 1].getDescription()}`);
   238          }
   239      }
   240  }
   241
   242  // ============================================================
   243  // EditorApplication - Combines all components
   244  // ============================================================
   245  class EditorApplication {
   246      private editor: TextEditor;
   247      private history: History;
   248
   249      constructor() {
   250          this.editor = new TextEditor();
   251          this.history = new History(100);
   252          console.log(`[Line 243] EditorApplication: Initialized`);
   253      }
   254
   255      // Perform action and save to history
   256      private saveState(): void {
   257          const memento = this.editor.save();
   258          this.history.push(memento);
   259      }
   260
   261      type(text: string): void {
   262          this.saveState();
   263          this.editor.type(text);
   264      }
   265
   266      delete(count: number): void {
   267          this.saveState();
   268          this.editor.delete(count);
   269      }
   270
   271      moveCursor(position: number): void {
   272          this.editor.moveCursor(position);
   273      }
   274
   275      select(start: number, end: number): void {
   276          this.editor.select(start, end);
   277      }
   278
   279      replaceSelection(text: string): void {
   280          this.saveState();
   281          this.editor.replaceSelection(text);
   282      }
   283
   284      undo(): void {
   285          console.log(`\n[Line 277] EditorApplication: Performing UNDO`);
   286          const currentState = this.editor.save();
   287          const previousState = this.history.undo(currentState);
   288          if (previousState) {
   289              this.editor.restore(previousState);
   290          }
   291      }
   292
   293      redo(): void {
   294          console.log(`\n[Line 286] EditorApplication: Performing REDO`);
   295          const nextState = this.history.redo();
   296          if (nextState) {
   297              this.editor.restore(nextState);
   298          }
   299      }
   300
   301      display(): void {
   302          this.editor.display();
   303          this.history.displayHistory();
   304      }
   305
   306      getContent(): string {
   307          return this.editor.getContent();
   308      }
   309  }
   310
   311  // ============================================================
   312  // Second Example: Game Save State
   313  // ============================================================
   314
   315  // Memento for game state
   316  class GameMemento {
   317      private readonly playerHealth: number;
   318      private readonly playerPosition: { x: number; y: number };
   319      private readonly score: number;
   320      private readonly level: number;
   321      private readonly inventory: string[];
   322      private readonly timestamp: Date;
   323
   324      constructor(
   325          health: number,
   326          position: { x: number; y: number },
   327          score: number,
   328          level: number,
   329          inventory: string[]
   330      ) {
   331          this.playerHealth = health;
   332          this.playerPosition = { ...position };
   333          this.score = score;
   334          this.level = level;
   335          this.inventory = [...inventory];
   336          this.timestamp = new Date();
   337          console.log(`[Line 325] GameMemento: Created save state - Level ${level}, Score ${score}`);
   338      }
   339
   340      getHealth(): number { return this.playerHealth; }
   341      getPosition(): { x: number; y: number } { return { ...this.playerPosition }; }
   342      getScore(): number { return this.score; }
   343      getLevel(): number { return this.level; }
   344      getInventory(): string[] { return [...this.inventory]; }
   345      getTimestamp(): Date { return this.timestamp; }
   346  }
   347
   348  // Originator - Game state
   349  class Game {
   350      private health: number = 100;
   351      private position: { x: number; y: number } = { x: 0, y: 0 };
   352      private score: number = 0;
   353      private level: number = 1;
   354      private inventory: string[] = [];
   355
   356      save(): GameMemento {
   357          console.log(`[Line 344] Game: Creating save state...`);
   358          return new GameMemento(
   359              this.health,
   360              this.position,
   361              this.score,
   362              this.level,
   363              this.inventory
   364          );
   365      }
   366
   367      restore(memento: GameMemento): void {
   368          this.health = memento.getHealth();
   369          this.position = memento.getPosition();
   370          this.score = memento.getScore();
   371          this.level = memento.getLevel();
   372          this.inventory = memento.getInventory();
   373          console.log(`[Line 360] Game: Restored to Level ${this.level}, Score ${this.score}`);
   374      }
   375
   376      // Game actions
   377      move(dx: number, dy: number): void {
   378          this.position.x += dx;
   379          this.position.y += dy;
   380          console.log(`[Line 367] Game: Moved to (${this.position.x}, ${this.position.y})`);
   381      }
   382
   383      takeDamage(damage: number): void {
   384          this.health = Math.max(0, this.health - damage);
   385          console.log(`[Line 372] Game: Took ${damage} damage. Health: ${this.health}`);
   386      }
   387
   388      heal(amount: number): void {
   389          this.health = Math.min(100, this.health + amount);
   390          console.log(`[Line 377] Game: Healed ${amount}. Health: ${this.health}`);
   391      }
   392
   393      addScore(points: number): void {
   394          this.score += points;
   395          console.log(`[Line 382] Game: Added ${points} points. Score: ${this.score}`);
   396      }
   397
   398      collectItem(item: string): void {
   399          this.inventory.push(item);
   400          console.log(`[Line 387] Game: Collected "${item}". Inventory: [${this.inventory.join(", ")}]`);
   401      }
   402
   403      nextLevel(): void {
   404          this.level++;
   405          this.position = { x: 0, y: 0 };
   406          console.log(`[Line 393] Game: Advanced to Level ${this.level}`);
   407      }
   408
   409      display(): void {
   410          console.log(`[Line 397] Game State:`);
   411          console.log(`  Level: ${this.level}`);
   412          console.log(`  Health: ${this.health}`);
   413          console.log(`  Score: ${this.score}`);
   414          console.log(`  Position: (${this.position.x}, ${this.position.y})`);
   415          console.log(`  Inventory: [${this.inventory.join(", ")}]`);
   416      }
   417
   418      getHealth(): number { return this.health; }
   419  }
   420
   421  // Caretaker - Save slots
   422  class SaveManager {
   423      private saveSlots: Map<string, GameMemento> = new Map();
   424
   425      saveGame(slotName: string, memento: GameMemento): void {
   426          this.saveSlots.set(slotName, memento);
   427          console.log(`[Line 413] SaveManager: Saved game to slot "${slotName}"`);
   428      }
   429
   430      loadGame(slotName: string): GameMemento | null {
   431          const memento = this.saveSlots.get(slotName);
   432          if (memento) {
   433              console.log(`[Line 419] SaveManager: Loading from slot "${slotName}"`);
   434              return memento;
   435          }
   436          console.log(`[Line 422] SaveManager: No save found in slot "${slotName}"`);
   437          return null;
   438      }
   439
   440      listSaves(): void {
   441          console.log(`[Line 427] SaveManager: Available saves:`);
   442          for (const [slot, memento] of this.saveSlots) {
   443              console.log(`  - ${slot}: Level ${memento.getLevel()}, Score ${memento.getScore()}`);
   444          }
   445      }
   446  }
```

## Program Output

```
============================================================
  Memento Design Pattern Demonstration
============================================================

--- Demo 1: Text Editor with Undo/Redo ---

[Line 168] History: Initialized with max 100 snapshots
[Line 243] EditorApplication: Initialized

[Action] Typing 'Hello World'...
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.113Z
[Line 180] History: Pushed state - "" (cursor: 0)
[Line 98] TextEditor: Typed "Hello" at position 0
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.114Z
[Line 180] History: Pushed state - "Hello" (cursor: 5)
[Line 98] TextEditor: Typed " " at position 5
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.115Z
[Line 180] History: Pushed state - "Hello " (cursor: 6)
[Line 98] TextEditor: Typed "World" at position 6
[Line 150] TextEditor Display:
  Content: "Hello World"
  Cursor Position: 11
[Line 225] History Status:
  Undo stack: 3 states
  Redo stack: 0 states
  Latest undo: "Hello " (cursor: 6)

[Action] Typing '!!!'...
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.115Z
[Line 180] History: Pushed state - "Hello World" (cursor: 11)
[Line 98] TextEditor: Typed "!!!" at position 11
[Line 150] TextEditor Display:
  Content: "Hello World!!!"
  Cursor Position: 14
[Line 225] History Status:
  Undo stack: 4 states
  Redo stack: 0 states
  Latest undo: "Hello World" (cursor: 11)

[Action] Performing Undo...

[Line 277] EditorApplication: Performing UNDO
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.116Z
[Line 198] History: Undo - moving to "Hello World" (cursor: 11)
[Line 87] TextEditor: Restored state from 2025-11-19T01:02:36.115Z
Content after undo: "Hello World"

[Action] Performing another Undo...

[Line 277] EditorApplication: Performing UNDO
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.116Z
[Line 198] History: Undo - moving to "Hello " (cursor: 6)
[Line 87] TextEditor: Restored state from 2025-11-19T01:02:36.115Z
Content after undo: "Hello "

[Action] Performing Redo...

[Line 286] EditorApplication: Performing REDO
[Line 211] History: Redo - moving to "Hello World" (cursor: 11)
[Line 87] TextEditor: Restored state from 2025-11-19T01:02:36.116Z
Content after redo: "Hello World"

[Action] Typing ' - TypeScript'...
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.117Z
[Line 175] History: Clearing 1 redo states
[Line 180] History: Pushed state - "Hello World" (cursor: 11)
[Line 98] TextEditor: Typed " - TypeScript" at position 11
Content: "Hello World - TypeScript"

[Action] Trying to Redo (should have nothing)...

[Line 286] EditorApplication: Performing REDO
[Line 205] History: Nothing to redo
Content: "Hello World - TypeScript"

[Action] Select and replace 'World' with 'Memento'...
[Line 125] TextEditor: Selected "World" (6-11)
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.117Z
[Line 180] History: Pushed state - "Hello World - TypeScript" (cursor: 11)
[Line 137] TextEditor: Replaced "World" with "Memento"
Content: "Hello Memento - TypeScript"

[Action] Multiple undos to go back to 'Hello'...

[Line 277] EditorApplication: Performing UNDO
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.117Z
[Line 198] History: Undo - moving to "Hello World - TypeScript" (cursor: 11)
[Line 87] TextEditor: Restored state from 2025-11-19T01:02:36.117Z

[Line 277] EditorApplication: Performing UNDO
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.118Z
[Line 198] History: Undo - moving to "Hello World" (cursor: 11)
[Line 87] TextEditor: Restored state from 2025-11-19T01:02:36.117Z

[Line 277] EditorApplication: Performing UNDO
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.118Z
[Line 198] History: Undo - moving to "Hello World" (cursor: 11)
[Line 87] TextEditor: Restored state from 2025-11-19T01:02:36.116Z

[Line 277] EditorApplication: Performing UNDO
[Line 72] TextEditor: Saving current state...
[Line 32] EditorMemento: Created snapshot at 2025-11-19T01:02:36.118Z
[Line 198] History: Undo - moving to "Hello" (cursor: 5)
[Line 87] TextEditor: Restored state from 2025-11-19T01:02:36.114Z
Content after multiple undos: "Hello"


--- Demo 2: Game Save States ---


[Action] Playing through Level 1...
[Line 367] Game: Moved to (5, 3)
[Line 387] Game: Collected "Sword". Inventory: [Sword]
[Line 382] Game: Added 100 points. Score: 100
[Line 372] Game: Took 20 damage. Health: 80

[Action] Saving game to 'checkpoint1'...
[Line 344] Game: Creating save state...
[Line 325] GameMemento: Created save state - Level 1, Score 100
[Line 413] SaveManager: Saved game to slot "checkpoint1"

[Action] Continuing to play...
[Line 367] Game: Moved to (15, 8)
[Line 387] Game: Collected "Shield". Inventory: [Sword, Shield]
[Line 382] Game: Added 200 points. Score: 300
[Line 372] Game: Took 50 damage. Health: 30

[Action] Saving game to 'checkpoint2'...
[Line 344] Game: Creating save state...
[Line 325] GameMemento: Created save state - Level 1, Score 300
[Line 413] SaveManager: Saved game to slot "checkpoint2"

[Action] Dangerous area - taking heavy damage...
[Line 372] Game: Took 40 damage. Health: 0
[Line 397] Game State:
  Level: 1
  Health: 0
  Score: 300
  Position: (15, 8)
  Inventory: [Sword, Shield]

[Action] Game over! Loading from checkpoint2...
[Line 419] SaveManager: Loading from slot "checkpoint2"
[Line 360] Game: Restored to Level 1, Score 300
[Line 397] Game State:
  Level: 1
  Health: 30
  Score: 300
  Position: (15, 8)
  Inventory: [Sword, Shield]

[Action] Want to restart level? Loading checkpoint1...
[Line 419] SaveManager: Loading from slot "checkpoint1"
[Line 360] Game: Restored to Level 1, Score 100
[Line 397] Game State:
  Level: 1
  Health: 80
  Score: 100
  Position: (5, 3)
  Inventory: [Sword]

[Action] Listing all save slots...
[Line 427] SaveManager: Available saves:
  - checkpoint1: Level 1, Score 100
  - checkpoint2: Level 1, Score 300

============================================================
  End of Demonstration
============================================================
```

## Code Analysis and Annotations

### Demo 1: Text Editor with Undo/Redo

This example demonstrates a text editor with complete undo/redo functionality using the Memento pattern.

#### Initialization Phase

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 168] History: Initialized...` | Line 174-176 | The History (Caretaker) initializes with a maximum of 100 snapshots to prevent unbounded memory growth |
| `[Line 243] EditorApplication: Initialized` | Line 249-252 | The application creates a TextEditor (Originator) and History (Caretaker) |

#### Typing Operations - State Saving Flow

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 72] TextEditor: Saving current state...` | Line 78-79 | Before each type operation, the editor creates a snapshot of its current state |
| `[Line 32] EditorMemento: Created snapshot...` | Line 30-35 | The Memento stores content, cursor position, selection, and timestamp |
| `[Line 180] History: Pushed state...` | Line 187-188 | The Caretaker adds the memento to the undo stack |
| `[Line 98] TextEditor: Typed...` | Line 98-105 | The actual typing operation modifies the editor state |

#### Undo Operation Flow

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 277] EditorApplication: Performing UNDO` | Line 284-285 | Application initiates undo operation |
| `[Line 72] TextEditor: Saving current state...` | Line 286 | Current state is saved to enable redo |
| `[Line 198] History: Undo - moving to...` | Line 204-206 | Caretaker pops from undo stack, pushes current to redo stack |
| `[Line 87] TextEditor: Restored state...` | Line 89-94 | Originator restores all fields from the memento |

#### Redo Operation Flow

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 286] EditorApplication: Performing REDO` | Line 293-294 | Application initiates redo operation |
| `[Line 211] History: Redo - moving to...` | Line 217-219 | Caretaker pops from redo stack, pushes to undo stack |
| `[Line 87] TextEditor: Restored state...` | Line 296-297 | Originator restores the redo state |

#### Redo Stack Clearing

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 175] History: Clearing 1 redo states` | Line 182-184 | When a new action is performed after undo, redo history is cleared (standard undo/redo behavior) |

### Demo 2: Game Save States

This example demonstrates named save slots for game checkpoint functionality.

#### Game Actions

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 367] Game: Moved to...` | Line 377-380 | Game (Originator) updates player position |
| `[Line 387] Game: Collected...` | Line 398-400 | Adding items to inventory array (deep copied in memento) |
| `[Line 382] Game: Added...` | Line 393-395 | Score accumulation |
| `[Line 372] Game: Took...` | Line 383-385 | Health reduction with floor at 0 |

#### Save Operation

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 344] Game: Creating save state...` | Line 356-357 | Game creates a memento with all current state |
| `[Line 325] GameMemento: Created save state...` | Line 331-337 | Memento performs deep copy of position and inventory using spread operator |
| `[Line 413] SaveManager: Saved game to slot...` | Line 425-427 | SaveManager (Caretaker) stores memento in named slot |

#### Load Operation

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[Line 419] SaveManager: Loading from slot...` | Line 431-434 | SaveManager retrieves memento by slot name |
| `[Line 360] Game: Restored to...` | Line 367-373 | Game restores all fields from memento |

### Pattern Component Mapping

#### Example 1: Text Editor

| Component | Class | Responsibility |
|-----------|-------|----------------|
| **Originator** | `TextEditor` | Owns the state (content, cursor, selection), can save/restore |
| **Memento** | `EditorMemento` | Immutable snapshot of editor state with timestamp |
| **Caretaker** | `History` | Manages undo/redo stacks, enforces history limit |
| **Client** | `EditorApplication` | Coordinates operations and state management |

#### Example 2: Game

| Component | Class | Responsibility |
|-----------|-------|----------------|
| **Originator** | `Game` | Owns game state (health, position, score, inventory, level) |
| **Memento** | `GameMemento` | Immutable snapshot with deep copies of complex data |
| **Caretaker** | `SaveManager` | Named save slots using Map for quick access |

### Key Implementation Details

1. **Encapsulation Preservation** (Lines 17-66, 316-346): Mementos use private readonly fields with getter methods, preventing external modification while allowing state retrieval.

2. **Deep Copying** (Lines 332-335): Complex objects like arrays and nested objects are deep-copied using spread operators to prevent reference sharing.

3. **History Management** (Lines 180-194): The Caretaker implements bounded history to prevent memory leaks with `maxHistory` parameter.

4. **Redo Stack Clearing** (Lines 181-185): Following standard undo/redo semantics, new actions clear the redo stack.

5. **State Validation** (Lines 108-118, 135-146): The Originator validates operations before state changes.

### Benefits of This Implementation

- **Single Responsibility**: Each class has a clear, focused purpose
- **Encapsulation**: Internal state is not exposed to the Caretaker
- **Flexibility**: Easy to add new state fields to mementos
- **Memory Control**: Bounded history prevents memory issues
- **Multiple Caretaker Strategies**: Stack-based (undo/redo) and named slots demonstrated
