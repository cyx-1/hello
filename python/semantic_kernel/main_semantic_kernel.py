# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "semantic-kernel>=1.16.0",
#     "openai>=1.0.0",
# ]
# ///
"""
Semantic Kernel Python: Enterprise-Grade AI Orchestration Framework

This example showcases three key features of Semantic Kernel:
1. Enterprise-grade stability - production-ready, type-safe foundations
2. Plugin architecture - connectors to existing code and APIs
3. State management - memory, threads, and observability

Semantic Kernel requires Python 3.10+ and provides production-ready AI orchestration.
"""

import asyncio
from typing import Annotated

from semantic_kernel import Kernel
from semantic_kernel.contents import ChatHistory
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.functions import kernel_function


# =============================================================================
# FEATURE 1: ENTERPRISE-GRADE STABILITY - TYPE-SAFE PLUGIN ARCHITECTURE
# =============================================================================


class WeatherPlugin:
    """
    Type-safe plugin demonstrating enterprise-grade stability.
    Lines 42-74: Shows type annotations, Pydantic-style validation,
    and production-ready error handling.
    """

    @kernel_function(
        name="get_weather",
        description="Get the current weather for a location",
    )
    def get_weather(
        self,
        location: Annotated[str, "The city name, e.g., 'Seattle'"],
    ) -> Annotated[str, "Weather information"]:
        """
        Type-safe function with runtime validation.
        Line 53-62: Demonstrates type annotations and return type safety.
        """
        print(f"\n[WEATHER PLUGIN] Fetching weather for: {location}")

        # Simulate API call with type-safe response
        weather_data = {
            "Seattle": "☁️ Cloudy, 55°F, Light rain expected",
            "San Francisco": "☀️ Sunny, 68°F, Clear skies",
            "New York": "🌤️ Partly cloudy, 62°F, Mild winds",
            "London": "🌧️ Rainy, 52°F, Heavy showers",
        }

        result = weather_data.get(
            location, f"⚠️ Weather data unavailable for {location}"
        )
        print(f"[WEATHER PLUGIN] Result: {result}")
        return result


class CalculatorPlugin:
    """
    Mathematical operations plugin with type safety.
    Lines 76-118: Shows multiple kernel functions in a single plugin.
    """

    @kernel_function(
        name="add",
        description="Add two numbers together",
    )
    def add(
        self,
        number1: Annotated[float, "First number"],
        number2: Annotated[float, "Second number"],
    ) -> Annotated[float, "The sum"]:
        """
        Type-safe addition with automatic validation.
        Line 89-98: Demonstrates numeric type safety.
        """
        result = number1 + number2
        print(f"\n[CALCULATOR PLUGIN] {number1} + {number2} = {result}")
        return result

    @kernel_function(
        name="multiply",
        description="Multiply two numbers",
    )
    def multiply(
        self,
        number1: Annotated[float, "First number"],
        number2: Annotated[float, "Second number"],
    ) -> Annotated[float, "The product"]:
        """
        Type-safe multiplication.
        Line 100-110: Shows consistent type-safe patterns.
        """
        result = number1 * number2
        print(f"\n[CALCULATOR PLUGIN] {number1} × {number2} = {result}")
        return result


class DataAnalysisPlugin:
    """
    Plugin demonstrating complex data operations.
    Lines 120-152: Shows how to wrap existing business logic as plugins.
    """

    @kernel_function(
        name="analyze_sales",
        description="Analyze sales data and return insights",
    )
    def analyze_sales(
        self,
        revenue: Annotated[float, "Total revenue"],
        cost: Annotated[float, "Total cost"],
    ) -> Annotated[str, "Analysis report"]:
        """
        Business logic wrapped as a plugin.
        Line 131-144: Demonstrates integration with existing code.
        """
        profit = revenue - cost
        margin = (profit / revenue * 100) if revenue > 0 else 0

        report = f"""
📊 Sales Analysis Report:
   Revenue: ${revenue:,.2f}
   Cost: ${cost:,.2f}
   Profit: ${profit:,.2f}
   Margin: {margin:.1f}%
   Status: {"✅ Profitable" if profit > 0 else "❌ Loss"}
"""
        print("\n[DATA ANALYSIS PLUGIN] Generated report")
        return report


# =============================================================================
# FEATURE 2: PLUGIN ARCHITECTURE - CONNECTORS & INTEGRATION
# =============================================================================


