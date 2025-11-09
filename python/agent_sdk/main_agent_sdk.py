# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "claude-agent-sdk>=0.1.0",
#     "anyio>=4.0.0",
# ]
# ///
"""
Claude Agent SDK for Python: Comprehensive Feature Demonstration

This example demonstrates all key features of the Claude Agent SDK:
1. Simple query() function for basic interactions
2. ClaudeSDKClient for advanced bidirectional conversations
3. Custom tools using @tool decorator and SDK MCP servers
4. Hooks for validation and permission control
5. Streaming responses and async iteration
6. ClaudeAgentOptions for configuration
7. Error handling with specific exception types
8. Tool allowlisting and permission modes
9. System prompts and turn limits
10. In-process MCP servers for high performance

The Claude Agent SDK (formerly Claude Code SDK) enables building AI agents
that can use tools, maintain state, and execute complex workflows.

Requires: Python 3.10+, Claude Code 2.0.0+
"""

import asyncio
from typing import Any

import anyio

try:
    from claude_agent_sdk import (
        ClaudeAgentOptions,
        ClaudeSDKClient,
        HookMatcher,
        create_sdk_mcp_server,
        query,
        tool,
    )
except ImportError:
    print("\n⚠️  Claude Agent SDK not available in this environment")
    print("This demonstration requires:")
    print("  • Claude Code 2.0.0+")
    print("  • claude-agent-sdk package (pip install claude-agent-sdk)")
    print("\nNote: The SDK is designed to work within Claude Code environment")
    print(
        "For documentation, visit: https://docs.claude.com/en/docs/agent-sdk/overview"
    )
    exit(1)


# ============================================================================
# EXAMPLE 1: Simple query() Function
# ============================================================================


async def example_1_basic_query():
    """
    Demonstrate the simplest way to interact with Claude using query().

    The query() function returns an async iterator of response messages.
    This is ideal for simple, one-off interactions.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic Query Function")
    print("=" * 70)

    print("\n📝 Sending a simple prompt to Claude...")
    print("Code: async for message in query(prompt='What is 2 + 2?')")

    try:
        async for message in query(prompt="What is 2 + 2?"):
            print(f"\n✅ Response: {message}")
            print(f"   Type: {type(message).__name__}")

        print("\n💡 The query() function provides a quick, stateless way to interact")
        print("   with Claude for simple tasks without managing client state.")

    except Exception as e:
        print(f"\n⚠️  Error: {e}")
        print("   (This is expected if running outside Claude Code environment)")


# ============================================================================
# EXAMPLE 2: Custom Tools with @tool Decorator
# ============================================================================


@tool(
    "calculate",
    "Perform basic arithmetic calculations",
    {"operation": str, "a": float, "b": float},
)
async def calculate_tool(args: dict[str, Any]) -> dict[str, Any]:
    """
    A custom tool that performs calculations.

    Tools are Python functions decorated with @tool that Claude can invoke.
    They must return a dict with a "content" key containing the result.
    """
    operation = args["operation"]
    a = args["a"]
    b = args["b"]

    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Error: Division by zero",
    }

    result = operations.get(operation, "Error: Unknown operation")

    return {"content": [{"type": "text", "text": f"Result: {result}"}]}


@tool(
    "get_weather",
    "Get simulated weather information for a city",
    {"city": str},
)
async def get_weather_tool(args: dict[str, Any]) -> dict[str, Any]:
    """
    A tool that simulates fetching weather data.

    This demonstrates how tools can perform I/O operations,
    API calls, or any async Python code.
    """
    city = args["city"]

    # Simulate weather data (in real use, would call an API)
    weather_data = {
        "San Francisco": {"temp": 18, "condition": "Foggy"},
        "New York": {"temp": 22, "condition": "Sunny"},
        "London": {"temp": 15, "condition": "Rainy"},
    }

    data = weather_data.get(city, {"temp": 20, "condition": "Unknown"})

    return {
        "content": [
            {
                "type": "text",
                "text": f"Weather in {city}: {data['temp']}°C, {data['condition']}",
            }
        ]
    }


@tool(
    "store_data",
    "Store data in memory (demonstrates stateful tools)",
    {"key": str, "value": str},
)
async def store_data_tool(args: dict[str, Any]) -> dict[str, Any]:
    """
    A stateful tool that maintains data across calls.

    This demonstrates how tools can maintain state within the agent session.
    """
    key = args["key"]
    value = args["value"]

    # Store in global state (in production, use proper state management)
    if not hasattr(store_data_tool, "storage"):
        store_data_tool.storage = {}

    store_data_tool.storage[key] = value

    return {
        "content": [
            {
                "type": "text",
                "text": f"Stored '{key}' = '{value}'. Total items: {len(store_data_tool.storage)}",
            }
        ]
    }


# ============================================================================
# EXAMPLE 3: SDK MCP Server Creation
# ============================================================================


def create_custom_mcp_server():
    """
    Create an SDK MCP server with custom tools.

    SDK MCP servers run in-process within your Python application,
    providing better performance than separate process MCP servers.

    Benefits:
    - No subprocess overhead
    - Single Python process deployment
    - Improved performance and debugging
    - Type-safe function calls
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Creating SDK MCP Server")
    print("=" * 70)

    print("\n🔧 Creating in-process MCP server with custom tools...")

    server = create_sdk_mcp_server(
        name="demo-tools",
        version="1.0.0",
        tools=[calculate_tool, get_weather_tool, store_data_tool],
    )

    print("✅ Server created with 3 tools:")
    print("   • calculate - Perform arithmetic operations")
    print("   • get_weather - Get weather information")
    print("   • store_data - Store key-value pairs")
    print("\n💡 SDK MCP servers run in-process for better performance")

    return server


