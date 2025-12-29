# Claude Code Usage Tracker

A Python demonstration of tracking and analyzing Claude Code API usage, including request counting, token usage, cost calculation, and rate limit monitoring.

## Overview

This example demonstrates how to build a comprehensive usage tracking system for Claude Code that monitors:
- API requests by type (completion, streaming, tool use, vision)
- Token consumption (input/output)
- Cost calculation based on 2025 pricing
- Rate limit monitoring
- Usage analytics and reporting

## Running the Example

```bash
uv run python main_ccusage_monitor.py
```

## Source Code

### Key Data Structures (Lines 23-57)

```python
# Line 23: Define usage event types
class EventType(Enum):
    COMPLETION = "completion"
    STREAMING = "streaming"
    TOOL_USE = "tool_use"
    VISION = "vision"


# Line 31: Define model pricing structure (as of 2025)
@dataclass
class ModelPricing:
    model_name: str
    input_tokens_per_million: float
    output_tokens_per_million: float


MODEL_PRICING = {
    "claude-sonnet-4-5": ModelPricing(
        model_name="Claude 4.5 Sonnet",
        input_tokens_per_million=3.00,
        output_tokens_per_million=15.00,
    ),
    "claude-opus-4-5": ModelPricing(
        model_name="Claude 4.5 Opus",
        input_tokens_per_million=15.00,
        output_tokens_per_million=75.00,
    ),
    "claude-haiku-3-5": ModelPricing(
        model_name="Claude 3.5 Haiku",
        input_tokens_per_million=0.80,
        output_tokens_per_million=4.00,
    ),
}
```

**Annotation:** Lines 23-57 define the core data structures using Python's `dataclass` and `Enum`. The pricing shows that Haiku is 10-20x cheaper than Opus, making it ideal for simple tasks. Python's type hints provide static analysis benefits similar to TypeScript.

### Usage Tracker Class (Lines 71-141)

```python
# Line 71: Claude Code Usage Tracker class
class ClaudeCodeUsageTracker:
    def __init__(self):
        self.events: list[UsageEvent] = []
        self.start_time = datetime.now()
        print("=== Claude Code Usage Tracker Initialized ===")
        print(f"Start time: {self.start_time.isoformat()}Z\n")

    # Line 80: Track a new usage event
    def track_event(
        self,
        event_type: EventType,
        model_id: str,
        input_tokens: int,
        output_tokens: int,
        duration_ms: int,
        success: bool,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        event = UsageEvent(
            timestamp=datetime.now(),
            event_type=event_type,
            model_id=model_id,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            duration_ms=duration_ms,
            success=success,
            metadata=metadata or {},
        )
        self.events.append(event)

    # Line 104: Calculate cost for a single event
    def _calculate_event_cost(self, event: UsageEvent) -> float:
        pricing = MODEL_PRICING.get(event.model_id)
        if not pricing:
            return 0.0

        input_cost = (event.input_tokens / 1_000_000) * pricing.input_tokens_per_million
        output_cost = (event.output_tokens / 1_000_000) * pricing.output_tokens_per_million
        return input_cost + output_cost

    # Line 116: Get total usage statistics
    def get_total_usage(self) -> dict[str, float]:
        total_requests = len(self.events)
        total_input_tokens = sum(e.input_tokens for e in self.events)
        total_output_tokens = sum(e.output_tokens for e in self.events)
        total_tokens = total_input_tokens + total_output_tokens
        total_cost = sum(self._calculate_event_cost(e) for e in self.events)
        avg_duration_ms = (
            sum(e.duration_ms for e in self.events) / total_requests
            if total_requests > 0
            else 0
        )
        success_count = sum(1 for e in self.events if e.success)
        success_rate = (success_count / total_requests * 100) if total_requests > 0 else 0

        return {
            "total_requests": total_requests,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "total_tokens": total_tokens,
            "total_cost": total_cost,
            "avg_duration_ms": avg_duration_ms,
            "success_rate": success_rate,
        }
```

**Annotation:** Lines 71-141 implement the core tracking functionality using Python's list comprehensions and generator expressions. The `track_event()` method (line 80) captures each API call with a timestamp, while `_calculate_event_cost()` (line 104) computes costs based on input/output token pricing. The `get_total_usage()` method (line 116) uses Python's `sum()` built-in with generator expressions for efficient aggregation.

### Usage Breakdown by Model (Lines 143-163)

