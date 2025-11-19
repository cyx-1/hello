# Facade Pattern

The Facade pattern provides a unified interface to a set of interfaces in a subsystem, making the subsystem easier to use.

## How to Run

```bash
cd java/facade
mvn compile exec:java
```

## Key Source Code

### Complex Subsystem Classes (Lines 9-96)
```java
class Amplifier {
    public void on() { ... }
    public void setVolume(int level) { ... }
    public void setSurroundSound() { ... }
}

class DVDPlayer {
    public void on() { ... }
    public void play(String movie) { ... }
}

class Projector {
    public void on() { ... }
    public void wideScreenMode() { ... }
}
// ... more subsystem classes
```

### Facade (Lines 99-142)
```java
class HomeTheaterFacade {
    private Amplifier amp;
    private DVDPlayer dvd;
    private Projector projector;
    // ...

    public void watchMovie(String movie) {
        popcorn.on();
        popcorn.pop();
        lights.dim(10);
        screen.down();
        projector.on();
        projector.wideScreenMode();
        amp.on();
        amp.setSurroundSound();
        amp.setVolume(5);
        dvd.on();
        dvd.play(movie);
    }
}
```

## Program Output

```
=== Facade Pattern Demonstration ===

--- 1. Home Theater Facade ---
Get ready to watch a movie...

  [Popcorn] Popcorn Maker is ON
  [Popcorn] Popping popcorn!
  [Lights] Dimming to 10%
  [Screen] 120-inch Screen going down
  [Projector] Epson HD Projector is ON
  [Projector] Widescreen mode (16:9)
  [Amplifier] Top-O-Line Amplifier is ON
  [Amplifier] Surround sound enabled
  [Amplifier] Setting volume to 5
  [DVDPlayer] Sony DVD Player is ON
  [DVDPlayer] Playing "Inception"

--- 2. Computer Startup Facade ---
Starting computer...

  [CPU] Freezing processor
  [HardDrive] Reading 512 bytes from sector 0
  [Memory] Loading data at position 0
  [CPU] Jumping to position 0
  [CPU] Executing instructions

  Computer started successfully!

--- 3. E-Commerce Order Facade ---
Processing order ORD-12345...

  [Inventory] Checking stock for PROD-789
  [Payment] Processing $99.99 for order ORD-12345
  [Inventory] Updating stock: PROD-789 -2
  [Shipping] Creating shipment for ORD-12345 to 123 Main St
  [Notification] Sending confirmation to customer@example.com

  Order ORD-12345 completed successfully!
```

## Pattern Benefits

1. **Simplification**: Hide subsystem complexity
2. **Decoupling**: Reduce dependencies on subsystem
3. **Layering**: Provide entry points to subsystem layers

## Requirements

- Java 17 or higher
- Maven 3.x
