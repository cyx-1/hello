# Mediator Pattern

The Mediator pattern defines an object that encapsulates how a set of objects interact. It promotes loose coupling by keeping objects from referring to each other explicitly and lets you vary their interaction independently.

**Key Components:**
- **Mediator**: Interface for communicating with Colleague objects
- **ConcreteMediator**: Implements cooperation between Colleagues
- **Colleague**: Communicates with other Colleagues via Mediator

**Requires**: Python 3.10+ (uses union types with `|` syntax)

## Key Source Code

### Mediator Interface

```python:main_mediator.py startLine=22 endLine=42
# Mediator interface
class ChatMediator(ABC):
    """Abstract mediator for chat room."""

    @abstractmethod
    def send_message(self, message: str, sender: "User") -> None:
        pass

    @abstractmethod
    def send_private_message(
        self, message: str, sender: "User", recipient: "User"
    ) -> None:
        pass

    @abstractmethod
    def add_user(self, user: "User") -> None:
        pass

    @abstractmethod
    def remove_user(self, user: "User") -> None:
        pass
```

### Colleague Base Class

```python:main_mediator.py startLine=45 endLine=68
# Colleague base class
class User(ABC):
    """Abstract colleague representing a chat user."""

    def __init__(self, name: str, mediator: ChatMediator):
        self._name = name
        self._mediator = mediator
        self._messages: list[str] = []

    @property
    def name(self) -> str:
        return self._name

    def send(self, message: str) -> None:
        """Send message to all users via mediator."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {self._name} sends: {message}")
        self._mediator.send_message(message, self)

    def send_private(self, message: str, recipient: "User") -> None:
        """Send private message via mediator."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {self._name} -> {recipient.name} (private): {message}")
        self._mediator.send_private_message(message, self, recipient)
```

### Concrete Mediator - ChatRoom

```python:main_mediator.py startLine=120 endLine=158
# Concrete Mediator
class ChatRoom(ChatMediator):
    """Concrete mediator implementing chat room."""

    def __init__(self, name: str):
        self._name = name
        self._users: list[User] = []
        self._message_history: list[dict] = []

    def add_user(self, user: User) -> None:
        self._users.append(user)
        print(f">>> {user.name} joined {self._name}")
        # Notify other users
        for u in self._users:
            if u != user:
                u.receive(f"{user.name} has joined the chat", BotUser("System", self))

    def remove_user(self, user: User) -> None:
        if user in self._users:
            self._users.remove(user)
            print(f"<<< {user.name} left {self._name}")
            # Notify other users
            for u in self._users:
                u.receive(f"{user.name} has left the chat", BotUser("System", self))

    def send_message(self, message: str, sender: User) -> None:
        """Broadcast message to all users except sender."""
        self._message_history.append(
            {
                "timestamp": datetime.now(),
                "sender": sender.name,
                "message": message,
                "type": "broadcast",
            }
        )

        for user in self._users:
            if user != sender:
                user.receive(message, sender)
```

### Air Traffic Control Mediator

```python:main_mediator.py startLine=216 endLine=267
class AirTrafficControl:
    """Mediator: Coordinates aircraft movements."""

    def __init__(self):
        self._runways: dict[str, Aircraft | None] = {
            "27L": None,
            "27R": None,
            "09L": None,
            "09R": None,
        }
        self._landing_queue: list[Aircraft] = []
        self._takeoff_queue: list[Aircraft] = []

    def request_landing(self, aircraft: Aircraft) -> None:
        # Find available runway
        for runway, occupant in self._runways.items():
            if occupant is None:
                self._runways[runway] = aircraft
                aircraft.receive_clearance(f"Cleared to land on runway {runway}")
                aircraft.land(runway)
                return

        # No runway available, add to queue
        self._landing_queue.append(aircraft)
        position = len(self._landing_queue)
        aircraft.receive_clearance(f"Hold position, #{position} in landing queue")

    def request_takeoff(self, aircraft: Aircraft) -> None:
        # Find runway where aircraft is located
        for runway, occupant in self._runways.items():
            if occupant == aircraft:
                aircraft.receive_clearance(f"Cleared for takeoff on runway {runway}")
                aircraft.takeoff(runway)
                self._runways[runway] = None
                self._process_queue()
                return

        # Aircraft not on runway
        self._takeoff_queue.append(aircraft)
        aircraft.receive_clearance("Taxi to runway and hold")

    def _process_queue(self) -> None:
        """Process waiting aircraft when runway becomes available."""
        if self._landing_queue:
            next_aircraft = self._landing_queue.pop(0)
            self.request_landing(next_aircraft)

    def get_status(self) -> dict[str, str | None]:
        return {
            runway: (aircraft.call_sign if aircraft else "Empty")
            for runway, aircraft in self._runways.items()
        }
```

## Program Output

