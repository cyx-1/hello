# Microsoft Agent Framework Illustration

## Overview

This example demonstrates **Microsoft Agent Framework**, the unified successor to both **AutoGen** and **Semantic Kernel**. The framework combines AutoGen's dynamic multi-agent orchestration with Semantic Kernel's enterprise-grade features, providing a production-ready platform for building AI agents with support for multiple LLM providers.

**Released:** October 2025 (Public Preview)
**Requires:** Python 3.11+

## Key Features Illustrated

### From AutoGen:
- ✅ Multi-agent orchestration and collaboration
- ✅ Dynamic agent-to-agent communication
- ✅ Group chat patterns for complex problem solving
- ✅ Flexible, LLM-driven agent behavior

### From Semantic Kernel:
- ✅ Type-safe function calling and tool integration
- ✅ Enterprise-grade telemetry and observability
- ✅ Thread-based state management
- ✅ Production-ready filters and middleware

### Multi-LLM Provider Support:
- ✅ OpenAI (GPT-4, GPT-3.5, etc.)
- ✅ Azure OpenAI Service
- ✅ Azure AI Foundry models (Llama, Mistral, etc.)
- ✅ Ollama for local models
- ✅ Google Gemini
- ✅ Semantic Kernel adapter for existing SK clients

## Installation

Dependencies are specified using inline script metadata in the Python file.
No separate installation needed - `uv` will handle dependencies automatically.

## Running the Example

```bash
# Using uv (handles dependencies automatically)
uv run main_microsoft_agent_framework.py

# Or with standard Python (after installing dependencies)
python main_microsoft_agent_framework.py
```

**Note:** For live API demonstrations, set `OPENAI_API_KEY` environment variable. The script runs successfully without it, showing code examples and expected outputs.

---

## Source Code with Line Numbers

### 1. Script Metadata (Lines 1-10)

```python
1  #!/usr/bin/env python3
2  # /// script
3  # requires-python = ">=3.11"
4  # dependencies = [
5  #     "agent-framework>=0.1.0",
6  #     "agent-framework-azure-ai>=0.1.0",
7  #     "openai>=1.0.0",
8  #     "azure-identity>=1.18.0",
9  # ]
10 # ///
```

**Annotation:** Uses PEP 723 inline script metadata for dependency management with `uv`. No `pyproject.toml` required.

---

### 2. Framework Overview (Lines 22-52)

```python
22 def demonstrate_framework_overview():
23     """Display overview of Microsoft Agent Framework features."""
24     print("=" * 80)
25     print("MICROSOFT AGENT FRAMEWORK - UNIFIED AI AGENT DEVELOPMENT")
26     print("=" * 80)
27     print()
28     print("The Microsoft Agent Framework combines the best of both worlds:")
29     print()
30     print("FROM AUTOGEN:")
31     print("  • Multi-agent orchestration and collaboration")
32     print("  • Dynamic agent-to-agent communication")
33     print("  • Group chat patterns for complex problem solving")
34     print("  • Flexible, LLM-driven agent behavior")
35     print()
36     print("FROM SEMANTIC KERNEL:")
37     print("  • Type-safe function calling and tool integration")
38     print("  • Enterprise-grade telemetry and observability")
39     print("  • State management with threads")
40     print("  • Production-ready filters and middleware")
41     print()
42     print("MULTI-LLM PROVIDER SUPPORT:")
43     print("  • OpenAI (GPT-4, GPT-3.5, etc.)")
44     print("  • Azure OpenAI Service")
45     print("  • Azure AI Foundry models")
46     print("  • Ollama for local models")
47     print("  • Google Gemini")
48     print("  • Semantic Kernel adapter for SK model clients")
49     print()
50     print("=" * 80)
51     print()
```

**Output (Lines 1-24):**
```
================================================================================
MICROSOFT AGENT FRAMEWORK - UNIFIED AI AGENT DEVELOPMENT
================================================================================

The Microsoft Agent Framework combines the best of both worlds:

FROM AUTOGEN:
  • Multi-agent orchestration and collaboration
  • Dynamic agent-to-agent communication
  • Group chat patterns for complex problem solving
  • Flexible, LLM-driven agent behavior

FROM SEMANTIC KERNEL:
  • Type-safe function calling and tool integration
  • Enterprise-grade telemetry and observability
  • State management with threads
  • Production-ready filters and middleware

MULTI-LLM PROVIDER SUPPORT:
  • OpenAI (GPT-4, GPT-3.5, etc.)
  • Azure OpenAI Service
  • Azure AI Foundry models
  • Ollama for local models
  • Google Gemini
  • Semantic Kernel adapter for SK model clients

================================================================================
```

