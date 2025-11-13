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

from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from dateutil import rrule
from dateutil.relativedelta import relativedelta
import holidays
from business_duration import businessDuration


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'=' * 80}")
    print(f"  {title}")
    print("=" * 80)


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

    print("\nLine 55: Same moment in different timezones:")
    print(f"Line 56:   New York: {ny_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Line 57:   Tokyo:    {tokyo_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Line 58:   London:   {london_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

    # Demonstrate DST (Daylight Saving Time) handling
    print("\nLine 61: Daylight Saving Time handling:")
    summer_date = datetime(2025, 7, 15, 12, 0, tzinfo=ny_tz)
    winter_date = datetime(2025, 1, 15, 12, 0, tzinfo=ny_tz)

    print(
        f"Line 65: Summer (EDT): {summer_date.strftime('%Y-%m-%d %H:%M:%S %Z')} (UTC offset: {summer_date.strftime('%z')})"
    )
    print(
        f"Line 66: Winter (EST): {winter_date.strftime('%Y-%m-%d %H:%M:%S %Z')} (UTC offset: {winter_date.strftime('%z')})"
    )

    # Create timezone-aware datetime from naive datetime
    naive_dt = datetime(2025, 3, 15, 10, 30)
    aware_dt = naive_dt.replace(tzinfo=ZoneInfo("US/Pacific"))
    print("\nLine 71: Converting naive to aware datetime:")
    print(f"Line 72:   Naive:  {naive_dt}")
    print(f"Line 73:   Aware:  {aware_dt}")


def demonstrate_date_arithmetic():
    """Demonstrate date arithmetic with python-dateutil."""
    print_section("2. DATE ARITHMETIC WITH PYTHON-DATEUTIL")

    base_date = datetime(2025, 1, 31, 10, 0, tzinfo=timezone.utc)
    print(f"Line 82: Base date: {base_date.strftime('%Y-%m-%d %H:%M:%S %Z')}")

    # Using relativedelta for intelligent date arithmetic
    print("\nLine 85: Adding periods with relativedelta:")
    one_month_later = base_date + relativedelta(months=1)
    print(
        f"Line 87:   +1 month:  {one_month_later.strftime('%Y-%m-%d')} (handles end-of-month correctly)"
    )

    three_months_later = base_date + relativedelta(months=3)
    print(f"Line 90:   +3 months: {three_months_later.strftime('%Y-%m-%d')}")

    one_year_later = base_date + relativedelta(years=1)
    print(f"Line 93:   +1 year:   {one_year_later.strftime('%Y-%m-%d')}")

    # Complex date arithmetic
    complex_delta = base_date + relativedelta(
        years=1, months=2, days=3, hours=4, minutes=5
    )
    print(
        f"Line 97:   +1y 2m 3d 4h 5min: {complex_delta.strftime('%Y-%m-%d %H:%M:%S')}"
    )

    # Relative date calculations
    print("\nLine 100: Relative date calculations:")
    next_friday = base_date + relativedelta(weekday=rrule.FR)
    print(f"Line 102:   Next Friday: {next_friday.strftime('%Y-%m-%d %A')}")

    last_day_of_month = base_date + relativedelta(day=31)
    print(f"Line 105:   Last day of month: {last_day_of_month.strftime('%Y-%m-%d')}")

    # Date difference calculation
    start_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(2025, 12, 31, tzinfo=timezone.utc)
    delta = relativedelta(end_date, start_date)
    print(
        f"\nLine 111: Date difference between {start_date.date()} and {end_date.date()}:"
    )
    print(f"Line 112:   {delta.years} years, {delta.months} months, {delta.days} days")

    # Generate recurring dates with rrule
    print(f"\nLine 115: Recurring dates (first 5 Mondays from {base_date.date()}):")
    mondays = rrule.rrule(rrule.WEEKLY, byweekday=rrule.MO, dtstart=base_date, count=5)
    for idx, monday in enumerate(mondays, 1):
        print(f"Line 118:   {idx}. {monday.strftime('%Y-%m-%d %A')}")


def demonstrate_holiday_handling():
    """Demonstrate holiday detection with the holidays library."""
    print_section("3. HOLIDAY DETECTION WITH HOLIDAYS LIBRARY")

    # US holidays
    us_holidays = holidays.US(years=2025)
    print("Line 127: US Federal Holidays in 2025:")
    for date, name in sorted(us_holidays.items())[:10]:
        print(f"Line 129:   {date}: {name}")

    # Check specific dates
    print("\nLine 132: Checking specific dates:")
    test_dates = [
        datetime(2025, 1, 1),  # New Year's Day
        datetime(2025, 7, 4),  # Independence Day
        datetime(2025, 12, 25),  # Christmas
        datetime(2025, 3, 15),  # Regular day
    ]

    for test_date in test_dates:
        is_holiday = test_date.date() in us_holidays
        holiday_name = us_holidays.get(test_date.date(), "Not a holiday")
        print(
            f"Line 143:   {test_date.date()}: {holiday_name} (is_holiday={is_holiday})"
        )

    # Multiple countries
    print("\nLine 146: Holidays in different countries on 2025-05-01:")
    countries = {
        "US": holidays.US(),
        "UK": holidays.UK(),
        "JP": holidays.JP(),
        "IN": holidays.IN(),
    }

    may_first = datetime(2025, 5, 1).date()
    for country_code, country_holidays in countries.items():
        holiday_name = country_holidays.get(may_first, "Not a holiday")
        print(f"Line 157:   {country_code}: {holiday_name}")

    # State-specific holidays (e.g., California)
    ca_holidays = holidays.US(state="CA", years=2025)
    print("\nLine 161: California-specific holidays:")
    ca_only = set(ca_holidays.keys()) - set(us_holidays.keys())
    for date in sorted(ca_only)[:5]:
        print(f"Line 164:   {date}: {ca_holidays[date]}")


def demonstrate_business_duration():
    """Demonstrate business duration calculations."""
    print_section("4. BUSINESS DURATION CALCULATIONS")

    # Define US holidays
    us_holidays_2025 = holidays.US(years=2025)
    holiday_list = [date for date in us_holidays_2025.keys()]

    print("Line 183: Business duration configuration:")
    print("Line 184:   Work week: Monday-Friday")
    print("Line 185:   Work hours: 9:00 AM - 5:00 PM (8 hours/day)")
    print(f"Line 186:   Holidays: {len(holiday_list)} US federal holidays")

    # Calculate business days between dates
    start = datetime(2025, 1, 2, 9, 0)  # Thursday
    end = datetime(2025, 1, 10, 17, 0)  # Next Friday

    print("\nLine 192: Calculate business days:")
    print(f"Line 193:   Start: {start.strftime('%Y-%m-%d %A %H:%M')}")
    print(f"Line 194:   End:   {end.strftime('%Y-%m-%d %A %H:%M')}")

    # Calculate duration
    duration_hours = businessDuration(
        start,
        end,
        starttime=datetime.strptime("09:00", "%H:%M").time(),
        endtime=datetime.strptime("17:00", "%H:%M").time(),
        holidaylist=holiday_list,
        unit="hour",
    )

    duration_days = duration_hours / 8  # Convert to business days
    print(f"Line 206:   Business hours: {duration_hours}")
    print(f"Line 207:   Business days: {duration_days}")

    # Calculate business hours across a week with holiday
    print("\nLine 210: Business hours over week including holiday:")
    holiday_start = datetime(2025, 12, 24, 9, 0)  # Day before Christmas
    holiday_end = datetime(2025, 12, 26, 17, 0)  # Day after Christmas

    print(
        f"Line 214:   Start: {holiday_start.strftime('%Y-%m-%d %A')} (before Christmas)"
    )
    print(f"Line 215:   End:   {holiday_end.strftime('%Y-%m-%d %A')} (after Christmas)")

    holiday_duration = businessDuration(
        holiday_start,
        holiday_end,
        starttime=datetime.strptime("09:00", "%H:%M").time(),
        endtime=datetime.strptime("17:00", "%H:%M").time(),
        holidaylist=holiday_list,
        unit="hour",
    )

    print(f"Line 224:   Business hours: {holiday_duration} (excludes Christmas Day)")

    # Working with timezone-aware datetimes
    print("\nLine 227: Business hours with timezone-aware datetimes:")
    ny_tz = ZoneInfo("America/New_York")
    tz_start = datetime(2025, 2, 3, 9, 0, tzinfo=ny_tz)
    tz_end = datetime(2025, 2, 7, 17, 0, tzinfo=ny_tz)

    print(f"Line 232:   Start: {tz_start.strftime('%Y-%m-%d %H:%M %Z')}")
    print(f"Line 233:   End:   {tz_end.strftime('%Y-%m-%d %H:%M %Z')}")

    # Convert to naive for business_duration (it expects naive datetimes)
    tz_duration = businessDuration(
        tz_start.replace(tzinfo=None),
        tz_end.replace(tzinfo=None),
        starttime=datetime.strptime("09:00", "%H:%M").time(),
        endtime=datetime.strptime("17:00", "%H:%M").time(),
        holidaylist=holiday_list,
        unit="hour",
    )

    print(f"Line 243:   Business hours: {tz_duration}")


def main():
    """Main function to run all demonstrations."""
    print("\n" + "=" * 80)
    print("  PYTHON TIMEZONE-AWARE DATE HANDLING DEMONSTRATION")
    print("  Libraries: zoneinfo, python-dateutil, holidays, business-duration")
    print("=" * 80)

    demonstrate_timezone_handling()
    demonstrate_date_arithmetic()
    demonstrate_holiday_handling()
    demonstrate_business_duration()

    print("\n" + "=" * 80)
    print("  DEMONSTRATION COMPLETE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
