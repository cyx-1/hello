# Python Timezone-Aware Date Handling

This example demonstrates comprehensive timezone-aware date handling, date arithmetic, holiday detection, and business date calculations in Python using modern libraries.

## Overview

This demonstration showcases:
1. **Timezone-aware datetime handling** with `zoneinfo` (Python 3.9+)
2. **Date arithmetic** with `python-dateutil`
3. **Holiday detection** with the `holidays` library
4. **Business duration calculations** with `business-duration`

## Requirements

- **Python Version**: Python 3.9+ (required for `zoneinfo` module)
- **Dependencies**:
  - `python-dateutil>=2.9.0` - Advanced date manipulation
  - `holidays>=0.58` - Country-specific holiday calendars
  - `business-duration>=0.5.0` - Business day/hour calculations

## Running the Example

```bash
uv run main_timezone_date_handling.py
```

The script uses inline script metadata (PEP 723), so `uv` automatically manages dependencies.

---

## Source Code

### Script Metadata and Imports (Lines 1-26)

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "python-dateutil>=2.9.0",
#     "holidays>=0.58",
#     "business-duration>=0.5.0",
# ]
# ///

"""
Comprehensive demonstration of Python timezone-aware date handling,
date arithmetic, holiday checking, and business date calculations.

This example showcases:
1. Timezone-aware datetime handling with zoneinfo (Python 3.9+)
2. Date arithmetic with python-dateutil
3. Holiday detection with the holidays library
4. Business duration calculations with business-duration
"""

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from dateutil import rrule
from dateutil.relativedelta import relativedelta
import holidays
from business_duration import businessDuration
```

**Note**: The inline script metadata (lines 2-9) allows `uv` to automatically install and manage dependencies without requiring a separate `pyproject.toml` file.

---

## 1. Timezone-Aware Date Handling with Zoneinfo

### Source Code (Lines 36-73)

```python
def demonstrate_timezone_handling():
    """Demonstrate timezone-aware date handling with zoneinfo."""
    print_section("1. TIMEZONE-AWARE DATE HANDLING WITH ZONEINFO")

    # Create timezone-aware datetime objects
    utc_time = datetime(2025, 1, 15, 14, 30, 0, tzinfo=timezone.utc)
    print(f"Line 42: UTC time: {utc_time}")
    print(f"Line 43: ISO format: {utc_time.isoformat()}")

    # Convert to different timezones
    ny_tz = ZoneInfo("America/New_York")
    tokyo_tz = ZoneInfo("Asia/Tokyo")
    london_tz = ZoneInfo("Europe/London")

    ny_time = utc_time.astimezone(ny_tz)
    tokyo_time = utc_time.astimezone(tokyo_tz)
    london_time = utc_time.astimezone(london_tz)

    print(f"\nLine 55: Same moment in different timezones:")
    print(f"Line 56:   New York: {ny_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Line 57:   Tokyo:    {tokyo_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Line 58:   London:   {london_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

    # Demonstrate DST (Daylight Saving Time) handling
    print(f"\nLine 61: Daylight Saving Time handling:")
    summer_date = datetime(2025, 7, 15, 12, 0, tzinfo=ny_tz)
    winter_date = datetime(2025, 1, 15, 12, 0, tzinfo=ny_tz)

    print(f"Line 65: Summer (EDT): {summer_date.strftime('%Y-%m-%d %H:%M:%S %Z')} (UTC offset: {summer_date.strftime('%z')})")
    print(f"Line 66: Winter (EST): {winter_date.strftime('%Y-%m-%d %H:%M:%S %Z')} (UTC offset: {winter_date.strftime('%z')})")

    # Create timezone-aware datetime from naive datetime
    naive_dt = datetime(2025, 3, 15, 10, 30)
    aware_dt = naive_dt.replace(tzinfo=ZoneInfo("US/Pacific"))
    print(f"\nLine 71: Converting naive to aware datetime:")
    print(f"Line 72:   Naive:  {naive_dt}")
    print(f"Line 73:   Aware:  {aware_dt}")
```

### Output

```
================================================================================
  1. TIMEZONE-AWARE DATE HANDLING WITH ZONEINFO
================================================================================
Line 42: UTC time: 2025-01-15 14:30:00+00:00
Line 43: ISO format: 2025-01-15T14:30:00+00:00

Line 55: Same moment in different timezones:
Line 56:   New York: 2025-01-15 09:30:00 EST
Line 57:   Tokyo:    2025-01-15 23:30:00 JST
Line 58:   London:   2025-01-15 14:30:00 GMT

Line 61: Daylight Saving Time handling:
Line 65: Summer (EDT): 2025-07-15 12:00:00 EDT (UTC offset: -0400)
Line 66: Winter (EST): 2025-01-15 12:00:00 EST (UTC offset: -0500)

Line 71: Converting naive to aware datetime:
Line 72:   Naive:  2025-03-15 10:30:00
Line 73:   Aware:  2025-03-15 10:30:00-07:00
```

### Key Observations

- **Lines 42-43**: Creating a timezone-aware datetime using `timezone.utc` produces an ISO 8601 formatted string with the `+00:00` UTC offset indicator.

- **Lines 56-58**: The same UTC moment (14:30) appears as:
  - 09:30 in New York (5 hours behind, EST timezone)
  - 23:30 in Tokyo (9 hours ahead, JST timezone)
  - 14:30 in London (same as UTC, GMT timezone)

- **Lines 65-66**: The `zoneinfo` module automatically handles Daylight Saving Time (DST):
  - Summer uses EDT (Eastern Daylight Time) with -04:00 offset
  - Winter uses EST (Eastern Standard Time) with -05:00 offset

- **Lines 72-73**: Converting naive datetime to timezone-aware using `.replace(tzinfo=...)` adds timezone information. The US/Pacific timezone shows -07:00 offset (PST).

---

## 2. Date Arithmetic with python-dateutil

### Source Code (Lines 76-119)

```python
def demonstrate_date_arithmetic():
    """Demonstrate date arithmetic with python-dateutil."""
    print_section("2. DATE ARITHMETIC WITH PYTHON-DATEUTIL")

    base_date = datetime(2025, 1, 31, 10, 0, tzinfo=timezone.utc)
    print(f"Line 82: Base date: {base_date.strftime('%Y-%m-%d %H:%M:%S %Z')}")

    # Using relativedelta for intelligent date arithmetic
    print(f"\nLine 85: Adding periods with relativedelta:")
    one_month_later = base_date + relativedelta(months=1)
    print(f"Line 87:   +1 month:  {one_month_later.strftime('%Y-%m-%d')} (handles end-of-month correctly)")

    three_months_later = base_date + relativedelta(months=3)
    print(f"Line 90:   +3 months: {three_months_later.strftime('%Y-%m-%d')}")

    one_year_later = base_date + relativedelta(years=1)
    print(f"Line 93:   +1 year:   {one_year_later.strftime('%Y-%m-%d')}")

    # Complex date arithmetic
    complex_delta = base_date + relativedelta(years=1, months=2, days=3, hours=4, minutes=5)
    print(f"Line 97:   +1y 2m 3d 4h 5min: {complex_delta.strftime('%Y-%m-%d %H:%M:%S')}")

    # Relative date calculations
    print(f"\nLine 100: Relative date calculations:")
    next_friday = base_date + relativedelta(weekday=rrule.FR)
    print(f"Line 102:   Next Friday: {next_friday.strftime('%Y-%m-%d %A')}")

    last_day_of_month = base_date + relativedelta(day=31)
    print(f"Line 105:   Last day of month: {last_day_of_month.strftime('%Y-%m-%d')}")

    # Date difference calculation
    start_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(2025, 12, 31, tzinfo=timezone.utc)
    delta = relativedelta(end_date, start_date)
    print(f"\nLine 111: Date difference between {start_date.date()} and {end_date.date()}:")
    print(f"Line 112:   {delta.years} years, {delta.months} months, {delta.days} days")

    # Generate recurring dates with rrule
    print(f"\nLine 115: Recurring dates (first 5 Mondays from {base_date.date()}):")
    mondays = rrule.rrule(rrule.WEEKLY, byweekday=rrule.MO, dtstart=base_date, count=5)
    for idx, monday in enumerate(mondays, 1):
        print(f"Line 118:   {idx}. {monday.strftime('%Y-%m-%d %A')}")
```

### Output

```
================================================================================
  2. DATE ARITHMETIC WITH PYTHON-DATEUTIL
================================================================================
Line 82: Base date: 2025-01-31 10:00:00 UTC

Line 85: Adding periods with relativedelta:
Line 87:   +1 month:  2025-02-28 (handles end-of-month correctly)
Line 90:   +3 months: 2025-04-30
Line 93:   +1 year:   2026-01-31
Line 97:   +1y 2m 3d 4h 5min: 2026-04-03 14:05:00

Line 100: Relative date calculations:
Line 102:   Next Friday: 2025-01-31 Friday
Line 105:   Last day of month: 2025-01-31

Line 111: Date difference between 2025-01-01 and 2025-12-31:
Line 112:   0 years, 11 months, 30 days

Line 115: Recurring dates (first 5 Mondays from 2025-01-31):
Line 118:   1. 2025-02-03 Monday
Line 118:   2. 2025-02-10 Monday
Line 118:   3. 2025-02-17 Monday
Line 118:   4. 2025-02-24 Monday
Line 118:   5. 2025-03-03 Monday
```

### Key Observations

- **Line 87**: The `relativedelta` intelligently handles month-end dates. Adding 1 month to January 31st results in February 28th (not an error), demonstrating proper end-of-month handling.

- **Line 90**: Adding 3 months to January 31st gives April 30th (the last day of April), showing consistent month-end behavior.

- **Line 93**: Adding 1 year to January 31st, 2025 correctly produces January 31st, 2026.

- **Line 97**: Complex date arithmetic combining years, months, days, hours, and minutes in a single operation: `2025-01-31 10:00:00` + 1y 2m 3d 4h 5min = `2026-04-03 14:05:00`.

- **Line 102**: Using `weekday=rrule.FR` finds the next Friday. Since January 31st, 2025 is already a Friday, it returns the same date.

- **Line 112**: The difference between January 1st and December 31st, 2025 is represented as "0 years, 11 months, 30 days" rather than just "364 days", providing more semantic meaning.

- **Lines 118**: The `rrule` module generates recurring dates. Starting from January 31st (Friday), the next 5 Mondays are: Feb 3, Feb 10, Feb 17, Feb 24, and Mar 3.

---

## 3. Holiday Detection with Holidays Library

### Source Code (Lines 122-165)

```python
def demonstrate_holiday_handling():
    """Demonstrate holiday detection with the holidays library."""
    print_section("3. HOLIDAY DETECTION WITH HOLIDAYS LIBRARY")

    # US holidays
    us_holidays = holidays.US(years=2025)
    print(f"Line 127: US Federal Holidays in 2025:")
    for date, name in sorted(us_holidays.items())[:10]:
        print(f"Line 129:   {date}: {name}")

    # Check specific dates
    print(f"\nLine 132: Checking specific dates:")
    test_dates = [
        datetime(2025, 1, 1),   # New Year's Day
        datetime(2025, 7, 4),   # Independence Day
        datetime(2025, 12, 25), # Christmas
        datetime(2025, 3, 15),  # Regular day
    ]

    for test_date in test_dates:
        is_holiday = test_date.date() in us_holidays
        holiday_name = us_holidays.get(test_date.date(), "Not a holiday")
        print(f"Line 143:   {test_date.date()}: {holiday_name} (is_holiday={is_holiday})")

    # Multiple countries
    print(f"\nLine 146: Holidays in different countries on 2025-05-01:")
    countries = {
        'US': holidays.US(),
        'UK': holidays.UK(),
        'JP': holidays.JP(),
        'IN': holidays.IN(),
    }

    may_first = datetime(2025, 5, 1).date()
    for country_code, country_holidays in countries.items():
        holiday_name = country_holidays.get(may_first, "Not a holiday")
        print(f"Line 157:   {country_code}: {holiday_name}")

    # State-specific holidays (e.g., California)
    ca_holidays = holidays.US(state='CA', years=2025)
    print(f"\nLine 161: California-specific holidays:")
    ca_only = set(ca_holidays.keys()) - set(us_holidays.keys())
    for date in sorted(ca_only)[:5]:
        print(f"Line 164:   {date}: {ca_holidays[date]}")
```

### Output

```
================================================================================
  3. HOLIDAY DETECTION WITH HOLIDAYS LIBRARY
================================================================================
Line 127: US Federal Holidays in 2025:
Line 129:   2025-01-01: New Year's Day
Line 129:   2025-01-20: Martin Luther King Jr. Day
Line 129:   2025-02-17: Washington's Birthday
Line 129:   2025-05-26: Memorial Day
Line 129:   2025-06-19: Juneteenth National Independence Day
Line 129:   2025-07-04: Independence Day
Line 129:   2025-09-01: Labor Day
Line 129:   2025-10-13: Columbus Day
Line 129:   2025-11-11: Veterans Day
Line 129:   2025-11-27: Thanksgiving Day

Line 132: Checking specific dates:
Line 143:   2025-01-01: New Year's Day (is_holiday=True)
Line 143:   2025-07-04: Independence Day (is_holiday=True)
Line 143:   2025-12-25: Christmas Day (is_holiday=True)
Line 143:   2025-03-15: Not a holiday (is_holiday=False)

Line 146: Holidays in different countries on 2025-05-01:
Line 157:   US: Not a holiday
Line 157:   UK: Not a holiday
Line 157:   JP: Not a holiday
Line 157:   IN: Not a holiday

Line 161: California-specific holidays:
Line 164:   2025-02-15: Susan B. Anthony Day
Line 164:   2025-03-31: Cesar Chavez Day
Line 164:   2025-11-28: Day After Thanksgiving
```

### Key Observations

- **Line 129**: The `holidays` library includes 11 US federal holidays for 2025, including modern additions like Juneteenth (June 19th, established in 2021).

- **Lines 143**: The library correctly identifies:
  - January 1st as New Year's Day
  - July 4th as Independence Day
  - December 25th as Christmas Day
  - March 15th as not a holiday

- **Line 157**: May 1st (International Workers' Day / May Day) is not a federal holiday in the US, UK, Japan, or India according to the library's default settings. This demonstrates how holidays vary by country.

- **Lines 164**: California has state-specific holidays beyond federal holidays:
  - **Susan B. Anthony Day** (February 15th) - honors women's suffrage
  - **Cesar Chavez Day** (March 31st) - honors the labor leader
  - **Day After Thanksgiving** (November 28th) - additional state holiday

---

## 4. Business Duration Calculations

### Source Code (Lines 168-244)

```python
def demonstrate_business_duration():
    """Demonstrate business duration calculations."""
    print_section("4. BUSINESS DURATION CALCULATIONS")

    # Configure business hours (Monday-Friday, 9 AM - 5 PM)
    unit_config = {
        'HOLIDAY': 0,      # No work on holidays
        'WEEKEND': 0,      # No work on weekends
        'WEEK': 5,         # 5 working days per week
        'WORKDAY': 8,      # 8 hours per working day
    }

    # Define US holidays
    us_holidays_2025 = holidays.US(years=2025)
    holiday_list = [date for date in us_holidays_2025.keys()]

    print(f"Line 183: Business duration configuration:")
    print(f"Line 184:   Work week: Monday-Friday")
    print(f"Line 185:   Work hours: 9:00 AM - 5:00 PM (8 hours/day)")
    print(f"Line 186:   Holidays: {len(holiday_list)} US federal holidays")

    # Calculate business days between dates
    start = datetime(2025, 1, 2, 9, 0)  # Thursday
    end = datetime(2025, 1, 10, 17, 0)  # Next Friday

    print(f"\nLine 192: Calculate business days:")
    print(f"Line 193:   Start: {start.strftime('%Y-%m-%d %A %H:%M')}")
    print(f"Line 194:   End:   {end.strftime('%Y-%m-%d %A %H:%M')}")

    # Calculate duration
    duration_hours = businessDuration(
        start, end,
        starttime=datetime.strptime('09:00', '%H:%M').time(),
        endtime=datetime.strptime('17:00', '%H:%M').time(),
        holidaylist=holiday_list,
        unit='hour'
    )

    duration_days = duration_hours / 8  # Convert to business days
    print(f"Line 206:   Business hours: {duration_hours}")
    print(f"Line 207:   Business days: {duration_days}")

    # Calculate business hours across a week with holiday
    print(f"\nLine 210: Business hours over week including holiday:")
    holiday_start = datetime(2025, 12, 24, 9, 0)  # Day before Christmas
    holiday_end = datetime(2025, 12, 26, 17, 0)   # Day after Christmas

    print(f"Line 214:   Start: {holiday_start.strftime('%Y-%m-%d %A')} (before Christmas)")
    print(f"Line 215:   End:   {holiday_end.strftime('%Y-%m-%d %A')} (after Christmas)")

    holiday_duration = businessDuration(
        holiday_start, holiday_end,
        starttime=datetime.strptime('09:00', '%H:%M').time(),
        endtime=datetime.strptime('17:00', '%H:%M').time(),
        holidaylist=holiday_list,
        unit='hour'
    )

    print(f"Line 224:   Business hours: {holiday_duration} (excludes Christmas Day)")

    # Working with timezone-aware datetimes
    print(f"\nLine 227: Business hours with timezone-aware datetimes:")
    ny_tz = ZoneInfo("America/New_York")
    tz_start = datetime(2025, 2, 3, 9, 0, tzinfo=ny_tz)
    tz_end = datetime(2025, 2, 7, 17, 0, tzinfo=ny_tz)

    print(f"Line 232:   Start: {tz_start.strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"Line 233:   End:   {tz_end.strftime('%Y-%m-%d %H:%M %Z')}")

    # Convert to naive for business_duration (it expects naive datetimes)
    tz_duration = businessDuration(
        tz_start.replace(tzinfo=None), tz_end.replace(tzinfo=None),
        starttime=datetime.strptime('09:00', '%H:%M').time(),
        endtime=datetime.strptime('17:00', '%H:%M').time(),
        holidaylist=holiday_list,
        unit='hour'
    )

    print(f"Line 243:   Business hours: {tz_duration}")
```

### Output

```
================================================================================
  4. BUSINESS DURATION CALCULATIONS
================================================================================
Line 183: Business duration configuration:
Line 184:   Work week: Monday-Friday
Line 185:   Work hours: 9:00 AM - 5:00 PM (8 hours/day)
Line 186:   Holidays: 11 US federal holidays

Line 192: Calculate business days:
Line 193:   Start: 2025-01-02 Thursday 09:00
Line 194:   End:   2025-01-10 Friday 17:00
Line 206:   Business hours: 56.0
Line 207:   Business days: 7.0

Line 210: Business hours over week including holiday:
Line 214:   Start: 2025-12-24 Wednesday (before Christmas)
Line 215:   End:   2025-12-26 Friday (after Christmas)
Line 224:   Business hours: 16.0 (excludes Christmas Day)

Line 227: Business hours with timezone-aware datetimes:
Line 232:   Start: 2025-02-03 09:00 EST
Line 233:   End:   2025-02-07 17:00 EST
Line 243:   Business hours: 40.0
```

### Key Observations

- **Line 186**: The configuration uses 11 US federal holidays for 2025, automatically excluding them from business hour calculations.

- **Lines 206-207**: From Thursday, January 2nd at 9 AM to Friday, January 10th at 5 PM:
  - **Calendar span**: 8 days
  - **Business hours**: 56.0 hours (excludes weekend: Saturday Jan 4-5 and Sunday Jan 5-6)
  - **Business days**: 7.0 days
  - Calculation: Thu (8h) + Fri (8h) + Mon (8h) + Tue (8h) + Wed (8h) + Thu (8h) + Fri (8h) = 56 hours

- **Line 224**: From December 24th (Wednesday) to December 26th (Friday):
  - **Business hours**: 16.0 hours
  - **Calculation**: Wed 12/24 (8h) + Christmas 12/25 (0h, holiday) + Fri 12/26 (8h) = 16 hours
  - This demonstrates that the library correctly excludes Christmas Day from the business hour count.

- **Line 243**: From Monday, February 3rd to Friday, February 7th (5-day work week):
  - **Business hours**: 40.0 hours (5 days × 8 hours/day)
  - This example shows that timezone-aware datetimes can be used by converting them to naive datetimes (the `business_duration` library expects naive datetimes).

---

## Summary

This example demonstrates the powerful capabilities of Python's date and time handling libraries:

1. **zoneinfo**: Built into Python 3.9+, provides robust timezone support with automatic DST handling
2. **python-dateutil**: Offers intelligent date arithmetic that handles edge cases like month-end dates
3. **holidays**: Maintains comprehensive holiday calendars for multiple countries and regions
4. **business-duration**: Calculates business hours/days while respecting weekends and holidays

These libraries work together to handle real-world date/time requirements in business applications, scheduling systems, and international software.
