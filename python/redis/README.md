# Redis Python Example

A comprehensive demonstration of Redis features using Python's redis-py library.

## Requirements

- **Python**: >= 3.11
- **Redis Server**: Any version (tested with 7.0.15)
- **Python Package**: `redis>=5.0.0`

## Running the Example

```bash
# Start Redis server (if not already running)
redis-server --daemonize yes

# Run the demonstration
uv run main_redis.py
```

## Overview

This example demonstrates the following Redis features:

1. **String Operations** - Basic key-value storage with expiration and atomic counters
2. **List Operations** - Queue-like data structures with FIFO/LIFO operations
3. **Set Operations** - Unique collections with set algebra (union, intersection)
4. **Hash Operations** - Field-value maps for structured data
5. **Sorted Set Operations** - Ordered collections with scores (leaderboards)
6. **Key Expiration** - Time-to-live (TTL) and automatic cleanup
7. **Transactions** - Atomic multi-command operations
8. **Pipeline** - Batching commands for performance
9. **Pub/Sub** - Message broadcasting and subscription

---

## Detailed Walkthrough

### 1. String Operations

**Source Code (Lines 38-62):**

```python
38:  # Set a simple key-value pair
39:  r.set("user:1000:name", "Alice Johnson")
40:  print(f"Line 38: SET user:1000:name -> 'Alice Johnson'")
41:
42:  # Get the value
43:  name = r.get("user:1000:name")
44:  print(f"Line 42: GET user:1000:name -> {name.decode()}")
45:
46:  # Set with expiration (5 seconds)
47:  r.setex("session:abc123", 5, "temporary_session_data")
48:  print(f"Line 46: SETEX session:abc123 (expires in 5s)")
49:
50:  # Check TTL (time to live)
51:  ttl = r.ttl("session:abc123")
52:  print(f"Line 50: TTL session:abc123 -> {ttl} seconds")
53:
54:  # Increment counter
55:  r.set("page:views", 0)
56:  for _ in range(5):
57:      views = r.incr("page:views")
58:  print(f"Line 54-57: INCR page:views (5 times) -> {views}")
59:
60:  # Decrement counter
61:  r.decr("page:views")
62:  views = r.get("page:views")
63:  print(f"Line 60-62: DECR page:views -> {views.decode()}")
```

**Output:**

```
Line 38: SET user:1000:name -> 'Alice Johnson'
Line 42: GET user:1000:name -> Alice Johnson
Line 46: SETEX session:abc123 (expires in 5s)
Line 50: TTL session:abc123 -> 5 seconds
Line 54-57: INCR page:views (5 times) -> 5
Line 60-62: DECR page:views -> 4
```

**Annotations:**

- **Lines 39-40**: Basic `SET` command stores a string value
- **Lines 43-44**: `GET` retrieves the stored value (needs `.decode()` for bytes to string)
- **Lines 47-48**: `SETEX` combines SET with expiration time (useful for sessions, caches)
- **Lines 51-52**: `TTL` returns remaining seconds before key expires
- **Lines 55-58**: `INCR` atomically increments integer values (thread-safe counters)
- **Lines 61-63**: `DECR` atomically decrements values

---

### 2. List Operations

**Source Code (Lines 70-88):**

```python
70:  # Push items to a list (right side)
71:  r.delete("tasks")  # Clean up first
72:  r.rpush("tasks", "task1", "task2", "task3")
73:  print(f"Line 70-72: RPUSH tasks -> ['task1', 'task2', 'task3']")
74:
75:  # Get list length
76:  length = r.llen("tasks")
77:  print(f"Line 75-76: LLEN tasks -> {length}")
78:
79:  # Get range of items
80:  items = r.lrange("tasks", 0, -1)
81:  print(f"Line 79-80: LRANGE tasks 0 -1 -> {[item.decode() for item in items]}")
82:
83:  # Pop from left (FIFO queue)
84:  first_task = r.lpop("tasks")
85:  print(f"Line 83-84: LPOP tasks -> {first_task.decode()}")
86:
87:  # Remaining items
88:  remaining = r.lrange("tasks", 0, -1)
89:  print(f"Line 87-88: LRANGE tasks 0 -1 -> {[item.decode() for item in remaining]}")
```

