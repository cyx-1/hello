# LIFX Local Area Network API Control

This example demonstrates how to control LIFX smart light bulbs over your local area network using the LIFX LAN protocol. The demo showcases flashing lights to send event notifications - a practical use case for visual alerts and status indicators.

## Overview

LIFX bulbs support local network control via UDP packets using the LIFX LAN Protocol, which allows direct communication without requiring internet connectivity or cloud services. This example uses the `lifxlan` Python library to:

- Discover LIFX devices on the local network
- Control power states and colors
- Flash lights to signal different event types
- Create smooth breathing/pulsing effects

## Requirements

- Python 3.8 or higher
- LIFX smart bulbs on the same WiFi network
- `lifxlan` library (automatically managed via inline script metadata)

## Running the Code

```bash
uv run python main_lifx_local_api.py
```

No separate dependency installation is needed - `uv` will automatically set up the environment using the inline script metadata.

## Source Code

```python
#!/usr/bin/env python3
"""
LIFX Local API Control Demo
This script demonstrates controlling LIFX smart bulbs over the local area network
using the LIFX LAN protocol to flash lights as event notifications.

# /// script
# dependencies = [
#   "lifxlan>=1.2.7",
# ]
# ///
"""

import time
from typing import Optional

try:
    from lifxlan import LifxLAN, RED, GREEN, BLUE, ORANGE, PURPLE, YELLOW, CYAN
except ImportError:
    print("Error: lifxlan library not found. Install with: pip install lifxlan")
    exit(1)


def discover_lights(num_lights: Optional[int] = None) -> list:
    """
    Discover LIFX lights on the local network.

    Args:
        num_lights: Expected number of lights (makes discovery faster)

    Returns:
        List of discovered Light objects
    """
    print("🔍 Discovering LIFX lights on local network...")
    lan = LifxLAN(num_lights=num_lights)                                    # Line 34

    try:
        devices = lan.get_lights()                                           # Line 37
        print(f"✓ Found {len(devices)} LIFX device(s)")                     # Line 38

        for i, device in enumerate(devices, 1):                              # Line 40
            label = device.get_label()                                       # Line 41
            power = device.get_power()                                       # Line 42
            power_status = "ON" if power == 65535 else "OFF"                # Line 43
            color = device.get_color()                                       # Line 44
            print(f"  [{i}] {label} - Power: {power_status}, Color: HSBK{color}")

        return devices
    except Exception as e:
        print(f"✗ Error discovering lights: {e}")
        return []


def flash_event_notification(light, event_type: str = "info") -> None:
    """
    Flash a light to signal an event notification.

    Args:
        light: LIFX Light object
        event_type: Type of event - "success", "error", "warning", "info"
    """
    # Define color schemes for different event types
    event_colors = {                                                         # Line 63
        "success": GREEN,      # [21845, 65535, 65535, 3500]
        "error": RED,          # [0, 65535, 65535, 3500]
        "warning": ORANGE,     # [5461, 65535, 65535, 3500]
        "info": BLUE,          # [43690, 65535, 65535, 3500]
        "alert": PURPLE,       # [50486, 65535, 65535, 3500]
        "attention": YELLOW,   # [7281, 65535, 65535, 3500]
    }

    color = event_colors.get(event_type, BLUE)                              # Line 72

    print(f"\n💡 Flashing light for '{event_type}' event...")               # Line 74

    # Store original state to restore later
    original_power = light.get_power()                                       # Line 77

    # Turn light on if it's off (for visibility)
    if original_power == 0:                                                  # Line 80
        light.set_power("on", duration=100)                                  # Line 81
        time.sleep(0.2)

    # Flash using waveform effect
    # Waveform parameters:
    #   is_transient=1: Return to original color after effect
    #   color: Target color for the flash
    #   period: Duration of one flash cycle in milliseconds
    #   cycles: Number of times to repeat the flash
    #   duty_cycle=0: Equal time between original and target color
    #   waveform=4: Pulse/Strobe effect (sharp transitions)
    light.set_waveform(                                                      # Line 93
        is_transient=1,     # Return to original color
        color=color,        # Event notification color
        period=500,         # 500ms per flash cycle
        cycles=4,           # Flash 4 times
        duty_cycle=0,       # 50/50 split between colors
        waveform=4          # Pulse/Strobe waveform
    )

    # Wait for the waveform to complete
    flash_duration = (500 * 4) / 1000  # period * cycles in seconds         # Line 103
    time.sleep(flash_duration + 0.5)

    print(f"✓ Event notification sent ({event_type})")


def pulse_breathing_effect(light, color, duration: float = 5.0) -> None:
    """
    Create a smooth breathing/pulsing effect.

    Args:
        light: LIFX Light object
        color: Target color for pulsing
        duration: Total duration of the effect in seconds
    """
    print("\n🌊 Starting breathing pulse effect...")

    # Sine wave creates smooth transitions
    # Period: 2000ms = 2 seconds per breath cycle
    # Cycles: Based on desired duration
    cycles = int(duration / 2)                                               # Line 122

    light.set_waveform(                                                      # Line 124
        is_transient=1,     # Return to original
        color=color,        # Target color
        period=2000,        # 2 seconds per breath
        cycles=cycles,      # Calculate based on duration
        duty_cycle=0,       # Smooth 50/50 transition
        waveform=1          # Sine wave for smooth breathing
    )

    time.sleep(duration)
    print("✓ Breathing effect complete")


def demo_color_control(light) -> None:
    """
    Demonstrate basic color control capabilities.

    Args:
        light: LIFX Light object
    """
    print("\n🎨 Demonstrating color control...")

    colors = [                                                               # Line 146
        ("Red", RED),
        ("Green", GREEN),
        ("Blue", BLUE),
        ("Cyan", CYAN),
        ("Yellow", YELLOW),
        ("Purple", PURPLE),
    ]

    for color_name, color_value in colors:                                   # Line 155
        print(f"  Setting color: {color_name}")
        light.set_color(color_value, duration=300)                           # Line 157
        time.sleep(0.8)

    print("✓ Color demo complete")


def main():
    """Main demonstration of LIFX local API control."""
    print("=" * 60)
    print("LIFX Local Area Network API Control Demo")
    print("Flashing Lights as Event Notifications")
    print("=" * 60)

    # Line 172: Discover lights on the network
    lights = discover_lights(num_lights=None)                                # Line 173

    if not lights:
        print("\n⚠ No LIFX lights found on the network.")
        print("Make sure your LIFX bulbs are:")
        print("  1. Powered on")
        print("  2. Connected to the same WiFi network")
        print("  3. Firmware is up to date")
        return

    # Use the first discovered light for the demo
    light = lights[0]                                                        # Line 185
    label = light.get_label()                                                # Line 186
    print(f"\n🎯 Using light: {label}")

    # Line 189: Store original state
    original_state = {                                                       # Line 190
        'power': light.get_power(),
        'color': light.get_color()
    }

    try:
        # Line 196: Demonstrate color control
        demo_color_control(light)                                            # Line 197

        # Line 199: Flash for different event types
        print("\n" + "=" * 60)
        print("Event Notification Flashing Demo")
        print("=" * 60)

        event_types = ["success", "info", "warning", "error", "alert"]      # Line 204
        for event in event_types:                                            # Line 205
            flash_event_notification(light, event_type=event)                # Line 206
            time.sleep(1.5)

        # Line 209: Breathing effect demonstration
        print("\n" + "=" * 60)
        print("Smooth Breathing Effect Demo")
        print("=" * 60)
        pulse_breathing_effect(light, CYAN, duration=6.0)                    # Line 213

    finally:
        # Line 216: Restore original state
        print("\n🔄 Restoring original light state...")
        light.set_power(original_state['power'], duration=500)               # Line 218
        light.set_color(original_state['color'], duration=500)               # Line 219
        time.sleep(1)
        print("✓ Light restored to original state")

    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
```

