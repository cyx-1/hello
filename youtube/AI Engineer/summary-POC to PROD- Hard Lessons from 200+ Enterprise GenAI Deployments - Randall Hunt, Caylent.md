# POC to PROD: Hard Lessons from 200+ Enterprise GenAI Deployments - Randall Hunt, Caylent

**Video URL:** https://www.youtube.com/watch?v=vW8wLsb3Nnc

---

## Executive Summary

Randall Hunt, from Caylent, shares practical lessons learned from over 200 enterprise GenAI deployments. The talk challenges common misconceptions about GenAI being a magical solution and emphasizes that successful production deployments require much more than just throwing AI at problems. Key themes include the critical importance of evaluations (evals), understanding your specific use case inputs/outputs, knowing your end users, avoiding unnecessary complexity, and managing economics. Hunt advocates for prompt engineering over fine-tuning with modern models, emphasizes UX as a critical component for managing slower inference times, and stresses that context management is a key differentiator. The presentation covers real-world examples from industries ranging from building management to sports footage analysis.

---

## Main Topics

### [1. Introduction and Company Overview](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=0s)
- **[00:16](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=16s)** - Caylent builds solutions for customers from Fortune 500 to startups
- **[00:48](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=48s)** - GenAI is not the magical pill many think it is
- **[01:12](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=72s)** - Customer example: BrainBox AI for HVAC building management and decarbonization
- **[01:43](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=103s)** - Customer example: Simmons for water management conservation

### [2. Demo: Multimodal Video Search](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=117s)
- **[01:57](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=117s)** - Interest in multimodal search and semantic understanding of videos
- **[02:03](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=123s)** - Nature Footage customer: indexing stock footage of wildlife
- **[02:22](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=142s)** - Leveraging Nova Pro models for video understanding and timestamps
- **[02:33](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=153s)** - Building pooling embeddings from frame samples
- **[02:44](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=164s)** - Using Titan v2 multimodal embeddings for text-to-image search
- **[02:59](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=179s)** - Sports footage processing architecture (March Madness example)

### [3. Sports Video Processing Architecture](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=189s)
- **[03:09](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=189s)** - Processing both real-time and batch archival sports footage
- **[03:14](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=194s)** - Pro tip: Use ffmpeg amplitude spectrograph to find highlights by detecting audience cheering
- **[03:26](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=206s)** - Generating embeddings from both text (transcription) and video
- **[03:57](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=237s)** - Small annotations dramatically improve video understanding models
- **[04:19](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=259s)** - Example: Annotating three-point line with blue line improves model performance
- **[04:32](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=272s)** - Using SAM 2 (Meta) for automated annotations

### [4. Speaker Background and Technology Stack](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=290s)
- **[04:54](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=294s)** - Randall's background: hacking video games, NASA, MongoDB (10gen), SpaceX CI/CD
- **[05:32](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=332s)** - Made video about transformer paper in July 2017
- **[05:50](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=350s)** - Caylent: AWS Partner of the Year, building chatbots to copilots to AI agents

### [5. Three Categories of AI Applications](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=373s)
- **[06:13](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=373s)** - Self-service productivity tools (can typically be bought, may need fine-tuning)
- **[06:30](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=390s)** - Tracking usage of third-party tools and APIs
- **[06:49](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=409s)** - Recommendation: Shure Path for network interception and PII/PHI detection
- **[06:59](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=419s)** - Automating business functions (getting time/dollars back end-to-end)
- **[07:09](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=429s)** - Example: Large logistics customer processing receipts and bills of lading
- **[07:18](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=438s)** - Intelligent document processing with custom classifier before GenAI
- **[07:31](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=451s)** - Monetization: Adding new SKU to existing SaaS product
- **[07:49](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=469s)** - Warning: Just building a chatbot is not enough (Polaroid/Kodak analogy)

### [6. Fundamental Architecture: Building Your Moat](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=482s)
- **[08:05](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=485s)** - Slide adapted from Twitter (possibly Jason Liu or DSPy community)
- **[08:19](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=499s)** - Most fundamental: Define your inputs and outputs clearly
- **[08:47](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=527s)** - "Developers, developers, developers" → "Evals, evals, evals!"
- **[08:54](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=534s)** - Eval layer proves system is robust, not just a vibe check
- **[09:03](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=543s)** - System architecture, LLMs, and tools are incidental and will evolve
- **[09:13](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=553s)** - What won't change: your fundamental inputs/outputs definition

