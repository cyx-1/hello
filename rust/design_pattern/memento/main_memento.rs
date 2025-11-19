// Memento Design Pattern - Text Editor Example
// Demonstrates save/restore functionality using Originator, Memento, and Caretaker

use std::time::{SystemTime, UNIX_EPOCH};

// Memento: Stores the internal state of the Originator
// In Rust, we keep this struct's fields private to maintain encapsulation
#[derive(Clone)]
struct EditorMemento {
    content: String,
    cursor_position: usize,
    timestamp: u64,
}

impl EditorMemento {
    fn get_timestamp(&self) -> u64 {
        self.timestamp
    }
}

// Originator: The object whose state needs to be saved and restored
struct TextEditor {
    content: String,
    cursor_position: usize,
}

impl TextEditor {
    fn new() -> Self {
        println!("[Editor] Creating new text editor");
        TextEditor {
            content: String::new(),
            cursor_position: 0,
        }
    }

    fn write(&mut self, text: &str) {
        self.content.push_str(text);
        self.cursor_position = self.content.len();
        println!("[Editor] Writing: \"{}\"", text);
        println!("[Editor] Current content: \"{}\"", self.content);
    }

    fn set_cursor(&mut self, position: usize) {
        self.cursor_position = position.min(self.content.len());
        println!("[Editor] Cursor moved to position: {}", self.cursor_position);
    }

    fn get_content(&self) -> &str {
        &self.content
    }

    fn get_cursor_position(&self) -> usize {
        self.cursor_position
    }

    // Save current state to a memento
    fn save(&self) -> EditorMemento {
        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs();

        println!("[Editor] Saving state - Content: \"{}\", Cursor: {}",
                 self.content, self.cursor_position);

        EditorMemento {
            content: self.content.clone(),
            cursor_position: self.cursor_position,
            timestamp,
        }
    }

    // Restore state from a memento
    fn restore(&mut self, memento: &EditorMemento) {
        self.content = memento.content.clone();
        self.cursor_position = memento.cursor_position;
        println!("[Editor] Restoring state - Content: \"{}\", Cursor: {}",
                 self.content, self.cursor_position);
    }
}

// Caretaker: Manages the history of mementos
struct History {
    snapshots: Vec<EditorMemento>,
}

impl History {
    fn new() -> Self {
        println!("[History] Creating new history manager");
        History {
            snapshots: Vec::new(),
        }
    }

    fn push(&mut self, memento: EditorMemento) {
        println!("[History] Saving snapshot #{} (timestamp: {})",
                 self.snapshots.len() + 1, memento.get_timestamp());
        self.snapshots.push(memento);
    }

    fn pop(&mut self) -> Option<EditorMemento> {
        if let Some(memento) = self.snapshots.pop() {
            println!("[History] Retrieving snapshot (timestamp: {})",
                     memento.get_timestamp());
            Some(memento)
        } else {
            println!("[History] No snapshots available!");
            None
        }
    }

    fn len(&self) -> usize {
        self.snapshots.len()
    }

    fn is_empty(&self) -> bool {
        self.snapshots.is_empty()
    }
}

fn main() {
    println!("=== Memento Pattern: Text Editor Example ===\n");

    // Create the originator (text editor) and caretaker (history)
    let mut editor = TextEditor::new();
    let mut history = History::new();

    println!("\n--- Step 1: Initial writing ---");
    editor.write("Hello");
    history.push(editor.save());

    println!("\n--- Step 2: Continue writing ---");
    editor.write(", World");
    history.push(editor.save());

    println!("\n--- Step 3: Add more text ---");
    editor.write("! Welcome to Rust.");
    editor.set_cursor(5);
    history.push(editor.save());

    println!("\n--- Step 4: Make a mistake ---");
    editor.write(" OOPS! This should not be here.");
    println!("[Main] Current editor state: \"{}\"", editor.get_content());

    println!("\n--- Step 5: Undo last action (restore previous state) ---");
    if let Some(memento) = history.pop() {
        editor.restore(&memento);
    }
    println!("[Main] After undo: \"{}\"", editor.get_content());
    println!("[Main] Cursor at position: {}", editor.get_cursor_position());

    println!("\n--- Step 6: Undo again ---");
    if let Some(memento) = history.pop() {
        editor.restore(&memento);
    }
    println!("[Main] After second undo: \"{}\"", editor.get_content());

    println!("\n--- Step 7: Undo once more ---");
    if let Some(memento) = history.pop() {
        editor.restore(&memento);
    }
    println!("[Main] After third undo: \"{}\"", editor.get_content());

    println!("\n--- Step 8: Try to undo when history is empty ---");
    if history.is_empty() {
        println!("[Main] Cannot undo: History is empty");
    } else if let Some(memento) = history.pop() {
        editor.restore(&memento);
    }

    println!("\n--- Final State ---");
    println!("[Main] Editor content: \"{}\"", editor.get_content());
    println!("[Main] Remaining snapshots in history: {}", history.len());

    println!("\n=== Memento Pattern Demo Complete ===");
}
