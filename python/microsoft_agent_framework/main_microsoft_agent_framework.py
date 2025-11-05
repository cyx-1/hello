#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "agent-framework>=0.1.0",
#     "agent-framework-azure-ai>=0.1.0",
#     "openai>=1.0.0",
#     "azure-identity>=1.18.0",
# ]
# ///
"""
Microsoft Agent Framework Illustration

This script demonstrates the Microsoft Agent Framework, which combines:
1. AutoGen's multi-agent orchestration capabilities
2. Semantic Kernel's enterprise-grade features and structured execution
3. Support for multiple LLM providers (OpenAI, Azure OpenAI, etc.)

The framework is the unified successor to both AutoGen and Semantic Kernel,
built by the same Microsoft teams.
"""

import asyncio
import os
from typing import Annotated


def demonstrate_framework_overview():
    """Display overview of Microsoft Agent Framework features."""
    print("=" * 80)
    print("MICROSOFT AGENT FRAMEWORK - UNIFIED AI AGENT DEVELOPMENT")
    print("=" * 80)
    print()
    print("The Microsoft Agent Framework combines the best of both worlds:")
    print()
    print("FROM AUTOGEN:")
    print("  • Multi-agent orchestration and collaboration")
    print("  • Dynamic agent-to-agent communication")
    print("  • Group chat patterns for complex problem solving")
    print("  • Flexible, LLM-driven agent behavior")
    print()
    print("FROM SEMANTIC KERNEL:")
    print("  • Type-safe function calling and tool integration")
    print("  • Enterprise-grade telemetry and observability")
    print("  • State management with threads")
    print("  • Production-ready filters and middleware")
    print()
    print("MULTI-LLM PROVIDER SUPPORT:")
    print("  • OpenAI (GPT-4, GPT-3.5, etc.)")
    print("  • Azure OpenAI Service")
    print("  • Azure AI Foundry models")
    print("  • Ollama for local models")
    print("  • Google Gemini")
    print("  • Semantic Kernel adapter for SK model clients")
    print()
    print("=" * 80)
    print()


async def demonstrate_basic_agent():
    """
    Demonstrate basic agent creation and execution.

    This showcases the simple, AutoGen-style agent interface.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 1: BASIC AGENT CREATION (AutoGen-style simplicity)")
    print("=" * 80)
    print()

    # Check if OpenAI API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Note: OPENAI_API_KEY not set. Using mock example.")
        print()
        print("Code example:")
        print("-" * 40)
        print("""from agent_framework import Agent
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
print(result.text)""")
        print("-" * 40)
        print()
        print("Expected output:")
        print("  'A pandas DataFrame is a 2-dimensional labeled data structure")
        print("   similar to a spreadsheet or SQL table...'")
        print()
        return

    try:
        from agent_framework.openai import OpenAIChatClient

        print("Creating OpenAI agent...")
        client = OpenAIChatClient(
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY")
        )

        agent = client.create_agent(
            name="DataAnalyst",
            instructions="You are an expert data analyst. Be concise."
        )

        print("Running agent with task...")
        result = await agent.run("Explain pandas DataFrame in one sentence.")
        print(f"\n✓ Agent response: {result.text}\n")

    except ImportError:
        print("⚠️  agent-framework not installed. Install with:")
        print("   pip install agent-framework --pre")
        print()
    except Exception as e:
        print(f"⚠️  Error: {e}")
        print()


async def demonstrate_multi_provider_support():
    """
    Demonstrate support for multiple LLM providers.

    This shows how the framework abstracts away provider differences.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 2: MULTI-LLM PROVIDER SUPPORT")
    print("=" * 80)
    print()

    print("The framework supports multiple providers with a consistent interface:")
    print()
    print("1. OPENAI PROVIDER:")
    print("-" * 40)
    print("""from agent_framework.openai import OpenAIChatClient

# Line 152: OpenAI client
openai_client = OpenAIChatClient(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")
)
agent = openai_client.create_agent(name="Assistant")""")
    print()

    print("2. AZURE OPENAI PROVIDER:")
    print("-" * 40)
    print("""from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import DefaultAzureCredential

# Line 165: Azure OpenAI with managed identity
azure_client = AzureOpenAIChatClient(
    endpoint="https://your-resource.openai.azure.com/",
    credential=DefaultAzureCredential(),
    deployment="gpt-4"
)
agent = azure_client.create_agent(name="AzureAssistant")""")
    print()

    print("3. AZURE AI FOUNDRY (Multiple Models):")
    print("-" * 40)
    print("""from agent_framework.azure import AzureAIFoundryChatClient

# Line 179: Azure AI with various models (Llama, Mistral, etc.)
foundry_client = AzureAIFoundryChatClient(
    endpoint="https://your-foundry.inference.ai.azure.com",
    credential=DefaultAzureCredential(),
    model="Llama-3-70B-Instruct"
)
agent = foundry_client.create_agent(name="FoundryAssistant")""")
    print()

    print("4. SEMANTIC KERNEL ADAPTER:")
    print("-" * 40)
    print("""from agent_framework.semantic_kernel import SemanticKernelAdapter
from semantic_kernel import ChatCompletionClientBase

# Line 193: Use any Semantic Kernel model client
sk_client = ... # Any SK ChatCompletionClientBase
adapter = SemanticKernelAdapter(sk_client)
agent = adapter.create_agent(name="SKAssistant")""")
    print()

    print("✓ All providers use the same Agent interface!")
    print()


