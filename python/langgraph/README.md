# LangGraph Python Illustration

This example demonstrates **LangGraph**, a library for building stateful, multi-actor applications with graphs. LangGraph enables you to create complex workflows with conditional routing, state management, and multi-step reasoning chains.

## Overview

This illustration showcases:
- ✅ Graph construction with nodes and edges
- ✅ State management using TypedDict
- ✅ Conditional edges for dynamic routing
- ✅ Agent workflow patterns
- ✅ Multi-step iterative processing

## Requirements

- **Python**: >= 3.11
- **LangGraph**: >= 0.2.0
- **LangChain Core**: >= 0.3.0

## Installation

```bash
uv sync
```

## Running the Example

```bash
uv run python main_langgraph.py
```

---

## Source Code with Annotations

### 1. State Definition (Lines 19-27)

The state is the data structure that flows through the graph. Using `Annotated` with `operator.add` means messages will be appended rather than replaced.

```python
class AgentState(TypedDict):
    """
    State that gets passed between nodes in the graph.
    The Annotated type with operator.add means values will be appended to lists.
    """

    messages: Annotated[list[str], operator.add]
    current_step: str
    counter: int
    final_result: str
```

**Key Concept**: The `Annotated[list[str], operator.add]` tells LangGraph to append new messages to the list instead of replacing it.

---

### 2. Node Functions (Lines 30-119)

Nodes are functions that receive state and return updated state. Each node represents a processing step in the workflow.

#### Input Node (Lines 30-45)
```python
def input_node(state: AgentState) -> AgentState:
    """
    First node: Processes initial input and adds to messages.
    """
    print("\n[INPUT NODE]")
    print(f"  Current step: {state.get('current_step', 'None')}")
    print(f"  Counter: {state.get('counter', 0)}")

    return {
        "messages": ["Starting workflow..."],
        "current_step": "input",
        "counter": 1,
    }
```

**Output Correlation**: See "INPUT NODE" section in execution output below.

---

#### Processing Node (Lines 48-62)
```python
def processing_node(state: AgentState) -> AgentState:
    """
    Second node: Processes data and updates state.
    """
    print("\n[PROCESSING NODE]")
    print(f"  Previous step: {state['current_step']}")
    print(f"  Message count: {len(state['messages'])}")
    print(f"  Counter: {state['counter']}")

    return {
        "messages": [f"Processing step {state['counter']}..."],
        "current_step": "processing",
        "counter": state["counter"] + 1,
    }
```

**Output Correlation**: This node runs twice (counter=1 and counter=2) as shown in the execution output.

---

#### Analysis Node (Lines 65-83)
```python
def analysis_node(state: AgentState) -> AgentState:
    """
    Third node: Analyzes data and makes decisions.
    """
    print("\n[ANALYSIS NODE]")
    print(f"  Previous step: {state['current_step']}")
    print(f"  Message count: {len(state['messages'])}")
    print(f"  Counter: {state['counter']}")

    # Simulate some analysis
    result = "Analysis complete" if state["counter"] >= 3 else "Needs more processing"

    return {
        "messages": [f"Analysis: {result}"],
        "current_step": "analysis",
        "counter": state["counter"] + 1,
    }
```

**Output Correlation**: This node runs twice (counter=3 and counter=4) with "Analysis complete" message.

---

#### Decision Node (Lines 86-105)
```python
def decision_node(state: AgentState) -> AgentState:
    """
    Decision node: Determines next action based on state.
    """
    print("\n[DECISION NODE]")
    print(f"  Previous step: {state['current_step']}")
    print(f"  Counter: {state['counter']}")

    # Check if we need more processing
    if state["counter"] < 5:
        decision = "continue"
    else:
        decision = "complete"

    print(f"  Decision: {decision}")

    return {
        "messages": [f"Decision made: {decision}"],
        "current_step": "decision",
    }
```

**Output Correlation**: Runs 5 times, making decisions to route to different nodes until counter reaches 5.

---

### 3. Conditional Routing (Lines 122-135)

This function determines which node to visit next based on the current state.

