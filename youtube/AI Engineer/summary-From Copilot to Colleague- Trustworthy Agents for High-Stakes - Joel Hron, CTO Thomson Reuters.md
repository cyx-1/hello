# From Copilot to Colleague: Trustworthy Agents for High-Stakes - Joel Hron, CTO Thomson Reuters

**Video URL:** https://www.youtube.com/watch?v=kDEvo2__Ijg

---

## Executive Summary

Joel Hron, CTO of Thomson Reuters, shares insights from building AI agents for high-stakes professional environments including law, tax, compliance, and fraud investigations. The talk chronicles Thomson Reuters' evolution from building "helpful" AI assistants to creating "productive" agentic systems that make autonomous decisions in domains where accuracy is critical. Key themes include treating agency as a spectrum of dials (autonomy, context, memory, coordination), the challenges of evaluation with non-deterministic systems, leveraging legacy applications as agent tools, and the importance of building complete systems rather than minimal MVPs. The presentation includes demos of AI agents handling end-to-end tax return generation and legal research with deep citation validation.

---

## Topics and Key Points

### [Introduction: The Shift from Helpfulness to Productivity](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=19s)
**Timestamp:** 00:19 - 01:00

- Thomson Reuters began building AI assistants 2-2.5 years ago with a focus on "helpfulness"
- Initial goals: accuracy, citations, and being helpful to users
- Over the past 6 months, the North Star has shifted from "helpfulness" to "productive"
- AI systems are now expected to produce output and make judgments on behalf of users
- In high-stakes environments (law, tax, global trade, fraud investigations), the risks of being wrong are not acceptable to end users

### [Company Context: Thomson Reuters Background](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=91s)
**Timestamp:** 01:31 - 03:00

- Over 100 years old as a company
- Serves legal, tax, compliance, audit, and risk industries
- 97% of top 100 US law firms are customers
- 99% of Fortune 100 companies are customers
- Top 100 US CPA firms are customers
- Employs 4,500 domain experts (highest employer of lawyers in the world)
- Maintains over 1.5 terabytes of proprietary content across industries
- Spent over $3 billion in acquisitions in recent years
- Applied research lab with 200+ scientists and engineers
- Spends over $200 million annually in capital on AI product development

### [The Profound Shift: Y Combinator's Vision](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=203s)
**Timestamp:** 03:23 - 04:00

- Y Combinator's 2025 request for startups quote: "Don't build agentic tools for law firms, build law firms of agents"
- This signifies the profound shift from helpful assistants to productive agents
- AI systems are now expected to produce output, judgments, and decisions, not just assist people

### [Understanding Agentic AI: A Spectrum, Not Binary](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=242s)
**Timestamp:** 04:02 - 05:00

- Agentic AI should be viewed as a spectrum, not binary (agentic vs. non-agentic)
- These are "dials" that can be tuned based on use case
- Exploratory use cases: dial agency up
- High-precision/certainty workflows: dial agency down
- The level of agency depends on user tolerance for risk

### [Four Agency Dials](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=301s)
**Timestamp:** 05:01 - 07:21

**1. Autonomy Dial:**
- Range: From discrete tasks (e.g., "summarize this document") to self-evolving workflows
- At high autonomy: AI plans its own work, executes, and replans based on observations

**2. Context Dial:**
- Evolution: Parametric knowledge → single RAG source → multiple knowledge sources
- Models must rationalize between controlled knowledge sources and the web
- Advanced: Models permuting data sources and updating schemas for future use

**3. Memory Dial:**
- Early RAG systems were stateless (retrieved context at point in time)
- Modern systems: Memory shared throughout workflow, across execution steps, and persistent across user sessions

**4. Coordination Dial:**
- Range: Atomic task execution → delegation to tools → full agent systems collaborating with each other

### [Key Lessons Learned](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=443s)
**Timestamp:** 07:23 - 12:01