```
============================================================
Mediator Pattern - Chat Room Demo
============================================================

--- Chat Room Demo ---
>>> Alice joined General
>>> Bob joined General
  [Alice received] System: Bob has joined the chat
>>> Charlie joined General
  [Alice received] System: Charlie has joined the chat
  [Bob received] System: Charlie has joined the chat
>>> HelperBot joined General
  [Alice received] System: HelperBot has joined the chat
  [Bob received] System: HelperBot has joined the chat
  [Charlie received] ★ System: HelperBot has joined the chat

--- Messages ---
[23:52:11] Alice sends: Hello everyone!
  [Bob received] Alice: Hello everyone!
  [Charlie received] ★ Alice: Hello everyone!
  [HelperBot received] Alice: Hello everyone!
[23:52:11] Bob sends: Hi Alice!
  [Alice received] Bob: Hi Alice!
  [Charlie received] ★ Bob: Hi Alice!
  [HelperBot received] Bob: Hi Alice!
[23:52:11] Charlie sends: How's it going?
  [Alice received] Charlie: How's it going?
  [Bob received] Charlie: How's it going?
  [HelperBot received] Charlie: How's it going?

--- Private Message ---
[23:52:11] Alice -> Bob (private): Can we talk later?
  [Bob received] Alice: (private) Can we talk later?

--- Bot Interaction ---
[23:52:11] Bob sends: !help
  [Alice received] Bob: !help
  [Charlie received] ★ Bob: !help
  [HelperBot received] Bob: !help
[23:52:11] HelperBot sends: Available commands: !help, !time, !users
  [Alice received] HelperBot: Available commands: !help, !time, !users
  [Bob received] HelperBot: Available commands: !help, !time, !users
  [Charlie received] ★ HelperBot: Available commands: !help, !time, !users

--- User Leaving ---
<<< Charlie left General
  [Alice received] System: Charlie has left the chat
  [Bob received] System: Charlie has left the chat
  [HelperBot received] System: Charlie has left the chat

Online users: ['Alice', 'Bob', 'HelperBot']
Total messages: 6

============================================================
Mediator Pattern - Air Traffic Control Demo
============================================================

--- Landing Requests ---
UA123: Requesting permission to land
UA123: Received - Cleared to land on runway 27L
UA123: Landing on runway 27L
AA456: Requesting permission to land
AA456: Received - Cleared to land on runway 27R
AA456: Landing on runway 27R
DL789: Requesting permission to land
DL789: Received - Cleared to land on runway 09L
DL789: Landing on runway 09L
SW101: Requesting permission to land
SW101: Received - Cleared to land on runway 09R
SW101: Landing on runway 09R
JB202: Requesting permission to land
JB202: Received - Hold position, #1 in landing queue

Runway status: {'27L': 'UA123', '27R': 'AA456', '09L': 'DL789', '09R': 'SW101'}

--- Takeoff Request ---
UA123: Requesting permission for takeoff
UA123: Received - Cleared for takeoff on runway 27L
UA123: Taking off from runway 27L
JB202: Received - Cleared to land on runway 27L
JB202: Landing on runway 27L

Runway status: {'27L': 'JB202', '27R': 'AA456', '09L': 'DL789', '09R': 'SW101'}

============================================================
Benefits of Mediator Pattern:
============================================================
1. Decouples colleagues from each other
2. Centralizes control logic
3. Simplifies object protocols
4. Easy to change interaction independently
5. Reduces subclassing
```

## Output Annotations

### Chat Room Demo

- **Lines 129-135**: When `add_user()` is called (line 129), the ChatRoom mediator prints the join message and notifies all existing users. Notice that Alice receives notifications about Bob, Charlie, and HelperBot joining because she was added first.

- **Lines 58-62**: When Alice calls `send()`, the method prints the timestamped message and delegates to the mediator's `send_message()`. The mediator then broadcasts to all other users (lines 156-158), which is why Bob, Charlie, and HelperBot all receive Alice's message.

- **Lines 83-86 (RegularUser) vs 92-95 (PremiumUser)**: Charlie's messages show the star prefix because PremiumUser formats messages differently in its `receive()` method.

- **Lines 64-68**: Private messages use `send_private()` which calls the mediator's `send_private_message()` (lines 160-175). Only Bob receives Alice's private message.

- **Lines 108-117 (BotUser)**: The BotUser auto-responds to commands. When Bob sends "!help", the bot's `receive()` detects the command prefix and calls `send()` with the response.

### Air Traffic Control Demo

- **Lines 229-241**: When aircraft request landing, the ATC mediator finds available runways. UA123-SW101 get cleared immediately (4 runways available). JB202 is queued because all runways are occupied.

- **Lines 243-255**: When UA123 requests takeoff (line 336), the ATC clears it and calls `_process_queue()` (lines 257-261), which automatically processes JB202's waiting request, assigning it the freed runway 27L.

- **Line 220**: Uses Python 3.10+ union type syntax `Aircraft | None` for runway occupancy tracking.

## Running the Demo

```bash
uv run python main_mediator.py
```
