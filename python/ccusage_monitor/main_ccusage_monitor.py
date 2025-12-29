#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
Claude Code Usage Tracker
Demonstrates tracking and analyzing Claude Code API usage including:
- Request counting and categorization
- Token usage (input/output)
- Cost calculation
- Rate limit monitoring
- Usage analytics and reporting
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Any
import random


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


# Line 59: Define usage event interface
@dataclass
class UsageEvent:
    timestamp: datetime
    event_type: EventType
    model_id: str
    input_tokens: int
    output_tokens: int
    duration_ms: int
    success: bool
    metadata: dict[str, Any] = field(default_factory=dict)


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
        output_cost = (
            event.output_tokens / 1_000_000
        ) * pricing.output_tokens_per_million
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
        success_rate = (
            (success_count / total_requests * 100) if total_requests > 0 else 0
        )

        return {
            "total_requests": total_requests,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "total_tokens": total_tokens,
            "total_cost": total_cost,
            "avg_duration_ms": avg_duration_ms,
            "success_rate": success_rate,
        }

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

    # Line 165: Get usage breakdown by event type
    def get_usage_by_event_type(self) -> dict[EventType, dict[str, float]]:
        type_stats: dict[EventType, dict[str, float]] = {}

        for event in self.events:
            if event.event_type not in type_stats:
                type_stats[event.event_type] = {
                    "count": 0,
                    "total_tokens": 0,
                    "total_duration_ms": 0,
                }

            stats = type_stats[event.event_type]
            count = stats["count"]
            stats["count"] = count + 1
            stats["total_tokens"] += event.input_tokens + event.output_tokens
            stats["total_duration_ms"] += event.duration_ms

        # Calculate averages
        for stats in type_stats.values():
            if stats["count"] > 0:
                stats["avg_duration_ms"] = stats["total_duration_ms"] / stats["count"]

        return type_stats

    # Line 194: Generate usage report
    def generate_report(self) -> None:
        print("\n=== Claude Code Usage Report ===\n")

        # Overall statistics
        total = self.get_total_usage()
        print("📊 Overall Statistics:")
        print(f"   Total Requests: {int(total['total_requests']):,}")
        print(f"   Total Input Tokens: {int(total['total_input_tokens']):,}")
        print(f"   Total Output Tokens: {int(total['total_output_tokens']):,}")
        print(f"   Total Tokens: {int(total['total_tokens']):,}")
        print(f"   Total Cost: ${total['total_cost']:.4f}")
        print(f"   Average Duration: {total['avg_duration_ms']:.2f}ms")
        print(f"   Success Rate: {total['success_rate']:.2f}%")
        print()

        # Model breakdown
        print("🤖 Usage by Model:")
        model_stats = self.get_usage_by_model()
        for model_id, stats in model_stats.items():
            pricing = MODEL_PRICING.get(model_id)
            model_name = pricing.model_name if pricing else model_id
            print(f"   {model_name}:")
            print(f"      Requests: {int(stats['requests']):,}")
            print(f"      Input Tokens: {int(stats['input_tokens']):,}")
            print(f"      Output Tokens: {int(stats['output_tokens']):,}")
            print(f"      Cost: ${stats['cost']:.4f}")
        print()

        # Event type breakdown
        print("📝 Usage by Event Type:")
        type_stats = self.get_usage_by_event_type()
        for event_type, stats in type_stats.items():
            print(f"   {event_type.value.upper()}:")
            print(f"      Count: {int(stats['count']):,}")
            print(f"      Total Tokens: {int(stats['total_tokens']):,}")
            print(f"      Avg Duration: {stats.get('avg_duration_ms', 0):.2f}ms")
        print()

        # Time-based analysis
        session_duration = (datetime.now() - self.start_time).total_seconds()
        print("⏱️  Time Analysis:")
        print(f"   Session Duration: {session_duration:.2f}s")
        print(
            f"   Requests per Minute: {(total['total_requests'] / session_duration * 60):.2f}"
        )
        print(f"   Tokens per Second: {(total['total_tokens'] / session_duration):.2f}")
        print()

        # Cost projection
        print("💰 Cost Projections:")
        cost_per_hour = (total["total_cost"] / session_duration) * 3600
        cost_per_day = cost_per_hour * 24
        cost_per_month = cost_per_day * 30
        print(f"   Hourly (at current rate): ${cost_per_hour:.4f}")
        print(f"   Daily (at current rate): ${cost_per_day:.2f}")
        print(f"   Monthly (at current rate): ${cost_per_month:.2f}")
        print()

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
        print(
            f"   Requests (last minute): {requests_last_minute}/{requests_per_minute_limit}"
        )
        print(
            f"   Tokens (last minute): {tokens_last_minute:,}/{tokens_per_minute_limit:,}"
        )

        if requests_last_minute >= requests_per_minute_limit * 0.8:
            print("   ⚠️  Warning: Approaching request rate limit!")
        if tokens_last_minute >= tokens_per_minute_limit * 0.8:
            print("   ⚠️  Warning: Approaching token rate limit!")
        print()


