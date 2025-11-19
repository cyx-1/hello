# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "tweepy>=4.14.0",
# ]
# ///
"""
Demonstration of fetching posts from X.com (Twitter) using the X API v2.

This script shows how to:
- Authenticate with the X API using Bearer Token
- Fetch recent tweets by user ID
- Search for tweets by keyword
- Retrieve tweet details including metrics

Required environment variable:
- X_BEARER_TOKEN: Your X API Bearer Token (from developer.x.com)
"""

import os
import sys
from datetime import datetime, timezone

import tweepy


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


def fetch_user_tweets(client: tweepy.Client, username: str, max_results: int = 5):
    """
    Fetch recent tweets from a specific user.

    Args:
        client: Authenticated tweepy Client
        username: X username (without @)
        max_results: Number of tweets to fetch (5-100)
    """
    print(f"\n{'=' * 60}")
    print(f"Fetching tweets from @{username}")
    print(f"{'=' * 60}")

    # First, get the user ID from username
    user = client.get_user(
        username=username, user_fields=["description", "public_metrics"]
    )

    if not user.data:
        print(f"User @{username} not found")
        return

    user_data = user.data
    print(f"\nUser: {user_data.name} (@{user_data.username})")
    print(
        f"Description: {user_data.description[:100]}..."
        if user_data.description
        else ""
    )

    metrics = user_data.public_metrics
    print(f"Followers: {metrics['followers_count']:,}")
    print(f"Following: {metrics['following_count']:,}")
    print(f"Tweet count: {metrics['tweet_count']:,}")

    # Fetch recent tweets
    tweets = client.get_users_tweets(
        id=user_data.id,
        max_results=max_results,
        tweet_fields=["created_at", "public_metrics", "text"],
        exclude=["retweets", "replies"],
    )

    if not tweets.data:
        print(f"\nNo tweets found for @{username}")
        return

    print(f"\n--- Recent {len(tweets.data)} Tweets ---\n")

    for i, tweet in enumerate(tweets.data, 1):
        print(f"Tweet {i}:")
        print(f"  ID: {tweet.id}")
        print(f"  Created: {tweet.created_at}")
        print(f"  Text: {tweet.text[:150]}{'...' if len(tweet.text) > 150 else ''}")

        if tweet.public_metrics:
            pm = tweet.public_metrics
            print(
                f"  Likes: {pm['like_count']} | Retweets: {pm['retweet_count']} | "
                f"Replies: {pm['reply_count']} | Quotes: {pm['quote_count']}"
            )
        print()


def search_recent_tweets(client: tweepy.Client, query: str, max_results: int = 10):
    """
    Search for recent tweets matching a query.

    Args:
        client: Authenticated tweepy Client
        query: Search query (supports X search operators)
        max_results: Number of tweets to fetch (10-100)
    """
    print(f"\n{'=' * 60}")
    print(f"Searching tweets for: '{query}'")
    print(f"{'=' * 60}")

    # Search recent tweets (last 7 days with Basic access)
    tweets = client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=["created_at", "public_metrics", "author_id", "lang"],
        expansions=["author_id"],
        user_fields=["username", "name"],
    )

    if not tweets.data:
        print(f"\nNo tweets found for query: '{query}'")
        return

    # Create user lookup dictionary
    users = {user.id: user for user in tweets.includes.get("users", [])}

    print(f"\n--- Found {len(tweets.data)} Tweets ---\n")

    for i, tweet in enumerate(tweets.data, 1):
        author = users.get(tweet.author_id)
        author_info = f"@{author.username}" if author else f"ID:{tweet.author_id}"

        print(f"Tweet {i} by {author_info}:")
        print(f"  Created: {tweet.created_at}")
        print(f"  Language: {tweet.lang}")
        print(f"  Text: {tweet.text[:150]}{'...' if len(tweet.text) > 150 else ''}")

        if tweet.public_metrics:
            pm = tweet.public_metrics
            print(f"  Engagement: {pm['like_count']} likes, {pm['retweet_count']} RTs")
        print()


