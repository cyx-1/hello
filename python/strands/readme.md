# Strands Agentic Workflow Pattern

This example demonstrates the **strands pattern** for building agentic workflows in Python. The strands pattern involves multiple independent execution threads (strands) that can run concurrently, maintain their own state, and communicate with each other.

## Requirements

- **Python Version**: >= 3.11
- **Dependencies**: None (uses only Python standard library)
- **Key Library**: `asyncio` for concurrent execution

## What is the Strands Pattern?

The strands pattern is a workflow architecture where:
1. **Multiple independent strands** execute concurrently
2. **Each strand maintains isolated state** (status, progress, results, errors)
3. **Strands can communicate** through shared channels
4. **Coordination layer** manages strand lifecycle and aggregates results
5. **Error handling** is isolated per strand, preventing cascade failures

This pattern is ideal for:
- Multi-agent AI systems
- Parallel data processing pipelines
- Concurrent API requests
- Distributed task execution

## Running the Example

```bash
uv run python main_strands.py
```

## Key Components

### 1. Strand State Management (Lines 48-60)

Each strand maintains its own state container:

```python
@dataclass
class StrandState:
    """
    State container for a single strand.
    Line 48-60: Each strand maintains its own isolated state.
    """
    strand_id: str
    task_name: str
    status: StrandStatus = StrandStatus.PENDING
    start_time: float = 0.0
    end_time: float = 0.0
    results: list[Any] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    progress: int = 0
```

**Output correlation**: You'll see state updates in the execution logs:
```
[STRAND-1] Processed 1 -> 2 (Progress: 20%)
[STRAND-1] Processed 2 -> 4 (Progress: 40%)
```

### 2. Basic Strand Operations (Lines 72-95)

Data processing strand that demonstrates async work:

```python
async def process_data_strand(strand_state: StrandState, data: list[int]) -> None:
    """
    Strand 1: Process numerical data.
    Line 72-95: Demonstrates a basic data processing strand.
    """
    print(f"\n[{strand_state.strand_id}] Starting data processing...")
    strand_state.status = StrandStatus.RUNNING
    strand_state.start_time = time.time()

    try:
        for i, value in enumerate(data):
            await asyncio.sleep(0.1)  # Simulate processing work
            result = value * 2
            strand_state.results.append(result)
            strand_state.progress = int((i + 1) / len(data) * 100)
            print(f"[{strand_state.strand_id}] Processed {value} -> {result}")
```

**Output**:
```
[STRAND-1] Starting data processing...
[STRAND-1] Processed 1 -> 2 (Progress: 20%)
[STRAND-1] Processed 2 -> 4 (Progress: 40%)
[STRAND-1] Processed 3 -> 6 (Progress: 60%)
[STRAND-1] Processed 4 -> 8 (Progress: 80%)
[STRAND-1] Processed 5 -> 10 (Progress: 100%)
[STRAND-1] ✓ Completed successfully
```

### 3. Concurrent Execution (Lines 212-223)

The coordinator runs multiple strands in parallel using `asyncio.gather()`:

```python
async def run_strands_parallel(self, strand_tasks: list[tuple[StrandState, Any]]) -> None:
    """
    Run multiple strands concurrently.
    Line 212-223: Core concurrent execution using asyncio.gather().
    """
    print("\nRUNNING STRANDS IN PARALLEL")
    self.start_time = time.time()

    # Create tasks for all strands
    tasks = [task for _, task in strand_tasks]

    # Execute all strands concurrently
    await asyncio.gather(*tasks)

    self.end_time = time.time()
```

**Output showing concurrent execution** (note how strands interleave):
```
[STRAND-1] Starting data processing...
[STRAND-2] Starting data fetch...
[STRAND-3] Starting analysis...
[STRAND-2] Fetched api/users -> data_from_api/users (Progress: 33%)
[STRAND-3] Analyzed 'Hello World': 2 words, 11 chars (Progress: 33%)
[STRAND-1] Processed 1 -> 2 (Progress: 20%)
[STRAND-2] Fetched api/posts -> data_from_api/posts (Progress: 66%)
```

Notice how the output is interleaved - this shows true concurrent execution!

### 4. Performance Comparison

