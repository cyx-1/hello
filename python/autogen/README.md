# AutoGen Python Illustration

This example demonstrates **AutoGen**, a framework for building multi-agent conversational AI systems. AutoGen enables you to create sophisticated applications where multiple AI agents collaborate, communicate, and solve complex problems together through event-driven orchestration.

## Overview

This illustration showcases:
- ✅ Multi-agent collaboration with specialized roles
- ✅ Agent-to-agent communication patterns
- ✅ Event-driven message handling and orchestration
- ✅ Group chat with dynamic speaker selection
- ✅ Code execution and review workflows

## Requirements

- **Python**: >= 3.11
- **PyAutoGen**: >= 0.2.0

## Installation

```bash
uv sync
```

## Running the Example

```bash
uv run python main_autogen.py
```

---

## Source Code with Annotations

### 1. Configuration Setup (Lines 62-89)

The first step is configuring the LLM settings that all agents will use to power their AI capabilities.

```python
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
```

**Key Concept**: The `llm_config` dictionary specifies which LLM model to use, API credentials, and generation parameters like temperature.

**Output Correlation**: See "CONFIGURING LLM SETTINGS" section in the execution output.

---

### 2. Creating Multi-Agent System (Lines 93-161)

AutoGen allows you to create different types of agents with specialized roles and capabilities.

#### UserProxyAgent (Lines 104-120)

```python
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
print(f"    Role: User proxy with code execution")
print(f"    Auto-reply limit: {user_proxy.max_consecutive_auto_reply}")
```

**Key Features**:
- Can execute Python code automatically
- Represents the user in conversations
- Has configurable auto-reply limits
- Detects termination messages

**Output Line**: `✓ Created: UserProxy`

---

#### AssistantAgent (Lines 122-131)

```python
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
```

**Key Features**:
- General-purpose AI assistant
- Powered by the configured LLM
- Can coordinate with other agents

**Output Line**: `✓ Created: Assistant`

---

#### Specialized Agents (Lines 133-161)

```python
# Agent 3: Specialized Coder Agent
print("\n[Agent 3: Coder]")
coder = autogen.AssistantAgent(
    name="Coder",
    system_message="""You are an expert programmer. You write clean, efficient code
    and explain your implementations. Focus on writing Python code that solves problems.
    Reply TERMINATE when the coding task is complete.""",
    llm_config=llm_config,
)

# Agent 4: Specialized Code Reviewer Agent
print("\n[Agent 4: Reviewer]")
reviewer = autogen.AssistantAgent(
    name="Reviewer",
    system_message="""You are a code review expert. You analyze code for correctness,
    efficiency, and best practices. Provide constructive feedback and suggest improvements.
    Reply TERMINATE when the review is complete.""",
    llm_config=llm_config,
)

# Agent 5: Project Manager Agent
print("\n[Agent 5: Manager]")
manager = autogen.AssistantAgent(
    name="Manager",
    system_message="""You are a project manager. You coordinate between team members,
    ensure tasks are completed properly, and make final decisions. You facilitate
    collaboration between the Coder and Reviewer. Reply TERMINATE when satisfied.""",
    llm_config=llm_config,
)
```

**Agent Specialization**:
- **Coder**: Expert at writing code
- **Reviewer**: Analyzes and reviews code
- **Manager**: Coordinates team collaboration

**Output**: Shows all 5 agents being created with their specialized roles.

---

### 3. Two-Agent Conversation Pattern (Lines 166-222)

The simplest multi-agent pattern: two agents communicating back and forth.

```python
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
    # ... code generation and execution ...
```

**Conversation Flow**:
1. UserProxy sends task to Assistant
2. Assistant generates code solution
3. UserProxy executes the code
4. UserProxy reports result back
5. Assistant acknowledges completion

**Output Section**: "EXAMPLE 1: TWO-AGENT CONVERSATION" showing the complete interaction.

---

### 4. Multi-Agent Group Chat (Lines 226-321)

Group chat enables multiple agents to collaborate on complex tasks with dynamic coordination.

#### Group Chat Setup (Lines 249-269)

```python
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
chat_manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=get_llm_config(),
)
print("  ✓ Group chat manager initialized")
```