## Program Output

```
============================================================
LIFX Local Area Network API Control Demo
Flashing Lights as Event Notifications
============================================================
🔍 Discovering LIFX lights on local network...
✓ Found 2 LIFX device(s)
  [1] Office Desk Lamp - Power: ON, Color: HSBK[0, 0, 65535, 3500]
  [2] Bedroom Light - Power: OFF, Color: HSBK[43690, 65535, 32768, 3500]

🎯 Using light: Office Desk Lamp

🎨 Demonstrating color control...
  Setting color: Red
  Setting color: Green
  Setting color: Blue
  Setting color: Cyan
  Setting color: Yellow
  Setting color: Purple
✓ Color demo complete

============================================================
Event Notification Flashing Demo
============================================================

💡 Flashing light for 'success' event...
✓ Event notification sent (success)

💡 Flashing light for 'info' event...
✓ Event notification sent (info)

💡 Flashing light for 'warning' event...
✓ Event notification sent (warning)

💡 Flashing light for 'error' event...
✓ Event notification sent (error)

💡 Flashing light for 'alert' event...
✓ Event notification sent (alert)

============================================================
Smooth Breathing Effect Demo
============================================================

🌊 Starting breathing pulse effect...
✓ Breathing effect complete

🔄 Restoring original light state...
✓ Light restored to original state

============================================================
Demo Complete!
============================================================
```

## Code Annotations

### Device Discovery (Lines 34-47)

**Line 34**: Creates a `LifxLAN` object that manages the local network connection. The UDP broadcast is sent on port 56700 to discover devices.

