/**
 * Memento Design Pattern in TypeScript
 *
 * The Memento pattern allows capturing and externalizing an object's internal
 * state so that it can be restored later, without violating encapsulation.
 * This is commonly used for implementing undo/redo functionality.
 *
 * Components:
 * - Originator: The object whose state needs to be saved
 * - Memento: Stores the internal state of the Originator
 * - Caretaker: Manages the mementos (history)
 */

// ============================================================
// Memento - Stores the state of the Originator
// ============================================================
class EditorMemento {
    private readonly content: string;
    private readonly cursorPosition: number;
    private readonly selectionStart: number;
    private readonly selectionEnd: number;
    private readonly timestamp: Date;

    constructor(
        content: string,
        cursorPosition: number,
        selectionStart: number,
        selectionEnd: number
    ) {
        this.content = content;
        this.cursorPosition = cursorPosition;
        this.selectionStart = selectionStart;
        this.selectionEnd = selectionEnd;
        this.timestamp = new Date();
        console.log(`[Line 32] EditorMemento: Created snapshot at ${this.timestamp.toISOString()}`);
    }

    // Getters for the Originator to restore state
    getContent(): string {
        return this.content;
    }

    getCursorPosition(): number {
        return this.cursorPosition;
    }

    getSelectionStart(): number {
        return this.selectionStart;
    }

    getSelectionEnd(): number {
        return this.selectionEnd;
    }

    getTimestamp(): Date {
        return this.timestamp;
    }

    // For display purposes
    getDescription(): string {
        const preview = this.content.length > 30
            ? this.content.substring(0, 30) + "..."
            : this.content;
        return `"${preview}" (cursor: ${this.cursorPosition})`;
    }
}

// ============================================================
// Originator - The object whose state we want to save
// ============================================================
class TextEditor {
    private content: string = "";
    private cursorPosition: number = 0;
    private selectionStart: number = 0;
    private selectionEnd: number = 0;

    // Create a memento (save state)
    save(): EditorMemento {
        console.log(`[Line 72] TextEditor: Saving current state...`);
        return new EditorMemento(
            this.content,
            this.cursorPosition,
            this.selectionStart,
            this.selectionEnd
        );
    }

    // Restore from memento
    restore(memento: EditorMemento): void {
        this.content = memento.getContent();
        this.cursorPosition = memento.getCursorPosition();
        this.selectionStart = memento.getSelectionStart();
        this.selectionEnd = memento.getSelectionEnd();
        console.log(`[Line 87] TextEditor: Restored state from ${memento.getTimestamp().toISOString()}`);
    }

    // Editor operations
    type(text: string): void {
        const before = this.content.substring(0, this.cursorPosition);
        const after = this.content.substring(this.cursorPosition);
        this.content = before + text + after;
        this.cursorPosition += text.length;
        this.selectionStart = this.cursorPosition;
        this.selectionEnd = this.cursorPosition;
        console.log(`[Line 98] TextEditor: Typed "${text}" at position ${this.cursorPosition - text.length}`);
    }

    delete(count: number): void {
        if (this.cursorPosition > 0 && count > 0) {
            const deleteStart = Math.max(0, this.cursorPosition - count);
            const deleted = this.content.substring(deleteStart, this.cursorPosition);
            const before = this.content.substring(0, deleteStart);
            const after = this.content.substring(this.cursorPosition);
            this.content = before + after;
            this.cursorPosition = deleteStart;
            console.log(`[Line 109] TextEditor: Deleted "${deleted}"`);
        }
    }

    moveCursor(position: number): void {
        this.cursorPosition = Math.max(0, Math.min(position, this.content.length));
        this.selectionStart = this.cursorPosition;
        this.selectionEnd = this.cursorPosition;
        console.log(`[Line 117] TextEditor: Moved cursor to position ${this.cursorPosition}`);
    }

    select(start: number, end: number): void {
        this.selectionStart = Math.max(0, Math.min(start, this.content.length));
        this.selectionEnd = Math.max(0, Math.min(end, this.content.length));
        this.cursorPosition = this.selectionEnd;
        const selected = this.content.substring(this.selectionStart, this.selectionEnd);
        console.log(`[Line 125] TextEditor: Selected "${selected}" (${this.selectionStart}-${this.selectionEnd})`);
    }

