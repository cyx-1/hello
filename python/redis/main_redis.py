#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "redis>=5.0.0",
# ]
# ///

"""
Redis Demonstration in Python
Showcases key Redis features including:
- String operations
- Data structures (Lists, Sets, Hashes, Sorted Sets)
- Expiration and TTL
- Pub/Sub messaging
- Transactions
- Pipelines
"""

import redis
import time
import json


def print_section(title: str):
    """Print a formatted section header"""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def demo_string_operations(r: redis.Redis):
    """Demonstrate basic string operations"""
    print_section("1. STRING OPERATIONS")

    # Line 38: Set a simple key-value pair
    r.set("user:1000:name", "Alice Johnson")
    print("Line 38: SET user:1000:name -> 'Alice Johnson'")

    # Line 42: Get the value
    name = r.get("user:1000:name")
    print(f"Line 42: GET user:1000:name -> {name.decode()}")

    # Line 46: Set with expiration (5 seconds)
    r.setex("session:abc123", 5, "temporary_session_data")
    print("Line 46: SETEX session:abc123 (expires in 5s)")

    # Line 50: Check TTL (time to live)
    ttl = r.ttl("session:abc123")
    print(f"Line 50: TTL session:abc123 -> {ttl} seconds")

    # Line 54: Increment counter
    r.set("page:views", 0)
    for _ in range(5):
        views = r.incr("page:views")
    print(f"Line 54-57: INCR page:views (5 times) -> {views}")

    # Line 60: Decrement counter
    r.decr("page:views")
    views = r.get("page:views")
    print(f"Line 60-62: DECR page:views -> {views.decode()}")


def demo_list_operations(r: redis.Redis):
    """Demonstrate Redis list operations"""
    print_section("2. LIST OPERATIONS")

    # Line 70: Push items to a list (right side)
    r.delete("tasks")  # Clean up first
    r.rpush("tasks", "task1", "task2", "task3")
    print("Line 70-72: RPUSH tasks -> ['task1', 'task2', 'task3']")

    # Line 75: Get list length
    length = r.llen("tasks")
    print(f"Line 75-76: LLEN tasks -> {length}")

    # Line 79: Get range of items
    items = r.lrange("tasks", 0, -1)
    print(f"Line 79-80: LRANGE tasks 0 -1 -> {[item.decode() for item in items]}")

    # Line 83: Pop from left (FIFO queue)
    first_task = r.lpop("tasks")
    print(f"Line 83-84: LPOP tasks -> {first_task.decode()}")

    # Line 87: Remaining items
    remaining = r.lrange("tasks", 0, -1)
    print(f"Line 87-88: LRANGE tasks 0 -1 -> {[item.decode() for item in remaining]}")


def demo_set_operations(r: redis.Redis):
    """Demonstrate Redis set operations"""
    print_section("3. SET OPERATIONS")

    # Line 96: Add members to sets
    r.delete("tags:python", "tags:web")
    r.sadd("tags:python", "django", "flask", "fastapi")
    r.sadd("tags:web", "react", "vue", "flask")
    print("Line 96-99: SADD tags:python -> {'django', 'flask', 'fastapi'}")
    print("Line 96-99: SADD tags:web -> {'react', 'vue', 'flask'}")

    # Line 103: Get all members
    python_tags = r.smembers("tags:python")
    print(
        f"Line 103-104: SMEMBERS tags:python -> {sorted([t.decode() for t in python_tags])}"
    )

    # Line 107: Check membership
    is_member = r.sismember("tags:python", "django")
    print(f"Line 107-108: SISMEMBER tags:python 'django' -> {bool(is_member)}")

    # Line 111: Set intersection (common elements)
    common = r.sinter("tags:python", "tags:web")
    print(
        f"Line 111-112: SINTER tags:python tags:web -> {[t.decode() for t in common]}"
    )

    # Line 115: Set union (all unique elements)
    all_tags = r.sunion("tags:python", "tags:web")
    print(
        f"Line 115-116: SUNION tags:python tags:web -> {sorted([t.decode() for t in all_tags])}"
    )


