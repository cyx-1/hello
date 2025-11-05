# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
CrewAI Example: Multi-Agent Collaboration Framework

This example showcases key CrewAI concepts and unique capabilities:
1. Role-based agents with distinct personalities and expertise
2. Crew orchestration with collaborative workflows
3. Task delegation and hierarchical execution
4. Agent memory and context sharing
5. Built-in tool integration and custom tools

UNIQUE DIFFERENTIATORS FROM OTHER FRAMEWORKS:
==============================================

VS. LANGGRAPH:
--------------
- CrewAI: Team/crew metaphor with role-based agents (CEO, researcher, writer)
- LangGraph: Graph-based state machines with nodes and edges
- CrewAI focuses on agent collaboration and delegation
- LangGraph focuses on state flow and conditional routing

VS. AUTOGEN:
------------
- CrewAI: Task-centric with explicit roles, goals, and backstories
- AutoGen: Conversation-centric with multi-agent chat patterns
- CrewAI has built-in process types (sequential, hierarchical)
- AutoGen emphasizes flexible conversation flows

VS. SEMANTIC KERNEL:
--------------------
- CrewAI: Agent-first design with crew orchestration
- Semantic Kernel: Plugin-first design with skills and planners
- CrewAI simulates organizational dynamics (teams, roles, hierarchy)
- Semantic Kernel focuses on function calling and memory

CREWAI'S UNIQUE STRENGTHS:
--------------------------
1. **Role-Based Design**: Agents have roles, goals, backstories
2. **Crew Orchestration**: Natural team collaboration patterns
3. **Process Types**: Sequential, hierarchical, consensus-based
4. **Memory Systems**: Short-term, long-term, entity memory
5. **Task Delegation**: Agents can delegate subtasks to specialists
6. **Built-in Tools**: Web search, file operations, code execution

NOTE: This is a demonstration/educational version that simulates CrewAI
concepts without requiring API keys or external services. For production use,
install crewai: pip install crewai crewai-tools
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


# =============================================================================
# SIMULATED CREWAI CLASSES FOR DEMONSTRATION
# =============================================================================
# These classes simulate CrewAI's API for educational purposes
# In production, use: from crewai import Agent, Crew, Process, Task


class Process(Enum):
    """Process types supported by CrewAI."""

    sequential = "sequential"
    hierarchical = "hierarchical"
    consensus = "consensus"


@dataclass
class Agent:
    """
    Simulated CrewAI Agent class.
    Real CrewAI agents would connect to LLMs and execute tasks.
    """

    role: str
    goal: str
    backstory: str
    verbose: bool = True
    allow_delegation: bool = False
    max_iter: int = 3


@dataclass
class Task:
    """
    Simulated CrewAI Task class.
    Real CrewAI tasks would be executed by agents using LLMs.
    """

    description: str
    expected_output: str
    agent: Agent
    context: list[Any] | None = None


@dataclass
class Crew:
    """
    Simulated CrewAI Crew class.
    Real CrewAI crews would orchestrate agent collaboration.
    """

    agents: list[Agent]
    tasks: list[Task]
    process: Process = Process.sequential
    verbose: bool = True

    def kickoff(self) -> str:
        """Simulate crew execution."""
        return "Crew execution simulated successfully."


# =============================================================================
# EXAMPLE 1: Define Specialized Agents with Roles
# =============================================================================
def create_research_agent() -> Agent:
    """
    Creates a Research Specialist agent.
    Lines 69-82: Demonstrates agent creation with role, goal, and backstory.

    UNIQUE TO CREWAI: The role/goal/backstory pattern creates rich agent
    personalities that guide behavior throughout the workflow.
    """
    print("\n[CREATING RESEARCH AGENT]")

    agent = Agent(
        role="Senior Research Analyst",
        goal="Uncover cutting-edge insights and comprehensive information on given topics",
        backstory=(
            "You are an expert research analyst with a PhD in Computer Science. "
            "You have 15 years of experience in technology research and analysis. "
            "You're known for your meticulous attention to detail and ability to "
            "synthesize complex information into clear, actionable insights."
        ),
        verbose=True,
        allow_delegation=False,  # This agent doesn't delegate
        max_iter=3,  # Maximum iterations for task completion
    )

    print(f"  ✓ Role: {agent.role}")
    print(f"  ✓ Goal: {agent.goal}")
    print(f"  ✓ Delegation: {agent.allow_delegation}")

    return agent


