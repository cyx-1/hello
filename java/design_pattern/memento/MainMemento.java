/**
 * Comprehensive demonstration of the Memento Pattern in Java
 *
 * The Memento pattern captures and externalizes an object's internal state
 * without violating encapsulation, allowing the object to be restored to
 * this state later.
 */

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Stack;

// Memento - stores the state
class EditorMemento {
    private final String content;
    private final int cursorPosition;
    private final Date timestamp;

    public EditorMemento(String content, int cursorPosition) {
        this.content = content;
        this.cursorPosition = cursorPosition;
        this.timestamp = new Date();
    }

    public String getContent() { return content; }
    public int getCursorPosition() { return cursorPosition; }
    public Date getTimestamp() { return timestamp; }
}

// Originator - creates and restores from mementos
class TextEditor {
    private String content = "";
    private int cursorPosition = 0;

    public void type(String text) {
        content = content.substring(0, cursorPosition) + text +
                  content.substring(cursorPosition);
        cursorPosition += text.length();
        System.out.println("  [Editor] Typed: \"" + text + "\"");
    }

    public void delete(int count) {
        if (cursorPosition >= count) {
            content = content.substring(0, cursorPosition - count) +
                      content.substring(cursorPosition);
            cursorPosition -= count;
            System.out.println("  [Editor] Deleted " + count + " characters");
        }
    }

    public void moveCursor(int position) {
        cursorPosition = Math.max(0, Math.min(position, content.length()));
    }

    public EditorMemento save() {
        System.out.println("  [Editor] Saving state...");
        return new EditorMemento(content, cursorPosition);
    }

    public void restore(EditorMemento memento) {
        content = memento.getContent();
        cursorPosition = memento.getCursorPosition();
        System.out.println("  [Editor] Restored to: \"" + content + "\"");
    }

    public String getContent() { return content; }

    public void display() {
        System.out.println("  Content: \"" + content + "\"");
        System.out.println("  Cursor at position: " + cursorPosition);
    }
}

// Caretaker - manages mementos
class EditorHistory {
    private Stack<EditorMemento> undoStack = new Stack<>();
    private Stack<EditorMemento> redoStack = new Stack<>();

    public void save(EditorMemento memento) {
        undoStack.push(memento);
        redoStack.clear();  // Clear redo stack on new save
    }

    public EditorMemento undo() {
        if (undoStack.size() > 1) {
            redoStack.push(undoStack.pop());
            return undoStack.peek();
        }
        return null;
    }

    public EditorMemento redo() {
        if (!redoStack.isEmpty()) {
            EditorMemento memento = redoStack.pop();
            undoStack.push(memento);
            return memento;
        }
        return null;
    }

    public boolean canUndo() {
        return undoStack.size() > 1;
    }

    public boolean canRedo() {
        return !redoStack.isEmpty();
    }
}

// Game save example

class GameMemento {
    private final int level;
    private final int health;
    private final int score;
    private final String position;

    public GameMemento(int level, int health, int score, String position) {
        this.level = level;
        this.health = health;
        this.score = score;
        this.position = position;
    }

    public int getLevel() { return level; }
    public int getHealth() { return health; }
    public int getScore() { return score; }
    public String getPosition() { return position; }
}

class Game {
    private int level = 1;
    private int health = 100;
    private int score = 0;
    private String position = "Start";

    public void play() {
        level++;
        score += 100;
        health -= 10;
        position = "Level " + level + " Checkpoint";
        System.out.println("  [Game] Playing... Level: " + level + ", Score: " + score + ", Health: " + health);
    }

    public void takeDamage(int damage) {
        health -= damage;
        System.out.println("  [Game] Took " + damage + " damage. Health: " + health);
    }

    public GameMemento save() {
        System.out.println("  [Game] Saving game...");
        return new GameMemento(level, health, score, position);
    }

    public void restore(GameMemento memento) {
        level = memento.getLevel();
        health = memento.getHealth();
        score = memento.getScore();
        position = memento.getPosition();
        System.out.println("  [Game] Game restored to: Level " + level + ", Health " + health + ", Score " + score);
    }

    public void display() {
        System.out.println("  Level: " + level + ", Health: " + health + ", Score: " + score + ", Position: " + position);
    }
}

class SaveSlots {
    private List<GameMemento> slots = new ArrayList<>();

    public void saveToSlot(GameMemento memento, int slot) {
        while (slots.size() <= slot) {
            slots.add(null);
        }
        slots.set(slot, memento);
        System.out.println("  [SaveSlots] Saved to slot " + slot);
    }

    public GameMemento loadFromSlot(int slot) {
        if (slot < slots.size() && slots.get(slot) != null) {
            System.out.println("  [SaveSlots] Loading from slot " + slot);
            return slots.get(slot);
        }
        System.out.println("  [SaveSlots] Slot " + slot + " is empty");
        return null;
    }
}