**Output:**

```
Line 70-72: RPUSH tasks -> ['task1', 'task2', 'task3']
Line 75-76: LLEN tasks -> 3
Line 79-80: LRANGE tasks 0 -1 -> ['task1', 'task2', 'task3']
Line 83-84: LPOP tasks -> task1
Line 87-88: LRANGE tasks 0 -1 -> ['task2', 'task3']
```

**Annotations:**

- **Line 72**: `RPUSH` adds elements to the right (end) of the list
- **Lines 76-77**: `LLEN` returns the number of elements in the list
- **Lines 80-81**: `LRANGE` retrieves elements by index range (0 to -1 means all elements)
- **Lines 84-85**: `LPOP` removes and returns element from left (FIFO queue behavior)
- **Lines 88-89**: After LPOP, "task1" is removed, leaving "task2" and "task3"

---

### 3. Set Operations

**Source Code (Lines 96-116):**

```python
 96:  # Add members to sets
 97:  r.delete("tags:python", "tags:web")
 98:  r.sadd("tags:python", "django", "flask", "fastapi")
 99:  r.sadd("tags:web", "react", "vue", "flask")
100:  print(f"Line 96-99: SADD tags:python -> {{'django', 'flask', 'fastapi'}}")
101:  print(f"Line 96-99: SADD tags:web -> {{'react', 'vue', 'flask'}}")
102:
103:  # Get all members
104:  python_tags = r.smembers("tags:python")
105:  print(f"Line 103-104: SMEMBERS tags:python -> {sorted([t.decode() for t in python_tags])}")
106:
107:  # Check membership
108:  is_member = r.sismember("tags:python", "django")
109:  print(f"Line 107-108: SISMEMBER tags:python 'django' -> {bool(is_member)}")
110:
111:  # Set intersection (common elements)
112:  common = r.sinter("tags:python", "tags:web")
113:  print(f"Line 111-112: SINTER tags:python tags:web -> {[t.decode() for t in common]}")
114:
115:  # Set union (all unique elements)
116:  all_tags = r.sunion("tags:python", "tags:web")
117:  print(f"Line 115-116: SUNION tags:python tags:web -> {sorted([t.decode() for t in all_tags])}")
```

**Output:**

```
Line 96-99: SADD tags:python -> {'django', 'flask', 'fastapi'}
Line 96-99: SADD tags:web -> {'react', 'vue', 'flask'}
Line 103-104: SMEMBERS tags:python -> ['django', 'fastapi', 'flask']
Line 107-108: SISMEMBER tags:python 'django' -> True
Line 111-112: SINTER tags:python tags:web -> ['flask']
Line 115-116: SUNION tags:python tags:web -> ['django', 'fastapi', 'flask', 'react', 'vue']
```

**Annotations:**

- **Lines 98-99**: `SADD` adds members to sets (duplicates are automatically ignored)
- **Lines 104-105**: `SMEMBERS` returns all unique members in the set
- **Lines 108-109**: `SISMEMBER` checks if element exists in set (returns boolean)
- **Lines 112-113**: `SINTER` finds intersection - "flask" appears in both sets
- **Lines 116-117**: `SUNION` combines all unique elements from both sets

---

### 4. Hash Operations

**Source Code (Lines 124-145):**

```python
124:  # Set hash fields
125:  r.delete("user:2000")
126:  r.hset("user:2000", mapping={
127:      "name": "Bob Smith",
128:      "email": "bob@example.com",
129:      "age": "30",
130:      "city": "New York"
131:  })
132:  print(f"Line 124-131: HSET user:2000 -> {{name, email, age, city}}")
133:
134:  # Get single field
135:  email = r.hget("user:2000", "email")
136:  print(f"Line 134-135: HGET user:2000 email -> {email.decode()}")
137:
138:  # Get all fields and values
139:  user_data = r.hgetall("user:2000")
140:  user_dict = {k.decode(): v.decode() for k, v in user_data.items()}
141:  print(f"Line 138-140: HGETALL user:2000 -> {json.dumps(user_dict, indent=2)}")
142:
143:  # Increment numeric field
144:  r.hincrby("user:2000", "age", 1)
145:  new_age = r.hget("user:2000", "age")
146:  print(f"Line 143-145: HINCRBY user:2000 age 1 -> {new_age.decode()}")
```

