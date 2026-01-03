# Layering every technique in RAG, one query at a time - David Karam, Pi Labs (fmr. Google Search)

**Video URL:** https://www.youtube.com/watch?v=w9u11ioHGA0

---

## Executive Summary

David Karam, formerly from Google Search and now co-founder of Pi Labs, presents a comprehensive framework for improving RAG (Retrieval-Augmented Generation) systems through systematic quality engineering. Rather than getting lost in buzzwords and hype, he advocates for a practical, empirical approach: start with outcomes, baseline your system, analyze failures, and incrementally apply techniques based on complexity-adjusted impact. The talk covers the full spectrum of RAG techniques from simple in-memory retrieval to advanced custom embeddings, re-rankers, multi-signal ranking, query decomposition, and model distillation. A key theme is that relevance alone is insufficient—real-world applications require domain-specific semantics, user preference signals, and thoughtful product design that gracefully degrades when the system's understanding is limited.

---

## Topics and Key Points

### [Introduction and Philosophy](https://www.youtube.com/watch?v=w9u11ioHGA0&t=0s)
**[00:00 - 02:00]**

- Speaker background: David Karam and team from Google Search, now at Pi Labs
- Core challenge: Too much focus on buzzwords (RAG is dead/not dead, agents, etc.) vs. practical orientation
- Goal: Plain English framework to understand where techniques fit and how to approach quality improvements
- Philosophy: Look at actual cases, queries, and failures—the essence of quality engineering at Google
- 50 slides in 19 minutes, slides available at pi.ai/talk

### [The Quality Engineering Loop](https://www.youtube.com/watch?v=w9u11ioHGA0&t=115s)
**[01:55 - 03:00]**

- Always start with outcomes and product problems, not techniques
- Define your quality bar (launch bar) for your application
- Set up evaluation benchmarks: easy, medium, and hard query sets
- The quality engineering loop: Baseline → Loss analysis → Apply techniques → Iterate
- Techniques should be complexity-adjusted impact: "stay lazy" - only fix what's broken
- Most important columns in technique catalog: difficulty and impact

### [Technique 1: In-Memory Retrieval](https://www.youtube.com/watch?v=w9u11ioHGA0&t=252s)
**[04:12 - 04:51]**

- Easiest approach: Shove all documents into the LLM context window
- Example: Notebook LM—upload 5 documents, ask questions, no RAG needed
- When it breaks: Documents don't fit in memory, or context window is overloaded, or documents aren't attended properly
- Failure signals when to move to next technique

### [Technique 2: BM25 (Term-Based Retrieval)](https://www.youtube.com/watch?v=w9u11ioHGA0&t=291s)
**[04:51 - 05:58]**

- BM25 components: Query terms, term frequency, document length, term rarity
- Very nice, works pretty well, easy to try, should absolutely use it
- Fails when queries don't have keyword nature (e.g., "iPhone battery life" works, but "how long does iPhone last before charging" doesn't)
- Example queries demonstrate clear difference between keyword vs. natural language queries

### [Technique 3: Relevance Embeddings (Vector Search)](https://www.youtube.com/watch?v=w9u11ioHGA0&t=320s)
**[05:20 - 06:10]**

- Vector space can handle way more nuance than keyword space
- Works for natural language queries: "How long does an iPhone last before I need to charge it again?"
- Fails with keyword matching scenarios
- Easy to know when each technique works by analyzing query patterns
- Recommendation: Do loss analysis to see if query stream matches the use case before investing

### [Technique 4: Re-rankers (Cross-Encoders)](https://www.youtube.com/watch?v=w9u11ioHGA0&t=370s)
**[06:10 - 07:01]**

- Used after combining BM25 and vector results to resolve conflicted candidate sets
- Cross-encoders vs. embeddings: Take both query and document, attend to both simultaneously for scoring
- More powerful but expensive—can't run on all documents
- Strategy: Retrieve many candidates, then re-rank smaller set with cross-encoder
- Really powerful, should use it, but has failure cases too

### [Technique 5: Custom Embeddings](https://www.youtube.com/watch?v=w9u11ioHGA0&t=421s)
**[07:01 - 09:00]**

- Problem: Standard embeddings only measure semantic similarity, not domain-specific ranking needs
- Relevance is not ranking—learned from 15-20 years of Google Search
- Example from Harvey (legal domain): Query with legal semantics impossible to catch with just relevance
- Terms like "regime," "material" have very specific legal meanings that differ from general usage
- When vocabulary is domain-specific and off-distribution, need custom embeddings
- Decision criteria: Eval sets, query sets, loss analysis showing vocabulary mismatch
- Don't overthink—let your data tell you if you need it

### [Technique 6: Multi-Signal Ranking](https://www.youtube.com/watch?v=w9u11ioHGA0&t=540s)
**[09:00 - 12:00]**

