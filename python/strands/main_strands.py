# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Strands Agentic Workflow Pattern in Python

This example demonstrates the "strands" pattern for agentic workflows:
1. Multiple independent execution strands (threads of work)
2. Concurrent task processing with asyncio
3. State management for each strand
4. Communication and coordination between strands
5. Synchronization points and result aggregation
6. Error handling in concurrent contexts

The strands pattern is ideal for:
- Multi-agent systems where agents work independently
- Parallel data processing pipelines
- Concurrent API requests or I/O operations
- Distributed task execution
"""

import asyncio
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


# ============================================================================
# SECTION 1: Strand State and Configuration
# ============================================================================


class StrandStatus(Enum):
    """Status states for a strand."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


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

    @property
    def duration(self) -> float:
        """Calculate execution duration."""
        if self.end_time > 0:
            return self.end_time - self.start_time
        return 0.0


# ============================================================================
# SECTION 2: Basic Strand Operations
# ============================================================================


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
            # Simulate processing work
            await asyncio.sleep(0.1)

            # Process the value
            result = value * 2
            strand_state.results.append(result)
            strand_state.progress = int((i + 1) / len(data) * 100)

            print(
                f"[{strand_state.strand_id}] Processed {value} -> {result} "
                f"(Progress: {strand_state.progress}%)"
            )

        strand_state.status = StrandStatus.COMPLETED
        print(f"[{strand_state.strand_id}] ✓ Completed successfully")

    except Exception as e:
        strand_state.status = StrandStatus.FAILED
        strand_state.errors.append(str(e))
        print(f"[{strand_state.strand_id}] ✗ Failed: {e}")

    finally:
        strand_state.end_time = time.time()


async def fetch_data_strand(strand_state: StrandState, urls: list[str]) -> None:
    """
    Strand 2: Simulate API data fetching.
    Line 108-133: Shows concurrent I/O simulation with varying delays.
    """
    print(f"\n[{strand_state.strand_id}] Starting data fetch...")
    strand_state.status = StrandStatus.RUNNING
    strand_state.start_time = time.time()

    try:
        for i, url in enumerate(urls):
            # Simulate varying network delays
            delay = 0.05 * (i + 1)
            await asyncio.sleep(delay)

            # Simulate fetched data
            data = f"data_from_{url}"
            strand_state.results.append(data)
            strand_state.progress = int((i + 1) / len(urls) * 100)

            print(
                f"[{strand_state.strand_id}] Fetched {url} -> {data} "
                f"(Progress: {strand_state.progress}%)"
            )

        strand_state.status = StrandStatus.COMPLETED
        print(f"[{strand_state.strand_id}] ✓ Completed successfully")

    except Exception as e:
        strand_state.status = StrandStatus.FAILED
        strand_state.errors.append(str(e))
        print(f"[{strand_state.strand_id}] ✗ Failed: {e}")

    finally:
        strand_state.end_time = time.time()


async def analyze_strand(strand_state: StrandState, items: list[str]) -> None:
    """
    Strand 3: Analyze text data.
    Line 146-173: Demonstrates analysis with conditional logic.
    """
    print(f"\n[{strand_state.strand_id}] Starting analysis...")
    strand_state.status = StrandStatus.RUNNING
    strand_state.start_time = time.time()

    try:
        for i, item in enumerate(items):
            await asyncio.sleep(0.08)

            # Simple analysis: count characters and words
            analysis = {
                "item": item,
                "length": len(item),
                "words": len(item.split()),
                "uppercase": sum(1 for c in item if c.isupper()),
            }
            strand_state.results.append(analysis)
            strand_state.progress = int((i + 1) / len(items) * 100)

            print(
                f"[{strand_state.strand_id}] Analyzed '{item}': "
                f"{analysis['words']} words, {analysis['length']} chars "
                f"(Progress: {strand_state.progress}%)"
            )

        strand_state.status = StrandStatus.COMPLETED
        print(f"[{strand_state.strand_id}] ✓ Completed successfully")

    except Exception as e:
        strand_state.status = StrandStatus.FAILED
        strand_state.errors.append(str(e))
        print(f"[{strand_state.strand_id}] ✗ Failed: {e}")

    finally:
        strand_state.end_time = time.time()


# ============================================================================
# SECTION 3: Strand Coordinator
# ============================================================================