**Output:**

```
Line 124-131: HSET user:2000 -> {name, email, age, city}
Line 134-135: HGET user:2000 email -> bob@example.com
Line 138-140: HGETALL user:2000 -> {
  "name": "Bob Smith",
  "email": "bob@example.com",
  "age": "30",
  "city": "New York"
}
Line 143-145: HINCRBY user:2000 age 1 -> 31
```

**Annotations:**

- **Lines 126-132**: `HSET` with mapping parameter sets multiple field-value pairs at once
- **Lines 135-136**: `HGET` retrieves a single field value from the hash
- **Lines 139-141**: `HGETALL` returns all fields and values as a dictionary
- **Lines 144-146**: `HINCRBY` atomically increments numeric field (age: 30 → 31)

**Use Case:** Hashes are ideal for representing objects (users, products, sessions) with multiple attributes.

---

### 5. Sorted Set Operations (Leaderboard)

**Source Code (Lines 153-179):**

```python
153:  # Add members with scores
154:  r.delete("leaderboard")
155:  r.zadd("leaderboard", {
156:      "player1": 1500,
157:      "player2": 2300,
158:      "player3": 1800,
159:      "player4": 2100,
160:      "player5": 1950
161:  })
162:  print(f"Line 153-161: ZADD leaderboard -> {{player:score pairs}}")
163:
164:  # Get top 3 players (highest scores)
165:  top_players = r.zrevrange("leaderboard", 0, 2, withscores=True)
166:  print(f"Line 164-165: ZREVRANGE leaderboard 0 2 WITHSCORES ->")
167:  for rank, (player, score) in enumerate(top_players, 1):
168:      print(f"  #{rank}: {player.decode()} - {int(score)} points")
169:
170:  # Get player rank
171:  rank = r.zrevrank("leaderboard", "player3")
172:  print(f"Line 170-171: ZREVRANK leaderboard player3 -> #{rank + 1}")
173:
174:  # Increment player score
175:  new_score = r.zincrby("leaderboard", 500, "player3")
176:  print(f"Line 174-175: ZINCRBY leaderboard 500 player3 -> {int(new_score)}")
177:
178:  # Get updated rank
179:  new_rank = r.zrevrank("leaderboard", "player3")
180:  print(f"Line 178-179: ZREVRANK leaderboard player3 -> #{new_rank + 1}")
```

**Output:**

```
Line 153-161: ZADD leaderboard -> {player:score pairs}
Line 164-165: ZREVRANGE leaderboard 0 2 WITHSCORES ->
  #1: player2 - 2300 points
  #2: player4 - 2100 points
  #3: player5 - 1950 points
Line 170-171: ZREVRANK leaderboard player3 -> #4
Line 174-175: ZINCRBY leaderboard 500 player3 -> 2300
Line 178-179: ZREVRANK leaderboard player3 -> #1
```

**Annotations:**

- **Lines 155-162**: `ZADD` adds members with scores (automatically sorted by score)
- **Lines 165-168**: `ZREVRANGE` returns top N members in descending order (highest scores first)
- **Lines 171-172**: `ZREVRANK` returns member's rank (player3 was #4 with score 1800)
- **Lines 175-176**: `ZINCRBY` increases player3's score by 500 (1800 + 500 = 2300)
- **Lines 179-180**: After increment, player3 ties with player2 at 2300 points and becomes #1

**Use Case:** Sorted sets are perfect for leaderboards, rankings, priority queues, and time-series data.

---

### 6. Key Expiration

**Source Code (Lines 187-208):**

