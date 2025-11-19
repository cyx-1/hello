# Memento Pattern

The Memento pattern captures and externalizes an object's internal state so that the object can be restored to this state later, without violating encapsulation.

**Key Components:**
- **Originator**: Object whose state needs to be saved and restored
- **Memento**: Stores internal state of Originator
- **Caretaker**: Manages and stores Mementos

**Requires**: Python 3.10+ (uses union types with `|` syntax, type hints)

## Key Source Code

### Memento Interface

```python:main_memento.py startLine=24 endLine=54
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
```

### Originator - TextDocument

```python:main_memento.py startLine=57 endLine=146
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

    def write(self, text: str) -> None:
        """Write text at cursor position."""
        before = self._content[: self._cursor_position]
        after = self._content[self._cursor_position :]
        self._content = before + text + after
        self._cursor_position += len(text)
        self._modified = True

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
```

### Caretaker - History

```python:main_memento.py startLine=149 endLine=200
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
```

### Game Save System

```python:main_memento.py startLine=280 endLine=304
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
```

## Program Output

```
============================================================
Memento Pattern - Text Editor Demo
============================================================

--- Text Document Demo ---
  [History] Saved: Initial
Content: ''
  [History] Saved: Added Hello
Content: 'Hello'
  [History] Saved: Added World
Content: 'Hello World'
  [History] Saved: Added !
Content: 'Hello World!'

--- Undo Operations ---
  [History] Restored: Added World
Content: 'Hello World'
  [History] Restored: Added Hello
Content: 'Hello'

--- Redo Operation ---
  [History] Restored: Added World
Content: 'Hello World'

History:
     [0] 23:52:18 - Initial
     [1] 23:52:18 - Added Hello
 --> [2] 23:52:18 - Added World
     [3] 23:52:18 - Added !

--- Font Changes ---
  [History] Saved: Changed font
Font: Times New Roman 14pt
  [History] Saved: Changed to Courier
Font: Courier 10pt
  [History] Restored: Changed font
After undo - Font: Times New Roman 14pt

============================================================
Memento Pattern - Game Save Demo
============================================================

--- Playing Game ---
Initial: {'level': 1, 'health': 100, 'score': 0, 'position': (0, 0), 'inventory': [], 'checkpoint': 'Start'}
  [SaveManager] Game saved to slot 'slot1': Level 1 - Start
  [SaveManager] Game saved to slot 'slot2': Level 1 - Start
  [SaveManager] Game saved to slot 'quicksave': Level 2 - Level 2 start

Current: {'level': 2, 'health': 100, 'score': 170, 'position': (20, 10), 'inventory': ['item_1'], 'checkpoint': 'Level 2 start'}

Save slots:
  [slot1] 2025-11-18 23:52:18 - Level 1 - Start
  [slot2] 2025-11-18 23:52:18 - Level 1 - Start
  [quicksave] 2025-11-18 23:52:18 - Level 2 - Level 2 start

--- Loading Earlier Save ---
  [SaveManager] Game loaded from slot 'slot1'
After loading slot1: {'level': 1, 'health': 100, 'score': 60, 'position': (10, 5), 'inventory': ['item_1'], 'checkpoint': 'Start'}

--- Loading Quicksave ---
  [SaveManager] Game loaded from slot 'quicksave'
After loading quicksave: {'level': 2, 'health': 100, 'score': 170, 'position': (20, 10), 'inventory': ['item_1'], 'checkpoint': 'Level 2 start'}

============================================================
Benefits of Memento Pattern:
============================================================
1. Preserves encapsulation boundaries
2. Simplifies originator code
3. Can implement undo/redo functionality
4. Stores object state without exposing internals
5. Caretaker doesn't know memento details
```

## Output Annotations

### Text Document Demo

- **Lines 110-124**: The `save()` method creates a memento by capturing all internal state (content, cursor, selection, font) into a dictionary. The `backup()` method in History (lines 158-167) calls this and stores the returned memento.

- **Lines 317-331**: Each `write()` call (lines 74-80) modifies the document's `_content` and `_cursor_position`. After each write, `backup()` creates a snapshot. The output shows content growing from '' to 'Hello' to 'Hello World' to 'Hello World!'.

- **Lines 169-179 (undo)**: When `undo()` is called, the History caretaker decrements `_current_index` and calls the originator's `restore()` method (lines 126-136) with the previous memento. Content reverts from 'Hello World!' to 'Hello World' to 'Hello'.

- **Lines 181-191 (redo)**: The `redo()` method increments the index and restores forward. After two undos and one redo, content returns to 'Hello World'.

- **Lines 193-199 (show_history)**: The arrow marker ` --> ` indicates the current position (index 2 = "Added World"), showing that there's one more state ahead (index 3 = "Added !") that can be redone.

- **Lines 161-162**: When a new backup is made while not at the end of history, forward history is discarded. This implements the typical text editor behavior where editing after undo removes the redo history.

### Game Save Demo

- **Lines 248-257 (Game.save)**: The Game originator's `save()` method captures game state including level, health, score, position, and inventory into a GameMemento.

- **Lines 286-289**: The GameSaveManager caretaker stores mementos in named slots. Unlike the linear History, this allows random access to different save states.

- **Lines 371-382**: Game state changes through `play()` actions (lines 232-246). After "move" (position changes, score +10), "collect" (inventory adds item, score +50), the state is saved to slot1. More actions lead to slot2 and quicksave.

- **Lines 291-297 (load_game)**: Loading from slot1 restores the earlier state with score=60 and position=(10,5). Loading quicksave jumps to level 2 with score=170. The memento encapsulates all state including complex types like inventory lists.

- **Lines 41-48 (deep copy)**: The `copy.deepcopy()` ensures mementos are independent snapshots. Without this, modifying the originator would affect saved mementos.

## Running the Demo

```bash
uv run python main_memento.py
```