```python
def should_continue(state: AgentState) -> str:
    """
    Routing function: Determines which node to visit next.
    """
    print(f"\n[ROUTING] Counter: {state['counter']}")

    # Route based on counter value
    if state["counter"] < 3:
        print("  → Routing to: processing")
        return "processing"
    elif state["counter"] < 5:
        print("  → Routing to: analysis")
        return "analysis"
    else:
        print("  → Routing to: output")
        return "output"
```

**Routing Logic**:
- Counter < 3: Routes to `processing` node
- Counter 3-4: Routes to `analysis` node
- Counter >= 5: Routes to `output` node (final step)

---

### 4. Graph Construction (Lines 142-206)

This is where we build the actual graph structure.

```python
def build_workflow_graph() -> StateGraph:
    """
    Constructs the LangGraph workflow.
    """
    # Initialize the graph with our state type
    workflow = StateGraph(AgentState)

    # Add nodes to the graph
    workflow.add_node("input", input_node)
    workflow.add_node("processing", processing_node)
    workflow.add_node("analysis", analysis_node)
    workflow.add_node("decision", decision_node)
    workflow.add_node("output", output_node)

    # Add edges to connect nodes
    workflow.add_edge(START, "input")
    workflow.add_edge("input", "decision")

    # Conditional routing from decision node
    workflow.add_conditional_edges(
        "decision",
        should_continue,
        {
            "processing": "processing",
            "analysis": "analysis",
            "output": "output",
        },
    )

    workflow.add_edge("processing", "decision")
    workflow.add_edge("analysis", "decision")
    workflow.add_edge("output", END)

    return workflow
```

**Graph Structure**:
```
START → input → decision ←─┐
                  ↓         │
          [conditional]     │
            ├→ processing ──┘
            ├→ analysis ────┘
            └→ output → END
```

---

### 5. Workflow Execution (Lines 209-247)

```python
def run_workflow():
    """
    Runs the complete LangGraph workflow.
    """
    # Build and compile the graph
    workflow = build_workflow_graph()
    app = workflow.compile()

    # Initial state
    initial_state = {
        "messages": [],
        "current_step": "start",
        "counter": 0,
        "final_result": "",
    }

    # Run the workflow
    final_state = app.invoke(initial_state)

    # Display results
    print(f"\nFinal step: {final_state['current_step']}")
    print(f"Total steps: {final_state['counter']}")
    print(f"Final result: {final_state['final_result']}")
```

**Key Operations**:
1. **Line 214-215**: Build and compile the graph
2. **Line 218-223**: Define initial state
3. **Line 229**: Execute the workflow with `app.invoke()`
4. **Lines 232-244**: Display final results

---

## Program Output

Below is the complete output from running the program, showing the workflow execution step-by-step.

```
======================================================================
🔄 LANGGRAPH DEMONSTRATION
======================================================================

LangGraph: A library for building stateful, multi-actor applications
Version: Compatible with langgraph >= 0.2.0

======================================================================
GRAPH STRUCTURE VISUALIZATION
======================================================================

Adding nodes:
  ✓ Added: input
  ✓ Added: processing
  ✓ Added: analysis
  ✓ Added: decision
  ✓ Added: output

Adding edges:
  ✓ START → input
  ✓ input → decision
  ✓ decision → [conditional routing]
  ✓ processing → decision
  ✓ analysis → decision
  ✓ output → END

Nodes:
  • input
  • processing
  • analysis
  • decision
  • output

Edge Flow:
  START
    ↓
  input
    ↓
  decision ←──┐
    ↓         │
  [conditional routing]
    ├→ processing ──┘
    ├→ analysis ────┘
    └→ output
         ↓
       END

======================================================================
EXECUTING WORKFLOW
======================================================================

✓ Graph compiled successfully!

Starting workflow execution...
----------------------------------------------------------------------

[INPUT NODE]
  Current step: start
  Counter: 0
```
**Annotation**: Initial node execution with counter=0

```
[DECISION NODE]
  Previous step: input
  Counter: 1
  Decision: continue

[ROUTING] Counter: 1
  → Routing to: processing
```
**Annotation**: First decision point - counter=1, routes to processing

