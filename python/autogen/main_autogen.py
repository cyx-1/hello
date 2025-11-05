# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pyautogen>=0.2.0",
# ]
# ///
"""
AutoGen Example: Multi-Agent Collaboration and Event-Driven Orchestration

This example showcases key AutoGen concepts:
1. Multiple agents with different roles and capabilities
2. Agent-to-agent communication and collaboration
3. Event-driven message handling and orchestration
4. Group chat with dynamic speaker selection
5. Conversational AI patterns with human-in-the-loop

Note: This is a conceptual demonstration. In production, you would configure
actual LLM API keys and use real agent interactions.
"""

# For demonstration purposes, we'll create simplified agent classes
# In production, you would use: import autogen
try:
    import autogen

    AUTOGEN_AVAILABLE = True
except ImportError:
    AUTOGEN_AVAILABLE = False

    # Create mock classes for demonstration
    class MockAgent:
        def __init__(self, name, **kwargs):
            self.name = name
            self.system_message = kwargs.get("system_message", "")
            self.max_consecutive_auto_reply = kwargs.get(
                "max_consecutive_auto_reply", 0
            )

    class MockUserProxyAgent(MockAgent):
        pass

    class MockAssistantAgent(MockAgent):
        pass

    class MockGroupChat:
        def __init__(self, agents, messages, max_round, speaker_selection_method):
            self.agents = agents
            self.messages = messages
            self.max_round = max_round
            self.speaker_selection_method = speaker_selection_method

    class MockGroupChatManager:
        def __init__(self, groupchat, llm_config):
            self.groupchat = groupchat
            self.llm_config = llm_config

    # Mock autogen module
    class autogen:
        UserProxyAgent = MockUserProxyAgent
        AssistantAgent = MockAssistantAgent
        GroupChat = MockGroupChat
        GroupChatManager = MockGroupChatManager


# Example 1: Configure LLM settings
# Lines 19-30: Setting up the LLM configuration for all agents
def get_llm_config():
    """
    Returns the LLM configuration for agents.
    In this example, we use a simulated config for demonstration.
    In production, you would configure with actual API keys.
    """
    print("\n" + "=" * 70)
    print("CONFIGURING LLM SETTINGS")
    print("=" * 70)

    # For demonstration, we'll use a config that simulates responses
    # In production, use: config_list=[{"model": "gpt-4", "api_key": "your-key"}]
    config = {
        "config_list": [
            {
                "model": "gpt-4",
                "api_key": "demo-key-for-illustration",
                "api_type": "demo",
            }
        ],
        "timeout": 120,
        "temperature": 0.7,
    }

    print("✓ LLM configuration created")
    print(f"  Model: {config['config_list'][0]['model']}")
    print(f"  Temperature: {config['temperature']}")

    return config


# Example 2: Create different types of agents
# Lines 53-130: Demonstrating various agent types and their configurations
def create_agents(llm_config):
    """
    Creates multiple agents with different roles and capabilities.
    This demonstrates how agents can have specialized functions.
    """
    print("\n" + "=" * 70)
    print("CREATING MULTI-AGENT SYSTEM")
    print("=" * 70)

    # Agent 1: UserProxyAgent - Represents the human user
    # Can execute code and interact with the user
    print("\n[Agent 1: User Proxy]")
    user_proxy = autogen.UserProxyAgent(
        name="UserProxy",
        system_message="A proxy for the user, can execute code and provide feedback.",
        human_input_mode="NEVER",  # For demo, no human input required
        max_consecutive_auto_reply=5,
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False,  # Set to True in production for safety
        },
        is_termination_msg=lambda x: x.get("content", "")
        .rstrip()
        .endswith("TERMINATE"),
    )
    print(f"  ✓ Created: {user_proxy.name}")
    print("    Role: User proxy with code execution")
    print(f"    Auto-reply limit: {user_proxy.max_consecutive_auto_reply}")

    # Agent 2: AssistantAgent - General purpose AI assistant
    print("\n[Agent 2: Assistant]")
    assistant = autogen.AssistantAgent(
        name="Assistant",
        system_message="""You are a helpful AI assistant. You can help with various tasks,
        coordinate with other agents, and provide solutions. Reply TERMINATE when the task is done.""",
        llm_config=llm_config,
    )
    print(f"  ✓ Created: {assistant.name}")
    print("    Role: General purpose assistant")

    # Agent 3: Specialized Coder Agent
    print("\n[Agent 3: Coder]")
    coder = autogen.AssistantAgent(
        name="Coder",
        system_message="""You are an expert programmer. You write clean, efficient code
        and explain your implementations. Focus on writing Python code that solves problems.
        Reply TERMINATE when the coding task is complete.""",
        llm_config=llm_config,
    )
    print(f"  ✓ Created: {coder.name}")
    print("    Role: Specialized coding agent")

    # Agent 4: Specialized Code Reviewer Agent
    print("\n[Agent 4: Reviewer]")
    reviewer = autogen.AssistantAgent(
        name="Reviewer",
        system_message="""You are a code review expert. You analyze code for correctness,
        efficiency, and best practices. Provide constructive feedback and suggest improvements.
        Reply TERMINATE when the review is complete.""",
        llm_config=llm_config,
    )
    print(f"  ✓ Created: {reviewer.name}")
    print("    Role: Code review specialist")

    # Agent 5: Project Manager Agent
    print("\n[Agent 5: Manager]")
    manager = autogen.AssistantAgent(
        name="Manager",
        system_message="""You are a project manager. You coordinate between team members,
        ensure tasks are completed properly, and make final decisions. You facilitate
        collaboration between the Coder and Reviewer. Reply TERMINATE when satisfied.""",
        llm_config=llm_config,
    )
    print(f"  ✓ Created: {manager.name}")
    print("    Role: Project coordination and management")

    print("\n✓ All agents created successfully!")

    return user_proxy, assistant, coder, reviewer, manager


