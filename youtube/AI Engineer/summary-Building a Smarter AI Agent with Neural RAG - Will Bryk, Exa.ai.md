# Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai

**Video URL:** https://www.youtube.com/watch?v=xnXqpUW_Kp8

---

## Executive Summary

Will Bryk from Exa.ai presents the story of building a neural search engine specifically designed for AI agents rather than humans. He explains how traditional search engines like Google were optimized for human users typing simple keyword queries, but AI systems have fundamentally different needs: they can process complex multi-paragraph queries, handle thousands of results simultaneously, and require precise controllable information. Exa.ai has spent four years developing a search engine that uses transformer-based embeddings instead of keyword matching, enabling semantic understanding of queries. The talk covers the technical evolution from Google's PageRank (1998) to neural search (2021-present), why LLMs will always need external search, and demonstrates how to build AI agents that combine neural and keyword search strategies to retrieve information from the web.

---

## Main Topics

### 1. The Evolution of Search: From PageRank to Neural Search
[https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=0s](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=0s)

**Key Points:**
- **[00:44](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=44s)** - Google's 1998 innovation: PageRank algorithm that ranked results by authority based on web graph structure
- **[01:22](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=82s)** - Fast forward to 2021: GPT-3 could understand complex paragraph-long inputs, but Google still failed on simple queries like "shirts without stripes"
- **[01:58](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=118s)** - Google's keyword comparison algorithm doesn't understand negation (the word "without")
- **[02:03](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=123s)** - Decision to devote 10+ years to building a search engine combining GPT-3 technology with search

### 2. Building Exa: The Neural Search Engine
[https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=140s](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=140s)

**Key Points:**
- **[02:33](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=153s)** - Joined Y Combinator Summer 2021, raised funding, spent half on GPU cluster (joking about YC advice)
- **[02:50](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=170s)** - Spent 1.5 years doing research without talking to customers (normally not recommended, but necessary for fundamental research)
- **[03:02](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=182s)** - Core idea: Apply next-token prediction transformers to search instead of keyword matching
- **[03:28](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=208s)** - Traditional search creates keyword index mapping words to documents
- **[04:04](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=244s)** - Neural approach: Convert documents into embeddings instead of keywords
- **[04:15](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=255s)** - Embeddings capture meaning, ideas, and how people refer to documents—not just keywords
- **[04:32](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=272s)** - Embeddings are arbitrarily powerful and will eventually destroy keyword-based search
- **[05:03](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=303s)** - Launched November 2022 with neural search that actually understands complex queries

### 3. Why LLMs Always Need Search
[https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=332s](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=332s)

**Key Points:**
- **[05:32](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=332s)** - ChatGPT launched 2 weeks after Exa, raising questions about search's role
- **[06:06](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=366s)** - LLMs don't know everything on the web—there's not enough information in the weights
- **[06:21](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=381s)** - Simple information theory argument: GPT-4 has ~few trillion parameters (<10 TB), but the web is >1 million TB
- **[06:48](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=408s)** - The web is in the exabyte range (hence the name "Exa")
- **[07:05](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=425s)** - The web constantly updates, making it impossible to store in model weights
- **[07:10](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=430s)** - LLMs will always need search for accessing web information

### 4. AI Search vs. Human Search: Fundamental Differences
[https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=441s](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=441s)

**Key Points:**
- **[07:41](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=461s)** - Traditional search engines were built for humans, not AI
- **[07:59](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=479s)** - Humans are "slow flesh creatures" typing keywords, wanting to read a few links, caring about UI
- **[08:14](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=494s)** - AIs can "gobble up information" extremely fast
- **[08:26](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=506s)** - AIs want complex queries, tons of knowledge, not just a couple of links
- **[08:43](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=523s)** - The optimal search algorithm for AI is fundamentally different from what's optimal for humans

**Three Key Differences:**

**A. Precise Controllable Information**
- **[09:11](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=551s)** - AIs want search engines that return exactly what they ask for, not what Google predicts they'll click
- **[09:42](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=582s)** - Example: Asking for "startups like Bell Labs" should return a list of startups, not articles about Bell Labs
- **[09:59](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=599s)** - AI agents will make tons of searches with precise criteria (NYC, specific qualities, etc.)

**B. Search with Lots of Context**
- **[10:20](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=620s)** - AI assistants accumulate context about users throughout conversations
- **[10:33](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=633s)** - Should be able to search with multi-paragraph context about user preferences
- **[10:47](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=647s)** - Google was optimized for simple keyword queries, not paragraph-long context
- **[10:56](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=656s)** - Google has a few dozen keyword limit; Exa can handle multiple paragraphs

