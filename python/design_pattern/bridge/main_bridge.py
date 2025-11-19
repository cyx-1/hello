# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Bridge Pattern

The Bridge pattern decouples an abstraction from its implementation so that
the two can vary independently. It separates the abstraction (high-level control)
from the implementation (low-level details).

Key Components:
- Abstraction: High-level control layer
- RefinedAbstraction: Extends the abstraction with more features
- Implementor: Interface for implementation classes
- ConcreteImplementor: Specific implementation
"""

from abc import ABC, abstractmethod


# Implementor interface
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


# Concrete Implementors
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


class PushNotificationSender(MessageSender):
    """Sends messages via push notification."""

    def __init__(self, service: str = "Firebase"):
        self.service = service
        self._last_status = "ready"

    def send(self, title: str, body: str) -> str:
        self._last_status = "pushed"
        return f"Push notification sent via {self.service}\nTitle: {title}\nBody: {body}"

    def get_delivery_status(self) -> str:
        return f"Push status: {self._last_status}"

    def get_platform_name(self) -> str:
        return "Push Notification"


class SlackSender(MessageSender):
    """Sends messages via Slack."""

    def __init__(self, workspace: str = "default"):
        self.workspace = workspace
        self._last_status = "ready"

    def send(self, title: str, body: str) -> str:
        self._last_status = "posted"
        return f"Slack message posted to {self.workspace}\n*{title}*\n{body}"

    def get_delivery_status(self) -> str:
        return f"Slack status: {self._last_status}"

    def get_platform_name(self) -> str:
        return "Slack"


# Abstraction
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


# Refined Abstractions
class SimpleNotification(Notification):
    """Simple notification with basic formatting."""

    def notify(self, message: str) -> str:
        return self._sender.send("Notification", message)


class UrgentNotification(Notification):
    """Urgent notification with priority formatting."""

    def notify(self, message: str) -> str:
        title = "🚨 URGENT"
        body = f"[HIGH PRIORITY]\n{message}\n\nPlease respond immediately!"
        return self._sender.send(title, body)


class ReminderNotification(Notification):
    """Reminder notification with gentle formatting."""

    def __init__(self, sender: MessageSender, reminder_count: int = 1):
        super().__init__(sender)
        self.reminder_count = reminder_count

    def notify(self, message: str) -> str:
        title = f"⏰ Reminder #{self.reminder_count}"
        body = f"This is a friendly reminder:\n{message}"
        return self._sender.send(title, body)

    def increment_reminder(self) -> None:
        self.reminder_count += 1


class ScheduledNotification(Notification):
    """Scheduled notification with timing information."""

    def __init__(self, sender: MessageSender, schedule_time: str):
        super().__init__(sender)
        self.schedule_time = schedule_time

    def notify(self, message: str) -> str:
        title = f"📅 Scheduled Message ({self.schedule_time})"
        body = f"Scheduled delivery time: {self.schedule_time}\n\n{message}"
        return self._sender.send(title, body)


class BatchNotification(Notification):
    """Batch notification that sends to multiple messages at once."""

    def __init__(self, sender: MessageSender):
        super().__init__(sender)
        self._messages: list[str] = []

    def add_message(self, message: str) -> None:
        self._messages.append(message)

    def notify(self, message: str) -> str:
        self._messages.append(message)
        return self._send_batch()

    def _send_batch(self) -> str:
        title = f"📬 Batch Update ({len(self._messages)} items)"
        body = "\n".join(f"• {msg}" for msg in self._messages)
        result = self._sender.send(title, body)
        self._messages.clear()
        return result


def main() -> None:
    print("=" * 60)
    print("Bridge Pattern - Notification System Demo")
    print("=" * 60)

    # Create different senders (implementors)
    email = EmailSender("mail.company.com")
    sms = SMSSender("twilio")
    push = PushNotificationSender("Firebase")
    slack = SlackSender("engineering")

    # Demo 1: Same abstraction with different implementors
    print("\n--- Simple Notification with Different Senders ---")
    for sender in [email, sms, push, slack]:
        notification = SimpleNotification(sender)
        print(f"\n[{notification.get_platform()}]")
        print(notification.notify("Your order has been shipped!"))
        print(notification.get_status())

    # Demo 2: Different abstractions with same implementor
    print("\n\n--- Different Notification Types with Email ---")

    simple = SimpleNotification(EmailSender())
    urgent = UrgentNotification(EmailSender())
    reminder = ReminderNotification(EmailSender(), reminder_count=2)

    print("\n[Simple]")
    print(simple.notify("Meeting at 3pm"))

    print("\n[Urgent]")
    print(urgent.notify("Server is down!"))

    print("\n[Reminder]")
    print(reminder.notify("Submit your timesheet"))

    # Demo 3: Scheduled notification
    print("\n\n--- Scheduled Notification ---")
    scheduled = ScheduledNotification(PushNotificationSender(), "2024-12-01 09:00 AM")
    print(scheduled.notify("Black Friday sale starts now!"))

    # Demo 4: Batch notification
    print("\n\n--- Batch Notification ---")
    batch = BatchNotification(SlackSender("team-updates"))
    batch.add_message("Deployed v2.1.0 to production")
    batch.add_message("Fixed authentication bug")
    print(batch.notify("Updated documentation"))

    # Demo 5: Runtime switching of implementor
    print("\n\n--- Runtime Implementor Switching ---")
    message = "System maintenance scheduled for tonight"

    # Start with email
    notification = SimpleNotification(email)
    print(f"[{notification.get_platform()}]: ", end="")
    print(notification.notify(message).split("\n")[0])

    # Switch to SMS for the same notification type
    notification = SimpleNotification(sms)
    print(f"[{notification.get_platform()}]: ", end="")
    print(notification.notify(message).split("\n")[0])

    print("\n" + "=" * 60)
    print("Benefits of Bridge Pattern:")
    print("=" * 60)
    print("1. Separates abstraction from implementation")
    print("2. Both can evolve independently")
    print("3. Hides implementation details from clients")
    print("4. Can switch implementations at runtime")
    print("5. Follows Single Responsibility Principle")


if __name__ == "__main__":
    main()
