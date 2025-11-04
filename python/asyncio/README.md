# Asyncio Example: Concurrent Asynchronous Programming

This example demonstrates the power of Python's `asyncio` library for writing concurrent code using async/await syntax.

## Key Concepts Illustrated

1. **Concurrent vs Sequential Execution** - Shows performance benefits
2. **Task Creation and Management** - Working with asyncio tasks
3. **Error Handling** - Graceful error handling in async code
4. **Async Context Managers** - Resource management with `async with`

## Running the Example

```bash
uv run python main_asyncio.py
```

## Source Code and Output Analysis

### 1. Sequential vs Concurrent Execution

**Source Code (main_asyncio.py:50-65):**
```python
# Sequential execution (slow)
log_time("\n🐌 Sequential Execution:")
start = time.time()
result1 = await fetch_data("API-1", 1.0)  # Line 53: Wait 1s
result2 = await fetch_data("API-2", 1.0)  # Line 54: Wait 1s
result3 = await fetch_data("API-3", 1.0)  # Line 55: Wait 1s
sequential_time = time.time() - start
log_time(f"⏱️  Sequential time: {sequential_time:.2f}s\n")

# Concurrent execution (fast)
log_time("🚀 Concurrent Execution (using asyncio.gather):")
start = time.time()
results = await asyncio.gather(           # Line 62: All start together
    fetch_data("API-1", 1.0),
    fetch_data("API-2", 1.0),
    fetch_data("API-3", 1.0),
)
```

**Output:**
```
[08:35:43.406] 🐌 Sequential Execution:
[08:35:43.406] 📥 Starting to fetch API-1...
[08:35:44.412] ✅ Finished fetching API-1      ← Line 53 completed (1s later)
[08:35:44.412] 📥 Starting to fetch API-2...
[08:35:45.419] ✅ Finished fetching API-2      ← Line 54 completed (1s later)
[08:35:45.419] 📥 Starting to fetch API-3...
[08:35:46.427] ✅ Finished fetching API-3      ← Line 55 completed (1s later)
[08:35:46.427] ⏱️  Sequential time: 3.02s      ← Total: ~3 seconds

[08:35:46.427] 🚀 Concurrent Execution (using asyncio.gather):
[08:35:46.427] 📥 Starting to fetch API-1...   ← Line 62: All three start
[08:35:46.427] 📥 Starting to fetch API-2...   ← at the same time!
[08:35:46.427] 📥 Starting to fetch API-3...
[08:35:47.433] ✅ Finished fetching API-1      ← All three finish
[08:35:47.433] ✅ Finished fetching API-2      ← at the same time!
[08:35:47.434] ✅ Finished fetching API-3
[08:35:47.434] ⏱️  Concurrent time: 1.01s      ← Total: ~1 second
[08:35:47.434] ⚡ Speedup: 3.00x faster!       ← 3x performance improvement!
```

**💡 Key Insight:**
- **Sequential** (lines 53-55): Each `await` blocks until complete. Total time = 1s + 1s + 1s = 3s
- **Concurrent** (line 62): `asyncio.gather()` runs all tasks simultaneously. Total time = max(1s, 1s, 1s) = 1s

---

### 2. Task Creation and Management

**Source Code (main_asyncio.py:75-88):**
```python
# Create tasks
task1 = asyncio.create_task(fetch_data("Task-1", 0.5))  # Line 76
task2 = asyncio.create_task(fetch_data("Task-2", 0.3))  # Line 77
task3 = asyncio.create_task(fetch_data("Task-3", 0.7))  # Line 78

log_time(f"📋 Created 3 tasks")
log_time(f"   Task-1 status: {task1.done()}")            # Line 81
log_time(f"   Task-2 status: {task2.done()}")            # Line 82
log_time(f"   Task-3 status: {task3.done()}\n")          # Line 83

# Wait for all tasks
await asyncio.gather(task1, task2, task3)                # Line 86

log_time(f"\n📋 All tasks completed!")
log_time(f"   Task-1 result: {task1.result()}")         # Line 89
```

**Output:**
```
[08:35:47.434] 📋 Created 3 tasks
[08:35:47.434]    Task-1 status: False         ← Line 81: Tasks created but not done
[08:35:47.434]    Task-2 status: False         ← Line 82: Tasks are now running
[08:35:47.434]    Task-3 status: False         ← Line 83: in the background

[08:35:47.434] 📥 Starting to fetch Task-1...
[08:35:47.434] 📥 Starting to fetch Task-2...
[08:35:47.434] 📥 Starting to fetch Task-3...
[08:35:47.737] ✅ Finished fetching Task-2     ← Fastest (0.3s)
[08:35:47.944] ✅ Finished fetching Task-1     ← Medium (0.5s)
[08:35:48.152] ✅ Finished fetching Task-3     ← Slowest (0.7s)

[08:35:48.152] 📋 All tasks completed!         ← Line 86: gather() completed
[08:35:48.152]    Task-1 result: Data from Task-1  ← Line 89: Can access results
```

