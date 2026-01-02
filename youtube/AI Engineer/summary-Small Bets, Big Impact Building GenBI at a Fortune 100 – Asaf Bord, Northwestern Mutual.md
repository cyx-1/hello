# Small Bets, Big Impact: Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual

**Video URL:** https://www.youtube.com/watch?v=LU9KgcZDRfY

---

## Executive Summary

Asaf Bord from Northwestern Mutual shares how his team built a Generative BI (GenBI) system at a 160-year-old Fortune 100 financial services company. The presentation focuses on balancing innovation with stability in a risk-averse organization by using incremental development, working with real messy data, and building trust through a crawl-walk-run approach. The project demonstrates how to successfully gain executive buy-in for GenAI research by delivering tangible business value at each phase while maintaining control over risk and investment.

---

## Key Topics

### [Introduction and Context](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=45s) (00:45)
- **What is GenBI**: Fusion of Generative AI and Business Intelligence - an agent that helps people answer business questions with data
- **Northwestern Mutual background**: 160-year-old financial services and life insurance company with extensive data, resources, and use cases
- **The challenge**: Balancing stability (generational responsibility) with innovation in a risk-averse environment
- **Main goal**: Data democratization - giving people access to data without relying on BI teams

### [Four Main Challenges](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=197s) (03:17)
1. **No precedent**: No one had done GenBI in this fashion before
2. **Real messy data**: Chose to use actual 160-year-old company data instead of synthesized/cleansed data
3. **Building trust**: Both with users and leadership regarding accuracy and reliability
4. **Budget justification**: Convincing risk-averse leadership to invest in unproven technology

### [Why Use Real Data](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=293s) (04:53)
- **Understanding complexities**: Facing actual challenges that would arise in production
- **Narrowing POC-to-production gap**: What works in the lab is more likely to work in reality
- **Subject matter expertise**: Working with people who understand the data day-in and day-out
- **Real-world examples**: Getting actual questions and answers for evaluation sets
- **Business buy-in**: End users became part of the research process, creating pull rather than push for adoption

### [Building Trust with Management](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=400s) (06:40)
- **Crawl-Walk-Run approach**:
  - Start with BI experts who can validate outputs
  - Move to business managers familiar with the data
  - Eventually (future) expand to executives
- **Not building SQL from scratch initially**: Started by surfacing existing certified reports and dashboards
- **80% of BI work**: Just sending people to the right report and helping them use it
- **Setting expectations**: Delivering same assets faster and more interactively, not generating new information

### [Incremental Development Process](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=601s) (10:01)
- **Gradual approach**: Gave leadership visibility and control at each step
- **Six-week sprints**: Each phase delivered tangible business value
- **Exit points**: Leadership could pull the plug at any time if not seeing value

#### Phase Breakdown:
1. **[Phase 1: Pure Research](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=647s)** (10:47) - Natural language to SQL, response generation, question understanding
2. **[Phase 2: Metadata & Context](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=660s)** (11:00) - Understanding what good metadata looks like for BI agents; had immediate impact on broader enterprise data ecosystem
3. **[Phase 3: Semantic Search](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=722s)** (12:02) - Multi-context search, data finder, and data owner finder (saving 2-4 weeks per query)
4. **[Phase 4: Data Pivoting](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=744s)** (12:24) - Light pivoting and manipulation of pulled data
5. **[Phase 5: Enterprise Setup](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=785s)** (13:05) - Role-based access and permissions
6. **[Phase 6: Full GenBI Agent](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=799s)** (13:19) - Running SQL queries independently, complex joins (still in progress)

### [Why This Approach Worked](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=819s) (13:39)
- **Early and frequent value**: Six-week sprints with tangible deliverables
- **Transparent progress**: Clear visibility into what's being funded and outcomes
- **Incremental business value**: Each step could be productized independently
- **Learning loops**: Each phase fed insights to the next
- **Risk control**: Eliminated sunk cost bias and competitive fears; flexibility to adopt third-party solutions if better

### [Architecture Overview](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=920s) (15:20)

**Why not just use ChatGPT?**
- Schemas are messy and lack context
- Governance requirements are critical
- Need control over the system behavior

**[System Components](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=957s)** (15:57):
1. **Data and metadata layer**: Custom-built foundation
2. **Four agents**:
   - **Metadata agent**: Understands context from catalogs and documentation
   - **RAG agent**: Finds certified reports from approved list
   - **SQL agent**: Creates queries when reports don't exist or need modification
   - **BI agent**: Translates data into business answers
3. **Supporting layers**: Governance, trust, orchestration, and contextual UI

**[Workflow](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=989s)** (16:29):
1. Business question → Orchestrator
2. Metadata agent understands context
3. RAG agent searches for existing certified reports
4. If needed, SQL agent creates/modifies queries (using reports as few-shot examples)
5. Execute against database
6. BI agent translates results into business language
7. Return answer to user

**[Modular Productization](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=1087s)** (18:07): Each agent can be packaged as standalone product with business impact

### [Business Impact Metrics](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=1114s) (18:34)
- **RAG agent**: Automated 80% of the 20% of BI team capacity spent just finding and sharing reports (equivalent to 2 FTEs on a 10-person team)
- **Metadata insights**: Enabled A/B testing proving measurable value of metadata enrichment; demonstrated LLM performance improvement with good metadata
- **Data pivoting bot**: Currently in experimentation for real-time dashboard modifications
- **Next steps**: Evaluating third-party tools (Databricks Genie), rigorous catalog enrichment

### [Future Considerations](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=1250s) (20:50)
1. **Data preparation**: Major market area with many tools emerging
2. **Task-specific models**: Startups building specialized applications
3. **Co-pilot approach**: Meeting users where they are
4. **Model security**: Critical concern for enterprise adoption
5. **[SaaS pricing in GenAI era](https://www.youtube.com/watch?v=LU9KgcZDRfY&t=1286s)** (21:26):
   - Individual workers can be 10x more effective with AI
   - Question: Should pricing be based on seats, usage, or value delivered?
   - Example: Salesforce Data Cloud moving to usage-based pricing
   - Impact on global SaaS economics regardless of whether product itself uses GenAI

---

## Key Takeaways

1. **Incremental value delivery** is crucial for securing ongoing investment in GenAI research at risk-averse organizations
2. **Working with real messy data** from the start helps ensure production viability and builds stakeholder buy-in
3. **Crawl-walk-run user rollout** (experts → managers → executives) builds trust incrementally
4. **Each research phase should produce standalone business value** that can be productized
5. **Modular architecture** allows individual components to deliver ROI independently
6. **Building internal solutions creates benchmarks** for evaluating third-party alternatives
7. **Six-week sprint cycles** provide natural checkpoints for leadership to assess progress and control risk

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**Last Updated:** December 31, 2025