    replaceSelection(text: string): void {
        if (this.selectionStart !== this.selectionEnd) {
            const before = this.content.substring(0, this.selectionStart);
            const after = this.content.substring(this.selectionEnd);
            const replaced = this.content.substring(this.selectionStart, this.selectionEnd);
            this.content = before + text + after;
            this.cursorPosition = this.selectionStart + text.length;
            this.selectionStart = this.cursorPosition;
            this.selectionEnd = this.cursorPosition;
            console.log(`[Line 137] TextEditor: Replaced "${replaced}" with "${text}"`);
        }
    }

    getContent(): string {
        return this.content;
    }

    getCursorPosition(): number {
        return this.cursorPosition;
    }

    display(): void {
        console.log(`[Line 150] TextEditor Display:`);
        console.log(`  Content: "${this.content}"`);
        console.log(`  Cursor Position: ${this.cursorPosition}`);
        if (this.selectionStart !== this.selectionEnd) {
            console.log(`  Selection: ${this.selectionStart}-${this.selectionEnd}`);
        }
    }
}

// ============================================================
// Caretaker - Manages the history of mementos
// ============================================================
class History {
    private undoStack: EditorMemento[] = [];
    private redoStack: EditorMemento[] = [];
    private maxHistory: number;

    constructor(maxHistory: number = 50) {
        this.maxHistory = maxHistory;
        console.log(`[Line 168] History: Initialized with max ${maxHistory} snapshots`);
    }

    // Push a new state to history
    push(memento: EditorMemento): void {
        // Clear redo stack when new action is performed
        if (this.redoStack.length > 0) {
            console.log(`[Line 175] History: Clearing ${this.redoStack.length} redo states`);
            this.redoStack = [];
        }

        this.undoStack.push(memento);
        console.log(`[Line 180] History: Pushed state - ${memento.getDescription()}`);

        // Limit history size
        if (this.undoStack.length > this.maxHistory) {
            this.undoStack.shift();
            console.log(`[Line 185] History: Removed oldest state (exceeded max history)`);
        }
    }

    // Get the previous state for undo
    undo(currentState: EditorMemento): EditorMemento | null {
        if (this.undoStack.length === 0) {
            console.log(`[Line 192] History: Nothing to undo`);
            return null;
        }

        const previousState = this.undoStack.pop()!;
        this.redoStack.push(currentState);
        console.log(`[Line 198] History: Undo - moving to ${previousState.getDescription()}`);
        return previousState;
    }

    // Get the next state for redo
    redo(): EditorMemento | null {
        if (this.redoStack.length === 0) {
            console.log(`[Line 205] History: Nothing to redo`);
            return null;
        }

        const nextState = this.redoStack.pop()!;
        this.undoStack.push(nextState);
        console.log(`[Line 211] History: Redo - moving to ${nextState.getDescription()}`);
        return nextState;
    }

    // Get history info
    getUndoCount(): number {
        return this.undoStack.length;
    }

    getRedoCount(): number {
        return this.redoStack.length;
    }

    displayHistory(): void {
        console.log(`[Line 225] History Status:`);
        console.log(`  Undo stack: ${this.undoStack.length} states`);
        console.log(`  Redo stack: ${this.redoStack.length} states`);
        if (this.undoStack.length > 0) {
            console.log(`  Latest undo: ${this.undoStack[this.undoStack.length - 1].getDescription()}`);
        }
    }
}

// ============================================================
// EditorApplication - Combines all components
// ============================================================
class EditorApplication {
    private editor: TextEditor;
    private history: History;

    constructor() {
        this.editor = new TextEditor();
        this.history = new History(100);
        console.log(`[Line 243] EditorApplication: Initialized`);
    }

    // Perform action and save to history
    private saveState(): void {
        const memento = this.editor.save();
        this.history.push(memento);
    }

    type(text: string): void {
        this.saveState();
        this.editor.type(text);
    }

    delete(count: number): void {
        this.saveState();
        this.editor.delete(count);
    }

    moveCursor(position: number): void {
        this.editor.moveCursor(position);
    }