// Configuration rollback example

class ConfigMemento {
    private final String dbHost;
    private final int dbPort;
    private final boolean cacheEnabled;
    private final int maxConnections;

    public ConfigMemento(String dbHost, int dbPort, boolean cacheEnabled, int maxConnections) {
        this.dbHost = dbHost;
        this.dbPort = dbPort;
        this.cacheEnabled = cacheEnabled;
        this.maxConnections = maxConnections;
    }

    public String getDbHost() { return dbHost; }
    public int getDbPort() { return dbPort; }
    public boolean isCacheEnabled() { return cacheEnabled; }
    public int getMaxConnections() { return maxConnections; }
}

class AppConfiguration {
    private String dbHost = "localhost";
    private int dbPort = 5432;
    private boolean cacheEnabled = true;
    private int maxConnections = 10;

    public void setDbHost(String host) {
        dbHost = host;
        System.out.println("  [Config] DB Host set to: " + host);
    }

    public void setDbPort(int port) {
        dbPort = port;
        System.out.println("  [Config] DB Port set to: " + port);
    }

    public void setCacheEnabled(boolean enabled) {
        cacheEnabled = enabled;
        System.out.println("  [Config] Cache enabled: " + enabled);
    }

    public void setMaxConnections(int max) {
        maxConnections = max;
        System.out.println("  [Config] Max connections: " + max);
    }

    public ConfigMemento createSnapshot() {
        return new ConfigMemento(dbHost, dbPort, cacheEnabled, maxConnections);
    }

    public void restore(ConfigMemento memento) {
        dbHost = memento.getDbHost();
        dbPort = memento.getDbPort();
        cacheEnabled = memento.isCacheEnabled();
        maxConnections = memento.getMaxConnections();
        System.out.println("  [Config] Configuration restored");
    }

    public void display() {
        System.out.println("  DB: " + dbHost + ":" + dbPort);
        System.out.println("  Cache: " + cacheEnabled + ", Max Connections: " + maxConnections);
    }
}

public class MainMemento {
    public static void main(String[] args) {
        System.out.println("=== Memento Pattern Demonstration ===\n");

        // Text editor with undo/redo
        System.out.println("--- 1. Text Editor with Undo/Redo ---");

        TextEditor editor = new TextEditor();
        EditorHistory history = new EditorHistory();

        // Initial save
        history.save(editor.save());

        editor.type("Hello");
        history.save(editor.save());

        editor.type(" World");
        history.save(editor.save());

        editor.type("!");
        history.save(editor.save());

        editor.display();

        System.out.println("\nUndo operations:");
        if (history.canUndo()) {
            editor.restore(history.undo());
        }
        if (history.canUndo()) {
            editor.restore(history.undo());
        }

        System.out.println("\nRedo operation:");
        if (history.canRedo()) {
            editor.restore(history.redo());
        }
        System.out.println();

        // Game save example
        System.out.println("--- 2. Game Save System ---");

        Game game = new Game();
        SaveSlots saveSlots = new SaveSlots();

        game.play();
        game.play();
        saveSlots.saveToSlot(game.save(), 0);  // Save at level 3

        game.play();
        game.takeDamage(50);
        saveSlots.saveToSlot(game.save(), 1);  // Save at level 4

        game.takeDamage(60);  // Game over scenario
        System.out.println("\n  [Game] Game Over! Health: 0");

        System.out.println("\nLoading from save slot 0:");
        GameMemento save = saveSlots.loadFromSlot(0);
        if (save != null) {
            game.restore(save);
        }

        System.out.println("\nLoading from save slot 1:");
        save = saveSlots.loadFromSlot(1);
        if (save != null) {
            game.restore(save);
        }
        System.out.println();

        // Configuration rollback
        System.out.println("--- 3. Configuration Rollback ---");

        AppConfiguration config = new AppConfiguration();
        List<ConfigMemento> configHistory = new ArrayList<>();

        System.out.println("Initial configuration:");
        config.display();
        configHistory.add(config.createSnapshot());

        System.out.println("\nUpdating configuration:");
        config.setDbHost("production-db.example.com");
        config.setDbPort(5433);
        config.setMaxConnections(100);
        configHistory.add(config.createSnapshot());

        System.out.println("\nCurrent configuration:");
        config.display();

        System.out.println("\nRolling back to previous configuration:");
        config.restore(configHistory.get(0));
        config.display();

        System.out.println("\n=== Summary ===");
        System.out.println("Memento pattern benefits:");
        System.out.println("  - Preserves encapsulation boundaries");
        System.out.println("  - Simplifies the originator");
        System.out.println("  - Provides easy recovery mechanism");
        System.out.println("\nUse cases:");
        System.out.println("  - Undo/redo functionality");
        System.out.println("  - Game save systems");
        System.out.println("  - Transaction rollbacks");
        System.out.println("  - Configuration management");
    }
}
