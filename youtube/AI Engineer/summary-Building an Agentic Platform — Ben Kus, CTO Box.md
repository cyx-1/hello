# Building an Agentic Platform — Ben Kus, CTO Box

**Video URL:** https://www.youtube.com/watch?v=12v5S1n1eOY

---

## Executive Summary

Ben Kus, CTO of Box, shares Box's journey from simple single-shot AI calls to sophisticated agentic architectures for data extraction from unstructured documents. The talk demonstrates how agentic approaches solved critical challenges including complex document processing, OCR limitations, multilingual support, and high-accuracy requirements for enterprise customers. Key insight: agentic architecture provides a clean abstraction layer that's easy to evolve and should be adopted early when AI models can potentially solve your problem.

---

## Main Topics

### [Introduction to Box and AI Journey](https://www.youtube.com/watch?v=12v5S1n1eOY&t=18s)
**Timestamp: 00:18**

- Box is an unstructured content platform serving 115,000+ enterprise customers
- Two-thirds of Fortune 500 companies use Box
- Over 1 exabyte of data and hundreds of billions of files
- For many enterprises, their first AI deployment was with Box due to security concerns
- Box focuses on safe and secure AI at the platform level
- Started AI journey in 2023 after generative AI became production-ready

**Key Points:**
- Box specializes in secure AI deployment for enterprises
- Built multiple AI features: Q&A across documents, data extraction, AI-powered workflows
- Focus of this talk: data extraction from unstructured documents

### [The Promise of Early AI - Single Shot Approach](https://www.youtube.com/watch?v=12v5S1n1eOY&t=115s)
**Timestamp: 01:55**

- Initial approach: OCR preprocessing + standard AI calls with decorated prompts
- Generic off-the-shelf models outperformed specialized ML models
- Worked amazingly well at first - flexible across any data type
- Team was thrilled with this "new generation of AI"

**Key Points:**
- Single-shot extraction worked well for simple cases
- Multi-vendor model support for redundancy
- Performance continuously improved as models evolved

### [Hitting the Wall - Complex Document Challenges](https://www.youtube.com/watch?v=12v5S1n1eOY&t=395s)
**Timestamp: 06:35**

Customer requests escalated in complexity:
- 300-page lease documents with 300+ fields
- Complex digital assets with intricate questions
- Risk assessments and complex field types
- AI struggled just like humans would with overwhelming complexity

**Problems encountered:**
- OCR proved to be a hard problem (scanned docs, handwriting, crossouts)
- Different file formats (PDFs) posed challenges
- Multilingual support was difficult
- AI had clear attention limits with many fields simultaneously
- 100-page documents with 100 complex fields: AI lost track

### [The Despair Moment](https://www.youtube.com/watch?v=12v5S1n1eOY&t=537s)
**Timestamp: 08:57**

- Team thought LLMs would solve everything, but hit limitations
- Accuracy became problematic for enterprise settings
- LLMs don't provide confidence scores like traditional ML models
- "LLM as a judge" could only tell them something was wrong, not fix it
- Customers wanted solutions, not just problem identification
- Considered waiting for next model versions, but architecture fragility was the real issue

**Key challenges:**
- Speed requirements
- Affordability concerns
- Enterprise-grade accuracy demands

### [The Agentic Solution](https://www.youtube.com/watch?v=12v5S1n1eOY&t=561s)
**Timestamp: 09:21**

Definition of their AI agent:
- Instructions and objectives with model
- Background context
- Secure tool access
- Memory for advancing and information lookup
- Full directed graph for orchestration
- Either AI-generated plans or predetermined orchestration

**Initial resistance:**
- Engineers suggested: better OCR, post-processing regex checks, fine-tuning ML models
- Concern about losing the genericness of the solution
- Not obvious that agentic approaches would solve data extraction problems

### [Agentic Architecture Implementation](https://www.youtube.com/watch?v=12v5S1n1eOY&t=648s)
**Timestamp: 10:48**

Implemented LangGraph-style agentic capabilities:

