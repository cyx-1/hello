# Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA

**Video URL:** https://www.youtube.com/watch?v=NTBX-wxUhHs

## Executive Summary

Val Bercovici (Chief AI Officer) and Kalen Fox (Head of Product Management) from WEKA present a groundbreaking approach to solving "token anxiety" through context platform engineering. They announce the open-sourcing of their context platform engineering toolkit featuring a sophisticated load generator for testing agent swarms. The core insight: KV cache hit rate is the single most important metric for production-grade AI agents, and context platform engineering dramatically simplifies reaching maximum cache hit rates. The presentation reveals how token storage is fundamentally a memory tier problem, demonstrating that WEKA's augmented memory grid using NVMe can maintain high cache hit rates at significantly higher concurrent user loads compared to traditional DRAM-based systems.

## Main Topics

### [Introduction and Toolkit Announcement](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=0s)
- WEKA is open-sourcing their context platform engineering toolkit on GitHub
- The toolkit features a load generator that allows configuration of agent swarms with specific SLOs
- Supports deterministic and random prompt cycles
- Enables engineering context platforms with various model parallelism options (disaggregated/aggregated pre-fill and decode)
- Includes memory tiering options critical to context platform engineering

### [Why KV Cache Hit Rate Matters](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=84s)
- Manus blog post highlighted that KV cache hit rate is the single most important metric for production-grade AI agents
- Context platform engineering dramatically simplifies reaching maximum KV cache hit rates
- Addresses "token anxiety" - the frustration of hitting token rate limits
- Context platform engineering helps eliminate token rate limits and improve developer productivity
- Alternative is "context financial engineering" - arbitraging between cache writes, cache reads, and input/output tokens with varying time-to-live periods (5 minutes, 1 hour)

### [Understanding Agent Token Consumption Patterns](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=222s)
- Agent workflows have a cadence mismatch: slow human feedback loops vs. fast agent subtask iteration
- The core problem is fundamentally a token storage problem
- When subscribing to token tiers or paying for cache rights, you're essentially purchasing cache KB slots in token storage
- Service Level Agreements (SLAs) from users convert to Service Level Objectives (SLOs) delivered by the context platform

### [Visualizing Agent Token Usage](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=360s)
- Salmon color represents new tokens, gray represents cacheable tokens, blue represents output tokens
- User responses are shown as blue dots at the bottom
- Common pattern: consume context until hitting a high watermark (model max length or provider limit)
- Summarization phase occurs, then a new cycle starts (often with loss of fidelity)
- In agentic coding, actual user input is a very small part - most is tool use and tool responses (system prompts)
- Median time between requests: 10-15 seconds; mean time: minutes to hours due to human response time

