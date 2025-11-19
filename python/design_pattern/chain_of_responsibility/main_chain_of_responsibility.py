# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Chain of Responsibility Pattern

The Chain of Responsibility pattern avoids coupling the sender of a request to
its receiver by giving more than one object a chance to handle the request.
It chains the receiving objects and passes the request along the chain until
an object handles it.

Key Components:
- Handler: Interface for handling requests, optionally has successor link
- ConcreteHandler: Handles requests it's responsible for, forwards others
- Client: Initiates request to a handler in the chain
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


# Request classes
class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


@dataclass
class SupportTicket:
    """A support ticket request."""

    ticket_id: str
    title: str
    description: str
    priority: Priority
    category: str
    customer_tier: str = "standard"  # standard, premium, enterprise


# Handler interface
class SupportHandler(ABC):
    """Abstract handler for support tickets."""

    def __init__(self):
        self._next_handler: SupportHandler | None = None

    def set_next(self, handler: "SupportHandler") -> "SupportHandler":
        """Set the next handler in chain. Returns the handler for chaining."""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, ticket: SupportTicket) -> str | None:
        """Handle the ticket or pass to next handler."""
        pass

    def pass_to_next(self, ticket: SupportTicket) -> str | None:
        """Pass ticket to next handler in chain."""
        if self._next_handler:
            return self._next_handler.handle(ticket)
        return None


# Concrete Handlers
class SpamFilter(SupportHandler):
    """First handler: filters spam tickets."""

    SPAM_KEYWORDS = ["free money", "winner", "lottery", "prince"]

    def handle(self, ticket: SupportTicket) -> str | None:
        text = f"{ticket.title} {ticket.description}".lower()
        if any(keyword in text for keyword in self.SPAM_KEYWORDS):
            return f"[SpamFilter] Ticket {ticket.ticket_id} marked as SPAM and discarded"
        print(f"  [SpamFilter] Ticket {ticket.ticket_id} passed spam check")
        return self.pass_to_next(ticket)


class PriorityEscalation(SupportHandler):
    """Escalates based on customer tier."""

    def handle(self, ticket: SupportTicket) -> str | None:
        original_priority = ticket.priority

        # Escalate priority for premium customers
        if ticket.customer_tier == "enterprise" and ticket.priority != Priority.CRITICAL:
            if ticket.priority == Priority.LOW:
                ticket.priority = Priority.MEDIUM
            elif ticket.priority == Priority.MEDIUM:
                ticket.priority = Priority.HIGH
            elif ticket.priority == Priority.HIGH:
                ticket.priority = Priority.CRITICAL

        if ticket.priority != original_priority:
            print(
                f"  [PriorityEscalation] Ticket {ticket.ticket_id} escalated from "
                f"{original_priority.name} to {ticket.priority.name} (enterprise customer)"
            )
        else:
            print(f"  [PriorityEscalation] Ticket {ticket.ticket_id} priority unchanged")

        return self.pass_to_next(ticket)


class BotHandler(SupportHandler):
    """Handles simple, common questions automatically."""

    FAQ_RESPONSES = {
        "password": "To reset your password, visit /reset-password",
        "pricing": "View our pricing at /pricing",
        "cancel": "To cancel subscription, go to Settings > Subscription",
        "refund": "Refund requests are processed within 5-7 business days",
    }

    def handle(self, ticket: SupportTicket) -> str | None:
        # Only handle low priority tickets
        if ticket.priority == Priority.LOW:
            text = f"{ticket.title} {ticket.description}".lower()
            for keyword, response in self.FAQ_RESPONSES.items():
                if keyword in text:
                    return (
                        f"[BotHandler] Ticket {ticket.ticket_id} auto-resolved:\n"
                        f"  Response: {response}"
                    )

        print(f"  [BotHandler] Ticket {ticket.ticket_id} requires human support")
        return self.pass_to_next(ticket)


class TechnicalSupport(SupportHandler):
    """Handles technical issues."""

    TECHNICAL_CATEGORIES = ["bug", "technical", "error", "api", "integration"]

    def handle(self, ticket: SupportTicket) -> str | None:
        if ticket.category.lower() in self.TECHNICAL_CATEGORIES:
            return (
                f"[TechnicalSupport] Ticket {ticket.ticket_id} assigned to Tech Team\n"
                f"  Category: {ticket.category}\n"
                f"  Priority: {ticket.priority.name}\n"
                f"  ETA: {self._get_eta(ticket.priority)}"
            )

        print(f"  [TechnicalSupport] Ticket {ticket.ticket_id} not technical")
        return self.pass_to_next(ticket)

    def _get_eta(self, priority: Priority) -> str:
        etas = {
            Priority.CRITICAL: "1 hour",
            Priority.HIGH: "4 hours",
            Priority.MEDIUM: "24 hours",
            Priority.LOW: "48 hours",
        }
        return etas[priority]


