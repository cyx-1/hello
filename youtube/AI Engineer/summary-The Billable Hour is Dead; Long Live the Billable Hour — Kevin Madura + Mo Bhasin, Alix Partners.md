# The Billable Hour is Dead; Long Live the Billable Hour — Kevin Madura + Mo Bhasin, Alix Partners

**Video URL:** https://www.youtube.com/watch?v=Wv1tAxKYLeE

---

## Executive Summary

Kevin Madura and Mo Bhasin from AlixPartners share their journey building an internal GenAI platform over two years with 20 engineers, scaling to 50 deployments and hundreds of users. They address the paradox where 89% of CEOs plan to implement AI, yet 75% struggle to achieve value and nearly half abandon initiatives. The key insight: there's a difference between employee productivity and enterprise productivity. They present three successful use cases—categorization, RAG (retrieval augmented generation), and structured data extraction—demonstrating how AI compresses the upfront work in consulting engagements from 50% to 10-20% of human effort while enabling analysis of 100% of data instead of just the top 20%. Their approach focuses on surgical deployment, building trust through accuracy, and converting skeptics into champions through concrete results.

---

## Main Topics

### [Introduction and Context](https://www.youtube.com/watch?v=Wv1tAxKYLeE&t=0s)
**Timestamp:** 00:00 - 01:28

- Mo Bhasin: Director of AI Products at AlixPartners, former co-founder of anomaly detection startup, ex-Google data scientist
- Kevin Madura: Helps companies, courts, and regulators understand AI and LLMs
- AlixPartners is a global management consulting firm that "rolls up sleeves" beyond just PowerPoints
- Platform stats: 2 years of development, 20 engineers, 50 deployments, hundreds of users
- Three main topics to cover:
  1. How AI reshapes knowledge work
  2. Three real-life use cases
  3. What doesn't work and future outlook

### [AI's Impact on Professional Services Models](https://www.youtube.com/watch?v=Wv1tAxKYLeE&t=88s)
**Timestamp:** 01:28 - 03:38