def create_writer_agent() -> Agent:
    """
    Creates a Content Writer agent.
    Lines 90-107: Shows how different agents have different capabilities.

    UNIQUE TO CREWAI: Each agent can have different settings like
    delegation capabilities, creating hierarchical team structures.
    """
    print("\n[CREATING WRITER AGENT]")

    agent = Agent(
        role="Expert Content Writer",
        goal="Create engaging, informative, and well-structured technical content",
        backstory=(
            "You are a seasoned technical writer with a talent for making complex "
            "topics accessible. You've written for major tech publications and "
            "have a gift for storytelling. Your content is known for clarity, "
            "depth, and engaging narrative flow."
        ),
        verbose=True,
        allow_delegation=True,  # This agent CAN delegate to others
        max_iter=5,
    )

    print(f"  ✓ Role: {agent.role}")
    print(f"  ✓ Goal: {agent.goal}")
    print(f"  ✓ Delegation: {agent.allow_delegation}")

    return agent


def create_editor_agent() -> Agent:
    """
    Creates an Editor agent for quality control.
    Lines 115-131: Demonstrates quality assurance agent role.

    UNIQUE TO CREWAI: Agents can be designed for specific workflow stages
    like review, approval, or quality control.
    """
    print("\n[CREATING EDITOR AGENT]")

    agent = Agent(
        role="Senior Content Editor",
        goal="Ensure content quality, accuracy, and professional standards",
        backstory=(
            "You are a meticulous editor with an eye for detail and a deep "
            "understanding of technical accuracy. You've edited hundreds of "
            "technical articles and are known for elevating good content to "
            "exceptional content while maintaining the author's voice."
        ),
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )

    print(f"  ✓ Role: {agent.role}")
    print(f"  ✓ Goal: {agent.goal}")

    return agent


# =============================================================================
# EXAMPLE 2: Define Tasks with Context and Dependencies
# =============================================================================
def create_research_task(agent: Agent, topic: str) -> Task:
    """
    Creates a research task for the research agent.
    Lines 151-169: Shows task creation with detailed descriptions.

    UNIQUE TO CREWAI: Tasks have explicit expected_output specifications
    that guide agents toward desired outcomes.
    """
    print("\n[CREATING RESEARCH TASK]")

    task = Task(
        description=(
            f"Research the topic: '{topic}'\n\n"
            "Conduct comprehensive research covering:\n"
            "1. Core concepts and fundamental principles\n"
            "2. Current state and recent developments\n"
            "3. Key advantages and unique features\n"
            "4. Comparison with alternatives\n"
            "5. Real-world applications and use cases\n"
            "\n"
            "Provide well-sourced, accurate information with clear structure."
        ),
        expected_output=(
            "A detailed research report with 5 main sections, "
            "each containing 2-3 key points with explanations."
        ),
        agent=agent,
    )

    print(f"  ✓ Assigned to: {agent.role}")
    print(f"  ✓ Topic: {topic}")

    return task


def create_writing_task(agent: Agent, research_task: Task) -> Task:
    """
    Creates a writing task that depends on research completion.
    Lines 179-199: Demonstrates task dependencies and context passing.

    UNIQUE TO CREWAI: Tasks can reference other tasks as context,
    creating automatic data flow between agents.
    """
    print("\n[CREATING WRITING TASK]")

    task = Task(
        description=(
            "Using the research provided, write an engaging technical article.\n\n"
            "Requirements:\n"
            "1. Start with a compelling introduction\n"
            "2. Organize information in logical sections\n"
            "3. Use clear, accessible language\n"
            "4. Include practical examples\n"
            "5. End with actionable conclusions\n"
            "\n"
            "Style: Professional yet conversational, technical but accessible."
        ),
        expected_output=(
            "A well-structured article of 400-500 words with clear sections, "
            "engaging narrative, and practical insights."
        ),
        agent=agent,
        context=[research_task],  # This task depends on research_task output
    )

    print(f"  ✓ Assigned to: {agent.role}")
    print("  ✓ Context: Depends on research task")

    return task


