# Evaluating AI Search: A Practical Framework for Augmented AI Systems — Quotient AI + Tavily

**Video URL:** https://www.youtube.com/watch?v=wRJD0inpmjU

---

## Executive Summary

This presentation from Quotient AI and Tavily discusses the challenges of evaluating AI search systems in production environments. The speakers introduce a comprehensive framework for evaluating AI search that addresses two key problems: (1) static benchmarks fail to capture real-world performance on dynamic web content, and (2) ground truth is often unavailable in production settings. They present an open-source agent that generates dynamic evaluation datasets and demonstrate how reference-free metrics (answer completeness, document relevance, hallucination detection) can effectively substitute for traditional accuracy measurements when ground truth is unavailable.

---

## Topics

### [Introduction and Problem Statement](https://www.youtube.com/watch?v=wRJD0inpmjU&t=17s)
**Timestamp:** 00:17 - 02:30

- **Speakers Introduction:** Julia (CEO), Danna Emmery (Founding AI Researcher), and Mara Sher (Head of Engineering) from Quotient AI
- **Core Challenge:** Traditional monitoring approaches fail to keep up with the complexity of modern AI systems
- **Key Issues:**
  - AI agents operate in dynamic, constantly changing environments
  - Multiple failure modes occur simultaneously (hallucinations, retrieval failures, reasoning errors)
  - Systems make real-time decisions based on evolving web content and user interactions
- **Quotient AI's Approach:** Monitor live AI agents with expert evaluators that detect objective system failures without requiring ground truth data, human feedback, or benchmarks
- **Tavily's Challenge:** Building production-ready search agents while dealing with two fundamental sources of unpredictability:
  - The web is not static (real-time information means ground truth is a moving target)
  - Users ask odd, malformed questions with implicit context

### [Tavily's Use Cases and Evaluation Principles](https://www.youtube.com/watch?v=wRJD0inpmjU&t=153s)
**Timestamp:** 02:33 - 03:59

- **Tavily Overview:** Infrastructure layer for agent interaction at scale, providing LLMs with real-time web data
- **Example Use Cases:**
  - CLM company: AI legal assistant for instant case insights
  - Sports news outlet: Hybrid RAG chat agent for scores, games, and news updates
  - Credit card company: Real-time search to fight fraud by pinpointing merchant locations
- **Two Guiding Principles:**
  1. The web (foundation of data) is constantly changing, so evaluation methods must keep up
  2. Truth is often subjective and contextual - evaluation methods must be unbiased and fair even when absolute truth is hard to pin down

### [Offline Evaluation: Static vs. Dynamic Datasets](https://www.youtube.com/watch?v=wRJD0inpmjU&t=245s)
**Timestamp:** 04:05 - 06:30

- **Static Datasets:**
  - **Simple QA:** OpenAI benchmark for evaluating retrieval accuracy on short fact-seeking questions with single empirical answers
  - **HotPot QA:** Tests ability to answer multi-hop questions requiring reasoning across multiple documents
- **Limitations of Static Datasets:**
  - Cannot measure systems keeping up with rapidly evolving information
  - Don't address benchmarking questions where there's no one truth answer or subjectivity is involved
- **Benefits of Dynamic Datasets:**
  - Real-world alignment
  - Broad coverage - easily create eval sets for any domain or use case
  - Continuous relevancy through regular refreshing
  - Essential for benchmarking RAG systems in production

### [Open-Source Dynamic Eval Set Generator](https://www.youtube.com/watch?v=wRJD0inpmjU&t=397s)
**Timestamp:** 06:37 - 09:11

- **Solution:** Open-source agent that builds dynamic eval sets for web-based RAG systems
- **Key Steps (using LangGraph framework):**
  1. Generate broad web search queries for targeted domains (allows customization for specific applications)
  2. Aggregate grounding documents from multiple real-time AI search providers (to maximize coverage and minimize bias)
  3. Generate evidence-based question and answer pairs with answer context (increases reliability, reduces hallucinations)
  4. Use LangSmith to track experiments and manage offline evaluation runs
- **Future Improvements:**
  - Support range of question types (simple fact-based and multi-hop questions)
  - Ensure freshness, fairness, and coverage by addressing bias proactively
  - Add supervisor node for coordination in multi-agent architectures
- **Acknowledgment:** Ayal (Head of Data at Tavily) initiated the project

### [Holistic Benchmarking Framework](https://www.youtube.com/watch?v=wRJD0inpmjU&t=566s)
**Timestamp:** 09:26 - 10:20

- **Beyond Accuracy:** Need holistic evaluation framework
- **Additional Metrics:**
  - Source diversity
  - Source relevancy
  - Hallucination rates