# ============================================================================
# EXAMPLE 4: Hooks for Validation and Permission Control
# ============================================================================


async def validate_bash_command(
    input_data: dict[str, Any], tool_use_id: str, context: dict[str, Any]
) -> dict[str, Any]:
    """
    Hook that validates Bash commands before execution.

    Hooks are invoked at specific points in the Claude agent loop
    for deterministic processing and automated feedback.

    This hook demonstrates PreToolUse validation to prevent
    dangerous or unwanted commands.
    """
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    # Only validate Bash commands
    if tool_name != "Bash":
        return {}

    command = tool_input.get("command", "")

    # Block patterns (customize as needed)
    blocked_patterns = ["rm -rf", "sudo", "format", "delete"]

    for pattern in blocked_patterns:
        if pattern in command:
            print(f"\n🚫 Hook blocked command containing: '{pattern}'")
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": f"Blocked: command contains '{pattern}'",
                }
            }

    print(f"\n✅ Hook approved command: {command[:50]}...")
    return {}


async def log_tool_usage(
    input_data: dict[str, Any], tool_use_id: str, context: dict[str, Any]
) -> dict[str, Any]:
    """
    Hook that logs all tool usage for monitoring.

    This demonstrates how hooks can be used for observability
    without affecting tool execution.
    """
    tool_name = input_data.get("tool_name", "Unknown")
    print(f"\n📊 Tool Usage Log: {tool_name} (ID: {tool_use_id})")

    # Return empty dict to allow execution
    return {}


# ============================================================================
# EXAMPLE 5: ClaudeSDKClient with Full Configuration
# ============================================================================