class StrandCoordinator:
    """
    Coordinates multiple strands of execution.
    Line 193-267: Central coordinator for managing concurrent strands.
    """

    def __init__(self):
        self.strands: dict[str, StrandState] = {}
        self.start_time: float = 0.0
        self.end_time: float = 0.0

    def register_strand(self, strand_state: StrandState) -> None:
        """Register a strand for tracking."""
        self.strands[strand_state.strand_id] = strand_state
        print(f"[Coordinator] Registered strand: {strand_state.strand_id}")

    async def run_strands_parallel(
        self, strand_tasks: list[tuple[StrandState, Any]]
    ) -> None:
        """
        Run multiple strands concurrently.
        Line 212-223: Core concurrent execution using asyncio.gather().
        """
        print("\n" + "=" * 70)
        print("RUNNING STRANDS IN PARALLEL")
        print("=" * 70)

        self.start_time = time.time()

        # Create tasks for all strands
        tasks = [task for _, task in strand_tasks]

        # Execute all strands concurrently
        await asyncio.gather(*tasks)

        self.end_time = time.time()

    async def run_strands_sequential(
        self, strand_tasks: list[tuple[StrandState, Any]]
    ) -> None:
        """
        Run strands one after another (for comparison).
        Line 234-245: Sequential execution for performance comparison.
        """
        print("\n" + "=" * 70)
        print("RUNNING STRANDS SEQUENTIALLY")
        print("=" * 70)

        self.start_time = time.time()

        for _, task in strand_tasks:
            await task

        self.end_time = time.time()

    def print_summary(self) -> None:
        """
        Print execution summary for all strands.
        Line 251-278: Comprehensive reporting of strand results.
        """
        print("\n" + "=" * 70)
        print("EXECUTION SUMMARY")
        print("=" * 70)

        total_duration = self.end_time - self.start_time
        print(f"\nTotal execution time: {total_duration:.3f}s\n")

        for strand_id, state in self.strands.items():
            status_symbol = "✓" if state.status == StrandStatus.COMPLETED else "✗"
            print(f"{status_symbol} Strand: {strand_id}")
            print(f"  Task: {state.task_name}")
            print(f"  Status: {state.status.value}")
            print(f"  Duration: {state.duration:.3f}s")
            print(f"  Progress: {state.progress}%")
            print(f"  Results count: {len(state.results)}")

            if state.errors:
                print(f"  Errors: {', '.join(state.errors)}")

            print()


# ============================================================================
# SECTION 4: Advanced Patterns - Strand Communication
# ============================================================================


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
        self.messages.append(f"{sender}: {message}")
        print(f"[Channel] {sender} → {message}")

    async def receive(self, receiver: str, timeout: float = 0.1) -> str | None:
        """Receive a message from the channel."""
        try:
            sender, message = await asyncio.wait_for(self.queue.get(), timeout)
            print(f"[Channel] {receiver} ← {message} (from {sender})")
            return message
        except asyncio.TimeoutError:
            return None


async def producer_strand(
    strand_state: StrandState, channel: SharedChannel, count: int
) -> None:
    """
    Producer strand: generates data and sends to channel.
    Line 325-349: Demonstrates producer pattern with channel communication.
    """
    print(f"\n[{strand_state.strand_id}] Starting producer...")
    strand_state.status = StrandStatus.RUNNING
    strand_state.start_time = time.time()

    try:
        for i in range(count):
            await asyncio.sleep(0.05)
            message = f"item_{i}"
            await channel.send(message, strand_state.strand_id)
            strand_state.results.append(message)
            strand_state.progress = int((i + 1) / count * 100)

        # Signal completion
        await channel.send("DONE", strand_state.strand_id)
        strand_state.status = StrandStatus.COMPLETED
        print(f"[{strand_state.strand_id}] ✓ Producer completed")

    except Exception as e:
        strand_state.status = StrandStatus.FAILED
        strand_state.errors.append(str(e))
        print(f"[{strand_state.strand_id}] ✗ Failed: {e}")

    finally:
        strand_state.end_time = time.time()


async def consumer_strand(
    strand_state: StrandState, channel: SharedChannel, expected_count: int
) -> None:
    """
    Consumer strand: receives and processes data from channel.
    Line 362-391: Demonstrates consumer pattern with channel communication.
    """
    print(f"\n[{strand_state.strand_id}] Starting consumer...")
    strand_state.status = StrandStatus.RUNNING
    strand_state.start_time = time.time()

    try:
        processed = 0
        while processed < expected_count:
            message = await channel.receive(strand_state.strand_id, timeout=2.0)
            if message:
                if message == "DONE":
                    break
                # Process the message
                result = f"processed_{message}"
                strand_state.results.append(result)
                processed += 1
                strand_state.progress = int(processed / expected_count * 100)

        strand_state.status = StrandStatus.COMPLETED
        print(f"[{strand_state.strand_id}] ✓ Consumer completed")

    except Exception as e:
        strand_state.status = StrandStatus.FAILED
        strand_state.errors.append(str(e))
        print(f"[{strand_state.strand_id}] ✗ Failed: {e}")

    finally:
        strand_state.end_time = time.time()