- Relevance helps with natural language, but many signals have nothing to do with relevance
- Examples: Price signals, merchant signals, listen count for podcasts, PageRank (prominence, not relevance)
- Perplexity example: Asked for "cheap gifts for my son, budget $50 or more" but got $15 and $40 items—price signal not captured
- Shopping domain: Need horizontal semantics (general language) AND vertical semantics (domain-specific)
- Complex applications (CRM, emails): Relevance is tiny part of semantic universe
- Ranking function evolution: Relevance → Semi-structured signals (price, merchant) → User preferences
- All signals combined into balanced ranking score

### [Technique 7: User Preference Signals](https://www.youtube.com/watch?v=w9u11ioHGA0&t=660s)
**[11:00 - 12:00]**

- Even with custom semantics, users click on unexpected items
- Need to incorporate click signals, thumbs up/down
- Build click-through prediction signal and combine with other signals
- Complex implementation but necessary at scale
- Final ranking: Relevance + Semi-structured signals + User preferences

### [Technique 8: Query Decomposition and Orchestration](https://www.youtube.com/watch?v=w9u11ioHGA0&t=720s)
**[12:00 - 14:25]**

- Problem: Impedance mismatch between search engine expectations and LLM-generated queries
- LLM doesn't know enough about your tool/search engine through prompting alone
- Solution: Take control of orchestration—decompose big query into N smaller queries ("fan out")
- Example: Google AI Mode makes 15-20 queries for complex requests
- Challenge: Boundary unclear between search engine handling complexity vs. LLM tailoring queries
- Need control because quality isn't there yet for fully autonomous agents
- Example: "Was David working on this?" needs decomposition to specific queries like "JC David Slack threads"

### [Technique 9: Supplementary Retrieval (Call More Backends)](https://www.youtube.com/watch?v=w9u11ioHGA0&t=865s)
**[14:25 - 15:40]**

- Common issue: Clients don't call search enough, try to over-optimize
- For high recall: Always search more, call more backends
- Example: "Simple Middle Eastern dish" query stumped Google Search organization
- Ambiguous intent requires reaching multiple backends: food/restaurants, images, recipes
- Google's solution: Create all backends and query them all
- Recommendation: Don't be skimpy unless facing real cost overload
- Similar to in-memory retrieval philosophy: Give more things

### [Technique 10: Model Distillation](https://www.youtube.com/watch?v=w9u11ioHGA0&t=940s)
**[15:40 - 17:12]**

- When to use: GPU cost overloads, latency becomes critical for user retention
- Large models are overqualified for specific tasks
- Example: Perplexity is very fast because they trained one model for one specific thing (question answering)
- Technique: Hold quality bar constant while decreasing model size
- Complex to implement—requires learning model fine-tuning
- Only pursue when latency directly impacts user churn (e.g., 10 seconds causes churn, 2 seconds doesn't)

### [Product Design and Graceful Degradation](https://www.youtube.com/watch?v=w9u11ioHGA0&t=1032s)
**[17:12 - 19:00]**

- When everything fails: Quality engineering will never be 100%, systems are stochastic
- Ultimate technique: "Blame the product manager" (half-joking)
- Serious point: Product design matters for how magical the system can seem
- Example from Google Shopping:
  - High understanding → High promise UI (clickable items, reviews, filters)
  - Low understanding → Degrade gracefully (show 10 things to choose from instead of prescribing one)
- UI must match understanding level
- Gracefully degrade when understanding is low, gracefully upgrade when understanding is high
- Only so much engineering can do before product must accommodate stochastic nature

### [Final Principles and Framework](https://www.youtube.com/watch?v=w9u11ioHGA0&t=1140s)
**[19:00 - 20:16]**

- Avoid theoretical debates (context window vs. RAG, agents vs. workflows, etc.)
- Everything is empirical in this domain
- Core loop: Baseline → Analyze losses → Look at toolbox for easy wins → Medium difficulty → Hard problems
- Complexity-adjusted decision making: Are there easy things? Medium things? Should I hire more people for hard things?
- Choice is yours, be principled—doing things too far ahead of curve is waste of time
- Slides available at pi.ai/talk
- Pi Labs team are information retrieval nerds, happy to discuss RAG challenges

---

## Key Takeaways

1. **Start with outcomes, not techniques**: Define quality bar and eval sets before choosing techniques
2. **Empirical over theoretical**: Let your data and query patterns guide technique selection
3. **Complexity-adjusted impact**: Always choose easy techniques first, only tackle hard ones when necessary
4. **Relevance is not enough**: Real applications need domain semantics, structural signals, and user preferences
5. **Product design matters**: UI must gracefully degrade/upgrade based on system understanding
6. **Quality engineering is iterative**: Baseline → Loss analysis → Apply technique → Repeat
7. **Systems are stochastic**: Will never be 100% perfect, plan for graceful failure

---

**Last Updated:** 2026-01-02
