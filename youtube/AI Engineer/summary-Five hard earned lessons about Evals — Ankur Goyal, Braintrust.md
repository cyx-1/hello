# Five Hard Earned Lessons About Evals — Ankur Goyal, Braintrust

**Video URL:** https://www.youtube.com/watch?v=a4BV0gGmXgA

---

## Executive Summary

Ankur Goyal, founder of Braintrust, shares five critical lessons learned about implementing effective AI evaluations (evals). The talk emphasizes that successful evals enable rapid model adoption (within 24 hours), require significant engineering investment rather than off-the-shelf solutions, focus on context beyond just prompts, must adapt to evolving AI models, and should be used proactively to guide product decisions rather than just prevent regressions. Real-world examples from companies like Notion and Replit demonstrate how well-engineered evals become a competitive advantage in the rapidly evolving AI landscape.

---

## Topics and Key Points

### 1. [Three Signs of Successful Evals](https://www.youtube.com/watch?v=a4BV0gGmXgA&t=16s)
**Timestamp: 00:16 - 02:13**

- **24-hour model deployment capability**: When a new model releases, you should be able to incorporate it into production within 24 hours
  - Example: Notion (mentioned by Sarah from Notion) consistently ships new model updates within 24 hours of release
  - If you can't do this, your evals infrastructure needs improvement

- **Clear path from user feedback to evals**: When users complain, you need a straightforward process to add their feedback into your eval dataset
  - Without this, valuable user insights disappear "into the ether"
  - This creates a feedback loop for continuous improvement

- **Use evals offensively, not just defensively**: Evals should help you understand which use cases you can solve and how well BEFORE shipping
  - Unlike unit tests that only catch regressions
  - Before launching new products, evals give you a reliable prediction of real-world performance

### 2. [Great Evals Must Be Engineered](https://www.youtube.com/watch?v=a4BV0gGmXgA&t=133s)
**Timestamp: 02:13 - 04:08**

- **No perfect dataset exists**: Synthetic datasets and generic "LLM-as-a-judge" scores aren't sufficient
  - Exception: Well-defined problems like competition math that already work perfectly
  - For most real-world use cases, pre-made datasets don't represent actual user experiences

- **Datasets require continuous reconciliation**: Best datasets evolve as you learn from production reality
  - This requires significant engineering investment
  - Treat dataset creation as an engineering problem, not a given

- **Scorers are like a PRD/spec for your AI application**:
  - Every advanced company writes custom scoring functions and constantly modifies them
  - Braintrust offers "auto evals" open-source library, but it's intentionally flexible
  - Generic scorers are specs for someone else's project, not yours
  - Justifies investment beyond off-the-shelf solutions

### 3. [Context Matters More Than Prompts](https://www.youtube.com/watch?v=a4BV0gGmXgA&t=248s)
**Timestamp: 04:08 - 06:40**

- **Traditional prompt engineering is evolving**: Must think beyond the system prompt to include all context

- **Modern agent prompts consist of**:
  - System prompt
  - For loop with: LLM calls → tool calls → incorporate results → iterate
  - Analysis of real agent trajectories shows the vast majority of tokens come from tool outputs, not the system prompt

- **Tool design is critical**:
  - Can't just mirror existing APIs or products
  - Must design tools for what the LLM wants to see
  - Writing good tools is "very disruptive" - not just an API wrapper layer

- **Tool output format matters significantly**:
  - Example: Switching from JSON to YAML made a measurable difference
  - YAML is more token-efficient and easier for LLMs to analyze
  - While JavaScript treats both as structured data, LLMs process them very differently
  - Must be thoughtful about tool definitions and outputs to maximize LLM performance

### 4. [Be Ready When New Models Change Everything](https://www.youtube.com/watch?v=a4BV0gGmXgA&t=400s)
**Timestamp: 06:40 - 08:40**

- **Model improvements can unlock new capabilities**: Engineer your team and product to capitalize quickly
  - Credit to Replit team for pioneering this pattern

- **Real example from Braintrust's own product**:
  - Maintained an eval for a feature for months before it was viable
  - Performance progression:
    - GPT-4o: ~10% (not viable for users)
    - GPT-4o1: slight improvement
    - Claude 3.7 Sonnet: much better
    - Claude 4 Sonnet: remarkably better (~90% success rate)
  - Because they had the eval ready, they shipped the feature just 2 weeks after Claude 4 Sonnet's release

- **Key mindset shift**: When new models come out, everything might change - be positioned to seize opportunities

### 5. [Simple Scoring Can Be Effective](https://www.youtube.com/watch?v=a4BV0gGmXgA&t=520s)
**Timestamp: 08:40 - 11:00**

- **Don't over-engineer scoring initially**: Start simple and iterate
  - Example: Basic "did it work? yes/no" scoring can be highly effective

- **Demo: AI-powered scoring tool**:
  - Braintrust's new feature that auto-generates scorers from natural language descriptions
  - Input: Description of what "good" looks like
  - Output: Executable scorer code
  - Can refine the scorer through conversational feedback
  - Handles both simple criteria and complex multi-step reasoning

- **Practical scoring approach**:
  - Start with basic metrics
  - Use LLM-assisted scoring to scale review capacity
  - Continuously refine based on real examples
  - Balance automation with human oversight

### 6. [Bonus: Building Trust in AI Systems](https://www.youtube.com/watch?v=a4BV0gGmXgA&t=660s)
**Timestamp: 11:00 - 14:30**

- **Evals create confidence**: When you have comprehensive evals, you can ship AI features with confidence

- **Iterative improvement cycle**:
  - Deploy → Collect real data → Update evals → Refine system → Redeploy
  - Each iteration makes the system more aligned with real-world usage

- **Product development implications**:
  - Can make data-driven decisions about which AI features to prioritize
  - Quantify improvement from different approaches
  - Set clear quality bars before launch

- **Organizational impact**:
  - Evals become shared language between product, engineering, and ML teams
  - Enables faster iteration cycles
  - Reduces guesswork in AI product development

---

## Key Takeaways

1. **Speed is a competitive advantage**: Ability to ship new model updates within 24 hours separates leaders from followers

2. **Investment in evals infrastructure pays dividends**: Don't rely on generic solutions - build custom evals tailored to your specific use cases

3. **Context engineering > Prompt engineering**: Focus on tool design and outputs, not just system prompts

4. **Maintain evals for future capabilities**: Track metrics on features that aren't viable yet - new models might change that overnight

5. **Start simple, iterate constantly**: Begin with straightforward scoring and evolve based on production learnings

6. **Evals enable offensive strategy**: Use them to discover new opportunities, not just prevent regressions

---

**Last Updated:** January 1, 2026
