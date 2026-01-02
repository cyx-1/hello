# Can you prove AI ROI in Software Eng (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford

**Video URL:** https://www.youtube.com/watch?v=JvosMkuNxF8

---

## Executive Summary

This presentation shares Stanford's research on measuring AI's impact on software engineering productivity across 120,000 developers. The study reveals a widening gap between top and bottom AI adopters (median 10% productivity gain), with key findings showing that AI usage quality matters more than volume. Environment cleanliness (code quality, tests, documentation) has a 0.40 R-squared correlation with productivity gains. The research introduces an AI engineering practices benchmark (levels 0-4) and proposes an ROI framework using engineering output as the primary metric with guardrail metrics for quality. A case study demonstrates why measuring only PRs can be misleading - one company saw 14% PR increase but 9% code quality decrease and 2.5x rework increase, suggesting potentially negative ROI.

---

## Topics & Key Points

### [Introduction and Research Overview](https://www.youtube.com/watch?v=JvosMkuNxF8&t=0s)
**[00:00 - 01:42]**

- Companies spend millions on AI tools for software engineering but lack clear understanding of effectiveness
- Stanford conducted 2-year research on AI's impact on software engineering productivity
- Research is time-series (historical Git data) and cross-sectional (across companies)
- Measurement uses ML model that replicates panel of 10-15 independent experts
- Experts evaluate code commits across implementation time, maintainability, and complexity

### [Productivity Gains and Performance Gap](https://www.youtube.com/watch?v=JvosMkuNxF8&t=102s)
**[01:42 - 03:14]**

- Study compared 46 AI-using teams with 46 non-AI teams, measuring quarterly productivity gains
- Median productivity gain stands at ~10% as of July
- Widening gap between top and bottom performers (middle 50% shows increasing variance)
- "Rich gets richer" effect where successful early adopters compound gains
- Leaders must measure impact to know which cohort they're in and course-correct

### [AI Usage vs Quality - The Death Valley Effect](https://www.youtube.com/watch?v=JvosMkuNxF8&t=194s)
**[03:14 - 04:02]**

- Correlation between token usage and productivity is loose (R² ≈ 0.20)
- "Death valley effect" around 10 million tokens/month where teams perform worse
- Teams using slightly fewer tokens sometimes outperform higher-usage teams
- Conclusion: **AI usage quality matters more than AI usage volume**

### [Environment Cleanliness Index](https://www.youtube.com/watch?v=JvosMkuNxF8&t=242s)
**[04:02 - 05:50]**

- Created composite score measuring tests, types, documentation, modularity, and code quality
- Strong correlation (R² = 0.40) between environment cleanliness and AI productivity gains
- Clean code amplifies AI gains across three key dimensions:
  - Green zone: AI can do most of the work
  - Yellow zone: AI can help
  - Red zone: AI is not very useful
- Codebase cleanliness position determines what percentage of tasks AI can effectively handle
- **Key takeaway: Invest in codebase hygiene to unlock AI productivity gains**

### [Managing Codebase Entropy](https://www.youtube.com/watch?v=JvosMkuNxF8&t=350s)
**[05:50 - 06:21]**

- Unchecked AI use accelerates tech debt and entropy
- Entropy pushes cleanliness to the left (degradation)
- Engineers must actively push back to maintain/improve cleanliness
- Engineers need to know when to use AI and when not to
- Failure pattern: AI outputs rejected → heavy rewriting → lost trust → collapsed AI gains

### [AI Engineering Practices Benchmark](https://www.youtube.com/watch?v=JvosMkuNxF8&t=381s)
**[06:21 - 07:35]**

- Scans codebase to detect AI fingerprints/artifacts (how teams use AI)
- Quantified by percentage of active engineering work using each AI pattern
- Measured monthly using Git history
- Five maturity levels:
  - **Level 0:** No AI usage, humans write all code
  - **Level 1:** Personal use, no prompt sharing or versioning
  - **Level 2:** Team use, sharing prompts and rules
  - **Level 3:** AI autonomously handles specific tasks (not full workflow)
  - **Level 4:** Agentic orchestration, AI runs entire process
- Will be open-source tool available via Sweeper research portal

### [Same Tools, Different Usage - Business Unit Comparison](https://www.youtube.com/watch?v=JvosMkuNxF8&t=455s)
**[07:35 - 08:33]**

