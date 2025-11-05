"""
LangGraph Example: Building Stateful Multi-Actor Applications

This example showcases key LangGraph concepts:
1. Graph construction with nodes and edges
2. State management with TypedDict
3. Conditional edges for dynamic routing
4. Agent workflow patterns
5. Multi-step reasoning chains
"""

import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph


# Example 1: Define the state structure
class AgentState(TypedDict):
    """
    State that gets passed between nodes in the graph.
    The Annotated type with operator.add means values will be appended to lists.
    """

    messages: Annotated[list[str], operator.add]
    current_step: str
    counter: int
    final_result: str


# Example 2: Define node functions
def input_node(state: AgentState) -> AgentState:
    """
    First node: Processes initial input and adds to messages.
    Line 37-43: Demonstrates basic node operation with state updates.
    """
    print("\n[INPUT NODE]")
    print(f"  Current step: {state.get('current_step', 'None')}")
    print(f"  Counter: {state.get('counter', 0)}")

    return {
        "messages": ["Starting workflow..."],
        "current_step": "input",
        "counter": 1,
    }


def processing_node(state: AgentState) -> AgentState:
    """
    Second node: Processes data and updates state.
    Line 50-60: Shows how nodes can read and modify state.
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


def analysis_node(state: AgentState) -> AgentState:
    """
    Third node: Analyzes data and makes decisions.
    Line 67-78: Demonstrates data analysis and decision-making.
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


def decision_node(state: AgentState) -> AgentState:
    """
    Decision node: Determines next action based on state.
    Line 85-96: Shows conditional logic within nodes.
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


def output_node(state: AgentState) -> AgentState:
    """
    Final node: Produces final output.
    Line 103-115: Demonstrates final result generation.
    """
    print("\n[OUTPUT NODE]")
    print(f"  Previous step: {state['current_step']}")
    print(f"  Total messages: {len(state['messages'])}")

    # Generate final result
    final_result = f"Workflow completed after {state['counter']} steps"

    return {
        "messages": ["Workflow finished!"],
        "current_step": "output",
        "final_result": final_result,
    }


# Example 3: Define routing logic for conditional edges
def should_continue(state: AgentState) -> str:
    """
    Routing function: Determines which node to visit next.
    Line 122-135: Shows conditional edge routing based on state.
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


# Example 4: Build the graph
def build_workflow_graph() -> StateGraph:
    """
    Constructs the LangGraph workflow.
    Line 142-168: Demonstrates graph construction with nodes and edges.
    """
    print("\n" + "=" * 70)
    print("BUILDING LANGGRAPH WORKFLOW")
    print("=" * 70)

    # Initialize the graph with our state type
    workflow = StateGraph(AgentState)

    # Add nodes to the graph
    print("\nAdding nodes:")
    workflow.add_node("input", input_node)
    print("  ✓ Added: input")
    workflow.add_node("processing", processing_node)
    print("  ✓ Added: processing")
    workflow.add_node("analysis", analysis_node)
    print("  ✓ Added: analysis")
    workflow.add_node("decision", decision_node)
    print("  ✓ Added: decision")
    workflow.add_node("output", output_node)
    print("  ✓ Added: output")

    # Add edges to connect nodes
    print("\nAdding edges:")
    # Start -> input (entry point)
    workflow.add_edge(START, "input")
    print("  ✓ START → input")

    # input -> decision
    workflow.add_edge("input", "decision")
    print("  ✓ input → decision")

    # decision -> conditional routing
    workflow.add_conditional_edges(
        "decision",
        should_continue,
        {
            "processing": "processing",
            "analysis": "analysis",
            "output": "output",
        },
    )
    print("  ✓ decision → [conditional routing]")

    # All paths lead back to decision for next iteration
    workflow.add_edge("processing", "decision")
    print("  ✓ processing → decision")
    workflow.add_edge("analysis", "decision")
    print("  ✓ analysis → decision")

    # output -> END (exit point)
    workflow.add_edge("output", END)
    print("  ✓ output → END")

    return workflow


# Example 5: Execute the workflow
def run_workflow():
    """
    Runs the complete LangGraph workflow.
    Line 208-235: Shows workflow execution and state tracking.
    """
    print("\n" + "=" * 70)
    print("EXECUTING WORKFLOW")
    print("=" * 70)

    # Build and compile the graph
    workflow = build_workflow_graph()
    app = workflow.compile()

    print("\n✓ Graph compiled successfully!")

    # Initial state
    initial_state = {
        "messages": [],
        "current_step": "start",
        "counter": 0,
        "final_result": "",
    }

    print("\nStarting workflow execution...")
    print("-" * 70)

    # Run the workflow
    final_state = app.invoke(initial_state)

    # Display results
    print("\n" + "=" * 70)
    print("WORKFLOW RESULTS")
    print("=" * 70)
    print(f"\nFinal step: {final_state['current_step']}")
    print(f"Total steps: {final_state['counter']}")
    print(f"Final result: {final_state['final_result']}")
    print(f"\nMessage history ({len(final_state['messages'])} messages):")
    for i, msg in enumerate(final_state["messages"], 1):
        print(f"  {i}. {msg}")


# Example 6: Visualize graph structure
def visualize_graph():
    """
    Prints a textual representation of the graph structure.
    Line 252-275: Demonstrates graph introspection.
    """
    print("\n" + "=" * 70)
    print("GRAPH STRUCTURE VISUALIZATION")
    print("=" * 70)

    # Build the graph to show structure
    build_workflow_graph()

    print("\nNodes:")
    print("  • input")
    print("  • processing")
    print("  • analysis")
    print("  • decision")
    print("  • output")

    print("\nEdge Flow:")
    print("  START")
    print("    ↓")
    print("  input")
    print("    ↓")
    print("  decision ←──┐")
    print("    ↓         │")
    print("  [conditional routing]")
    print("    ├→ processing ──┘")
    print("    ├→ analysis ────┘")
    print("    └→ output")
    print("         ↓")
    print("       END")


def main():
    """Main entry point for the LangGraph demonstration."""
    print("=" * 70)
    print("🔄 LANGGRAPH DEMONSTRATION")
    print("=" * 70)
    print("\nLangGraph: A library for building stateful, multi-actor applications")
    print("Version: Compatible with langgraph >= 0.2.0")

    # Run the visualization first
    visualize_graph()

    # Execute the workflow
    run_workflow()

    print("\n" + "=" * 70)
    print("✨ DEMONSTRATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