**Lesson 1: Evaluation is the Hardest Challenge (07:35 - 09:01)**
- Users expect determinism for trust, but AI systems are non-deterministic
- Even highly trained domain experts show 10%+ accuracy swings when evaluating the same questions a week later
- Human judgment itself is highly variable
- Expensive to iterate weekly with highly trained professionals (lawyers, tax professionals)
- Challenges amplified by agentic systems:
  - Referencing source material becomes more difficult
  - Agents drift in unpredictable ways
  - Building guardrail systems requires deep expert knowledge
- Solution: Rigorous rubrics, but ultimately rely on preference-based evaluation as North Star

**Lesson 2: Legacy Applications are Enabling Assets (10:05 - 11:01)**
- Thomson Reuters has 100+ years of software with highly tuned domain logic
- Early approach: Starting over, building assistants from scratch
- New approach with agents: Decompose legacy applications into tools that agents can use
- Previously viewed as "baggage," now seen as unique assets
- Agents can leverage decades of refined business logic and domain expertise

**Lesson 3: Build the Whole System First, Not MVPs (11:03 - 12:01)**
- Teams overindexed on "minimal" in MVP
- Chased optimization rabbit holes trying to build the smallest valuable piece
- Only by building the complete system could they see:
  - Which components needed optimization
  - What was "healed" by the agentic nature of the system itself
- Mindset shift: Build the whole thing first, then learn and optimize

### [Demo 1: Tax Return Generation](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=727s)
**Timestamp:** 12:07 - 13:46

**Use Case:** End-to-end tax return preparation from source documents

**Workflow:**
1. AI extracts data from source documents (W2, 1099, etc.)
2. AI maps extracted data to tax engine fields
3. AI understands tax law rules and conditions for numerical values
4. AI determines which values apply to which lines based on context
5. AI generates complete tax return end-to-end

**Key Capabilities:**
- Leverages legacy tax calculation engine as a tool
- Uses built-in validation engine to:
  - Validate its own work
  - Inspect errors
  - Look for more information from documents when needed
  - Resolve issues to complete workflow

**Significance:** Only possible because of legacy tools (tax engine, validation engine) now accessible to AI agents

### [Demo 2: Legal Research and Litigation Preparation](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=832s)
**Timestamp:** 13:52 - 16:00

**Use Case:** Deep legal research for litigation preparation using 1.5+ TB of proprietary content

**Agent Tools from Legacy Litigation Research Product:**
- Searching for documents
- Fetching documents
- Comparing citations across cases
- Validating citations within cases

**Content Sources:**
- Case law
- Statutes
- Regulations
- Legal know-how (articles, blogs)
- Licensed content

**Agent Workflow:**
1. Agent searches multiple content sources using legacy product tools
2. Reasons across different types of legal content
3. Writes notes to itself about findings throughout the research process
4. Rationalizes notes into final comprehensive report
5. Links every claim to hard citations (actual cases, statutes)
6. Flags risk associated with each citation

**Key Differentiator:** Every blue hyperlink connects to a true case or statute in Thomson Reuters' verified content

### [Concluding Principles](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=975s)
**Timestamp:** 16:15 - 17:36

1. **Begin with the whole problem in mind** when building agentic systems
2. **Agency is a spectrum**, not binary - dial it up or down based on risk tolerance and use case
3. **Decompose legacy systems** into agent-accessible tools to bring new life to old infrastructure
4. **Focus on human-in-the-loop evaluation** - internal domain expert evaluators (SMEs) are crucial
5. **Leverage your unique assets** - For Thomson Reuters: 4,500 domain experts and terabytes of proprietary content. Ask yourself: What unique assets do you have and how can you best leverage them to create differentiation?

### [Q&A: Cybersecurity Posture](https://www.youtube.com/watch?v=kDEvo2__Ijg&t=1077s)
**Timestamp:** 17:57 - 19:33

**Question:** How would you describe the cybersecurity postures for government/financial firms (CISA requirements, LLM firewalls, guardrails, vulnerability scanning, SCM security)?

**Answer:**
- Heavily focused on compliance with FedRAMP and government standards
- Conforming to latest standards including ISO standards for AI
- Several products are compliant with recent ISO AI standards
- Rapidly evolving space - Thomson Reuters remains adaptable
- Technical documentation available online for detailed information

---

**Last Updated:** January 3, 2026
