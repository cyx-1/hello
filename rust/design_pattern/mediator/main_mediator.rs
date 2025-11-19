// Mediator Design Pattern - Chat Room Example
// Demonstrates how a mediator coordinates communication between colleagues

use std::cell::RefCell;
use std::rc::Rc;

// Mediator trait - defines the interface for communication
trait Mediator {
    fn send_message(&self, message: &str, sender_id: usize);
    fn add_user(&mut self, user: Rc<RefCell<User>>);
}

// Concrete Mediator - ChatRoom coordinates all user communication
struct ChatRoom {
    name: String,
    users: Vec<Rc<RefCell<User>>>,
}

impl ChatRoom {
    fn new(name: &str) -> Self {
        println!("[ChatRoom] Creating chat room: '{}'", name);
        ChatRoom {
            name: name.to_string(),
            users: Vec::new(),
        }
    }
}

impl Mediator for ChatRoom {
    fn add_user(&mut self, user: Rc<RefCell<User>>) {
        let user_name = user.borrow().name.clone();
        println!("[ChatRoom] User '{}' joined '{}'", user_name, self.name);
        self.users.push(user);
    }

    fn send_message(&self, message: &str, sender_id: usize) {
        // Find sender name for display
        let sender_name = self.users
            .iter()
            .find(|u| u.borrow().id == sender_id)
            .map(|u| u.borrow().name.clone())
            .unwrap_or_else(|| "Unknown".to_string());

        println!("[ChatRoom] Mediating message from '{}': \"{}\"", sender_name, message);

        // Deliver message to all other users (not the sender)
        for user in &self.users {
            let user_ref = user.borrow();
            if user_ref.id != sender_id {
                println!("[ChatRoom] -> Delivering to '{}'", user_ref.name);
                drop(user_ref); // Release borrow before calling receive
                user.borrow_mut().receive(message, &sender_name);
            }
        }
    }
}

// Colleague - User who communicates through the mediator
struct User {
    id: usize,
    name: String,
    mediator: Option<Rc<RefCell<dyn Mediator>>>,
    messages_received: Vec<String>,
}

impl User {
    fn new(id: usize, name: &str) -> Rc<RefCell<Self>> {
        println!("[User] Creating user: '{}' (id: {})", name, id);
        Rc::new(RefCell::new(User {
            id,
            name: name.to_string(),
            mediator: None,
            messages_received: Vec::new(),
        }))
    }

    fn set_mediator(&mut self, mediator: Rc<RefCell<dyn Mediator>>) {
        self.mediator = Some(mediator);
    }

    fn send(&self, message: &str) {
        println!("[User] '{}' sending: \"{}\"", self.name, message);
        if let Some(mediator) = &self.mediator {
            mediator.borrow().send_message(message, self.id);
        } else {
            println!("[User] '{}' has no chat room to send message!", self.name);
        }
    }

    fn receive(&mut self, message: &str, from: &str) {
        let formatted = format!("{}: {}", from, message);
        println!("[User] '{}' received: \"{}\"", self.name, formatted);
        self.messages_received.push(formatted);
    }

    fn show_inbox(&self) {
        println!("[User] '{}' inbox ({} messages):", self.name, self.messages_received.len());
        for (i, msg) in self.messages_received.iter().enumerate() {
            println!("       {}. {}", i + 1, msg);
        }
    }
}

// Helper function to connect user to chat room
fn join_chat_room(user: &Rc<RefCell<User>>, chat_room: &Rc<RefCell<ChatRoom>>) {
    user.borrow_mut().set_mediator(chat_room.clone());
    chat_room.borrow_mut().add_user(user.clone());
}

fn main() {
    println!("=== Mediator Pattern: Chat Room Demo ===\n");

    // Create the mediator (chat room)
    let chat_room = Rc::new(RefCell::new(ChatRoom::new("Rust Developers")));

    println!();

    // Create colleagues (users)
    let alice = User::new(1, "Alice");
    let bob = User::new(2, "Bob");
    let charlie = User::new(3, "Charlie");

    println!();

    // Register users with the mediator
    println!("--- Users Joining Chat Room ---");
    join_chat_room(&alice, &chat_room);
    join_chat_room(&bob, &chat_room);
    join_chat_room(&charlie, &chat_room);

    println!("\n--- Communication Through Mediator ---\n");

    // Users communicate through the mediator
    alice.borrow().send("Hello everyone! Anyone working on design patterns?");

    println!();

    bob.borrow().send("Hi Alice! Yes, I'm implementing the Mediator pattern.");

    println!();

    charlie.borrow().send("Great topic! The Mediator helps reduce coupling.");

    println!();

    alice.borrow().send("Exactly! Objects don't need direct references to each other.");

    println!("\n--- Final Inbox Status ---\n");

    // Show what each user received
    alice.borrow().show_inbox();
    println!();
    bob.borrow().show_inbox();
    println!();
    charlie.borrow().show_inbox();

    println!("\n=== Demo Complete ===");
}