**Multi-step process:**
1. **Field Preparation** - Intelligently group related fields (e.g., parties + addresses together)
2. **Multiple Queries** - Break complex documents into manageable chunks
3. **Tool-based Checking** - Double-check results using multiple methods:
   - OCR verification
   - Visual inspection of page images
   - Multi-model voting (consensus from different vendors)
4. **LLM as Judge** - Not just for validation, but for iterative improvement with feedback

**Key insight:** Takes longer but achieves enterprise-grade accuracy

### [Benefits of Agentic Approach](https://www.youtube.com/watch?v=12v5S1n1eOY&t=734s)
**Timestamp: 12:14**

- **Iterative improvement:** Instead of rethinking everything, just adjust prompts or add nodes
- **Easy evolution:** Example - sloppy output fixed by adding summarization node at the end
- **Clean abstraction:** Natural to think in terms of intelligent workflows
- **Enabled advanced features:** Deep research capabilities on enterprise content
- **Platform benefits:** Customers can build their own agentic solutions

**Example - Deep Research Feature:**
- Similar to OpenAI/Gemini deep research, but on enterprise data in Box
- Multi-step directed graph: search → relevance check → outline → plan → process
- Would not have been possible without agentic foundation

### [Platform Evolution](https://www.youtube.com/watch?v=12v5S1n1eOY&t=929s)
**Timestamp: 15:29**

**Team transformation:**
- Need to shift team thinking to "agentic-first" and "AI-first"
- Let engineers build to understand the paradigm
- Platform customers can leverage same agentic capabilities

**Platform features:**
- Published MCP servers
- Agent-to-agent communications
- API-first approach with agent APIs

### [Lessons Learned](https://www.youtube.com/watch?v=12v5S1n1eOY&t=846s)
**Timestamp: 14:06**

1. **Agentic abstraction is clean** - Natural way to think about intelligent workflows
2. **Separate concerns** - Keep agentic framework separate from distributed system scaling
3. **Easy to evolve** - Add nodes, adjust prompts without full redesigns
4. **Build it early** - If AI models can plausibly help, build agentic architecture from the start
5. **Looking back** - Would have adopted agentic approach sooner to take continuous advantage

**Key recommendation:** If it's plausible that AI models could help solve your problem, build the agentic architecture early - don't wait.

### [Q&A Highlights](https://www.youtube.com/watch?v=12v5S1n1eOY&t=996s)
**Timestamp: 16:36**

**API Availability:**
- Very API-first oriented
- Agent APIs available to call agents and provide arguments
- Tools provided to call Box APIs

**Evaluation Approach:**
- Standard eval sets
- Challenge sets for difficult edge cases
- LLM as a judge
- Customer feedback loops
- Limited visibility into enterprise usage but collect feedback

**Fine-tuning vs. Agents:**
- Actively avoiding fine-tuning currently
- Challenges: must fine-tune each model version evolution
- Support multiple vendors (Gemini, Llama, OpenAI, Anthropic)
- Hard to consistently fine-tune across vendors
- Next model versions typically solve previous problems
- Prefer: prompts, cached prompts, and agenticness over fine-tuning
- Approach works well for their use cases

---

## Technical Architecture Insights

**Agentic Pipeline Components:**
- Field grouping and preparation
- Intelligent document chunking
- Multi-model consensus voting
- OCR + visual verification
- Iterative feedback loops
- LLM-as-judge for quality control

**Architecture Principles:**
- Separation of agentic logic from scaling infrastructure
- Directed acyclic graphs for workflow orchestration
- Multiple vendor model support
- API-first design philosophy

---

## Key Takeaways

1. **Single-shot AI is insufficient** for complex enterprise use cases
2. **Agentic architecture provides resilience** through multi-step verification and iteration
3. **Early adoption is crucial** - don't wait until hitting limitations
4. **Clean separation of concerns** - agentic logic vs. distributed systems
5. **Avoid premature fine-tuning** - generic models with good prompts and agentic flows often suffice
6. **Platform thinking** - build capabilities that both internal teams and customers can leverage

---

**Video Duration:** ~19 minutes
**Speaker:** Ben Kus, CTO of Box
**Event:** AI Engineer Conference
**Date:** 2024 (based on context references to 2023 start)