**💡 Key Insight:**
- **Lines 76-78:** `create_task()` schedules tasks to run in the background immediately
- **Lines 81-83:** Tasks show `False` status because they haven't completed yet
- **Line 86:** `gather()` waits for all tasks to complete
- **Notice:** Tasks complete in order of duration (shortest first), not creation order!

---

### 3. Error Handling in Async Code

**Source Code (main_asyncio.py:99-105):**
```python
# Using return_exceptions=True to handle errors gracefully
results = await asyncio.gather(
    fetch_with_error_handling("Operation-1", 0.3, should_fail=False),  # Line 101
    fetch_with_error_handling("Operation-2", 0.5, should_fail=True),   # Line 102: Will fail!
    fetch_with_error_handling("Operation-3", 0.2, should_fail=False),  # Line 103
    return_exceptions=True,  # Line 104: Don't raise, return exceptions
)
```

**fetch_with_error_handling() function (main_asyncio.py:36-47):**
```python
async def fetch_with_error_handling(name, delay, should_fail=False):
    try:
        log_time(f"🔄 Starting {name}...")
        await asyncio.sleep(delay)
        if should_fail:                                    # Line 41
            raise ValueError(f"Simulated error in {name}") # Line 42
        log_time(f"✅ Completed {name}")
        return f"Success: {name}"
    except ValueError as e:                                # Line 45: Catch error
        log_time(f"❌ Error in {name}: {e}")
        return f"Failed: {name}"
```

**Output:**
```
[08:35:48.152] 🔄 Starting Operation-1...
[08:35:48.152] 🔄 Starting Operation-2...
[08:35:48.152] 🔄 Starting Operation-3...
[08:35:48.360] ✅ Completed Operation-3        ← Line 103: Success (0.2s)
[08:35:48.470] ✅ Completed Operation-1        ← Line 101: Success (0.3s)
[08:35:48.661] ❌ Error in Operation-2: ...    ← Line 102: Error (0.5s), but caught!

[08:35:48.661] 📊 Results:
[08:35:48.661]    Operation-1: Success: Operation-1  ← Returned normally
[08:35:48.661]    Operation-2: Failed: Operation-2   ← Error handled gracefully
[08:35:48.661]    Operation-3: Success: Operation-3  ← Returned normally
```

**💡 Key Insight:**
- **Line 104:** `return_exceptions=True` prevents one failure from canceling other tasks
- **Line 42:** Raises an exception, but...
- **Line 45:** ...the exception is caught and handled gracefully
- **Result:** All three operations complete; failures return error messages instead of crashing

---

### 4. Async Context Manager

**Source Code (main_asyncio.py:115-129):**
```python
class AsyncResourceManager:
    async def __aenter__(self):                           # Line 121: Called on entry
        log_time(f"🔓 Opening resource: {self.name}")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb): # Line 126: Called on exit
        log_time(f"🔒 Closing resource: {self.name}")
        await asyncio.sleep(0.1)

    async def use(self):                                  # Line 131
        log_time(f"⚙️  Using resource: {self.name}")
        await asyncio.sleep(0.2)
```

**Usage (main_asyncio.py:141-143):**
```python
async with AsyncResourceManager("Database Connection") as resource:  # Line 141
    await resource.use()                                             # Line 142
# Line 143: Automatically calls __aexit__
```

**Output:**
```
[08:35:48.661] 🔓 Opening resource: Database Connection   ← Line 121: __aenter__ called
[08:35:48.772] ⚙️  Using resource: Database Connection    ← Line 131: use() called
[08:35:48.979] 🔒 Closing resource: Database Connection   ← Line 126: __aexit__ called
[08:35:49.090]                                            ← Line 143: Cleanup complete
```

**💡 Key Insight:**
- **Line 121:** `__aenter__` handles async setup (e.g., opening DB connections)
- **Line 142:** Use the resource
- **Line 126:** `__aexit__` handles async cleanup (e.g., closing connections)
- **Guarantee:** Cleanup happens even if errors occur (like try/finally)

---

## Performance Summary

| Execution Type | Time | Speedup |
|----------------|------|---------|
| Sequential (3 × 1s tasks) | ~3.02s | 1.0x |
| Concurrent (3 × 1s tasks) | ~1.01s | **3.0x faster** |

## Key Takeaways

1. **`async`/`await`** - Define and call asynchronous functions
2. **`asyncio.gather()`** - Run multiple async operations concurrently
3. **`asyncio.create_task()`** - Schedule tasks to run in background
4. **`return_exceptions=True`** - Handle errors without stopping other tasks
5. **Async context managers** - Clean resource management with `async with`

## When to Use Asyncio

✅ **Good for:**
- I/O-bound operations (network requests, file I/O, database queries)
- Handling many concurrent connections (web servers, chat apps)
- Operations that spend time waiting

❌ **Not ideal for:**
- CPU-bound operations (use `multiprocessing` instead)
- Simple scripts without concurrent operations
- When you need true parallelism (asyncio is concurrent, not parallel)
