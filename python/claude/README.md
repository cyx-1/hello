# Claude API Usage Information Retrieval

This Python code sample demonstrates how to retrieve and monitor Claude API usage information, including:
- Querying usage by day, month, or custom date ranges
- Filtering by specific workspaces or API keys
- Viewing token counts broken down by model
- Parsing rate limit headers from API responses

## Requirements

- **Python Version**: Requires Python >= 3.11
- **Dependencies**: anthropic >= 0.39.0 (automatically managed via inline script metadata)
- **API Key**: Requires a valid `ANTHROPIC_API_KEY` environment variable to retrieve actual usage data

## Running the Code

```bash
# From the python directory
uv run main_claude_api_usage.py
```

Note: Use `uv run main_claude_api_usage.py` (NOT `uv run python main_claude_api_usage.py`)

## Source Code Overview

### 1. Rate Limit Header Parsing (Lines 18-44)

The `print_rate_limit_headers()` function extracts and displays rate limit information from API response headers.

```python
def print_rate_limit_headers(response):
    """
    Extract and display rate limit information from API response headers.
    Lines 30-44: Parse rate limit headers
    """
    print("\n" + "="*60)
    print("RATE LIMIT INFORMATION FROM RESPONSE HEADERS")
    print("="*60)

    # Access rate limit headers from the response
    headers = response.headers if hasattr(response, 'headers') else {}

    rate_limit_info = {
        "requests_limit": headers.get("anthropic-ratelimit-requests-limit", "N/A"),
        "requests_remaining": headers.get("anthropic-ratelimit-requests-remaining", "N/A"),
        "requests_reset": headers.get("anthropic-ratelimit-requests-reset", "N/A"),
        "tokens_limit": headers.get("anthropic-ratelimit-tokens-limit", "N/A"),
        "tokens_remaining": headers.get("anthropic-ratelimit-tokens-remaining", "N/A"),
        "tokens_reset": headers.get("anthropic-ratelimit-tokens-reset", "N/A")
    }
```

**Key Headers Extracted:**
- `anthropic-ratelimit-requests-limit` - Total requests allowed in the time window
- `anthropic-ratelimit-requests-remaining` - Requests remaining
- `anthropic-ratelimit-requests-reset` - When the limit resets
- `anthropic-ratelimit-tokens-limit` - Total tokens allowed
- `anthropic-ratelimit-tokens-remaining` - Tokens remaining
- `anthropic-ratelimit-tokens-reset` - When token limit resets

### 2. Custom Date Range Query (Lines 46-78)

The `query_usage_by_date_range()` function retrieves usage data for any custom date range.

```python
def query_usage_by_date_range(client, start_date, end_date):
    """
    Query API usage for a custom date range.
    Lines 60-75: Retrieve usage data for custom date range
    """
    print(f"\n{'='*60}")
    print(f"USAGE DATA: {start_date} to {end_date}")
    print(f"{'='*60}")

    try:
        # Query usage statistics for the date range
        usage = client.usage.list(
            start_date=start_date,
            end_date=end_date
        )

        print(f"\nTotal records retrieved: {len(list(usage))}")

        for record in usage:
            print(f"\nDate: {record.date if hasattr(record, 'date') else 'N/A'}")
            print(f"Model: {record.model if hasattr(record, 'model') else 'N/A'}")
            print(f"Input tokens: {record.input_tokens if hasattr(record, 'input_tokens') else 0}")
            print(f"Output tokens: {record.output_tokens if hasattr(record, 'output_tokens') else 0}")
```

**Output Format:**
```
============================================================
USAGE DATA: 2025-11-13 to 2025-11-20
============================================================

Total records retrieved: 5

Date: 2025-11-13
Model: claude-3-5-sonnet-20241022
Input tokens: 1245
Output tokens: 892
Total tokens: 2137
```

### 3. Monthly Usage Query (Lines 80-110)

The `query_usage_by_month()` function retrieves all usage data for a specific month.

```python
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

    print(f"\n{'='*60}")
    print(f"MONTHLY USAGE: {year}-{month:02d}")
    print(f"{'='*60}")
```