def get_tweet_by_id(client: tweepy.Client, tweet_id: str):
    """
    Fetch a specific tweet by its ID.

    Args:
        client: Authenticated tweepy Client
        tweet_id: The ID of the tweet to fetch
    """
    print(f"\n{'=' * 60}")
    print(f"Fetching tweet ID: {tweet_id}")
    print(f"{'=' * 60}")

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

    if not tweet.data:
        print(f"Tweet {tweet_id} not found")
        return

    tweet_data = tweet.data
    author = tweet.includes["users"][0] if tweet.includes.get("users") else None

    print(f"\nAuthor: {author.name} (@{author.username})" if author else "")
    print(f"Created: {tweet_data.created_at}")
    print(f"Text: {tweet_data.text}")

    if tweet_data.public_metrics:
        pm = tweet_data.public_metrics
        print("\nEngagement Metrics:")
        print(f"  Likes: {pm['like_count']:,}")
        print(f"  Retweets: {pm['retweet_count']:,}")
        print(f"  Replies: {pm['reply_count']:,}")
        print(f"  Quotes: {pm['quote_count']:,}")
        print(f"  Bookmarks: {pm.get('bookmark_count', 0):,}")
        print(f"  Impressions: {pm.get('impression_count', 'N/A')}")


def demo_mode():
    """Run demonstration with sample output when no API key is available."""
    print("\n" + "=" * 60)
    print("DEMO MODE - Showing expected output format")
    print("=" * 60)
    print("\nNote: Set X_BEARER_TOKEN to fetch real data\n")

    # Simulated user data
    print(f"{'=' * 60}")
    print("Fetching tweets from @Python")
    print(f"{'=' * 60}")

    print("\nUser: Python (@Python)")
    print("Description: News & links for the Python programming language...")
    print("Followers: 1,234,567")
    print("Following: 42")
    print("Tweet count: 5,432")

    print("\n--- Recent 3 Tweets ---\n")

    sample_tweets = [
        {
            "id": "1234567890123456789",
            "created": "2024-01-15 14:30:00+00:00",
            "text": "Python 3.13 is now available! Check out the new features including improved error messages and performance optimizations.",
            "likes": 2543,
            "retweets": 876,
            "replies": 123,
            "quotes": 45,
        },
        {
            "id": "1234567890123456790",
            "created": "2024-01-14 10:15:00+00:00",
            "text": "Join us for PyCon 2024! Early bird registration is now open. Don't miss the chance to connect with the Python community.",
            "likes": 1876,
            "retweets": 543,
            "replies": 89,
            "quotes": 32,
        },
        {
            "id": "1234567890123456791",
            "created": "2024-01-13 16:45:00+00:00",
            "text": "New tutorial: Building async web applications with Python and FastAPI. Learn modern web development patterns.",
            "likes": 987,
            "retweets": 234,
            "replies": 56,
            "quotes": 12,
        },
    ]

    for i, tweet in enumerate(sample_tweets, 1):
        print(f"Tweet {i}:")
        print(f"  ID: {tweet['id']}")
        print(f"  Created: {tweet['created']}")
        print(f"  Text: {tweet['text'][:150]}...")
        print(
            f"  Likes: {tweet['likes']} | Retweets: {tweet['retweets']} | "
            f"Replies: {tweet['replies']} | Quotes: {tweet['quotes']}"
        )
        print()


def main():
    """Main entry point demonstrating X API v2 capabilities."""
    print("X.com (Twitter) API v2 - Post Fetching Demo")
    print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")

    # Check if we have credentials
    if not os.environ.get("X_BEARER_TOKEN"):
        demo_mode()
        return

    # Initialize client
    client = get_client()

    # Example 1: Fetch tweets from a user
    fetch_user_tweets(client, "Python", max_results=5)

    # Example 2: Search for recent tweets
    search_recent_tweets(
        client, "python programming -is:retweet lang:en", max_results=5
    )

    # Example 3: Get a specific tweet (example ID - replace with real ID)
    # get_tweet_by_id(client, "1234567890123456789")

    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