def create_editing_task(agent: Agent, writing_task: Task) -> Task:
    """
    Creates an editing task for final quality control.
    Lines 209-227: Shows final review stage in the workflow.

    UNIQUE TO CREWAI: Multi-stage workflows with different agents
    handling different phases (research → write → edit).
    """
    print("\n[CREATING EDITING TASK]")

    task = Task(
        description=(
            "Review and refine the article for publication.\n\n"
            "Focus areas:\n"
            "1. Technical accuracy and clarity\n"
            "2. Grammar, style, and flow\n"
            "3. Logical structure and transitions\n"
            "4. Overall readability and impact\n"
            "\n"
            "Provide the final, polished version ready for publication."
        ),
        expected_output=(
            "A publication-ready article with all edits applied, "
            "maintaining technical accuracy while ensuring excellent readability."
        ),
        agent=agent,
        context=[writing_task],  # This task depends on writing_task output
    )

    print(f"  ✓ Assigned to: {agent.role}")
    print("  ✓ Context: Depends on writing task")

    return task


# =============================================================================
# EXAMPLE 3: Create and Execute a Crew (Sequential Process)
# =============================================================================
def run_sequential_crew(topic: str) -> str:
    """
    Executes a crew with sequential process.
    Lines 246-284: Demonstrates CrewAI's core orchestration pattern.

    UNIQUE TO CREWAI: The Crew abstraction orchestrates multiple agents
    working on interconnected tasks with automatic context passing.

    PROCESS TYPES IN CREWAI:
    - Sequential: Tasks execute in order (used here)
    - Hierarchical: Manager agent delegates to workers
    - Consensus: Multiple agents vote on decisions
    """
    print("\n" + "=" * 70)
    print("RUNNING SEQUENTIAL CREW WORKFLOW")
    print("=" * 70)
    print(f"\nTopic: {topic}")

    # Step 1: Create agents
    print("\n--- STEP 1: Creating Team ---")
    researcher = create_research_agent()
    writer = create_writer_agent()
    editor = create_editor_agent()

    # Step 2: Create tasks
    print("\n--- STEP 2: Defining Tasks ---")
    research_task = create_research_task(researcher, topic)
    writing_task = create_writing_task(writer, research_task)
    editing_task = create_editing_task(editor, writing_task)

    # Step 3: Assemble crew
    print("\n--- STEP 3: Assembling Crew ---")
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        process=Process.sequential,  # Tasks execute in order
        verbose=True,
    )

    print(f"  ✓ Agents: {len(crew.agents)}")
    print(f"  ✓ Tasks: {len(crew.tasks)}")
    print(f"  ✓ Process: {crew.process}")

    # Step 4: Execute workflow
    print("\n--- STEP 4: Executing Workflow ---")
    print("\nNOTE: Each agent will work on their assigned task in sequence.")
    print("Output from each task becomes input for the next.\n")

    result = crew.kickoff()  # Start the crew workflow

    return str(result)


# =============================================================================
# EXAMPLE 4: Demonstrate Agent Delegation
# =============================================================================
def run_delegation_example() -> None:
    """
    Demonstrates agent delegation capabilities.
    Lines 303-344: Shows hierarchical collaboration through delegation.

    UNIQUE TO CREWAI: Agents with allow_delegation=True can delegate
    subtasks to other team members, enabling hierarchical workflows.
    """
    print("\n" + "=" * 70)
    print("AGENT DELEGATION EXAMPLE")
    print("=" * 70)

    print("\n[DELEGATION CONCEPT]")
    print("When allow_delegation=True, an agent can:")
    print("  • Break down complex tasks")
    print("  • Assign subtasks to specialists")
    print("  • Coordinate multiple agents")
    print("  • Synthesize results")

    # Create a delegating manager agent
    manager = Agent(
        role="Project Manager",
        goal="Coordinate team efforts and deliver high-quality results",
        backstory=(
            "You are an experienced project manager who knows how to leverage "
            "team expertise. You break down complex projects and delegate to "
            "specialists, ensuring efficient collaboration."
        ),
        verbose=True,
        allow_delegation=True,  # KEY: Manager can delegate
        max_iter=5,
    )

    # Create specialist agents
    researcher = create_research_agent()
    writer = create_writer_agent()

    print("\n[DELEGATION HIERARCHY]")
    print(f"  Manager: {manager.role} (can delegate: {manager.allow_delegation})")
    print(
        f"  ├─ Specialist 1: {researcher.role} (can delegate: {researcher.allow_delegation})"
    )
    print(f"  └─ Specialist 2: {writer.role} (can delegate: {writer.allow_delegation})")

    print("\nIn a real scenario, the manager would:")
    print("  1. Receive a complex task")
    print("  2. Break it into subtasks")
    print("  3. Delegate to researchers and writers")
    print("  4. Review and synthesize the results")