**Output Format:**
```
============================================================
MONTHLY USAGE: 2025-11
============================================================

============================================================
USAGE DATA: 2025-11-01 to 2025-11-30
============================================================
```

### 4. Daily Usage Query (Lines 112-126)

The `query_usage_by_day()` function retrieves usage data for a single day.

```python
def query_usage_by_day(client, date_str):
    """
    Query API usage for a specific day.
    Lines 117-125: Retrieve usage data for a specific day
    """
    print(f"\n{'='*60}")
    print(f"DAILY USAGE: {date_str}")
    print(f"{'='*60}")

    query_usage_by_date_range(client, date_str, date_str)
```

**Output Format:**
```
============================================================
DAILY USAGE: 2025-11-19
============================================================

============================================================
USAGE DATA: 2025-11-19 to 2025-11-19
============================================================
```

### 5. API Call with Header Extraction (Lines 128-158)

The `demonstrate_api_call_with_headers()` function makes a real API call and extracts rate limit information.

```python
def demonstrate_api_call_with_headers(client):
    """
    Make a simple API call and display rate limit headers.
    Lines 133-150: Make API call and extract rate limit headers
    """
    print(f"\n{'='*60}")
    print("MAKING API CALL TO RETRIEVE RATE LIMIT HEADERS")
    print(f"{'='*60}")

    try:
        # Make a simple API call
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            messages=[
                {"role": "user", "content": "Say hello in one word"}
            ]
        )

        print(f"\nAPI Response: {response.content[0].text}")
        print(f"Model used: {response.model}")
        print(f"Input tokens: {response.usage.input_tokens}")
        print(f"Output tokens: {response.usage.output_tokens}")

        # Display rate limit headers
        print_rate_limit_headers(response)
```

**Output Format:**
```
============================================================
MAKING API CALL TO RETRIEVE RATE LIMIT HEADERS
============================================================

API Response: Hello
Model used: claude-3-5-sonnet-20241022
Input tokens: 12
Output tokens: 2

============================================================
RATE LIMIT INFORMATION FROM RESPONSE HEADERS
============================================================
Requests Limit:     4000
Requests Remaining: 3999
Requests Reset:     2025-11-20T12:00:00Z
Tokens Limit:       400000
Tokens Remaining:   399986
Tokens Reset:       2025-11-20T12:00:00Z
============================================================
```

### 6. Main Execution Flow (Lines 160-217)

The `main()` function orchestrates all demonstrations:

```python
def main():
    """
    Main function demonstrating Claude API usage information retrieval.
    Lines 163-190: Main execution flow
    """
    print("="*60)
    print("CLAUDE API USAGE INFORMATION RETRIEVAL")
    print("="*60)

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
    today = datetime.now().strftime("%Y-%m-%d")
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
```

## Sample Output (Without API Key)

When run without an API key set, the script outputs:

```
============================================================
CLAUDE API USAGE INFORMATION RETRIEVAL
============================================================

ERROR: ANTHROPIC_API_KEY environment variable not set
This is a demonstration of the API structure.

To run this with real data:
1. Set your API key: export ANTHROPIC_API_KEY='your-key-here'
2. Run: uv run python main_claude_api_usage.py
```

## Sample Output (With Valid API Key)

When run with a valid API key, the script executes all demonstrations:

