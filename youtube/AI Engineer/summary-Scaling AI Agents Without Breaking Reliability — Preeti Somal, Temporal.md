# Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal

**Video URL:** https://www.youtube.com/watch?v=1izYWsokr9s

---

## Executive Summary

Preeti Somal from Temporal presents how Temporal addresses the reliability and scalability challenges of building agentic AI applications. She explains that AI agents are complex distributed systems requiring orchestration, durability, and reliability. Temporal provides a developer-focused platform with language-idiomatic SDKs that handle the "plumbing code" (error handling, retries, state management) so developers can focus on business logic. The talk includes real-world customer examples (Dust, Gorgeous) running agents at scale in production, demonstrates a ticket booking agent architecture, and shows how Temporal's workflow abstraction manages the orchestration of LLMs, tools, and state over long periods with built-in visibility and debugging capabilities.

---

## Key Topics

### [Introduction to Temporal and Reliability](https://www.youtube.com/watch?v=1izYWsokr9s&t=17s)
- Temporal's mascot is a tardigrade (water bear), the most resilient animal, symbolizing their focus on reliability
- Company mission: outsource reliability and scalability for complex distributed systems
- Goal: convince audience that Temporal is the right platform for building agentic AI applications

**Key Points:**
- Temporal takes reliability "incredibly seriously"
- Company has booth with stickers and pins at the conference

### [AI Agents Are Complex Distributed Systems](https://www.youtube.com/watch?v=1izYWsokr9s&t=73s)
- Agents need to scale and provide durability and reliability
- Complex systems require orchestration with workflows at their core
- Must handle state over long periods of time
- Need human interaction for approvals
- Must run in parallel for efficiency and call tools

**Key Points:**
- Systems are inherently unreliable - LLM calls don't succeed 100% of the time
- Difficult to debug and test
- Visibility into what's happening is incredibly hard to get
- These problems have existed in building complex distributed systems before AI

### [Temporal's Solution](https://www.youtube.com/watch?v=1izYWsokr9s&t=200s)
- Founded to solve reliability and scalability problems in distributed systems
- Provides language-idiomatic SDKs (Python, Go, TypeScript, Java, .NET)
- Python overtook other languages in January, showing AI/ML adoption
- Handles all "plumbing code" - reliability, guardrails, retries
- Battle-tested: in production for over a decade

**Key Points:**
- Used in mission-critical applications by major customers
- Provides reliability "out of the box"
- Developer-focused tool, not for business users or non-technical people

### [Customer Examples and Use Cases](https://www.youtube.com/watch?v=1izYWsokr9s&t=297s)
- Dust: building agents on Temporal
- Gorgeous: AI agents for customer service (Reebok, Timbuktu, Glossier)
- Running agents at scale in production today
- Payment processing use case shows mission-critical workloads

**Key Points:**
- Customers achieve incredible agility and speed
- Can focus on business logic instead of reliability concerns
- Feature delivery velocity increased by 6x in some cases
- Cloud handles scaling automatically

### [Architecture: Before and After Temporal](https://www.youtube.com/watch?v=1izYWsokr9s&t=383s)
- Before: lots of interaction and error handling code
- After: abstracted into "workflow" concept
- Workflow is written as code by developers
- Orchestrates LLMs, chat history, database, and tools

**Key Points:**
- No "plumbing code" (if/retry statements) needed
- Workflow abstraction handles orchestration
- Code remains in developer's control and environment

### [Impact for Engineers](https://www.youtube.com/watch?v=1izYWsokr9s&t=480s)
- Accelerate development - applications in production within weeks
- Reach greater scale without managing scale logic
- Better reliability = better sleep and happier customers

**Key Points:**
- 6x improvement in feature delivery velocity (case study)
- Consumer applications scale automatically with events
- Cloud handles all scaling

### [Ticket Booking Agent Demo Walkthrough](https://www.youtube.com/watch?v=1izYWsokr9s&t=532s)
- Example architecture with user, system (Temporal), AI/LLMs, goals, and tools
- Workflow defines application flow as code
- Orchestrates interactive loops, receives signals, handles queries

**Key Points:**
- No plumbing code for failures and retries
- Temporal stores all workflow history for visibility
- Activities wrap tools as code
- Works with any LLM provider
- Failures handled transparently

### [Temporal Concepts and Abstractions](https://www.youtube.com/watch?v=1izYWsokr9s&t=600s)
- Workflow: defines flow, written as code, orchestrates interactions
- Signal: how workflow receives input
- Query: retrieve information from workflow
- Activities: wrap tools and external operations
- History: complete record of agent execution

**Key Points:**
- Rich set of programming abstractions
- All interactions stored in workflow history
- History can be exported for compliance or debugging
- Support for loops and complex patterns

### [Worker and Deployment Model](https://www.youtube.com/watch?v=1izYWsokr9s&t=781s)
- Worker: your code running in your environment
- Fits into existing CI/CD practices
- Temporal meets developers where they are
- Don't need to change how you write code

**Key Points:**
- Code runs in your environment, not Temporal's
- Temporal Cloud handles execution state, call stack, failures, retries
- Focus on business logic, not infrastructure concerns

### [Getting Started with Temporal](https://www.youtube.com/watch?v=1izYWsokr9s&t=840s)
- Open-source product
- Code Exchange has examples and samples
- Temporal Cloud available with free credits
- Easy to get started and "kick the tires"

**Key Points:**
- Can run examples locally or against cloud
- Quick to get up and running
- Booth G3 at conference for more information
- QR codes available for code examples

---

## Technical Highlights

**Workflow Abstraction Benefits:**
- Handles retries automatically
- Manages state durability
- Provides execution visibility
- Enables human-in-the-loop patterns
- Supports parallel execution

**Developer Experience:**
- Write code in familiar languages
- No new paradigms to learn
- Standard CI/CD integration
- Local development supported
- Cloud deployment simple

**Production Readiness:**
- Over a decade in production
- Used by major enterprises
- Handles mission-critical workloads (payments, customer service)
- Proven scalability
- Built-in observability

---

**Last Updated:** 2026-01-02
