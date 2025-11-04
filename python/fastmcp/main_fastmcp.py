"""
FastMCP Example: Building Model Context Protocol (MCP) Servers

This example demonstrates FastMCP, a Pythonic framework for building MCP servers.
MCP is a standardized protocol for providing context and tools to LLMs.

Key concepts illustrated:
1. Tools - Functions callable by LLM applications
2. Resources - Read-only data exposure with URI patterns
3. Prompts - Reusable message templates
4. Client - Connecting to and interacting with MCP servers
5. Context - Accessing server capabilities and session info
"""

import asyncio
import sys
from datetime import datetime
from typing import Annotated

from fastmcp import Context, FastMCP

# Fix Windows console encoding for emojis
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


def log(msg):
    """Helper function to print timestamped messages."""
    print(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] {msg}")


# Create a FastMCP server instance
mcp = FastMCP("Demo Server 🚀")


# Example 1: Basic Tool - Simple Calculator
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    result = a + b
    log(f"🔢 Tool 'add' called: {a} + {b} = {result}")
    return result


@mcp.tool()
def multiply(x: float, y: float) -> float:
    """Multiply two numbers.

    Args:
        x: First number
        y: Second number

    Returns:
        Product of x and y
    """
    result = x * y
    log(f"✖️  Tool 'multiply' called: {x} × {y} = {result}")
    return result


# Example 2: Tool with String Processing
@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse the given text.

    Args:
        text: Text to reverse

    Returns:
        Reversed text
    """
    result = text[::-1]
    log(f"🔄 Tool 'reverse_text' called: '{text}' → '{result}'")
    return result


# Example 3: Static Resource - Configuration Data
@mcp.resource("config://version")
def get_version() -> str:
    """Get the current version of the application."""
    version = "2.0.1"
    log(f"📋 Resource 'config://version' accessed → {version}")
    return version


@mcp.resource("config://settings")
def get_settings() -> dict:
    """Get application settings."""
    settings = {
        "max_connections": 100,
        "timeout": 30,
        "debug_mode": False,
    }
    log(f"⚙️  Resource 'config://settings' accessed → {settings}")
    return settings


# Example 4: Dynamic Resource with Parameters
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: Annotated[int, "User ID"]) -> dict:
    """Get user profile by ID.

    Args:
        user_id: The unique identifier for the user
    """
    # Simulate database lookup
    profiles = {
        1: {"name": "Alice", "role": "Engineer", "active": True},
        2: {"name": "Bob", "role": "Designer", "active": True},
        3: {"name": "Charlie", "role": "Manager", "active": False},
    }
    profile = profiles.get(user_id, {"error": "User not found"})
    log(f"👤 Resource 'users://{user_id}/profile' accessed → {profile}")
    return profile


# Example 5: Resource with Dynamic Template
@mcp.resource("data://{category}/{item_id}")
def get_data_item(
    category: Annotated[str, "Data category"],
    item_id: Annotated[int, "Item identifier"],
) -> dict:
    """Get a data item by category and ID.

    Args:
        category: Category name (e.g., 'products', 'orders')
        item_id: Item ID within the category
    """
    # Simulate data lookup
    data = {
        "category": category,
        "item_id": item_id,
        "timestamp": datetime.now().isoformat(),
        "data": f"Item {item_id} from {category}",
    }
    log(f"📦 Resource 'data://{category}/{item_id}' accessed → {data}")
    return data


# Example 6: Prompt Template
@mcp.prompt()
def code_review_prompt(language: str, code: str) -> str:
    """Generate a code review prompt.

    Args:
        language: Programming language
        code: Code to review
    """
    prompt = f"""Please review this {language} code:

```{language}
{code}
```

