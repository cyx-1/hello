# Command Pattern

The Command pattern encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

**Requires Python 3.10+** (uses union types with `|` syntax and tuple type hints)

## Key Source Code

### Command Interface

```python:main_command.py startLine=26 endLine=39
class Command(ABC):
    """Abstract command interface."""

    @abstractmethod
    def execute(self) -> str:
        pass

    @abstractmethod
    def undo(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass
```

### Concrete Command with Undo Support

```python:main_command.py startLine=87 endLine=104
class InsertCommand(Command):
    """Command to insert text."""

    def __init__(self, editor: TextEditor, text: str, position: int):
        self._editor = editor
        self._text = text
        self._position = position

    def execute(self) -> str:
        self._editor.insert(self._text, self._position)
        return f"Inserted '{self._text}' at position {self._position}"

    def undo(self) -> str:
        self._editor.delete(self._position, self._position + len(self._text))
        return f"Undid insert of '{self._text}'"

    def get_description(self) -> str:
        return f"Insert '{self._text}' at {self._position}"
```

### Invoker with History Management

```python:main_command.py startLine=229 endLine=267
class EditorInvoker:
    """Invoker that executes commands and manages history."""

    def __init__(self, editor: TextEditor):
        self._editor = editor
        self._history: list[HistoryEntry] = []
        self._redo_stack: list[HistoryEntry] = []

    def execute(self, command: Command) -> str:
        """Execute command and add to history."""
        result = command.execute()
        entry = HistoryEntry(
            command=command, timestamp=datetime.now(), executed=True
        )
        self._history.append(entry)
        self._redo_stack.clear()  # Clear redo stack on new command
        return result

    def undo(self) -> str:
        """Undo last command."""
        if not self._history:
            return "Nothing to undo"

        entry = self._history.pop()
        result = entry.command.undo()
        entry.executed = False
        self._redo_stack.append(entry)
        return result

    def redo(self) -> str:
        """Redo last undone command."""
        if not self._redo_stack:
            return "Nothing to redo"

        entry = self._redo_stack.pop()
        result = entry.command.execute()
        entry.executed = True
        self._history.append(entry)
        return result
```

### Macro Command (Composite)

```python:main_command.py startLine=197 endLine=218
class MacroCommand(Command):
    """Composite command that executes multiple commands."""

    def __init__(self, name: str, commands: list[Command]):
        self._name = name
        self._commands = commands

    def execute(self) -> str:
        results = []
        for cmd in self._commands:
            results.append(cmd.execute())
        return f"Macro '{self._name}' executed:\n  " + "\n  ".join(results)

    def undo(self) -> str:
        results = []
        # Undo in reverse order
        for cmd in reversed(self._commands):
            results.append(cmd.undo())
        return f"Macro '{self._name}' undone:\n  " + "\n  ".join(results)

    def get_description(self) -> str:
        return f"Macro: {self._name} ({len(self._commands)} commands)"
```

## Program Output

```
============================================================
Command Pattern - Text Editor Demo
============================================================

--- Basic Commands ---
Inserted 'Hello' at position 0
Text: 'Hello'
Inserted ' World' at position 5
Text: 'Hello World'
Inserted '!' at position 11
Text: 'Hello World!'

--- Undo/Redo ---
Undid insert of '!'
Text after undo: 'Hello World'
Undid insert of ' World'
Text after undo: 'Hello'
Inserted ' World' at position 5
Text after redo: 'Hello World'

--- Replace and Delete ---
Replaced 'Hello' with 'Hi'
Text: 'Hi World'
Deleted ' World'
Text: 'Hi'

--- Copy and Paste ---
Inserted 'Python is great' at position 0
Text: 'Python is greatHi'
Copied 'Python' to clipboard
Pasted 'Python' at position 10
Text: 'Python is PythongreatHi'

--- Macro Command ---
Macro 'Add Header' executed:
  Inserted '=====
' at position 0
  Inserted 'HEADER' at position 6
  Inserted '
=====' at position 12
Text: '=====
HEADER
====='

Undo macro:
Macro 'Add Header' undone:
  Undid insert of '
====='
  Undid insert of 'HEADER'
  Undid insert of '=====
'
Text: ''

--- Command History ---
First editor history:
  23:52:20 - Insert 'Hello' at 0
  23:52:20 - Insert ' World' at 5
  23:52:20 - Replace at 0-5 with 'Hi'
  23:52:20 - Delete from 2 to 8
  23:52:20 - Insert 'Python is great' at 0
  23:52:20 - Copy from 0 to 6
  23:52:20 - Paste at 10

--- Multiple Undos ---
Current text: 'Python is PythongreatHi'
Undid paste of 'Python'
  Text: 'Python is greatHi'
Restored previous clipboard content
  Text: 'Python is greatHi'
Undid insert of 'Python is great'
  Text: 'Hi'

============================================================
Benefits of Command Pattern:
============================================================
1. Decouples invoker from receiver
2. Commands are first-class objects
3. Easy to add new commands
4. Supports undo/redo operations
5. Supports macros (composite commands)
6. Commands can be queued, logged, or serialized
```

## Output Analysis

### Basic Commands (Lines 293-303)
- `InsertCommand` at line 95-96 inserts text and returns confirmation
- Each insert stores the text and position needed for undo
- Text builds progressively: "Hello" -> "Hello World" -> "Hello World!"

### Undo/Redo Operations (Lines 247-267)
- First undo (line 252-255): Removes "!" by calling `InsertCommand.undo()` which deletes the inserted text
- Second undo: Removes " World", text becomes "Hello"
- Redo (line 263-266): Re-executes the insert, restoring " World"
- Note: `_redo_stack` is cleared when new commands are executed (line 244)

### Replace and Delete (Lines 128-149, 107-125)
- `ReplaceCommand` at line 139 stores the old text ("Hello") before replacement
- `DeleteCommand` at line 117 stores deleted text (" World") for potential undo
- Both commands preserve state needed for reversal

### Copy and Paste (Lines 152-193)
- `CopyCommand` at line 162-164 stores previous clipboard for undo
- `PasteCommand` at line 184-186 uses clipboard content and stores it for undo
- Demonstrates command interaction through shared editor state

### Macro Command (Lines 197-218, 346-358)
- Executes multiple commands as a single operation (lines 204-208)
- Undo reverses in opposite order (line 213) - critical for correctness
- Single undo operation reverts all three inserts atomically

### Command History (Lines 269-274)
- Each executed command is timestamped (line 241)
- History shows all operations in execution order
- `get_description()` provides human-readable command summary

### Multiple Undos (Lines 367-372)
- Demonstrates stack-based undo with LIFO behavior
- Each undo pops from history and pushes to redo stack
- Commands independently track their undo state

## Usage

```bash
uv run python main_command.py
```
