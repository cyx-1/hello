# [Full Workshop] Building Metrics that actually work — David Karam, Pi Labs (fmr Google Search)

**Video URL:** https://www.youtube.com/watch?v=jxrGodnopHo

---

## Executive Summary

This hands-on workshop, led by David Karam and his team from Pi Labs (former Google Search engineers), teaches practical methodologies for building effective evaluation metrics for AI applications. Drawing from over a decade of experience at Google Search dealing with stochastic systems, the presenters introduce a scoring system approach that breaks down coarse-grained subjective quality into multiple fine-grained, objective dimensions. The workshop covers both methodology (how to think about metrics, calibration, and iterative improvement) and practical implementation using Pi Labs' tools, including a co-pilot for building scoring systems, spreadsheet integration, and Python code examples. Key techniques demonstrated include multi-sample generation with ranking, model comparison, prompt testing, and calibrating metrics against user feedback data.

---

## Main Topics

### [Introduction and Participant Expectations](https://www.youtube.com/watch?v=jxrGodnopHo&t=0s)
**[00:00 - 06:00]**

- Workshop opens with audience interaction about evaluation challenges
- Common pain points identified:
  - Defining correct answers when outputs can vary widely
  - Bridging gap between technical metrics and business questions
  - Labor-intensive manual review processes
  - Validation taking 80% of feature development time (up from 30% in traditional QA)
  - Each use case being too unique to reuse previous work
  - Lack of best practices for AI evaluation
- Presenters introduce their Google Search background and experience with stochastic systems
- Promise to share methodology learned at Google, adapted for AI agents

### [Why Evaluation Matters - The Foundation of AI Development](https://www.youtube.com/watch?v=jxrGodnopHo&t=330s)
**[05:30 - 14:00]**

- Evals are compared to training data for machine learning - essential feedback mechanism
- Key insight: **Evals are where domain knowledge lives**, not just testing
- With good evals, you can:
  - Automate prompt optimization (using tools like DSPy)
  - Filter synthetic data for fine-tuning
  - Implement online reinforcement learning
  - Create feedback loops from production systems
- Google Search example: had 300+ metrics, not just 4
- Evaluation is not a one-time setup but an ongoing part of development
- The investment in evals pays off across multiple dimensions of development

### [The Progression of Evaluation Maturity](https://www.youtube.com/watch?v=jxrGodnopHo&t=540s)
**[09:00 - 12:30]**

1. **Vibe Testing**: Manual testing, trying things out - gets you pretty far, especially for simple applications
2. **Human Evals**: Expensive, most companies skip this unless they have subject matter experts
3. **Code-based Evals**: Where most teams spend time - writing code to test verifiable things
4. **LLM-as-Judge**: Natural language evaluation, but challenging because:
   - LLMs are designed to be creative, not consistent judges
   - Temperature affects reliability
   - Hard to get stable, reproducible results

**No right or wrong approach** - you layer these techniques based on ROI and system scale. Start simple, add sophistication as needed.

### [The Scoring System Methodology](https://www.youtube.com/watch?v=jxrGodnopHo&t=633s)
**[10:30 - 19:15]**

**Core Philosophy**: Don't build comprehensive metrics upfront. Start with 5-10 correlated signals and iterate.

**Key Principle: Break Down Subjective into Objective**
- Instead of asking "Is this helpful?" (coarse-grained, subjective)
- Break into multiple specific dimensions:
  - Does output include required fields?
  - Is the format correct?
  - Are action items specific and actionable?
  - Is the title concise (under 10 words)?
  - Does it capture key insights?

**Benefits of this approach**:
- **Lower variance**: Measuring objective things reduces flip-flopping
- **Higher precision**: Multiple signals combine for high-fidelity scores
- **Better analysis**: Can slice and dice by fine-grained dimensions
- **Iterative improvement**: Just keep adding signals as you discover what matters
- **Debuggability**: Can identify exactly what's failing

### [Demo: The Meeting Summarizer Use Case](https://www.youtube.com/watch?v=jxrGodnopHo&t=1155s)
**[19:15 - 27:45]**

**Application**: Takes meeting transcripts and generates structured JSON with:
- Title
- Key insights
- Action items
- Participants

**Pi Labs Co-pilot Tool** demonstrated:
- Start with system prompt, examples, or criteria
- Uses reasoning model to generate initial scoring dimensions
- Produces both natural language questions and Python code checks
- Example dimensions generated:
  - "Does the output include any insights from the meeting?" (NL question)
  - Title length check (Python code)
  - JSON format validation (Python code)
  - Action item presence and specificity (NL question)

**Weighting System**:
- Critical / Major / Minor labels for dimensions
- Controls relative importance
- Can be learned over time from examples
- Uses mathematical combination function

**Interactive Refinement**:
- Chat-based iteration on scoring system
- Can add, remove, or modify dimensions
- Can adjust weights in real-time
- Immediate feedback on changes