```python
# Line 143: Get usage breakdown by model
def get_usage_by_model(self) -> dict[str, dict[str, float]]:
    model_stats: dict[str, dict[str, float]] = {}

    for event in self.events:
        if event.model_id not in model_stats:
            model_stats[event.model_id] = {
                "requests": 0,
                "input_tokens": 0,
                "output_tokens": 0,
                "cost": 0.0,
            }

        stats = model_stats[event.model_id]
        stats["requests"] += 1
        stats["input_tokens"] += event.input_tokens
        stats["output_tokens"] += event.output_tokens
        stats["cost"] += self._calculate_event_cost(event)

    return model_stats
```

**Annotation:** Lines 143-163 provide model-level analytics using Python dictionaries. This allows you to see which Claude models (Sonnet, Opus, Haiku) you're using most and their respective costs, crucial for cost optimization.

### Rate Limit Monitoring (Lines 256-278)

```python
# Line 256: Check if approaching rate limits
def check_rate_limits(
    self, requests_per_minute_limit: int = 50, tokens_per_minute_limit: int = 40000
) -> None:
    one_minute_ago = datetime.now() - timedelta(minutes=1)
    recent_events = [e for e in self.events if e.timestamp >= one_minute_ago]

    requests_last_minute = len(recent_events)
    tokens_last_minute = sum(
        e.input_tokens + e.output_tokens for e in recent_events
    )

    print("🚦 Rate Limit Status:")
    print(f"   Requests (last minute): {requests_last_minute}/{requests_per_minute_limit}")
    print(f"   Tokens (last minute): {tokens_last_minute:,}/{tokens_per_minute_limit:,}")

    if requests_last_minute >= requests_per_minute_limit * 0.8:
        print("   ⚠️  Warning: Approaching request rate limit!")
    if tokens_last_minute >= tokens_per_minute_limit * 0.8:
        print("   ⚠️  Warning: Approaching token rate limit!")
    print()
```

**Annotation:** Lines 256-278 implement rate limit monitoring using Python's `timedelta` for date arithmetic and list comprehensions to filter recent events. The warning threshold is set at 80% to give advance notice before hitting limits. This is essential for production applications.

### Simulating Usage (Lines 286-366)

```python
# Line 286: Simulate various API calls
print("1. Code completion request (Sonnet)")
tracker.track_event(
    event_type=EventType.COMPLETION,
    model_id="claude-sonnet-4-5",
    input_tokens=1500,
    output_tokens=800,
    duration_ms=1250,
    success=True,
    metadata={"task": "code_generation"},
)

# Line 300: Simulate streaming response
tracker.track_event(
    event_type=EventType.STREAMING,
    model_id="claude-opus-4-5",
    input_tokens=3200,
    output_tokens=2500,
    duration_ms=3500,
    success=True,
    metadata={"task": "conversation"},
)

# Line 313: Simulate tool use
tracker.track_event(
    event_type=EventType.TOOL_USE,
    model_id="claude-sonnet-4-5",
    input_tokens=2100,
    output_tokens=450,
    duration_ms=980,
    success=True,
    metadata={"tools": ["bash", "grep", "edit"]},
)
```

**Annotation:** Lines 286-366 demonstrate tracking different types of Claude API requests using Python's keyword arguments for clarity. Notice how different event types have different token profiles - tool use (line 313) has lower output tokens since it returns structured data, while streaming conversations (line 300) have higher token counts.

## Program Output

```
=== Claude Code Usage Tracker Initialized ===
Start time: 2025-12-29T22:13:45.885848Z

Simulating Claude Code API usage...

1. Code completion request (Sonnet)
   ✓ Tracked code completion request

2. Streaming conversation (Opus)
   ✓ Tracked streaming conversation

3. Tool use request (Sonnet)
   ✓ Tracked tool use request

4. Vision analysis (Sonnet)
   ✓ Tracked vision analysis

5. Multiple quick completions (Haiku)
   ✓ Tracked 5 quick completions

6. Failed request (rate limit)
   ✓ Tracked failed request
```

**Annotation (Output Lines 1-20):** The tracker initializes and simulates various API calls. Notice we're tracking 6 different scenarios including a failed request (line 20), demonstrating real-world usage patterns.

```
=== Claude Code Usage Report ===

📊 Overall Statistics:
   Total Requests: 10
   Total Input Tokens: 17,678
   Total Output Tokens: 7,085
   Total Tokens: 24,763
   Total Cost: $0.3128
   Average Duration: 1083.30ms
   Success Rate: 90.00%
```

