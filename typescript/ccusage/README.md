# Claude Code Usage Tracker

A TypeScript demonstration of tracking and analyzing Claude Code API usage, including request counting, token usage, cost calculation, and rate limit monitoring.

## Overview

This example demonstrates how to build a comprehensive usage tracking system for Claude Code that monitors:
- API requests by type (completion, streaming, tool use, vision)
- Token consumption (input/output)
- Cost calculation based on 2025 pricing
- Rate limit monitoring
- Usage analytics and reporting

## Running the Example

```bash
npm install
npm start
```

## Source Code

### Key Data Structures (Lines 12-45)

```typescript
// Line 12: Define usage event types
enum EventType {
  COMPLETION = 'completion',
  STREAMING = 'streaming',
  TOOL_USE = 'tool_use',
  VISION = 'vision'
}

// Line 28: Model pricing structure
const MODEL_PRICING: Record<string, ModelPricing> = {
  'claude-sonnet-4-5': {
    modelName: 'Claude 4.5 Sonnet',
    inputTokensPerMillion: 3.00,
    outputTokensPerMillion: 15.00
  },
  'claude-opus-4-5': {
    modelName: 'Claude 4.5 Opus',
    inputTokensPerMillion: 15.00,
    outputTokensPerMillion: 75.00
  },
  'claude-haiku-3-5': {
    modelName: 'Claude 3.5 Haiku',
    inputTokensPerMillion: 0.80,
    outputTokensPerMillion: 4.00
  }
};
```

**Annotation:** Lines 12-45 define the core data structures for tracking different types of Claude API events and their associated costs. Notice that Haiku is 10-20x cheaper than Opus, making it ideal for simple tasks.

### Usage Tracker Class (Lines 60-124)

```typescript
// Line 60: Main tracker class
class ClaudeCodeUsageTracker {
  private events: UsageEvent[] = [];

  // Line 72: Track a new usage event
  trackEvent(event: Omit<UsageEvent, 'timestamp'>): void {
    const fullEvent: UsageEvent = {
      ...event,
      timestamp: new Date()
    };
    this.events.push(fullEvent);
  }

  // Line 82: Calculate cost for a single event
  private calculateEventCost(event: UsageEvent): number {
    const pricing = MODEL_PRICING[event.modelId];
    if (!pricing) return 0;

    const inputCost = (event.inputTokens / 1_000_000) * pricing.inputTokensPerMillion;
    const outputCost = (event.outputTokens / 1_000_000) * pricing.outputTokensPerMillion;
    return inputCost + outputCost;
  }

  // Line 93: Get total usage statistics
  getTotalUsage(): {
    totalRequests: number;
    totalInputTokens: number;
    totalOutputTokens: number;
    totalTokens: number;
    totalCost: number;
    avgDurationMs: number;
    successRate: number;
  } {
    const totalRequests = this.events.length;
    const totalInputTokens = this.events.reduce((sum, e) => sum + e.inputTokens, 0);
    const totalOutputTokens = this.events.reduce((sum, e) => sum + e.outputTokens, 0);
    const totalTokens = totalInputTokens + totalOutputTokens;
    const totalCost = this.events.reduce((sum, e) => sum + this.calculateEventCost(e), 0);
    const avgDurationMs = totalRequests > 0
      ? this.events.reduce((sum, e) => sum + e.durationMs, 0) / totalRequests
      : 0;
    const successCount = this.events.filter(e => e.success).length;
    const successRate = totalRequests > 0 ? (successCount / totalRequests) * 100 : 0;

    return {
      totalRequests,
      totalInputTokens,
      totalOutputTokens,
      totalTokens,
      totalCost,
      avgDurationMs,
      successRate
    };
  }
}
```

**Annotation:** Lines 60-124 implement the core tracking functionality. The `trackEvent()` method (line 72) captures each API call with timestamp, while `calculateEventCost()` (line 82) computes costs based on input/output token pricing. The `getTotalUsage()` method (line 93) aggregates statistics including success rate.

### Usage Breakdown by Model (Lines 126-159)

```typescript
// Line 126: Get usage breakdown by model
getUsageByModel(): Map<string, {
  requests: number;
  inputTokens: number;
  outputTokens: number;
  cost: number;
}> {
  const modelStats = new Map();

  for (const event of this.events) {
    const existing = modelStats.get(event.modelId) || {
      requests: 0,
      inputTokens: 0,
      outputTokens: 0,
      cost: 0
    };

    modelStats.set(event.modelId, {
      requests: existing.requests + 1,
      inputTokens: existing.inputTokens + event.inputTokens,
      outputTokens: existing.outputTokens + event.outputTokens,
      cost: existing.cost + this.calculateEventCost(event)
    });
  }

  return modelStats;
}
```

**Annotation:** Lines 126-159 provide model-level analytics, allowing you to see which Claude models (Sonnet, Opus, Haiku) you're using most and their respective costs. This is crucial for cost optimization.

### Rate Limit Monitoring (Lines 263-288)