**Parallel Execution** (Lines 403-440) - Total time: **0.504s**
```
Total execution time: 0.504s

✓ Strand: STRAND-1
  Duration: 0.504s
✓ Strand: STRAND-2
  Duration: 0.303s
✓ Strand: STRAND-3
  Duration: 0.245s
```

**Sequential Execution** (Lines 447-476) - Total time: **1.048s**
```
Total execution time: 1.048s

✓ Strand: STRAND-A
  Duration: 0.504s
✓ Strand: STRAND-B
  Duration: 0.303s
✓ Strand: STRAND-C
  Duration: 0.242s
```

**Performance gain**: Parallel execution is **~2x faster** (0.504s vs 1.048s)!

### 5. Inter-Strand Communication (Lines 290-315)

Strands can communicate through shared channels:

```python
class SharedChannel:
    """
    Communication channel between strands.
    Line 290-315: Enables inter-strand communication.
    """
    def __init__(self):
        self.queue: asyncio.Queue = asyncio.Queue()
        self.messages: list[str] = []

    async def send(self, message: str, sender: str) -> None:
        """Send a message to the channel."""
        await self.queue.put((sender, message))
        print(f"[Channel] {sender} → {message}")

    async def receive(self, receiver: str, timeout: float = 0.1) -> str | None:
        """Receive a message from the channel."""
        sender, message = await asyncio.wait_for(self.queue.get(), timeout)
        print(f"[Channel] {receiver} ← {message} (from {sender})")
        return message
```

**Producer-Consumer Pattern Output** (Lines 483-512):
```
[PRODUCER] Starting producer...
[CONSUMER] Starting consumer...
[Channel] PRODUCER → item_0
[Channel] CONSUMER ← item_0 (from PRODUCER)
[Channel] PRODUCER → item_1
[Channel] CONSUMER ← item_1 (from PRODUCER)
[Channel] PRODUCER → item_2
[Channel] CONSUMER ← item_2 (from PRODUCER)
```

The producer strand generates data while the consumer strand processes it concurrently.

### 6. Error Handling and State Tracking (Lines 251-278)

Each strand tracks its own errors independently:

```python
def print_summary(self) -> None:
    """
    Print execution summary for all strands.
    Line 251-278: Comprehensive reporting of strand results.
    """
    for strand_id, state in self.strands.items():
        status_symbol = "✓" if state.status == StrandStatus.COMPLETED else "✗"
        print(f"{status_symbol} Strand: {strand_id}")
        print(f"  Status: {state.status.value}")
        print(f"  Duration: {state.duration:.3f}s")
        print(f"  Progress: {state.progress}%")
        print(f"  Results count: {len(state.results)}")
        if state.errors:
            print(f"  Errors: {', '.join(state.errors)}")
```

**Summary Output**:
```
✓ Strand: STRAND-1
  Task: Data Processing
  Status: completed
  Duration: 0.504s
  Progress: 100%
  Results count: 5

✓ Strand: STRAND-2
  Task: Data Fetching
  Status: completed
  Duration: 0.303s
  Progress: 100%
  Results count: 3
```

## Complete Output