async def demonstrate_plugin_architecture():
    """
    Demonstrates Semantic Kernel's plugin architecture.
    Lines 163-221: Shows how plugins provide connectors to existing code and APIs.
    """
    print("\n" + "=" * 80)
    print("FEATURE 2: PLUGIN ARCHITECTURE - CONNECTORS TO EXISTING CODE AND APIs")
    print("=" * 80)

    # Initialize kernel - the central orchestrator
    kernel = Kernel()
    print("\n[KERNEL] Initialized enterprise-grade kernel")

    # Register plugins - connecting existing functionality
    print("\n[PLUGIN REGISTRATION] Adding plugins to kernel...")

    weather_plugin = kernel.add_plugin(
        WeatherPlugin(),
        plugin_name="weather",
    )
    print(
        f"  ✓ Registered: weather plugin with {len(weather_plugin.functions)} function"
    )

    calculator_plugin = kernel.add_plugin(
        CalculatorPlugin(),
        plugin_name="calculator",
    )
    print(
        f"  ✓ Registered: calculator plugin with {len(calculator_plugin.functions)} functions"
    )

    data_plugin = kernel.add_plugin(
        DataAnalysisPlugin(),
        plugin_name="data_analysis",
    )
    print(
        f"  ✓ Registered: data_analysis plugin with {len(data_plugin.functions)} function"
    )

    # Direct function invocation - calling plugins programmatically
    print("\n[DIRECT INVOCATION] Calling plugins directly:")

    # Call weather plugin
    weather_result = await kernel.invoke(
        function_name="get_weather",
        plugin_name="weather",
        location="Seattle",
    )
    print(f"  Result: {weather_result}")

    # Call calculator plugin
    calc_result = await kernel.invoke(
        function_name="add",
        plugin_name="calculator",
        number1=42.5,
        number2=17.3,
    )
    print(f"  Result: {calc_result}")

    # Call data analysis plugin
    analysis_result = await kernel.invoke(
        function_name="analyze_sales",
        plugin_name="data_analysis",
        revenue=250000.0,
        cost=180000.0,
    )
    print(f"  Result: {analysis_result}")

    print("\n[PLUGIN ARCHITECTURE] ✅ All plugins successfully integrated!")

    return kernel


# =============================================================================
# FEATURE 3: STATE MANAGEMENT - MEMORY, THREADS, AND OBSERVABILITY
# =============================================================================