# Example 3: Two-Agent Conversation
# Lines 145-180: Simple two-agent interaction pattern
def demonstrate_two_agent_chat(user_proxy, assistant):
    """
    Demonstrates basic two-agent conversation.
    This is the simplest form of multi-agent interaction.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 1: TWO-AGENT CONVERSATION")
    print("=" * 70)
    print("\nPattern: User Proxy ←→ Assistant")
    print("Use case: Simple task delegation and execution\n")

    # Define a simple task
    task = """Calculate the sum of numbers from 1 to 100 using Python.
    Show me the code and the result."""

    print(f"Task: {task}")
    print("\n" + "-" * 70)
    print("Starting conversation...")
    print("-" * 70)

    # Simulate the conversation flow (in real usage, this would call LLM)
    print("\n[UserProxy → Assistant]")
    print(f"Message: {task}")

    print("\n[Assistant → UserProxy]")
    print("Message: I'll help you calculate the sum of numbers from 1 to 100.")
    print("Code:")
    print("```python")
    print("# Calculate sum of numbers from 1 to 100")
    print("total = sum(range(1, 101))")
    print("print(f'The sum of numbers from 1 to 100 is: {total}')")
    print("```")

    print("\n[UserProxy - Code Execution]")
    print("Executing code...")
    total = sum(range(1, 101))
    print(f"Output: The sum of numbers from 1 to 100 is: {total}")

    print("\n[UserProxy → Assistant]")
    print("Message: Code executed successfully. Result: 5050")

    print("\n[Assistant → UserProxy]")
    print("Message: Perfect! The calculation is complete. TERMINATE")

    print("\n" + "=" * 70)
    print("✓ Two-agent conversation completed")
    print("=" * 70)


# Example 4: Multi-Agent Group Chat
# Lines 196-275: Complex multi-agent collaboration with group chat
def demonstrate_group_chat(user_proxy, coder, reviewer, manager):
    """
    Demonstrates group chat with multiple agents collaborating.
    This shows event-driven orchestration with dynamic speaker selection.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 2: MULTI-AGENT GROUP CHAT")
    print("=" * 70)
    print("\nPattern: Manager coordinates Coder and Reviewer")
    print("Use case: Collaborative software development with review process\n")

    # Create a group chat
    print("[Setting up Group Chat]")
    groupchat = autogen.GroupChat(
        agents=[user_proxy, coder, reviewer, manager],
        messages=[],
        max_round=10,
        speaker_selection_method="round_robin",  # Can also be "auto" or custom
    )
    print(f"  ✓ Group chat created with {len(groupchat.agents)} agents")
    print(f"  ✓ Max rounds: {groupchat.max_round}")
    print(f"  ✓ Speaker selection: {groupchat.speaker_selection_method}")

    # Create a group chat manager
    print("\n[Creating Group Chat Manager]")
    _chat_manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config=get_llm_config(),
    )
    print("  ✓ Group chat manager initialized")

    # Define a collaborative task
    task = """Create a Python function that finds all prime numbers up to a given limit using
    the Sieve of Eratosthenes algorithm. The Reviewer should check the implementation for
    correctness and efficiency."""

    print(f"\nTask: {task}")
    print("\n" + "-" * 70)
    print("Starting group conversation...")
    print("-" * 70)

    # Simulate the multi-agent conversation
    print("\n[Round 1 - Manager speaks]")
    print(f"Manager: Let's work on this task: {task}")
    print("Manager: Coder, please implement the function.")

    print("\n[Round 2 - Coder speaks]")
    print("Coder: I'll implement the Sieve of Eratosthenes algorithm.")
    print("\nCode:")
    print("```python")
    print("def sieve_of_eratosthenes(limit):")
    print("    '''Find all prime numbers up to limit using Sieve of Eratosthenes.'''")
    print("    if limit < 2:")
    print("        return []")
    print("    ")
    print("    # Initialize boolean array")
    print("    is_prime = [True] * (limit + 1)")
    print("    is_prime[0] = is_prime[1] = False")
    print("    ")
    print("    # Sieve algorithm")
    print("    for i in range(2, int(limit**0.5) + 1):")
    print("        if is_prime[i]:")
    print("            for j in range(i*i, limit + 1, i):")
    print("                is_prime[j] = False")
    print("    ")
    print("    # Collect primes")
    print("    return [num for num in range(limit + 1) if is_prime[num]]")
    print("```")
    print("\nCoder: Implementation complete. Reviewer, please check.")

    print("\n[Round 3 - Reviewer speaks]")
    print("Reviewer: Analyzing the code...")
    print("\nReview findings:")
    print("  ✓ Algorithm correctly implements Sieve of Eratosthenes")
    print("  ✓ Time complexity: O(n log log n) - optimal for this problem")
    print("  ✓ Space complexity: O(n) - necessary for the sieve")
    print("  ✓ Edge case handling: Correctly handles limit < 2")
    print("  ✓ Code style: Clean and well-documented")
    print("\nReviewer: The implementation is excellent! I approve this code.")

    print("\n[Round 4 - Manager speaks]")
    print("Manager: Great work team! Let's test the function.")
    print("Manager: UserProxy, please execute the code with limit=30.")

    print("\n[Round 5 - UserProxy executes]")
    print("UserProxy: Executing test...")
    print("\nTest code:")
    print("```python")
    print("primes = sieve_of_eratosthenes(30)")
    print("print(f'Primes up to 30: {primes}')")
    print("```")

    print("\nExecution result:")

    # Actually execute to show real output
    def sieve_of_eratosthenes(limit):
        """Find all prime numbers up to limit using Sieve of Eratosthenes."""
        if limit < 2:
            return []

        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        return [num for num in range(limit + 1) if is_prime[num]]

    primes = sieve_of_eratosthenes(30)
    print(f"Primes up to 30: {primes}")

    print("\n[Round 6 - Manager speaks]")
    print("Manager: Perfect! The code works correctly.")
    print("Manager: Task completed successfully. TERMINATE")

    print("\n" + "=" * 70)
    print("✓ Group chat demonstration completed")
    print("=" * 70)