```python
187:  # Set key with 3-second expiration
188:  r.setex("temp:data", 3, "This will expire soon")
189:  print(f"Line 187-188: SETEX temp:data 3 -> 'This will expire soon'")
190:
191:  # Check if key exists
192:  exists = r.exists("temp:data")
193:  print(f"Line 191-192: EXISTS temp:data -> {bool(exists)}")
194:
195:  # Wait 2 seconds
196:  print(f"Line 195-196: Waiting 2 seconds...")
197:  time.sleep(2)
198:
199:  # Check TTL
200:  ttl = r.ttl("temp:data")
201:  print(f"Line 199-200: TTL temp:data -> {ttl} second(s)")
202:
203:  # Wait for expiration
204:  print(f"Line 203-204: Waiting 2 more seconds...")
205:  time.sleep(2)
206:
207:  # Check if key still exists
208:  exists = r.exists("temp:data")
209:  print(f"Line 207-208: EXISTS temp:data -> {bool(exists)} (expired)")
```

**Output:**

```
Line 187-188: SETEX temp:data 3 -> 'This will expire soon'
Line 191-192: EXISTS temp:data -> True
Line 195-196: Waiting 2 seconds...
Line 199-200: TTL temp:data -> 1 second(s)
Line 203-204: Waiting 2 more seconds...
Line 207-208: EXISTS temp:data -> False (expired)
```

**Annotations:**

- **Lines 188-189**: Key created with 3-second TTL
- **Lines 192-193**: `EXISTS` confirms key is present initially
- **Lines 197-201**: After 2 seconds, TTL shows 1 second remaining
- **Lines 205-209**: After total 4 seconds, key has expired and no longer exists

**Use Case:** Automatic expiration is ideal for session management, caching, rate limiting, and temporary data.

---

### 7. Transactions (MULTI/EXEC)

**Source Code (Lines 216-230):**

```python
216:  # Execute multiple commands atomically
217:  r.set("balance:alice", 1000)
218:  r.set("balance:bob", 500)
219:  print(f"Line 216-218: Initial balances -> Alice: 1000, Bob: 500")
220:
221:  # Transfer 100 from Alice to Bob
222:  pipe = r.pipeline()
223:  pipe.decrby("balance:alice", 100)
224:  pipe.incrby("balance:bob", 100)
225:  results = pipe.execute()
226:  print(f"Line 221-225: MULTI/EXEC Transfer 100 from Alice to Bob")
227:
228:  # Check final balances
229:  alice_balance = r.get("balance:alice")
230:  bob_balance = r.get("balance:bob")
231:  print(f"Line 228-230: Final balances -> Alice: {alice_balance.decode()}, Bob: {bob_balance.decode()}")
```

**Output:**

```
Line 216-218: Initial balances -> Alice: 1000, Bob: 500
Line 221-225: MULTI/EXEC Transfer 100 from Alice to Bob
Line 228-230: Final balances -> Alice: 900, Bob: 600
```

**Annotations:**

- **Lines 217-219**: Set up initial account balances
- **Lines 222-226**: Pipeline executes both commands atomically (no other commands can interleave)
- **Lines 229-231**: Transfer completed successfully: Alice 1000→900, Bob 500→600

**Use Case:** Transactions ensure atomic operations for financial transfers, inventory management, and any multi-step operation that must complete fully or not at all.

---

### 8. Pipeline (Performance Optimization)

**Source Code (Lines 238-256):**

```python
238:  # Without pipeline
239:  start = time.time()
240:  for i in range(100):
241:      r.set(f"key:{i}", f"value{i}")
242:  without_pipeline = time.time() - start
243:  print(f"Line 238-242: Set 100 keys WITHOUT pipeline -> {without_pipeline:.4f}s")
244:
245:  # With pipeline
246:  r.delete(*[f"pkey:{i}" for i in range(100)])
247:  start = time.time()
248:  pipe = r.pipeline()
249:  for i in range(100):
250:      pipe.set(f"pkey:{i}", f"value{i}")
251:  pipe.execute()
252:  with_pipeline = time.time() - start
253:  print(f"Line 245-252: Set 100 keys WITH pipeline -> {with_pipeline:.4f}s")
254:
255:  # Performance improvement
256:  speedup = without_pipeline / with_pipeline
257:  print(f"Line 255-256: Pipeline is {speedup:.1f}x faster")
```

**Output:**

```
Line 238-242: Set 100 keys WITHOUT pipeline -> 0.0245s
Line 245-252: Set 100 keys WITH pipeline -> 0.0015s
Line 255-256: Pipeline is 16.2x faster
```

**Annotations:**