- **Unsupervised Evaluation:** Leverage methods that remove need for labeled data, enabling scaled evaluations and addressing subjectivity issues

### [Experiment: Static vs. Dynamic Benchmark Comparison](https://www.youtube.com/watch?v=wRJD0inpmjU&t=621s)
**Timestamp:** 10:21 - 12:44

- **Two-Part Evaluation of Six AI Search Providers:**
  1. Compare accuracy on static (Simple QA) vs. dynamic benchmark (1000 rows from Tavily)
  2. Evaluate dynamic dataset responses using reference-free metrics
- **Results:**
  - Both datasets have similar topic distributions for fair comparison
  - **Simple QA Correctness Metric:** LLM judge comparing model responses against ground truth (correct/incorrect/not attempted)
  - **Key Finding:** Dynamic benchmark correctness scores substantially lower than static benchmark
  - **Ranking Changes:** Relative rankings changed considerably (e.g., Provider F performed worst on Simple QA but best on dynamic benchmark)
- **Simple QA Evaluator Limitations:**
  - False negatives: Responses flagged as incorrect despite containing correct answer
  - False positives: Responses flagged as correct but containing hallucinations in additional text

### [Reference-Free Metrics Overview](https://www.youtube.com/watch?v=wRJD0inpmjU&t=783s)
**Timestamp:** 13:03 - 14:55

- **Core Question:** Can reference-free metrics effectively identify issues in AI search when ground truths are unavailable?
- **Three Quotient Reference-Free Metrics:**
  1. **Answer Completeness:** Identifies if all question components were answered (fully addressed/unaddressed/unknown)
  2. **Document Relevance:** Percent of retrieved documents actually relevant to the question
  3. **Hallucination Detection:** Identifies facts in model response not present in retrieved documents

### [Answer Completeness Results](https://www.youtube.com/watch?v=wRJD0inpmjU&t=900s)
**Timestamp:** 15:00 - 15:44

- **Finding:** Answer completeness rankings closely match dynamic benchmark rankings
- **Correlation:** 0.94 correlation between average performance scores
- **Implication:** Reference-free metric can capture relative performance well
- **Caveat:** Completeness ≠ correctness; need to examine grounding documents for accuracy

### [Document Relevance and Transparency Issues](https://www.youtube.com/watch?v=wRJD0inpmjU&t=944s)
**Timestamp:** 15:44 - 17:04

- **Critical Limitation:** Only 3 of 6 search providers return retrieved documents used to generate answers
- **Majority Issue:** Most providers only provide citations, which are unhelpful at scale and limit transparency for debugging
- **Key Correlations:**
  - Strong inverse correlation between document relevance and number of unknown answers
  - Intuition: No relevant documents → model should say "I don't know" rather than attempt to answer

### [Hallucination Detection and Trade-offs](https://www.youtube.com/watch?v=wRJD0inpmjU&t=1027s)
**Timestamp:** 17:07 - 18:30

- **Surprising Finding:** Direct relationship between hallucination rate and document relevance
- **Case Study - Provider X:**
  - Highest hallucination rate
  - Highest overall document relevance
  - High answer completeness
  - Lowest rate of unknown answers
  - Highest answer correctness among three providers
- **Interpretation:** Provider X likely provides more reasoning, interpretations, or detailed responses, creating more opportunity for hallucination
- **Key Insight:** Different metrics measure different dimensions of response quality - performance in one may come at the expense of another (trade-off between answer completeness and hallucination)

### [Using Metrics to Diagnose and Fix Issues](https://www.youtube.com/watch?v=wRJD0inpmjU&t=1121s)
**Timestamp:** 18:41 - 19:26

- **Framework for Action:** Use metrics in conjunction to understand why things went wrong and identify strategies
- **Example Diagnosis:** Incomplete response + relevant documents + no hallucinations → retrieve more documents
- **Big Picture:** Evaluation should:
  - Do more than provide relative rankings
  - Help identify types of issues present
  - Guide understanding of what strategies to implement

### [Conclusion and Future Vision](https://www.youtube.com/watch?v=wRJD0inpmjU&t=1170s)
**Timestamp:** 19:30 - 20:27

- **Not Just About Evaluation:** Moving beyond better benchmarking, monitoring, or evaluation
- **Ultimate Goal:** Creating AI systems that can continuously improve themselves
- **Future Vision:**
  - Agents learn from patterns of outdated information, unreliable sources, and user needs
  - Detect hallucinations mid-conversation and correct course without human intervention
- **Building Blocks:** Dynamic datasets, holistic evaluation, and reference-free metrics are the foundation for self-improving augmented AI systems

---

**Last Updated:** January 2, 2026