**Key Parameters**:
- `agents`: List of participating agents
- `max_round`: Maximum conversation rounds
- `speaker_selection_method`: How to choose next speaker
  - `"round_robin"`: Fixed rotation
  - `"auto"`: AI-driven selection
  - Custom function: Your own logic

**Output Lines 169-176**: Shows group chat configuration.

---

#### Collaborative Task Execution (Lines 277-321)

The group chat demonstrates a real software development workflow:

```python
# Define a collaborative task
task = """Create a Python function that finds all prime numbers up to a given limit using
the Sieve of Eratosthenes algorithm. The Reviewer should check the implementation for
correctness and efficiency."""
```

**Execution Flow**:

1. **Round 1 - Manager assigns task**: (Output line 183-185)
   ```
   Manager: Let's work on this task: [task description]
   Manager: Coder, please implement the function.
   ```

2. **Round 2 - Coder implements**: (Output lines 187-205)
   ```python
   def sieve_of_eratosthenes(limit):
       '''Find all prime numbers up to limit using Sieve of Eratosthenes.'''
       if limit < 2:
           return []
       # ... implementation ...
   ```

3. **Round 3 - Reviewer analyzes**: (Output lines 207-216)
   ```
   Reviewer: Analyzing the code...
   Review findings:
     ✓ Algorithm correctly implements Sieve of Eratosthenes
     ✓ Time complexity: O(n log log n) - optimal
     ✓ Space complexity: O(n) - necessary
     ✓ Edge case handling: Correctly handles limit < 2
     ✓ Code style: Clean and well-documented
   ```

4. **Round 4 - Manager requests testing**: (Output lines 218-219)
   ```
   Manager: Great work team! Let's test the function.
   Manager: UserProxy, please execute the code with limit=30.
   ```

5. **Round 5 - UserProxy executes**: (Output lines 221-229)
   ```
   UserProxy: Executing test...
   Execution result:
   Primes up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
   ```

6. **Round 6 - Manager concludes**: (Output lines 231-233)
   ```
   Manager: Perfect! The code works correctly.
   Manager: Task completed successfully. TERMINATE
   ```

**Key Observation**: Each agent plays its specialized role, demonstrating effective multi-agent collaboration.

---

### 5. Event-Driven Orchestration Patterns (Lines 325-400)

AutoGen supports various event-driven patterns for flexible agent coordination.

#### Pattern 1: Message Broadcasting (Lines 341-352)

```python
print("[Pattern 1: Message Broadcasting]")
print("Description: One agent sends a message to multiple recipients")
print("\nFlow:")
print("  Coordinator: 'Starting new task batch'")
print("    ↓")
print("  ├─→ Agent A: Receives broadcast, acknowledges")
print("  ├─→ Agent B: Receives broadcast, acknowledges")
print("  └─→ Agent C: Receives broadcast, acknowledges")
```

**Use Case**: Notifying all agents simultaneously about events or updates.

**Output Lines 240-249**: Shows the broadcast pattern visualization.

---

#### Pattern 2: Sequential Processing Pipeline (Lines 354-366)

```python
print("[Pattern 2: Sequential Processing Pipeline]")
print("Description: Messages flow through agents in sequence")
print("\nFlow:")
print("  Agent A (Data Collector)")
print("    ↓ [passes data]")
print("  Agent B (Data Processor)")
print("    ↓ [passes results]")
print("  Agent C (Data Validator)")
print("    ↓ [passes validated results]")
print("  Agent D (Reporter)")
```

**Use Case**: ETL workflows, data processing chains, validation pipelines.

**Output Lines 251-262**: Shows the sequential pipeline pattern.

---

#### Pattern 3: Conditional Message Routing (Lines 368-381)

```python
print("[Pattern 3: Conditional Message Routing]")
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
```

**Use Case**: Smart routing based on message content or context.

**Output Lines 264-276**: Shows the conditional routing pattern.

---

#### Pattern 4: Request-Response with Timeout (Lines 383-395)

```python
print("[Pattern 4: Request-Response with Timeout]")
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
```

**Use Case**: Asynchronous communication with reliability guarantees.

**Output Lines 278-290**: Shows the request-response pattern.

---

#### Pattern 5: Publish-Subscribe Event System (Lines 397-409)

