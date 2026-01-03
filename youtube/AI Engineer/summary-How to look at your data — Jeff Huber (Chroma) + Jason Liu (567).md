# How to look at your data — Jeff Huber (Chroma) + Jason Liu (567)

**Video URL:** https://www.youtube.com/watch?v=jryZvCuA0Uc

---

## Executive Summary

This presentation by Jeff Huber (Chroma CEO) and Jason Liu covers a comprehensive two-part approach to improving AI applications through data analysis. Part 1 focuses on evaluating and optimizing retrieval inputs using fast, inexpensive evaluations with golden datasets. Part 2 demonstrates how to extract structured data from conversation outputs to make data-driven product decisions. The key thesis: you can only manage what you measure, and looking at your data (mentioned 15+ times) is essential for systematic improvement. All code and resources presented are open source.

---

## Main Topics

### 1. [Introduction & Thesis](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=0s)
**Timestamp:** 00:00 - 01:30

- Jeff Huber and Jason Liu present a content-packed two-part session
- Everything presented is open source and code available
- Central hypothesis: **You should look at your data** (goal: say this 15+ times)
- Core principle: "You can only manage what you measure" (Peter Drucker)
- Great measurement makes systematic improvement easy

**Key Points:**
- Part 1 (Jeff): How to look at your inputs (retrieval systems)
- Part 2 (Jason): How to look at your outputs (conversations)

---

### 2. [Fast Evals for Retrieval Systems](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=90s)
**Timestamp:** 01:30 - 03:00

**The Problem:** How do you know if your retrieval system is good and how to make it better?

**Bad Options:**
- Guess and cross your fingers
- Use LLM as a judge ($600 and 3 hours to run)
- Rely solely on public benchmarks (like MTeb)

**The Solution: Fast Evals**
- Simple query-document pairs (golden dataset)
- If this query goes in, this document should come out
- Measure: do the expected documents actually get retrieved?
- **Very fast and inexpensive** (runs in seconds/minutes for pennies)
- Enables rapid experimentation

**Benefits:**
- Run lots of experiments quickly and cheaply
- Experimentation energy stays high (vs. 6-hour eval runs)
- Can test different embedding models, chunking strategies, etc.

---

### 3. [Generating Synthetic Queries](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=180s)
**Timestamp:** 03:00 - 05:00

**Challenge:** What if you don't have queries yet?

**Solution:** Teach LLMs to write realistic queries
- Naive approach ("Hey LLM, write me a question") doesn't work well
- Need to align synthetic queries to real-world query patterns

**Example of Problems with Benchmarks:**
- MTeb example: "What is a pergola used for in a garden?" → answer starts with "A pergola in a garden..."
- Real-world data is **never this clean**
- Queries are too specific and don't represent actual user behavior

**Chroma's Research:**
- Deep dive into aligning synthetic queries with real-world patterns
- Graphs show semantic alignment of query specificity
- Can match synthetic queries to actual user query complexity
- Full report available at research.trychroma.com

---

### 4. [Real-World Case Study: Weights & Biases](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=300s)
**Timestamp:** 05:00 - 07:00

**Methodology:**
- Tested 4 different embedding models on W&B chatbot
- Measured recall@10 for each model
- Compared ground truth queries (actual user queries) vs. generated queries

**Key Findings:**

1. **Original model wasn't optimal:**
   - Text-embedding-3-small (their existing choice) performed the worst
   - Could empirically determine this through fast evals

2. **Public benchmarks don't tell the whole story:**
   - Jina embeddings v3 performs very well on MTeb (English)
   - But for W&B's specific data, it didn't perform as well
   - **Voyage 3 Large** actually performed best for their use case

3. **Synthetic queries aligned with real queries:**
   - Blue line (ground truth) and generated queries showed similar patterns
   - Ranking order stayed consistent between both
   - Validates that synthetic query generation works

**Takeaway:** Empirically validate on YOUR data, don't just trust benchmarks and Twitter hype.

**Resources:** Full report with notebooks at research.trychroma.com (QR code provided)

---

### 5. [Looking at Outputs: The Challenge](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=420s)
**Timestamp:** 07:00 - 09:00

**Jason Liu's Part Begins**