**Annotation:** The framework unifies two major Microsoft AI frameworks into a single, production-ready solution.

---

### 3. Basic Agent Creation (Lines 55-108) - AutoGen Style

```python
55  async def demonstrate_basic_agent():
56      """
57      Demonstrate basic agent creation and execution.
58
59      This showcases the simple, AutoGen-style agent interface.
60      """
61      print("\n" + "=" * 80)
62      print("EXAMPLE 1: BASIC AGENT CREATION (AutoGen-style simplicity)")
63      print("=" * 80)
64      print()
...
85      # Line 85: Create a chat client with OpenAI
86      client = OpenAIChatClient(
87          model="gpt-4",
88          api_key=os.getenv("OPENAI_API_KEY")
89      )
90
91      # Line 91: Create an agent with specific instructions
92      agent = client.create_agent(
93          name="DataAnalyst",
94          instructions="You are an expert data analyst specialized in Python."
95      )
96
97      # Line 97: Run the agent with a task
98      result = await agent.run("Explain what pandas DataFrame is in 2 sentences.")
99      print(result.text)
```

**Output (Lines 27-41):**
```
================================================================================
EXAMPLE 1: BASIC AGENT CREATION (AutoGen-style simplicity)
================================================================================

⚠️  Note: OPENAI_API_KEY not set. Using mock example.

Code example:
----------------------------------------
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient

# Line 85: Create a chat client with OpenAI
client = OpenAIChatClient(
    model="gpt-4",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Line 91: Create an agent with specific instructions
agent = client.create_agent(
    name="DataAnalyst",
    instructions="You are an expert data analyst specialized in Python."
)

# Line 97: Run the agent with a task
result = await agent.run("Explain what pandas DataFrame is in 2 sentences.")
print(result.text)
```

**Annotation:** Simple three-step agent creation inherited from AutoGen: (1) create client, (2) create agent with instructions, (3) run with task. The API is intuitive and minimal.

---

### 4. Multi-LLM Provider Support (Lines 111-200)

```python
152     # Line 152: OpenAI client
153     openai_client = OpenAIChatClient(
154         model="gpt-4o",
155         api_key=os.getenv("OPENAI_API_KEY")
156     )
157     agent = openai_client.create_agent(name="Assistant")
```

**Output (Lines 47-60):**
```
1. OPENAI PROVIDER:
----------------------------------------
from agent_framework.openai import OpenAIChatClient

# Line 152: OpenAI client
openai_client = OpenAIChatClient(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")
)
agent = openai_client.create_agent(name="Assistant")

2. AZURE OPENAI PROVIDER:
----------------------------------------
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import DefaultAzureCredential

# Line 165: Azure OpenAI with managed identity
azure_client = AzureOpenAIChatClient(
    endpoint="https://your-resource.openai.azure.com/",
    credential=DefaultAzureCredential(),
    deployment="gpt-4"
)
agent = azure_client.create_agent(name="AzureAssistant")

3. AZURE AI FOUNDRY (Multiple Models):
----------------------------------------
from agent_framework.azure import AzureAIFoundryChatClient

# Line 179: Azure AI with various models (Llama, Mistral, etc.)
foundry_client = AzureAIFoundryChatClient(
    endpoint="https://your-foundry.inference.ai.azure.com",
    credential=DefaultAzureCredential(),
    model="Llama-3-70B-Instruct"
)
agent = foundry_client.create_agent(name="FoundryAssistant")

4. SEMANTIC KERNEL ADAPTER:
----------------------------------------
from agent_framework.semantic_kernel import SemanticKernelAdapter
from semantic_kernel import ChatCompletionClientBase

# Line 193: Use any Semantic Kernel model client
sk_client = ... # Any SK ChatCompletionClientBase
adapter = SemanticKernelAdapter(sk_client)
agent = adapter.create_agent(name="SKAssistant")

✓ All providers use the same Agent interface!
```