**Annotation (Output Lines 22-31):** The overall statistics show we made 10 requests totaling ~24.7K tokens at a cost of $0.31. The 90% success rate reflects the one failed request we simulated. This section provides a high-level view of API usage.

```
🤖 Usage by Model:
   Claude 4.5 Sonnet:
      Requests: 4
      Input Tokens: 9,300
      Output Tokens: 2,450
      Cost: $0.0646
   Claude 4.5 Opus:
      Requests: 1
      Input Tokens: 3,200
      Output Tokens: 2,500
      Cost: $0.2355
   Claude 3.5 Haiku:
      Requests: 5
      Input Tokens: 5,178
      Output Tokens: 2,135
      Cost: $0.0127
```

**Annotation (Output Lines 33-47):** Model breakdown reveals cost differences: a single Opus request ($0.24) costs nearly 20x more than 5 Haiku requests ($0.01). This demonstrates why choosing the right model for each task is crucial for cost optimization.

```
📝 Usage by Event Type:
   COMPLETION:
      Count: 7
      Total Tokens: 10,813
      Avg Duration: 607.57ms
   STREAMING:
      Count: 1
      Total Tokens: 5,700
      Avg Duration: 3500.00ms
   TOOL_USE:
      Count: 1
      Total Tokens: 2,550
      Avg Duration: 980.00ms
   VISION:
      Count: 1
      Total Tokens: 5,700
      Avg Duration: 2100.00ms
```

**Annotation (Output Lines 49-63):** Event type breakdown shows performance characteristics. Streaming (3500ms) and vision (2100ms) requests take longer than simple completions (607ms), which is expected given their complexity.

```
⏱️  Time Analysis:
   Session Duration: 0.00s
   Requests per Minute: 521739.13
   Tokens per Second: 21533043.48

💰 Cost Projections:
   Hourly (at current rate): $979301.4261
   Daily (at current rate): $23503234.23
   Monthly (at current rate): $705097026.78
```

**Annotation (Output Lines 65-73):** Time-based analysis and cost projections. Note: These projections are extremely high because the simulation runs all requests instantly. In real usage, requests would be spread over time, resulting in much more reasonable costs.

```
🚦 Rate Limit Status:
   Requests (last minute): 10/50
   Tokens (last minute): 24,763/40,000
```

**Annotation (Output Lines 75-77):** Rate limit monitoring shows we're at 20% of request capacity and 62% of token capacity. This early warning system helps prevent hitting rate limits.

```
💡 Cost Optimization Tips:
   • Use Haiku for simple tasks (10-20x cheaper than Opus)
   • Cache frequently used context to reduce input tokens
   • Batch similar requests when possible
   • Use streaming to show partial results faster
   • Monitor token usage with prompt caching
```

**Annotation (Output Lines 79-84):** Practical optimization tips based on the analysis. The first tip (using Haiku) is validated by our model breakdown showing 20x cost difference.

## Key Takeaways

1. **Model Selection Matters**: Haiku costs 10-20x less than Opus. Use the right model for each task.

2. **Token Tracking**: Input tokens (17,678) are generally cheaper than output tokens (7,085), but output tokens cost 3-5x more per token.

3. **Rate Limit Awareness**: Monitoring both request count and token usage prevents hitting API limits.

4. **Success Rate Tracking**: The 90% success rate (9/10 requests) helps identify reliability issues.

5. **Event Type Analysis**: Different request types have different performance profiles:
   - Completions: Fast (607ms avg)
   - Streaming: Slower but better UX (3500ms)
   - Tool Use: Moderate speed (980ms)
   - Vision: Moderate-slow (2100ms)

6. **Python-Specific Benefits**:
   - Type hints provide static analysis similar to TypeScript
   - Dataclasses reduce boilerplate for data structures
   - List comprehensions and generator expressions provide concise, readable aggregations
   - No build step required - run directly with `uv`

## Requirements

- Python 3.11+ (for modern type hints with `|` union syntax and PEP 585 built-in generics)
- uv for running the script

## Dependencies

None - this is a standalone script with no external dependencies. All functionality uses Python's standard library:
- `dataclasses` for data structures
- `datetime` and `timedelta` for time tracking
- `enum` for event types
- `typing` for type hints
- `random` for simulating variable token usage

The script uses inline metadata (PEP 723) for declaring Python version requirements, making it runnable with `uv run python main_ccusage_monitor.py` without a separate `pyproject.toml`.
