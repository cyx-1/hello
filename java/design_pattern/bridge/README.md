# Bridge Pattern

The Bridge pattern decouples an abstraction from its implementation so that the two can vary independently.

## How to Run

```bash
cd java/bridge
mvn compile exec:java
```

## Key Source Code

### Implementor Interface (Lines 9-17)
```java
interface Device {
    boolean isEnabled();
    void enable();
    void disable();
    int getVolume();
    void setVolume(int volume);
    // ...
}
```

### Abstraction (Lines 124-154)
```java
abstract class RemoteControl {
    protected Device device;  // Bridge to implementation

    protected RemoteControl(Device device) {
        this.device = device;
    }

    public void togglePower() {
        if (device.isEnabled()) {
            device.disable();
        } else {
            device.enable();
        }
    }
}
```

### Refined Abstraction (Lines 163-179)
```java
class AdvancedRemote extends RemoteControl {
    public void mute() {
        device.setVolume(0);
    }

    public void setVolumeLevel(int level) {
        device.setVolume(level);
    }
}
```

## Program Output

```
=== Bridge Pattern Demonstration ===

--- 1. Basic Remote with TV ---
  [TV] TV is now ON
  [TV] Volume set to 40
  [TV] Channel set to 2
  [TV] Channel set to 3
Status: TV [on=true, volume=40, channel=3]

--- 2. Advanced Remote with Radio ---
  [Radio] Radio is now ON
  [AdvancedRemote] Setting exact volume level
  [Radio] Volume set to 75
  [AdvancedRemote] Going to channel 102
  [Radio] Frequency set to 102 FM
  [AdvancedRemote] Muting device
  [Radio] Volume set to 0

--- 4. Shapes with Vector Renderer ---
  [VectorRenderer] Drawing circle at (5.0, 10.0) with radius 25.0
  [VectorRenderer] Drawing rectangle at (10.0, 20.0) with size 100.0x50.0

--- 5. Same Shapes with Raster Renderer ---
  [RasterRenderer] Rasterizing circle at (5.0, 10.0) with radius 25.0 pixels
  [RasterRenderer] Rasterizing rectangle at (10.0, 20.0) with size 100.0x50.0 pixels
```

## Pattern Benefits

1. **Decoupling**: Abstraction and implementation can vary independently
2. **Extensibility**: Add new abstractions and implementations without modifying existing code
3. **Platform Independence**: Same abstraction with different platform implementations

## Requirements

- Java 17 or higher
- Maven 3.x