**Annotation:** The framework provides a unified interface across multiple LLM providers:
- **OpenAI**: Direct integration with OpenAI API
- **Azure OpenAI**: Enterprise deployment with managed identity
- **Azure AI Foundry**: Access to open-source models (Llama, Mistral, Phi, etc.)
- **Semantic Kernel Adapter**: Use existing SK model clients

All providers expose the same `.create_agent()` API, making it easy to switch providers without code changes.

---

### 5. Tools & Function Calling (Lines 203-290) - Semantic Kernel Feature

```python
217     # Define tools with type annotations (SK-style)
218     def get_weather(
219         location: Annotated[str, "The city and state, e.g. San Francisco, CA"]
220     ) -> str:
221         """Get the current weather for a location."""
222         # Mock implementation
223         return f"Weather in {location}: Sunny, 72°F"
224
225     def calculate_sum(
226         a: Annotated[float, "First number"],
227         b: Annotated[float, "Second number"]
228     ) -> float:
229         """Calculate the sum of two numbers."""
230         return a + b
...
260             # Line 260: Register tools with the agent
261             agent = client.create_agent(
262                 name="ToolUser",
263                 instructions="You are a helpful assistant that can use tools.",
264                 tools=[get_weather, calculate_sum]
265             )
```

**Output (Lines 82-105):**
```
================================================================================
EXAMPLE 3: TOOLS & FUNCTION CALLING (Semantic Kernel feature)
================================================================================

Tools defined with type annotations (Semantic Kernel style):
----------------------------------------
def get_weather(
    location: Annotated[str, "The city and state, e.g. San Francisco, CA"]
) -> str:
    '''Get the current weather for a location.'''
    return f"Weather in {location}: Sunny, 72°F"

def calculate_sum(
    a: Annotated[float, "First number"],
    b: Annotated[float, "Second number"]
) -> float:
    '''Calculate the sum of two numbers.'''
    return a + b

Code example for registering tools:
----------------------------------------
agent = client.create_agent(
    name="ToolUser",
    instructions="You are a helpful assistant.",
    tools=[get_weather, calculate_sum]  # Line 297: Register tools
)

result = await agent.run("What's the weather in Seattle?")
# Agent automatically calls the appropriate tool
```

**Annotation:** Type-safe function calling is a key Semantic Kernel feature:
- Functions use `Annotated` types for parameter descriptions
- Docstrings provide function descriptions to the LLM
- Tools are registered directly with the agent
- The agent automatically determines when to call tools based on user input
- Return values are type-safe and validated

This provides better IDE support and runtime type checking compared to AutoGen's looser function definitions.

---

### 6. Multi-Agent Orchestration (Lines 293-368) - AutoGen Feature

```python
322     # Line 322: Define multiple specialized agents
323     researcher = client.create_agent(
324         name="Researcher",
325         instructions="Research and analyze requirements. Be thorough."
326     )
327
328     architect = client.create_agent(
329         name="Architect",
330         instructions="Design system architecture. Focus on scalability."
331     )
332
333     developer = client.create_agent(
334         name="Developer",
335         instructions="Write code implementations. Follow best practices."
336     )
337
338     reviewer = client.create_agent(
339         name="Reviewer",
340         instructions="Review code for bugs and improvements."
341     )
342
343     # Line 343: Create a workflow with agent handoffs
344     from agent_framework import Workflow, Step
345
346     workflow = Workflow(
347         steps=[
348             Step(agent=researcher, output="requirements"),
349             Step(agent=architect, input="requirements", output="design"),
350             Step(agent=developer, input="design", output="code"),
351             Step(agent=reviewer, input="code", output="review")
352         ]
353     )
354
355     # Line 355: Execute the workflow
356     result = await workflow.run("Create a REST API for user management")
357     print(result.review)  # Final output from reviewer agent
```