```typescript
// Line 263: Check if approaching rate limits
checkRateLimits(requestsPerMinuteLimit: number = 50, tokensPerMinuteLimit: number = 40000): void {
  const oneMinuteAgo = new Date(Date.now() - 60000);
  const recentEvents = this.events.filter(e => e.timestamp >= oneMinuteAgo);

  const requestsLastMinute = recentEvents.length;
  const tokensLastMinute = recentEvents.reduce(
    (sum, e) => sum + e.inputTokens + e.outputTokens,
    0
  );

  console.log('🚦 Rate Limit Status:');
  console.log(`   Requests (last minute): ${requestsLastMinute}/${requestsPerMinuteLimit}`);
  console.log(`   Tokens (last minute): ${tokensLastMinute.toLocaleString()}/${tokensPerMinuteLimit.toLocaleString()}`);

  if (requestsLastMinute >= requestsPerMinuteLimit * 0.8) {
    console.log('   ⚠️  Warning: Approaching request rate limit!');
  }
  if (tokensLastMinute >= tokensPerMinuteLimit * 0.8) {
    console.log('   ⚠️  Warning: Approaching token rate limit!');
  }
}
```

**Annotation:** Lines 263-288 implement rate limit monitoring by filtering events from the last minute. The warning threshold is set at 80% to give advance notice before hitting limits. This is essential for production applications.

### Simulating Usage (Lines 296-377)

```typescript
// Line 296: Simulate various API calls
console.log('1. Code completion request (Sonnet)');
tracker.trackEvent({
  eventType: EventType.COMPLETION,
  modelId: 'claude-sonnet-4-5',
  inputTokens: 1500,
  outputTokens: 800,
  durationMs: 1250,
  success: true,
  metadata: { task: 'code_generation' }
});

// Line 309: Simulate streaming response
tracker.trackEvent({
  eventType: EventType.STREAMING,
  modelId: 'claude-opus-4-5',
  inputTokens: 3200,
  outputTokens: 2500,
  durationMs: 3500,
  success: true,
  metadata: { task: 'conversation' }
});

// Line 322: Simulate tool use
tracker.trackEvent({
  eventType: EventType.TOOL_USE,
  modelId: 'claude-sonnet-4-5',
  inputTokens: 2100,
  outputTokens: 450,
  durationMs: 980,
  success: true,
  metadata: { tools: ['bash', 'grep', 'edit'] }
});
```

**Annotation:** Lines 296-377 demonstrate tracking different types of Claude API requests. Notice how different event types have different token profiles - tool use (line 322) has lower output tokens since it returns structured data, while streaming conversations (line 309) have higher token counts.

## Program Output

```
=== Claude Code Usage Tracker Initialized ===
Start time: 2025-12-29T19:57:27.199Z

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
   Total Input Tokens: 17,579
   Total Output Tokens: 6,973
   Total Tokens: 24,552
   Total Cost: $0.3123
   Average Duration: 1059.80ms
   Success Rate: 90.00%
```

**Annotation (Output Lines 22-31):** The overall statistics show we made 10 requests totaling ~24.5K tokens at a cost of $0.31. The 90% success rate reflects the one failed request we simulated. This section provides a high-level view of API usage.

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
      Input Tokens: 5,079
      Output Tokens: 2,023
      Cost: $0.0122
```

**Annotation (Output Lines 33-47):** Model breakdown reveals cost differences: a single Opus request ($0.24) costs nearly 20x more than 5 Haiku requests ($0.01). This demonstrates why choosing the right model for each task is crucial for cost optimization.

```
📝 Usage by Event Type:
   COMPLETION:
      Count: 7
      Total Tokens: 10,602
      Avg Duration: 574.00ms
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

**Annotation (Output Lines 49-63):** Event type breakdown shows performance characteristics. Streaming (3500ms) and vision (2100ms) requests take longer than simple completions (574ms), which is expected given their complexity.

```
⏱️  Time Analysis:
   Session Duration: 0.02s
   Requests per Minute: 26086.96
   Tokens per Second: 1067478.26

💰 Cost Projections:
   Hourly (at current rate): $48882.5530
   Daily (at current rate): $1173181.27
   Monthly (at current rate): $35195438.19
```

**Annotation (Output Lines 65-73):** Time-based analysis and cost projections. Note: These projections are extremely high because the simulation runs all requests instantly. In real usage, requests would be spread over time, resulting in much more reasonable costs.

```
🚦 Rate Limit Status:
   Requests (last minute): 10/50
   Tokens (last minute): 24,552/40,000
```

**Annotation (Output Lines 75-77):** Rate limit monitoring shows we're at 20% of request capacity and 61% of token capacity. This early warning system helps prevent hitting rate limits.

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

2. **Token Tracking**: Input tokens (17,579) are generally cheaper than output tokens (6,973), but output tokens cost 3-5x more per token.

3. **Rate Limit Awareness**: Monitoring both request count and token usage prevents hitting API limits.

4. **Success Rate Tracking**: The 90% success rate (9/10 requests) helps identify reliability issues.

5. **Event Type Analysis**: Different request types have different performance profiles:
   - Completions: Fast (574ms avg)
   - Streaming: Slower but better UX (3500ms)
   - Tool Use: Moderate speed (980ms)
   - Vision: Moderate-slow (2100ms)

## Requirements

- Node.js 18+ (for ES2022 features)
- TypeScript 5.7+
- tsx for running TypeScript directly

## Dependencies

- `tsx`: TypeScript execution environment
- `@types/node`: TypeScript definitions for Node.js
- `typescript`: TypeScript compiler

All dependencies are automatically installed via `npm install`.
