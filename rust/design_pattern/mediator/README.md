# Mediator Design Pattern in Rust

## Description

The **Mediator** design pattern defines an object (the mediator) that encapsulates how a set of objects (colleagues) interact. This pattern promotes loose coupling by preventing objects from referring to each other explicitly, allowing their interaction to be varied independently.

In this implementation, we demonstrate a **Chat Room** example where:
- **ChatRoom** acts as the mediator, coordinating all communication
- **Users** are the colleagues who send and receive messages through the mediator
- Users never communicate directly; all messages flow through the ChatRoom

## Source Code

```rust
 1  // Mediator Design Pattern - Chat Room Example
 2  // Demonstrates how a mediator coordinates communication between colleagues
 3
 4  use std::cell::RefCell;
 5  use std::rc::Rc;
 6
 7  // Mediator trait - defines the interface for communication
 8  trait Mediator {
 9      fn send_message(&self, message: &str, sender_id: usize);
10      fn add_user(&mut self, user: Rc<RefCell<User>>);
11  }
12
13  // Concrete Mediator - ChatRoom coordinates all user communication
14  struct ChatRoom {
15      name: String,
16      users: Vec<Rc<RefCell<User>>>,
17  }
18
19  impl ChatRoom {
20      fn new(name: &str) -> Self {
21          println!("[ChatRoom] Creating chat room: '{}'", name);
22          ChatRoom {
23              name: name.to_string(),
24              users: Vec::new(),
25          }
26      }
27  }
28
29  impl Mediator for ChatRoom {
30      fn add_user(&mut self, user: Rc<RefCell<User>>) {
31          let user_name = user.borrow().name.clone();
32          println!("[ChatRoom] User '{}' joined '{}'", user_name, self.name);
33          self.users.push(user);
34      }
35
36      fn send_message(&self, message: &str, sender_id: usize) {
37          // Find sender name for display
38          let sender_name = self.users
39              .iter()
40              .find(|u| u.borrow().id == sender_id)
41              .map(|u| u.borrow().name.clone())
42              .unwrap_or_else(|| "Unknown".to_string());
43
44          println!("[ChatRoom] Mediating message from '{}': \"{}\"", sender_name, message);
45
46          // Deliver message to all other users (not the sender)
47          for user in &self.users {
48              let user_ref = user.borrow();
49              if user_ref.id != sender_id {
50                  println!("[ChatRoom] -> Delivering to '{}'", user_ref.name);
51                  drop(user_ref); // Release borrow before calling receive
52                  user.borrow_mut().receive(message, &sender_name);
53              }
54          }
55      }
56  }
57
58  // Colleague - User who communicates through the mediator
59  struct User {
60      id: usize,
61      name: String,
62      mediator: Option<Rc<RefCell<dyn Mediator>>>,
63      messages_received: Vec<String>,
64  }
65
66  impl User {
67      fn new(id: usize, name: &str) -> Rc<RefCell<Self>> {
68          println!("[User] Creating user: '{}' (id: {})", name, id);
69          Rc::new(RefCell::new(User {
70              id,
71              name: name.to_string(),
72              mediator: None,
73              messages_received: Vec::new(),
74          }))
75      }
76
77      fn set_mediator(&mut self, mediator: Rc<RefCell<dyn Mediator>>) {
78          self.mediator = Some(mediator);
79      }
80
81      fn send(&self, message: &str) {
82          println!("[User] '{}' sending: \"{}\"", self.name, message);
83          if let Some(mediator) = &self.mediator {
84              mediator.borrow().send_message(message, self.id);
85          } else {
86              println!("[User] '{}' has no chat room to send message!", self.name);
87          }
88      }
89
90      fn receive(&mut self, message: &str, from: &str) {
91          let formatted = format!("{}: {}", from, message);
92          println!("[User] '{}' received: \"{}\"", self.name, formatted);
93          self.messages_received.push(formatted);
94      }
95
96      fn show_inbox(&self) {
97          println!("[User] '{}' inbox ({} messages):", self.name, self.messages_received.len());
98          for (i, msg) in self.messages_received.iter().enumerate() {
99              println!("       {}. {}", i + 1, msg);
100         }
101     }
102 }
103
104 // Helper function to connect user to chat room
105 fn join_chat_room(user: &Rc<RefCell<User>>, chat_room: &Rc<RefCell<ChatRoom>>) {
106     user.borrow_mut().set_mediator(chat_room.clone());
107     chat_room.borrow_mut().add_user(user.clone());
108 }
109
110 fn main() {
111     println!("=== Mediator Pattern: Chat Room Demo ===\n");
112
113     // Create the mediator (chat room)
114     let chat_room = Rc::new(RefCell::new(ChatRoom::new("Rust Developers")));
115
116     println!();
117
118     // Create colleagues (users)
119     let alice = User::new(1, "Alice");
120     let bob = User::new(2, "Bob");
121     let charlie = User::new(3, "Charlie");
122
123     println!();
124
125     // Register users with the mediator
126     println!("--- Users Joining Chat Room ---");
127     join_chat_room(&alice, &chat_room);
128     join_chat_room(&bob, &chat_room);
129     join_chat_room(&charlie, &chat_room);
130
131     println!("\n--- Communication Through Mediator ---\n");
132
133     // Users communicate through the mediator
134     alice.borrow().send("Hello everyone! Anyone working on design patterns?");
135
136     println!();
137
138     bob.borrow().send("Hi Alice! Yes, I'm implementing the Mediator pattern.");
139
140     println!();
141
142     charlie.borrow().send("Great topic! The Mediator helps reduce coupling.");
143
144     println!();
145
146     alice.borrow().send("Exactly! Objects don't need direct references to each other.");
147
148     println!("\n--- Final Inbox Status ---\n");
149
150     // Show what each user received
151     alice.borrow().show_inbox();
152     println!();
153     bob.borrow().show_inbox();
154     println!();
155     charlie.borrow().show_inbox();
156
157     println!("\n=== Demo Complete ===");
158 }
```

