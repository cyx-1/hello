# X.com (Twitter) Posts Fetching with Python

This example demonstrates how to fetch posts from X.com (formerly Twitter) using the official X API v2 with the `tweepy` library.

## Requirements

- Python >= 3.10
- X API Bearer Token (from [developer.x.com](https://developer.x.com))

## Running the Script

```bash
# Set your API credentials
export X_BEARER_TOKEN='your_bearer_token_here'

# Run with uv
uv run main_x_posts.py
```

## Key Source Code

### Inline Dependencies (Lines 1-6)
```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "tweepy>=4.14.0",
# ]
# ///
```
Uses PEP 723 inline script metadata to specify dependencies, allowing `uv` to automatically install `tweepy` without a separate requirements file.

### Authentication (Lines 27-40)
```python
def get_client() -> tweepy.Client:
    """Initialize and return an authenticated X API client."""
    bearer_token = os.environ.get("X_BEARER_TOKEN")

    if not bearer_token:
        print("Error: X_BEARER_TOKEN environment variable not set")
        print("\nTo get a Bearer Token:")
        print("1. Go to https://developer.x.com/en/portal/dashboard")
        print("2. Create a project and app")
        print("3. Generate a Bearer Token")
        print("4. Set it: export X_BEARER_TOKEN='your_token_here'")
        sys.exit(1)

    return tweepy.Client(bearer_token=bearer_token)
```
- **Line 29**: Retrieves Bearer Token from environment variable for security
- **Lines 31-38**: Provides helpful instructions if token is missing
- **Line 40**: Creates authenticated `tweepy.Client` using Bearer Token authentication

### Fetching User Tweets (Lines 43-104)
```python
def fetch_user_tweets(client: tweepy.Client, username: str, max_results: int = 5):
    # First, get the user ID from username
    user = client.get_user(
        username=username, user_fields=["description", "public_metrics"]
    )

    # ... user validation ...

    # Fetch recent tweets
    tweets = client.get_users_tweets(
        id=user_data.id,
        max_results=max_results,
        tweet_fields=["created_at", "public_metrics", "text"],
        exclude=["retweets", "replies"],
    )
```
- **Lines 57-59**: Converts username to user ID (required by API v2) and fetches user metadata
- **Lines 79-84**: Retrieves user's tweets with engagement metrics, excluding retweets/replies
- **Line 82**: `tweet_fields` parameter specifies which data to include for each tweet

### Searching Recent Tweets (Lines 107-150)
```python
def search_recent_tweets(client: tweepy.Client, query: str, max_results: int = 10):
    tweets = client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=["created_at", "public_metrics", "author_id", "lang"],
        expansions=["author_id"],
        user_fields=["username", "name"],
    )

    # Create user lookup dictionary
    users = {user.id: user for user in tweets.includes.get("users", [])}
```
- **Lines 121-127**: Searches tweets from last 7 days with specified fields
- **Line 125**: `expansions` parameter fetches related user data
- **Line 134**: Creates efficient lookup for author information using dictionary comprehension

### Fetching Specific Tweet (Lines 153-196)
```python
def get_tweet_by_id(client: tweepy.Client, tweet_id: str):
    tweet = client.get_tweet(
        id=tweet_id,
        tweet_fields=[
            "created_at",
            "public_metrics",
            "author_id",
            "context_annotations",
        ],
        expansions=["author_id"],
        user_fields=["username", "name", "verified"],
    )
```
- **Lines 165-175**: Fetches detailed tweet data including context annotations
- **Lines 191-196**: Displays comprehensive engagement metrics (likes, retweets, replies, quotes, bookmarks, impressions)

## Program Output

```
X.com (Twitter) API v2 - Post Fetching Demo
Timestamp: 2025-11-19T08:29:19.691306+00:00

============================================================
DEMO MODE - Showing expected output format
============================================================

Note: Set X_BEARER_TOKEN to fetch real data

============================================================
Fetching tweets from @Python
============================================================

User: Python (@Python)
Description: News & links for the Python programming language...
Followers: 1,234,567
Following: 42
Tweet count: 5,432

--- Recent 3 Tweets ---

Tweet 1:
  ID: 1234567890123456789
  Created: 2024-01-15 14:30:00+00:00
  Text: Python 3.13 is now available! Check out the new features including improved error messages and performance optimizations....
  Likes: 2543 | Retweets: 876 | Replies: 123 | Quotes: 45

Tweet 2:
  ID: 1234567890123456790
  Created: 2024-01-14 10:15:00+00:00
  Text: Join us for PyCon 2024! Early bird registration is now open. Don't miss the chance to connect with the Python community....
  Likes: 1876 | Retweets: 543 | Replies: 89 | Quotes: 32

Tweet 3:
  ID: 1234567890123456791
  Created: 2024-01-13 16:45:00+00:00
  Text: New tutorial: Building async web applications with Python and FastAPI. Learn modern web development patterns....
  Likes: 987 | Retweets: 234 | Replies: 56 | Quotes: 12
```

## Output Annotations

| Output Line | Source Reference | Description |
|-------------|------------------|-------------|
| `X.com (Twitter) API v2 - Post Fetching Demo` | Line 263 | Script banner from `main()` |
| `Timestamp: ...` | Line 264 | UTC timestamp using `datetime.now(timezone.utc)` |
| `DEMO MODE` | Lines 201-203 | Triggered when `X_BEARER_TOKEN` not set (line 267) |
| `User: Python (@Python)` | Line 211 | Simulated user data in demo mode |
| `Followers: 1,234,567` | Line 213 | Uses comma formatting for readability |
| `Tweet 1:` | Line 250 | Loop iteration with `enumerate(sample_tweets, 1)` |
| `Likes: 2543 \| Retweets: 876 \| ...` | Lines 254-257 | Engagement metrics formatted with pipe separators |

## API Access Tiers

| Feature | Free | Basic ($100/mo) | Pro ($5000/mo) |
|---------|------|-----------------|----------------|
| Posts per month | 1,500 | 10,000 | 1,000,000 |
| Search recent tweets | Last 7 days | Last 7 days | Full archive |
| User lookup | Yes | Yes | Yes |
| Engagement metrics | Yes | Yes | Yes |

## X API Search Operators

The `search_recent_tweets` function (line 278-280) uses X search operators:

```python
search_recent_tweets(
    client, "python programming -is:retweet lang:en", max_results=5
)
```

Common operators:
- `-is:retweet` - Exclude retweets
- `lang:en` - Only English tweets
- `from:username` - Tweets from specific user
- `has:media` - Tweets with media
- `is:verified` - From verified accounts

## Error Handling Notes

- **Line 31-38**: Graceful exit with instructions when Bearer Token missing
- **Line 61-63**: Handles non-existent users
- **Line 86-88**: Handles users with no tweets
- **Line 129-131**: Handles empty search results

## Security Best Practices

1. **Never hardcode tokens** - Always use environment variables (line 29)
2. **Use Bearer Token** - Read-only access, no user-context required
3. **Rate limiting** - API has strict limits, implement backoff for production use

## Additional Resources

- [X API v2 Documentation](https://developer.x.com/en/docs/twitter-api)
- [Tweepy Documentation](https://docs.tweepy.org/)
- [X Developer Portal](https://developer.x.com/en/portal/dashboard)
