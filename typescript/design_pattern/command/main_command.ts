/**
 * Command Design Pattern in TypeScript
 *
 * The Command pattern encapsulates a request as an object, thereby allowing
 * parameterization of clients with different requests, queuing of requests,
 * and support for undoable operations.
 */

// Command Interface - declares the execution and undo methods
interface Command {
    execute(): void;
    undo(): void;
    getDescription(): string;
}

// Receiver - the object that performs the actual work
class TextEditor {
    private content: string = "";
    private cursorPosition: number = 0;

    getContent(): string {
        return this.content;
    }

    getCursorPosition(): number {
        return this.cursorPosition;
    }

    setCursorPosition(position: number): void {
        this.cursorPosition = Math.max(0, Math.min(position, this.content.length));
        console.log(`[Line 31] TextEditor: Cursor moved to position ${this.cursorPosition}`);
    }

    insertAt(position: number, text: string): void {
        const before = this.content.substring(0, position);
        const after = this.content.substring(position);
        this.content = before + text + after;
        this.cursorPosition = position + text.length;
        console.log(`[Line 38] TextEditor: Inserted "${text}" at position ${position}`);
        console.log(`[Line 39] TextEditor: Content is now "${this.content}"`);
    }

    deleteRange(start: number, length: number): string {
        const deleted = this.content.substring(start, start + length);
        const before = this.content.substring(0, start);
        const after = this.content.substring(start + length);
        this.content = before + after;
        this.cursorPosition = start;
        console.log(`[Line 47] TextEditor: Deleted "${deleted}" from position ${start}`);
        console.log(`[Line 48] TextEditor: Content is now "${this.content}"`);
        return deleted;
    }

    replaceRange(start: number, length: number, newText: string): string {
        const replaced = this.content.substring(start, start + length);
        const before = this.content.substring(0, start);
        const after = this.content.substring(start + length);
        this.content = before + newText + after;
        this.cursorPosition = start + newText.length;
        console.log(`[Line 57] TextEditor: Replaced "${replaced}" with "${newText}" at position ${start}`);
        console.log(`[Line 58] TextEditor: Content is now "${this.content}"`);
        return replaced;
    }

    selectAll(): void {
        console.log(`[Line 63] TextEditor: Selected all text - "${this.content}"`);
    }

    clear(): void {
        this.content = "";
        this.cursorPosition = 0;
        console.log(`[Line 69] TextEditor: Cleared all content`);
    }
}

// Concrete Command 1: Insert Text
class InsertTextCommand implements Command {
    private editor: TextEditor;
    private text: string;
    private position: number;

    constructor(editor: TextEditor, text: string, position: number) {
        this.editor = editor;
        this.text = text;
        this.position = position;
        console.log(`[Line 82] InsertTextCommand: Created command to insert "${text}" at position ${position}`);
    }

    execute(): void {
        console.log(`[Line 86] InsertTextCommand: Executing insert`);
        this.editor.insertAt(this.position, this.text);
    }

    undo(): void {
        console.log(`[Line 91] InsertTextCommand: Undoing insert`);
        this.editor.deleteRange(this.position, this.text.length);
    }

    getDescription(): string {
        return `Insert "${this.text}" at position ${this.position}`;
    }
}

// Concrete Command 2: Delete Text
class DeleteTextCommand implements Command {
    private editor: TextEditor;
    private position: number;
    private length: number;
    private deletedText: string = "";

    constructor(editor: TextEditor, position: number, length: number) {
        this.editor = editor;
        this.position = position;
        this.length = length;
        console.log(`[Line 110] DeleteTextCommand: Created command to delete ${length} chars at position ${position}`);
    }

    execute(): void {
        console.log(`[Line 114] DeleteTextCommand: Executing delete`);
        this.deletedText = this.editor.deleteRange(this.position, this.length);
    }

    undo(): void {
        console.log(`[Line 119] DeleteTextCommand: Undoing delete - restoring "${this.deletedText}"`);
        this.editor.insertAt(this.position, this.deletedText);
    }

    getDescription(): string {
        return `Delete ${this.length} characters at position ${this.position}`;
    }
}

// Concrete Command 3: Replace Text
class ReplaceTextCommand implements Command {
    private editor: TextEditor;
    private position: number;
    private length: number;
    private newText: string;
    private oldText: string = "";

    constructor(editor: TextEditor, position: number, length: number, newText: string) {
        this.editor = editor;
        this.position = position;
        this.length = length;
        this.newText = newText;
        console.log(`[Line 140] ReplaceTextCommand: Created command to replace ${length} chars with "${newText}" at position ${position}`);
    }

