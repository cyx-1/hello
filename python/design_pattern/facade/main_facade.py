# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Facade Pattern

The Facade pattern provides a unified interface to a set of interfaces in a
subsystem. It defines a higher-level interface that makes the subsystem easier
to use.

Key Components:
- Facade: Provides simple interface to complex subsystem
- Subsystem classes: Implement subsystem functionality
- Client: Uses Facade instead of subsystem directly
"""


# Subsystem classes for a home theater system
class Amplifier:
    """Audio amplifier subsystem."""

    def __init__(self, description: str):
        self.description = description
        self._volume = 0
        self._source = ""

    def on(self) -> str:
        return f"{self.description} is ON"

    def off(self) -> str:
        return f"{self.description} is OFF"

    def set_source(self, source: str) -> str:
        self._source = source
        return f"{self.description} source set to {source}"

    def set_volume(self, level: int) -> str:
        self._volume = level
        return f"{self.description} volume set to {level}"

    def set_surround_sound(self) -> str:
        return f"{self.description} surround sound ON"


class DvdPlayer:
    """DVD player subsystem."""

    def __init__(self, description: str):
        self.description = description
        self._movie = ""

    def on(self) -> str:
        return f"{self.description} is ON"

    def off(self) -> str:
        return f"{self.description} is OFF"

    def play(self, movie: str) -> str:
        self._movie = movie
        return f"{self.description} playing '{movie}'"

    def pause(self) -> str:
        return f"{self.description} paused '{self._movie}'"

    def stop(self) -> str:
        return f"{self.description} stopped '{self._movie}'"

    def eject(self) -> str:
        return f"{self.description} DVD ejected"


class StreamingPlayer:
    """Streaming player subsystem."""

    def __init__(self, description: str):
        self.description = description
        self._show = ""

    def on(self) -> str:
        return f"{self.description} is ON"

    def off(self) -> str:
        return f"{self.description} is OFF"

    def play(self, show: str) -> str:
        self._show = show
        return f"{self.description} streaming '{show}'"

    def stop(self) -> str:
        return f"{self.description} stopped streaming"


class Projector:
    """Projector subsystem."""

    def __init__(self, description: str):
        self.description = description

    def on(self) -> str:
        return f"{self.description} is ON"

    def off(self) -> str:
        return f"{self.description} is OFF"

    def wide_screen_mode(self) -> str:
        return f"{self.description} in widescreen mode (16:9)"

    def tv_mode(self) -> str:
        return f"{self.description} in TV mode (4:3)"


class Screen:
    """Projection screen subsystem."""

    def __init__(self, description: str):
        self.description = description

    def down(self) -> str:
        return f"{self.description} going down"

    def up(self) -> str:
        return f"{self.description} going up"


class TheaterLights:
    """Theater lighting subsystem."""

    def __init__(self, description: str):
        self.description = description
        self._level = 100

    def on(self) -> str:
        return f"{self.description} are ON"

    def off(self) -> str:
        return f"{self.description} are OFF"

    def dim(self, level: int) -> str:
        self._level = level
        return f"{self.description} dimmed to {level}%"


class PopcornPopper:
    """Popcorn maker subsystem."""

    def __init__(self, description: str):
        self.description = description

    def on(self) -> str:
        return f"{self.description} is ON"

    def off(self) -> str:
        return f"{self.description} is OFF"

    def pop(self) -> str:
        return f"{self.description} popping popcorn!"


# Facade
class HomeTheaterFacade:
    """Facade providing simple interface to home theater subsystem."""

    def __init__(
        self,
        amp: Amplifier,
        dvd: DvdPlayer,
        streaming: StreamingPlayer,
        projector: Projector,
        screen: Screen,
        lights: TheaterLights,
        popper: PopcornPopper,
    ):
        self.amp = amp
        self.dvd = dvd
        self.streaming = streaming
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watch_movie(self, movie: str) -> list[str]:
        """Simple operation to watch a DVD movie."""
        actions = [
            "Get ready to watch a movie...",
            self.popper.on(),
            self.popper.pop(),
            self.lights.dim(10),
            self.screen.down(),
            self.projector.on(),
            self.projector.wide_screen_mode(),
            self.amp.on(),
            self.amp.set_source("DVD"),
            self.amp.set_surround_sound(),
            self.amp.set_volume(5),
            self.dvd.on(),
            self.dvd.play(movie),
        ]
        return actions

    def end_movie(self) -> list[str]:
        """Simple operation to end movie watching."""
        actions = [
            "Shutting movie theater down...",
            self.popper.off(),
            self.lights.on(),
            self.screen.up(),
            self.projector.off(),
            self.amp.off(),
            self.dvd.stop(),
            self.dvd.eject(),
            self.dvd.off(),
        ]
        return actions

    def stream_show(self, show: str) -> list[str]:
        """Simple operation to stream a show."""
        actions = [
            "Get ready to stream a show...",
            self.lights.dim(20),
            self.projector.on(),
            self.projector.tv_mode(),
            self.amp.on(),
            self.amp.set_source("Streaming"),
            self.amp.set_volume(4),
            self.streaming.on(),
            self.streaming.play(show),
        ]
        return actions

    def end_streaming(self) -> list[str]:
        """Simple operation to end streaming."""
        actions = [
            "Shutting down streaming...",
            self.streaming.stop(),
            self.streaming.off(),
            self.amp.off(),
            self.projector.off(),
            self.lights.on(),
        ]
        return actions

    def listen_to_music(self, source: str = "Bluetooth") -> list[str]:
        """Simple operation to listen to music."""
        actions = [
            "Setting up for music...",
            self.lights.dim(50),
            self.amp.on(),
            self.amp.set_source(source),
            self.amp.set_volume(6),
        ]
        return actions

    def end_music(self) -> list[str]:
        """Simple operation to stop music."""
        actions = [
            "Shutting down music...",
            self.amp.off(),
            self.lights.on(),
        ]
        return actions


# Additional facade example: Computer startup
class CPU:
    def freeze(self) -> str:
        return "CPU: Freezing processor"

    def jump(self, address: str) -> str:
        return f"CPU: Jumping to {address}"

    def execute(self) -> str:
        return "CPU: Executing instructions"


class Memory:
    def load(self, address: str, data: str) -> str:
        return f"Memory: Loading '{data}' at {address}"


class HardDrive:
    def read(self, sector: int, size: int) -> str:
        return f"HardDrive: Reading {size} bytes from sector {sector}"


class ComputerFacade:
    """Facade for computer startup."""

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self) -> list[str]:
        """Simple start operation."""
        return [
            "Starting computer...",
            self.cpu.freeze(),
            self.memory.load("0x00", "BIOS"),
            self.cpu.jump("0x00"),
            self.hard_drive.read(0, 1024),
            self.memory.load("0x0A", "Boot loader"),
            self.cpu.jump("0x0A"),
            self.cpu.execute(),
            "Computer started successfully!",
        ]


def main() -> None:
    print("=" * 60)
    print("Facade Pattern - Home Theater Demo")
    print("=" * 60)

    # Create subsystem components
    amp = Amplifier("Top-O-Line Amplifier")
    dvd = DvdPlayer("Top-O-Line DVD Player")
    streaming = StreamingPlayer("Streaming Player")
    projector = Projector("Top-O-Line Projector")
    screen = Screen("Theater Screen")
    lights = TheaterLights("Theater Ceiling Lights")
    popper = PopcornPopper("Popcorn Popper")

    # Create facade
    home_theater = HomeTheaterFacade(
        amp, dvd, streaming, projector, screen, lights, popper
    )

    # Demo 1: Watch a movie (simple operation)
    print("\n--- Watch Movie ---")
    for action in home_theater.watch_movie("Raiders of the Lost Ark"):
        print(f"  {action}")

    print("\n--- End Movie ---")
    for action in home_theater.end_movie():
        print(f"  {action}")

    # Demo 2: Stream a show
    print("\n--- Stream Show ---")
    for action in home_theater.stream_show("Stranger Things"):
        print(f"  {action}")

    print("\n--- End Streaming ---")
    for action in home_theater.end_streaming():
        print(f"  {action}")

    # Demo 3: Listen to music
    print("\n--- Listen to Music ---")
    for action in home_theater.listen_to_music("Spotify"):
        print(f"  {action}")

    print("\n--- End Music ---")
    for action in home_theater.end_music():
        print(f"  {action}")

    # Demo 4: Computer facade
    print("\n--- Computer Startup Facade ---")
    computer = ComputerFacade()
    for action in computer.start():
        print(f"  {action}")

    # Demo 5: Show the complexity hidden by facade
    print("\n--- Without Facade (Direct Subsystem Access) ---")
    print("To watch a movie, client would need to:")
    print("  1. popper.on()")
    print("  2. popper.pop()")
    print("  3. lights.dim(10)")
    print("  4. screen.down()")
    print("  5. projector.on()")
    print("  6. projector.wide_screen_mode()")
    print("  7. amp.on()")
    print("  8. amp.set_source('DVD')")
    print("  9. amp.set_surround_sound()")
    print("  10. amp.set_volume(5)")
    print("  11. dvd.on()")
    print("  12. dvd.play(movie)")
    print("\nWith Facade: home_theater.watch_movie(movie)")

    print("\n" + "=" * 60)
    print("Benefits of Facade Pattern:")
    print("=" * 60)
    print("1. Simplifies client interaction with complex subsystems")
    print("2. Decouples client from subsystem components")
    print("3. Doesn't prevent direct subsystem access if needed")
    print("4. Can layer facades for large systems")
    print("5. Follows Principle of Least Knowledge")


if __name__ == "__main__":
    main()
