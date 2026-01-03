# Make your LLM app a Domain Expert: How to Build an Expert System

**Speaker:** Christopher Lovejoy, Medical Doctor & AI Engineer at Anterior
**Video URL:** https://www.youtube.com/watch?v=MRM7oA3JsFs
**Channel:** AI Engineer

---

## Executive Summary

Christopher Lovejoy, a medical doctor turned AI engineer at Anterior, shares a comprehensive playbook for building domain-native LLM applications that achieve expert-level performance. Drawing from his experience building AI systems for healthcare (serving 50M lives in the US), he argues that **the system for incorporating domain insights is far more important than model sophistication**. The core thesis: solving the "last mile problem" requires an **Adaptive Domain Intelligence Engine** that systematically converts customer-specific domain expertise into measurable performance improvements. The approach achieved 99% accuracy in medical necessity reviews, up from 95% baseline, by creating tight feedback loops between domain experts, engineers, and production data.

---

## Key Topics

### 1. **Introduction & Background** - [00:16](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=16s)
- Christopher's journey: 8 years as a medical doctor, 7 years building AI systems with medical domain expertise
- Worked at Serakare (tech-enabled home care, hit $500M ARR)
- Currently at Anterior: NY-based clinician-led company providing clinical reasoning tools for health insurance
- Serves health insurance providers covering ~50M lives in the US

**Key Insight:** Domain expertise + AI engineering creates unique competitive advantage in vertical applications.

---

### 2. **The Core Thesis: System > Model** - [01:19](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=79s)
- For vertical AI applications, the system for incorporating domain insights matters more than model sophistication
- Limitation isn't model reasoning capability—it's whether the model understands industry/customer-specific context
- Success requires building systems that enable rapid iteration with customers

**Key Quote:** "The limitation these days is not how powerful is your model... It's more can your model understand the context in that industry for that particular customer."

---

### 3. **The Last Mile Problem Explained** - [02:25](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=145s)
- Real-world example: 78-year-old patient with knee pain, doctor recommends arthroscopy
- Question: "Is there documentation of unsuccessful conservative therapy for at least 6 weeks?"
- Surface-level simplicity hides deep complexity:
  - **Conservative therapy ambiguity:** What counts? Physiotherapy, weight loss, medication? Depends on context.
  - **"Unsuccessful" definition:** Full symptom resolution required? Partial improvement acceptable? What threshold?
  - **Documentation standards:** Can we infer 8 weeks of treatment from a single mention? Need explicit completion documentation?

**Key Insight:** Even seemingly simple domain questions contain hidden nuances that general models miss without domain-specific context.

---

### 4. **Performance Reality: 95% → 99%** - [05:45](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=345s)
- Initial pipeline optimization (prompts, models) reached ~95% accuracy
- Hit a saturation point—couldn't improve further through traditional methods
- Applied the Adaptive Domain Intelligence system → achieved 99% accuracy
- Recently won Glassdoor Lightward Award for this achievement

**Key Insight:** The final 4-5% performance gain (95% → 99%) comes from systematic domain integration, not better models.

---

### 5. **Adaptive Domain Intelligence Engine Overview** - [06:33](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=393s)
- Two main components:
  1. **Measurement:** How is the current pipeline performing?
  2. **Improvement:** How do we systematically enhance it?
- System converts customer-specific domain insights into performance improvements
- Central role: Domain expert PM orchestrating the entire process

---

### 6. **Measurement Part 1: Define Critical Metrics** - [07:10](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=430s)
- Collaborate with customers to identify what matters most (usually 1-2 metrics)
- Examples across industries:
  - **Healthcare (Anterior):** Minimize false approvals (unnecessary care = patient risk + wasted insurance costs)
  - **Legal:** Minimize missed critical contract terms
  - **Fraud detection:** Prevent dollar loss from fraud
  - **Education:** Optimize test score improvements

**Key Practice:** Push yourself to identify the single most important metric—forces clarity and focus.

---

### 7. **Measurement Part 2: Failure Mode Ontology** - [08:24](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=504s)
- Design a taxonomy of all the ways your AI can fail
- Example categories for medical necessity review:
  1. **Medical record extraction** (data retrieval issues)
  2. **Clinical reasoning** (logical/diagnostic errors)
  3. **Rules interpretation** (guideline application mistakes)
- Each category has various subtypes
- Iterative process—requires domain experts leading the design

**Critical Success Factor:** Domain experts must lead failure mode design, not just engineers analyzing traces in isolation.

---

### 8. **The Power of Combined Measurement** - [09:15](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=555s)
- Custom dashboard showing:
  - Right side: Patient medical records + guidelines
  - Left side: AI outputs (decision + reasoning)
- Domain experts can:
  - Mark correct/incorrect
  - Tag specific failure mode
  - All in one interface

**Result:** Can plot failure modes against top metric (e.g., false approvals) to prioritize which failures to fix first.

---

### 9. **Improvement Strategy: Ready-Made Data Sets** - [10:48](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=648s)
- Failure mode labeling creates ready-made test datasets
- Advantages:
  - Directly from production (representative of real distribution)
  - More valuable than synthetic data
  - Can pick specific failure mode (e.g., 100 cases) for targeted iteration
- Engineers iterate against specific data sets with clear performance targets

**Example:** PM tells engineer: "This failure mode is at 10% accuracy. Fix it until you reach 50%."

---