### [Multi-Agent Architectures](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=500s)
- Common pattern: orchestrator agent + sub-agents for individual tasks
- Sub-agents may be short-lived (context doesn't endure) or long-lived (context persists)
- Multi-agent architectures allow targeting context at specific problem parts but consume more overall context
- There's common context shared between agents that creates dependencies and relationships

### [The Cache Hit Rate Problem](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=580s)
- Reality: you don't get 100% cache hits even though much content could be cached
- For API users: cache misses cost 10x more (paying full input token cost vs. cache read cost)
- For subscription users: cache misses burn through rate limits faster due to cache usage limits
- WEKA works with providers to maximize cache efficiency for better user and provider experience

### [Time-to-Live Impact on Cache Hit Rates](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=660s)
- Working set analysis: tokens held in cache memory based on different TTLs
- 1-minute TTL: thrashing behavior when request intervals exceed 1 minute
- 5-minute TTL: rides out more cache hits, higher hit rate
- 1-hour TTL: requires holding more tokens but delivers much better user experience
- The challenge: longer TTLs require ability to hold many tokens in cache with good memory tiers

### [Understanding Cache Efficiency](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=780s)
- Another metric: number of times token chunks are re-prefilled
- At 1-minute TTL: same tokens re-prefilled 15-16 times
- Longer TTLs approach 1 re-prefill (optimal)
- Significant difference in experience for both users and inference providers

### [Context Platform Engineering Goals](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=840s)
- Expected trend for 2026: people hosting their own or dedicated inference systems
- Key relationship: context length, cache hit rate, and output tokens
- Non-linear curve dependent on context length, accelerators, disaggregated prefill approaches
- Goal: operate in the optimal zone (high cache hit rates leading to maximum output tokens)
- Staying in point C vs. A or B means profitability and value extraction

### [Incentivizing Cache Usage](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=900s)
- Inference providers incentivize users to stay within cache through pricing
- Why subscription = buying cache allotments: cache hit rate massively impacts output capacity
- Critical for agentic workflows - poor cache hit rates will "melt GPU clusters"
- Understanding this relationship is essential for context platform engineering

### [Token Storage Requirements](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=960s)
Three key requirements for memory tiers supporting token storage:
1. **Sufficient capacity**: Hold optimal amount of cache (reaching diminishing returns point)
2. **Fast writes**: Store extremely fast to avoid dropping KVs or blocking GPUs
3. **Fast reads**: Fetch from token storage rapidly to avoid blocking GPUs (GPUs are first-class citizens)

### [Memory Tier Options](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=1020s)
- **HBM**: Ideal but not reasonable to keep all sessions in HBM at all times
- **DRAM**: Most common today, limited in size, okay performance, tightly coupled with compute
- **Pooled DRAM**: Can aggregate more but hurts performance
- **WEKA Augmented Memory Grid**: Optimized connector between inference systems and WEKA's existing product, backed by NVMe, ~1000x denser than DRAM, proven in AI training and HPC environments
- **Traditional storage**: Can achieve 50-60 GB/s but still relatively slow for this use case

### [Testing Methodology](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=1120s)
- Open-sourced toolkit acts like an inference provider
- Can configure to keep load within specific SLOs (time to first token, output tokens per request)
- Two modes:
  - Static number of coding agent users
  - Increasing users over time to gradually utilize more memory tiers
- **Sequential mode**: Very deterministic, shows massive performance drop when overflowing memory tier
- **Random sampling mode**: More fair testing, increases concurrent users over time, creates blended performance numbers across memory tiers

### [Performance Results: Decode-Focused Workload](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=1236s)
Three configurations compared:
- **Purple**: HBM + WEKA
- **Orange**: HBM + DRAM
- **Pink**: HBM + DRAM + POSIX storage

Early phase (shaded area): All three benefit from HBM for primary cache hit rate

As concurrent users increase:
- Orange and pink: Both drop off dramatically as DRAM memory tier overflows
- Purple (WEKA): Also drops slightly (less HBM advantage) but maintains much higher performance at steady state
- WEKA maintains high output tokens at significantly higher concurrent user counts

### [Performance Results: Pre-fill Focused Workload](https://www.youtube.com/watch?v=NTBX-wxUhHs&t=1320s)
- Disaggregated prefill scenarios show even better results for WEKA
- GPUs much more efficient with large batches of pre-fill tokens with single decode
- WEKA can saturate systems more fairly and sustain performance
- Key difference: Purple (WEKA) vs. Orange (DRAM) in maintaining performance under load

## Key Takeaways

1. **KV cache hit rate is critical** for production AI agents - it's not just about cost, but about system capacity and user experience
2. **Token anxiety stems from storage problems** - subscriptions are effectively purchasing cache storage allotments
3. **Time-to-live matters enormously** - longer TTLs (1 hour vs. 5 minutes vs. 1 minute) dramatically improve cache efficiency
4. **Memory tiers are the bottleneck** - DRAM limitations cause performance cliffs; NVMe-backed solutions like WEKA's augmented memory grid provide ~1000x more density
5. **Context platform engineering > context financial engineering** - Better to optimize the infrastructure than arbitrage pricing models
6. **The future is self-hosted** - 2026 will see more dedicated inference systems requiring proper context platform engineering
7. **Open-source toolkit available** - GitHub toolkit enables testing and optimizing context platforms with realistic agent workloads

## Resources
- WEKA Context Platform Engineering Toolkit: Available on GitHub
- Blog post by Kalen Fox with detailed testing methodology
- Original Manus blog post on context engineering