```
[PROCESSING NODE]
  Previous step: decision
  Message count: 2
  Counter: 1

[DECISION NODE]
  Previous step: processing
  Counter: 2
  Decision: continue

[ROUTING] Counter: 2
  → Routing to: processing
```
**Annotation**: First processing iteration - counter increments to 2

```
[PROCESSING NODE]
  Previous step: decision
  Message count: 4
  Counter: 2

[DECISION NODE]
  Previous step: processing
  Counter: 3
  Decision: continue

[ROUTING] Counter: 3
  → Routing to: analysis
```
**Annotation**: Second processing iteration - counter=3, routing changes to analysis

```
[ANALYSIS NODE]
  Previous step: decision
  Message count: 6
  Counter: 3

[DECISION NODE]
  Previous step: analysis
  Counter: 4
  Decision: continue

[ROUTING] Counter: 4
  → Routing to: analysis
```
**Annotation**: First analysis iteration - counter=4

```
[ANALYSIS NODE]
  Previous step: decision
  Message count: 8
  Counter: 4

[DECISION NODE]
  Previous step: analysis
  Counter: 5
  Decision: complete

[ROUTING] Counter: 5
  → Routing to: output
```
**Annotation**: Second analysis iteration - counter=5, decision changes to "complete"

```
[OUTPUT NODE]
  Previous step: decision
  Total messages: 10

======================================================================
WORKFLOW RESULTS
======================================================================

Final step: output
Total steps: 5
Final result: Workflow completed after 5 steps

Message history (11 messages):
  1. Starting workflow...
  2. Decision made: continue
  3. Processing step 1...
  4. Decision made: continue
  5. Processing step 2...
  6. Decision made: continue
  7. Analysis: Analysis complete
  8. Decision made: continue
  9. Analysis: Analysis complete
  10. Decision made: complete
  11. Workflow finished!

======================================================================
✨ DEMONSTRATION COMPLETE
======================================================================
```

---

## Execution Flow Summary

The workflow executes in the following sequence:

1. **INPUT** (counter: 0→1): Initialize workflow
2. **DECISION** → **PROCESSING** (counter: 1→2): First processing cycle
3. **DECISION** → **PROCESSING** (counter: 2→3): Second processing cycle
4. **DECISION** → **ANALYSIS** (counter: 3→4): First analysis cycle
5. **DECISION** → **ANALYSIS** (counter: 4→5): Second analysis cycle
6. **DECISION** → **OUTPUT**: Final output generation

**Total Iterations**: 5 cycles through the decision node, demonstrating dynamic routing based on state.

---

## Key Concepts Illustrated

### 1. **State Management**
- State flows through nodes and accumulates data
- `operator.add` annotation enables message accumulation
- State updates are partial - only specified fields are modified

### 2. **Conditional Routing**
- `add_conditional_edges()` enables dynamic graph navigation
- Routing function (`should_continue`) determines next node
- Different paths based on state values (counter in this example)

### 3. **Cyclic Graphs**
- Nodes can loop back (processing → decision → processing)
- Useful for iterative refinement and multi-step reasoning
- Loop continues until condition met (counter >= 5)

### 4. **Node Functions**
- Pure functions that receive and return state
- Can perform any computation, API calls, or LLM interactions
- Return partial state updates (LangGraph merges them)

---

## Common Use Cases

LangGraph is particularly useful for:

- **Agent Workflows**: Multi-step agent reasoning with tool calls
- **Chatbots**: Stateful conversations with context management
- **Data Pipelines**: Complex ETL workflows with conditional logic
- **Approval Workflows**: Human-in-the-loop systems
- **Multi-Agent Systems**: Coordinating multiple AI agents

---

## Additional Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [LangChain Documentation](https://python.langchain.com/)

---

## Version Requirements

This example requires:
- **Python 3.11+**: Uses modern type hints and TypedDict
- **LangGraph 0.2.0+**: Compatible with the latest API
- **LangChain Core 0.3.0+**: Required dependency for LangGraph

The code uses standard LangGraph patterns that should remain stable across minor version updates.