```python
print("[Pattern 5: Publish-Subscribe Event System]")
print("Description: Agents subscribe to events and react accordingly")
print("\nEvent: 'CodeCommitted'")
print("  ↓")
print("  Subscribers notified:")
print("  ├─→ TestRunner: Runs automated tests")
print("  ├─→ BuildAgent: Triggers new build")
print("  ├─→ NotificationAgent: Sends team notification")
print("  └─→ AnalyticsAgent: Updates metrics")
```

**Use Case**: Decoupled event-driven architecture, CI/CD pipelines.

**Output Lines 292-303**: Shows the pub-sub pattern.

---

### 6. Collaboration Patterns Summary (Lines 413-455)

The illustration concludes with a summary of key multi-agent collaboration patterns:

```python
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
```

**Output Lines 308-330**: Complete pattern summary with use cases.

---

## Complete Program Output

Below is the full output from running the program, showing all examples in action.

```
======================================================================
🤖 AUTOGEN MULTI-AGENT SYSTEM DEMONSTRATION
======================================================================

AutoGen: A framework for building multi-agent conversational AI systems
Version: Compatible with pyautogen >= 0.2.0

Key Features Demonstrated:
  • Multi-agent collaboration with specialized roles
  • Agent-to-agent communication patterns
  • Event-driven message orchestration
  • Group chat with dynamic coordination
  • Code execution and review workflows

======================================================================
CONFIGURING LLM SETTINGS
======================================================================
✓ LLM configuration created
  Model: gpt-4
  Temperature: 0.7

======================================================================
CREATING MULTI-AGENT SYSTEM
======================================================================

[Agent 1: User Proxy]
  ✓ Created: UserProxy
    Role: User proxy with code execution
    Auto-reply limit: 5

[Agent 2: Assistant]
  ✓ Created: Assistant
    Role: General purpose assistant

[Agent 3: Coder]
  ✓ Created: Coder
    Role: Specialized coding agent

[Agent 4: Reviewer]
  ✓ Created: Reviewer
    Role: Code review specialist

[Agent 5: Manager]
  ✓ Created: Manager
    Role: Project coordination and management

✓ All agents created successfully!

======================================================================
EXAMPLE 1: TWO-AGENT CONVERSATION
======================================================================

Pattern: User Proxy ←→ Assistant
Use case: Simple task delegation and execution

Task: Calculate the sum of numbers from 1 to 100 using Python.
    Show me the code and the result.

----------------------------------------------------------------------
Starting conversation...
----------------------------------------------------------------------

[UserProxy → Assistant]
Message: Calculate the sum of numbers from 1 to 100 using Python.
    Show me the code and the result.

[Assistant → UserProxy]
Message: I'll help you calculate the sum of numbers from 1 to 100.
Code:
```python
# Calculate sum of numbers from 1 to 100
total = sum(range(1, 101))
print(f'The sum of numbers from 1 to 100 is: {total}')
```

[UserProxy - Code Execution]
Executing code...
Output: The sum of numbers from 1 to 100 is: 5050

[UserProxy → Assistant]
Message: Code executed successfully. Result: 5050

[Assistant → UserProxy]
Message: Perfect! The calculation is complete. TERMINATE

======================================================================
✓ Two-agent conversation completed
======================================================================

======================================================================
EXAMPLE 2: MULTI-AGENT GROUP CHAT
======================================================================

Pattern: Manager coordinates Coder and Reviewer
Use case: Collaborative software development with review process

[Setting up Group Chat]
  ✓ Group chat created with 4 agents
  ✓ Max rounds: 10
  ✓ Speaker selection: round_robin

[Creating Group Chat Manager]
======================================================================
CONFIGURING LLM SETTINGS
======================================================================
✓ LLM configuration created
  Model: gpt-4
  Temperature: 0.7
  ✓ Group chat manager initialized

Task: Create a Python function that finds all prime numbers up to a given limit using
    the Sieve of Eratosthenes algorithm. The Reviewer should check the implementation for
    correctness and efficiency.

----------------------------------------------------------------------
Starting group conversation...
----------------------------------------------------------------------

[Round 1 - Manager speaks]
Manager: Let's work on this task: Create a Python function that finds all prime numbers up to a given limit using
    the Sieve of Eratosthenes algorithm. The Reviewer should check the implementation for
    correctness and efficiency.
Manager: Coder, please implement the function.

[Round 2 - Coder speaks]
Coder: I'll implement the Sieve of Eratosthenes algorithm.

Code:
```python
def sieve_of_eratosthenes(limit):
    '''Find all prime numbers up to limit using Sieve of Eratosthenes.'''
    if limit < 2:
        return []

    # Initialize boolean array
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # Sieve algorithm
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    # Collect primes
    return [num for num in range(limit + 1) if is_prime[num]]