### 10. **Tracking Improvements Over Time** - [11:30](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=690s)
- Visualization: Pipeline versions (x-axis) vs. Performance score (y-axis)
- Track improvements for each failure mode across releases
- Ensures no regression on previously fixed issues
- Clear visibility into which changes drive the biggest gains

---

### 11. **Domain Experts as Active Contributors** - [12:02](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=722s)
- Build tooling enabling non-technical domain experts to suggest:
  1. **Pipeline changes** (workflow adjustments)
  2. **New domain knowledge** (context the model needs)
- Domain experts best positioned to identify what knowledge matters
- Pipeline in the middle uses these suggestions
- Domain evals (failure mode datasets + generic eval sets) validate suggestions data-driven way
- Fast loop: Production issue → Clinical analysis → Domain knowledge added → Evals prove it → Goes live same day

**Architecture:** Domain Expert Suggestions → Pipeline → Domain Evals → Production

---

### 12. **Dashboard with Domain Knowledge Button** - [13:00](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=780s)
- Same review dashboard + "Domain Knowledge Addition" button
- Domain experts can suggest knowledge in context while reviewing cases
- Example failure: Model misinterprets "suspicion of condition" when patient has the condition
  - Solution: Add medical context on how "suspicion" should be interpreted
- Other example: Model lacks access to scoring systems used in clinical guidelines
  - Solution: Add scoring system as domain knowledge

**Speed:** Can go from production issue → analysis → fix → validated → live in a single day.

---

### 13. **Three Outputs from Domain Expert Reviews** - [14:27](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=867s)
Domain expert reviews generate:
1. **Performance metrics** (accuracy, false approval rate, etc.)
2. **Failure modes** (categorized error taxonomy)
3. **Suggested improvements** (domain knowledge + pipeline changes)

All from a single review workflow—highly efficient.

---

### 14. **Q&A: Defining Domain Experts** - [14:46](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=886s)
**Question:** What level of expertise is needed?

**Answer:** Depends on the workflow and optimization goals:
- For clinical reasoning quality: Need doctors with relevant specialty expertise
- For simpler tasks: Junior clinical staff (nurses) may suffice
- Core principle: Should have real-world experience performing the workflow

---

### 15. **Q&A: Bespoke vs. Off-the-Shelf Tooling** - [15:38](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=938s)
**Question:** Is this bespoke tooling?

**Answer:** Yes, for good reason:
- If domain expert feedback is central to your system and feeds into multiple parts of your pipeline
- Bespoke tooling enables tight integration with rest of platform
- Worth the investment when this is core to your competitive advantage

---

### 16. **Q&A: In-House vs. Customer Domain Experts** - [16:03](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=963s)
**Question:** Are domain experts users or employees?

**Answer:** Can be both:
- **Initially:** Hire in-house domain experts to generate initial data for iteration
- **Later:** Customers may want to validate AI outputs themselves
- Customer-facing version becomes a product feature for their validation workflows

---

### 17. **The Complete System Flow** - [16:42](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=1002s)
**End-to-End Process:**
1. **Production Application** generates AI outputs/decisions
2. **Domain Experts** review outputs → provide metrics + failure modes + suggestions
3. **PM (Domain Expert)** receives rich information on priorities (based on failure mode impact)
4. **PM** directs engineer: "Fix this failure mode to X% performance"
5. **Engineer** iterates using ready-made failure mode datasets (prompting, models, fine-tuning, etc.)
6. **Engineer** runs evals on failure mode datasets, monitors performance
7. **Engineer** reports back to PM: "Here are changes, here's impact"
8. **PM** evaluates broader product impact, makes go/no-go decision
9. **Changes go live** in production
10. **Loop continues** with new production data

**Key Feature:** Tight feedback loop with data-driven decision making at every step.

---

### 18. **Final Takeaways** - [18:07](https://www.youtube.com/watch?v=MRM7oA3JsFs&t=1087s)
1. **The Last Mile Problem:** Domain-native applications need context, not just powerful models
2. **Solution:** Adaptive Domain Intelligence Engine (systematic domain insight → performance improvement)
3. **Power Source:** Domain experts reviewing AI outputs generate:
   - Metrics
   - Failure modes
   - Suggested improvements
4. **Result:** Production data + customer context → nuanced understanding of workflows → continuous iteration toward expertise-level performance
5. **Management:** Self-improving, data-driven process managed by domain expert PM

**Final Philosophy:** This creates a competitive moat—the team that builds the best system for translating domain insights into pipeline improvements wins in vertical AI.

---

## Resources

- **Christopher's Website:** [chris-lovejoy.me](https://chris-lovejoy.me) (articles on vertical AI, evals, AI product management)
- **Contact:** chris@anterior.com
- **Careers:** [anterior.com/careers](https://anterior.com/careers)

---

## Key Technical Concepts

- **Adaptive Domain Intelligence Engine:** System that converts domain insights → performance improvements
- **Failure Mode Ontology:** Taxonomy of all possible AI failure types
- **Domain-Specific Evals:** Test sets derived from production data, labeled by failure mode
- **Last Mile Problem:** Gap between general model capability and domain-specific expertise requirements
- **Domain Expert PM:** Product manager with domain expertise orchestrating the improvement system

---

## Applicable Across Industries

While focused on healthcare, the framework applies to any vertical:
- Legal (contract analysis)
- Finance (fraud detection)
- Education (personalized learning)
- Any domain requiring nuanced, expert-level decision-making

The key is building the system that enables rapid translation of domain knowledge into model performance.