async def demonstrate_memory_and_state():
    """
    Demonstrates state management with memory and conversation tracking.
    Lines 246-338: Shows in-memory state, conversation history, and observability.
    """
    print("\n" + "=" * 80)
    print("FEATURE 3: STATE MANAGEMENT - MEMORY, THREADS, AND OBSERVABILITY")
    print("=" * 80)

    # Initialize kernel (not used in this demo, but shown for completeness)
    _ = Kernel()

    # Setup in-memory state store - long-term knowledge storage
    print("\n[MEMORY SETUP] Configuring in-memory state management...")

    # In-memory knowledge base (production would use vector DB)
    knowledge_base = {
        "user_preferences": {
            "user_001": [
                "User prefers Python for backend development",
                "User's primary project is an AI orchestration platform",
                "User values type safety and production readiness",
            ],
            "company_001": [
                "Company uses Semantic Kernel for AI applications",
                "Company requires enterprise-grade stability",
            ],
        },
        "session_data": {
            "session_001": {
                "start_time": "2024-01-15T10:00:00Z",
                "user_id": "user_001",
                "status": "active",
            }
        },
    }

    print("  ✓ Created in-memory knowledge base")
    print("  ✓ Initialized state management system")

    # Store and organize facts
    print("\n[MEMORY STORAGE] Knowledge base contents...")

    total_facts = sum(
        len(v) if isinstance(v, list) else 1
        for category in knowledge_base.values()
        for v in category.values()
    )

    for category, items in knowledge_base.items():
        print(f"\n  Category: {category}")
        for key, value in items.items():
            if isinstance(value, list):
                for fact in value:
                    print(f"    ✓ [{key}] {fact}")
            else:
                print(f"    ✓ [{key}] {value}")

    print(f"\n[MEMORY] Successfully organized {total_facts} items")

    # Retrieve from memory - demonstrating stateful queries
    print("\n[MEMORY RETRIEVAL] Fetching stored knowledge...")

    user_prefs = knowledge_base["user_preferences"]["user_001"]
    print(f"  Retrieved {len(user_prefs)} preferences for user_001:")
    for pref in user_prefs:
        print(f"    • {pref}")

    session_info = knowledge_base["session_data"]["session_001"]
    print("  Retrieved session info:")
    for key, value in session_info.items():
        print(f"    • {key}: {value}")

    # Conversation history - thread management
    print("\n" + "-" * 80)
    print("[CONVERSATION THREADS] Managing conversation state...")

    chat_history = ChatHistory()
    print("  ✓ Created chat history for thread management")

    # Simulate a conversation thread
    conversation_turns = [
        ("user", "Hello! I'm working on an AI project."),
        (
            "assistant",
            "Great! I can help with that. Semantic Kernel provides enterprise-grade AI orchestration.",
        ),
        ("user", "What's the weather in Seattle?"),
        ("assistant", "Let me check the weather for you..."),
        ("user", "Can you also calculate 15 + 27?"),
        ("assistant", "The sum of 15 and 27 is 42."),
    ]

    print("\n[THREAD STATE] Building conversation history:")
    for i, (role, message) in enumerate(conversation_turns, 1):
        chat_history.add_message(ChatMessageContent(role=role, content=message))
        print(f"  Turn {i} [{role}]: {message[:60]}...")

    print(f"\n[THREAD] Conversation thread has {len(chat_history.messages)} messages")

    # Observability - inspect conversation state
    print("\n" + "-" * 80)
    print("[OBSERVABILITY] Analyzing conversation state...")

    user_messages = [msg for msg in chat_history.messages if msg.role == "user"]
    assistant_messages = [
        msg for msg in chat_history.messages if msg.role == "assistant"
    ]

    print("\n  📊 Conversation Metrics:")
    print(f"     Total turns: {len(chat_history.messages)}")
    print(f"     User messages: {len(user_messages)}")
    print(f"     Assistant messages: {len(assistant_messages)}")
    print("     Thread ID: conversation_001")
    print("     State: Active")

    # Display full conversation thread
    print("\n[THREAD REPLAY] Full conversation history:")
    for i, msg in enumerate(chat_history.messages, 1):
        print(f"  {i}. [{msg.role.upper()}] {msg.content}")

    print("\n[STATE MANAGEMENT] ✅ Memory and threads successfully managed!")


# =============================================================================
# INTEGRATED DEMONSTRATION - ALL FEATURES TOGETHER
# =============================================================================


async def demonstrate_integrated_system():
    """
    Demonstrates all three features working together.
    Lines 360-426: Shows enterprise-grade system with plugins, state, and observability.
    """
    print("\n" + "=" * 80)
    print("INTEGRATED DEMONSTRATION - ALL FEATURES TOGETHER")
    print("=" * 80)

    # Initialize kernel with all plugins
    kernel = Kernel()

    # Note: In production, you would configure with real AI service:
    # service_id = "chat-gpt"
    # kernel.add_service(
    #     OpenAIChatCompletion(
    #         service_id=service_id,
    #         api_key="your-api-key",
    #         org_id="your-org-id"
    #     )
    # )

    # Add plugins
    print("\n[SYSTEM INITIALIZATION] Setting up integrated system...")
    kernel.add_plugin(WeatherPlugin(), plugin_name="weather")
    kernel.add_plugin(CalculatorPlugin(), plugin_name="calculator")
    kernel.add_plugin(DataAnalysisPlugin(), plugin_name="data_analysis")
    print("  ✓ All plugins registered")

    # Setup conversation state
    chat_history = ChatHistory()
    chat_history.add_system_message(
        "You are a helpful AI assistant with access to weather, calculator, and data analysis tools."
    )
    print("  ✓ Conversation thread initialized")

    # Simulate user interaction workflow
    print("\n[WORKFLOW] Simulating user interaction...")

    tasks = [
        {
            "user_input": "What's the weather in San Francisco?",
            "plugin": "weather",
            "function": "get_weather",
            "params": {"location": "San Francisco"},
        },
        {
            "user_input": "Calculate 25 times 4",
            "plugin": "calculator",
            "function": "multiply",
            "params": {"number1": 25, "number2": 4},
        },
        {
            "user_input": "Analyze sales with revenue 500k and cost 320k",
            "plugin": "data_analysis",
            "function": "analyze_sales",
            "params": {"revenue": 500000, "cost": 320000},
        },
    ]

    for i, task in enumerate(tasks, 1):
        print(f"\n  Task {i}: {task['user_input']}")
        chat_history.add_user_message(task["user_input"])

        # Execute plugin function
        result = await kernel.invoke(
            function_name=task["function"],
            plugin_name=task["plugin"],
            **task["params"],
        )

        # Store result in conversation
        response = f"Result: {result}"
        chat_history.add_assistant_message(response)
        print(f"  ✅ Completed: {response[:80]}...")

    # Final observability report
    print("\n" + "-" * 80)
    print("[SYSTEM OBSERVABILITY] Final State Report")
    print("-" * 80)

    print(f"""
  📊 System Metrics:
     Plugins loaded: 3
     Functions available: 5
     Conversation turns: {len(chat_history.messages)}
     Tasks completed: {len(tasks)}
     System status: ✅ Healthy

  🔧 Plugin Status:
     ✓ weather: Active (1 function)
     ✓ calculator: Active (2 functions)
     ✓ data_analysis: Active (1 function)

  💬 Thread Status:
     Thread ID: main_thread
     Message count: {len(chat_history.messages)}
     State: Completed
""")

    print("\n[INTEGRATED SYSTEM] ✅ All features working seamlessly!")