def demo_hash_operations(r: redis.Redis):
    """Demonstrate Redis hash operations"""
    print_section("4. HASH OPERATIONS")

    # Line 124: Set hash fields
    r.delete("user:2000")
    r.hset(
        "user:2000",
        mapping={
            "name": "Bob Smith",
            "email": "bob@example.com",
            "age": "30",
            "city": "New York",
        },
    )
    print("Line 124-131: HSET user:2000 -> {name, email, age, city}")

    # Line 134: Get single field
    email = r.hget("user:2000", "email")
    print(f"Line 134-135: HGET user:2000 email -> {email.decode()}")

    # Line 138: Get all fields and values
    user_data = r.hgetall("user:2000")
    user_dict = {k.decode(): v.decode() for k, v in user_data.items()}
    print(f"Line 138-140: HGETALL user:2000 -> {json.dumps(user_dict, indent=2)}")

    # Line 143: Increment numeric field
    r.hincrby("user:2000", "age", 1)
    new_age = r.hget("user:2000", "age")
    print(f"Line 143-145: HINCRBY user:2000 age 1 -> {new_age.decode()}")


def demo_sorted_set_operations(r: redis.Redis):
    """Demonstrate Redis sorted set operations"""
    print_section("5. SORTED SET OPERATIONS (Leaderboard)")

    # Line 153: Add members with scores
    r.delete("leaderboard")
    r.zadd(
        "leaderboard",
        {
            "player1": 1500,
            "player2": 2300,
            "player3": 1800,
            "player4": 2100,
            "player5": 1950,
        },
    )
    print("Line 153-161: ZADD leaderboard -> {player:score pairs}")

    # Line 164: Get top 3 players (highest scores)
    top_players = r.zrevrange("leaderboard", 0, 2, withscores=True)
    print("Line 164-165: ZREVRANGE leaderboard 0 2 WITHSCORES ->")
    for rank, (player, score) in enumerate(top_players, 1):
        print(f"  #{rank}: {player.decode()} - {int(score)} points")

    # Line 170: Get player rank
    rank = r.zrevrank("leaderboard", "player3")
    print(f"Line 170-171: ZREVRANK leaderboard player3 -> #{rank + 1}")

    # Line 174: Increment player score
    new_score = r.zincrby("leaderboard", 500, "player3")
    print(f"Line 174-175: ZINCRBY leaderboard 500 player3 -> {int(new_score)}")

    # Line 178: Get updated rank
    new_rank = r.zrevrank("leaderboard", "player3")
    print(f"Line 178-179: ZREVRANK leaderboard player3 -> #{new_rank + 1}")


def demo_expiration(r: redis.Redis):
    """Demonstrate key expiration"""
    print_section("6. KEY EXPIRATION")

    # Line 187: Set key with 3-second expiration
    r.setex("temp:data", 3, "This will expire soon")
    print("Line 187-188: SETEX temp:data 3 -> 'This will expire soon'")

    # Line 191: Check if key exists
    exists = r.exists("temp:data")
    print(f"Line 191-192: EXISTS temp:data -> {bool(exists)}")

    # Line 195: Wait 2 seconds
    print("Line 195-196: Waiting 2 seconds...")
    time.sleep(2)

    # Line 199: Check TTL
    ttl = r.ttl("temp:data")
    print(f"Line 199-200: TTL temp:data -> {ttl} second(s)")

    # Line 203: Wait for expiration
    print("Line 203-204: Waiting 2 more seconds...")
    time.sleep(2)

    # Line 207: Check if key still exists
    exists = r.exists("temp:data")
    print(f"Line 207-208: EXISTS temp:data -> {bool(exists)} (expired)")


def demo_transactions(r: redis.Redis):
    """Demonstrate Redis transactions"""
    print_section("7. TRANSACTIONS (MULTI/EXEC)")

    # Line 216: Execute multiple commands atomically
    r.set("balance:alice", 1000)
    r.set("balance:bob", 500)
    print("Line 216-218: Initial balances -> Alice: 1000, Bob: 500")

    # Line 221: Transfer 100 from Alice to Bob
    pipe = r.pipeline()
    pipe.decrby("balance:alice", 100)
    pipe.incrby("balance:bob", 100)
    pipe.execute()
    print("Line 221-225: MULTI/EXEC Transfer 100 from Alice to Bob")

    # Line 228: Check final balances
    alice_balance = r.get("balance:alice")
    bob_balance = r.get("balance:bob")
    print(
        f"Line 228-230: Final balances -> Alice: {alice_balance.decode()}, Bob: {bob_balance.decode()}"
    )