- **Lines 239-243**: Without pipeline, each SET command requires a round-trip to server (100 round-trips)
- **Lines 247-253**: Pipeline batches all 100 commands into a single request
- **Lines 256-257**: Pipeline achieves **16.2x speedup** by reducing network round-trips

**Use Case:** Pipelines dramatically improve performance for batch operations, bulk imports, and any scenario with multiple independent commands.

---

### 9. Pub/Sub Messaging

**Source Code (Lines 264-289):**

```python
264:  print("Line 264: Creating separate connections for publisher and subscriber")
265:
266:  # Note: Real pub/sub requires separate connections and threads
267:  # This is a simplified demonstration
268:  publisher = redis.Redis(host='localhost', port=6379, decode_responses=True)
269:  subscriber = redis.Redis(host='localhost', port=6379, decode_responses=True)
270:
271:  pubsub = subscriber.pubsub()
272:  pubsub.subscribe("news:tech")
273:  print(f"Line 271-273: SUBSCRIBE news:tech")
274:
275:  # Skip subscription confirmation message
276:  pubsub.get_message()
277:
278:  # Publish messages
279:  publisher.publish("news:tech", "Python 3.13 released!")
280:  publisher.publish("news:tech", "Redis 7.2 now available!")
281:  print(f"Line 277-279: PUBLISH news:tech -> 2 messages sent")
282:
283:  # Receive messages
284:  print(f"Line 282: Receiving messages:")
285:  for _ in range(2):
286:      time.sleep(0.1)
287:      message = pubsub.get_message()
288:      if message and message['type'] == 'message':
289:          print(f"  -> {message['data']}")
```

**Output:**

```
Line 264: Creating separate connections for publisher and subscriber
Line 271-273: SUBSCRIBE news:tech
Line 277-279: PUBLISH news:tech -> 2 messages sent
Line 282: Receiving messages:
  -> Python 3.13 released!
  -> Redis 7.2 now available!
```

**Annotations:**

- **Lines 268-269**: Pub/Sub requires separate Redis connections for publisher and subscriber
- **Lines 271-273**: Subscriber subscribes to the "news:tech" channel
- **Lines 279-281**: Publisher broadcasts 2 messages to the channel
- **Lines 285-289**: Subscriber receives both messages in order

**Use Case:** Pub/Sub enables real-time messaging, chat applications, notification systems, and event broadcasting.

---

## Performance Comparison

The pipeline demonstration shows significant performance gains:

| Method | Time | Operations |
|--------|------|------------|
| Without Pipeline | 0.0245s | 100 individual SET commands |
| With Pipeline | 0.0015s | 100 batched SET commands |
| **Speedup** | **16.2x** | **Network round-trip reduction** |

**Key Insight:** Pipelines reduce network latency by batching multiple commands into a single request/response cycle.

---

## Redis Data Structure Use Cases

| Data Structure | Primary Use Cases |
|----------------|-------------------|
| **Strings** | Simple caching, session storage, counters, feature flags |
| **Lists** | Task queues, activity feeds, recent items, message queues |
| **Sets** | Unique items, tags, social graphs (followers), membership checks |
| **Hashes** | Object storage (users, products), session data, configuration |
| **Sorted Sets** | Leaderboards, rankings, time-series data, priority queues |

---

## Key Takeaways

1. **Atomic Operations**: Commands like INCR, DECR, HINCRBY are thread-safe and atomic
2. **Expiration**: Built-in TTL support eliminates need for manual cleanup
3. **Rich Data Types**: Different structures optimize for different access patterns
4. **Performance**: Pipelines dramatically reduce latency for bulk operations
5. **Pub/Sub**: Built-in message broadcasting without external message brokers
6. **Transactions**: MULTI/EXEC ensures atomicity for multi-step operations

---

## Additional Resources

- **Redis Documentation**: https://redis.io/docs/
- **redis-py Documentation**: https://redis-py.readthedocs.io/
- **Redis Commands Reference**: https://redis.io/commands/
- **Redis Data Types**: https://redis.io/docs/data-types/

---

*This example requires Redis server running locally on port 6379. Use `redis-server` to start the server, or run Redis in Docker: `docker run -d -p 6379:6379 redis:latest`*