async def demonstrate_tools_and_functions():
    """
    Demonstrate tool/function calling (Semantic Kernel feature).

    This shows type-safe function integration, a key SK feature.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 3: TOOLS & FUNCTION CALLING (Semantic Kernel feature)")
    print("=" * 80)
    print()

    # Define tools with type annotations (SK-style)
    def get_weather(
        location: Annotated[str, "The city and state, e.g. San Francisco, CA"]
    ) -> str:
        """Get the current weather for a location."""
        # Mock implementation
        return f"Weather in {location}: Sunny, 72°F"

    def calculate_sum(
        a: Annotated[float, "First number"],
        b: Annotated[float, "Second number"]
    ) -> float:
        """Calculate the sum of two numbers."""
        return a + b

    print("Tools defined with type annotations (Semantic Kernel style):")
    print("-" * 40)
    print("""def get_weather(
    location: Annotated[str, "The city and state, e.g. San Francisco, CA"]
) -> str:
    '''Get the current weather for a location.'''
    return f"Weather in {location}: Sunny, 72°F"

def calculate_sum(
    a: Annotated[float, "First number"],
    b: Annotated[float, "Second number"]
) -> float:
    '''Calculate the sum of two numbers.'''
    return a + b""")
    print()

    if os.getenv("OPENAI_API_KEY"):
        try:
            from agent_framework.openai import OpenAIChatClient

            print("Creating agent with tools...")
            client = OpenAIChatClient(
                model="gpt-4o-mini",
                api_key=os.getenv("OPENAI_API_KEY")
            )

            # Line 260: Register tools with the agent
            agent = client.create_agent(
                name="ToolUser",
                instructions="You are a helpful assistant that can use tools.",
                tools=[get_weather, calculate_sum]
            )

            print("Running agent with tool-requiring task...")
            result = await agent.run(
                "What's the weather in Seattle, WA and what's 45 + 67?"
            )
            print(f"\n✓ Agent response: {result.text}\n")
            print("  (Agent automatically called get_weather and calculate_sum tools)")
            print()

        except Exception as e:
            print(f"⚠️  Could not run live example: {e}")
            print()
            print("Expected behavior:")
            print("  • Agent recognizes it needs weather data and sum calculation")
            print("  • Calls get_weather('Seattle, WA') -> 'Sunny, 72°F'")
            print("  • Calls calculate_sum(45, 67) -> 112")
            print("  • Returns: 'In Seattle, WA it's sunny and 72°F. 45 + 67 = 112'")
            print()
    else:
        print("Code example for registering tools:")
        print("-" * 40)
        print("""agent = client.create_agent(
    name="ToolUser",
    instructions="You are a helpful assistant.",
    tools=[get_weather, calculate_sum]  # Line 297: Register tools
)

result = await agent.run("What's the weather in Seattle?")
# Agent automatically calls the appropriate tool""")
        print()


async def demonstrate_multi_agent_collaboration():
    """
    Demonstrate multi-agent orchestration (AutoGen feature).

    This shows how multiple agents can collaborate on complex tasks.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 4: MULTI-AGENT ORCHESTRATION (AutoGen feature)")
    print("=" * 80)
    print()

    print("Multiple agents collaborating on a complex task:")
    print()
    print("Scenario: Software development workflow with specialized agents")
    print()
    print("-" * 40)
    print("""# Line 322: Define multiple specialized agents
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
print(result.review)  # Final output from reviewer agent""")
    print("-" * 40)
    print()
    print("Expected behavior:")
    print("  1. Researcher analyzes requirements")
    print("  2. Architect designs the API structure")
    print("  3. Developer implements the code")
    print("  4. Reviewer provides feedback")
    print()
    print("✓ Each agent specializes, collaborates sequentially (AutoGen pattern)")
    print()