### [7. AWS Technology Stack for GenAI](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=572s)
- **[09:34](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=574s)** - Bottom layer: Bedrock and SageMaker
- **[09:41](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=581s)** - SageMaker comes with compute premium; can also use EKS or EC2
- **[09:50](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=590s)** - Custom silicon: Trainium and Inferentia (~60% price/performance improvement over Nvidia)
- **[09:59](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=599s)** - Downside: Less HBM RAM than H200
- **[10:04](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=604s)** - News: Amazon reduced P4/P5 instance prices by up to 40%
- **[10:18](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=618s)** - Must use Neuron SDK (similar to XLA for TPUs)
- **[10:34](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=634s)** - Model layer: Claude, Nova, Llama, DeepSeek, open source models
- **[10:46](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=646s)** - Vector stores: Preference for Postgres with pgvector

### [8. Database and Vector Store Selection](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=649s)
- **[10:54](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=654s)** - MemoryDB on AWS for persistent Redis with vector search
- **[11:00](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=660s)** - Redis vector search: Extremely fast but extremely expensive (RAM-based)
- **[11:07](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=667s)** - IVF flat indexes blow up RAM usage
- **[11:16](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=676s)** - Postgres and OpenSearch: Can use disk with HNSW indexes for better allocation
- **[11:24](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=684s)** - Prompt versioning/management is incidental and not unique
- **[11:34](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=694s)** - **Context management is incredibly important and a key differentiator**
- **[11:44](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=704s)** - Context about user, page, browsing history enables strategic inference

### [9. Key Lessons Learned](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=722s)
- **[12:10](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=730s)** - **Lesson 1: Evals and embeddings are not all you need**
- **[12:17](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=737s)** - Understanding access patterns and user behavior matters more
- **[12:25](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=745s)** - Embeddings alone don't make a great query system
- **[12:29](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=749s)** - Need faceted search and filters on top of embeddings
- **[12:36](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=756s)** - **Lesson 2: Speed matters**
- **[12:43](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=763s)** - UX can mitigate slowness of inference
- **[12:47](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=767s)** - Can use caching and other techniques
- **[12:54](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=774s)** - Slower + more expensive = won't be used
- **[12:57](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=777s)** - Slower + cheaper with good UX (spinners, etc.) can still win
- **[13:09](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=789s)** - **Lesson 3: Know your end customer**

### [10. Anti-Pattern: Unnecessary Tool Use](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=796s)
- **[13:16](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=796s)** - Stop defining tools for simple things like "get current date"
- **[13:22](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=802s)** - Just use `import time.now` and format string in prompt
- **[13:28](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=808s)** - You control the prompt - use it!
- **[13:36](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=816s)** - Downside: Putting dynamic info high in prompt hurts caching
- **[13:41](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=821s)** - Solution: Put dynamic info at bottom after instructions for effective caching

### [11. Prompt Engineering vs Fine-Tuning](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=831s)
- **[13:51](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=831s)** - "I used to say we should fine-tune... turns out I was wrong"
- **[13:56](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=836s)** - **Prompt engineering has proven unreasonably effective**
- **[14:06](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=846s)** - Claude 3.5 to 3.7: Some regressions observed
- **[14:18](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=858s)** - Claude 3.7 to 4: Zero regressions across all use cases
- **[14:21](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=861s)** - Faster, better, cheaper, more optimized - drop-in replacement
- **[14:31](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=871s)** - Hope: Era of adjusting prompts for each new model is ending
- **[14:39](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=879s)** - **Lesson 4: Know your economics**
- **[14:41](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=881s)** - Will this inference bankrupt my company?
- **[14:47](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=887s)** - Opus models may not always be the best choice cost-wise

### [12. Building Effective Evaluations](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=893s)
- **[14:55](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=895s)** - Slide from Anthropic on creating evals
- **[15:01](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=901s)** - Vibe check is your first eval
- **[15:12](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=912s)** - Change data and inputs to build eval set
- **[15:16](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=916s)** - 20 minutes later, you have basic evals running
- **[15:22](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=922s)** - Metrics don't need to be BERT scores or benchmarks
- **[15:29](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=929s)** - **Boolean true/false (success/failure) is often easier and sufficient**
- **[15:39](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=939s)** - Just iterate and keep going
- **[15:43](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=943s)** - Speed matters, but UX matters more

