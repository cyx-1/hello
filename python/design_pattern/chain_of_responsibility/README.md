# Chain of Responsibility Pattern

The Chain of Responsibility pattern avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. It chains the receiving objects and passes the request along the chain until an object handles it.

**Requires Python 3.10+** (uses union types with `|` syntax)

## Key Source Code

### Handler Interface and Chain Setup

```python:main_chain_of_responsibility.py startLine=44 endLine=66
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
```

### Concrete Handler Example (SpamFilter)

```python:main_chain_of_responsibility.py startLine=69 endLine=79
class SpamFilter(SupportHandler):
    """First handler: filters spam tickets."""

    SPAM_KEYWORDS = ["free money", "winner", "lottery", "prince"]

    def handle(self, ticket: SupportTicket) -> str | None:
        text = f"{ticket.title} {ticket.description}".lower()
        if any(keyword in text for keyword in self.SPAM_KEYWORDS):
            return f"[SpamFilter] Ticket {ticket.ticket_id} marked as SPAM and discarded"
        print(f"  [SpamFilter] Ticket {ticket.ticket_id} passed spam check")
        return self.pass_to_next(ticket)
```

### Building the Chain

```python:main_chain_of_responsibility.py startLine=206 endLine=222
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
```

## Program Output

```
============================================================
Chain of Responsibility - Support Ticket System
============================================================

──────────────────────────────────────────────────
Processing Ticket: T001
Title: Free Money Winner!
Priority: LOW
Category: general
Customer: standard
──────────────────────────────────────────────────

Result:
[SpamFilter] Ticket T001 marked as SPAM and discarded

──────────────────────────────────────────────────
Processing Ticket: T002
Title: How to reset password?
Priority: LOW
Category: account
Customer: standard
──────────────────────────────────────────────────
  [SpamFilter] Ticket T002 passed spam check
  [PriorityEscalation] Ticket T002 priority unchanged
  [ManagerEscalation] Ticket T002 not critical

Result:
[BotHandler] Ticket T002 auto-resolved:
  Response: To reset your password, visit /reset-password

──────────────────────────────────────────────────
Processing Ticket: T003
Title: API returning 500 error
Priority: HIGH
Category: technical
Customer: enterprise
──────────────────────────────────────────────────
  [SpamFilter] Ticket T003 passed spam check
  [PriorityEscalation] Ticket T003 escalated from HIGH to CRITICAL (enterprise customer)

Result:
[ManagerEscalation] CRITICAL Ticket T003 escalated to Manager
  Title: API returning 500 error
  Customer Tier: enterprise
  Action: Immediate attention required

──────────────────────────────────────────────────
Processing Ticket: T004
Title: Double charged
Priority: MEDIUM
Category: billing
Customer: standard
──────────────────────────────────────────────────
  [SpamFilter] Ticket T004 passed spam check
  [PriorityEscalation] Ticket T004 priority unchanged
  [ManagerEscalation] Ticket T004 not critical
  [BotHandler] Ticket T004 requires human support
  [TechnicalSupport] Ticket T004 not technical

Result:
[BillingSupport] Ticket T004 assigned to Billing Team
  Category: billing
  Priority: MEDIUM

──────────────────────────────────────────────────
Processing Ticket: T005
Title: Site is completely down
Priority: CRITICAL
Category: technical
Customer: standard
──────────────────────────────────────────────────
  [SpamFilter] Ticket T005 passed spam check
  [PriorityEscalation] Ticket T005 priority unchanged

Result:
[ManagerEscalation] CRITICAL Ticket T005 escalated to Manager
  Title: Site is completely down
  Customer Tier: standard
  Action: Immediate attention required

──────────────────────────────────────────────────
Processing Ticket: T006
Title: Feature suggestion
Priority: LOW
Category: feedback
Customer: standard
──────────────────────────────────────────────────
  [SpamFilter] Ticket T006 passed spam check
  [PriorityEscalation] Ticket T006 priority unchanged
  [ManagerEscalation] Ticket T006 not critical
  [BotHandler] Ticket T006 requires human support
  [TechnicalSupport] Ticket T006 not technical
  [BillingSupport] Ticket T006 not billing related

Result:
[GeneralSupport] Ticket T006 assigned to General Queue
  Category: feedback
  Priority: LOW
  Note: Will be triaged by available agent

──────────────────────────────────────────────────
Processing Ticket: T007
Title: Integration not working
Priority: MEDIUM
Category: integration
Customer: premium
──────────────────────────────────────────────────
  [SpamFilter] Ticket T007 passed spam check
  [PriorityEscalation] Ticket T007 priority unchanged
  [ManagerEscalation] Ticket T007 not critical
  [BotHandler] Ticket T007 requires human support

Result:
[TechnicalSupport] Ticket T007 assigned to Tech Team
  Category: integration
  Priority: MEDIUM
  ETA: 24 hours

============================================================
Chain Structure:
============================================================
SpamFilter -> PriorityEscalation -> ManagerEscalation ->
BotHandler -> TechnicalSupport -> BillingSupport -> GeneralSupport

============================================================
Benefits of Chain of Responsibility:
============================================================
1. Decouples sender from receivers
2. Adds flexibility in assigning responsibilities
3. Easy to add/remove handlers dynamically
4. Each handler has single responsibility
5. Request can be handled by multiple handlers
```

## Output Analysis

### T001: Spam Detection (Lines 69-79)
- Ticket contains "Free Money" and "Winner" which match spam keywords
- `SpamFilter.handle()` at line 76 detects spam and returns immediately
- Chain terminates at first handler - no further processing

### T002: Bot Auto-Resolution (Lines 108-130)
- Passes SpamFilter (line 78 prints pass message)
- PriorityEscalation doesn't escalate (standard customer)
- ManagerEscalation passes (not critical)
- BotHandler at line 120-127 matches "password" keyword and auto-resolves

### T003: Enterprise Escalation (Lines 82-105, 189-203)
- Passes SpamFilter
- PriorityEscalation at lines 89-95 escalates HIGH to CRITICAL for enterprise customer
- ManagerEscalation at lines 192-200 catches CRITICAL priority and escalates to manager
- Chain terminates before reaching TechnicalSupport

### T004: Billing Assignment (Lines 160-174)
- Traverses SpamFilter, PriorityEscalation, ManagerEscalation, BotHandler, TechnicalSupport
- Each prints pass message showing chain traversal
- BillingSupport at lines 165-171 matches "billing" category

### T005: Critical Technical Issue
- Already CRITICAL priority, so ManagerEscalation catches it
- Demonstrates that critical issues always get manager attention

### T006: Catch-All Handler (Lines 177-186)
- Traverses entire chain without any handler claiming it
- GeneralSupport at line 180-186 acts as catch-all
- Shows complete chain traversal in print output

### T007: Technical Support Assignment (Lines 133-157)
- Passes through until TechnicalSupport matches "integration" category
- Demonstrates partial chain traversal

## Usage

```bash
uv run python main_chain_of_responsibility.py
```
