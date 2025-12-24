# Summary: Benchmarks vs Economics - The AI Capability Measurement Gap

**Video URL:** https://www.youtube.com/watch?v=RhfqQKe22ZA

**Speaker:** Joel Becker, METR (Model Evaluation and Threat Research)

## Executive Summary

Joel Becker from METR presents a puzzling discrepancy between two ways of measuring AI capabilities: benchmarks show impressive, rapidly improving performance, while a field experiment reveals that expert developers using AI tools were actually **19% slower** than those without AI. This talk explores both measurement approaches and attempts to reconcile this surprising gap.

---

## Topics

### 1. Introduction to METR
[00:22](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=22s)

- METR = Model Evaluation and Threat Research
- Independent research nonprofit informing public, policymakers, and labs about AI risks
- Two focus areas: understanding AI capabilities/propensities AND connecting them to catastrophic risks
- Will compare benchmark evidence vs. economic/field experiment evidence

### 2. Problems with Traditional Benchmarks
[02:00](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=120s)

- Traditional benchmarks (GPQA, SWE-Bench) have limited interpretability
- What does 50% performance on GPQA actually mean for real-world capability?
- Benchmarks saturate quickly - less time between creation and full saturation
- Hard to create benchmarks that maintain signal over extended periods

### 3. METR's Time Horizon Approach
[03:16](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=196s)

- Gather human baseline data for diverse tasks spanning difficulty ranges
- Human baselines are "experienced experts on their first week on the job"
- Task distributions: Hcast (software tasks), SWAR suite (atomic problems), Rebench (challenging ML research)
- Measure AI performance under identical conditions
- Convert human completion time into "time horizon" metric (50% success point)

### 4. The Time Horizon Results
[05:00](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=300s)

- Models perform well on short tasks (4 minutes or less = ~100% success)
- Performance drops significantly on longer, harder tasks
- Claude 3.7 Sonnet time horizon: ~30 minutes
- Claude 3 Opus time horizon: ~4 minutes
- O1 Preview time horizon: ~15 minutes
- **Remarkably steady exponential trend** - time horizon doubles every 6-7 months
- Trend has held up through GPT-5.1 CEX max

### 5. Limitations of Benchmark Evidence
[07:44](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=464s)

Three key limitations:
1. **Low-context baselines** - Humans are experts but unfamiliar with specific tasks
2. **Low ceiling** - Benchmarks saturate (like GPQA); time horizon also will eventually saturate
3. **Not messy enough** - Problems don't require human coordination, are in contained environments, not massive real codebases

### 6. Field Experiment Design (RCT)
[10:42](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=642s)

- 16 experienced developers on large mature open-source projects
- Repositories: Haskell compiler, scikit-learn, Hugging Face Transformers (avg 1M+ lines, 10+ years old)
- Developers are on average 3rd top contributor (out of hundreds/thousands), 5 years experience on repo
- ~16 tasks per developer from real GitHub issues
- Random assignment: AI allowed vs AI disallowed
- AI disallowed = "software development in 2019" (no autocomplete, no Cursor, no LLMs)
- AI allowed = Cursor Pro with Claude 3.6/3.7 Sonnet

### 7. The Shocking Results
[12:29](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=749s)

**Predictions:**
- Economics/ML experts expected: ~40% time savings
- Developers themselves (before study): ~24-25% time savings
- Developers (after study): estimated ~20% time savings

**Actual Result: Developers were 19% SLOWER with AI**

### 8. Explanations for the Slowdown
[14:14](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=854s)

Contributing factors identified:
- **Over-optimism about AI usefulness** - Developers overuse AI despite mixed results
- **Implicit repository context** - Developers already know solutions; typing speed is the bottleneck, not thinking
- **High developer familiarity** - AI can't match domain expertise built over years
- **Large/complex repositories** - AI performs worse on massive codebases
- **Low AI reliability** - Need to check/correct AI work; only 50-80% correct requires costly verification

### 9. Important Caveats
[16:00](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=960s)

- Results specific to this population: extremely experienced developers on extremely complex projects
- Joel personally feels sped up by AI on smaller, simpler repositories
- Experiment concentrated in March 2025 - may already be outdated
- AI progress is rapid

### 10. Resolving the Puzzle
[17:15](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=1035s)

Possible explanations for benchmark vs. real-world gap:

1. **Experimental issues** - Maybe developers aren't skilled with AI tools yet
2. **Incentive problems** - Paid hourly, not incentivized to finish quickly
3. **Small sample size** - Need larger studies (in progress)
4. **Reliability threshold** - Need 95-99% correctness for "tab tab tab" workflow; anything less requires costly verification
5. **Scoring differences** - SWE-Bench doesn't measure code maintainability, style, holistic quality
6. **Context differences** - High-context experts vs low-context baselines
7. **Task distribution** - Real tasks are messier than benchmarks
8. **Suboptimal elicitation** - Cursor may not extract maximum capability from models
9. **Task interdependence** - Humans need to maintain context across related subtasks

### 11. Conclusion and Hiring
[20:25](https://www.youtube.com/watch?v=RhfqQKe22ZA&t=1225s)

- METR is hiring at metr.org/careers
- Looking for: Research engineers, research scientists, director of operations
- Welcome both academic researchers and "scrappy startup people"
- Continuing work on longer tasks, more ambitious RCTs, more evidence sources

---

## Key Takeaways

1. **Benchmark performance ≠ Real-world productivity** - At least for expert developers on complex codebases
2. **AI reliability threshold is high** - Need near-perfect correctness to avoid costly verification overhead
3. **Domain expertise matters** - AI struggles to match years of accumulated context and familiarity
4. **Time horizon is a useful metric** - Shows steady exponential progress (~2x every 6-7 months)
5. **The gap is a puzzle worth solving** - Multiple plausible explanations, more research needed
