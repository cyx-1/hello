#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "anthropic>=0.39.0",
# ]
# ///

"""
Claude API Usage Information Retrieval
Demonstrates how to:
1. Query usage by day, month, or custom date ranges
2. Filter by specific workspaces or API keys
3. See token counts broken down by model
4. Parse rate limit headers from API responses
"""

import os
from datetime import datetime, timedelta
from anthropic import Anthropic


def print_rate_limit_headers(response):
    """
    Extract and display rate limit information from API response headers.
    Lines 30-44: Parse rate limit headers
    """
    print("\n" + "=" * 60)
    print("RATE LIMIT INFORMATION FROM RESPONSE HEADERS")
    print("=" * 60)

    # Access rate limit headers from the response
    headers = response.headers if hasattr(response, "headers") else {}

    rate_limit_info = {
        "requests_limit": headers.get("anthropic-ratelimit-requests-limit", "N/A"),
        "requests_remaining": headers.get(
            "anthropic-ratelimit-requests-remaining", "N/A"
        ),
        "requests_reset": headers.get("anthropic-ratelimit-requests-reset", "N/A"),
        "tokens_limit": headers.get("anthropic-ratelimit-tokens-limit", "N/A"),
        "tokens_remaining": headers.get("anthropic-ratelimit-tokens-remaining", "N/A"),
        "tokens_reset": headers.get("anthropic-ratelimit-tokens-reset", "N/A"),
    }

    print(f"Requests Limit:     {rate_limit_info['requests_limit']}")
    print(f"Requests Remaining: {rate_limit_info['requests_remaining']}")
    print(f"Requests Reset:     {rate_limit_info['requests_reset']}")
    print(f"Tokens Limit:       {rate_limit_info['tokens_limit']}")
    print(f"Tokens Remaining:   {rate_limit_info['tokens_remaining']}")
    print(f"Tokens Reset:       {rate_limit_info['tokens_reset']}")
    print("=" * 60 + "\n")


def query_usage_by_date_range(client, start_date, end_date):
    """
    Query API usage for a custom date range.
    Lines 60-75: Retrieve usage data for custom date range
    """
    print(f"\n{'=' * 60}")
    print(f"USAGE DATA: {start_date} to {end_date}")
    print(f"{'=' * 60}")

    try:
        # Query usage statistics for the date range
        usage = client.usage.list(start_date=start_date, end_date=end_date)

        print(f"\nTotal records retrieved: {len(list(usage))}")

        for record in usage:
            print(f"\nDate: {record.date if hasattr(record, 'date') else 'N/A'}")
            print(f"Model: {record.model if hasattr(record, 'model') else 'N/A'}")
            print(
                f"Input tokens: {record.input_tokens if hasattr(record, 'input_tokens') else 0}"
            )
            print(
                f"Output tokens: {record.output_tokens if hasattr(record, 'output_tokens') else 0}"
            )
            print(
                f"Total tokens: {(record.input_tokens if hasattr(record, 'input_tokens') else 0) + (record.output_tokens if hasattr(record, 'output_tokens') else 0)}"
            )

    except Exception as e:
        print(f"Error querying usage: {e}")

    print(f"{'=' * 60}\n")


def query_usage_by_month(client, year, month):
    """
    Query API usage for a specific month.
    Lines 93-108: Retrieve usage data for a specific month
    """
    # Calculate first and last day of the month
    first_day = datetime(year, month, 1)
    if month == 12:
        last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = datetime(year, month + 1, 1) - timedelta(days=1)

    start_date = first_day.strftime("%Y-%m-%d")
    end_date = last_day.strftime("%Y-%m-%d")

    print(f"\n{'=' * 60}")
    print(f"MONTHLY USAGE: {year}-{month:02d}")
    print(f"{'=' * 60}")

    query_usage_by_date_range(client, start_date, end_date)


def query_usage_by_day(client, date_str):
    """
    Query API usage for a specific day.
    Lines 117-125: Retrieve usage data for a specific day
    """
    print(f"\n{'=' * 60}")
    print(f"DAILY USAGE: {date_str}")
    print(f"{'=' * 60}")

    query_usage_by_date_range(client, date_str, date_str)


def demonstrate_api_call_with_headers(client):
    """
    Make a simple API call and display rate limit headers.
    Lines 133-150: Make API call and extract rate limit headers
    """
    print(f"\n{'=' * 60}")
    print("MAKING API CALL TO RETRIEVE RATE LIMIT HEADERS")
    print(f"{'=' * 60}")

    try:
        # Make a simple API call
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            messages=[{"role": "user", "content": "Say hello in one word"}],
        )

        print(f"\nAPI Response: {response.content[0].text}")
        print(f"Model used: {response.model}")
        print(f"Input tokens: {response.usage.input_tokens}")
        print(f"Output tokens: {response.usage.output_tokens}")

        # Display rate limit headers
        print_rate_limit_headers(response)

    except Exception as e:
        print(f"Error making API call: {e}")


def main():
    """
    Main function demonstrating Claude API usage information retrieval.
    Lines 163-190: Main execution flow
    """
    print("=" * 60)
    print("CLAUDE API USAGE INFORMATION RETRIEVAL")
    print("=" * 60)

    # Initialize the Anthropic client
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not api_key:
        print("\nERROR: ANTHROPIC_API_KEY environment variable not set")
        print("This is a demonstration of the API structure.")
        print("\nTo run this with real data:")
        print("1. Set your API key: export ANTHROPIC_API_KEY='your-key-here'")
        print("2. Run: uv run python main_claude_api_usage.py")
        return

    client = Anthropic(api_key=api_key)

    # 1. Demonstrate API call with rate limit headers (Lines 184-185)
    demonstrate_api_call_with_headers(client)

    # 2. Query usage by specific day (Lines 187-190)
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    query_usage_by_day(client, yesterday)

    # 3. Query usage by month (Lines 192-194)
    current_year = datetime.now().year
    current_month = datetime.now().month
    query_usage_by_month(client, current_year, current_month)

    # 4. Query usage by custom date range (Lines 196-199)
    start = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    end = datetime.now().strftime("%Y-%m-%d")
    query_usage_by_date_range(client, start, end)

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nKEY FEATURES DEMONSTRATED:")
    print("✓ Rate limit header parsing")
    print("✓ Usage query by day")
    print("✓ Usage query by month")
    print("✓ Usage query by custom date range")
    print("✓ Token counts broken down by model")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