**When to Look Manually:**
- With hundreds of conversations: look at everything manually
- Think carefully about each interaction
- Only use LLM-based analysis when you're not smarter than the LLM

**The Scale Problem:**
- When you have thousands/tens of thousands of conversations
- Too much volume to manually review
- Too much detail in conversations (tool calls, chains, reasoning steps)
- Difficult to scan and understand

**The Hidden Value:**
- Feedback exists in the conversations themselves
- Users say things like "Try again," "This is not what I meant," "Be less lazy"
- Retry patterns reveal frustration and failure modes
- Better than thumbs up/down widgets

---

### 6. [Marketing Analogy: Segmentation Matters](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=540s)
**Timestamp:** 09:00 - 10:00

**The Problem with Single Metrics:**
- "Eval score is 0.5" → What does that mean?
- "Factuality is 0.6" → Is that good or bad?
- KPI of 0.5 → Not actionable

**Marketing Example:**
- Discover: 80% of users are under 35, 20% over 35
- Younger audience performs well, older performs poorly
- **Drawing a line in the sand enables decisions:**
  - Double down on younger audience marketing?
  - Or figure out why older audience isn't converting?
  - Should we advertise on podcasts? Run a Super Bowl ad?

**Key Insight:** Segmentation turns generic goals ("make it better") into specific, actionable strategies.

---

### 7. [Extracting Structure from Conversations](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=600s)
**Timestamp:** 10:00 - 12:00

**The Approach:**
- Extract structured metadata from conversations using LLMs
- Build a portfolio of metadata fields

**Example Extraction Schema:**
- Summary of what happened
- Tools used
- Errors encountered
- Satisfaction metrics
- Frustration metrics
- Number of conversation turns

**The Process:**
1. Extract structured data from conversations
2. Embed the metadata
3. Find clusters to identify segments
4. Test hypotheses against segments
5. Do traditional data analysis

**Why This Works:**
- Converts unstructured conversation data into analyzable structure
- Enables product engineering and data science approaches
- No different than any other product analytics

---

### 8. [Introducing Cura: Conversation Analysis Library](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=660s)
**Timestamp:** 11:00 - 13:00

**Real-World Example: Anthropic Claude**
- Found code use was 40x more represented by Claude users than GDP value creation
- Led to investing heavily in code-related features

**Cura Library Capabilities:**
- Summarize conversations
- Cluster conversations
- Build hierarchies of clusters
- Compare evals across different KPIs

**Example: Factuality Analysis**
- "Factuality is 0.6" → Hard to interpret
- "Factuality is low for queries requiring time filters" → Actionable!
- "Factuality is high for contract search queries" → Good signal!

**Pipeline Steps:**
1. **Summarization models** - Extract key information
2. **Clustering models** - Find cohesive groups
3. **Aggregation models** - Build hierarchies

**Demo with Fake Gemini Data:**
- Load conversations
- Extract summaries (topics, frustrations, errors)
- **Cluster findings:**
  - Data visualization requests
  - SEO content requests
  - Authentication errors
- **Higher-level themes:**
  - Technical support issues
  - Database debugging needs
  - Data visualization tools needed

---

### 9. [Making Product Decisions from Clusters](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=780s)
**Timestamp:** 13:00 - 15:00

**From Clusters to Action:**

After clustering, you see patterns:
- **High-level usage:** SEO, content, data analysis
- **Lower-level specifics:** Blog posts, marketing

**Decision Framework:**
- What kind of tools should we build?
- How should we develop our product?
- Should we change our marketing?
- Do we need to update prompts?

**The Goal:** Understand what to do next
- Segmentation reveals hypotheses
- Make targeted investments within segments
- Example: 80% of conversations are about SEO optimization → build SEO integrations

**Key Principle:**
- Often the solution isn't making the AI better
- It's providing the right infrastructure and tools
- Example: Many queries use time filters → add time filter metadata to improve evals significantly
- Example: Contract signature detection → add one more OCR extraction step

---

### 10. [The Improvement Process](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=840s)
**Timestamp:** 14:00 - 16:00

**Standard Practice:**
1. Define evals

**Missing Practice (often overlooked):**
2. Find clusters in conversations
3. Compare KPIs across clusters
4. Make decisions: what to build, fix, or ignore

