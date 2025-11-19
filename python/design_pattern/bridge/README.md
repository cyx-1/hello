# Bridge Pattern

The Bridge pattern decouples an abstraction from its implementation so that the two can vary independently. It separates the abstraction (high-level control) from the implementation (low-level details).

**Requires: Python 3.10+** (uses union types with `|` syntax)

## Key Components

- **Abstraction**: High-level control layer (`Notification`)
- **RefinedAbstraction**: Extends the abstraction with more features (`UrgentNotification`, `ReminderNotification`)
- **Implementor**: Interface for implementation classes (`MessageSender`)
- **ConcreteImplementor**: Specific implementation (`EmailSender`, `SMSSender`, `SlackSender`)

## Source Code

### Implementor Interface (Lines 23-36)

```python:main_bridge.py startLine=23 endLine=36
class MessageSender(ABC):
    """Implementation interface for sending messages."""

    @abstractmethod
    def send(self, title: str, body: str) -> str:
        pass

    @abstractmethod
    def get_delivery_status(self) -> str:
        pass

    @abstractmethod
    def get_platform_name(self) -> str:
        pass
```

### Concrete Implementors (Lines 40-111)

```python:main_bridge.py startLine=40 endLine=75
class EmailSender(MessageSender):
    """Sends messages via email."""

    def __init__(self, smtp_server: str = "smtp.example.com"):
        self.smtp_server = smtp_server
        self._last_status = "ready"

    def send(self, title: str, body: str) -> str:
        self._last_status = "sent"
        return f"Email sent via {self.smtp_server}\nSubject: {title}\nBody: {body}"

    def get_delivery_status(self) -> str:
        return f"Email status: {self._last_status}"

    def get_platform_name(self) -> str:
        return "Email"


class SMSSender(MessageSender):
    """Sends messages via SMS."""

    def __init__(self, gateway: str = "twilio"):
        self.gateway = gateway
        self._last_status = "ready"

    def send(self, title: str, body: str) -> str:
        self._last_status = "delivered"
        # SMS typically has limited space, so we truncate
        message = f"{title}: {body}"[:160]
        return f"SMS sent via {self.gateway} gateway\nMessage: {message}"

    def get_delivery_status(self) -> str:
        return f"SMS status: {self._last_status}"

    def get_platform_name(self) -> str:
        return "SMS"
```

### Abstraction (Lines 115-129)

```python:main_bridge.py startLine=115 endLine=129
class Notification(ABC):
    """Abstraction for notifications."""

    def __init__(self, sender: MessageSender):
        self._sender = sender

    @abstractmethod
    def notify(self, message: str) -> str:
        pass

    def get_status(self) -> str:
        return self._sender.get_delivery_status()

    def get_platform(self) -> str:
        return self._sender.get_platform_name()
```

### Refined Abstractions (Lines 133-197)

```python:main_bridge.py startLine=133 endLine=163
class SimpleNotification(Notification):
    """Simple notification with basic formatting."""

    def notify(self, message: str) -> str:
        return self._sender.send("Notification", message)


class UrgentNotification(Notification):
    """Urgent notification with priority formatting."""

    def notify(self, message: str) -> str:
        title = "URGENT"
        body = f"[HIGH PRIORITY]\n{message}\n\nPlease respond immediately!"
        return self._sender.send(title, body)


class ReminderNotification(Notification):
    """Reminder notification with gentle formatting."""

    def __init__(self, sender: MessageSender, reminder_count: int = 1):
        super().__init__(sender)
        self.reminder_count = reminder_count

    def notify(self, message: str) -> str:
        title = f"Reminder #{self.reminder_count}"
        body = f"This is a friendly reminder:\n{message}"
        return self._sender.send(title, body)

    def increment_reminder(self) -> None:
        self.reminder_count += 1
```

## Program Output

```
============================================================
Bridge Pattern - Notification System Demo
============================================================

--- Simple Notification with Different Senders ---

[Email]
Email sent via mail.company.com
Subject: Notification
Body: Your order has been shipped!
Email status: sent

[SMS]
SMS sent via twilio gateway
Message: Notification: Your order has been shipped!
SMS status: delivered

[Push Notification]
Push notification sent via Firebase
Title: Notification
Body: Your order has been shipped!
Push status: pushed

[Slack]
Slack message posted to engineering
*Notification*
Your order has been shipped!
Slack status: posted


--- Different Notification Types with Email ---

[Simple]
Email sent via smtp.example.com
Subject: Notification
Body: Meeting at 3pm

[Urgent]
Email sent via smtp.example.com
Subject: URGENT
Body: [HIGH PRIORITY]
Server is down!

Please respond immediately!

[Reminder]
Email sent via smtp.example.com
Subject: Reminder #2
Body: This is a friendly reminder:
Submit your timesheet


--- Scheduled Notification ---
Push notification sent via Firebase
Title: Scheduled Message (2024-12-01 09:00 AM)
Body: Scheduled delivery time: 2024-12-01 09:00 AM

Black Friday sale starts now!


--- Batch Notification ---
Slack message posted to team-updates
*Batch Update (3 items)*
- Deployed v2.1.0 to production
- Fixed authentication bug
- Updated documentation


--- Runtime Implementor Switching ---
[Email]: Email sent via mail.company.com
[SMS]: SMS sent via twilio gateway

============================================================
Benefits of Bridge Pattern:
============================================================
1. Separates abstraction from implementation
2. Both can evolve independently
3. Hides implementation details from clients
4. Can switch implementations at runtime
5. Follows Single Responsibility Principle
```

## Annotations

### How It Works

1. **Implementor Interface (Lines 23-36)**: The `MessageSender` abstract class defines the low-level operations: `send()`, `get_delivery_status()`, and `get_platform_name()`.

2. **Concrete Implementors (Lines 40-111)**: Four different message sending platforms implement the interface:
   - `EmailSender` formats output with Subject/Body
   - `SMSSender` truncates to 160 characters
   - `PushNotificationSender` formats with Title/Body
   - `SlackSender` uses Slack markdown formatting

3. **Abstraction (Lines 115-129)**: The `Notification` class holds a reference to a `MessageSender` and delegates the actual sending. The abstraction focuses on *what* to send, not *how* to send it.

4. **Refined Abstractions (Lines 133-197)**: Different notification types add their own formatting logic:
   - `SimpleNotification` - basic "Notification" title
   - `UrgentNotification` - adds "[HIGH PRIORITY]" and urgency markers
   - `ReminderNotification` - includes reminder count
   - `BatchNotification` - aggregates multiple messages

### Output Analysis

**Same Abstraction, Different Implementors (Lines 211-217)**:
The output shows a `SimpleNotification` sent via four different platforms. Each platform formats the message differently (Email uses Subject/Body, SMS concatenates with truncation, Slack uses markdown), but the abstraction code remains the same.

**Different Abstractions, Same Implementor (Lines 219-233)**:
Three notification types all use `EmailSender`, but produce different formatted messages. The `UrgentNotification` adds priority markers while `ReminderNotification` adds the reminder count.

**Runtime Switching (Lines 247-259)**:
The same message is sent first via email, then via SMS, demonstrating that implementors can be switched at runtime without changing the abstraction.

### Key Insight

The Bridge pattern creates a two-dimensional matrix: notification types (abstractions) x delivery platforms (implementations). Without the Bridge, you would need separate classes for EmailUrgentNotification, SMSUrgentNotification, SlackUrgentNotification, etc. With the Bridge, you can freely combine any notification type with any sender, resulting in m + n classes instead of m * n.