```

Coder: Implementation complete. Reviewer, please check.

[Round 3 - Reviewer speaks]
Reviewer: Analyzing the code...

Review findings:
  ✓ Algorithm correctly implements Sieve of Eratosthenes
  ✓ Time complexity: O(n log log n) - optimal for this problem
  ✓ Space complexity: O(n) - necessary for the sieve
  ✓ Edge case handling: Correctly handles limit < 2
  ✓ Code style: Clean and well-documented

Reviewer: The implementation is excellent! I approve this code.

[Round 4 - Manager speaks]
Manager: Great work team! Let's test the function.
Manager: UserProxy, please execute the code with limit=30.

[Round 5 - UserProxy executes]
UserProxy: Executing test...

Test code:
```python
primes = sieve_of_eratosthenes(30)
print(f'Primes up to 30: {primes}')
```

Execution result:
Primes up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

[Round 6 - Manager speaks]
Manager: Perfect! The code works correctly.
Manager: Task completed successfully. TERMINATE

======================================================================
✓ Group chat demonstration completed
======================================================================

======================================================================
EXAMPLE 3: EVENT-DRIVEN ORCHESTRATION
======================================================================

Demonstrating message-driven agent interactions

[Pattern 1: Message Broadcasting]
Description: One agent sends a message to multiple recipients

Flow:
  Coordinator: 'Starting new task batch'
    ↓
  ├─→ Agent A: Receives broadcast, acknowledges
  ├─→ Agent B: Receives broadcast, acknowledges
  └─→ Agent C: Receives broadcast, acknowledges

✓ All agents notified simultaneously

[Pattern 2: Sequential Processing Pipeline]
Description: Messages flow through agents in sequence

Flow:
  Agent A (Data Collector)
    ↓ [passes data]
  Agent B (Data Processor)
    ↓ [passes results]
  Agent C (Data Validator)
    ↓ [passes validated results]
  Agent D (Reporter)

✓ Each agent processes and forwards to next

[Pattern 3: Conditional Message Routing]
Description: Router agent directs messages based on content

Flow:
  Router Agent receives message
    ↓
  [Analyzes message type]
    ↓
  ├─→ If 'bug report' → BugTriageAgent
  ├─→ If 'feature request' → ProductAgent
  ├─→ If 'question' → SupportAgent
  └─→ If 'code review' → ReviewerAgent

✓ Dynamic routing based on message content

[Pattern 4: Request-Response with Timeout]
Description: Agent waits for response with timeout handling

Flow:
  Agent A: Sends request
  Agent A: Waits for response (timeout: 30s)
    ↓
  Agent B: Processes request
  Agent B: Sends response
    ↓
  Agent A: Receives response within timeout
  Agent A: Continues processing

✓ Handles async communication with timeout protection

[Pattern 5: Publish-Subscribe Event System]
Description: Agents subscribe to events and react accordingly

Event: 'CodeCommitted'
  ↓
  Subscribers notified:
  ├─→ TestRunner: Runs automated tests
  ├─→ BuildAgent: Triggers new build
  ├─→ NotificationAgent: Sends team notification
  └─→ AnalyticsAgent: Updates metrics

✓ Decoupled event-driven architecture

======================================================================
✓ Event-driven patterns demonstrated
======================================================================

======================================================================
MULTI-AGENT COLLABORATION PATTERNS SUMMARY
======================================================================

1. Two-Agent Chat
   Description: Simple back-and-forth between two agents
   Use Case: Task delegation, Q&A, simple workflows
   Complexity: Low

2. Group Chat
   Description: Multiple agents in round-robin or auto-selected conversation
   Use Case: Team collaboration, complex problem solving
   Complexity: Medium

3. Sequential Chain
   Description: Agents process in fixed order like a pipeline
   Use Case: Data processing, ETL, validation chains
   Complexity: Medium

4. Hierarchical
   Description: Manager agent coordinates subordinate agents
   Use Case: Project management, task decomposition
   Complexity: High

5. Nested Chat
   Description: Agents can initiate sub-conversations
   Use Case: Complex problem decomposition, recursive tasks
   Complexity: High

======================================================================

======================================================================
✨ DEMONSTRATION COMPLETE
======================================================================

Key Takeaways:
  1. Multiple agents can work together on complex tasks
  2. Agents have specialized roles and capabilities
  3. Communication can be two-way, group-based, or event-driven
  4. Group chats enable dynamic multi-agent collaboration
  5. Event-driven patterns provide flexible orchestration

AutoGen enables building sophisticated multi-agent systems
for AI-powered automation and collaboration!
======================================================================
```