# Example 5: Event-Driven Message Handling
# Lines 292-340: Demonstrates event-driven patterns in agent communication
def demonstrate_event_driven_patterns():
    """
    Illustrates event-driven orchestration patterns.
    Shows how agents respond to messages and events dynamically.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 3: EVENT-DRIVEN ORCHESTRATION")
    print("=" * 70)
    print("\nDemonstrating message-driven agent interactions\n")

    # Pattern 1: Message Broadcasting
    print("[Pattern 1: Message Broadcasting]")
    print("Description: One agent sends a message to multiple recipients")
    print("\nFlow:")
    print("  Coordinator: 'Starting new task batch'")
    print("    ↓")
    print("  ├─→ Agent A: Receives broadcast, acknowledges")
    print("  ├─→ Agent B: Receives broadcast, acknowledges")
    print("  └─→ Agent C: Receives broadcast, acknowledges")
    print("\n✓ All agents notified simultaneously")

    # Pattern 2: Sequential Processing
    print("\n[Pattern 2: Sequential Processing Pipeline]")
    print("Description: Messages flow through agents in sequence")
    print("\nFlow:")
    print("  Agent A (Data Collector)")
    print("    ↓ [passes data]")
    print("  Agent B (Data Processor)")
    print("    ↓ [passes results]")
    print("  Agent C (Data Validator)")
    print("    ↓ [passes validated results]")
    print("  Agent D (Reporter)")
    print("\n✓ Each agent processes and forwards to next")

    # Pattern 3: Conditional Routing
    print("\n[Pattern 3: Conditional Message Routing]")
    print("Description: Router agent directs messages based on content")
    print("\nFlow:")
    print("  Router Agent receives message")
    print("    ↓")
    print("  [Analyzes message type]")
    print("    ↓")
    print("  ├─→ If 'bug report' → BugTriageAgent")
    print("  ├─→ If 'feature request' → ProductAgent")
    print("  ├─→ If 'question' → SupportAgent")
    print("  └─→ If 'code review' → ReviewerAgent")
    print("\n✓ Dynamic routing based on message content")

    # Pattern 4: Request-Response with Timeout
    print("\n[Pattern 4: Request-Response with Timeout]")
    print("Description: Agent waits for response with timeout handling")
    print("\nFlow:")
    print("  Agent A: Sends request")
    print("  Agent A: Waits for response (timeout: 30s)")
    print("    ↓")
    print("  Agent B: Processes request")
    print("  Agent B: Sends response")
    print("    ↓")
    print("  Agent A: Receives response within timeout")
    print("  Agent A: Continues processing")
    print("\n✓ Handles async communication with timeout protection")

    # Pattern 5: Pub-Sub Event System
    print("\n[Pattern 5: Publish-Subscribe Event System]")
    print("Description: Agents subscribe to events and react accordingly")
    print("\nEvent: 'CodeCommitted'")
    print("  ↓")
    print("  Subscribers notified:")
    print("  ├─→ TestRunner: Runs automated tests")
    print("  ├─→ BuildAgent: Triggers new build")
    print("  ├─→ NotificationAgent: Sends team notification")
    print("  └─→ AnalyticsAgent: Updates metrics")
    print("\n✓ Decoupled event-driven architecture")

    print("\n" + "=" * 70)
    print("✓ Event-driven patterns demonstrated")
    print("=" * 70)


# Example 6: Agent Collaboration Patterns Summary
# Lines 358-395: Overview of collaboration patterns
def summarize_collaboration_patterns():
    """
    Summarizes key multi-agent collaboration patterns.
    """
    print("\n" + "=" * 70)
    print("MULTI-AGENT COLLABORATION PATTERNS SUMMARY")
    print("=" * 70)

    patterns = [
        {
            "name": "Two-Agent Chat",
            "description": "Simple back-and-forth between two agents",
            "use_case": "Task delegation, Q&A, simple workflows",
            "complexity": "Low",
        },
        {
            "name": "Group Chat",
            "description": "Multiple agents in round-robin or auto-selected conversation",
            "use_case": "Team collaboration, complex problem solving",
            "complexity": "Medium",
        },
        {
            "name": "Sequential Chain",
            "description": "Agents process in fixed order like a pipeline",
            "use_case": "Data processing, ETL, validation chains",
            "complexity": "Medium",
        },
        {
            "name": "Hierarchical",
            "description": "Manager agent coordinates subordinate agents",
            "use_case": "Project management, task decomposition",
            "complexity": "High",
        },
        {
            "name": "Nested Chat",
            "description": "Agents can initiate sub-conversations",
            "use_case": "Complex problem decomposition, recursive tasks",
            "complexity": "High",
        },
    ]

    for i, pattern in enumerate(patterns, 1):
        print(f"\n{i}. {pattern['name']}")
        print(f"   Description: {pattern['description']}")
        print(f"   Use Case: {pattern['use_case']}")
        print(f"   Complexity: {pattern['complexity']}")

    print("\n" + "=" * 70)


# Main execution
def main():
    """Main entry point for the AutoGen demonstration."""
    print("=" * 70)
    print("🤖 AUTOGEN MULTI-AGENT SYSTEM DEMONSTRATION")
    print("=" * 70)
    print("\nAutoGen: A framework for building multi-agent conversational AI systems")
    print("Version: Compatible with pyautogen >= 0.2.0")
    print("\nKey Features Demonstrated:")
    print("  • Multi-agent collaboration with specialized roles")
    print("  • Agent-to-agent communication patterns")
    print("  • Event-driven message orchestration")
    print("  • Group chat with dynamic coordination")
    print("  • Code execution and review workflows")

    # Get LLM configuration
    llm_config = get_llm_config()

    # Create agents
    user_proxy, assistant, coder, reviewer, manager = create_agents(llm_config)

    # Example 1: Two-agent conversation
    demonstrate_two_agent_chat(user_proxy, assistant)

    # Example 2: Multi-agent group chat
    demonstrate_group_chat(user_proxy, coder, reviewer, manager)

    # Example 3: Event-driven patterns
    demonstrate_event_driven_patterns()

    # Summary
    summarize_collaboration_patterns()

    print("\n" + "=" * 70)
    print("✨ DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  1. Multiple agents can work together on complex tasks")
    print("  2. Agents have specialized roles and capabilities")
    print("  3. Communication can be two-way, group-based, or event-driven")
    print("  4. Group chats enable dynamic multi-agent collaboration")
    print("  5. Event-driven patterns provide flexible orchestration")
    print("\nAutoGen enables building sophisticated multi-agent systems")
    print("for AI-powered automation and collaboration!")
    print("=" * 70)


if __name__ == "__main__":
    main()
