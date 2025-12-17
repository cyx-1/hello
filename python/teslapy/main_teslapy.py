#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "teslapy>=2.10.0",
# ]
# ///

"""
TeslaPY Demonstration - Python Library for Tesla API
=====================================================
This script demonstrates the TeslaPY library for interacting with Tesla's API.
TeslaPY allows you to authenticate, retrieve vehicle data, and control Tesla vehicles.

Note: This requires a Tesla account with at least one vehicle registered.
"""

import os
from typing import Optional


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def demo_authentication() -> Optional[object]:
    """
    Demonstrate TeslaPY authentication.
    Returns Tesla object if successful, None otherwise.
    """
    print_section("1. AUTHENTICATION")

    try:
        import teslapy

        # Line 40: Initialize Tesla API client
        # The cache file stores authentication tokens
        cache_file = os.path.join(os.path.dirname(__file__), 'cache.json')
        print(f"Line 40: Initializing Tesla API client with cache: {cache_file}")

        with teslapy.Tesla(os.environ.get('TESLA_EMAIL', 'demo@example.com'),
                          cache_file=cache_file) as tesla:

            # Line 48: Check if we need to authenticate
            if not tesla.authorized:
                print("\nLine 48: Not authorized - authentication required")
                print("  In production, this would open a browser for OAuth login")
                print("  or require MFA code input via tesla.fetch_token()")
                print("\n  For demo purposes, skipping actual authentication...")
                return None

            print(f"Line 55: Successfully authenticated as: {os.environ.get('TESLA_EMAIL', 'demo@example.com')}")
            return tesla

    except ImportError:
        print("Error: teslapy module not found")
        return None
    except Exception as e:
        print(f"Line 62: Authentication info: {str(e)}")
        print("  Note: Full authentication requires valid Tesla credentials")
        return None


def demo_vehicle_list(tesla: object) -> Optional[list]:
    """Demonstrate fetching the list of vehicles."""
    print_section("2. VEHICLE LIST")

    try:
        # Line 73: Fetch list of vehicles associated with the account
        print("Line 73: Fetching vehicle list from Tesla API...")
        vehicles = tesla.vehicle_list()

        print(f"Line 76: Found {len(vehicles)} vehicle(s) in account\n")

        for idx, vehicle in enumerate(vehicles, 1):
            print(f"  Vehicle {idx}:")
            print(f"    VIN: {vehicle['vin']}")
            print(f"    Display Name: {vehicle['display_name']}")
            print(f"    State: {vehicle['state']}")
            print(f"    Vehicle ID: {vehicle['id']}")
            print()

        return vehicles

    except Exception as e:
        print(f"Error fetching vehicles: {str(e)}")
        return None


def demo_vehicle_data(vehicle: object) -> None:
    """Demonstrate retrieving detailed vehicle data."""
    print_section("3. VEHICLE DATA")

    try:
        # Line 100: Wake up the vehicle if it's asleep
        print("Line 100: Waking up vehicle (if asleep)...")
        vehicle.sync_wake_up()

        # Line 104: Get comprehensive vehicle data
        print("Line 104: Retrieving vehicle data...")
        data = vehicle.get_vehicle_data()

        # Line 108: Display battery and charging information
        print("\n📊 BATTERY & CHARGING:")
        charge_state = data['charge_state']
        print(f"  Battery Level: {charge_state['battery_level']}%")
        print(f"  Charge Limit: {charge_state['charge_limit_soc']}%")
        print(f"  Charging State: {charge_state['charging_state']}")
        print(f"  Range: {charge_state['battery_range']:.1f} miles")
        print(f"  Est. Range: {charge_state['est_battery_range']:.1f} miles")

        # Line 118: Display climate information
        print("\n🌡️  CLIMATE:")
        climate_state = data['climate_state']
        print(f"  Inside Temp: {climate_state['inside_temp']}°C")
        print(f"  Outside Temp: {climate_state['outside_temp']}°C")
        print(f"  Driver Temp Setting: {climate_state['driver_temp_setting']}°C")
        print(f"  Climate On: {climate_state['is_climate_on']}")

        # Line 127: Display vehicle state
        print("\n🚗 VEHICLE STATE:")
        vehicle_state = data['vehicle_state']
        print(f"  Odometer: {vehicle_state['odometer']:.1f} miles")
        print(f"  Locked: {vehicle_state['locked']}")
        print(f"  Software Version: {vehicle_state['car_version']}")
        print(f"  Sentry Mode: {vehicle_state.get('sentry_mode', 'N/A')}")

        # Line 135: Display drive state
        print("\n📍 LOCATION & DRIVE:")
        drive_state = data['drive_state']
        print(f"  Speed: {drive_state.get('speed', 0) or 0} mph")
        print(f"  Shift State: {drive_state.get('shift_state', 'P')}")
        print(f"  Latitude: {drive_state.get('latitude', 'N/A')}")
        print(f"  Longitude: {drive_state.get('longitude', 'N/A')}")

    except Exception as e:
        print(f"Error retrieving vehicle data: {str(e)}")