**Output (Lines 108-145):**
```
================================================================================
EXAMPLE 4: MULTI-AGENT ORCHESTRATION (AutoGen feature)
================================================================================

Multiple agents collaborating on a complex task:

Scenario: Software development workflow with specialized agents

----------------------------------------
# Line 322: Define multiple specialized agents
researcher = client.create_agent(
    name="Researcher",
    instructions="Research and analyze requirements. Be thorough."
)

architect = client.create_agent(
    name="Architect",
    instructions="Design system architecture. Focus on scalability."
)

developer = client.create_agent(
    name="Developer",
    instructions="Write code implementations. Follow best practices."
)

reviewer = client.create_agent(
    name="Reviewer",
    instructions="Review code for bugs and improvements."
)

# Line 343: Create a workflow with agent handoffs
from agent_framework import Workflow, Step

workflow = Workflow(
    steps=[
        Step(agent=researcher, output="requirements"),
        Step(agent=architect, input="requirements", output="design"),
        Step(agent=developer, input="design", output="code"),
        Step(agent=reviewer, input="code", output="review")
    ]
)

# Line 355: Execute the workflow
result = await workflow.run("Create a REST API for user management")
print(result.review)  # Final output from reviewer agent
----------------------------------------

Expected behavior:
  1. Researcher analyzes requirements
  2. Architect designs the API structure
  3. Developer implements the code
  4. Reviewer provides feedback

✓ Each agent specializes, collaborates sequentially (AutoGen pattern)
```

**Annotation:** Multi-agent orchestration is AutoGen's signature feature:
- **Specialized agents**: Each agent has a specific role and expertise
- **Sequential workflow**: Output from one agent becomes input to the next
- **Named outputs**: Results are stored with semantic names for clarity
- **Complex problem solving**: Breaking down tasks across multiple AI agents

This pattern is ideal for tasks requiring different types of expertise or perspectives.

---

### 7. State Management with Threads (Lines 371-423) - Semantic Kernel Feature

```python
388     # Line 388: Create a thread for persistent state
389     thread = Thread(metadata={"user_id": "user123", "session": "abc"})
390
391     # Line 391: Multiple interactions maintain context
392     response1 = await agent.run(
393         "My name is Alice and I like Python.",
394         thread=thread
395     )
396     print(response1.text)  # "Nice to meet you, Alice!"
397
398     # Line 398: Agent remembers previous context
399     response2 = await agent.run(
400         "What's my name and favorite language?",
401         thread=thread
402     )
403     print(response2.text)  # "Your name is Alice and you like Python."
404
405     # Line 404: Thread state persists
406     thread_id = thread.id  # Save for later
407     # ... later in another session ...
408     restored_thread = Thread(id=thread_id)
409     response3 = await agent.run("What do you remember about me?", thread=restored_thread)
```

**Output (Lines 148-177):**
```
================================================================================
EXAMPLE 5: STATE MANAGEMENT WITH THREADS (Semantic Kernel feature)
================================================================================

Thread-based state enables persistent multi-turn conversations:

----------------------------------------
from agent_framework import Thread

# Line 388: Create a thread for persistent state
thread = Thread(metadata={"user_id": "user123", "session": "abc"})

# Line 391: Multiple interactions maintain context
response1 = await agent.run(
    "My name is Alice and I like Python.",
    thread=thread
)
print(response1.text)  # "Nice to meet you, Alice!"

# Line 398: Agent remembers previous context
response2 = await agent.run(
    "What's my name and favorite language?",
    thread=thread
)
print(response2.text)  # "Your name is Alice and you like Python."

# Line 404: Thread state persists
thread_id = thread.id  # Save for later
# ... later in another session ...
restored_thread = Thread(id=thread_id)
response3 = await agent.run("What do you remember about me?", thread=restored_thread)

----------------------------------------

Key benefits:
  • Conversation history is automatically managed
  • State persists across sessions
  • Metadata enables user/session tracking
  • Enterprise-grade for production applications
```

**Annotation:** Thread-based state management is a Semantic Kernel feature for production applications:
- **Automatic context**: Conversation history is managed automatically
- **Persistent state**: Threads can be saved and restored across sessions
- **Metadata**: Associate threads with users, sessions, or custom data
- **Enterprise-ready**: Supports external state stores (Redis, CosmosDB, etc.)

This is crucial for building chatbots and assistants that remember context across multiple interactions.

---

### 8. Filters & Telemetry (Lines 426-491) - Semantic Kernel Feature