# Line 280: Demo usage tracking
def demonstrate_usage_tracking() -> None:
    tracker = ClaudeCodeUsageTracker()

    print("Simulating Claude Code API usage...\n")

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
    print("   ✓ Tracked code completion request\n")

    # Line 300: Simulate streaming response
    print("2. Streaming conversation (Opus)")
    tracker.track_event(
        event_type=EventType.STREAMING,
        model_id="claude-opus-4-5",
        input_tokens=3200,
        output_tokens=2500,
        duration_ms=3500,
        success=True,
        metadata={"task": "conversation"},
    )
    print("   ✓ Tracked streaming conversation\n")

    # Line 313: Simulate tool use
    print("3. Tool use request (Sonnet)")
    tracker.track_event(
        event_type=EventType.TOOL_USE,
        model_id="claude-sonnet-4-5",
        input_tokens=2100,
        output_tokens=450,
        duration_ms=980,
        success=True,
        metadata={"tools": ["bash", "grep", "edit"]},
    )
    print("   ✓ Tracked tool use request\n")

    # Line 326: Simulate vision request
    print("4. Vision analysis (Sonnet)")
    tracker.track_event(
        event_type=EventType.VISION,
        model_id="claude-sonnet-4-5",
        input_tokens=4500,
        output_tokens=1200,
        duration_ms=2100,
        success=True,
        metadata={"images": 2},
    )
    print("   ✓ Tracked vision analysis\n")

    # Line 339: Simulate multiple quick requests
    print("5. Multiple quick completions (Haiku)")
    for i in range(5):
        tracker.track_event(
            event_type=EventType.COMPLETION,
            model_id="claude-haiku-3-5",
            input_tokens=800 + random.randint(0, 400),
            output_tokens=300 + random.randint(0, 200),
            duration_ms=400 + random.randint(0, 300),
            success=True,
            metadata={"batch": i + 1},
        )
    print("   ✓ Tracked 5 quick completions\n")

    # Line 354: Simulate a failed request
    print("6. Failed request (rate limit)")
    tracker.track_event(
        event_type=EventType.COMPLETION,
        model_id="claude-sonnet-4-5",
        input_tokens=1200,
        output_tokens=0,
        duration_ms=150,
        success=False,
        metadata={"error": "rate_limit_exceeded"},
    )
    print("   ✓ Tracked failed request\n")

    # Line 368: Generate comprehensive report
    tracker.generate_report()

    # Line 371: Check rate limits
    tracker.check_rate_limits()

    # Line 374: Show cost optimization tips
    print("💡 Cost Optimization Tips:")
    print("   • Use Haiku for simple tasks (10-20x cheaper than Opus)")
    print("   • Cache frequently used context to reduce input tokens")
    print("   • Batch similar requests when possible")
    print("   • Use streaming to show partial results faster")
    print("   • Monitor token usage with prompt caching")
    print()

    print("=== Demo Complete ===")


# Line 387: Run the demonstration
if __name__ == "__main__":
    demonstrate_usage_tracking()
