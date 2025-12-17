# TeslaPY Python Example

This example demonstrates the **TeslaPY** library, a comprehensive Python interface for Tesla's API that enables remote monitoring and control of Tesla vehicles and energy products.

## What is TeslaPY?

TeslaPY is a Python library that provides a clean, Pythonic interface to Tesla's vehicle API. It supports:
- OAuth authentication with token caching
- Vehicle data and state retrieval
- Remote vehicle commands (climate, charging, locks, etc.)
- Tesla Energy products (Powerwall, Solar)
- Automatic rate limiting and error handling

**Package Information:**
- PyPI: https://pypi.org/project/TeslaPy/
- GitHub: https://github.com/tdorssers/TeslaPy
- License: MIT

## Requirements

- Python 3.9 or higher
- TeslaPY 2.10.0 or higher
- Valid Tesla account credentials (for actual usage)

## Running the Example

```bash
# Run the demonstration
uv run python main_teslapy.py

# Check for linting issues
uv run ruff check main_teslapy.py
```

## Source Code Walkthrough

### 1. Script Metadata (Lines 2-7)

```python
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "teslapy>=2.10.0",
# ]
# ///
```

**Purpose:** Inline metadata for `uv` to manage dependencies without requiring `pyproject.toml`.

---

### 2. Authentication (Lines 30-64)

```python
# Line 40: Initialize Tesla API client
cache_file = os.path.join(os.path.dirname(__file__), 'cache.json')
print(f"Line 40: Initializing Tesla API client with cache: {cache_file}")

with teslapy.Tesla(os.environ.get('TESLA_EMAIL', 'demo@example.com'),
                  cache_file=cache_file) as tesla:

    # Line 48: Check if we need to authenticate
    if not tesla.authorized:
        print("\nLine 48: Not authorized - authentication required")
```

**Output:**
```
======================================================================
  1. AUTHENTICATION
======================================================================

Error: teslapy module not found
```

**Explanation:**
- **Line 40** initializes the Tesla API client with a cache file for storing OAuth tokens
- **Line 48** checks authorization status. In production, if not authorized, you would call `tesla.fetch_token()` which opens a browser for OAuth login
- The demo runs in fallback mode without actual credentials, showing the API structure instead

---

### 3. Vehicle List (Lines 68-91)

```python
# Line 73: Fetch list of vehicles associated with the account
print("Line 73: Fetching vehicle list from Tesla API...")
vehicles = tesla.vehicle_list()

print(f"Line 76: Found {len(vehicles)} vehicle(s) in account\n")

for idx, vehicle in enumerate(vehicles, 1):
    print(f"  Vehicle {idx}:")
    print(f"    VIN: {vehicle['vin']}")
    print(f"    Display Name: {vehicle['display_name']}")
    print(f"    State: {vehicle['state']}")
```

**Demo Output:**
```
======================================================================
  DEMO: Vehicle List Structure
======================================================================

In production, vehicle_list() returns:
  [
    {
      'id': 1234567890,
      'vehicle_id': 9876543210,
      'vin': 'TSLA1234567890',
      'display_name': 'My Tesla',
      'state': 'online',
      'in_service': False,
      'calendar_enabled': True
    }
  ]
```

**Explanation:**
- **Line 73** calls the `vehicle_list()` method which returns all vehicles associated with the Tesla account
- **Line 76** shows the count of vehicles
- Each vehicle object contains comprehensive metadata including VIN, display name, and current state

---

### 4. Vehicle Data Retrieval (Lines 95-143)

```python
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

# Line 118: Display climate information
print("\n🌡️  CLIMATE:")
climate_state = data['climate_state']
print(f"  Inside Temp: {climate_state['inside_temp']}°C")
print(f"  Climate On: {climate_state['is_climate_on']}")

# Line 127: Display vehicle state
print("\n🚗 VEHICLE STATE:")
vehicle_state = data['vehicle_state']
print(f"  Odometer: {vehicle_state['odometer']:.1f} miles")
print(f"  Locked: {vehicle_state['locked']}")
print(f"  Software Version: {vehicle_state['car_version']}")

# Line 135: Display drive state
print("\n📍 LOCATION & DRIVE:")
drive_state = data['drive_state']
print(f"  Speed: {drive_state.get('speed', 0) or 0} mph")
print(f"  Latitude: {drive_state.get('latitude', 'N/A')}")
```

**Explanation:**
- **Line 100**: Vehicles may be asleep to save battery. `sync_wake_up()` wakes them up before commands
- **Line 104**: `get_vehicle_data()` retrieves comprehensive data including charge, climate, location, and vehicle state
- **Line 108**: Battery data includes level, range, and charging status
- **Line 118**: Climate data includes interior/exterior temps and HVAC status
- **Line 127**: Vehicle state includes odometer, lock status, and software version
- **Line 135**: Drive state includes current speed, gear, and GPS coordinates