```python
444     # Line 444: Before agent processes request
445     async def on_request(self, context: FilterContext):
446         print(f"[LOG] Request: {context.request.text}")
447         context.metadata["start_time"] = time.time()
448
449     # Line 449: After agent generates response
450     async def on_response(self, context: FilterContext):
451         duration = time.time() - context.metadata["start_time"]
452         print(f"[LOG] Response: {context.response.text}")
453         print(f"[LOG] Duration: {duration:.2f}s")
454
455     # Line 455: Register filter with client
456     client = OpenAIChatClient(filters=[LoggingFilter()])
...
464     # Line 464: Enable OpenTelemetry for monitoring
465     telemetry_config = OpenTelemetryConfig(
466         service_name="my-agent-app",
467         tracer=trace.get_tracer(__name__)
468     )
469
470     client = OpenAIChatClient(telemetry=telemetry_config)
471
472     # Line 472: All agent operations are automatically traced
473     # - Token usage
474     # - Latency
475     # - Error rates
476     # - Tool calls
477     # - Agent handoffs
```

**Output (Lines 180-227):**
```
================================================================================
EXAMPLE 6: FILTERS & TELEMETRY (Semantic Kernel feature)
================================================================================

Enterprise-grade observability and middleware:

1. REQUEST/RESPONSE FILTERS:
----------------------------------------
from agent_framework import Filter, FilterContext

class LoggingFilter(Filter):
    '''Log all agent interactions.'''

    # Line 444: Before agent processes request
    async def on_request(self, context: FilterContext):
        print(f"[LOG] Request: {context.request.text}")
        context.metadata["start_time"] = time.time()

    # Line 449: After agent generates response
    async def on_response(self, context: FilterContext):
        duration = time.time() - context.metadata["start_time"]
        print(f"[LOG] Response: {context.response.text}")
        print(f"[LOG] Duration: {duration:.2f}s")

# Line 455: Register filter with client
client = OpenAIChatClient(filters=[LoggingFilter()])

2. TELEMETRY INTEGRATION:
----------------------------------------
from agent_framework.telemetry import OpenTelemetryConfig
from opentelemetry import trace

# Line 464: Enable OpenTelemetry for monitoring
telemetry_config = OpenTelemetryConfig(
    service_name="my-agent-app",
    tracer=trace.get_tracer(__name__)
)

client = OpenAIChatClient(telemetry=telemetry_config)

# Line 472: All agent operations are automatically traced
# - Token usage
# - Latency
# - Error rates
# - Tool calls
# - Agent handoffs

✓ Production-ready observability out of the box!
```

**Annotation:** Enterprise observability features from Semantic Kernel:
- **Filters**: Middleware for request/response interception
  - Logging, authentication, rate limiting, etc.
  - Can modify context and metadata
  - Async-first design
- **Telemetry**: Built-in OpenTelemetry integration
  - Automatic tracing of all operations
  - Token usage tracking
  - Performance metrics
  - Distributed tracing across agent handoffs

These features are essential for production deployments, monitoring, and debugging.

---

### 9. Framework Comparison Table (Lines 494-527)

```python
503     print("┌─────────────────────────────────────────────────────────────────────┐")
504     print("│ FEATURE                    │ AutoGen │ Semantic Kernel │ Agent FW │")
505     print("├────────────────────────────┼─────────┼─────────────────┼──────────┤")
506     print("│ Multi-agent orchestration  │    ✓    │        ~        │     ✓    │")
507     print("│ Simple agent abstractions  │    ✓    │        -        │     ✓    │")
508     print("│ Type-safe function calling │    -    │        ✓        │     ✓    │")
509     print("│ Thread-based state         │    -    │        ✓        │     ✓    │")
510     print("│ Filters & middleware       │    -    │        ✓        │     ✓    │")
511     print("│ Enterprise telemetry       │    -    │        ✓        │     ✓    │")
512     print("│ Workflow orchestration     │    ~    │        ✓        │     ✓    │")
513     print("│ Multi-LLM provider support │    ✓    │        ✓        │     ✓    │")
514     print("│ Production-ready           │    ~    │        ✓        │     ✓    │")
515     print("│ Python + .NET support      │    ✓    │        ✓        │     ✓    │")
516     print("└────────────────────────────┴─────────┴─────────────────┴──────────┘")
```

