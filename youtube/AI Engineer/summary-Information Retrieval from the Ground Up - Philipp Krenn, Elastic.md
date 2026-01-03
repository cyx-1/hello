# Information Retrieval from the Ground Up - Philipp Krenn, Elastic

**Video URL:** https://www.youtube.com/watch?v=4Xe_iMYxBQc

---

## Executive Summary

This is a comprehensive 1 hour 48 minute workshop on information retrieval and RAG (Retrieval Augmented Generation) systems, presented by Philipp Krenn from Elastic at an AI Engineer conference. The talk focuses primarily on the "R" (Retrieval) component of RAG, covering everything from classic keyword search to modern dense vector embeddings. The speaker provides hands-on demonstrations using Elasticsearch with Star Wars examples, explaining the fundamental concepts, trade-offs, and practical implementation of various retrieval methods. Key message: vector search alone is insufficient - hybrid approaches combining lexical and semantic search deliver the best results.

---

## Topics & Timestamps

### 1. [Introduction & Keyword/Lexical Search Fundamentals](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=0s) (00:00 - 15:00)

**Key Points:**
- RAG overview - focus on the Retrieval component only, not generation
- [Retrieval is 50-70 years old](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=90s), not a new concept despite current hype
- Keyword search vs vector search - **both are needed**, not either/or
- [Text analysis pipeline](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=420s): tokenization, lowercasing, stop word removal, stemming
- Example: "These are not the droids you're looking for" → tokens: "droid", "you", "look"
- Language-specific analyzers (English, German, French examples)
- [Tokenization walkthrough](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=420s) showing position tracking and offset storage for highlighting
- Importance of proper language detection - wrong analyzer = garbage results

**Quote:** *"Vector search is a feature of retrieval, only one of multiple features"*

---

### 2. [Analysis Customization & Advanced Text Processing](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=900s) (15:00 - 30:00)

**Key Points:**
- [Stop words debate](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=900s) - should you always remove them? Answer: **"It depends"**
- "To be or not to be" would be completely removed as all stop words
- Custom analyzers: HTML stripping, standard tokenizer, lowercase filter, snowball stemmer
- [Phrase search](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=1200s) and the "slop" parameter for fuzzy phrase matching
- N-grams and edge n-grams for partial matching
- [Compound nouns challenge](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=1680s) (German, Korean) - "Blackberry" example
- Blackberry stemming demonstration showing rule-based vs dictionary-based approaches
- Default English stop words: ~33 words

---

### 3. [Scoring & Relevance (BM25 Algorithm)](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=2280s) (38:00 - 47:00)

**Key Points:**
- [BM25 (Best Match 25th iteration)](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=2280s) vs classic TF-IDF
- **Three main components:**
  1. **Term Frequency (TF):** square root scaling to prevent one term from dominating
  2. **Inverse Document Frequency (IDF):** rare terms are more relevant
  3. **Field Length Norm:** shorter fields with matches score higher
- Vector angle calculation for multi-term queries
- [**CRITICAL WARNING**](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=2700s): **DON'T convert scores to percentages** - they're only comparable within one query
- Scores change as data changes, making percentage mapping meaningless
- [Demonstration of why percentage scoring fails](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=2700s) using "my father's machines" example

**Technical Detail:** Elasticsearch uses BM25 by default (not classic TF-IDF)

---

### 4. [Dense Vector Search & Embeddings](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=2820s) (47:00 - 52:00)

**Key Points:**
- [OpenAI text-embedding-small](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=2820s) (128 dimensions) example
- Vector space representation with multiple dimensions (realistic/cartoonish, human/machine axes)
- [Star Wars character mapping in vector space](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=2880s)
- Dense vectors: floating-point arrays stored and compared for similarity
- Models learn representations but **dimensions aren't human-interpretable**
- 128-4096 dimensions typical
- **More dimensions ≠ always better** - trade-off with cost and performance
- HNSW (Hierarchical Navigable Small World) for efficient vector search

**Visual Example:** [Star Wars characters in 2D vector space](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=2880s) (realistic/cartoonish vs human/machine axes)

---

### 5. [Sparse Vector Search (SPLADE)](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=3120s) (52:00 - 55:00)

**Key Points:**
- [SPLADE/E5 models](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=3120s) for sparse embeddings
- Learned token expansion with relevance weights
- "These are not the droids you're looking for" expands to **~100 tokens** with scores
- **More interpretable** than dense vectors - can see which terms contribute
- Trade-off: expensive at query time due to many OR operations
- Didn't gain as much traction as dense vectors but useful for transparency
- [Live demonstration](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=3120s) of sparse vector output showing token expansion

**Example Output:** Original query expands to tokens like "droid" (0.8), "robot" (0.6), "android" (0.5), etc.

---

### 6. [Chunking Strategies](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=3300s) (55:00 - 01:19:00)

**Key Points:**
- Breaking long documents into smaller chunks for vector search
- **Chunking strategies:** by page, paragraph, sentence, with or without overlap
- [Semantic text field](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=3300s) automatically handles chunking in Elasticsearch
- Fragment highlighting to show which chunk matched
- [Example: "murder in the Skywalker saga"](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=4680s) finding relevant segment in long transcript
- Dense vectors have **limited context capacity** - can't embed entire books
- ["Murder" search finding "kill"](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=4680s) in chunked Star Wars transcript