def demo_climate_control(vehicle: object) -> None:
    """Demonstrate climate control commands."""
    print_section("4. CLIMATE CONTROL")

    try:
        # Line 153: Start climate control
        print("Line 153: Starting climate control...")
        print("  Command: vehicle.command('CLIMATE_ON')")
        print("  This would turn on the HVAC system")
        print("  Note: Skipping actual command in demo mode\n")

        # Line 159: Set temperature
        print("Line 159: Setting temperature to 22°C...")
        print("  Command: vehicle.command('CHANGE_CLIMATE_TEMPERATURE_SETTING',")
        print("                          driver_temp=22, passenger_temp=22)")
        print("  This would set both driver and passenger temperatures\n")

        # Line 165: Turn on seat heaters
        print("Line 165: Activating seat heater...")
        print("  Command: vehicle.command('REMOTE_SEAT_HEATER_REQUEST',")
        print("                          heater=0, level=2)")
        print("  heater=0 is driver seat, level ranges 0-3")

    except Exception as e:
        print(f"Error with climate control: {str(e)}")


def demo_charging_control(vehicle: object) -> None:
    """Demonstrate charging control commands."""
    print_section("5. CHARGING CONTROL")

    try:
        # Line 181: Set charge limit
        print("Line 181: Setting charge limit to 80%...")
        print("  Command: vehicle.command('CHANGE_CHARGE_LIMIT', percent=80)")
        print("  This sets the maximum charge level\n")

        # Line 186: Start charging
        print("Line 186: Starting charge...")
        print("  Command: vehicle.command('START_CHARGE')")
        print("  This initiates charging if plugged in\n")

        # Line 191: Stop charging
        print("Line 191: Stopping charge...")
        print("  Command: vehicle.command('STOP_CHARGE')")
        print("  This stops an active charging session")

    except Exception as e:
        print(f"Error with charging control: {str(e)}")


def demo_additional_features(vehicle: object) -> None:
    """Demonstrate additional TeslaPY features."""
    print_section("6. ADDITIONAL FEATURES")

    try:
        # Line 206: Lock/Unlock doors
        print("Line 206: Door lock control")
        print("  Lock: vehicle.command('DOOR_LOCK')")
        print("  Unlock: vehicle.command('DOOR_UNLOCK')\n")

        # Line 211: Honk horn and flash lights
        print("Line 211: Horn and lights")
        print("  Honk: vehicle.command('HONK_HORN')")
        print("  Flash: vehicle.command('FLASH_LIGHTS')\n")

        # Line 216: Open/close trunk/frunk
        print("Line 216: Trunk control")
        print("  Rear: vehicle.command('ACTUATE_TRUNK', which_trunk='rear')")
        print("  Front: vehicle.command('ACTUATE_TRUNK', which_trunk='front')\n")

        # Line 221: Sentry mode
        print("Line 221: Sentry mode control")
        print("  Enable: vehicle.command('SET_SENTRY_MODE', on=True)")
        print("  Disable: vehicle.command('SET_SENTRY_MODE', on=False)\n")

        # Line 226: Remote start
        print("Line 226: Remote start (for keyless driving)")
        print("  Start: vehicle.command('REMOTE_START_DRIVE')")
        print("  Requires password parameter")

    except Exception as e:
        print(f"Error with additional features: {str(e)}")


