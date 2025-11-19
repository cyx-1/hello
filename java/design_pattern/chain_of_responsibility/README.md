# Chain of Responsibility Pattern

Passes requests along a chain of handlers, where each handler can process or pass the request to the next handler.

## How to Run
```bash
cd java/chain_of_responsibility
mvn compile exec:java
```

## Key Source Code

### Handler Interface (Lines 8-32)
```java
abstract class SupportHandler {
    protected SupportHandler nextHandler;

    public SupportHandler setNext(SupportHandler handler) {
        this.nextHandler = handler;
        return handler;
    }

    public void handle(SupportTicket ticket) {
        if (canHandle(ticket)) {
            processTicket(ticket);
        } else if (nextHandler != null) {
            nextHandler.handle(ticket);
        }
    }

    protected abstract boolean canHandle(SupportTicket ticket);
    protected abstract void processTicket(SupportTicket ticket);
}
```

## Program Output
```
--- 1. Customer Support Chain ---
Ticket 1: General inquiry (LOW)
  [Front Desk] Handling general inquiry: How do I reset password?

Ticket 2: Technical issue (MEDIUM)
  [Front Desk] Passing to next handler...
  [Technical Support] Resolving technical issue: Application crashes on startup

Ticket 4: Critical issue (CRITICAL)
  [Front Desk] Passing to next handler...
  [Technical Support] Passing to next handler...
  [Billing Department] Passing to next handler...
  [Manager] Escalated issue handled: System completely down
```

## Pattern Benefits
- Decouples sender from receiver
- Chain can be modified dynamically
- Each handler has single responsibility

## Requirements
- Java 17 or higher
- Maven 3.x
