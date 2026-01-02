# Building Cursor Composer – Lee Robinson, Cursor

## Executive Summary

Lee Robinson from Cursor presents the development journey of Cursor Composer, their first agent model designed for real-world software engineering. The model achieves a unique balance of intelligence and speed—performing comparably to frontier models like Claude Sonnet 4.5 and GPT-5.1 while being approximately 4x faster at token generation. Robinson details the technical infrastructure, reinforcement learning approach, and key design decisions that enabled Cursor to build a production-grade coding agent that developers use daily.

---

## Main Topics

### [Introduction to Cursor Composer](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=22s)

**Timestamp:** [00:22](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=22s)

- Cursor Composer is designed for real-world software engineering, balancing both speed and intelligence
- Performance benchmarks show it's better than best open source models and competitive with recent frontier models
- Key differentiator: approximately 4x more efficient at token generation than models at similar intelligence levels
- Slightly below latest frontier models (Sonnet 4.5, GPT-5.1) but significantly faster

### [Why Cursor Built Their Own Model](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=70s)

**Timestamp:** [01:10](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=70s)

- Cursor's research and product teams previously built "Tab" for autocomplete with low latency
- Wanted to apply the same low-latency approach to coding agents
- Initial "cheetah slug" prototype received positive feedback for speed but needed more intelligence
- Built internal benchmarks representing actual usage on Cursor's own repositories
- Key breakthrough: enabling parallel tool calling and effective semantic search

### [The Cursor Agent Architecture](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=211s)

**Timestamp:** [03:31](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=211s)

- Agent has approximately 10 tools, with 5 core ones:
  - Reading files
  - Editing files
  - Searching codebase (semantic search)
  - Looking at lints
  - Running terminal/shell commands
- Agent autonomously decides whether to call tools serially or in parallel
- Demo shows rapid tool calling, file edits, shell commands, and todo management
- Different programming experience: keeps developers in flow rather than context-switching during long waits

### [Reinforcement Learning Approach](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=236s)

**Timestamp:** [03:56](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=236s)

- Goal: Mirror the Cursor production environment as closely as possible in training
- Process involves running multiple rollouts from same starting point with different tool combinations
- Scoring outputs to determine which approach is better
- Updating model parameters based on comparison results
- Simple concept but challenging to scale effectively

### [Three Major Infrastructure Challenges](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=282s)

**Timestamp:** [04:42](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=282s)

**Challenge 1: Matching Training and Inference Environments**
- Training large mixture of experts model parallelized across thousands of GPUs
- Need to speed up training while keeping it close to production environment

**Challenge 2: Complex Rollout Management**
- Models use hundreds of thousands to millions of tokens
- Hundreds of different tool calls per rollout
- Variable completion times require sophisticated handling

**Challenge 3: Maintaining Consistency**
- Must use exactly same tool format and responses as production
- Bursty compute in training differs from production patterns
- All three ML challenges ultimately required infrastructure solutions

### [Technical Architecture: Three-Server System](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=361s)

**Timestamp:** [06:01](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=361s)

- **Inference Server:** Standard ML stack with PyTorch
- **Rollout Server:** Uses Ray for distributed rollout management
- **Environment Servers:** Simulate the Cursor production environment
- Servers communicate to send advantages back to trainer, updating model parameters
- Custom kernel library enables very low precision training for speed improvements

### [Code Execution and Sandboxing](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=458s)

**Timestamp:** [07:38](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=458s)

- Cursor uses E2B (a YC company) for sandboxed code execution environments
- Allows safe execution of arbitrary code during training and inference
- Can run linters, execute code, install packages safely
- Critical for both production and training consistency
- Real code execution enables more accurate model evaluation

### [Scaling Rollouts with Ray](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=525s)

**Timestamp:** [08:45](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=525s)

- Ray framework handles distributed rollout orchestration
- Each rollout can take vastly different amounts of time (variable task complexity)
- Started with simple setup: one node pool, standard instance types
- Initial problems: very slow rollouts, GPU underutilization, many failures
- Solution involved sophisticated infrastructure improvements

### [Infrastructure Optimizations](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=580s)

**Timestamp:** [09:40](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=580s)

**Key Improvements:**
- **Multi-tier node pools:** Different instance types for different workload characteristics
- **Autoscaling:** Dynamic resource allocation based on demand
- **Custom scheduling:** Better distribution of variable-length tasks
- **Parallel tool execution:** Reduced wall-clock time significantly
- **Caching:** Aggressive caching of tool outputs and intermediate results

**Results:**
- Reduced rollout time from hours to minutes in many cases
- Improved GPU utilization from ~30% to ~85%
- Enabled running thousands of rollouts in parallel

### [Benchmark Development and Evaluation](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=720s)

**Timestamp:** [12:00](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=720s)

- Built custom internal benchmarks based on real Cursor repository tasks
- Evaluated against both internal metrics and public benchmarks
- Key metric: Would Cursor's own developers use this model daily?
- Focused on practical software engineering tasks, not just coding puzzles
- Continuous evaluation loop with real user feedback

### [Production Deployment Considerations](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=840s)

**Timestamp:** [14:00](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=840s)

- Serving infrastructure must handle highly variable request patterns
- Mix of quick autocomplete requests and long-running agent tasks
- Built custom serving infrastructure optimized for mixture of experts models
- Focus on minimizing cold start times and maintaining low latency
- Careful attention to cost efficiency while maintaining performance

### [Future Directions and Lessons Learned](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=960s)

**Timestamp:** [16:00](https://www.youtube.com/watch?v=fL1iJHtl51Q&t=960s)

**Key Takeaways:**
- Speed and intelligence are both critical for coding agents
- Infrastructure challenges are as important as ML challenges
- Matching training to production environment is crucial
- Real code execution during training improves model quality
- User feedback loop essential for model improvement

**Looking Forward:**
- Continuing to improve model intelligence while maintaining speed advantage
- Expanding tool capabilities and agent behaviors
- Better understanding of when to use different model sizes
- Improving context understanding and multi-file reasoning

---

**Video Link:** [Building Cursor Composer – Lee Robinson, Cursor](https://www.youtube.com/watch?v=fL1iJHtl51Q)
