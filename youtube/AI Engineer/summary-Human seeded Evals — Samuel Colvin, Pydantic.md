# Human seeded Evals — Samuel Colvin, Pydantic

**Video URL:** https://www.youtube.com/watch?v=o_LRtAomJCs

---

## Executive Summary

Samuel Colvin, creator of Pydantic, presents practical techniques for building AI applications with type safety and reliability. He demonstrates how Pydantic AI's approach differs from frameworks like LangChain by providing full type safety, validation error recovery through agentic loops, and observability with Logfire. The talk showcases live coding examples including structured data extraction with validation retry logic, type-safe dependency injection for tools, and long-term memory implementation with PostgreSQL. While titled around evals, the presentation focuses primarily on Pydantic AI's architecture and type safety features.

---

## Topics

### [Introduction and Context](https://www.youtube.com/watch?v=o_LRtAomJCs&t=0s)
**[00:00 - 01:00]**

- Samuel introduces the talk, adapted from his Pyon presentation on "Building AI Applications the Pydantic Way"
- Acknowledges he won't have time to cover evals in detail due to time constraints
- Core thesis: While everything is changing rapidly with AI, the fundamentals remain—building reliable, scalable applications is still hard (arguably harder with GenAI)
- Type safety is crucial not just for production bug prevention, but for rapid refactoring during development
- AI coding agents like Cursor can use type checking to "mark their own homework"

### [What is an Agent?](https://www.youtube.com/watch?v=o_LRtAomJCs&t=117s)
**[01:57 - 03:00]**

- References Barry Zhang's definition from Anthropic (presented at AI Engineer NYC, February)
- Now widely adopted by OpenAI, Google ADK, and others
- Key components:
  - Environment and tools that access it
  - System prompt describing the task
  - While loop: call LLM → get actions → run tools → update state → repeat
- Critical bug in the pseudocode: no exit condition for the loop

### [Handling Agent Loop Termination](https://www.youtube.com/watch?v=o_LRtAomJCs&t=180s)
**[03:00 - 03:33]**

- The challenge: determining when to exit the agentic loop
- Multiple approaches:
  - Exit when LLM returns plain text instead of tool calls
  - Use "final result tools" that trigger termination
  - Leverage structured output types (OpenAI, Google) to signal completion
- This is a non-trivial design decision in agent architecture

### [Live Demo: Simple Structured Data Extraction](https://www.youtube.com/watch?v=o_LRtAomJCs&t=213s)
**[03:33 - 04:25]**

- Minimal example: Pydantic model with three fields (Person: name, date of birth, etc.)
- Extract structured data from unstructured text using Pydantic AI
- Input could scale from simple sentences to large PDFs
- Schema can be simple or incredibly complex with nested models
- Single-shot extraction: one LLM call → structured output → validation → result
- Uses "final result tool" under the hood
- No agentic loop needed for this simple case

### [Agentic Loop with Validation Retry](https://www.youtube.com/watch?v=o_LRtAomJCs&t=265s)
**[04:25 - 06:00]**

- Enhanced example: field validator requires date of birth before 1900
- Intentionally ambiguous input: "born in '87" (could be 1887 or 1987)
- First attempt: model assumes 1987 → validation error
- Agentic retry: validation errors returned to model with "please try again"
- Model uses validation feedback to correct to 1887
- Demonstrates the power of validation-driven retry loops

### [Observability with Logfire](https://www.youtube.com/watch?v=o_LRtAomJCs&t=360s)
**[06:00 - 06:45]**

- Code instrumented with Logfire (Pydantic's observability platform)
- Complete trace visibility:
  - User prompt
  - Tool calls (final_result with initial date: 1987)
  - Validation error response
  - Retry with corrected date: 1887
- Two LLM calls to Gemini Flash visible in the trace
- Demonstrates debugging and understanding agent behavior

### [Type Safety Deep Dive](https://www.youtube.com/watch?v=o_LRtAomJCs&t=405s)
**[06:45 - 08:00]**

- Agent class is generic over output type (Person)
- Result.data is guaranteed to be type Person both at runtime (Pydantic validation) and in type checkers
- Accessing `result.data.name` works; accessing `result.data.first_name` produces type error
- Second generic: `deps` type for dependency injection
- Type-safe dependencies available to tools
- Strong contrast with LangChain/LangGraph which "either through decision or inability decided not to build something that's type safe"
- Admits type safety requires work on both framework and user side, but pays off during refactoring

### [Tools and Dependency Injection](https://www.youtube.com/watch?v=o_LRtAomJCs&t=480s)
**[08:00 - 09:00]**

- Example: long-term memory implementation
- Two tools: `record_memory` and `retrieve_memory`
- Tools registered with `@agent.tool` decorator
- Deps type defined as dataclass
- First parameter: `RunContext` parameterized with deps type
- Accessing `context.deps` is type-safe: IDE knows available attributes
- Changing field types produces immediate type errors
- Claims Pydantic AI is the only framework working this hard on type safety

### [Type Safety Benefits](https://www.youtube.com/watch?v=o_LRtAomJCs&t=540s)
**[09:00 - 10:00]**

- Type guarantee chain:
  - Deps type declaration → tool context → agent run
  - All parts must match; mismatches caught by type checker
- Requires effort to set up but "incredibly easy to refactor your code"
- When calling `agent.run()`, deps parameter must be instance of declared deps type
- Wrong type produces typing error before runtime
- Live coding setup: attempting to run memory example with PostgreSQL

### [Live Demo: Memory with Observability](https://www.youtube.com/watch?v=o_LRtAomJCs&t=600s)
**[10:00 - 12:00]**

- Quick Docker setup for PostgreSQL
- First run fails, demonstrates using Logfire to debug
- Trace analysis shows:
  - Run 1: Called `record_memory` with "user's name is Samuel"
  - Query with "your name" failed (not a substring match)
  - Run 2: Query with "name" succeeded (substring match works)
- Demonstrates observability value for debugging agent behavior
- Trace shows timing for each call
- Pricing information available at both aggregate and individual span level
- Talk ends due to time constraints

---

## Key Takeaways

1. **Type Safety is Critical**: Pydantic AI prioritizes complete type safety across agent definitions, tool registration, and dependency injection—unique among agent frameworks

2. **Validation as Feedback**: Returning validation errors to models creates effective retry loops without explicit prompting

3. **Observability is Essential**: Logfire integration provides complete visibility into agent runs, tool calls, timing, and costs

4. **Agentic Loops Add Value**: Even simple structured extraction benefits from retry capability when validation fails

5. **Dependencies Done Right**: Type-safe dependency injection ensures tools have guaranteed access to properly typed resources

6. **Practical Trade-offs**: Admits type safety requires more setup effort but delivers major benefits during refactoring and development

7. **Framework Philosophy**: Direct criticism of LangChain/LangGraph for lack of type safety; positions Pydantic AI as the type-safe alternative

---

**Last updated:** January 3, 2026