# =============================================================================
# EXAMPLE 5: Display Framework Comparison
# =============================================================================
def display_framework_comparison() -> None:
    """
    Shows detailed comparison between agent frameworks.
    Lines 361-442: Comprehensive framework comparison guide.
    """
    print("\n" + "=" * 70)
    print("FRAMEWORK COMPARISON: CrewAI vs Others")
    print("=" * 70)

    print("\n┌─────────────────────────────────────────────────────────────────┐")
    print("│ CREWAI: Team Collaboration Framework                           │")
    print("└─────────────────────────────────────────────────────────────────┘")
    print("\n✦ Core Metaphor: Simulating company/team dynamics")
    print("✦ Key Concept: Agents with roles working toward shared goals")
    print("✦ Strengths:")
    print("  • Natural modeling of organizational workflows")
    print("  • Built-in role/goal/backstory for rich agent personalities")
    print("  • Multiple process types (sequential, hierarchical, consensus)")
    print("  • Task delegation and agent collaboration")
    print("  • Memory systems (short-term, long-term, entity)")
    print("\n✦ Best For:")
    print("  • Content creation pipelines")
    print("  • Multi-stage review processes")
    print("  • Organizational workflow simulation")
    print("  • Team-based problem solving")

    print("\n┌─────────────────────────────────────────────────────────────────┐")
    print("│ LANGGRAPH: State Machine Framework                             │")
    print("└─────────────────────────────────────────────────────────────────┘")
    print("\n✦ Core Metaphor: State machines with nodes and edges")
    print("✦ Key Concept: State flows through a directed graph")
    print("✦ Strengths:")
    print("  • Precise control over execution flow")
    print("  • Conditional routing and cyclic graphs")
    print("  • Explicit state management")
    print("  • Visual graph representation")
    print("  • Great for complex state transitions")
    print("\n✦ Best For:")
    print("  • Workflows with complex conditional logic")
    print("  • Iterative refinement loops")
    print("  • State-dependent decision making")
    print("  • Cyclic and branching workflows")

    print("\n┌─────────────────────────────────────────────────────────────────┐")
    print("│ AUTOGEN: Conversation Framework                                │")
    print("└─────────────────────────────────────────────────────────────────┘")
    print("\n✦ Core Metaphor: Multi-agent conversations")
    print("✦ Key Concept: Agents communicate through natural dialogue")
    print("✦ Strengths:")
    print("  • Flexible conversation patterns")
    print("  • Human-in-the-loop integration")
    print("  • Code generation and execution")
    print("  • Dynamic agent interactions")
    print("  • GroupChat for multi-agent scenarios")
    print("\n✦ Best For:")
    print("  • Conversational AI applications")
    print("  • Code generation workflows")
    print("  • Interactive problem solving")
    print("  • Human-AI collaboration")

    print("\n┌─────────────────────────────────────────────────────────────────┐")
    print("│ SEMANTIC KERNEL: Plugin Framework                              │")
    print("└─────────────────────────────────────────────────────────────────┘")
    print("\n✦ Core Metaphor: Skills and plugins with orchestration")
    print("✦ Key Concept: Function calling with AI planners")
    print("✦ Strengths:")
    print("  • Rich plugin/skill ecosystem")
    print("  • Memory and embeddings built-in")
    print("  • Multiple LLM provider support")
    print("  • Enterprise-ready architecture")
    print("  • Microsoft ecosystem integration")
    print("\n✦ Best For:")
    print("  • Enterprise applications")
    print("  • .NET/Microsoft stack integration")
    print("  • Plugin-based architectures")
    print("  • Semantic function orchestration")

    print("\n" + "=" * 70)
    print("QUICK SELECTION GUIDE")
    print("=" * 70)
    print("\nChoose CrewAI when you want:")
    print("  → Role-based agent teams")
    print("  → Organizational workflow patterns")
    print("  → Agent delegation and collaboration")
    print("\nChoose LangGraph when you want:")
    print("  → Precise state flow control")
    print("  → Complex conditional routing")
    print("  → Cyclic and iterative workflows")
    print("\nChoose AutoGen when you want:")
    print("  → Natural conversation flows")
    print("  → Code generation tasks")
    print("  → Human-in-the-loop scenarios")
    print("\nChoose Semantic Kernel when you want:")
    print("  → Enterprise Microsoft integration")
    print("  → Plugin-first architecture")
    print("  → Rich memory and embeddings")


