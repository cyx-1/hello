# Practical tactics to build reliable AI apps — Dmitry Kuchin, Multinear

**Video URL:** https://www.youtube.com/watch?v=-T6uZYYzkWw

## Executive Summary

Dmitry Kuchin, co-founder and CTO with 15+ years of experience, presents a practical approach to building reliable AI applications that challenges conventional wisdom. The core insight: instead of using generic data science metrics like groundedness and factuality, you should evaluate AI apps based on real user scenarios and business outcomes. He advocates for building specific, scenario-based evaluations at the very beginning of development (not at the end), creating benchmarks that mimic actual user behavior, and running continuous experiments while catching regressions early. The approach emphasizes using LLMs to generate evaluations from existing materials, defining precise criteria for each scenario, and iterating rapidly with detailed feedback rather than relying on average metrics.

---

## Main Topics

### [Introduction and Speaker Background](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=17s)
**Time:** 00:17 - 01:02

Dmitry introduces himself and establishes credibility with 15 years as a startup co-founder and CTO, 5 years in executive positions at enterprises, and extensive experience developing GenAI projects ranging from POCs to production-level solutions. He notes that despite many conference tracks on evals and reliability, nobody was discussing the most important approaches.

### [The Challenge of AI Development](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=82s)
**Time:** 01:26 - 02:57

The standard software development lifecycle (design, develop, test, deploy) becomes problematic with AI. While POCs are easy and can work 50% of the time, making AI work reliably for the remaining 50% is extremely hard due to non-deterministic models. Changes to code, prompts, models, or data can impact solutions in unexpected ways, requiring a data science approach with continuous experimentation.

### [The Wrong Approach: Generic Data Science Metrics](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=177s)
**Time:** 02:57 - 04:20

People commonly make the mistake of starting with generic data science metrics like groundedness, factuality, and bias. Dmitry provides a concrete example: a colleague building a customer support bot measured factuality, but the truly important metric was the escalation rate from AI bot to human support. A response can be highly factual and grounded but still fail to provide the right answer users expect.

### [The Right Approach: Real-World Scenarios](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=260s)
**Time:** 04:20 - 05:03

The solution is to reverse-engineer metrics from real-world scenarios. Metrics should be very specific to your end goal, coming from product experience and business outcomes. Instead of measuring generic averages, you need to measure very specific criteria. Universal evals don't work - you need scenario-specific evaluations.

### [How to Build Evaluations: The Customer Support Bot Example](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=303s)
**Time:** 05:03 - 08:25

Using a bank FAQ customer support bot as an example (one of the hardest things to do properly), Dmitry demonstrates the process:
- Use advanced LLMs (like GPT-4 or o1/o3) to reverse-engineer user questions from FAQ materials
- Define specific criteria for what constitutes a correct answer (e.g., for password reset: must mention mobile validation, what to do if no mobile number, etc.)
- Missing any critical information means the answer is incorrect
- Create many variations of the same question to test consistency
- Each question needs its own specific checklist of required information

### [The Development Process: Build Evals First](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=505s)
**Time:** 08:25 - 10:01

Contrary to traditional approaches, build evaluations at the very beginning, not at the end:
1. Build first version of POC
2. Define first version of test evaluations
3. Run them and examine details (not just averages)
4. Identify why tests fail (incorrect test definition or solution not working)
5. Make changes (model, logic, prompt, or data)
6. Run experiments iteratively
7. Common problem: fixing one test often breaks previously working tests (regressions)
8. Without evaluations, you can't catch regressions in time

### [Reaching Your Benchmark](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=601s)
**Time:** 10:01 - 11:46

The iterative process continues:
- Build first version and first version of evals
- Match and run evals
- Improve solution or add more evaluations
- Continuously improve until satisfied for that specific point in time
- Result: you have a baseline benchmark for optimization
- Now you can confidently experiment with different approaches (models, architectures, etc.)

### [Optimization with Confidence](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=706s)
**Time:** 11:46 - 12:01

Once you have your benchmark, you can experiment with confidence:
- Try different models (GPT-4 vs GPT-4 mini)
- Compare approaches (graph RAG vs simpler solutions)
- Evaluate agentic approaches (better but higher inference cost and time)
- Simplify logic for specific portions
- All experimentation backed by reliable benchmarks

### [Different Solutions Require Different Evaluation Approaches](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=721s)
**Time:** 12:01 - 13:23

While the overall approach remains the same, evaluation methods differ by solution type:
- **Support bots:** Use LLM-as-a-judge with specific criteria
- **Text-to-SQL/Graph DB:** Create mock databases with known schema and data, test against known expected results
- **Call center classifiers:** Simple match tests (correct rubric or not)
- **Guardrails:** Cover questions that shouldn't be answered, should be answered differently, or have no material

### [Key Takeaways](https://www.youtube.com/watch?v=-T6uZYYzkWw&t=803s)
**Time:** 13:23 - 14:49

Final recommendations:
1. **Evaluate apps the way users actually use them** - avoid abstract metrics that don't measure what matters
2. **Use experimentation approach** - run evaluations frequently for rapid progress with fewer regressions
3. **Test frequently** - catches surprises and regressions early
4. **Get explainable AI** - properly defined evaluations give you clarity on exactly what your solution does and how it works
5. **Tools don't matter** - the approach is simple and doesn't require specific platforms (though Dmitry created Multinear open-source platform to support this workflow)

Dmitry emphasizes that he's not trying to sell anything - the platform is completely open source and could be recreated in days. The value is in the approach, not the tooling.

---

**Summary created:** 2026-01-02