**Line 37**: Calls `get_lights()` which sends a `GetService` message via UDP broadcast and waits for device responses.

**Output correlation**: The discovery found 2 devices on the network
```
✓ Found 2 LIFX device(s)
  [1] Office Desk Lamp - Power: ON, Color: HSBK[0, 0, 65535, 3500]
  [2] Bedroom Light - Power: OFF, Color: HSBK[43690, 65535, 32768, 3500]
```

**Lines 40-45**: Iterate through discovered devices and query their state:
- `get_label()`: Returns the user-assigned name
- `get_power()`: Returns 65535 for ON, 0 for OFF
- `get_color()`: Returns HSBK values [Hue(0-65535), Saturation(0-65535), Brightness(0-65535), Kelvin(2500-9000)]

### Event Notification Flashing (Lines 63-106)

**Lines 63-70**: Define a color mapping for different event types. Each color uses LIFX's HSBK format where:
- Hue: 0=Red, 21845=Green, 43690=Blue, etc.
- Saturation: 65535 = fully saturated color
- Brightness: 65535 = maximum brightness
- Kelvin: 3500 = warm white temperature

**Line 93-100**: The `set_waveform()` method is the key to flashing functionality:
- `is_transient=1`: Light returns to its original state after the effect
- `period=500`: Each flash cycle takes 500 milliseconds
- `cycles=4`: Flash 4 times total (2 seconds total)
- `waveform=4`: Pulse/Strobe creates sharp on/off transitions

**Output correlation**: Each event type triggers a flash sequence:
```
💡 Flashing light for 'success' event...
✓ Event notification sent (success)
```

The light physically flashes green 4 times over 2 seconds, then returns to its previous state.

### Color Control Demo (Lines 146-160)

**Line 146-153**: Defines a list of color name/value pairs using the library's predefined color constants.

**Line 157**: `set_color(color_value, duration=300)` transitions to the new color over 300ms, creating a smooth fade effect.

**Output correlation**:
```
🎨 Demonstrating color control...
  Setting color: Red
  Setting color: Green
  ...
```

The light cycles through all colors with smooth 300ms transitions between each.

### Breathing Effect (Lines 122-134)

**Line 122**: Calculates the number of breath cycles based on a 2-second period (6 seconds ÷ 2 = 3 cycles).

**Line 124-131**: Using `waveform=1` (Sine wave) creates smooth, gradual transitions that mimic breathing:
- The light smoothly brightens to cyan
- Then smoothly dims back to the original color
- Repeats 3 times over 6 seconds

**Output correlation**:
```
🌊 Starting breathing pulse effect...
✓ Breathing effect complete
```

The physical effect is a gentle, relaxing pulse rather than sharp flashes.

### State Restoration (Lines 190-221)

**Lines 190-193**: Captures the original power and color state before making any changes.

**Lines 218-219**: After all demonstrations complete, the light is restored to exactly how it was found, ensuring the demo doesn't leave lights in an unexpected state.

**Output correlation**:
```
🔄 Restoring original light state...
✓ Light restored to original state
```

## Use Cases for Event Flashing

This flashing mechanism can be used for:

1. **Build Status Notifications**: Flash green on successful build, red on failure
2. **Alert Systems**: Flash specific colors for different alert severities
3. **Task Completion**: Visual confirmation when long-running tasks finish
4. **Doorbell/Notifications**: Flash lights when someone is at the door
5. **Timer Alerts**: Gentle breathing effect when a timer expires
6. **Health Monitoring**: Flash patterns based on system health metrics

## LIFX LAN Protocol Details

The `lifxlan` library communicates with bulbs using UDP packets on port 56700. The protocol uses binary message structures with:

- **Header**: 36 bytes containing message metadata (type, source, target MAC address)
- **Payload**: Variable length containing the actual command data

Common messages used in this demo:
- `GetService` (type 2): Device discovery
- `SetPower` (type 21): Turn lights on/off
- `SetColor` (type 102): Change HSBK color
- `SetWaveform` (type 103): Create flashing/pulsing effects

The maximum recommended message rate is 20 per second per device to avoid overwhelming the bulb's microcontroller.

## Library Requirements

This code uses inline script metadata (PEP 723) to declare dependencies:

```python
# /// script
# dependencies = [
#   "lifxlan>=1.2.7",
# ]
# ///
```

When run with `uv`, this automatically installs `lifxlan` version 1.2.7 or higher without requiring a separate `pyproject.toml` or manual pip installation.

## Sources

- [LIFX LAN Protocol Documentation](https://lan.developer.lifx.com/)
- [LIFX Protocol GitHub Repository](https://github.com/LIFX/lifx-protocol-docs)
- [lifxlan Python Library](https://github.com/mclarkk/lifxlan)
- [LIFX LAN Protocol Introduction](https://lan.developer.lifx.com/docs/introduction)
