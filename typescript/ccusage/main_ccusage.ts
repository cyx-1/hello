#!/usr/bin/env node

/**
 * Claude Code Usage Tracker
 * Demonstrates tracking and analyzing Claude Code API usage including:
 * - Request counting and categorization
 * - Token usage (input/output)
 * - Cost calculation
 * - Rate limit monitoring
 * - Usage analytics and reporting
 */

// Line 12: Define usage event types
enum EventType {
  COMPLETION = 'completion',
  STREAMING = 'streaming',
  TOOL_USE = 'tool_use',
  VISION = 'vision'
}

// Line 20: Define model pricing structure (as of 2025)
interface ModelPricing {
  inputTokensPerMillion: number;
  outputTokensPerMillion: number;
  modelName: string;
}

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

// Line 47: Define usage event interface
interface UsageEvent {
  timestamp: Date;
  eventType: EventType;
  modelId: string;
  inputTokens: number;
  outputTokens: number;
  durationMs: number;
  success: boolean;
  metadata?: Record<string, any>;
}

// Line 60: Claude Code Usage Tracker class
class ClaudeCodeUsageTracker {
  private events: UsageEvent[] = [];
  private startTime: Date;

  constructor() {
    this.startTime = new Date();
    console.log('=== Claude Code Usage Tracker Initialized ===');
    console.log(`Start time: ${this.startTime.toISOString()}\n`);
  }

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

  // Line 126: Get usage breakdown by model
  getUsageByModel(): Map<string, {
    requests: number;
    inputTokens: number;
    outputTokens: number;
    cost: number;
  }> {
    const modelStats = new Map<string, {
      requests: number;
      inputTokens: number;
      outputTokens: number;
      cost: number;
    }>();

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

  // Line 160: Get usage breakdown by event type
  getUsageByEventType(): Map<EventType, {
    count: number;
    totalTokens: number;
    avgDurationMs: number;
  }> {
    const typeStats = new Map<EventType, {
      count: number;
      totalTokens: number;
      avgDurationMs: number;
    }>();

    for (const event of this.events) {
      const existing = typeStats.get(event.eventType) || {
        count: 0,
        totalTokens: 0,
        avgDurationMs: 0
      };

      const totalTokens = existing.totalTokens + event.inputTokens + event.outputTokens;
      const count = existing.count + 1;
      const avgDurationMs = ((existing.avgDurationMs * existing.count) + event.durationMs) / count;

      typeStats.set(event.eventType, {
        count,
        totalTokens,
        avgDurationMs
      });
    }

    return typeStats;
  }

  // Line 194: Generate usage report
  generateReport(): void {
    console.log('\n=== Claude Code Usage Report ===\n');

    // Overall statistics
    const total = this.getTotalUsage();
    console.log('📊 Overall Statistics:');
    console.log(`   Total Requests: ${total.totalRequests.toLocaleString()}`);
    console.log(`   Total Input Tokens: ${total.totalInputTokens.toLocaleString()}`);
    console.log(`   Total Output Tokens: ${total.totalOutputTokens.toLocaleString()}`);
    console.log(`   Total Tokens: ${total.totalTokens.toLocaleString()}`);
    console.log(`   Total Cost: $${total.totalCost.toFixed(4)}`);
    console.log(`   Average Duration: ${total.avgDurationMs.toFixed(2)}ms`);
    console.log(`   Success Rate: ${total.successRate.toFixed(2)}%`);
    console.log();

    // Model breakdown
    console.log('🤖 Usage by Model:');
    const modelStats = this.getUsageByModel();
    for (const [modelId, stats] of modelStats.entries()) {
      const pricing = MODEL_PRICING[modelId];
      console.log(`   ${pricing?.modelName || modelId}:`);
      console.log(`      Requests: ${stats.requests.toLocaleString()}`);
      console.log(`      Input Tokens: ${stats.inputTokens.toLocaleString()}`);
      console.log(`      Output Tokens: ${stats.outputTokens.toLocaleString()}`);
      console.log(`      Cost: $${stats.cost.toFixed(4)}`);
    }
    console.log();

    // Event type breakdown
    console.log('📝 Usage by Event Type:');
    const typeStats = this.getUsageByEventType();
    for (const [type, stats] of typeStats.entries()) {
      console.log(`   ${type.toUpperCase()}:`);
      console.log(`      Count: ${stats.count.toLocaleString()}`);
      console.log(`      Total Tokens: ${stats.totalTokens.toLocaleString()}`);
      console.log(`      Avg Duration: ${stats.avgDurationMs.toFixed(2)}ms`);
    }
    console.log();

    // Time-based analysis
    const sessionDuration = (new Date().getTime() - this.startTime.getTime()) / 1000;
    console.log('⏱️  Time Analysis:');
    console.log(`   Session Duration: ${sessionDuration.toFixed(2)}s`);
    console.log(`   Requests per Minute: ${((total.totalRequests / sessionDuration) * 60).toFixed(2)}`);
    console.log(`   Tokens per Second: ${(total.totalTokens / sessionDuration).toFixed(2)}`);
    console.log();

    // Cost projection
    console.log('💰 Cost Projections:');
    const costPerHour = (total.totalCost / sessionDuration) * 3600;
    const costPerDay = costPerHour * 24;
    const costPerMonth = costPerDay * 30;
    console.log(`   Hourly (at current rate): $${costPerHour.toFixed(4)}`);
    console.log(`   Daily (at current rate): $${costPerDay.toFixed(2)}`);
    console.log(`   Monthly (at current rate): $${costPerMonth.toFixed(2)}`);
    console.log();
  }

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
    console.log();
  }
}

