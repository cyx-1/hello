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
    lan = LifxLAN(num_lights=num_lights)

    try:
        devices = lan.get_lights()
        print(f"✓ Found {len(devices)} LIFX device(s)")

        for i, device in enumerate(devices, 1):
            label = device.get_label()
            power = device.get_power()
            power_status = "ON" if power == 65535 else "OFF"
            color = device.get_color()
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
    event_colors = {
        "success": GREEN,      # [21845, 65535, 65535, 3500]
        "error": RED,          # [0, 65535, 65535, 3500]
        "warning": ORANGE,     # [5461, 65535, 65535, 3500]
        "info": BLUE,          # [43690, 65535, 65535, 3500]
        "alert": PURPLE,       # [50486, 65535, 65535, 3500]
        "attention": YELLOW,   # [7281, 65535, 65535, 3500]
    }

    color = event_colors.get(event_type, BLUE)

    print(f"\n💡 Flashing light for '{event_type}' event...")

    # Store original state to restore later
    original_power = light.get_power()

    # Turn light on if it's off (for visibility)
    if original_power == 0:
        light.set_power("on", duration=100)
        time.sleep(0.2)

    # Flash using waveform effect
    # Waveform parameters:
    #   is_transient=1: Return to original color after effect
    #   color: Target color for the flash
    #   period: Duration of one flash cycle in milliseconds
    #   cycles: Number of times to repeat the flash
    #   duty_cycle=0: Equal time between original and target color
    #   waveform=4: Pulse/Strobe effect (sharp transitions)
    light.set_waveform(
        is_transient=1,     # Return to original color
        color=color,        # Event notification color
        period=500,         # 500ms per flash cycle
        cycles=4,           # Flash 4 times
        duty_cycle=0,       # 50/50 split between colors
        waveform=4          # Pulse/Strobe waveform
    )

    # Wait for the waveform to complete
    flash_duration = (500 * 4) / 1000  # period * cycles in seconds
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
    cycles = int(duration / 2)

    light.set_waveform(
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

    colors = [
        ("Red", RED),
        ("Green", GREEN),
        ("Blue", BLUE),
        ("Cyan", CYAN),
        ("Yellow", YELLOW),
        ("Purple", PURPLE),
    ]

    for color_name, color_value in colors:
        print(f"  Setting color: {color_name}")
        light.set_color(color_value, duration=300)
        time.sleep(0.8)

    print("✓ Color demo complete")


def main():
    """Main demonstration of LIFX local API control."""
    print("=" * 60)
    print("LIFX Local Area Network API Control Demo")
    print("Flashing Lights as Event Notifications")
    print("=" * 60)

    # Line 163: Discover lights on the network
    lights = discover_lights(num_lights=None)

    if not lights:
        print("\n⚠ No LIFX lights found on the network.")
        print("Make sure your LIFX bulbs are:")
        print("  1. Powered on")
        print("  2. Connected to the same WiFi network")
        print("  3. Firmware is up to date")
        return

    # Use the first discovered light for the demo
    light = lights[0]
    label = light.get_label()
    print(f"\n🎯 Using light: {label}")

    # Line 179: Store original state
    original_state = {
        'power': light.get_power(),
        'color': light.get_color()
    }

    try:
        # Line 186: Demonstrate color control
        demo_color_control(light)

        # Line 189: Flash for different event types
        print("\n" + "=" * 60)
        print("Event Notification Flashing Demo")
        print("=" * 60)

        event_types = ["success", "info", "warning", "error", "alert"]
        for event in event_types:
            flash_event_notification(light, event_type=event)
            time.sleep(1.5)

        # Line 200: Breathing effect demonstration
        print("\n" + "=" * 60)
        print("Smooth Breathing Effect Demo")
        print("=" * 60)
        pulse_breathing_effect(light, CYAN, duration=6.0)

    finally:
        # Line 207: Restore original state
        print("\n🔄 Restoring original light state...")
        light.set_power(original_state['power'], duration=500)
        light.set_color(original_state['color'], duration=500)
        time.sleep(1)
        print("✓ Light restored to original state")

    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
