# Memento Pattern

Captures and externalizes an object's internal state without violating encapsulation, allowing restoration later.

## How to Run
```bash
cd java/memento
mvn compile exec:java
```

## Key Source Code

### Memento (Lines 13-27)
```java
class EditorMemento {
    private final String content;
    private final int cursorPosition;

    public EditorMemento(String content, int cursorPosition) {
        this.content = content;
        this.cursorPosition = cursorPosition;
    }
}
```

### Originator (Lines 30-55)
```java
class TextEditor {
    public EditorMemento save() {
        return new EditorMemento(content, cursorPosition);
    }

    public void restore(EditorMemento memento) {
        content = memento.getContent();
        cursorPosition = memento.getCursorPosition();
    }
}
```

### Caretaker (Lines 58-78)
```java
class EditorHistory {
    private Stack<EditorMemento> undoStack = new Stack<>();
    private Stack<EditorMemento> redoStack = new Stack<>();

    public EditorMemento undo() {
        redoStack.push(undoStack.pop());
        return undoStack.peek();
    }
}
```

## Program Output
```
--- 1. Text Editor with Undo/Redo ---
  [Editor] Typed: "Hello"
  [Editor] Saving state...
  [Editor] Typed: " World"
  [Editor] Typed: "!"
  Content: "Hello World!"

Undo operations:
  [Editor] Restored to: "Hello World"
  [Editor] Restored to: "Hello"

--- 2. Game Save System ---
  [Game] Playing... Level: 2, Score: 100
  [SaveSlots] Saved to slot 0
  [Game] Took 60 damage. Health: 0
  [Game] Game Over!

Loading from save slot 0:
  [Game] Game restored to: Level 2, Health 90, Score 100
```

## Pattern Benefits
- Preserves encapsulation
- Provides recovery mechanism
- Supports undo/redo functionality

## Requirements
- Java 17 or higher
- Maven 3.x