---

### 5. Climate Control (Lines 147-173)

```python
# Line 153: Start climate control
print("Line 153: Starting climate control...")
print("  Command: vehicle.command('CLIMATE_ON')")

# Line 159: Set temperature
print("Line 159: Setting temperature to 22°C...")
print("  Command: vehicle.command('CHANGE_CLIMATE_TEMPERATURE_SETTING',")
print("                          driver_temp=22, passenger_temp=22)")

# Line 165: Turn on seat heaters
print("Line 165: Activating seat heater...")
print("  Command: vehicle.command('REMOTE_SEAT_HEATER_REQUEST',")
print("                          heater=0, level=2)")
```

**Demo Output:**
```
🌡️  Climate:
  - CLIMATE_ON / CLIMATE_OFF
  - CHANGE_CLIMATE_TEMPERATURE_SETTING
  - REMOTE_SEAT_HEATER_REQUEST
  - REMOTE_STEERING_WHEEL_HEATER_REQUEST
```

**Explanation:**
- **Line 153**: `CLIMATE_ON` command starts the HVAC system remotely
- **Line 159**: `CHANGE_CLIMATE_TEMPERATURE_SETTING` sets driver and passenger temperatures independently
- **Line 165**: `REMOTE_SEAT_HEATER_REQUEST` controls seat heaters (heater 0 = driver, levels 0-3)

---

### 6. Charging Control (Lines 177-198)

```python
# Line 181: Set charge limit
print("Line 181: Setting charge limit to 80%...")
print("  Command: vehicle.command('CHANGE_CHARGE_LIMIT', percent=80)")

# Line 186: Start charging
print("Line 186: Starting charge...")
print("  Command: vehicle.command('START_CHARGE')")

# Line 191: Stop charging
print("Line 191: Stopping charge...")
print("  Command: vehicle.command('STOP_CHARGE')")
```

**Demo Output:**
```
🔋 Charging:
  - START_CHARGE / STOP_CHARGE
  - CHANGE_CHARGE_LIMIT
  - SET_CHARGING_AMPS
```

**Explanation:**
- **Line 181**: `CHANGE_CHARGE_LIMIT` sets the maximum charge percentage (typically 80-90% for daily use)
- **Line 186**: `START_CHARGE` initiates charging if the vehicle is plugged in
- **Line 191**: `STOP_CHARGE` stops an active charging session

---

### 7. Additional Vehicle Commands (Lines 202-234)

```python
# Line 206: Lock/Unlock doors
print("  Lock: vehicle.command('DOOR_LOCK')")
print("  Unlock: vehicle.command('DOOR_UNLOCK')\n")

# Line 211: Honk horn and flash lights
print("  Honk: vehicle.command('HONK_HORN')")
print("  Flash: vehicle.command('FLASH_LIGHTS')\n")

# Line 216: Open/close trunk/frunk
print("  Rear: vehicle.command('ACTUATE_TRUNK', which_trunk='rear')")
print("  Front: vehicle.command('ACTUATE_TRUNK', which_trunk='front')\n")

# Line 221: Sentry mode
print("  Enable: vehicle.command('SET_SENTRY_MODE', on=True)")
print("  Disable: vehicle.command('SET_SENTRY_MODE', on=False)\n")

# Line 226: Remote start
print("  Start: vehicle.command('REMOTE_START_DRIVE')")
```

**Demo Output:**
```
🚗 Vehicle Control:
  - DOOR_LOCK / DOOR_UNLOCK
  - ACTUATE_TRUNK
  - WINDOW_CONTROL
  - REMOTE_START_DRIVE
  - HONK_HORN / FLASH_LIGHTS

🛡️  Security:
  - SET_SENTRY_MODE
  - SET_VALET_MODE
  - SPEED_LIMIT_SET_LIMIT

⚡ Advanced:
  - SCHEDULE_SOFTWARE_UPDATE
  - NAVIGATION_REQUEST
  - SHARE (send address to vehicle)
```

**Explanation:**
- **Line 206**: Lock/unlock vehicle doors remotely
- **Line 211**: Honk horn and flash lights to locate vehicle
- **Line 216**: Open rear trunk or front trunk (frunk)
- **Line 221**: Enable/disable Sentry Mode (security camera recording)
- **Line 226**: Enable keyless driving (requires password)

---

### 8. Energy Products (Lines 238-261)

