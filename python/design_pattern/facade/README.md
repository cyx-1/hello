# Facade Pattern

The Facade pattern provides a unified interface to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use by hiding its complexity.

**Requires Python 3.10+**

## Key Components

- **Facade** (`HomeTheaterFacade`, `ComputerFacade`): Provides simple interface to complex subsystem
- **Subsystem classes**: Implement subsystem functionality (Amplifier, DvdPlayer, Projector, etc.)
- **Client**: Uses Facade instead of interacting with subsystem directly

## Source Code

### Subsystem Classes

```python:main_facade.py startLine=19 endLine=71
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
```

### Facade Implementation

```python:main_facade.py startLine=160 endLine=199
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
```

### Client Usage

```python:main_facade.py startLine=328 endLine=335
    # Demo 1: Watch a movie (simple operation)
    print("\n--- Watch Movie ---")
    for action in home_theater.watch_movie("Raiders of the Lost Ark"):
        print(f"  {action}")

    print("\n--- End Movie ---")
    for action in home_theater.end_movie():
        print(f"  {action}")
```

## Program Output

```
============================================================
Facade Pattern - Home Theater Demo
============================================================

--- Watch Movie ---
  Get ready to watch a movie...
  Popcorn Popper is ON
  Popcorn Popper popping popcorn!
  Theater Ceiling Lights dimmed to 10%
  Theater Screen going down
  Top-O-Line Projector is ON
  Top-O-Line Projector in widescreen mode (16:9)
  Top-O-Line Amplifier is ON
  Top-O-Line Amplifier source set to DVD
  Top-O-Line Amplifier surround sound ON
  Top-O-Line Amplifier volume set to 5
  Top-O-Line DVD Player is ON
  Top-O-Line DVD Player playing 'Raiders of the Lost Ark'

--- End Movie ---
  Shutting movie theater down...
  Popcorn Popper is OFF
  Theater Ceiling Lights are ON
  Theater Screen going up
  Top-O-Line Projector is OFF
  Top-O-Line Amplifier is OFF
  Top-O-Line DVD Player stopped 'Raiders of the Lost Ark'
  Top-O-Line DVD Player DVD ejected
  Top-O-Line DVD Player is OFF

--- Stream Show ---
  Get ready to stream a show...
  Theater Ceiling Lights dimmed to 20%
  Top-O-Line Projector is ON
  Top-O-Line Projector in TV mode (4:3)
  Top-O-Line Amplifier is ON
  Top-O-Line Amplifier source set to Streaming
  Top-O-Line Amplifier volume set to 4
  Streaming Player is ON
  Streaming Player streaming 'Stranger Things'

--- End Streaming ---
  Shutting down streaming...
  Streaming Player stopped streaming
  Streaming Player is OFF
  Top-O-Line Amplifier is OFF
  Top-O-Line Projector is OFF
  Theater Ceiling Lights are ON

--- Listen to Music ---
  Setting up for music...
  Theater Ceiling Lights dimmed to 50%
  Top-O-Line Amplifier is ON
  Top-O-Line Amplifier source set to Spotify
  Top-O-Line Amplifier volume set to 6

--- End Music ---
  Shutting down music...
  Top-O-Line Amplifier is OFF
  Theater Ceiling Lights are ON

--- Computer Startup Facade ---
  Starting computer...
  CPU: Freezing processor
  Memory: Loading 'BIOS' at 0x00
  CPU: Jumping to 0x00
  HardDrive: Reading 1024 bytes from sector 0
  Memory: Loading 'Boot loader' at 0x0A
  CPU: Jumping to 0x0A
  CPU: Executing instructions
  Computer started successfully!

--- Without Facade (Direct Subsystem Access) ---
To watch a movie, client would need to:
  1. popper.on()
  2. popper.pop()
  3. lights.dim(10)
  4. screen.down()
  5. projector.on()
  6. projector.wide_screen_mode()
  7. amp.on()
  8. amp.set_source('DVD')
  9. amp.set_surround_sound()
  10. amp.set_volume(5)
  11. dvd.on()
  12. dvd.play(movie)

With Facade: home_theater.watch_movie(movie)

============================================================
Benefits of Facade Pattern:
============================================================
1. Simplifies client interaction with complex subsystems
2. Decouples client from subsystem components
3. Doesn't prevent direct subsystem access if needed
4. Can layer facades for large systems
5. Follows Principle of Least Knowledge
```

## Annotations

### Watch Movie Operation (Lines 182-198)
The `watch_movie()` method (line 182) orchestrates 12 different subsystem operations with a single call. The output shows each subsystem being activated in the proper sequence:
1. Popcorn popper turns on and starts popping
2. Lights dim to 10%
3. Screen comes down
4. Projector turns on in widescreen mode
5. Amplifier configures for DVD with surround sound
6. DVD player starts the movie

This is the core value of the Facade pattern - one method call replaces 12 separate subsystem interactions.

### End Movie Operation (Lines 201-214)
The `end_movie()` method demonstrates proper shutdown sequence. Output shows all components turning off in reverse order, with the DVD being stopped, ejected, and turned off.

### Different Use Cases (Lines 216-261)
The facade provides different simplified operations:
- `stream_show()`: Different configuration (4:3 mode, no popcorn, different volume)
- `listen_to_music()`: Minimal setup (just lights and amplifier)

Each outputs a different sequence of subsystem calls tailored to the use case.

### Computer Startup Facade (Lines 286-306)
The `ComputerFacade` shows another example where a single `start()` call coordinates CPU, Memory, and HardDrive operations. Output shows the complex boot sequence hidden behind a simple interface.

### Complexity Hidden (Lines 362-376)
The output explicitly contrasts using the facade (1 line) versus direct subsystem access (12 lines). This demonstrates the pattern's primary benefit: simplified client code.

## Running the Code

```bash
uv run python main_facade.py
```