## Program Output

```
=== Mediator Pattern: Chat Room Demo ===

[ChatRoom] Creating chat room: 'Rust Developers'

[User] Creating user: 'Alice' (id: 1)
[User] Creating user: 'Bob' (id: 2)
[User] Creating user: 'Charlie' (id: 3)

--- Users Joining Chat Room ---
[ChatRoom] User 'Alice' joined 'Rust Developers'
[ChatRoom] User 'Bob' joined 'Rust Developers'
[ChatRoom] User 'Charlie' joined 'Rust Developers'

--- Communication Through Mediator ---

[User] 'Alice' sending: "Hello everyone! Anyone working on design patterns?"
[ChatRoom] Mediating message from 'Alice': "Hello everyone! Anyone working on design patterns?"
[ChatRoom] -> Delivering to 'Bob'
[User] 'Bob' received: "Alice: Hello everyone! Anyone working on design patterns?"
[ChatRoom] -> Delivering to 'Charlie'
[User] 'Charlie' received: "Alice: Hello everyone! Anyone working on design patterns?"

[User] 'Bob' sending: "Hi Alice! Yes, I'm implementing the Mediator pattern."
[ChatRoom] Mediating message from 'Bob': "Hi Alice! Yes, I'm implementing the Mediator pattern."
[ChatRoom] -> Delivering to 'Alice'
[User] 'Alice' received: "Bob: Hi Alice! Yes, I'm implementing the Mediator pattern."
[ChatRoom] -> Delivering to 'Charlie'
[User] 'Charlie' received: "Bob: Hi Alice! Yes, I'm implementing the Mediator pattern."

[User] 'Charlie' sending: "Great topic! The Mediator helps reduce coupling."
[ChatRoom] Mediating message from 'Charlie': "Great topic! The Mediator helps reduce coupling."
[ChatRoom] -> Delivering to 'Alice'
[User] 'Alice' received: "Charlie: Great topic! The Mediator helps reduce coupling."
[ChatRoom] -> Delivering to 'Bob'
[User] 'Bob' received: "Charlie: Great topic! The Mediator helps reduce coupling."

[User] 'Alice' sending: "Exactly! Objects don't need direct references to each other."
[ChatRoom] Mediating message from 'Alice': "Exactly! Objects don't need direct references to each other."
[ChatRoom] -> Delivering to 'Bob'
[User] 'Bob' received: "Alice: Exactly! Objects don't need direct references to each other."
[ChatRoom] -> Delivering to 'Charlie'
[User] 'Charlie' received: "Alice: Exactly! Objects don't need direct references to each other."

--- Final Inbox Status ---

[User] 'Alice' inbox (2 messages):
       1. Bob: Hi Alice! Yes, I'm implementing the Mediator pattern.
       2. Charlie: Great topic! The Mediator helps reduce coupling.

[User] 'Bob' inbox (3 messages):
       1. Alice: Hello everyone! Anyone working on design patterns?
       2. Charlie: Great topic! The Mediator helps reduce coupling.
       3. Alice: Exactly! Objects don't need direct references to each other.

[User] 'Charlie' inbox (3 messages):
       1. Alice: Hello everyone! Anyone working on design patterns?
       2. Bob: Hi Alice! Yes, I'm implementing the Mediator pattern.
       3. Alice: Exactly! Objects don't need direct references to each other.

=== Demo Complete ===
```

## Code Annotations

### Key Sections Explained

#### Lines 4-5: Smart Pointer Imports
```rust
use std::cell::RefCell;
use std::rc::Rc;
```
These imports are essential for the Mediator pattern in Rust. `Rc` provides reference counting for shared ownership, while `RefCell` enables interior mutability - allowing mutation through shared references at runtime.