async def example_5_advanced_client():
    """
    Demonstrate ClaudeSDKClient with complete configuration.

    ClaudeSDKClient enables:
    - Bidirectional, stateful conversations
    - Custom tools and hooks
    - Streaming responses
    - Advanced configuration options
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Advanced ClaudeSDKClient Usage")
    print("=" * 70)

    # Create SDK MCP server
    server = create_sdk_mcp_server(
        name="advanced-tools",
        version="1.0.0",
        tools=[calculate_tool, get_weather_tool],
    )

    # Configure options
    options = ClaudeAgentOptions(
        # System prompt for agent behavior
        system_prompt="You are a helpful assistant with access to calculation and weather tools.",
        # Limit conversation turns (None = unlimited)
        turn_limit=10,
        # Register MCP servers
        mcp_servers={"tools": server},
        # Allow specific tools (use allowlist for security)
        allowed_tools=[
            "mcp__tools__calculate",
            "mcp__tools__get_weather",
        ],
        # Register hooks for validation
        hooks={
            "PreToolUse": [
                HookMatcher(matcher="Bash", hooks=[validate_bash_command]),
                HookMatcher(matcher="*", hooks=[log_tool_usage]),
            ],
        },
        # Working directory
        working_dir=".",
    )

    print("\n⚙️  Configuration:")
    print("   • System prompt: Set")
    print(f"   • Turn limit: {options.turn_limit}")
    print(f"   • Tools allowed: {len(options.allowed_tools)}")
    print(f"   • Hooks registered: {len(options.hooks)}")

    try:
        print("\n🤖 Creating ClaudeSDKClient...")

        async with ClaudeSDKClient(options=options) as client:
            print("✅ Client created successfully")

            # Send a query that will use our custom tools
            print("\n📤 Sending query: 'Calculate 15 * 7 and get weather for London'")

            await client.query(
                "Calculate 15 multiplied by 7, then tell me the weather in London"
            )

            print("\n📥 Receiving streaming response:")

            # Process streaming response
            message_count = 0
            async for message in client.receive_response():
                message_count += 1
                print(f"\n   Message {message_count}: {str(message)[:100]}...")

            print(f"\n✅ Received {message_count} message(s)")
            print("💡 ClaudeSDKClient supports bidirectional, stateful interactions")

    except Exception as e:
        print(f"\n⚠️  Error: {e}")
        print("   (This is expected if running outside Claude Code environment)")


# ============================================================================
# EXAMPLE 6: Streaming Message Input
# ============================================================================


async def example_6_streaming_input():
    """
    Demonstrate streaming messages to Claude.

    You can stream input dynamically rather than sending all at once,
    useful for processing data as it arrives or building prompts incrementally.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Streaming Input Messages")
    print("=" * 70)

    async def message_stream():
        """Generator that yields messages dynamically."""
        print("\n📊 Streaming data to Claude:")

        messages = [
            "Analyze the following sensor readings:",
            "Temperature: 25°C",
            "Humidity: 60%",
            "Pressure: 1013 hPa",
            "Air Quality: Good",
        ]

        for msg in messages:
            print(f"   → {msg}")
            yield {"type": "text", "text": msg}
            await asyncio.sleep(0.1)  # Simulate data arrival delay

    try:
        print("\n🤖 Sending streaming input to Claude...")

        async with ClaudeSDKClient() as client:
            await client.query(message_stream())

            print("\n📥 Processing response:")
            async for message in client.receive_response():
                print(f"   {str(message)[:80]}...")

        print("\n💡 Streaming input is useful for real-time data processing")

    except Exception as e:
        print(f"\n⚠️  Error: {e}")
        print("   (This is expected if running outside Claude Code environment)")


# ============================================================================
# EXAMPLE 7: Error Handling
# ============================================================================


