# Evals Are Not Unit Tests — Ido Pesok, Vercel v0

**Video URL:** https://www.youtube.com/watch?v=L8OoYeDI_ls

---

## Executive Summary

Ido Pesok from Vercel v0 presents an introduction to evaluations (evals) at the application layer for AI systems. Using the analogy of a basketball court, he explains that evals are fundamentally different from unit tests - they're about understanding your application's "court" (domain), collecting the right data points, and systematically measuring improvements. The key insight: LLMs are inherently unreliable, so you must build a practice environment that mirrors production, collect real user queries, keep scoring simple and deterministic, and integrate evals into your CI/CD pipeline to catch regressions before they reach users.

---

## Main Topics

### [Introduction to Vercel v0](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=17s)
- Ido introduces himself as an engineer at Vercel working on v0, a full-stack vibe coding platform
- v0 recently launched GitHub sync feature allowing users to push generated code to GitHub
- Announced milestone: 100 million messages sent on the platform
- Goal: Introduction to evals specifically at the application layer (not model-level evals from research labs)

### [The Fruit Letter Counter Story - Illustrating LLM Unreliability](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=84s)
- Example app: "Fruit Letter Counter" that counts letters in fruit names
- Built with v0, tested twice, appeared to work perfectly (GPT-4 correctly returned "3" for strawberry)
- After launch, users reported failures (returned "2" instead of "3")
- Key lesson: LLMs are inherently unreliable by nature
- This principle scales from simple apps to the biggest AI applications
- AI apps are "demo savvy" - look great in demos but hallucinations appear in production

### [First Attempt at Improvement - Prompt Engineering](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=207s)
- Improved prompt with chain-of-thought: "You're an exuberant fruit-loving AI on an epic quest..."
- Tested 10 times in a row on ChatGPT - worked every time
- Shipped to production, but failed again on complex queries
- User asked about multiple fruits in one query and got wrong answer ("5")
- Reality: Users come up with queries you could never imagine
- Challenge: 95% of the app works 100% of the time (UI, auth, login), but the crucial 5% (LLM) can fail

### [The Basketball Court Analogy - Understanding Your Domain](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=311s)
- Basketball court represents your application domain
- Blue dots = successful outputs (shot made)
- Red dots = failed outputs (shot missed)
- The farther from the basket, the harder the query
- Out-of-bounds shots = queries outside your app's scope (don't waste time on these)
- Data point placement on court represents query difficulty
- Examples:
  - "How many Rs in strawberry?" - close to basket (easy)
  - Complex multi-fruit query - far from basket (hard)
  - "How many syllables in carrot?" - out of bounds (not your app's purpose)

### [Building Your Eval Dataset](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=420s)
- **Data** = points on the court (user queries)
- **Task/Shot** = how you attempt to solve the problem (your prompt, model, preprocessing)
- **Score** = did it work or not (in the basket or missed)
- Most important step: Understanding your court (your application domain)

**Common Traps to Avoid:**
- Out-of-bounds trap: Don't create evals for queries users don't care about
- Concentrated points: Don't test only easy queries - spread tests across entire domain

**How to Collect Data:**
- Thumbs up/thumbs down feedback (can be noisy but valuable signal)
- Observability logs - randomly sample 100 requests weekly and review manually
- Community forums where users report issues
- Social media (X/Twitter) - noisy but useful
- No shortcuts - must do the work to understand your domain

### [Structuring Evals - Data vs Task](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=557s)
- Put constants in **data**, variables in **task**
- Like factoring in math/programming - improves clarity, reuse, and generalization
- Example: User query "How many Rs in strawberry?" goes in data (constant)
- System prompt, preprocessing, RAG configuration go in task (variables you're testing)
- This way you can change your system prompt without recreating all your test data
- Braintrust supports this pattern well

**Using AI SDK Middleware:**
- AI SDK offers middleware abstraction for preprocessing logic
- Put RAG, system prompts, etc. in middleware
- Share same code between production API routes and evals
- Practice should mirror the real game as closely as possible

### [Scoring Strategy](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=642s)
- Scoring varies greatly by domain
- Fruit letter counter: simple check if output contains correct number
- Writing tasks: much more difficult to score

**Principles for Good Scoring:**
- Lean toward deterministic scoring and pass/fail
- Keep scores as simple as possible for easier debugging
- Ask yourself: "When looking at the data, what am I looking for to see if this failed?"
- Simple scores are easier to share across teams
- Some cases may require human review - that's okay, don't avoid building evals because of it

**Scoring Tricks:**
- Add extra prompting just for evals (e.g., "output your final answer in these answer tags")
- Makes string matching easier while production doesn't need this

### [Integrating Evals into CI/CD](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=738s)
- Add evals to continuous integration
- Braintrust provides eval reports showing improvements and regressions
- When colleague makes PR changing prompt, you can see impact across entire "court"
- Visualize: Did the change flip more tiles from red to blue?
- Prevent scenario where prompt fixes one area but breaks another

### [Benefits and Conclusion](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=790s)
- Evals are like practice for your AI system
- Can switch "players" (models) and see how different models perform
- Understand system performance when changing RAG, system prompts, etc.

**Key Quote:** "Improvement without measurement is limited and imprecise"

**Benefits of Good Evals:**
- Better reliability and quality
- Higher conversion and retention
- Less time on support and ops (practice environment catches issues)

**Final Note:** The basketball court diagrams in the presentation were built using v0 itself

### [Q&A - Handling Probabilistic Failures](https://www.youtube.com/watch?v=L8OoYeDI_ls&t=884s)
- Question about how to handle probabilistic failures (sometimes works, sometimes doesn't)
- Answer: Run evals on a schedule (daily or more frequently)
- Like basketball player with 90% success rate - may miss more in certain areas
- Running evals daily gives good sense of where failures occur and if there are regressions
- Could also run same question multiple times to get percentage success rate (4 out of 5, etc.)

---

## Key Takeaways

1. **Evals are NOT unit tests** - they're about understanding your domain and measuring improvements systematically
2. **Understand your court** - know the boundaries of your application domain and what users actually care about
3. **Collect real user data** - use feedback, logs, forums, social media to build comprehensive test datasets
4. **Keep scoring simple** - deterministic pass/fail is better than complex scoring systems
5. **Integrate into CI/CD** - catch regressions before they reach production
6. **Practice mirrors production** - share code between evals and production to ensure realistic testing
7. **Measure to improve** - without measurement, improvement is limited and imprecise

---

**Channel:** AI Engineer
**Speaker:** Ido Pesok, Engineer at Vercel v0
**Tools Mentioned:** Vercel v0, Braintrust, AI SDK