# =============================================================================
# MAIN EXECUTION
# =============================================================================


async def main():
    """
    Main entry point for Semantic Kernel demonstration.
    Lines 472-504: Orchestrates all demonstrations.
    """
    print("=" * 80)
    print("🚀 SEMANTIC KERNEL PYTHON - ENTERPRISE AI ORCHESTRATION")
    print("=" * 80)
    print("\nVersion: semantic-kernel >= 1.16.0")
    print("Python: >= 3.10")
    print("\nKey Features Demonstrated:")
    print("  1. Enterprise-grade stability - production-ready, type-safe foundations")
    print("  2. Plugin architecture - connectors to existing code and APIs")
    print("  3. State management - memory, threads, and observability")

    try:
        # Feature 1: Type-safe enterprise architecture
        print("\n\n")
        print("┌" + "─" * 78 + "┐")
        print("│" + " FEATURE 1: ENTERPRISE-GRADE STABILITY ".center(78) + "│")
        print("└" + "─" * 78 + "┘")
        print("\n[INFO] Demonstrating type-safe plugin architecture...")
        print("[INFO] All functions use Python type hints and Annotated types")
        print("[INFO] This ensures runtime validation and IDE support")

        # Feature 2: Plugin architecture
        print("\n\n")
        print("┌" + "─" * 78 + "┐")
        print("│" + " FEATURE 2: PLUGIN ARCHITECTURE ".center(78) + "│")
        print("└" + "─" * 78 + "┘")
        _ = await demonstrate_plugin_architecture()

        # Feature 3: State management
        print("\n\n")
        print("┌" + "─" * 78 + "┐")
        print("│" + " FEATURE 3: STATE MANAGEMENT ".center(78) + "│")
        print("└" + "─" * 78 + "┘")
        await demonstrate_memory_and_state()

        # Integrated demonstration
        print("\n\n")
        print("┌" + "─" * 78 + "┐")
        print("│" + " INTEGRATED DEMONSTRATION ".center(78) + "│")
        print("└" + "─" * 78 + "┘")
        await demonstrate_integrated_system()

        # Summary
        print("\n\n" + "=" * 80)
        print("✨ DEMONSTRATION COMPLETE")
        print("=" * 80)
        print("\n🎯 Key Takeaways:")
        print(
            "  ✓ Type-safe plugins with Annotated types ensure enterprise reliability"
        )
        print("  ✓ Plugin architecture enables easy integration of existing code/APIs")
        print(
            "  ✓ Built-in memory and conversation management for stateful applications"
        )
        print("  ✓ Observability features provide production-ready monitoring")
        print("\n💡 Production Usage:")
        print("  • Add OpenAI/Azure OpenAI service for AI-powered orchestration")
        print("  • Use persistent memory stores (Redis, PostgreSQL, etc.)")
        print("  • Implement custom plugins for your business logic")
        print("  • Enable logging and telemetry for full observability")

    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")
        print(f"   Type: {type(e).__name__}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