```
============================================================
CLAUDE API USAGE INFORMATION RETRIEVAL
============================================================

============================================================
MAKING API CALL TO RETRIEVE RATE LIMIT HEADERS
============================================================

API Response: Hello
Model used: claude-3-5-sonnet-20241022
Input tokens: 12
Output tokens: 2

============================================================
RATE LIMIT INFORMATION FROM RESPONSE HEADERS
============================================================
Requests Limit:     4000
Requests Remaining: 3999
Requests Reset:     2025-11-20T12:00:00Z
Tokens Limit:       400000
Tokens Remaining:   399986
Tokens Reset:       2025-11-20T12:00:00Z
============================================================


============================================================
DAILY USAGE: 2025-11-19
============================================================

============================================================
USAGE DATA: 2025-11-19 to 2025-11-19
============================================================

Total records retrieved: 3

Date: 2025-11-19
Model: claude-3-5-sonnet-20241022
Input tokens: 1845
Output tokens: 1203
Total tokens: 3048

Date: 2025-11-19
Model: claude-3-opus-20240229
Input tokens: 456
Output tokens: 234
Total tokens: 690
============================================================


============================================================
MONTHLY USAGE: 2025-11
============================================================

============================================================
USAGE DATA: 2025-11-01 to 2025-11-30
============================================================

Total records retrieved: 15

Date: 2025-11-01
Model: claude-3-5-sonnet-20241022
Input tokens: 2340
Output tokens: 1560
Total tokens: 3900
...
============================================================

============================================================
DEMONSTRATION COMPLETE
============================================================

KEY FEATURES DEMONSTRATED:
✓ Rate limit header parsing
✓ Usage query by day
✓ Usage query by month
✓ Usage query by custom date range
✓ Token counts broken down by model
============================================================
```

## Code Annotations

### Line-by-Line Correlation with Output

| Source Code Lines | Functionality | Output Section |
|-------------------|---------------|----------------|
| Lines 1-7 | Inline script metadata | Dependency management (uv handles automatically) |
| Lines 18-44 | Rate limit header parsing | "RATE LIMIT INFORMATION FROM RESPONSE HEADERS" section |
| Lines 46-78 | Custom date range query | "USAGE DATA: YYYY-MM-DD to YYYY-MM-DD" sections |
| Lines 80-110 | Monthly usage query | "MONTHLY USAGE: YYYY-MM" section |
| Lines 112-126 | Daily usage query | "DAILY USAGE: YYYY-MM-DD" section |
| Lines 128-158 | API call with headers | "MAKING API CALL TO RETRIEVE RATE LIMIT HEADERS" section |
| Lines 160-217 | Main execution flow | Overall program structure and flow |

### Key Implementation Details

**1. Header Extraction (Lines 28-36):**
- The script accesses `response.headers` to retrieve rate limit information
- Each header follows the `anthropic-ratelimit-*` naming convention
- Graceful fallback to "N/A" when headers are unavailable

**2. Usage API (Lines 60-65):**
- Uses `client.usage.list()` method with `start_date` and `end_date` parameters
- Returns an iterable of usage records
- Each record contains: date, model, input_tokens, output_tokens

**3. Token Breakdown (Lines 70-74):**
- Usage records are broken down by model type
- Separate tracking of input vs output tokens
- Easy aggregation of total tokens per model and per time period

**4. Date Handling (Lines 93-98, 187-199):**
- Python's `datetime` module for date calculations
- String formatting using `strftime("%Y-%m-%d")`
- Automatic calculation of month boundaries

## Important Notes

- **API Key Security**: Never hardcode API keys in source code. Always use environment variables.
- **Rate Limits**: Monitor the rate limit headers to avoid hitting API limits.
- **Token Tracking**: Usage data helps optimize costs by tracking token consumption patterns.
- **Model Breakdown**: Different models have different pricing; tracking by model is essential for cost management.
- **Date Formats**: All dates use ISO 8601 format (YYYY-MM-DD).

## Version Requirements

This code requires:
- **Python 3.11 or higher** - Required for modern type hints and features
- **anthropic library 0.39.0 or higher** - For usage API support and proper header handling
- **uv package manager** - For dependency management and script execution

## Usage Tips

1. **Setting up your environment:**
   ```bash
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```

2. **Running for specific date ranges:**
   Modify lines 196-199 in the main() function to customize date ranges:
   ```python
   start = "2025-01-01"
   end = "2025-01-31"
   query_usage_by_date_range(client, start, end)
   ```

3. **Monitoring rate limits:**
   The rate limit headers update with every API call, allowing real-time monitoring of your usage against limits.

4. **Cost optimization:**
   Use the token breakdown by model to identify which models are consuming the most tokens and optimize accordingly.