    select(start: number, end: number): void {
        this.editor.select(start, end);
    }

    replaceSelection(text: string): void {
        this.saveState();
        this.editor.replaceSelection(text);
    }

    undo(): void {
        console.log(`\n[Line 277] EditorApplication: Performing UNDO`);
        const currentState = this.editor.save();
        const previousState = this.history.undo(currentState);
        if (previousState) {
            this.editor.restore(previousState);
        }
    }

    redo(): void {
        console.log(`\n[Line 286] EditorApplication: Performing REDO`);
        const nextState = this.history.redo();
        if (nextState) {
            this.editor.restore(nextState);
        }
    }

    display(): void {
        this.editor.display();
        this.history.displayHistory();
    }

    getContent(): string {
        return this.editor.getContent();
    }
}

// ============================================================
// Second Example: Game Save State
// ============================================================

// Memento for game state
class GameMemento {
    private readonly playerHealth: number;
    private readonly playerPosition: { x: number; y: number };
    private readonly score: number;
    private readonly level: number;
    private readonly inventory: string[];
    private readonly timestamp: Date;

    constructor(
        health: number,
        position: { x: number; y: number },
        score: number,
        level: number,
        inventory: string[]
    ) {
        this.playerHealth = health;
        this.playerPosition = { ...position };
        this.score = score;
        this.level = level;
        this.inventory = [...inventory];
        this.timestamp = new Date();
        console.log(`[Line 325] GameMemento: Created save state - Level ${level}, Score ${score}`);
    }

    getHealth(): number { return this.playerHealth; }
    getPosition(): { x: number; y: number } { return { ...this.playerPosition }; }
    getScore(): number { return this.score; }
    getLevel(): number { return this.level; }
    getInventory(): string[] { return [...this.inventory]; }
    getTimestamp(): Date { return this.timestamp; }
}

// Originator - Game state
class Game {
    private health: number = 100;
    private position: { x: number; y: number } = { x: 0, y: 0 };
    private score: number = 0;
    private level: number = 1;
    private inventory: string[] = [];

    save(): GameMemento {
        console.log(`[Line 344] Game: Creating save state...`);
        return new GameMemento(
            this.health,
            this.position,
            this.score,
            this.level,
            this.inventory
        );
    }

    restore(memento: GameMemento): void {
        this.health = memento.getHealth();
        this.position = memento.getPosition();
        this.score = memento.getScore();
        this.level = memento.getLevel();
        this.inventory = memento.getInventory();
        console.log(`[Line 360] Game: Restored to Level ${this.level}, Score ${this.score}`);
    }

    // Game actions
    move(dx: number, dy: number): void {
        this.position.x += dx;
        this.position.y += dy;
        console.log(`[Line 367] Game: Moved to (${this.position.x}, ${this.position.y})`);
    }

    takeDamage(damage: number): void {
        this.health = Math.max(0, this.health - damage);
        console.log(`[Line 372] Game: Took ${damage} damage. Health: ${this.health}`);
    }

    heal(amount: number): void {
        this.health = Math.min(100, this.health + amount);
        console.log(`[Line 377] Game: Healed ${amount}. Health: ${this.health}`);
    }

    addScore(points: number): void {
        this.score += points;
        console.log(`[Line 382] Game: Added ${points} points. Score: ${this.score}`);
    }

    collectItem(item: string): void {
        this.inventory.push(item);
        console.log(`[Line 387] Game: Collected "${item}". Inventory: [${this.inventory.join(", ")}]`);
    }

    nextLevel(): void {
        this.level++;
        this.position = { x: 0, y: 0 };
        console.log(`[Line 393] Game: Advanced to Level ${this.level}`);
    }

    display(): void {
        console.log(`[Line 397] Game State:`);
        console.log(`  Level: ${this.level}`);
        console.log(`  Health: ${this.health}`);
        console.log(`  Score: ${this.score}`);
        console.log(`  Position: (${this.position.x}, ${this.position.y})`);
        console.log(`  Inventory: [${this.inventory.join(", ")}]`);
    }

    getHealth(): number { return this.health; }
}

// Caretaker - Save slots
class SaveManager {
    private saveSlots: Map<string, GameMemento> = new Map();

