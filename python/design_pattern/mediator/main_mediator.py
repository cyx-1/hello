# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Mediator Pattern

The Mediator pattern defines an object that encapsulates how a set of objects
interact. It promotes loose coupling by keeping objects from referring to each
other explicitly and lets you vary their interaction independently.

Key Components:
- Mediator: Interface for communicating with Colleague objects
- ConcreteMediator: Implements cooperation between Colleagues
- Colleague: Communicates with other Colleagues via Mediator
"""

from abc import ABC, abstractmethod
from datetime import datetime


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

    @abstractmethod
    def receive(self, message: str, sender: "User") -> None:
        """Receive message from another user."""
        pass

    def get_messages(self) -> list[str]:
        return self._messages.copy()


# Concrete Colleagues
class RegularUser(User):
    """Regular chat user."""

    def receive(self, message: str, sender: "User") -> None:
        formatted = f"{sender.name}: {message}"
        self._messages.append(formatted)
        print(f"  [{self._name} received] {formatted}")


class PremiumUser(User):
    """Premium user with special formatting."""

    def receive(self, message: str, sender: "User") -> None:
        formatted = f"★ {sender.name}: {message}"
        self._messages.append(formatted)
        print(f"  [{self._name} received] {formatted}")


class BotUser(User):
    """Bot user that can auto-respond."""

    def __init__(self, name: str, mediator: ChatMediator):
        super().__init__(name, mediator)
        self._auto_responses: dict[str, str] = {
            "help": "Available commands: !help, !time, !users",
            "time": f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        }

    def receive(self, message: str, sender: "User") -> None:
        formatted = f"{sender.name}: {message}"
        self._messages.append(formatted)
        print(f"  [{self._name} received] {formatted}")

        # Auto-respond to commands
        if message.startswith("!"):
            cmd = message[1:].lower()
            if cmd in self._auto_responses:
                self.send(self._auto_responses[cmd])


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

    def send_private_message(self, message: str, sender: User, recipient: User) -> None:
        """Send private message to specific user."""
        self._message_history.append(
            {
                "timestamp": datetime.now(),
                "sender": sender.name,
                "recipient": recipient.name,
                "message": message,
                "type": "private",
            }
        )

        if recipient in self._users:
            recipient.receive(f"(private) {message}", sender)
        else:
            sender.receive(f"User {recipient.name} is not in the chat", BotUser("System", self))

    def get_online_users(self) -> list[str]:
        return [user.name for user in self._users]

    def get_message_count(self) -> int:
        return len(self._message_history)


# Advanced Mediator Example: Air Traffic Control
class Aircraft:
    """Colleague: An aircraft communicating via ATC."""

    def __init__(self, call_sign: str, atc: "AirTrafficControl"):
        self.call_sign = call_sign
        self._atc = atc
        self._altitude = 0
        self._runway: str | None = None

    def request_landing(self) -> None:
        print(f"{self.call_sign}: Requesting permission to land")
        self._atc.request_landing(self)

    def request_takeoff(self) -> None:
        print(f"{self.call_sign}: Requesting permission for takeoff")
        self._atc.request_takeoff(self)

    def receive_clearance(self, message: str) -> None:
        print(f"{self.call_sign}: Received - {message}")

    def land(self, runway: str) -> None:
        self._runway = runway
        self._altitude = 0
        print(f"{self.call_sign}: Landing on runway {runway}")

    def takeoff(self, runway: str) -> None:
        self._runway = None
        self._altitude = 1000
        print(f"{self.call_sign}: Taking off from runway {runway}")


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


def main() -> None:
    print("=" * 60)
    print("Mediator Pattern - Chat Room Demo")
    print("=" * 60)

    # Demo 1: Basic chat room
    print("\n--- Chat Room Demo ---")
    chat_room = ChatRoom("General")

    # Create users
    alice = RegularUser("Alice", chat_room)
    bob = RegularUser("Bob", chat_room)
    charlie = PremiumUser("Charlie", chat_room)
    helper_bot = BotUser("HelperBot", chat_room)

    # Users join
    chat_room.add_user(alice)
    chat_room.add_user(bob)
    chat_room.add_user(charlie)
    chat_room.add_user(helper_bot)

    print("\n--- Messages ---")
    # Send messages
    alice.send("Hello everyone!")
    bob.send("Hi Alice!")
    charlie.send("How's it going?")

    # Private message
    print("\n--- Private Message ---")
    alice.send_private("Can we talk later?", bob)

    # Bot interaction
    print("\n--- Bot Interaction ---")
    bob.send("!help")

    # User leaves
    print("\n--- User Leaving ---")
    chat_room.remove_user(charlie)

    print(f"\nOnline users: {chat_room.get_online_users()}")
    print(f"Total messages: {chat_room.get_message_count()}")

    # Demo 2: Air Traffic Control
    print("\n" + "=" * 60)
    print("Mediator Pattern - Air Traffic Control Demo")
    print("=" * 60)

    atc = AirTrafficControl()

    # Create aircraft
    flight1 = Aircraft("UA123", atc)
    flight2 = Aircraft("AA456", atc)
    flight3 = Aircraft("DL789", atc)
    flight4 = Aircraft("SW101", atc)
    flight5 = Aircraft("JB202", atc)

    print("\n--- Landing Requests ---")
    flight1.request_landing()
    flight2.request_landing()
    flight3.request_landing()
    flight4.request_landing()
    flight5.request_landing()  # This one should queue

    print(f"\nRunway status: {atc.get_status()}")

    print("\n--- Takeoff Request ---")
    flight1.request_takeoff()  # This frees up a runway

    print(f"\nRunway status: {atc.get_status()}")

    print("\n" + "=" * 60)
    print("Benefits of Mediator Pattern:")
    print("=" * 60)
    print("1. Decouples colleagues from each other")
    print("2. Centralizes control logic")
    print("3. Simplifies object protocols")
    print("4. Easy to change interaction independently")
    print("5. Reduces subclassing")


if __name__ == "__main__":
    main()