def demo_pipeline(r: redis.Redis):
    """Demonstrate pipeline for performance"""
    print_section("8. PIPELINE (Performance Optimization)")

    # Line 238: Without pipeline
    start = time.time()
    for i in range(100):
        r.set(f"key:{i}", f"value{i}")
    without_pipeline = time.time() - start
    print(f"Line 238-242: Set 100 keys WITHOUT pipeline -> {without_pipeline:.4f}s")

    # Line 245: With pipeline
    r.delete(*[f"pkey:{i}" for i in range(100)])
    start = time.time()
    pipe = r.pipeline()
    for i in range(100):
        pipe.set(f"pkey:{i}", f"value{i}")
    pipe.execute()
    with_pipeline = time.time() - start
    print(f"Line 245-252: Set 100 keys WITH pipeline -> {with_pipeline:.4f}s")

    # Line 255: Performance improvement
    speedup = without_pipeline / with_pipeline
    print(f"Line 255-256: Pipeline is {speedup:.1f}x faster")


def demo_pubsub():
    """Demonstrate Pub/Sub messaging"""
    print_section("9. PUB/SUB MESSAGING")

    print("Line 264: Creating separate connections for publisher and subscriber")

    # Note: Real pub/sub requires separate connections and threads
    # This is a simplified demonstration
    publisher = redis.Redis(host="localhost", port=6379, decode_responses=True)
    subscriber = redis.Redis(host="localhost", port=6379, decode_responses=True)

    pubsub = subscriber.pubsub()
    pubsub.subscribe("news:tech")
    print("Line 271-273: SUBSCRIBE news:tech")

    # Skip subscription confirmation message
    pubsub.get_message()

    # Line 277: Publish messages
    publisher.publish("news:tech", "Python 3.13 released!")
    publisher.publish("news:tech", "Redis 7.2 now available!")
    print("Line 277-279: PUBLISH news:tech -> 2 messages sent")

    # Line 282: Receive messages
    print("Line 282: Receiving messages:")
    for _ in range(2):
        time.sleep(0.1)
        message = pubsub.get_message()
        if message and message["type"] == "message":
            print(f"  -> {message['data']}")

    pubsub.unsubscribe()
    pubsub.close()


def main():
    """Main function to run all Redis demonstrations"""
    print("\n" + "=" * 60)
    print("  REDIS PYTHON DEMONSTRATION")
    print("  Comprehensive Redis Feature Showcase")
    print("=" * 60)

    try:
        # Line 304: Connect to Redis
        r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=False)

        # Line 312: Test connection
        r.ping()
        print("\n✓ Connected to Redis successfully")
        print(f"  Server version: {r.info()['redis_version']}")

        # Run all demonstrations
        demo_string_operations(r)
        demo_list_operations(r)
        demo_set_operations(r)
        demo_hash_operations(r)
        demo_sorted_set_operations(r)
        demo_expiration(r)
        demo_transactions(r)
        demo_pipeline(r)
        demo_pubsub()

        # Line 328: Cleanup
        print_section("10. CLEANUP")
        pattern_keys = [
            "user:*",
            "tasks",
            "tags:*",
            "leaderboard",
            "page:views",
            "balance:*",
            "key:*",
            "pkey:*",
        ]
        for pattern in pattern_keys:
            keys = r.keys(pattern)
            if keys:
                r.delete(*keys)
        print("Line 328-336: Cleaned up all demo keys")

        print("\n" + "=" * 60)
        print("  ✓ All Redis demonstrations completed successfully!")
        print("=" * 60 + "\n")

    except redis.ConnectionError:
        print("\n❌ ERROR: Could not connect to Redis server")
        print("   Please ensure Redis is running on localhost:6379")
        print("   Start Redis with: redis-server")
        print("\n   For installation:")
        print("   - macOS: brew install redis")
        print("   - Ubuntu/Debian: sudo apt-get install redis-server")
        print("   - Docker: docker run -d -p 6379:6379 redis:latest\n")
    except Exception as e:
        print(f"\n❌ ERROR: {e}\n")


if __name__ == "__main__":
    main()
