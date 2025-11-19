# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Memento Pattern

The Memento pattern captures and externalizes an object's internal state so
that the object can be restored to this state later, without violating
encapsulation.

Key Components:
- Originator: Object whose state needs to be saved and restored
- Memento: Stores internal state of Originator
- Caretaker: Manages and stores Mementos
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any
import copy


# Memento interface (narrow interface for caretaker)
class Memento(ABC):
    """Abstract memento interface."""

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> datetime:
        pass


# Concrete Memento
class DocumentMemento(Memento):
    """Concrete memento storing document state."""

    def __init__(self, state: dict[str, Any], name: str):
        self._state = copy.deepcopy(state)
        self._name = name
        self._date = datetime.now()

    def get_state(self) -> dict[str, Any]:
        """Only Originator should access this."""
        return copy.deepcopy(self._state)

    def get_name(self) -> str:
        return self._name

    def get_date(self) -> datetime:
        return self._date


# Originator
class TextDocument:
    """Originator: A text document that can save/restore state."""

    def __init__(self):
        self._content = ""
        self._cursor_position = 0
        self._selection_start = 0
        self._selection_end = 0
        self._font = "Arial"
        self._font_size = 12
        self._modified = False

    @property
    def content(self) -> str:
        return self._content

    def write(self, text: str) -> None:
        """Write text at cursor position."""
        before = self._content[: self._cursor_position]
        after = self._content[self._cursor_position :]
        self._content = before + text + after
        self._cursor_position += len(text)
        self._modified = True

    def delete(self, count: int) -> None:
        """Delete characters before cursor."""
        if count > self._cursor_position:
            count = self._cursor_position
        start = self._cursor_position - count
        self._content = self._content[:start] + self._content[self._cursor_position :]
        self._cursor_position = start
        self._modified = True

    def set_cursor(self, position: int) -> None:
        """Set cursor position."""
        self._cursor_position = max(0, min(position, len(self._content)))

    def set_font(self, font: str, size: int) -> None:
        """Set font properties."""
        self._font = font
        self._font_size = size
        self._modified = True

    def select(self, start: int, end: int) -> None:
        """Select text range."""
        self._selection_start = max(0, min(start, len(self._content)))
        self._selection_end = max(0, min(end, len(self._content)))

    def get_selected_text(self) -> str:
        """Get selected text."""
        return self._content[self._selection_start : self._selection_end]

    def save(self, name: str = "") -> Memento:
        """Create memento with current state."""
        if not name:
            name = f"Save at {datetime.now().strftime('%H:%M:%S')}"

        state = {
            "content": self._content,
            "cursor_position": self._cursor_position,
            "selection_start": self._selection_start,
            "selection_end": self._selection_end,
            "font": self._font,
            "font_size": self._font_size,
        }
        self._modified = False
        return DocumentMemento(state, name)

    def restore(self, memento: Memento) -> None:
        """Restore state from memento."""
        if isinstance(memento, DocumentMemento):
            state = memento.get_state()
            self._content = state["content"]
            self._cursor_position = state["cursor_position"]
            self._selection_start = state["selection_start"]
            self._selection_end = state["selection_end"]
            self._font = state["font"]
            self._font_size = state["font_size"]
            self._modified = False

    def get_info(self) -> dict[str, Any]:
        """Get current document info."""
        return {
            "content": self._content,
            "length": len(self._content),
            "cursor": self._cursor_position,
            "font": f"{self._font} {self._font_size}pt",
            "modified": self._modified,
        }


# Caretaker
class History:
    """Caretaker that manages mementos."""

    def __init__(self, originator: TextDocument):
        self._originator = originator
        self._history: list[Memento] = []
        self._current_index = -1

    def backup(self, name: str = "") -> None:
        """Create a backup of current state."""
        # Remove any forward history if we're not at the end
        if self._current_index < len(self._history) - 1:
            self._history = self._history[: self._current_index + 1]

        memento = self._originator.save(name)
        self._history.append(memento)
        self._current_index = len(self._history) - 1
        print(f"  [History] Saved: {memento.get_name()}")

    def undo(self) -> bool:
        """Restore previous state."""
        if self._current_index <= 0:
            print("  [History] Nothing to undo")
            return False

        self._current_index -= 1
        memento = self._history[self._current_index]
        self._originator.restore(memento)
        print(f"  [History] Restored: {memento.get_name()}")
        return True

    def redo(self) -> bool:
        """Restore next state."""
        if self._current_index >= len(self._history) - 1:
            print("  [History] Nothing to redo")
            return False

        self._current_index += 1
        memento = self._history[self._current_index]
        self._originator.restore(memento)
        print(f"  [History] Restored: {memento.get_name()}")
        return True

    def show_history(self) -> None:
        """Display all saved states."""
        print("\nHistory:")
        for i, memento in enumerate(self._history):
            marker = " --> " if i == self._current_index else "     "
            date = memento.get_date().strftime("%H:%M:%S")
            print(f"{marker}[{i}] {date} - {memento.get_name()}")


# Game example
class GameMemento(Memento):
    """Memento for game state."""

    def __init__(self, state: dict[str, Any]):
        self._state = copy.deepcopy(state)
        self._date = datetime.now()
        self._name = f"Level {state['level']} - {state['checkpoint']}"

    def get_state(self) -> dict[str, Any]:
        return copy.deepcopy(self._state)

    def get_name(self) -> str:
        return self._name

    def get_date(self) -> datetime:
        return self._date