async def demonstrate_state_management():
    """
    Demonstrate thread-based state management (Semantic Kernel feature).

    This shows persistent conversation state across multiple interactions.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 5: STATE MANAGEMENT WITH THREADS (Semantic Kernel feature)")
    print("=" * 80)
    print()

    print("Thread-based state enables persistent multi-turn conversations:")
    print()
    print("-" * 40)
    print("""from agent_framework import Thread

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
""")
    print("-" * 40)
    print()
    print("Key benefits:")
    print("  • Conversation history is automatically managed")
    print("  • State persists across sessions")
    print("  • Metadata enables user/session tracking")
    print("  • Enterprise-grade for production applications")
    print()


async def demonstrate_filters_and_telemetry():
    """
    Demonstrate filters and telemetry (Semantic Kernel feature).

    This shows observability and middleware capabilities.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 6: FILTERS & TELEMETRY (Semantic Kernel feature)")
    print("=" * 80)
    print()

    print("Enterprise-grade observability and middleware:")
    print()
    print("1. REQUEST/RESPONSE FILTERS:")
    print("-" * 40)
    print("""from agent_framework import Filter, FilterContext

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
client = OpenAIChatClient(filters=[LoggingFilter()])""")
    print()

    print("2. TELEMETRY INTEGRATION:")
    print("-" * 40)
    print("""from agent_framework.telemetry import OpenTelemetryConfig
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
# - Agent handoffs""")
    print()

    print("✓ Production-ready observability out of the box!")
    print()


async def demonstrate_framework_comparison():
    """Show how the framework unifies AutoGen and Semantic Kernel."""
    print("\n" + "=" * 80)
    print("FRAMEWORK EVOLUTION: AutoGen + Semantic Kernel = Agent Framework")
    print("=" * 80)
    print()

    print("┌─────────────────────────────────────────────────────────────────────┐")
    print("│ FEATURE                    │ AutoGen │ Semantic Kernel │ Agent FW │")
    print("├────────────────────────────┼─────────┼─────────────────┼──────────┤")
    print("│ Multi-agent orchestration  │    ✓    │        ~        │     ✓    │")
    print("│ Simple agent abstractions  │    ✓    │        -        │     ✓    │")
    print("│ Type-safe function calling │    -    │        ✓        │     ✓    │")
    print("│ Thread-based state         │    -    │        ✓        │     ✓    │")
    print("│ Filters & middleware       │    -    │        ✓        │     ✓    │")
    print("│ Enterprise telemetry       │    -    │        ✓        │     ✓    │")
    print("│ Workflow orchestration     │    ~    │        ✓        │     ✓    │")
    print("│ Multi-LLM provider support │    ✓    │        ✓        │     ✓    │")
    print("│ Production-ready           │    ~    │        ✓        │     ✓    │")
    print("│ Python + .NET support      │    ✓    │        ✓        │     ✓    │")
    print("└────────────────────────────┴─────────┴─────────────────┴──────────┘")
    print()
    print("Legend: ✓ = Full support, ~ = Partial support, - = Not available")
    print()
    print("Microsoft Agent Framework is the unified successor, combining")
    print("the best features from both projects with new capabilities.")
    print()


async def main():
    """Main entry point demonstrating all features."""
    print("\n")

    # Overview
    demonstrate_framework_overview()

    # Basic agent (AutoGen-style)
    await demonstrate_basic_agent()

    # Multi-provider support
    await demonstrate_multi_provider_support()

    # Tools and functions (SK-style)
    await demonstrate_tools_and_functions()

    # Multi-agent orchestration (AutoGen-style)
    await demonstrate_multi_agent_collaboration()

    # State management (SK-style)
    await demonstrate_state_management()

    # Filters and telemetry (SK-style)
    await demonstrate_filters_and_telemetry()

    # Comparison
    await demonstrate_framework_comparison()

    print("=" * 80)
    print("INSTALLATION")
    print("=" * 80)
    print()
    print("Install the framework:")
    print("  pip install agent-framework --pre")
    print()
    print("Optional components:")
    print("  pip install agent-framework-azure-ai --pre  # For Azure AI support")
    print("  pip install agent-framework-redis --pre     # For Redis state store")
    print()
    print("=" * 80)
    print("DOCUMENTATION & RESOURCES")
    print("=" * 80)
    print()
    print("• GitHub: https://github.com/microsoft/agent-framework")
    print("• Docs: https://learn.microsoft.com/agent-framework")
    print("• Samples: https://github.com/microsoft/Agent-Framework-Samples")
    print()
    print("=" * 80)
    print()


if __name__ == "__main__":
    asyncio.run(main())
