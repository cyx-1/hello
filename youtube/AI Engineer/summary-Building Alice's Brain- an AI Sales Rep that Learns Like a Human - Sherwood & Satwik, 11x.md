# Building Alice's Brain: an AI Sales Rep that Learns Like a Human - Sherwood & Satwik, 11x

**Video URL:** https://www.youtube.com/watch?v=KWmkMV0FNwQ

---

## Executive Summary

This talk from 11x discusses how they built Alice, an AI Sales Development Representative (SDR) that sends 50,000 personalized emails daily across 300 business organizations. The presenters explain their evolution from a manual "library" system where sellers had to input product details manually, to an automated "knowledge base" system where Alice proactively learns about the seller's business through document ingestion. The talk covers their RAG (Retrieval Augmented Generation) pipeline architecture, including parsing strategies for different content types (documents, websites, media), vendor selection, chunking approaches, and quality assurance systems. Key technical details include using Pinecone for vector storage, Anthropic's Claude for LLM operations, and various parsing vendors for different content types.

---

## Topics with Timestamps

### [Introduction and What is an SDR](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=18s)
- **Time:** 00:18 - 02:00
- Definition of Sales Development Representative (SDR) role
- Three core responsibilities: sourcing leads, contacting them, and booking meetings
- Alice sends 50,000 emails/day vs. human SDRs sending 20-50
- Running campaigns for ~300 business organizations
- Key metrics: positive replies and meetings booked

**Key Points:**
- SDR is entry-level sales role focused on lead generation
- Alice's scale: 1,000x more emails than human SDRs
- Two main requirements: knowing the seller's business and knowing the leads

### [The Old Manual Library System](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=189s)
- **Time:** 03:09 - 04:49
- Sellers had to manually push context about their business to Alice
- Library interface required detailed descriptions of products, offers, pain points, and value props
- During campaign creation, users selected which offers Alice could access
- Three major problems: extremely tedious, created onboarding friction, generated sub-optimal emails

**Key Points:**
- Manual data entry was cumbersome and time-consuming
- Users had to choose between too few offers (irrelevant) or too many (diluted context)
- Created barriers to running campaigns quickly

### [The Knowledge Base Solution](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=289s)
- **Time:** 04:49 - 06:36
- Flipped the model: Alice proactively pulls context instead of sellers pushing it
- Mimics human SDR training where documents are provided for self-learning
- Centralized repository for seller information
- Three content categories: documents/images, websites, and media (audio/video)

**Key Points:**
- Knowledge base acts as Alice's "brain" - a learning system similar to human onboarding
- Resources include marketing materials, case studies, sales calls, press releases
- Eliminates manual data entry burden on sellers

### [Architecture Overview](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=398s)
- **Time:** 06:38 - 08:00
- User uploads resource → saved to S3 → backend creates DB records
- Jobs kicked off based on resource type and vendor selected
- Vendors asynchronously parse content and send webhook
- Parsed artifacts stored in DB and upserted to Pinecone (vector DB)
- Embeddings created for retrieval
- Agent queries Pinecone during message generation

**Key Points:**
- Asynchronous processing pipeline with vendor integration
- Dual storage: relational DB for metadata, Pinecone for semantic search
- Webhook-based architecture for vendor communication

### [Step 1: Parsing - Documents and Images](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=506s)
- **Time:** 08:26 - 11:00
- Goal: Convert unstructured data into structured markdown
- Vendors tested: Unstructured.io, LlamaParse, Docling, Azure Document Intelligence
- Final choice: Docling for documents, Azure for forms
- Docling advantages: open source, good at tables, extractable bounding boxes
- Azure advantages: excellent OCR for handwritten text and forms

**Key Points:**
- Quality benchmarking across multiple vendors
- Docling chosen for most documents due to table handling and bounding box extraction
- Azure specifically for OCR-heavy use cases
- Bounding box metadata useful for future highlighting features

### [Step 1: Parsing - Websites](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=710s)
- **Time:** 11:50 - 13:20
- Challenge: Websites are dynamic, not static documents
- Two approaches: crawling (BFS traversal) vs. sitemap parsing
- Final choice: Firecrawl for crawling
- Discovered most websites don't have usable sitemaps
- Fallback: screenshot entire page and use vision model (Anthropic Claude) to extract text

**Key Points:**
- Crawling more reliable than sitemap parsing in practice
- Vision models as fallback for difficult-to-parse pages
- Firecrawl chosen for its crawling capabilities

### [Step 1: Parsing - Media (Audio/Video)](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=822s)
- **Time:** 13:42 - 14:30
- Process: Transcribe audio → summarize transcript → chunk summaries
- Vendors: Assembly AI, Deepgram (both very good)
- Final choice: Assembly AI (better pricing)
- Post-processing: Remove disfluencies (ums, ahs), generate summary with Claude
- Chunking done on summarized content for efficiency

**Key Points:**
- Transcription quality similar between top vendors
- Pricing was deciding factor
- Summary generation improves retrieval quality
- Removes conversational artifacts for cleaner content