- Reference to METR (Meter) organization chart showing exponential growth in LLM task completion capabilities
- Takeoff rate significant in verifiable domains like software engineering; slower in "messy" knowledge work
- Two traditional professional services models:
  - **Junior leverage model:** Senior individuals directing many junior staff (throw 50 people at a problem)
  - **Senior leverage model:** Experienced folks (15-20 years) doing hands-on work (AlixPartners' approach)
- Future vision: AI-first firm concept (from Dvergesh Patel's podcast)
  - Replicate knowledge and experience of senior individuals
  - Scale out "50 copies of the CEO"
  - Provide leverage below using AI instead of junior staff

### [Typical Engagement Workflow](https://www.youtube.com/watch?v=Wv1tAxKYLeE&t=218s)
**Timestamp:** 03:38 - 06:29

Three phases of consulting work:

1. **Upfront Work (~50% of effort historically):**
   - Ingesting PDFs, databases, Excel files
   - Understanding what you have
   - Normalizing, categorizing data
   - Creating usable frameworks
   - AI is compressing this from 50% to 10-20% of human effort

2. **Analysis Phase (Black part):**
   - Applying playbooks and methodologies
   - Hypothesis generation
   - Deriving insights from structured data

3. **Deliverable Phase (What clients care about):**
   - Solving business problems
   - Recommendations and outputs
   - Actual value delivery

**Key Breakthrough:** No longer limited by human throughput
- Example: 5,000 contracts at 30 minutes each
- Previously: Forced to prioritize top 20% due to time/cost constraints
- Now with AI: Can analyze 100% of corpus, derive comprehensive insights
- Enables more high-value work and better outputs

### [The AI Investment Paradox](https://www.youtube.com/watch?v=Wv1tAxKYLeE&t=398s)
**Timestamp:** 06:38 - 07:27

The contradiction:
- 89% of CEOs planning to implement agentic AI (Deloitte)
- National Bureau of Economic Research: No significant impact on earnings or recorded hours
- BCG: 75% of companies struggle to achieve and scale value
- S&P Global: Almost half abandoning AI initiatives

**Key Insight:** Difference between employee productivity vs. enterprise productivity
- Focus on use cases that drive enterprise productivity, not just individual efficiency

### [Use Case 1: Categorization with Structured Outputs](https://www.youtube.com/watch?v=Wv1tAxKYLeE&t=447s)
**Timestamp:** 07:27 - 10:32

**Problem Examples:**
- IT support tickets: Categorize "laptop keeps restarting" to hardware department
- Vendor spend analysis: Categorize "United Airlines" under travel category

**Old Way (Pre-LLM):**
- Word clouds
- Build machine learning models
- Stem data, remove stop words
- Train classifiers (SVM, Naive Bayes)
- Lots of manual work

**New Way: Structured Outputs**
- Unsupervised learning approach
- Example: Categorize companies like "JD Factors" into NAICS codes
- Use tool calling to run web queries for unknown companies
- Append information and categorize at enormous volumes

**Results:**
- 95% accuracy categorizing 10,000 vendors
- Minutes instead of days
- Order of magnitude less cost

**Key Learnings:**
- **Democratized access** to text classification
- **Not unchecked**: Accuracy gains require close partnership with business
- **Converts skeptics to champions**: From push to pull demand
- **Business context critical**: Embedded in taxonomies for classification
- **Building blocks for agents**: Individual steps must be robust before chaining
- **Stochastic not deterministic**: Results come with risks

### [Use Case 2: RAG at Enterprise Scale](https://www.youtube.com/watch?v=Wv1tAxKYLeE&t=632s)
**Timestamp:** 10:34 - 12:48

**Typical Scenarios:**
- Dumped with 80GB of internal documents
- Questions like: "What did Acme release in 2020?"
- Court filings due Monday, received Friday
- "What is Acme's escalation procedures for reporting safety violations?"

**Old Approach:**
- Literal Excel index of received/not received documents
- SharePoint search (often ineffective)
- Manual document tracking

**New Approach: Enterprise RAG**
- Handles hundreds of gigabytes
- Multiple formats: PowerPoints, Word docs, Excel, CSVs
- Tool calls to third-party proprietary databases
- Democratized access to previously siloed information

**Innovation: Teaching LLMs to Use APIs**
- Previously: Teams with licenses → pull from web UI → email Excel → analysis
- Now: Embed API specs, teach LLM to call APIs directly
- Condensed days of work into immediate access

**Challenges:**
- Users have high expectations (e.g., "reason across all documents")
- RAG doesn't work that way - need step-by-step solutions
- Long journey of building features on RAG substrate

**Value:**
- Invaluable for consulting: Quick onboarding to new projects
- Substrate for additional GenAI features
- Significant time compression for high-value work

### [Use Case 3: Structured Data Extraction from Documents](https://www.youtube.com/watch?v=Wv1tAxKYLeE&t=768s)
**Timestamp:** 12:48 - 15:57

**Core Capability:**
- Take unstructured data (PDFs) and create structure
- Example: 50-page credit agreement → extract parties, maturity date, senior lenders, etc.
- Jason Liu quote: "Pydantic is all you need" (still true)

**Technical Implementation:**
- Document + Schema + LLM + Validation/Scaffolding
- Business value is in the schema definition
- Flexibility to reapply across different engagement types (M&A, investigations, etc.)

**User Trust Features:**
- Expose model internals for transparency
- Use log probabilities (log probs) from OpenAI API
- Align with structured output schema
- Calculate geometric mean of log probs for extracted values
- Color-code confidence levels (green = high, yellow = medium)
- Provides intuitive understanding for human review

**Benefits:**
- Works at scale: thousands to hundreds of thousands of documents
- Days/weeks of human review → minutes with LLMs
- "Light bulb moment" for non-technical users
- Total unlock for knowledge work
- Game-changer when properly validated

**Challenges:**
- Significant validation work required
- Must reach level of rigor users can trust
- Similar effort to Box and other providers

### [Must-Haves for Enterprise Scale](https://www.youtube.com/watch?v=Wv1tAxKYLeE&t=957s)
**Timestamp:** 15:57 - 16:56

**Critical Success Factors (Beyond Technology):**

1. **Regular Demos:**
   - Prototype in Streamlit, build production in React
   - Monthly cadence showing latest capabilities
   - Inspires the firm and secures continued investment

2. **Focus on Metrics Over Trends:**
   - Ignore "next shiny thing" (agents, MCP, latest models)
   - NPS (Net Promoter Score) and ROI are the metrics
   - Hard-earned "one bug fix at a time"

3. **Partnerships:**
   - People skills essential for enterprise success
   - Work closely with organization
   - Shared journey approach

**Final Thought:**
"Once Excel powered LLMs actually work, we will be at AGI" - humorous acknowledgment of Excel's ubiquity and complexity in enterprise settings.

---

## Key Takeaways

1. **Enterprise vs. Employee Productivity:** Focus on use cases that drive enterprise-wide value, not just individual efficiency gains

2. **Surgical Deployment:** Target specific high-value workflows rather than broad AI adoption

3. **Trust Through Accuracy:** Convert skeptics to champions by demonstrating concrete results and maintaining high accuracy standards

4. **Democratization of Capabilities:** Make advanced capabilities (text classification, API access, document analysis) accessible to non-technical users

5. **100% Coverage Advantage:** AI enables analyzing entire datasets instead of being limited to prioritized subsets

6. **Build Before Chain:** Perfect individual steps before creating agentic workflows

7. **Validation is Critical:** Invest heavily in validation and user trust mechanisms (like confidence scoring)

8. **People + Technology:** Success requires both technical excellence and organizational partnership

9. **Metrics Matter:** Focus on NPS and ROI, not latest trends or technologies

10. **The Future is Hybrid:** Combining senior expertise with AI leverage rather than junior staff leverage