    execute(): void {
        console.log(`[Line 144] ReplaceTextCommand: Executing replace`);
        this.oldText = this.editor.replaceRange(this.position, this.length, this.newText);
    }

    undo(): void {
        console.log(`[Line 149] ReplaceTextCommand: Undoing replace - restoring "${this.oldText}"`);
        this.editor.replaceRange(this.position, this.newText.length, this.oldText);
    }

    getDescription(): string {
        return `Replace ${this.length} characters with "${this.newText}" at position ${this.position}`;
    }
}

// Concrete Command 4: Composite/Macro Command
class MacroCommand implements Command {
    private commands: Command[] = [];
    private name: string;

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 165] MacroCommand: Created macro "${name}"`);
    }

    addCommand(command: Command): void {
        this.commands.push(command);
        console.log(`[Line 170] MacroCommand: Added command to "${this.name}" - ${command.getDescription()}`);
    }

    execute(): void {
        console.log(`[Line 174] MacroCommand: Executing macro "${this.name}" with ${this.commands.length} commands`);
        for (const command of this.commands) {
            command.execute();
        }
    }

    undo(): void {
        console.log(`[Line 181] MacroCommand: Undoing macro "${this.name}" (${this.commands.length} commands in reverse)`);
        // Undo in reverse order
        for (let i = this.commands.length - 1; i >= 0; i--) {
            this.commands[i].undo();
        }
    }

    getDescription(): string {
        return `Macro "${this.name}" (${this.commands.length} commands)`;
    }
}

// Invoker - manages command execution, history, and undo/redo
class CommandManager {
    private history: Command[] = [];
    private redoStack: Command[] = [];
    private commandQueue: Command[] = [];

    executeCommand(command: Command): void {
        console.log(`\n[Line 199] CommandManager: Executing command - ${command.getDescription()}`);
        command.execute();
        this.history.push(command);
        // Clear redo stack when new command is executed
        this.redoStack = [];
        console.log(`[Line 204] CommandManager: History size is now ${this.history.length}`);
    }

    queueCommand(command: Command): void {
        this.commandQueue.push(command);
        console.log(`[Line 209] CommandManager: Queued command - ${command.getDescription()}`);
        console.log(`[Line 210] CommandManager: Queue size is now ${this.commandQueue.length}`);
    }

    executeQueue(): void {
        console.log(`\n[Line 214] CommandManager: Executing queue of ${this.commandQueue.length} commands`);
        while (this.commandQueue.length > 0) {
            const command = this.commandQueue.shift()!;
            console.log(`\n[Line 217] CommandManager: Dequeuing and executing - ${command.getDescription()}`);
            command.execute();
            this.history.push(command);
        }
        this.redoStack = [];
        console.log(`[Line 222] CommandManager: Queue executed. History size is now ${this.history.length}`);
    }

    undo(): boolean {
        if (this.history.length === 0) {
            console.log(`[Line 227] CommandManager: Nothing to undo`);
            return false;
        }

        const command = this.history.pop()!;
        console.log(`\n[Line 232] CommandManager: Undoing - ${command.getDescription()}`);
        command.undo();
        this.redoStack.push(command);
        console.log(`[Line 235] CommandManager: History size is now ${this.history.length}, Redo stack size is ${this.redoStack.length}`);
        return true;
    }

    redo(): boolean {
        if (this.redoStack.length === 0) {
            console.log(`[Line 241] CommandManager: Nothing to redo`);
            return false;
        }

        const command = this.redoStack.pop()!;
        console.log(`\n[Line 246] CommandManager: Redoing - ${command.getDescription()}`);
        command.execute();
        this.history.push(command);
        console.log(`[Line 249] CommandManager: History size is now ${this.history.length}, Redo stack size is ${this.redoStack.length}`);
        return true;
    }

    getHistorySize(): number {
        return this.history.length;
    }

    getRedoStackSize(): number {
        return this.redoStack.length;
    }

    printHistory(): void {
        console.log(`\n[Line 262] CommandManager: Command History (${this.history.length} items):`);
        this.history.forEach((cmd, index) => {
            console.log(`  ${index + 1}. ${cmd.getDescription()}`);
        });
    }
}

// Main demonstration
function main(): void {
    console.log("=== Command Pattern Demonstration ===");
    console.log("Text Editor with Undo/Redo Functionality\n");

    // Create the receiver and invoker
    const editor = new TextEditor();
    const manager = new CommandManager();

    // ============================================================
    // Demo 1: Basic Command Execution
    // ============================================================
    console.log("\n--- Demo 1: Basic Command Execution ---\n");

    // Create and execute commands
    const insertHello = new InsertTextCommand(editor, "Hello", 0);
    manager.executeCommand(insertHello);

    const insertWorld = new InsertTextCommand(editor, " World", 5);
    manager.executeCommand(insertWorld);

    const insertExclaim = new InsertTextCommand(editor, "!", 11);
    manager.executeCommand(insertExclaim);

    console.log(`\n[Line 293] Current content: "${editor.getContent()}"`);

    // ============================================================
    // Demo 2: Undo Functionality
    // ============================================================
    console.log("\n--- Demo 2: Undo Functionality ---");

    manager.undo(); // Remove "!"
    console.log(`[Line 301] After undo: "${editor.getContent()}"`);

    manager.undo(); // Remove " World"
    console.log(`[Line 304] After undo: "${editor.getContent()}"`);

    // ============================================================
    // Demo 3: Redo Functionality
    // ============================================================
    console.log("\n--- Demo 3: Redo Functionality ---");

    manager.redo(); // Re-add " World"
    console.log(`[Line 312] After redo: "${editor.getContent()}"`);

    // ============================================================
    // Demo 4: Delete and Replace Commands
    // ============================================================
    console.log("\n--- Demo 4: Delete and Replace Commands ---\n");

    // Delete "World" (positions 6-11)
    const deleteWorld = new DeleteTextCommand(editor, 6, 5);
    manager.executeCommand(deleteWorld);

    // Replace "Hello " with "Hi "
    const replaceHello = new ReplaceTextCommand(editor, 0, 6, "Hi ");
    manager.executeCommand(replaceHello);

    // Insert new text
    const insertTS = new InsertTextCommand(editor, "TypeScript", 3);
    manager.executeCommand(insertTS);

    console.log(`\n[Line 330] Current content: "${editor.getContent()}"`);

    // ============================================================
    // Demo 5: Command Queue
    // ============================================================
    console.log("\n--- Demo 5: Command Queue ---\n");

    // Queue multiple commands
    manager.queueCommand(new InsertTextCommand(editor, " is", 13));
    manager.queueCommand(new InsertTextCommand(editor, " awesome", 16));
    manager.queueCommand(new InsertTextCommand(editor, "!", 24));

    // Execute all queued commands at once
    manager.executeQueue();

    console.log(`\n[Line 345] After queue execution: "${editor.getContent()}"`);

    // ============================================================
    // Demo 6: Macro Command
    // ============================================================
    console.log("\n--- Demo 6: Macro Command (Composite) ---\n");

    // Undo everything to start fresh
    console.log("[Line 352] Undoing all commands to start fresh...");
    while (manager.getHistorySize() > 0) {
        manager.undo();
    }
    console.log(`[Line 356] Content after undoing all: "${editor.getContent()}"`);

    // Create a macro that formats text
    const formatMacro = new MacroCommand("Format Greeting");
    formatMacro.addCommand(new InsertTextCommand(editor, ">>> ", 0));
    formatMacro.addCommand(new InsertTextCommand(editor, "Welcome", 4));
    formatMacro.addCommand(new InsertTextCommand(editor, " <<<", 11));

    // Execute the macro
    manager.executeCommand(formatMacro);

    console.log(`\n[Line 367] After macro execution: "${editor.getContent()}"`);

    // Undo the entire macro (all three operations)
    manager.undo();
    console.log(`[Line 371] After undoing macro: "${editor.getContent()}"`);

    // Redo the macro
    manager.redo();
    console.log(`[Line 375] After redoing macro: "${editor.getContent()}"`);

    // ============================================================
    // Demo 7: Command History
    // ============================================================
    console.log("\n--- Demo 7: Command History ---");
    manager.printHistory();

    // ============================================================
    // Demo 8: Edge Cases
    // ============================================================
    console.log("\n--- Demo 8: Edge Cases ---");

    // Try to undo when nothing to undo
    while (manager.getHistorySize() > 0) {
        manager.undo();
    }
    manager.undo(); // Should show "Nothing to undo"

    // Try to redo when nothing to redo
    manager.redo(); // Should show "Nothing to redo"

    console.log("\n=== End of Demonstration ===");
}

// Run the demonstration
main();
