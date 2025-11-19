# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Command Pattern

The Command pattern encapsulates a request as an object, thereby letting you
parameterize clients with different requests, queue or log requests, and
support undoable operations.

Key Components:
- Command: Interface for executing an operation
- ConcreteCommand: Binds a receiver to an action
- Invoker: Asks the command to carry out the request
- Receiver: Knows how to perform the operations
- Client: Creates commands and sets their receivers
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


# Command interface
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


# Receivers
class TextEditor:
    """Receiver: text editor that performs actual operations."""

    def __init__(self):
        self._text = ""
        self._clipboard = ""
        self._selection_start = 0
        self._selection_end = 0

    @property
    def text(self) -> str:
        return self._text

    def insert(self, text: str, position: int) -> None:
        self._text = self._text[:position] + text + self._text[position:]

    def delete(self, start: int, end: int) -> str:
        deleted = self._text[start:end]
        self._text = self._text[:start] + self._text[end:]
        return deleted

    def replace(self, start: int, end: int, new_text: str) -> str:
        old_text = self._text[start:end]
        self._text = self._text[:start] + new_text + self._text[end:]
        return old_text

    def get_text_range(self, start: int, end: int) -> str:
        return self._text[start:end]

    def select(self, start: int, end: int) -> None:
        self._selection_start = start
        self._selection_end = end

    def get_selection(self) -> tuple[int, int]:
        return (self._selection_start, self._selection_end)

    def copy_to_clipboard(self, text: str) -> None:
        self._clipboard = text

    def get_clipboard(self) -> str:
        return self._clipboard


# Concrete Commands
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


class DeleteCommand(Command):
    """Command to delete text."""

    def __init__(self, editor: TextEditor, start: int, end: int):
        self._editor = editor
        self._start = start
        self._end = end
        self._deleted_text = ""

    def execute(self) -> str:
        self._deleted_text = self._editor.delete(self._start, self._end)
        return f"Deleted '{self._deleted_text}'"

    def undo(self) -> str:
        self._editor.insert(self._deleted_text, self._start)
        return f"Undid delete, restored '{self._deleted_text}'"

    def get_description(self) -> str:
        return f"Delete from {self._start} to {self._end}"


class ReplaceCommand(Command):
    """Command to replace text."""

    def __init__(self, editor: TextEditor, start: int, end: int, new_text: str):
        self._editor = editor
        self._start = start
        self._end = end
        self._new_text = new_text
        self._old_text = ""

    def execute(self) -> str:
        self._old_text = self._editor.replace(self._start, self._end, self._new_text)
        return f"Replaced '{self._old_text}' with '{self._new_text}'"

    def undo(self) -> str:
        self._editor.replace(
            self._start, self._start + len(self._new_text), self._old_text
        )
        return f"Undid replace, restored '{self._old_text}'"

    def get_description(self) -> str:
        return f"Replace at {self._start}-{self._end} with '{self._new_text}'"


class CopyCommand(Command):
    """Command to copy text to clipboard."""

    def __init__(self, editor: TextEditor, start: int, end: int):
        self._editor = editor
        self._start = start
        self._end = end
        self._previous_clipboard = ""

    def execute(self) -> str:
        self._previous_clipboard = self._editor.get_clipboard()
        text = self._editor.get_text_range(self._start, self._end)
        self._editor.copy_to_clipboard(text)
        return f"Copied '{text}' to clipboard"

    def undo(self) -> str:
        self._editor.copy_to_clipboard(self._previous_clipboard)
        return "Restored previous clipboard content"

    def get_description(self) -> str:
        return f"Copy from {self._start} to {self._end}"


class PasteCommand(Command):
    """Command to paste from clipboard."""

    def __init__(self, editor: TextEditor, position: int):
        self._editor = editor
        self._position = position
        self._pasted_text = ""

    def execute(self) -> str:
        self._pasted_text = self._editor.get_clipboard()
        self._editor.insert(self._pasted_text, self._position)
        return f"Pasted '{self._pasted_text}' at position {self._position}"

    def undo(self) -> str:
        self._editor.delete(self._position, self._position + len(self._pasted_text))
        return f"Undid paste of '{self._pasted_text}'"

    def get_description(self) -> str:
        return f"Paste at {self._position}"