### [Step 2: Chunking Strategy](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=877s)
- **Time:** 14:37 - 17:00
- Approaches tested: Semantic chunking, fixed-size chunking
- Final choice: Agentic chunking (LLM-based)
- Agentic chunking: Identify propositions, group related ones, generate summaries
- Results: 3-6 chunks per page vs. 200+ with fixed-size
- Benefits: Better retrieval, fewer hallucinations, more accurate citations

**Key Points:**
- Agentic chunking dramatically reduces chunk count
- Each chunk gets its own summary for better retrieval
- Proposition-based approach groups related content logically
- Improved accuracy in citing sources

### [Step 3: Retrieval and Reranking](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=1046s)
- **Time:** 17:26 - 19:30
- Two-stage process: vector search + reranking
- Vector DB: Pinecone (chosen for managed infrastructure)
- Embeddings: Voyage AI (text-embedding-3 model)
- Reranking: Cohere
- Query expansion for better recall
- Metadata filtering (source, date, etc.)
- Returns top 5 reranked chunks

**Key Points:**
- Pinecone for managed vector storage at scale
- Voyage AI embeddings for semantic similarity
- Cohere reranking improves precision
- Query expansion broadens search coverage
- Metadata filtering for targeted retrieval

### [Quality Assurance System](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=1193s)
- **Time:** 19:53 - 21:30
- Three-tier approach: golden dataset, LLM as judge, human evaluation
- Golden dataset: Expert-curated question-answer pairs with source citations
- LLM judge: Evaluates retrieval quality (relevance, completeness)
- Human evaluation: Continuous spot-checking and feedback
- Metrics tracked: retrieval precision, answer accuracy, citation correctness

**Key Points:**
- Multi-layered evaluation strategy
- Golden dataset provides ground truth
- LLM judge scales evaluation
- Human oversight ensures quality standards
- Continuous improvement through feedback loops

### [User Experience and Demo](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=1297s)
- **Time:** 21:37 - 24:00
- Upload interface supports drag-and-drop
- Progress tracking for parsing jobs
- Preview of parsed content
- Chat interface to query knowledge base
- Alice automatically retrieves relevant context during email generation
- Shows source attribution in emails

**Key Points:**
- Simple upload experience (drag and drop)
- Real-time status updates during processing
- Chat interface for testing retrieval
- Transparent source attribution
- Seamless integration with email generation

### [Results and Impact](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=1463s)
- **Time:** 24:23 - 25:30
- Eliminated onboarding friction
- Users can start campaigns immediately after uploading documents
- Better email personalization
- Higher engagement rates
- Reduced manual configuration time from hours to minutes

**Key Points:**
- Dramatically improved time-to-value
- Better email quality through comprehensive context
- Sellers can iterate faster on campaigns
- Knowledge base continuously improves as more content is added

### [Lessons Learned](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=1534s)
- **Time:** 25:34 - 27:00
- Start simple: MVP with basic parsing before optimizing
- Vendor evaluation crucial: Test multiple options with real data
- Quality over quantity: Fewer, better chunks beat many mediocre ones
- User feedback essential: Iterate based on actual usage patterns
- Observability matters: Track metrics at every pipeline stage

**Key Points:**
- Iterative approach paid off
- Real-world testing revealed vendor strengths/weaknesses
- Chunking quality has outsized impact on retrieval
- Build instrumentation from day one
- User behavior guides optimization priorities

### [Future Plans](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=1623s)
- **Time:** 27:03 - 28:30
- Continuous learning: Alice learns from successful/unsuccessful emails
- Multi-modal expansion: Better image and video understanding
- Personalization: Adapt knowledge base per campaign or lead segment
- Active learning: Alice asks clarifying questions when context is ambiguous
- Integration expansion: CRM, sales call recordings, customer feedback

**Key Points:**
- Reinforcement learning from email performance
- Expanding beyond text to rich media
- Campaign-specific knowledge customization
- Interactive learning through questions
- Deeper integration with sales stack

### [Q&A Highlights](https://www.youtube.com/watch?v=KWmkMV0FNwQ&t=1710s)
- **Time:** 28:30 - 31:00
- Question about hallucinations: Addressed through source attribution and reranking
- Question about cost: Parsing is one-time cost, retrieval very cheap at scale
- Question about latency: Async processing means no impact on email generation
- Question about multilingual: Currently English-focused, expanding to other languages

**Key Points:**
- Hallucination mitigation through grounding and attribution
- Economics work at scale due to one-time parsing
- Architecture decouples parsing from generation
- Language expansion on roadmap

---

## Technical Stack Summary

- **LLM:** Anthropic Claude (Sonnet and Opus)
- **Vector Database:** Pinecone
- **Embeddings:** Voyage AI (text-embedding-3)
- **Reranking:** Cohere
- **Document Parsing:** Docling (primary), Azure Document Intelligence (forms/OCR)
- **Website Crawling:** Firecrawl
- **Transcription:** Assembly AI
- **Storage:** S3 (files), PostgreSQL (metadata)
- **Infrastructure:** Webhook-based async processing

---

**Last Updated:** January 2, 2026