### [Spreadsheet Integration for Calibration](https://www.youtube.com/watch?v=jxrGodnopHo&t=1665s)
**[27:45 - 31:00]**

**Workflow**:
1. Copy scoring criteria from co-pilot to spreadsheet
2. Spreadsheet contains ~120 examples with real user feedback (thumbs up/down)
3. Run scorer via Extensions menu → Score Selected Ranges
4. View confusion matrix showing alignment:
   - Agreement on thumbs up
   - Agreement on thumbs down
   - Disagreements
5. Iterate on dimensions in spreadsheet to improve alignment
6. Test changes by modifying data (e.g., breaking JSON to see if metrics catch it)

**Use Case**: Calibrating automated metrics against real user behavior/preferences

### [Python Collab Notebook Implementation](https://www.youtube.com/watch?v=jxrGodnopHo&t=2184s)
**[36:24 - 40:21]**

**Step-by-step exercises**:

**1. Basic Setup and Validation** [36:56 - 37:58]
- Install Pi Labs SDK
- Define scoring spec (natural language + Python code)
- Copy spec from co-pilot's "Code" view
- Load dataset from Hugging Face (same as spreadsheet data)
- Run scorer and generate confusion matrix
- Validates alignment with user feedback

**2. Model Comparison** [38:04 - 38:48]
- Compare GPT-4o 1.5 vs 2.5 on same task
- Results: 2.5 slightly better but not huge delta (task not reasoning-heavy)
- Smaller models (Claude Haiku) show bigger quality gaps
- Process: Takes 10 examples, calls 5 different models, generates responses, scores with custom system
- **Use case**: Choosing the right model for your specific task based on YOUR criteria, not generic benchmarks

**3. Prompt Comparison** [38:48 - 39:23]
- Test different system prompts against same scoring spec
- Ensures changes don't cause regression
- Example: "Bad prompt" vs "Good prompt" shows clear score difference
- **Use case**: Safe prompt iteration with quantitative validation

**4. Online Reinforcement Learning** [39:23 - 40:21]
**Most exciting application** - Production use case
- Generate multiple responses (increase temperature, sample 3-4 responses)
- Score each response using your scoring system
- Return the highest-scoring response to user
- **Results**: Score steadily improves as you increase number of samples
- Technique used extensively at Google and big labs
- Requires no changes to prompts or models - just sampling and ranking
- Quality improvement "for free" with good scoring system

### [Production Scale Considerations](https://www.youtube.com/watch?v=jxrGodnopHo&t=1827s)
**[30:27 - 30:45]**

Question raised: How to handle tens/hundreds of thousands of examples?

Answer: Covered in Python section - teams can:
- Run on subsets for rapid iteration
- Use long-running batch processes for full dataset validation
- Integration points available for various workflows

### [Key Methodological Takeaways](https://www.youtube.com/watch?v=jxrGodnopHo&t=750s)
**Throughout workshop**

1. **Start Small, Iterate**: Begin with 5-10 signals you know correlate with quality
2. **Layer Complexity**: Add techniques based on ROI as system scales
3. **Calibrate Against Reality**: Use real user data (thumbs up/down, behavior) to validate
4. **Think in Dimensions**: Break subjective quality into objective, measurable components
5. **Treat Evals as Product**: Domain knowledge lives here, invest accordingly
6. **Embrace the Feedback Loop**: Build → Measure → Learn → Build (not one-time testing)
7. **Methodology Over Tools**: The thinking framework matters more than specific technology

### [Comparison to Google Search Experience](https://www.youtube.com/watch?v=jxrGodnopHo&t=345s)
**[05:45 - 07:43]**

- Google called this "quality" not "evals"
- Constant benchmarking: exhaust one benchmark, move to next
- 300+ metrics for search (vs. typical 4 metrics teams start with)
- Metrics calibrated against both human raters and user behavioral data
- "Arbitrarily complex" - no single solution, evolves with product
- Core to development process, not separate testing phase

---

## Resources Mentioned

- **Workshop Hub**: pi.ai/workshop (Google Doc with all links, steps, slide deck)
- **Slack Channel**: workshops (for continued discussion)
- **Pre-built Spreadsheet**: Available in workshop doc for hands-on exercises
- **Collab Notebook**: Pre-configured with all exercises ready to run
- **Dataset**: Public on Hugging Face with thumbs up/down user feedback
- **Integrations**: RLHF frameworks, other eval platforms mentioned

---

## Summary

This workshop provides a practical, methodology-driven approach to AI evaluation based on proven techniques from Google Search. The key insight is treating evaluation metrics as the primary repository of domain knowledge, not just a testing afterthought. By decomposing subjective quality into multiple objective dimensions, teams can build scoring systems that are precise, debuggable, and iteratively improvable. The hands-on exercises demonstrate real-world applications from model selection to production quality improvement through multi-sample generation. The emphasis throughout is on starting simple, measuring against reality, and layering sophistication based on what delivers value for your specific use case.

---

**Last Updated**: 2026-01-02