**C. Comprehensive Knowledge**
- **[11:05](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=665s)** - Humans can't process 10,000 links (would take 10 days), but AI can do it in 3 seconds if parallelized
- **[11:20](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=680s)** - VCs want literally ALL companies in a space, not just 10-20 that Google finds
- **[11:35](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=695s)** - Need search engines that can return 1,000 or 10,000 results with semantic understanding
- **[11:42](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=702s)** - Google literally can't do this at all

### 5. The Expanding Query Space
[https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=708s](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=708s)

**Key Points:**
- **[11:50](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=710s)** - The space of possible queries is way larger than people realize
- **[12:07](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=727s)** - Pre-2022: Basic keyword queries (stripe pricing, GitHub pages, Taylor Swift's boyfriend)
- **[12:22](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=742s)** - Post-ChatGPT: New query types like "explain this concept like I'm 5" or "debug my code"
- **[12:41](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=761s)** - Semantic queries: "people in San Francisco who know assembly" (Exa introduced this)
- **[12:51](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=771s)** - Super complex queries: "find every article that argues X and not Y from author like Z"
- **[13:02](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=782s)** - Turns the web into a database you can filter however you want
- **[13:15](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=795s)** - Every week, new types of queries emerge that no search engine could do before

### 6. Exa's Vision: One API for Any Web Information
[https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=813s](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=813s)

**Key Points:**
- **[13:36](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=816s)** - Goal: One API to get any information from the web
- **[13:45](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=825s)** - Handle keyword queries, semantic queries, super complex queries, and eventually all queries
- **[13:53](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=833s)** - Give AI systems whatever knowledge they want through a single interface

### 7. Live Demo: Building AI Agents with Exa
[https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=842s](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=842s)

**Key Points:**
- **[14:33](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=873s)** - Exa search dashboard allows testing different queries
- **[14:42](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=882s)** - Exposes many toggles/filters for full control: number of results (10/100/1000), date ranges, domain filters
- **[15:02](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=902s)** - Multiple toggles are a feature, not a bug—AIs want full control
- **[15:09](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=909s)** - Supports both neural and keyword search modes

**Demo 1: Mark the Markdown Agent**
- **[15:21](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=921s)** - Created agent "Mark" that converts anything into markdown
- **[15:39](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=939s)** - Neural query: "personal site of engineer in San Francisco who likes information retrieval"
- **[16:01](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=961s)** - Agent makes query and outputs markdown list

**Demo 2: Keyword Search for GitHub**
- **[16:32](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=992s)** - Switch to keyword search for traditional Google-like queries
- **[16:42](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1002s)** - Example: Getting information from Will Bryk's GitHub using keyword search

**Demo 3: Hybrid Agent (Neural + Keyword)**
- **[17:00](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1020s)** - Real agents combine multiple search types
- **[17:30](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1050s)** - One-shot prompt with GPT-3 to create hybrid GitHub agent
- **[17:39](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1059s)** - Strategy: First neural search to find engineers in SF interested in information retrieval, then keyword search for each person's GitHub
- **[17:47](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1067s)** - Can scale to 100 or 1000 results on enterprise plans
- **[18:10](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1090s)** - Demo successfully retrieves GitHub information for multiple engineers

### 8. New Research Endpoint
[https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1096s](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1096s)

**Key Points:**
- **[18:16](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1096s)** - Just launched today: Research endpoint
- **[18:21](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1101s)** - Performs multiple searches and LLM calls in the background
- **[18:25](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1105s)** - Returns perfect reports or structured outputs automatically
- **[18:29](https://www.youtube.com/watch?v=xnXqpUW_Kp8&t=1109s)** - State-of-the-art deep research API

---

## Key Takeaways

1. **Traditional search was built for humans, not AI** - Google optimizes for what humans will click, not what AI agents need
2. **Neural search understands meaning, not just keywords** - Embeddings capture ideas and semantic relationships
3. **LLMs will always need external search** - Simple information theory: the web (exabytes) is far larger than model weights (terabytes)
4. **AI agents have fundamentally different needs**: complex queries, massive context, comprehensive results (1000s of links)
5. **The future is hybrid search** - Combining neural and keyword search strategies based on query type
6. **The query space is exploding** - Post-ChatGPT, we're discovering entirely new types of queries weekly
7. **Give AI full control** - Search APIs for AI should expose maximum configurability, not simplified interfaces

---

**Last Updated:** January 2, 2026