### [13. Generative UI Case Study](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=953s)
- **[15:56](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=956s)** - CloudZero customer: Chat with AWS infrastructure for cost optimization
- **[16:03](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=963s)** - Using generative UI to render information in charts
- **[16:11](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=971s)** - Just-in-time crafting of React components injected into response
- **[16:20](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=980s)** - Caching components and describing them in prompt for reuse
- **[16:30](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=990s)** - Generative UI allows tool to constantly evolve and personalize
- **[16:37](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=997s)** - **Extremely powerful paradigm, finally fast enough with modern models**

### [14. Know Your End User Examples](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1006s)
- **[16:50](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1010s)** - Customer with users in remote areas (low connectivity)
- **[17:00](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1020s)** - Problem: 200 MB PDF downloads in low-bandwidth areas
- **[17:06](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1026s)** - Solution: Send text summary + screenshot of relevant PDF page only
- **[17:13](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1033s)** - Server-side processing reduces bandwidth requirements
- **[17:22](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1042s)** - Hospital system: Built voice bot for nurses
- **[17:27](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1047s)** - **Nurses hated voice bots**: Hospitals are loud and noisy
- **[17:30](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1050s)** - Voice transcription poor in noisy environments
- **[17:35](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1055s)** - Switched to regular chat interface based on user feedback

### [15. Let Computers Do What They're Good At](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1062s)
- **[17:43](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1063s)** - **Don't do math in an LLM**
- **[17:46](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1066s)** - Most expensive possible way of doing math
- **[17:52](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1072s)** - Let the computer do calculations traditionally
- **[17:54](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1074s)** - Prompt engineering best practices (won't detail - covered elsewhere)

### [16. Economic Optimization Strategies](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1096s)
- **[18:08](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1088s)** - Think about output tokens and associated costs
- **[18:12](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1092s)** - Optimize for better performance
- **[18:17](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1097s)** - Prompt caching as cost optimization tool
- **[18:19](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1099s)** - Tool usage optimization
- **[18:22](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1102s)** - **Batch on Bedrock: 50% off across the board**
- **[18:28](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1108s)** - **Context management and optimization**
- **[18:31](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1111s)** - Figure out minimum viable context for correct inference
- **[18:35](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1115s)** - Optimize context over time
- **[18:40](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1120s)** - Inject relevant information, remove irrelevant information
- **[18:44](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1124s)** - Give model less to reason over for efficiency

### [17. Conclusion and Call to Action](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1132s)
- **[18:54](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1134s)** - Happy to hop on phone with customers
- **[18:56](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1136s)** - QR code available for contact
- **[18:58](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1138s)** - Team of talented engineers excited to build
- **[19:05](https://www.youtube.com/watch?v=vW8wLsb3Nnc&t=1145s)** - Looking for super cool use cases

---

## Key Takeaways

1. **Evals are Everything**: The eval layer is the most critical component - it proves your system works beyond just "vibe checks"

2. **Define Inputs/Outputs First**: Your fundamental input/output specification is your moat - everything else (models, architecture) is incidental and will evolve

3. **Prompt Engineering > Fine-Tuning**: Modern models (especially Claude 3.7 to 4.0) have made prompt engineering unreasonably effective, often eliminating the need for fine-tuning

4. **Context is King**: Context management is the key differentiator between competitors - knowing your user, their page, browsing history enables strategic inference

5. **Know Your End User**: Understanding user environment and constraints (remote areas, noisy hospitals) is critical for design decisions

6. **Don't Over-Engineer Tools**: Stop creating tools for simple operations like "get current date" - just use the prompt directly

7. **Speed + UX Matter**: If you're slower, UX (spinners, generative UI) can mitigate the impact; being slow AND expensive means you won't be used

8. **Economic Optimization**: Use batch processing (50% discount), prompt caching, context optimization, and choose appropriate model tiers

9. **Let Computers Be Computers**: Don't do math in LLMs - it's the most expensive way to calculate

10. **Minimum Viable Context**: Optimize context to include only what's necessary for correct inference, reducing both cost and latency

11. **Evals Can Be Simple**: Boolean success/failure metrics are often easier and more practical than complex scoring systems

12. **Video Understanding Hacks**: Simple annotations (like marking court lines) dramatically improve model performance; use audio amplitude to find highlights

---

**Last Updated:** 2026-01-03