    saveGame(slotName: string, memento: GameMemento): void {
        this.saveSlots.set(slotName, memento);
        console.log(`[Line 413] SaveManager: Saved game to slot "${slotName}"`);
    }

    loadGame(slotName: string): GameMemento | null {
        const memento = this.saveSlots.get(slotName);
        if (memento) {
            console.log(`[Line 419] SaveManager: Loading from slot "${slotName}"`);
            return memento;
        }
        console.log(`[Line 422] SaveManager: No save found in slot "${slotName}"`);
        return null;
    }

    listSaves(): void {
        console.log(`[Line 427] SaveManager: Available saves:`);
        for (const [slot, memento] of this.saveSlots) {
            console.log(`  - ${slot}: Level ${memento.getLevel()}, Score ${memento.getScore()}`);
        }
    }
}

// ============================================================
// Demonstration
// ============================================================
function main(): void {
    console.log("=".repeat(60));
    console.log("  Memento Design Pattern Demonstration");
    console.log("=".repeat(60));

    // Demo 1: Text Editor with Undo/Redo
    console.log("\n--- Demo 1: Text Editor with Undo/Redo ---\n");

    const app = new EditorApplication();

    console.log("\n[Action] Typing 'Hello World'...");
    app.type("Hello");
    app.type(" ");
    app.type("World");
    app.display();

    console.log("\n[Action] Typing '!!!'...");
    app.type("!!!");
    app.display();

    console.log("\n[Action] Performing Undo...");
    app.undo();
    console.log(`Content after undo: "${app.getContent()}"`);

    console.log("\n[Action] Performing another Undo...");
    app.undo();
    console.log(`Content after undo: "${app.getContent()}"`);

    console.log("\n[Action] Performing Redo...");
    app.redo();
    console.log(`Content after redo: "${app.getContent()}"`);

    console.log("\n[Action] Typing ' - TypeScript'...");
    app.type(" - TypeScript");
    console.log(`Content: "${app.getContent()}"`);

    console.log("\n[Action] Trying to Redo (should have nothing)...");
    app.redo();
    console.log(`Content: "${app.getContent()}"`);

    // Demonstrate selection and replace
    console.log("\n[Action] Select and replace 'World' with 'Memento'...");
    app.select(6, 11);
    app.replaceSelection("Memento");
    console.log(`Content: "${app.getContent()}"`);

    // Multiple undos
    console.log("\n[Action] Multiple undos to go back to 'Hello'...");
    app.undo();
    app.undo();
    app.undo();
    app.undo();
    console.log(`Content after multiple undos: "${app.getContent()}"`);

    // Demo 2: Game Save States
    console.log("\n\n--- Demo 2: Game Save States ---\n");

    const game = new Game();
    const saveManager = new SaveManager();

    console.log("\n[Action] Playing through Level 1...");
    game.move(5, 3);
    game.collectItem("Sword");
    game.addScore(100);
    game.takeDamage(20);

    console.log("\n[Action] Saving game to 'checkpoint1'...");
    saveManager.saveGame("checkpoint1", game.save());

    console.log("\n[Action] Continuing to play...");
    game.move(10, 5);
    game.collectItem("Shield");
    game.addScore(200);
    game.takeDamage(50);

    console.log("\n[Action] Saving game to 'checkpoint2'...");
    saveManager.saveGame("checkpoint2", game.save());

    console.log("\n[Action] Dangerous area - taking heavy damage...");
    game.takeDamage(40);
    game.display();

    console.log("\n[Action] Game over! Loading from checkpoint2...");
    const savedState = saveManager.loadGame("checkpoint2");
    if (savedState) {
        game.restore(savedState);
    }
    game.display();

    console.log("\n[Action] Want to restart level? Loading checkpoint1...");
    const checkpoint1 = saveManager.loadGame("checkpoint1");
    if (checkpoint1) {
        game.restore(checkpoint1);
    }
    game.display();

    console.log("\n[Action] Listing all save slots...");
    saveManager.listSaves();

    console.log("\n" + "=".repeat(60));
    console.log("  End of Demonstration");
    console.log("=".repeat(60));
}

main();