class BillingSupport(SupportHandler):
    """Handles billing issues."""

    BILLING_CATEGORIES = ["billing", "payment", "invoice", "charge", "refund"]

    def handle(self, ticket: SupportTicket) -> str | None:
        if ticket.category.lower() in self.BILLING_CATEGORIES:
            return (
                f"[BillingSupport] Ticket {ticket.ticket_id} assigned to Billing Team\n"
                f"  Category: {ticket.category}\n"
                f"  Priority: {ticket.priority.name}"
            )

        print(f"  [BillingSupport] Ticket {ticket.ticket_id} not billing related")
        return self.pass_to_next(ticket)


class GeneralSupport(SupportHandler):
    """Handles general inquiries - catch-all handler."""

    def handle(self, ticket: SupportTicket) -> str | None:
        return (
            f"[GeneralSupport] Ticket {ticket.ticket_id} assigned to General Queue\n"
            f"  Category: {ticket.category}\n"
            f"  Priority: {ticket.priority.name}\n"
            f"  Note: Will be triaged by available agent"
        )


class ManagerEscalation(SupportHandler):
    """Handles critical priority by escalating to manager."""

    def handle(self, ticket: SupportTicket) -> str | None:
        if ticket.priority == Priority.CRITICAL:
            return (
                f"[ManagerEscalation] CRITICAL Ticket {ticket.ticket_id} "
                f"escalated to Manager\n"
                f"  Title: {ticket.title}\n"
                f"  Customer Tier: {ticket.customer_tier}\n"
                f"  Action: Immediate attention required"
            )

        print(f"  [ManagerEscalation] Ticket {ticket.ticket_id} not critical")
        return self.pass_to_next(ticket)


def create_support_chain() -> SupportHandler:
    """Create and configure the support handler chain."""
    # Create handlers
    spam_filter = SpamFilter()
    priority_escalation = PriorityEscalation()
    manager_escalation = ManagerEscalation()
    bot_handler = BotHandler()
    technical = TechnicalSupport()
    billing = BillingSupport()
    general = GeneralSupport()

    # Build chain
    spam_filter.set_next(priority_escalation).set_next(manager_escalation).set_next(
        bot_handler
    ).set_next(technical).set_next(billing).set_next(general)

    return spam_filter


def main() -> None:
    print("=" * 60)
    print("Chain of Responsibility - Support Ticket System")
    print("=" * 60)

    # Create the handler chain
    support_chain = create_support_chain()

    # Test tickets
    tickets = [
        SupportTicket(
            "T001",
            "Free Money Winner!",
            "You won the lottery!",
            Priority.LOW,
            "general",
        ),
        SupportTicket(
            "T002",
            "How to reset password?",
            "I forgot my password",
            Priority.LOW,
            "account",
        ),
        SupportTicket(
            "T003",
            "API returning 500 error",
            "Production API failing",
            Priority.HIGH,
            "technical",
            "enterprise",
        ),
        SupportTicket(
            "T004",
            "Double charged",
            "I was charged twice this month",
            Priority.MEDIUM,
            "billing",
        ),
        SupportTicket(
            "T005",
            "Site is completely down",
            "Cannot access anything",
            Priority.CRITICAL,
            "technical",
        ),
        SupportTicket(
            "T006",
            "Feature suggestion",
            "Would be nice to have dark mode",
            Priority.LOW,
            "feedback",
        ),
        SupportTicket(
            "T007",
            "Integration not working",
            "Slack integration broken",
            Priority.MEDIUM,
            "integration",
            "premium",
        ),
    ]

    # Process each ticket
    for ticket in tickets:
        print(f"\n{'─' * 50}")
        print(f"Processing Ticket: {ticket.ticket_id}")
        print(f"Title: {ticket.title}")
        print(f"Priority: {ticket.priority.name}")
        print(f"Category: {ticket.category}")
        print(f"Customer: {ticket.customer_tier}")
        print(f"{'─' * 50}")

        result = support_chain.handle(ticket)
        if result:
            print(f"\nResult:\n{result}")
        else:
            print("\nResult: Ticket not handled by any handler")

    # Demo: Show chain structure
    print("\n" + "=" * 60)
    print("Chain Structure:")
    print("=" * 60)
    print("SpamFilter -> PriorityEscalation -> ManagerEscalation -> ")
    print("BotHandler -> TechnicalSupport -> BillingSupport -> GeneralSupport")

    print("\n" + "=" * 60)
    print("Benefits of Chain of Responsibility:")
    print("=" * 60)
    print("1. Decouples sender from receivers")
    print("2. Adds flexibility in assigning responsibilities")
    print("3. Easy to add/remove handlers dynamically")
    print("4. Each handler has single responsibility")
    print("5. Request can be handled by multiple handlers")


if __name__ == "__main__":
    main()