**The 2x2 Matrix: Usage vs. Performance**

|  | **Low Usage** | **High Usage** |
|---|---|---|
| **High Performance** | → Market/educate users<br/>→ Add pre-filled questions<br/>→ Show capabilities | ✅ **Great!** Keep doing this |
| **Low Performance** | → Add "Sorry, can't help" message<br/>→ Redirect to manager | 🔴 **Critical!** Must fix |

**Decision Examples:**
- **High usage + bad performance:** Clearly must fix
- **High usage + good performance:** All good, keep going
- **Low usage + good performance:** Product/marketing issue, educate users
- **Low usage + bad performance:** One-line prompt change: "Sorry, I can't help you"

---

### 11. [Monitoring and Continuous Improvement](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=900s)
**Timestamp:** 15:00 - 16:30

**After Clustering:**
- Build classifiers to identify specific intents
- Build routers for different query types
- Build more tools based on discovered needs
- Monitor performance over time

**Monitoring Approach:**
- Track different categories of query types over time
- "0.5" doesn't mean anything in isolation
- **Changes over time across specific categories** reveal product usage patterns

**Real-World Discovery:**
- New customers use applications very differently than historical customers
- Can make targeted investments based on usage patterns
- Creates data-driven product roadmap

**Core Philosophy:**
- Research leads to better products
- NOT: products justifying research we don't know is possible
- True progress = high-quality hypotheses + ability to test many hypotheses quickly

---

### 12. [Key Takeaways & Resources](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=980s)
**Timestamp:** 16:30 - 18:40

**Part 1 Takeaways (Inputs/Retrieval):**
1. **Don't use public benchmarks alone** - Build evals on YOUR data
2. **Focus on retrieval first** - It's the only thing LLM improvements won't fix
3. **LLMs get better over time, but bad retrieval stays bad**
4. **Earn the right to tinker with the LLM** by having good retrieval
5. **Start with synthetic data** if you don't have users yet
6. **Once you have users, look at your data**

**Part 2 Takeaways (Outputs/Conversations):**
1. **Extract structure** from conversations
2. **Understand the data:**
   - How many conversations?
   - Tool misuse patterns?
   - Error types?
   - Frustration signals?
3. **Do population-level data analysis**
4. **Find similar clusters**
5. **Create impact-weighted understanding** of what matters

**Example Impact Statement:**
- ❌ "Maybe we should build more data visualization tools"
- ✅ "40% of our conversations are about data visualization, and code execution only succeeds 10% of the time. We should build 2 more plotting tools and measure the impact."

**Compare KPIs across clusters:**
- Make better decisions across product development
- Start small, look for structure, understand structure
- Compare KPIs to decide: what to fix, what to build, what to ignore

**Resources:**
- **Chroma research:** research.trychroma.com
- **Cura library notebooks:** [Jupyter notebooks with W&B conversation analysis]
- Three notebooks covering the full process from loading conversations to making product decisions

---

### 13. [Q&A: Spicy Take](https://www.youtube.com/watch?v=jryZvCuA0Uc&t=1110s)
**Timestamp:** 18:30 - 19:15

**Question:** What's the spicy take?

**Answer:** "More agent businesses should try to price their services on the work done rather than the tokens used. Price on success, price on value."

(Note: Unrelated to the main talk, but an interesting business model perspective)

---

## Additional Resources

1. **Full Research Report:** research.trychroma.com
   - Deep dive into synthetic query generation
   - Alignment methodology for real-world queries
   - Full notebooks with code

2. **Cura Library:**
   - Three Jupyter notebooks demonstrating:
     - Loading W&B conversations
     - Cluster analysis
     - Making product decisions from data

3. **All code is open source** - QR codes provided in presentation

---

## Key Quotes

> "You can only manage what you measure." - Peter Drucker

> "Look at your data." - Repeated 15+ times throughout the talk

> "Real-world data is never this clean." - On benchmark datasets

> "You need to earn the right to tinker with the LLM by having good retrieval."

> "Often the solution isn't making the AI better. It's really just providing the right infrastructure."

> "Research leads to better products, rather than products justifying research we don't know is possible."

> "It's one thing to say 'maybe we should build more tools.' It's another thing to say '40% of our conversations are about X and we only succeed 10% of the time.'"
