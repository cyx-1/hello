# Mediator Pattern

Defines an object that encapsulates how a set of objects interact, promoting loose coupling.

## How to Run
```bash
cd java/mediator
mvn compile exec:java
```

## Key Source Code

### Mediator Interface (Lines 10-13)
```java
interface ChatMediator {
    void sendMessage(String message, User user);
    void addUser(User user);
}
```

### Concrete Mediator (Lines 16-29)
```java
class ChatRoom implements ChatMediator {
    private List<User> users = new ArrayList<>();

    @Override
    public void sendMessage(String message, User sender) {
        for (User user : users) {
            if (user != sender) {
                user.receive(message, sender.getName());
            }
        }
    }
}
```

## Program Output
```
--- 1. Chat Room Mediator ---
  [ChatRoom] Alice joined the chat
  [ChatRoom] Bob joined the chat
  [ChatRoom] Charlie joined the chat

  [Alice] Sending: Hello everyone!
  [Bob] Received from Alice: Hello everyone!
  [Charlie] Received from Alice: Hello everyone!

--- 2. Air Traffic Control Mediator ---
  [AA123] Requesting landing
  [ATC] AA123 cleared for landing
  [UA456] Requesting landing
  [ATC] UA456 please hold, runway busy

--- 3. Smart Home Mediator ---
Coming home (disarming security):
  [Home Security] Security system DISARMED
  [Controller] Welcome home! Adjusting settings...
  [Living Room Light] Light is ON
  [Main Thermostat] Temperature set to 72°F
  [Kitchen Coffee Maker] Starting to brew coffee
```

## Pattern Benefits
- Reduces coupling between colleagues
- Centralizes complex communication logic
- Simplifies object protocols

## Requirements
- Java 17 or higher
- Maven 3.x