#### Lines 8-11: Mediator Trait Definition
```rust
trait Mediator {
    fn send_message(&self, message: &str, sender_id: usize);
    fn add_user(&mut self, user: Rc<RefCell<User>>);
}
```
Defines the abstract mediator interface. The trait specifies how colleagues register with the mediator and how messages are sent. Using a trait allows for different mediator implementations.

#### Lines 14-17: ChatRoom Structure
```rust
struct ChatRoom {
    name: String,
    users: Vec<Rc<RefCell<User>>>,
}
```
The concrete mediator holds references to all colleague objects (users). Using `Rc<RefCell<User>>` allows multiple owners and mutable access to users.

#### Lines 36-55: Message Mediation Logic
```rust
fn send_message(&self, message: &str, sender_id: usize) {
    // ... find sender, then deliver to others
    for user in &self.users {
        if user_ref.id != sender_id {
            user.borrow_mut().receive(message, &sender_name);
        }
    }
}
```
This is the core mediation logic. The mediator receives a message from one colleague and delivers it to all others. The sender is excluded from receiving their own message.

#### Lines 59-64: User (Colleague) Structure
```rust
struct User {
    id: usize,
    name: String,
    mediator: Option<Rc<RefCell<dyn Mediator>>>,
    messages_received: Vec<String>,
}
```
Users hold an optional reference to their mediator. The `dyn Mediator` trait object allows polymorphic mediator references. `Option` handles the case where a user isn't yet registered.

#### Lines 81-88: Sending Through Mediator
```rust
fn send(&self, message: &str) {
    if let Some(mediator) = &self.mediator {
        mediator.borrow().send_message(message, self.id);
    }
}
```
Users never communicate directly. They always delegate to the mediator, which decides how to route the message.

#### Lines 105-108: Registration Helper
```rust
fn join_chat_room(user: &Rc<RefCell<User>>, chat_room: &Rc<RefCell<ChatRoom>>) {
    user.borrow_mut().set_mediator(chat_room.clone());
    chat_room.borrow_mut().add_user(user.clone());
}
```
Two-way registration: the user gets a reference to the mediator, and the mediator adds the user to its collection.

### Output-to-Source Correlation Table

| Output Line | Source Line | Description |
|-------------|-------------|-------------|
| `[ChatRoom] Creating chat room: 'Rust Developers'` | 21 | ChatRoom constructor logs creation |
| `[User] Creating user: 'Alice' (id: 1)` | 68 | User::new() logs each user creation |
| `[ChatRoom] User 'Alice' joined 'Rust Developers'` | 32 | Mediator logs when colleagues register |
| `[User] 'Alice' sending: "..."` | 82 | User.send() logs outgoing message |
| `[ChatRoom] Mediating message from 'Alice': "..."` | 44 | Mediator receives and announces message |
| `[ChatRoom] -> Delivering to 'Bob'` | 50 | Mediator shows routing decision |
| `[User] 'Bob' received: "Alice: ..."` | 92 | User.receive() logs incoming message |
| `[User] 'Alice' inbox (2 messages):` | 97 | show_inbox() displays message count |
| `       1. Bob: Hi Alice! ...` | 99 | Enumerated inbox contents |

### Key Characteristics of Mediator Pattern in Rust

1. **Interior Mutability with RefCell**: Rust's ownership rules require `RefCell` for runtime borrow checking when multiple components need mutable access through shared references.

2. **Reference Counting with Rc**: `Rc<T>` enables multiple ownership, essential when both the mediator holds references to colleagues and colleagues hold references to the mediator.

3. **Trait Objects for Polymorphism**: Using `dyn Mediator` allows colleagues to work with any mediator implementation, promoting flexibility and adherence to the Open/Closed principle.

4. **Option for Optional References**: `Option<Rc<RefCell<dyn Mediator>>>` elegantly handles the case where a colleague may not yet be registered with a mediator.

5. **Explicit Borrow Management**: Line 51 shows `drop(user_ref)` to release a borrow before acquiring a new mutable borrow - a Rust-specific consideration for avoiding runtime panics.

6. **Decoupled Communication**: Users have no direct references to other users. All communication flows through the ChatRoom mediator, reducing coupling from O(n^2) to O(n).

7. **Centralized Control**: The mediator encapsulates the communication protocol. Changing how messages are routed only requires modifying the ChatRoom, not all users.

### Benefits Demonstrated

- **Loose Coupling**: Alice, Bob, and Charlie never reference each other directly
- **Single Responsibility**: ChatRoom handles all routing logic
- **Easy Extension**: Adding a new user requires no changes to existing users
- **Centralized Logic**: Message filtering, logging, or transformation can be added in one place

### Compile and Run

```bash
rustc main_mediator.rs -o main_mediator && ./main_mediator
```

This code compiles with standard Rust (rustc) and requires no external dependencies.