# ============================================================================
# SECTION 5: Demonstration Functions
# ============================================================================


async def demo_parallel_strands() -> None:
    """
    Demonstrate parallel execution of multiple strands.
    Line 403-440: Shows concurrent execution with performance benefits.
    """
    print("\n" + "=" * 70)
    print("DEMO 1: PARALLEL STRANDS EXECUTION")
    print("=" * 70)

    coordinator = StrandCoordinator()

    # Create strand states
    strand1 = StrandState(strand_id="STRAND-1", task_name="Data Processing")
    strand2 = StrandState(strand_id="STRAND-2", task_name="Data Fetching")
    strand3 = StrandState(strand_id="STRAND-3", task_name="Data Analysis")

    # Register strands
    coordinator.register_strand(strand1)
    coordinator.register_strand(strand2)
    coordinator.register_strand(strand3)

    # Prepare tasks
    strand_tasks = [
        (strand1, process_data_strand(strand1, [1, 2, 3, 4, 5])),
        (
            strand2,
            fetch_data_strand(strand2, ["api/users", "api/posts", "api/comments"]),
        ),
        (
            strand3,
            analyze_strand(strand3, ["Hello World", "Strands Pattern", "Async Python"]),
        ),
    ]

    # Run in parallel
    await coordinator.run_strands_parallel(strand_tasks)
    coordinator.print_summary()


async def demo_sequential_strands() -> None:
    """
    Demonstrate sequential execution (for comparison).
    Line 447-476: Shows sequential execution for performance comparison.
    """
    print("\n" + "=" * 70)
    print("DEMO 2: SEQUENTIAL STRANDS EXECUTION (FOR COMPARISON)")
    print("=" * 70)

    coordinator = StrandCoordinator()

    # Create strand states
    strand1 = StrandState(strand_id="STRAND-A", task_name="Data Processing")
    strand2 = StrandState(strand_id="STRAND-B", task_name="Data Fetching")
    strand3 = StrandState(strand_id="STRAND-C", task_name="Data Analysis")

    coordinator.register_strand(strand1)
    coordinator.register_strand(strand2)
    coordinator.register_strand(strand3)

    strand_tasks = [
        (strand1, process_data_strand(strand1, [1, 2, 3, 4, 5])),
        (
            strand2,
            fetch_data_strand(strand2, ["api/users", "api/posts", "api/comments"]),
        ),
        (
            strand3,
            analyze_strand(strand3, ["Hello World", "Strands Pattern", "Async Python"]),
        ),
    ]

    # Run sequentially
    await coordinator.run_strands_sequential(strand_tasks)
    coordinator.print_summary()


async def demo_strand_communication() -> None:
    """
    Demonstrate communication between strands.
    Line 483-512: Shows producer-consumer pattern with inter-strand communication.
    """
    print("\n" + "=" * 70)
    print("DEMO 3: STRAND COMMUNICATION (PRODUCER-CONSUMER)")
    print("=" * 70)

    coordinator = StrandCoordinator()
    channel = SharedChannel()

    # Create strands
    producer = StrandState(strand_id="PRODUCER", task_name="Data Generation")
    consumer = StrandState(strand_id="CONSUMER", task_name="Data Processing")

    coordinator.register_strand(producer)
    coordinator.register_strand(consumer)

    # Run producer and consumer concurrently
    await coordinator.run_strands_parallel(
        [
            (producer, producer_strand(producer, channel, 5)),
            (consumer, consumer_strand(consumer, channel, 5)),
        ]
    )

    coordinator.print_summary()

    print(f"\nChannel message history ({len(channel.messages)} messages):")
    for msg in channel.messages:
        print(f"  • {msg}")


# ============================================================================
# SECTION 6: Main Entry Point
# ============================================================================


async def main() -> None:
    """Main entry point for strands workflow demonstration."""
    print("\n" + "=" * 70)
    print("STRANDS AGENTIC WORKFLOW PATTERN")
    print("=" * 70)
    print("\nDemonstrating concurrent execution of independent work strands")
    print("Using Python's asyncio for efficient concurrent operations")
    print("=" * 70)

    # Run all demonstrations
    await demo_parallel_strands()
    await demo_sequential_strands()
    await demo_strand_communication()

    print("\n" + "=" * 70)
    print("ALL DEMONSTRATIONS COMPLETE")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  1. Parallel strands execute concurrently for better performance")
    print("  2. Each strand maintains independent state and lifecycle")
    print("  3. Strands can communicate through shared channels")
    print("  4. Error handling is isolated per strand")
    print("  5. Coordinator manages and monitors all strands")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