# =============================================================================
# EXAMPLE 6: Show Memory and Context Features
# =============================================================================
def demonstrate_memory_features() -> None:
    """
    Explains CrewAI's memory capabilities.
    Lines 462-494: Memory system overview.

    UNIQUE TO CREWAI: Built-in memory systems for agent context.
    """
    print("\n" + "=" * 70)
    print("CREWAI MEMORY SYSTEMS")
    print("=" * 70)

    print("\n[1] SHORT-TERM MEMORY")
    print("  • Stores recent interactions within current session")
    print("  • Automatically maintains conversation context")
    print("  • Helps agents remember previous task outputs")
    print("  • Usage: Enable with memory=True in Crew")

    print("\n[2] LONG-TERM MEMORY")
    print("  • Persists information across sessions")
    print("  • Learns from past executions")
    print("  • Improves performance over time")
    print("  • Usage: Configured via memory settings")

    print("\n[3] ENTITY MEMORY")
    print("  • Tracks entities mentioned in tasks")
    print("  • Maintains entity relationships")
    print("  • Provides entity context to agents")
    print("  • Usage: Automatically populated during execution")

    print("\n[4] CONTEXT PASSING")
    print("  • Tasks can reference other tasks as context")
    print("  • Output from one task flows to dependent tasks")
    print("  • Enables multi-stage processing pipelines")
    print("  • Usage: Set context=[previous_task] in Task")

    print("\nExample Memory Configuration:")
    print("  crew = Crew(")
    print("      agents=[...],")
    print("      tasks=[...],")
    print("      memory=True,  # Enable memory systems")
    print("      verbose=True")
    print("  )")


# =============================================================================
# MAIN EXECUTION
# =============================================================================
def main() -> None:
    """Main entry point for CrewAI demonstration."""
    print("=" * 70)
    print("🤖 CREWAI DEMONSTRATION")
    print("=" * 70)
    print("\nCrewAI: Role-Based Multi-Agent Collaboration Framework")
    print("Version: Compatible with crewai >= 0.80.0")

    # Show framework comparison
    display_framework_comparison()

    # Show memory features
    demonstrate_memory_features()

    # Show delegation example
    run_delegation_example()

    # Run main workflow with simulated execution
    print("\n" + "=" * 70)
    print("SIMULATED WORKFLOW EXECUTION")
    print("=" * 70)
    print("\nNote: This is a simplified demonstration.")
    print("In production, agents would use LLMs for actual task completion.")

    topic = "Multi-Agent AI Frameworks"

    # Create a simulated result instead of actual execution
    print("\n--- Creating Agents and Tasks ---")
    researcher = create_research_agent()
    writer = create_writer_agent()
    editor = create_editor_agent()

    print("\n--- Defining Workflow ---")
    research_task = create_research_task(researcher, topic)
    writing_task = create_writing_task(writer, research_task)
    editing_task = create_editing_task(editor, writing_task)

    print("\n--- Assembling Crew ---")
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        process=Process.sequential,
        verbose=False,  # Reduced verbosity for demo
    )

    print(
        f"\n✓ Crew assembled with {len(crew.agents)} agents and {len(crew.tasks)} tasks"
    )
    print(f"✓ Process type: {crew.process}")

    print("\n[WORKFLOW SEQUENCE]")
    print("1. Research Agent → Investigates topic")
    print("2. Writer Agent   → Creates article using research")
    print("3. Editor Agent   → Reviews and refines content")

    print("\n" + "=" * 70)
    print("✨ DEMONSTRATION COMPLETE")
    print("=" * 70)

    print("\n[KEY TAKEAWAYS]")
    print("✓ CrewAI uses role-based agents with rich personalities")
    print("✓ Tasks can depend on other tasks for automatic data flow")
    print("✓ Multiple process types support different workflow patterns")
    print("✓ Agent delegation enables hierarchical team structures")
    print("✓ Built-in memory systems maintain context across interactions")

    print("\n[UNIQUE VALUE PROPOSITIONS]")
    print("1. Natural team collaboration metaphor")
    print("2. Rich agent personalities (role/goal/backstory)")
    print("3. Task delegation and hierarchical workflows")
    print("4. Multiple built-in process types")
    print("5. Integrated memory and context management")


if __name__ == "__main__":
    main()
