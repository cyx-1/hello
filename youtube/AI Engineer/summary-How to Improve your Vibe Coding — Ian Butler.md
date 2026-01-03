# How to Improve your Vibe Coding — Ian Butler

**Video URL:** https://www.youtube.com/watch?v=g03m-WFEu1U

---

## Executive Summary

Ian Butler, CEO of Bismouth, presents findings from a comprehensive benchmark evaluating how well AI coding agents find and fix bugs. The research tested 6 agents across 100+ repositories and 1,200+ issues, revealing that popular agents like Cursor and Devon have alarmingly high false positive rates (97% and <10% true positive rates). He provides practical tips for improving "vibe coding" with AI agents, including using bug-focused rules, managing context carefully, and leveraging thinking models which significantly outperform standard models at finding bugs.

---

## Main Topics

### [Introduction & Problem Statement](https://www.youtube.com/watch?v=g03m-WFEu1U&t=0s)
**[00:00 - 01:39]**

- Ian Butler introduces Bismouth, an end-to-end agentic coding solution
- They've been benchmarking agent performance at finding and fixing bugs for several months
- Key finding: Agents have very low overall bug detection rates and generate massive numbers of false positives
- Popular agents like Devon and Cursor have less than 10% true positive rates
- This creates "alert fatigue" that reduces developer trust in these tools

### [The Hard Truth: Benchmark Results](https://www.youtube.com/watch?v=g03m-WFEu1U&t=74s)
**[01:14 - 01:59]**

- 3 out of 6 agents tested had 10% or less true positive rates out of 900+ reports
- One agent generated 70 issues for a single task - all were false positives
- Cursor specifically had a 97% false positive rate across 100+ repos and 1,200+ issues
- Real-world impact: Alert fatigue reduces trust in agents, causing bugs to slip into production
- Agents struggle with "needle in a haystack" problems when navigating larger codebases

### [Solution #1: Bug-Focused Rules](https://www.youtube.com/watch?v=g03m-WFEu1U&t=120s)
**[02:00 - 04:26]**

- Use agent rules files to provide scoped instructions about security issues and logical bugs
- Feed specific security information like OWASP Top 10 to bias the model
- Prioritize explicit bug classes rather than vague "find bugs" requests
- Example: Instead of "find bugs", specify "examine for auth bypasses, SQL injection, protocol pollution"
- Require fix validation - mandate tests must pass before changes are accepted
- Structured rules eliminate vague requests that produce alert fatigue and prime agents for higher quality output

### [Solution #2: Context Management](https://www.youtube.com/watch?v=g03m-WFEu1U&t=266s)
**[04:26 - 05:30]**

- Agents struggle significantly with cross-repo navigation and understanding
- When agents hit context limits, they summarize/compact files, which severely reduces bug detection ability
- Users need to actively manage context in their IDE:
  - Feed diffs of changed code to help agents understand cause and effect
  - Ensure key files aren't being summarized or removed from context
  - Ask agents to create a step-by-step component inventory (classes, variables, usage patterns)
- Creating an inventory helps agents become much more effective at finding bugs

### [Solution #3: Thinking Models Rock](https://www.youtube.com/watch?v=g03m-WFEu1U&t=330s)
**[05:30 - 06:44]**

- Thinking models (like Claude Opus with chain-of-thought) significantly outperform standard models
- Their thought traces show them expanding across multiple considerations in the codebase
- They dive deeper into the chain of thought when finding bugs
- In practice, they find deeper bugs than non-thinking models
- Limitation: Even thinking models show high variability across runs - the specific bugs found change between runs even if the total count stays similar
- Agents aren't truly holistically looking at files like humans do
- Users shouldn't need to run agents 100 times to get comprehensive bug coverage (this remains an unsolved problem)

### [Bismouth Product Pitch & Resources](https://www.youtube.com/watch?v=g03m-WFEu1U&t=404s)
**[06:44 - 07:25]**

- Bismouth.sh features: automatic PR creation, GitHub/GitLab/Jira/Linear integration
- Scans for vulnerabilities and provides code reviews
- Offers on-prem deployments
- Full benchmark available on their website with methodology, results, and raw data
- Includes SM100 benchmark for evaluating agent performance at finding and fixing bugs

---

## Key Takeaways

1. **Current agent performance is poor**: Less than 10% true positive rates for bug detection
2. **Be specific with instructions**: Use explicit bug classes and security frameworks (OWASP Top 10)
3. **Manage context actively**: Don't let agents summarize key files; provide diffs and ask for component inventories
4. **Use thinking models**: They find deeper, more complex bugs than standard models
5. **Require validation**: Always mandate tests pass before accepting fixes
6. **Alert fatigue is real**: Too many false positives reduce trust and let bugs slip through

---

**Closing quote:** "May your vibes be immaculate."