async def example_7_error_handling():
    """
    Demonstrate proper error handling with specific exception types.

    The SDK provides specific exceptions for different error scenarios:
    - CLINotFoundError: Claude Code CLI not found
    - ProcessError: Process execution error
    - CLIConnectionError: Connection error to CLI
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Error Handling")
    print("=" * 70)

    print("\n🔍 Testing error handling scenarios...")

    try:
        from claude_agent_sdk import CLIConnectionError, CLINotFoundError, ProcessError

        print("\n✅ Exception types imported:")
        print("   • CLINotFoundError - CLI not found in PATH")
        print("   • ProcessError - Process execution failure")
        print("   • CLIConnectionError - Connection failure")

        # Example error handling pattern
        try:
            async with ClaudeSDKClient() as client:
                await client.query("Test query")
                async for message in client.receive_response():
                    print(message)

        except CLINotFoundError:
            print("\n⚠️  Claude Code CLI not found in PATH")
            print("   Install Claude Code 2.0.0+ to use the SDK")

        except CLIConnectionError as e:
            print(f"\n⚠️  Connection error: {e}")
            print("   Check if Claude Code is running properly")

        except ProcessError as e:
            print(f"\n⚠️  Process error: {e}")
            print("   An error occurred during execution")

    except ImportError:
        print("\n⚠️  Exception types not available (SDK not installed)")
    except Exception as e:
        print(f"\n⚠️  Error during demonstration: {type(e).__name__}: {e}")
        print("   (This is expected if running outside Claude Code environment)")

    print("\n💡 Always use specific exception types for robust error handling")


# ============================================================================
# EXAMPLE 8: Multiple Tool Interactions
# ============================================================================


async def example_8_complex_workflow():
    """
    Demonstrate a complex workflow with multiple tool interactions.

    This shows how Claude can:
    - Chain multiple tool calls
    - Maintain context across turns
    - Make decisions based on tool results
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Complex Multi-Tool Workflow")
    print("=" * 70)

    server = create_sdk_mcp_server(
        name="workflow-tools",
        version="1.0.0",
        tools=[calculate_tool, get_weather_tool, store_data_tool],
    )

    options = ClaudeAgentOptions(
        system_prompt=(
            "You are a data processing assistant. "
            "Use the available tools to complete complex tasks efficiently."
        ),
        mcp_servers={"tools": server},
        allowed_tools=[
            "mcp__tools__calculate",
            "mcp__tools__get_weather",
            "mcp__tools__store_data",
        ],
    )

    try:
        print("\n🤖 Executing complex workflow...")

        async with ClaudeSDKClient(options=options) as client:
            # Complex multi-step query
            query_text = (
                "Please do the following in order: "
                "1. Calculate 25 + 75 "
                "2. Get weather for New York "
                "3. Store the calculation result with key 'sum' "
                "4. Store the weather condition with key 'ny_weather' "
                "5. Summarize what you did"
            )

            print(f"\n📤 Query: {query_text[:80]}...")

            await client.query(query_text)

            print("\n📥 Workflow execution:")
            async for message in client.receive_response():
                print(f"   {str(message)[:100]}...")

        print("\n✅ Complex workflow completed")
        print("💡 Claude can orchestrate multiple tools to achieve complex goals")

    except Exception as e:
        print(f"\n⚠️  Error: {e}")
        print("   (This is expected if running outside Claude Code environment)")


# ============================================================================
# EXAMPLE 9: Summary of Key Features
# ============================================================================


