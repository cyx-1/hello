// Command Design Pattern in Rust
// Demonstrates a text editor with undo functionality

use std::cell::RefCell;
use std::rc::Rc;

// Receiver: The object that performs the actual work
struct TextEditor {
    content: String,
}

impl TextEditor {
    fn new() -> Self {
        println!("[TextEditor] Created new text editor");
        TextEditor {
            content: String::new(),
        }
    }

    fn insert(&mut self, text: &str, position: usize) {
        let pos = position.min(self.content.len());
        self.content.insert_str(pos, text);
        println!("[TextEditor] Inserted '{}' at position {}", text, pos);
    }

    fn delete(&mut self, position: usize, length: usize) -> String {
        let pos = position.min(self.content.len());
        let end = (pos + length).min(self.content.len());
        let deleted: String = self.content.drain(pos..end).collect();
        println!("[TextEditor] Deleted '{}' from position {}", deleted, pos);
        deleted
    }

    fn get_content(&self) -> &str {
        &self.content
    }
}

// Command trait: The interface for all commands
trait Command {
    fn execute(&mut self);
    fn undo(&mut self);
    fn description(&self) -> String;
}

// Concrete Command: Insert text
struct InsertCommand {
    editor: Rc<RefCell<TextEditor>>,
    text: String,
    position: usize,
}

impl InsertCommand {
    fn new(editor: Rc<RefCell<TextEditor>>, text: String, position: usize) -> Self {
        InsertCommand {
            editor,
            text,
            position,
        }
    }
}

impl Command for InsertCommand {
    fn execute(&mut self) {
        println!(">>> Executing InsertCommand: '{}' at {}", self.text, self.position);
        self.editor.borrow_mut().insert(&self.text, self.position);
    }

    fn undo(&mut self) {
        println!("<<< Undoing InsertCommand: removing '{}' from {}", self.text, self.position);
        self.editor.borrow_mut().delete(self.position, self.text.len());
    }

    fn description(&self) -> String {
        format!("Insert '{}' at position {}", self.text, self.position)
    }
}

// Concrete Command: Delete text
struct DeleteCommand {
    editor: Rc<RefCell<TextEditor>>,
    position: usize,
    length: usize,
    deleted_text: String, // Store for undo
}

impl DeleteCommand {
    fn new(editor: Rc<RefCell<TextEditor>>, position: usize, length: usize) -> Self {
        DeleteCommand {
            editor,
            position,
            length,
            deleted_text: String::new(),
        }
    }
}

impl Command for DeleteCommand {
    fn execute(&mut self) {
        println!(">>> Executing DeleteCommand: {} chars at position {}", self.length, self.position);
        self.deleted_text = self.editor.borrow_mut().delete(self.position, self.length);
    }

    fn undo(&mut self) {
        println!("<<< Undoing DeleteCommand: restoring '{}' at {}", self.deleted_text, self.position);
        self.editor.borrow_mut().insert(&self.deleted_text, self.position);
    }

    fn description(&self) -> String {
        format!("Delete {} chars at position {}", self.length, self.position)
    }
}

// Concrete Command: Replace text (combines delete + insert)
struct ReplaceCommand {
    editor: Rc<RefCell<TextEditor>>,
    position: usize,
    old_length: usize,
    new_text: String,
    old_text: String, // Store for undo
}

impl ReplaceCommand {
    fn new(editor: Rc<RefCell<TextEditor>>, position: usize, old_length: usize, new_text: String) -> Self {
        ReplaceCommand {
            editor,
            position,
            old_length,
            new_text,
            old_text: String::new(),
        }
    }
}

impl Command for ReplaceCommand {
    fn execute(&mut self) {
        println!(">>> Executing ReplaceCommand: {} chars with '{}' at {}", self.old_length, self.new_text, self.position);
        self.old_text = self.editor.borrow_mut().delete(self.position, self.old_length);
        self.editor.borrow_mut().insert(&self.new_text, self.position);
    }

    fn undo(&mut self) {
        println!("<<< Undoing ReplaceCommand: restoring '{}' at {}", self.old_text, self.position);
        self.editor.borrow_mut().delete(self.position, self.new_text.len());
        self.editor.borrow_mut().insert(&self.old_text, self.position);
    }

    fn description(&self) -> String {
        format!("Replace {} chars with '{}' at position {}", self.old_length, self.new_text, self.position)
    }
}

// Invoker: Manages command execution and history
struct EditorController {
    history: Vec<Box<dyn Command>>,
    editor: Rc<RefCell<TextEditor>>,
}

impl EditorController {
    fn new(editor: Rc<RefCell<TextEditor>>) -> Self {
        println!("[EditorController] Created new controller");
        EditorController {
            history: Vec::new(),
            editor,
        }
    }

    fn execute_command(&mut self, mut command: Box<dyn Command>) {
        println!("\n[EditorController] Executing: {}", command.description());
        command.execute();
        self.history.push(command);
        self.print_content();
    }

    fn undo(&mut self) {
        if let Some(mut command) = self.history.pop() {
            println!("\n[EditorController] Undoing: {}", command.description());
            command.undo();
            self.print_content();
        } else {
            println!("\n[EditorController] Nothing to undo!");
        }
    }

    fn print_content(&self) {
        println!("[EditorController] Current content: \"{}\"", self.editor.borrow().get_content());
    }

    fn history_size(&self) -> usize {
        self.history.len()
    }
}

fn main() {
    println!("=== Command Design Pattern Demo ===\n");

    // Create the receiver
    let editor = Rc::new(RefCell::new(TextEditor::new()));

    // Create the invoker
    let mut controller = EditorController::new(Rc::clone(&editor));

    println!("\n--- Executing Commands ---");

    // Create and execute commands
    let cmd1 = Box::new(InsertCommand::new(Rc::clone(&editor), "Hello".to_string(), 0));
    controller.execute_command(cmd1);

    let cmd2 = Box::new(InsertCommand::new(Rc::clone(&editor), " World".to_string(), 5));
    controller.execute_command(cmd2);

    let cmd3 = Box::new(InsertCommand::new(Rc::clone(&editor), "!".to_string(), 11));
    controller.execute_command(cmd3);

    // Delete command
    let cmd4 = Box::new(DeleteCommand::new(Rc::clone(&editor), 5, 6));
    controller.execute_command(cmd4);

    // Replace command
    let cmd5 = Box::new(ReplaceCommand::new(Rc::clone(&editor), 0, 5, "Goodbye".to_string()));
    controller.execute_command(cmd5);

    println!("\n--- Command History ---");
    println!("Total commands in history: {}", controller.history_size());

    println!("\n--- Undoing Commands ---");

    // Undo all commands
    controller.undo(); // Undo Replace
    controller.undo(); // Undo Delete
    controller.undo(); // Undo Insert !
    controller.undo(); // Undo Insert World
    controller.undo(); // Undo Insert Hello

    // Try to undo when history is empty
    controller.undo();

    println!("\n=== Demo Complete ===");
}