```
======================================================================
STRANDS AGENTIC WORKFLOW PATTERN
======================================================================

Demonstrating concurrent execution of independent work strands
Using Python's asyncio for efficient concurrent operations
======================================================================

======================================================================
DEMO 1: PARALLEL STRANDS EXECUTION
======================================================================
[Coordinator] Registered strand: STRAND-1
[Coordinator] Registered strand: STRAND-2
[Coordinator] Registered strand: STRAND-3

======================================================================
RUNNING STRANDS IN PARALLEL
======================================================================

[STRAND-1] Starting data processing...
[STRAND-2] Starting data fetch...
[STRAND-3] Starting analysis...
[STRAND-2] Fetched api/users -> data_from_api/users (Progress: 33%)
[STRAND-3] Analyzed 'Hello World': 2 words, 11 chars (Progress: 33%)
[STRAND-1] Processed 1 -> 2 (Progress: 20%)
[STRAND-2] Fetched api/posts -> data_from_api/posts (Progress: 66%)
[STRAND-3] Analyzed 'Strands Pattern': 2 words, 15 chars (Progress: 66%)
[STRAND-1] Processed 2 -> 4 (Progress: 40%)
[STRAND-3] Analyzed 'Async Python': 2 words, 12 chars (Progress: 100%)
[STRAND-3] ✓ Completed successfully
[STRAND-2] Fetched api/comments -> data_from_api/comments (Progress: 100%)
[STRAND-2] ✓ Completed successfully
[STRAND-1] Processed 3 -> 6 (Progress: 60%)
[STRAND-1] Processed 4 -> 8 (Progress: 80%)
[STRAND-1] Processed 5 -> 10 (Progress: 100%)
[STRAND-1] ✓ Completed successfully

======================================================================
EXECUTION SUMMARY
======================================================================

Total execution time: 0.504s

✓ Strand: STRAND-1
  Task: Data Processing
  Status: completed
  Duration: 0.504s
  Progress: 100%
  Results count: 5

✓ Strand: STRAND-2
  Task: Data Fetching
  Status: completed
  Duration: 0.303s
  Progress: 100%
  Results count: 3

✓ Strand: STRAND-3
  Task: Data Analysis
  Status: completed
  Duration: 0.245s
  Progress: 100%
  Results count: 3

======================================================================
DEMO 2: SEQUENTIAL STRANDS EXECUTION (FOR COMPARISON)
======================================================================

Total execution time: 1.048s
(Sequential execution takes ~2x longer than parallel)

======================================================================
DEMO 3: STRAND COMMUNICATION (PRODUCER-CONSUMER)
======================================================================

[PRODUCER] Starting producer...
[CONSUMER] Starting consumer...
[Channel] PRODUCER → item_0
[Channel] CONSUMER ← item_0 (from PRODUCER)
[Channel] PRODUCER → item_1
[Channel] CONSUMER ← item_1 (from PRODUCER)
[Channel] PRODUCER → item_2
[Channel] CONSUMER ← item_2 (from PRODUCER)
[Channel] PRODUCER → item_3
[Channel] CONSUMER ← item_3 (from PRODUCER)
[Channel] PRODUCER → item_4
[Channel] PRODUCER → DONE
[PRODUCER] ✓ Producer completed
[Channel] CONSUMER ← item_4 (from PRODUCER)
[CONSUMER] ✓ Consumer completed

======================================================================
ALL DEMONSTRATIONS COMPLETE
======================================================================

Key Takeaways:
  1. Parallel strands execute concurrently for better performance
  2. Each strand maintains independent state and lifecycle
  3. Strands can communicate through shared channels
  4. Error handling is isolated per strand
  5. Coordinator manages and monitors all strands
======================================================================
```

## Key Concepts Demonstrated

### 1. **Concurrency vs Parallelism**
- Lines 212-223: `asyncio.gather()` enables concurrent execution
- The output shows interleaved execution, proving true concurrency
- Performance benchmark shows ~2x speedup for parallel vs sequential

### 2. **State Isolation**
- Lines 48-60: Each strand has isolated state
- No shared mutable state between strands (except explicit channels)
- Prevents race conditions and makes debugging easier

### 3. **Communication Patterns**
- Lines 290-315: Producer-consumer via asyncio.Queue
- Lines 325-391: Demonstrate message passing between strands
- Decoupled communication allows flexible workflow composition

### 4. **Coordinator Pattern**
- Lines 193-267: Central coordinator manages all strands
- Tracks lifecycle, collects results, handles errors
- Provides unified interface for complex multi-strand workflows

### 5. **Error Resilience**
- Lines 72-95: Try-catch blocks in each strand
- Errors are captured in strand state, not propagated
- One strand's failure doesn't crash entire workflow

## Use Cases

1. **Multi-Agent AI Systems**: Multiple AI agents working on different tasks concurrently
2. **Data Pipelines**: Parallel ETL operations on different data sources
3. **API Orchestration**: Concurrent calls to multiple APIs with result aggregation
4. **Distributed Computing**: Coordinating work across multiple workers
5. **Real-time Systems**: Processing multiple event streams simultaneously

## Language Version Notes

- **Python 3.11+** is required for:
  - Modern `async`/`await` syntax improvements
  - Type hints with `|` operator (e.g., `str | None`)
  - Performance improvements in asyncio

- **Standard library only** - no external dependencies needed!