**Output (Lines 230-246):**
```
================================================================================
FRAMEWORK EVOLUTION: AutoGen + Semantic Kernel = Agent Framework
================================================================================

┌─────────────────────────────────────────────────────────────────────┐
│ FEATURE                    │ AutoGen │ Semantic Kernel │ Agent FW │
├────────────────────────────┼─────────┼─────────────────┼──────────┤
│ Multi-agent orchestration  │    ✓    │        ~        │     ✓    │
│ Simple agent abstractions  │    ✓    │        -        │     ✓    │
│ Type-safe function calling │    -    │        ✓        │     ✓    │
│ Thread-based state         │    -    │        ✓        │     ✓    │
│ Filters & middleware       │    -    │        ✓        │     ✓    │
│ Enterprise telemetry       │    -    │        ✓        │     ✓    │
│ Workflow orchestration     │    ~    │        ✓        │     ✓    │
│ Multi-LLM provider support │    ✓    │        ✓        │     ✓    │
│ Production-ready           │    ~    │        ✓        │     ✓    │
│ Python + .NET support      │    ✓    │        ✓        │     ✓    │
└────────────────────────────┴─────────┴─────────────────┴──────────┘

Legend: ✓ = Full support, ~ = Partial support, - = Not available

Microsoft Agent Framework is the unified successor, combining
the best features from both projects with new capabilities.
```

**Annotation:** This comparison clearly shows how Microsoft Agent Framework combines the strengths of both predecessor frameworks:
- **AutoGen strengths**: Simple abstractions, multi-agent patterns, multi-LLM support
- **Semantic Kernel strengths**: Type safety, state management, enterprise features
- **Agent Framework**: Gets the best of both, plus new unified capabilities

---

## Complete Program Output

```
================================================================================
MICROSOFT AGENT FRAMEWORK - UNIFIED AI AGENT DEVELOPMENT
================================================================================

The Microsoft Agent Framework combines the best of both worlds:

FROM AUTOGEN:
  • Multi-agent orchestration and collaboration
  • Dynamic agent-to-agent communication
  • Group chat patterns for complex problem solving
  • Flexible, LLM-driven agent behavior

FROM SEMANTIC KERNEL:
  • Type-safe function calling and tool integration
  • Enterprise-grade telemetry and observability
  • State management with threads
  • Production-ready filters and middleware

MULTI-LLM PROVIDER SUPPORT:
  • OpenAI (GPT-4, GPT-3.5, etc.)
  • Azure OpenAI Service
  • Azure AI Foundry models
  • Ollama for local models
  • Google Gemini
  • Semantic Kernel adapter for SK model clients

================================================================================

[... Examples 1-6 as shown above ...]

================================================================================
INSTALLATION
================================================================================

Install the framework:
  pip install agent-framework --pre

All dependencies are managed via inline script metadata.
Use 'uv run main_microsoft_agent_framework.py' to run with automatic dependency installation.

================================================================================
DOCUMENTATION & RESOURCES
================================================================================

• GitHub: https://github.com/microsoft/agent-framework
• Docs: https://learn.microsoft.com/agent-framework
• Samples: https://github.com/microsoft/Agent-Framework-Samples

================================================================================
```

---

## Version Requirements

**This example requires:**
- **Python:** 3.11 or higher (specified in script metadata)
- **Microsoft Agent Framework:** Version 0.1.0+ (currently in public preview)
- **Optional:** OpenAI API key for live demonstrations

The framework is in **public preview** as of October 2025. Use the `--pre` flag when installing via pip.

---

## Key Takeaways

1. **Unified Framework**: Microsoft Agent Framework replaces AutoGen and Semantic Kernel with a single, cohesive API
2. **Multi-LLM Support**: Switch between OpenAI, Azure OpenAI, Azure AI Foundry, and other providers with minimal code changes
3. **Best of Both Worlds**: Combines AutoGen's simplicity with Semantic Kernel's enterprise features
4. **Production-Ready**: Built-in telemetry, filters, state management, and type safety
5. **Future-Proof**: Microsoft's unified AI agent framework going forward

---

## Resources

- **GitHub Repository:** https://github.com/microsoft/agent-framework
- **Documentation:** https://learn.microsoft.com/agent-framework
- **Sample Projects:** https://github.com/microsoft/Agent-Framework-Samples
- **AutoGen Migration Guide:** Available in official docs
- **Semantic Kernel Migration Guide:** Available in official docs