- Case study: Two business units with equal AI access (same licenses, spend, tools)
- Business Unit 1: Used AI for ~40% of work (high adoption)
- Business Unit 2: Struggled with significantly lower adoption
- **Key insight:** Access to AI ≠ effective AI usage across organization
- Leaders must understand not just whether engineers use AI, but **how** they use it

### [Measuring AI ROI - Framework Introduction](https://www.youtube.com/watch?v=JvosMkuNxF8&t=513s)
**[08:33 - 09:33]**

- Ideal: Measure business outcomes (revenue, NRR), but too much noise and confounding variables
- Sales execution, macro environment, product strategy create confounding effects
- Alternative: Focus on **engineering outcomes** - clearer signal between treatment and result
- Three key caveats:
  1. Assumes product function properly directs increased capacity into value generation
  2. Assumes engineering is meaningful bottleneck for value creation
  3. Guard against Goodhart's Law with balanced metrics and healthy culture

### [ROI Framework Part 1: Measuring Usage](https://www.youtube.com/watch?v=JvosMkuNxF8&t=573s)
**[10:33 - 11:48]**

- Two measurement approaches:
  - **Access-based:** Track when people get tool access
    - Pilot group with AI vs similar group without AI
    - Same team measured across time
    - Problem: Noisy results
  - **Usage-based (Gold Standard):** Telemetry from coding assistant APIs
    - Different vendor APIs provide different granularity
    - GitHub Copilot: Aggregated data
    - Cursor: More granular data
- **Key advantage:** Can measure retroactively using Git history - no need to wait 6 months for new experiments

### [ROI Framework Part 2: Engineering Outcome Metrics](https://www.youtube.com/watch?v=JvosMkuNxF8&t=708s)
**[11:48 - 12:57]**

- **Primary Metric: Engineering Output**
  - NOT lines of code, PR counts, or DORA metrics
  - Uses ML model replicating expert panel evaluation
  - Goal: Maximize this metric
- **Guardrail Metrics (maintain healthy, don't maximize):**
  1. Rework and refactoring
  2. Quality, tech debt, and risk
  3. People and DevOps (useful but not productivity metrics)
- Strategy: Keep guardrails healthy while increasing primary metric

### [Case Study: Large Enterprise - The PR Illusion](https://www.youtube.com/watch?v=JvosMkuNxF8&t=777s)
**[12:57 - 15:46]**

- **Setup:** 350-person team under VP, adopted AI in May
- **Measured:** 4 months before vs 4 months after AI adoption
- **Results:**
  - ✓ Pull requests: +14% (appears positive)
  - ✗ Code quality: -9% (problematic)
  - ✗ Code quality became more erratic/unstable
  - ~ Effective output: No meaningful increase
  - ✗ Rework: Increased 2.5x (very bad)
- **Output breakdown:** Rework, refactoring, added code, removed code
- **Benchmark:** Compared against similar companies in industry
- **Potential ROI: NEGATIVE** despite positive PR count

### [Key Insights and Conclusion](https://www.youtube.com/watch?v=JvosMkuNxF8&t=946s)
**[15:46 - 16:20]**

- **The Danger:** Measuring only PRs would suggest 14% productivity gain → false confidence
- **The Reality:** Comprehensive metrics reveal potentially negative ROI
- **Recommendation:** Don't abandon AI, use data to understand and improve usage
- AI is transformative and here to stay - measurement enables improvement
- Research portal: software engineering productivity.stanford.edu
- Special invitation for Cursor Enterprise users to participate in research
- Open-source AI practices benchmark tool available for participants

---

## Methodology Notes

- **Scale:** 120,000 developers across multiple companies
- **Duration:** 2 years of research
- **Approach:** Time-series analysis using Git historical data + cross-sectional comparison
- **Quality Measurement:** ML model trained on millions of expert evaluations
- **Environment Cleanliness Index:** Composite score of tests, types, documentation, modularity, code quality

---

## Key Takeaways

1. **Quality over quantity:** AI usage quality matters more than token volume
2. **Clean code is essential:** Environment cleanliness (R² = 0.40) is critical for AI productivity
3. **Manage entropy:** Balance AI acceleration with deliberate code quality maintenance
4. **Measure comprehensively:** PR counts alone are misleading - need primary + guardrail metrics
5. **Usage varies widely:** Same AI tools yield vastly different results across teams
6. **Retroactive analysis possible:** Git history enables measuring past AI impact
7. **Gap is widening:** Early adopters who measure and optimize are pulling ahead

---

**Last Updated:** 2026-01-01