// Line 290: Demo usage tracking
async function demonstrateUsageTracking() {
  const tracker = new ClaudeCodeUsageTracker();

  console.log('Simulating Claude Code API usage...\n');

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
  console.log('   ✓ Tracked code completion request\n');

  // Line 309: Simulate streaming response
  console.log('2. Streaming conversation (Opus)');
  tracker.trackEvent({
    eventType: EventType.STREAMING,
    modelId: 'claude-opus-4-5',
    inputTokens: 3200,
    outputTokens: 2500,
    durationMs: 3500,
    success: true,
    metadata: { task: 'conversation' }
  });
  console.log('   ✓ Tracked streaming conversation\n');

  // Line 322: Simulate tool use
  console.log('3. Tool use request (Sonnet)');
  tracker.trackEvent({
    eventType: EventType.TOOL_USE,
    modelId: 'claude-sonnet-4-5',
    inputTokens: 2100,
    outputTokens: 450,
    durationMs: 980,
    success: true,
    metadata: { tools: ['bash', 'grep', 'edit'] }
  });
  console.log('   ✓ Tracked tool use request\n');

  // Line 335: Simulate vision request
  console.log('4. Vision analysis (Sonnet)');
  tracker.trackEvent({
    eventType: EventType.VISION,
    modelId: 'claude-sonnet-4-5',
    inputTokens: 4500,
    outputTokens: 1200,
    durationMs: 2100,
    success: true,
    metadata: { images: 2 }
  });
  console.log('   ✓ Tracked vision analysis\n');

  // Line 348: Simulate multiple quick requests
  console.log('5. Multiple quick completions (Haiku)');
  for (let i = 0; i < 5; i++) {
    tracker.trackEvent({
      eventType: EventType.COMPLETION,
      modelId: 'claude-haiku-3-5',
      inputTokens: 800 + Math.floor(Math.random() * 400),
      outputTokens: 300 + Math.floor(Math.random() * 200),
      durationMs: 400 + Math.floor(Math.random() * 300),
      success: true,
      metadata: { batch: i + 1 }
    });
  }
  console.log('   ✓ Tracked 5 quick completions\n');

  // Line 365: Simulate a failed request
  console.log('6. Failed request (rate limit)');
  tracker.trackEvent({
    eventType: EventType.COMPLETION,
    modelId: 'claude-sonnet-4-5',
    inputTokens: 1200,
    outputTokens: 0,
    durationMs: 150,
    success: false,
    metadata: { error: 'rate_limit_exceeded' }
  });
  console.log('   ✓ Tracked failed request\n');

  // Line 379: Generate comprehensive report
  tracker.generateReport();

  // Line 382: Check rate limits
  tracker.checkRateLimits();

  // Line 385: Show cost optimization tips
  console.log('💡 Cost Optimization Tips:');
  console.log('   • Use Haiku for simple tasks (10-20x cheaper than Opus)');
  console.log('   • Cache frequently used context to reduce input tokens');
  console.log('   • Batch similar requests when possible');
  console.log('   • Use streaming to show partial results faster');
  console.log('   • Monitor token usage with prompt caching');
  console.log();

  console.log('=== Demo Complete ===');
}

// Line 397: Run the demonstration
demonstrateUsageTracking().catch(console.error);