def demo_battery_products(tesla: object) -> None:
    """Demonstrate interaction with Tesla Energy products (Powerwall, etc.)."""
    print_section("7. ENERGY PRODUCTS")

    try:
        # Line 242: List energy products
        print("Line 242: Checking for Tesla Energy products...")
        print("  Command: tesla.battery_list()")
        print("  This retrieves Powerwall and Solar products\n")

        print("  Energy products include:")
        print("    - Powerwall: Home battery storage")
        print("    - Solar Panels: Solar energy generation")
        print("    - Solar Roof: Integrated solar tiles\n")

        print("  Available data for energy products:")
        print("    - Battery percentage and capacity")
        print("    - Power flow (grid, battery, home, solar)")
        print("    - Operation mode (self-powered, backup, etc.)")
        print("    - Energy site information")

    except Exception as e:
        print(f"Error with energy products: {str(e)}")


def main() -> None:
    """Main demonstration function."""
    print("=" * 70)
    print("  TeslaPY - Python Library for Tesla API")
    print("  Comprehensive Feature Demonstration")
    print("=" * 70)
    print("\nTeslaPY provides a Python interface to Tesla's vehicle API,")
    print("enabling remote monitoring and control of Tesla vehicles and")
    print("energy products through their official API.")

    # Line 275: Authentication demo
    tesla = demo_authentication()

    # For demo purposes without credentials, show all features
    if tesla is None:
        print("\n" + "=" * 70)
        print("  Running in DEMO MODE (no Tesla credentials)")
        print("  Showing API structure and available commands")
        print("=" * 70)

        # Line 284: Show simulated feature demos
        print_section("DEMO: Vehicle List Structure")
        print("In production, vehicle_list() returns:")
        print("  [")
        print("    {")
        print("      'id': 1234567890,")
        print("      'vehicle_id': 9876543210,")
        print("      'vin': 'TSLA1234567890',")
        print("      'display_name': 'My Tesla',")
        print("      'state': 'online',")
        print("      'in_service': False,")
        print("      'calendar_enabled': True")
        print("    }")
        print("  ]")

        # Line 300: Show data structure examples
        print_section("DEMO: Available Commands")
        print("TeslaPY supports extensive vehicle control:")
        print("\n🔋 Charging:")
        print("  - START_CHARGE / STOP_CHARGE")
        print("  - CHANGE_CHARGE_LIMIT")
        print("  - SET_CHARGING_AMPS")

        print("\n🌡️  Climate:")
        print("  - CLIMATE_ON / CLIMATE_OFF")
        print("  - CHANGE_CLIMATE_TEMPERATURE_SETTING")
        print("  - REMOTE_SEAT_HEATER_REQUEST")
        print("  - REMOTE_STEERING_WHEEL_HEATER_REQUEST")

        print("\n🚗 Vehicle Control:")
        print("  - DOOR_LOCK / DOOR_UNLOCK")
        print("  - ACTUATE_TRUNK")
        print("  - WINDOW_CONTROL")
        print("  - REMOTE_START_DRIVE")
        print("  - HONK_HORN / FLASH_LIGHTS")

        print("\n🛡️  Security:")
        print("  - SET_SENTRY_MODE")
        print("  - SET_VALET_MODE")
        print("  - SPEED_LIMIT_SET_LIMIT")

        print("\n⚡ Advanced:")
        print("  - SCHEDULE_SOFTWARE_UPDATE")
        print("  - NAVIGATION_REQUEST")
        print("  - SHARE (send address to vehicle)")

        # Line 336: Library information
        print_section("LIBRARY INFORMATION")
        print("Package: teslapy")
        print("PyPI: https://pypi.org/project/TeslaPy/")
        print("GitHub: https://github.com/tdorssers/TeslaPy")
        print("License: MIT")
        print("\nKey Features:")
        print("  ✓ OAuth authentication with token caching")
        print("  ✓ Vehicle data and state retrieval")
        print("  ✓ Remote vehicle commands")
        print("  ✓ Energy products support (Powerwall/Solar)")
        print("  ✓ Automatic rate limiting")
        print("  ✓ Comprehensive error handling")

        print("\n" + "=" * 70)
        print("  Demo completed successfully!")
        print("=" * 70)

    else:
        # Line 358: If authenticated, run real demos
        vehicles = demo_vehicle_list(tesla)

        if vehicles and len(vehicles) > 0:
            # Use the first vehicle for demonstrations
            vehicle = vehicles[0]

            demo_vehicle_data(vehicle)
            demo_climate_control(vehicle)
            demo_charging_control(vehicle)
            demo_additional_features(vehicle)

        demo_battery_products(tesla)


if __name__ == "__main__":
    main()
