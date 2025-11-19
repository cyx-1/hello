# Command Pattern

Encapsulates a request as an object, allowing parameterization, queuing, and undo/redo operations.

## How to Run
```bash
cd java/command
mvn compile exec:java
```

## Key Source Code

### Command Interface (Lines 13-17)
```java
interface Command {
    void execute();
    void undo();
    String getDescription();
}
```

### Concrete Command (Lines 74-91)
```java
class LightOnCommand implements Command {
    private Light light;

    @Override
    public void execute() { light.on(); }

    @Override
    public void undo() { light.off(); }
}
```

### Invoker with Undo (Lines 149-182)
```java
class RemoteControl {
    private Stack<Command> undoStack;

    public void undoButtonPressed() {
        if (!undoStack.isEmpty()) {
            Command command = undoStack.pop();
            command.undo();
        }
    }
}
```

## Program Output
```
--- 1. Smart Home Remote Control ---
  [Light] Living Room light is ON
  [Light] Kitchen light is ON
  [Stereo] Living Room stereo is ON

Undoing last command:
  Undoing: Turn stereo on
  [Stereo] Living Room stereo is OFF

--- 2. Macro Command (Party Mode) ---
Activating Party Mode:
  [Light] Party Room 1 light is ON
  [Light] Party Room 2 light is ON
  [Light] Party Room 1 light dimmed to 30%
```

## Pattern Benefits
- Decouples invoker from receiver
- Supports undo/redo
- Commands can be queued or logged
- Supports macro commands

## Requirements
- Java 17 or higher
- Maven 3.x