Focus on:
1. Code quality and best practices
2. Potential bugs or issues
3. Performance considerations
4. Readability and maintainability
"""
    log(f"📝 Prompt 'code_review_prompt' generated for {language}")
    return prompt


@mcp.prompt()
def summarize_prompt(text: str, max_words: int = 100) -> str:
    """Generate a text summarization prompt.

    Args:
        text: Text to summarize
        max_words: Maximum words in summary
    """
    prompt = f"Summarize the following text in {max_words} words or less:\n\n{text}"
    log(f"📄 Prompt 'summarize_prompt' generated (max {max_words} words)")
    return prompt


# Example 7: Tool with Context
@mcp.tool()
async def get_server_info(context: Context) -> dict:
    """Get information about the server using the Context object.

    Args:
        context: MCP context providing access to server capabilities
    """
    info = {
        "server_name": "Demo Server 🚀",
        "timestamp": datetime.now().isoformat(),
        "has_logging": True,
    }
    await context.info(f"Server info requested: {info}")
    log("ℹ️  Tool 'get_server_info' called with context")
    return info


# Example 8: Tool with Progress Reporting
@mcp.tool()
async def process_items(count: int, context: Context) -> str:
    """Process multiple items with progress reporting.

    Args:
        count: Number of items to process
        context: MCP context for progress reporting
    """
    log(f"⚡ Tool 'process_items' called: processing {count} items")

    for i in range(1, count + 1):
        await context.info(f"Processing item {i}/{count}")
        await asyncio.sleep(0.1)  # Simulate work

        # Report progress
        progress = i / count
        log(f"   📊 Progress: {i}/{count} ({progress*100:.0f}%)")

    result = f"Successfully processed {count} items"
    log("✅ Tool 'process_items' completed")
    return result


# Demonstration function
async def demonstrate_server():
    """Demonstrate the MCP server capabilities."""
    log("=" * 70)
    log("🚀 FastMCP Server Demonstration")
    log("=" * 70)

    # Import client here to demonstrate usage
    from fastmcp import Client

    log("\n📡 Starting MCP server and client...")

    # Connect to our server using the in-memory client
    async with Client(mcp) as client:
        log("✅ Client connected to server\n")

        # Example 1: List available tools
        log("=" * 70)
        log("EXAMPLE 1: Discovering Tools")
        log("=" * 70)
        tools = await client.list_tools()
        log(f"📋 Available tools ({len(tools)}):")
        for tool in tools:
            log(f"   • {tool.name}: {tool.description.split('.')[0]}")

        # Example 2: Call calculator tools
        log("\n" + "=" * 70)
        log("EXAMPLE 2: Using Calculator Tools")
        log("=" * 70)
        result1 = await client.call_tool("add", {"a": 15, "b": 27})
        log(f"   Result: {result1}")

        result2 = await client.call_tool("multiply", {"x": 12.5, "y": 4.0})
        log(f"   Result: {result2}")

        # Example 3: String processing tool
        log("\n" + "=" * 70)
        log("EXAMPLE 3: String Processing Tool")
        log("=" * 70)
        result3 = await client.call_tool(
            "reverse_text", {"text": "FastMCP is awesome!"}
        )
        log(f"   Result: {result3}")

        # Example 4: List available resources
        log("\n" + "=" * 70)
        log("EXAMPLE 4: Discovering Resources")
        log("=" * 70)
        resources = await client.list_resources()
        log(f"📋 Available resources ({len(resources)}):")
        for resource in resources:
            log(f"   • {resource.uri}: {resource.description.split('.')[0]}")

        # Example 5: Access static resources
        log("\n" + "=" * 70)
        log("EXAMPLE 5: Accessing Static Resources")
        log("=" * 70)
        version = await client.read_resource("config://version")
        log(f"   Version: {version}")

        settings = await client.read_resource("config://settings")
        log(f"   Settings: {settings}")

        # Example 6: Access dynamic resources
        log("\n" + "=" * 70)
        log("EXAMPLE 6: Accessing Dynamic Resources (Parameterized)")
        log("=" * 70)
        profile1 = await client.read_resource("users://1/profile")
        log(f"   User 1 Profile: {profile1}")

        profile2 = await client.read_resource("users://2/profile")
        log(f"   User 2 Profile: {profile2}")

        data_item = await client.read_resource("data://products/42")
        log(f"   Data Item: {data_item}")

        # Example 7: List available prompts
        log("\n" + "=" * 70)
        log("EXAMPLE 7: Discovering Prompts")
        log("=" * 70)
        prompts = await client.list_prompts()
        log(f"📋 Available prompts ({len(prompts)}):")
        for prompt in prompts:
            log(f"   • {prompt.name}: {prompt.description.split('.')[0]}")

        # Example 8: Use prompt templates
        log("\n" + "=" * 70)
        log("EXAMPLE 8: Using Prompt Templates")
        log("=" * 70)
        code_prompt = await client.get_prompt(
            "code_review_prompt",
            {"language": "python", "code": "def hello():\n    print('Hello!')"},
        )
        log("   Generated code review prompt (first 100 chars):")
        log(f"   {str(code_prompt)[:100]}...")

        # Example 9: Tool with context
        log("\n" + "=" * 70)
        log("EXAMPLE 9: Tool with Context Access")
        log("=" * 70)
        server_info = await client.call_tool("get_server_info", {})
        log(f"   Server Info: {server_info}")

        # Example 10: Tool with progress reporting
        log("\n" + "=" * 70)
        log("EXAMPLE 10: Tool with Progress Reporting")
        log("=" * 70)
        process_result = await client.call_tool("process_items", {"count": 5})
        log(f"   Final Result: {process_result}")

    log("\n" + "=" * 70)
    log("✨ All demonstrations completed successfully!")
    log("=" * 70)


async def main():
    """Main entry point for the demonstration."""
    await demonstrate_server()


if __name__ == "__main__":
    asyncio.run(main())