**Best Practice:** Overlap chunks to avoid splitting important context across boundaries

---

### 7. [Hybrid Search & RRF](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=4800s) (01:20:00 - 01:23:00)

**Key Points:**
- [Combining lexical + semantic search](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=4800s)
- **Full Text Search** = lexical match + rank features (margin, ratings, clicks, freshness)
- **Boolean filters** (hard include/exclude) vs **scoring queries** (influence ranking)
- [**RRF (Reciprocal Rank Fusion)**](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=4800s): Position-based merging, **not score-based**
- **RRF Formula:** `1/(60 + position)` - blends different retrieval methods fairly
- **Hybrid** = any combination of 2+ search types (keyword + dense, keyword + sparse, all three, etc.)
- Information retrieval map showing lexical, semantic (sparse/dense), filters, and hybrid approaches

**Why RRF?** Scores from different systems (BM25 vs cosine similarity) aren't directly comparable

---

### 8. [Re-ranking](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=5580s) (01:33:00 - 01:42:00)

**Key Points:**
- [Two-step process](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=5580s):
  1. **Cheap retrieval** of N candidates (e.g., 1000)
  2. **Expensive re-ranking** of top K (e.g., 10)
- Elastic's built-in re-ranker model (version 1)
- **Window size** controls candidate pool (larger = slower but potentially better quality)
- **Minimum score threshold** to filter irrelevant candidates before re-ranking
- Trade-off: retrieval speed vs re-ranking quality
- [Re-ranking workflow](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=5640s): 1000 candidates from 1 million documents → re-rank top 10

**Example:** Initial search gets 1000 documents in 10ms, re-ranking top 10 takes 100ms

---

### 9. [Practical Considerations & Best Practices](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=5220s) (Distributed throughout)

**Key Points:**
- [Model evaluation](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=5220s): golden dataset, human experts, LLM-assisted evaluation
- Click-stream analysis for quality signals
- **E-commerce principle:** showing something > showing nothing
- [Postgres/PG-vector vs dedicated search engines](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=5220s)
  - **Postgres limitations:** no full BM25, scaling challenges, basic keyword search only
  - **Dedicated search engines:** designed for retrieval workloads
- [Vector search alone often insufficient](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=76s) - need hybrid approach for:
  - Brand names
  - Product IDs
  - Exact matches
  - Typos and fuzzy matching
- [Query rewriting with LLMs](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=5400s) before search
- [ES|QL pipe query language](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=6000s) as JSON alternative (introduced in 8.16)
- [Fuzziness](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=1800s) (Levenshtein distance) with auto-tuning based on term length
- HNSW index merging challenges

**Apache Lucene Foundation:** Shared with Solr, Tantivy - similar behavior across these systems

---

### 10. [Workshop Setup & Hands-on Examples](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=240s) (Throughout)

**Key Points:**
- [Shared Elasticsearch instance](https://www.youtube.com/watch?v=4Xe_iMYxBQc&t=240s) at **elasti.engineer**
- **Credentials:** workshop/workshop
- Star Wars dataset with 3 sample quotes
- Live query demonstrations with `explain=true` for debugging
- Participants encouraged to follow along or just watch
- Replace index name with unique handle to avoid conflicts

**Access:** https://elasti.engineer (gist with all code examples)

---

## Key Takeaways

1. **Keyword search is NOT dead** - still essential for exact matches, brands, product IDs
2. **Hybrid search is the future** - combine lexical + semantic for best results
3. **Chunking is critical** for long documents in vector search - can't embed entire books
4. **Language matters** - wrong analyzer = garbage results, use language-specific analyzers
5. **Scores are relative** - never convert to percentages, only comparable within one query
6. **"It depends"** - no one-size-fits-all solution, domain-specific tuning required
7. **Evaluation is hard** - requires golden datasets, human review, or LLM assistance
8. **Vector dimensions** - more ≠ better, depends on use case and cost tolerance
9. **RRF for hybrid** - position-based fusion works better than score-based merging
10. **Re-ranking wins** - two-step process balances speed and quality

---

## Technical Specifications

- **Default scoring:** BM25 (not classic TF-IDF)
- **Vector index:** HNSW (Hierarchical Navigable Small World)
- **Foundation:** Apache Lucene (shared with Solr, Tantivy)
- **Query language:** JSON DSL or ES|QL (pipe syntax, introduced in 8.16)
- **Semantic text field:** Automatic embedding management with chunking
- **Default English stop words:** ~33 words
- **Typical vector dimensions:** 128-4096

---

## Resources Mentioned

- **Workshop URL:** https://elasti.engineer
- **Credentials:** workshop/workshop
- **Dataset:** Star Wars quotes (3 samples)
- **Models discussed:**
  - OpenAI text-embedding-small (128 dimensions)
  - SPLADE/E5 (sparse vectors)
  - Elastic re-ranker model v1

---

**Video Duration:** 1:48:00
**Speaker:** Philipp Krenn, Elastic
**Event:** AI Engineer Conference
**Focus:** Information Retrieval fundamentals for RAG systems