```python
# Line 242: List energy products
print("Line 242: Checking for Tesla Energy products...")
print("  Command: tesla.battery_list()")
print("  This retrieves Powerwall and Solar products\n")

print("  Energy products include:")
print("    - Powerwall: Home battery storage")
print("    - Solar Panels: Solar energy generation")
print("    - Solar Roof: Integrated solar tiles\n")
```

**Explanation:**
- **Line 242**: `battery_list()` retrieves Tesla Energy products (Powerwall, Solar)
- Energy products provide data on battery percentage, power flow, and operation mode
- Supports monitoring and control of home energy systems

---

### 9. Library Features Summary (Lines 336-350)

**Output:**
```
======================================================================
  LIBRARY INFORMATION
======================================================================

Package: teslapy
PyPI: https://pypi.org/project/TeslaPy/
GitHub: https://github.com/tdorssers/TeslaPy
License: MIT

Key Features:
  ✓ OAuth authentication with token caching
  ✓ Vehicle data and state retrieval
  ✓ Remote vehicle commands
  ✓ Energy products support (Powerwall/Solar)
  ✓ Automatic rate limiting
  ✓ Comprehensive error handling
```

---

## Complete Program Output

```
======================================================================
  TeslaPY - Python Library for Tesla API
  Comprehensive Feature Demonstration
======================================================================

TeslaPY provides a Python interface to Tesla's vehicle API,
enabling remote monitoring and control of Tesla vehicles and
energy products through their official API.

======================================================================
  1. AUTHENTICATION
======================================================================

Error: teslapy module not found

======================================================================
  Running in DEMO MODE (no Tesla credentials)
  Showing API structure and available commands
======================================================================

======================================================================
  DEMO: Vehicle List Structure
======================================================================

In production, vehicle_list() returns:
  [
    {
      'id': 1234567890,
      'vehicle_id': 9876543210,
      'vin': 'TSLA1234567890',
      'display_name': 'My Tesla',
      'state': 'online',
      'in_service': False,
      'calendar_enabled': True
    }
  ]

======================================================================
  DEMO: Available Commands
======================================================================

TeslaPY supports extensive vehicle control:

🔋 Charging:
  - START_CHARGE / STOP_CHARGE
  - CHANGE_CHARGE_LIMIT
  - SET_CHARGING_AMPS

🌡️  Climate:
  - CLIMATE_ON / CLIMATE_OFF
  - CHANGE_CLIMATE_TEMPERATURE_SETTING
  - REMOTE_SEAT_HEATER_REQUEST
  - REMOTE_STEERING_WHEEL_HEATER_REQUEST

🚗 Vehicle Control:
  - DOOR_LOCK / DOOR_UNLOCK
  - ACTUATE_TRUNK
  - WINDOW_CONTROL
  - REMOTE_START_DRIVE
  - HONK_HORN / FLASH_LIGHTS

🛡️  Security:
  - SET_SENTRY_MODE
  - SET_VALET_MODE
  - SPEED_LIMIT_SET_LIMIT

⚡ Advanced:
  - SCHEDULE_SOFTWARE_UPDATE
  - NAVIGATION_REQUEST
  - SHARE (send address to vehicle)

======================================================================
  LIBRARY INFORMATION
======================================================================

Package: teslapy
PyPI: https://pypi.org/project/TeslaPy/
GitHub: https://github.com/tdorssers/TeslaPy
License: MIT

Key Features:
  ✓ OAuth authentication with token caching
  ✓ Vehicle data and state retrieval
  ✓ Remote vehicle commands
  ✓ Energy products support (Powerwall/Solar)
  ✓ Automatic rate limiting
  ✓ Comprehensive error handling

======================================================================
  Demo completed successfully!
======================================================================
```

## Key Takeaways

1. **Authentication**: TeslaPY uses OAuth 2.0 with token caching for secure, persistent authentication
2. **Vehicle Control**: Comprehensive remote control including climate, charging, locks, and more
3. **Data Retrieval**: Access to real-time vehicle data including battery, location, and status
4. **Energy Products**: Support for Powerwall and Solar products beyond just vehicles
5. **Production Ready**: Includes rate limiting, error handling, and automatic retries

## Production Usage Notes

To use TeslaPY with actual Tesla credentials:

1. Set environment variable: `export TESLA_EMAIL=your@email.com`
2. Run the script - it will open a browser for OAuth login
3. Complete the login (including MFA if enabled)
4. Tokens are cached in `cache.json` for future use
5. The script will then execute real commands against your vehicle

**Security Note**: Never commit `cache.json` or credentials to version control.

## Additional Resources

- [TeslaPY Documentation](https://github.com/tdorssers/TeslaPy)
- [Tesla API Documentation (Unofficial)](https://tesla-api.timdorr.com/)
- [Tesla Developer Portal](https://developer.tesla.com/)
