# How BlackRock Builds Custom Knowledge Apps at Scale — Vaibhav Page & Infant Vasanth, BlackRock

**Video URL:** https://www.youtube.com/watch?v=08mH36_NVos

---

## Executive Summary

BlackRock's data engineering team presents their framework for rapidly building custom AI-powered knowledge applications at scale. The presentation focuses on how they reduced the time to build complex AI applications from 3-8 months down to a couple of days through a sandbox-and-factory architecture. Their approach emphasizes enabling domain experts to build applications through prompt engineering, modular LLM strategies, and human-in-the-loop design, particularly important in the highly regulated financial services environment.

---

## Main Topics

### 1. BlackRock's Business Context and Use Cases
[https://www.youtube.com/watch?v=08mH36_NVos&t=0s](https://www.youtube.com/watch?v=08mH36_NVos&t=0s)

**Key Points:**
- BlackRock is the world's largest asset management firm where portfolio managers process torrents of daily information to develop investment strategies
- Investment operations teams build internal tools to support activities from data acquisition through trade execution, compliance, and post-trading operations
- AI applications fall into four categories:
  - Document extraction (extracting entities from documents)
  - Complex workflow/automation (multi-step processes with downstream integrations)
  - Q&A systems (chat interfaces)
  - Agentic systems

**Specific Use Case - New Issue Operations** ([https://www.youtube.com/watch?v=08mH36_NVos&t=143s](https://www.youtube.com/watch?v=08mH36_NVos&t=143s))
- Team responsible for setting up new securities when market events occur (IPOs, stock splits)
- Must ingest prospectuses/term sheets, consult domain experts (equity teams, ETF teams), produce structured output, and integrate with downstream systems
- Process traditionally takes a long time and involves complex coordination between business and engineering teams

### 2. Challenges with Building AI Apps at Scale
[https://www.youtube.com/watch?v=08mH36_NVos&t=240s](https://www.youtube.com/watch?v=08mH36_NVos&t=240s)

**Challenge #1: Prompt Engineering** ([https://www.youtube.com/watch?v=08mH36_NVos&t=245s](https://www.youtube.com/watch?v=08mH36_NVos&t=245s))
- Complex financial documents require extensive prompt development
- Prompts that start as a couple of sentences quickly become three paragraphs long
- Need for prompt versioning, comparison, and evaluation against test datasets
- Domain experts must iterate extensively with engineering teams

**Challenge #2: LLM Strategy Selection** ([https://www.youtube.com/watch?v=08mH36_NVos&t=262s](https://www.youtube.com/watch?v=08mH36_NVos&t=262s))
- Different strategies needed depending on the use case:
  - Simple documents: in-context learning with simple models
  - Large documents (thousands to 10,000+ pages): requires different approaches due to context limitations
  - Often requires mixing multiple strategies
- Must iterate across different prompts AND different LLM strategies
- Context limitations, model limitations, and vendor differences add complexity
- This iteration process can take months

**Challenge #3: Deployment Complexity** ([https://www.youtube.com/watch?v=08mH36_NVos&t=359s](https://www.youtube.com/watch?v=08mH36_NVos&t=359s))
- Traditional challenges: distribution, access control, app federation
- AI-specific challenges: choosing appropriate cluster types
  - GPU-based inference clusters for bulk overnight processing (e.g., analyzing 500 research reports)
  - Burstable clusters for on-demand processing (e.g., new issue setup)
- Need for CI/CD pipeline integration and cost controls

### 3. The Solution: Sandbox and App Factory Architecture
[https://www.youtube.com/watch?v=08mH36_NVos&t=421s](https://www.youtube.com/watch?v=08mH36_NVos&t=421s)

**Results Achieved:**
- Compressed development time from 3-8 months to a couple of days
- Enabled domain experts to build applications with minimal engineering involvement

**Architecture Components:**

**Data Platform & Developer Platform** (foundational layers)
- Standard data ingestion and orchestration
- Pipeline transformations
- Distribution as apps or reports

**Sandbox** ([https://www.youtube.com/watch?v=08mH36_NVos&t=527s](https://www.youtube.com/watch?v=08mH36_NVos&t=527s))
- Playground for operators to quickly build and refine extraction templates
- Federated to domain experts for rapid iteration
- Key capabilities:
  - Prompt creation
  - Extraction template management
  - LLM strategy selection
  - Extraction runs
  - Comparison and contrast of results
  - Building transformation logic
  - Executor configuration

**App Factory** ([https://www.youtube.com/watch?v=08mH36_NVos&t=506s](https://www.youtube.com/watch?v=08mH36_NVos&t=506s))
- Cloud-native operator that takes definitions and spins out applications
- Automates the deployment pipeline
- Takes knowledge from sandbox and creates end-to-end applications

### 4. Technical Implementation Details
[https://www.youtube.com/watch?v=08mH36_NVos&t=537s](https://www.youtube.com/watch?v=08mH36_NVos&t=537s)

**Extraction Template Configuration** ([https://www.youtube.com/watch?v=08mH36_NVos&t=600s](https://www.youtube.com/watch?v=08mH36_NVos&t=600s))
- Goes beyond simple prompt templates and data types
- Supports complex configurations:
  - Multiple QC checks on result values
  - Extensive validations and constraints on fields
  - Inter-field dependencies (e.g., if bond is callable, then call date and call price must have values)
- Fields include:
  - Field name
  - Data type
  - Source (extracted vs. derived)
  - Required/optional status
  - Field dependencies and validations

**Document Management** ([https://www.youtube.com/watch?v=08mH36_NVos&t=667s](https://www.youtube.com/watch?v=08mH36_NVos&t=667s))
- Documents ingested from data platform
- Tagged by business category
- Labeled and embedded

**Transformation and Execution Workflows** ([https://www.youtube.com/watch?v=08mH36_NVos&t=738s](https://www.youtube.com/watch?v=08mH36_NVos&t=738s))
- Low-code/no-code framework for operators
- Operators build transformation and execution workflows
- End-to-end pipeline from extraction to downstream integration
- Addresses the gap in existing tools that do extraction well but struggle with downstream process integration
- Eliminates manual CSV/JSON downloads and transformations

**End-User Experience** ([https://www.youtube.com/watch?v=08mH36_NVos&t=846s](https://www.youtube.com/watch?v=08mH36_NVos&t=846s))
- End users receive complete applications without needing to:
  - Configure templates
  - Understand integration details
  - Worry about transformation logic
- Simply upload documents, run extraction, and get results through entire pipeline

### 5. Key Takeaways and Best Practices
[https://www.youtube.com/watch?v=08mH36_NVos&t=777s](https://www.youtube.com/watch?v=08mH36_NVos&t=777s)

**Takeaway #1: Invest in Prompt Engineering Skills** ([https://www.youtube.com/watch?v=08mH36_NVos&t=781s](https://www.youtube.com/watch?v=08mH36_NVos&t=781s))
- Especially critical in financial services
- Defining and describing complex financial documents is very difficult
- Domain experts need deep prompt engineering capabilities

**Takeaway #2: Educate on LLM Strategies** ([https://www.youtube.com/watch?v=08mH36_NVos&t=792s](https://www.youtube.com/watch?v=08mH36_NVos&t=792s))
- Educate the firm on what different LLM strategies mean
- Help teams understand how to select appropriate strategies for specific use cases
- No one-size-fits-all approach

**Takeaway #3: Evaluate ROI Carefully** ([https://www.youtube.com/watch?v=08mH36_NVos&t=804s](https://www.youtube.com/watch?v=08mH36_NVos&t=804s))
- Great for experimentation and prototyping, but production requires ROI analysis
- Consider whether custom AI apps are more expensive than off-the-shelf products
- Make data-driven decisions about when to build vs. buy

**Takeaway #4: Design for Human-in-the-Loop** ([https://www.youtube.com/watch?v=08mH36_NVos&t=827s](https://www.youtube.com/watch?v=08mH36_NVos&t=827s))
- Despite temptation to go "all agent tech," human oversight is critical in regulated environments
- Compliance and regulations require four-eyes checks
- Design applications with human-in-the-loop from the start, especially in highly regulated industries

### 6. Q&A Highlights
[https://www.youtube.com/watch?v=08mH36_NVos&t=892s](https://www.youtube.com/watch?v=08mH36_NVos&t=892s)

**On Executive Use Cases** ([https://www.youtube.com/watch?v=08mH36_NVos&t=930s](https://www.youtube.com/watch?v=08mH36_NVos&t=930s))
- Framework specifically targets investment operations domain experts building applications
- CEO-level use cases (asset/liability memos, etc.) would be different initiatives
- Framework has reusable components that can be leveraged for other use cases

**On Security and Data Protection** ([https://www.youtube.com/watch?v=08mH36_NVos&t=1033s](https://www.youtube.com/watch?v=08mH36_NVos&t=1033s))
- Multiple layers of security controls from infrastructure through platform, application, and user levels
- Different policies across the stack
- Software-defined networking with comprehensive security policies

**On Handling Complex Documents** ([https://www.youtube.com/watch?v=08mH36_NVos&t=1093s](https://www.youtube.com/watch?v=08mH36_NVos&t=1093s))
- Multiple model providers used
- Multiple different strategies employed based on use case
- Various engineering tweaks applied
- Quite complex process overall

---

## Notable Insights

1. **Scale of Impact**: Reducing app development from 3-8 months to days represents a 90%+ time reduction
2. **Modular Approach**: Success comes from federating bottlenecks (prompt creation, LLM strategy selection, transformation logic) to domain experts
3. **Regulatory Constraints**: Human-in-the-loop design is not optional in financial services - it's a regulatory requirement
4. **Practical AI**: The team acknowledges agentic systems "don't quite work right now" for their complex use cases due to domain knowledge complexity

---

*Video Duration: ~18 minutes*
*Presentation by: Infant Vasanth (Director of Engineering) and Vaibhav Page (Principal Engineer) from BlackRock's Data Teams*