class Game:
    """Game originator."""

    def __init__(self):
        self._level = 1
        self._health = 100
        self._score = 0
        self._position = (0, 0)
        self._inventory: list[str] = []
        self._checkpoint = "Start"

    def play(self, action: str) -> None:
        """Simulate game actions."""
        if action == "move":
            self._position = (self._position[0] + 10, self._position[1] + 5)
            self._score += 10
        elif action == "collect":
            self._inventory.append(f"item_{len(self._inventory) + 1}")
            self._score += 50
        elif action == "fight":
            self._health -= 20
            self._score += 100
        elif action == "level_up":
            self._level += 1
            self._checkpoint = f"Level {self._level} start"
            self._health = 100

    def save(self) -> Memento:
        state = {
            "level": self._level,
            "health": self._health,
            "score": self._score,
            "position": self._position,
            "inventory": self._inventory.copy(),
            "checkpoint": self._checkpoint,
        }
        return GameMemento(state)

    def restore(self, memento: Memento) -> None:
        if isinstance(memento, GameMemento):
            state = memento.get_state()
            self._level = state["level"]
            self._health = state["health"]
            self._score = state["score"]
            self._position = state["position"]
            self._inventory = state["inventory"]
            self._checkpoint = state["checkpoint"]

    def get_status(self) -> dict[str, Any]:
        return {
            "level": self._level,
            "health": self._health,
            "score": self._score,
            "position": self._position,
            "inventory": self._inventory,
            "checkpoint": self._checkpoint,
        }


class GameSaveManager:
    """Caretaker for game saves."""

    def __init__(self):
        self._saves: dict[str, Memento] = {}

    def save_game(self, game: Game, slot: str) -> None:
        memento = game.save()
        self._saves[slot] = memento
        print(f"  [SaveManager] Game saved to slot '{slot}': {memento.get_name()}")

    def load_game(self, game: Game, slot: str) -> bool:
        if slot not in self._saves:
            print(f"  [SaveManager] No save found in slot '{slot}'")
            return False
        game.restore(self._saves[slot])
        print(f"  [SaveManager] Game loaded from slot '{slot}'")
        return True

    def list_saves(self) -> None:
        print("\nSave slots:")
        for slot, memento in self._saves.items():
            date = memento.get_date().strftime("%Y-%m-%d %H:%M:%S")
            print(f"  [{slot}] {date} - {memento.get_name()}")


def main() -> None:
    print("=" * 60)
    print("Memento Pattern - Text Editor Demo")
    print("=" * 60)

    # Demo 1: Text document with undo/redo
    print("\n--- Text Document Demo ---")
    doc = TextDocument()
    history = History(doc)

    # Initial state
    history.backup("Initial")
    print(f"Content: '{doc.content}'")

    # Make changes
    doc.write("Hello")
    history.backup("Added Hello")
    print(f"Content: '{doc.content}'")

    doc.write(" World")
    history.backup("Added World")
    print(f"Content: '{doc.content}'")

    doc.write("!")
    history.backup("Added !")
    print(f"Content: '{doc.content}'")

    # Undo
    print("\n--- Undo Operations ---")
    history.undo()
    print(f"Content: '{doc.content}'")

    history.undo()
    print(f"Content: '{doc.content}'")

    # Redo
    print("\n--- Redo Operation ---")
    history.redo()
    print(f"Content: '{doc.content}'")

    # Show history
    history.show_history()

    # Demo 2: Font changes
    print("\n--- Font Changes ---")
    doc.set_font("Times New Roman", 14)
    history.backup("Changed font")
    print(f"Font: {doc.get_info()['font']}")

    doc.set_font("Courier", 10)
    history.backup("Changed to Courier")
    print(f"Font: {doc.get_info()['font']}")

    history.undo()
    print(f"After undo - Font: {doc.get_info()['font']}")

    # Demo 3: Game save system
    print("\n" + "=" * 60)
    print("Memento Pattern - Game Save Demo")
    print("=" * 60)

    game = Game()
    save_manager = GameSaveManager()

    print("\n--- Playing Game ---")
    print(f"Initial: {game.get_status()}")

    game.play("move")
    game.play("collect")
    save_manager.save_game(game, "slot1")

    game.play("fight")
    game.play("move")
    save_manager.save_game(game, "slot2")

    game.play("level_up")
    save_manager.save_game(game, "quicksave")

    print(f"\nCurrent: {game.get_status()}")

    # List saves
    save_manager.list_saves()

    # Load earlier save
    print("\n--- Loading Earlier Save ---")
    save_manager.load_game(game, "slot1")
    print(f"After loading slot1: {game.get_status()}")

    # Load quicksave
    print("\n--- Loading Quicksave ---")
    save_manager.load_game(game, "quicksave")
    print(f"After loading quicksave: {game.get_status()}")

    print("\n" + "=" * 60)
    print("Benefits of Memento Pattern:")
    print("=" * 60)
    print("1. Preserves encapsulation boundaries")
    print("2. Simplifies originator code")
    print("3. Can implement undo/redo functionality")
    print("4. Stores object state without exposing internals")
    print("5. Caretaker doesn't know memento details")


if __name__ == "__main__":
    main()