def example_9_feature_summary():
    """
    Display a comprehensive summary of Claude Agent SDK features.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 9: Feature Summary")
    print("=" * 70)

    features = {
        "Core Functions": [
            "query() - Simple async iterator for basic interactions",
            "ClaudeSDKClient - Advanced bidirectional conversations",
        ],
        "Custom Tools": [
            "@tool decorator - Define tools as Python functions",
            "create_sdk_mcp_server() - Create in-process MCP servers",
            "Type-safe parameters and return values",
            "Async/await support for I/O operations",
        ],
        "Hooks System": [
            "PreToolUse - Validate tools before execution",
            "HookMatcher - Pattern-based hook registration",
            "Permission control (allow/deny decisions)",
            "Deterministic processing and feedback",
        ],
        "Configuration (ClaudeAgentOptions)": [
            "system_prompt - Set agent behavior",
            "turn_limit - Control conversation length",
            "allowed_tools - Allowlist specific tools",
            "mcp_servers - Register tool servers",
            "hooks - Add validation and monitoring",
            "working_dir - Set working directory",
        ],
        "Advanced Features": [
            "Streaming input and output",
            "Stateful tool implementations",
            "Error handling with specific exceptions",
            "Concurrent tool execution",
            "In-process MCP servers (no subprocess overhead)",
        ],
        "Performance Benefits": [
            "Single Python process deployment",
            "No subprocess overhead",
            "Improved debugging capabilities",
            "Type-safe tool integration",
        ],
    }

    print("\n📚 Claude Agent SDK Feature Catalog:\n")

    for category, items in features.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  • {item}")

    print("\n" + "=" * 70)
    print("📖 Documentation: https://docs.claude.com/en/docs/agent-sdk/overview")
    print("💻 GitHub: https://github.com/anthropics/claude-agent-sdk-python")
    print("📦 PyPI: https://pypi.org/project/claude-agent-sdk/")
    print("=" * 70)


# ============================================================================
# Main Entry Point
# ============================================================================


async def main():
    """
    Main entry point that runs all demonstrations.

    Each example demonstrates a different aspect of the Claude Agent SDK.
    """
    print("\n" + "=" * 70)
    print("🚀 Claude Agent SDK for Python - Comprehensive Demonstration")
    print("=" * 70)
    print("\nThis demo showcases all key features of the Claude Agent SDK:")
    print("  • Simple query() function")
    print("  • ClaudeSDKClient for advanced usage")
    print("  • Custom tools with @tool decorator")
    print("  • SDK MCP servers (in-process)")
    print("  • Hooks for validation and control")
    print("  • Streaming input/output")
    print("  • Configuration options")
    print("  • Error handling")
    print("  • Complex multi-tool workflows")

    # Run all examples sequentially
    await example_1_basic_query()

    # Example 2 is the tool definitions (already shown)
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Custom Tools Defined")
    print("=" * 70)
    print("\n✅ Three custom tools defined using @tool decorator:")
    print("   • calculate_tool - Arithmetic operations")
    print("   • get_weather_tool - Weather information")
    print("   • store_data_tool - Stateful key-value storage")
    print("\n💡 Tools are async Python functions that Claude can invoke")
    print("   See lines 84-162 in the source code")

    create_custom_mcp_server()

    # Example 4 is the hook definitions (already shown)
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Hooks Defined")
    print("=" * 70)
    print("\n✅ Two hooks defined for validation and monitoring:")
    print("   • validate_bash_command - Security validation")
    print("   • log_tool_usage - Usage monitoring")
    print("\n💡 Hooks provide deterministic control over tool execution")
    print("   See lines 178-222 in the source code")

    await example_5_advanced_client()
    await example_6_streaming_input()
    await example_7_error_handling()
    await example_8_complex_workflow()
    example_9_feature_summary()

    print("\n" + "=" * 70)
    print("✨ All Demonstrations Completed!")
    print("=" * 70)
    print("\n🎯 Key Takeaways:")
    print("  1. Use query() for simple, stateless interactions")
    print("  2. Use ClaudeSDKClient for complex, stateful agents")
    print("  3. Create custom tools with @tool decorator")
    print("  4. Use SDK MCP servers for in-process performance")
    print("  5. Add hooks for validation and permission control")
    print("  6. Configure behavior with ClaudeAgentOptions")
    print("  7. Handle errors with specific exception types")
    print("  8. Stream input/output for real-time processing")
    print("\n💡 The Claude Agent SDK enables building powerful AI agents")
    print("   that can use tools, maintain state, and execute workflows!")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("Running Claude Agent SDK demonstration...")
    print("=" * 70)

    try:
        anyio.run(main)
    except KeyboardInterrupt:
        print("\n\n⚠️  Demonstration interrupted by user")
    except Exception as e:
        print(f"\n\n⚠️  Error: {type(e).__name__}: {e}")
        print("\nNote: This SDK requires Claude Code 2.0.0+ environment to run.")
        print("The code demonstrates the API structure and features.")