# Macro Command (Composite Command)
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


# Invoker
@dataclass
class HistoryEntry:
    command: Command
    timestamp: datetime
    executed: bool


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

    def get_history(self) -> list[str]:
        """Get command history descriptions."""
        return [
            f"{entry.timestamp.strftime('%H:%M:%S')} - {entry.command.get_description()}"
            for entry in self._history
        ]

    def get_current_text(self) -> str:
        """Get current editor text."""
        return self._editor.text


def main() -> None:
    print("=" * 60)
    print("Command Pattern - Text Editor Demo")
    print("=" * 60)

    # Create receiver and invoker
    editor = TextEditor()
    invoker = EditorInvoker(editor)

    # Demo 1: Basic commands
    print("\n--- Basic Commands ---")

    cmd = InsertCommand(editor, "Hello", 0)
    print(invoker.execute(cmd))
    print(f"Text: '{invoker.get_current_text()}'")

    cmd = InsertCommand(editor, " World", 5)
    print(invoker.execute(cmd))
    print(f"Text: '{invoker.get_current_text()}'")

    cmd = InsertCommand(editor, "!", 11)
    print(invoker.execute(cmd))
    print(f"Text: '{invoker.get_current_text()}'")

    # Demo 2: Undo/Redo
    print("\n--- Undo/Redo ---")
    print(invoker.undo())
    print(f"Text after undo: '{invoker.get_current_text()}'")

    print(invoker.undo())
    print(f"Text after undo: '{invoker.get_current_text()}'")

    print(invoker.redo())
    print(f"Text after redo: '{invoker.get_current_text()}'")

    # Demo 3: Replace and Delete
    print("\n--- Replace and Delete ---")
    cmd = ReplaceCommand(editor, 0, 5, "Hi")
    print(invoker.execute(cmd))
    print(f"Text: '{invoker.get_current_text()}'")

    cmd = DeleteCommand(editor, 2, 8)
    print(invoker.execute(cmd))
    print(f"Text: '{invoker.get_current_text()}'")

    # Demo 4: Copy and Paste
    print("\n--- Copy and Paste ---")
    cmd = InsertCommand(editor, "Python is great", 0)
    print(invoker.execute(cmd))
    print(f"Text: '{invoker.get_current_text()}'")

    cmd = CopyCommand(editor, 0, 6)  # Copy "Python"
    print(invoker.execute(cmd))

    cmd = PasteCommand(editor, 10)
    print(invoker.execute(cmd))
    print(f"Text: '{invoker.get_current_text()}'")

    # Demo 5: Macro Command
    print("\n--- Macro Command ---")

    # Create a macro to add formatted header
    editor2 = TextEditor()
    invoker2 = EditorInvoker(editor2)

    macro_commands = [
        InsertCommand(editor2, "=====\n", 0),
        InsertCommand(editor2, "HEADER", 6),
        InsertCommand(editor2, "\n=====", 12),
    ]

    macro = MacroCommand("Add Header", macro_commands)
    print(invoker2.execute(macro))
    print(f"Text: '{invoker2.get_current_text()}'")

    print("\nUndo macro:")
    print(invoker2.undo())
    print(f"Text: '{invoker2.get_current_text()}'")

    # Demo 6: Command History
    print("\n--- Command History ---")
    print("First editor history:")
    for entry in invoker.get_history():
        print(f"  {entry}")

    # Demo 7: Multiple undos
    print("\n--- Multiple Undos ---")
    print(f"Current text: '{invoker.get_current_text()}'")
    for _ in range(3):
        result = invoker.undo()
        print(result)
        print(f"  Text: '{invoker.get_current_text()}'")

    print("\n" + "=" * 60)
    print("Benefits of Command Pattern:")
    print("=" * 60)
    print("1. Decouples invoker from receiver")
    print("2. Commands are first-class objects")
    print("3. Easy to add new commands")
    print("4. Supports undo/redo operations")
    print("5. Supports macros (composite commands)")
    print("6. Commands can be queued, logged, or serialized")


if __name__ == "__main__":
    main()