---

## Key Concepts Illustrated

### 1. **Multi-Agent Collaboration**
- Multiple agents with specialized roles work together
- Each agent has distinct capabilities (coding, reviewing, managing)
- Agents communicate through structured message passing
- Collaboration patterns from simple (2-agent) to complex (group chat)

### 2. **Agent Types**
- **UserProxyAgent**: Represents the user, can execute code
- **AssistantAgent**: AI-powered agents with specialized system prompts
- **GroupChatManager**: Coordinates multi-agent conversations

### 3. **Event-Driven Orchestration**
- **Message Broadcasting**: One-to-many communication
- **Sequential Pipeline**: Ordered processing chain
- **Conditional Routing**: Dynamic path selection
- **Request-Response**: Async communication with timeouts
- **Pub-Sub**: Event-driven architecture

### 4. **Speaker Selection Methods**
- **round_robin**: Fixed rotation through agents
- **auto**: AI-driven selection based on context
- **custom**: User-defined selection logic

### 5. **Termination Handling**
- Agents signal completion with "TERMINATE" message
- Conversation can end naturally or after max rounds
- Supports graceful shutdown of multi-agent workflows

---

## Common Use Cases

AutoGen is particularly useful for:

- **Software Development**: Code generation, review, and testing workflows
- **Research Automation**: Literature review, data analysis, report generation
- **Customer Support**: Multi-tier support with specialized agents
- **Data Processing**: ETL pipelines with validation and quality checks
- **Decision Making**: Multi-perspective analysis and consensus building
- **Education**: Tutoring systems with different teaching approaches
- **Creative Projects**: Collaborative content creation and editing

---

## Advanced Features (Not Shown in This Example)

AutoGen also supports:

- **Human-in-the-Loop**: Interactive conversations with real users
- **Function Calling**: Agents can call external tools and APIs
- **Nested Chats**: Agents starting sub-conversations
- **Custom Selection**: Complex logic for choosing next speaker
- **State Management**: Persistent conversation state across sessions
- **Async Execution**: Non-blocking agent operations

---

## Production Considerations

When deploying AutoGen in production:

1. **Security**:
   - Enable Docker for code execution (`use_docker=True`)
   - Validate and sanitize all code before execution
   - Use proper API key management

2. **LLM Configuration**:
   - Use actual API keys from OpenAI, Azure, or other providers
   - Configure appropriate rate limits and timeouts
   - Monitor token usage and costs

3. **Error Handling**:
   - Implement robust error recovery
   - Set reasonable max_consecutive_auto_reply limits
   - Handle network failures and API errors

4. **Logging and Monitoring**:
   - Log all agent conversations
   - Track performance metrics
   - Monitor for infinite loops or runaway conversations

---

## Additional Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [AutoGen GitHub](https://github.com/microsoft/autogen)
- [AutoGen Examples](https://github.com/microsoft/autogen/tree/main/notebook)
- [Research Paper](https://arxiv.org/abs/2308.08155)

---

## Version Requirements

This example requires:
- **Python 3.11+**: Uses modern type hints and features
- **PyAutoGen 0.2.0+**: Compatible with the latest API
- **Optional**: Docker for safe code execution in production

**Note**: This illustration uses simulated agents for demonstration purposes. In production, you would configure actual LLM API keys (OpenAI, Azure OpenAI, etc.) to enable real AI-powered agent conversations.

The code demonstrates AutoGen's core concepts and patterns that remain stable across versions, making it a reliable foundation for building multi-agent systems.
