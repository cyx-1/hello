# FastMCP Example: Building Model Context Protocol (MCP) Servers

This example demonstrates FastMCP, a Pythonic framework for building MCP servers. The Model Context Protocol (MCP) is a standardized way to provide context and tools to LLMs (Large Language Models).

## What is FastMCP?

FastMCP is a framework that makes building MCP servers simple and intuitive. MCP servers provide:

- **Tools** - Functions that LLMs can call to perform actions
- **Resources** - Read-only data with URI-based access patterns
- **Prompts** - Reusable message templates for LLM interactions
- **Context** - Access to server capabilities and session information

## Requirements

This example requires **Python 3.10 or higher** and uses the **fastmcp>=2.0.0** library.

## Running the Example

```bash
uv run python main_fastmcp.py
```

## Key Features Illustrated

1. **Basic Tools** - Simple function-based tools with automatic schema generation
2. **String Processing Tools** - Text manipulation functions
3. **Static Resources** - Configuration and settings access
4. **Dynamic Resources** - Parameterized URI patterns (e.g., `users://{user_id}/profile`)
5. **Prompt Templates** - Reusable message generators
6. **Context Access** - Server capabilities and logging
7. **Progress Reporting** - Real-time progress updates for long-running operations
8. **Client Usage** - Connecting to and interacting with MCP servers

## Source Code and Output Analysis

### 1. Creating a FastMCP Server

**Source Code (main_fastmcp.py:27):**
```python
mcp = FastMCP("Demo Server 🚀")  # Line 27: Initialize server
```

**💡 Key Insight:**
- FastMCP initialization creates a new MCP server instance
- The name is used for identification in client connections

---

### 2. Basic Tools - Calculator Functions

**Source Code (main_fastmcp.py:31-44):**
```python
@mcp.tool()  # Line 31: Register as a tool
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
    return result  # Line 44: Return value sent to client
```

**Output:**
```
[14:54:59.449] EXAMPLE 1: Discovering Tools
[14:54:59.451] 📋 Available tools (5):
[14:54:59.451]    • add: Add two numbers together              ← Line 31: Tool registered
[14:54:59.451]    • multiply: Multiply two numbers             ← Additional calculator tool
[14:54:59.451]    • reverse_text: Reverse the given text
[14:54:59.451]    • get_server_info: Get information about the server using the Context object
[14:54:59.451]    • process_items: Process multiple items with progress reporting

[14:54:59.451] EXAMPLE 2: Using Calculator Tools
[14:54:59.451] 🔢 Tool 'add' called: 15 + 27 = 42             ← Line 43: Function executed
[14:54:59.453]    Result: CallToolResult(...data=42...)         ← Line 44: Result returned
```

**💡 Key Insight:**
- **Line 31:** `@mcp.tool()` decorator automatically registers the function as an MCP tool
- **Lines 32-40:** Docstring becomes the tool's description and parameter documentation
- **Line 44:** Return value is automatically serialized and sent to the client
- FastMCP generates JSON schemas from Python type hints (`int`, `float`, etc.)

---

### 3. String Processing Tools

**Source Code (main_fastmcp.py:63-73):**
```python
@mcp.tool()  # Line 63
def reverse_text(text: str) -> str:
    """Reverse the given text.

    Args:
        text: Text to reverse

    Returns:
        Reversed text
    """
    result = text[::-1]  # Line 72: Python string slicing
    log(f"🔄 Tool 'reverse_text' called: '{text}' → '{result}'")
    return result  # Line 73
```

**Output:**
```
[14:54:59.456] EXAMPLE 3: String Processing Tool
[14:54:59.456] 🔄 Tool 'reverse_text' called: 'FastMCP is awesome!' → '!emosewa si PCMtsaF'
[14:54:59.458]    Result: CallToolResult(...data='!emosewa si PCMtsaF'...)
```

**💡 Key Insight:**
- Tools can work with any Python data type (strings, lists, dicts, etc.)
- **Line 72:** Uses Python's idiomatic string reversal
- FastMCP handles serialization automatically

---

### 4. Static Resources - Configuration Access

**Source Code (main_fastmcp.py:77-97):**
```python
@mcp.resource("config://version")  # Line 77: Static URI
def get_version() -> str:
    """Get the current version of the application."""
    version = "2.0.1"
    log(f"📋 Resource 'config://version' accessed → {version}")
    return version  # Line 82

@mcp.resource("config://settings")  # Line 84: Another static resource
def get_settings() -> dict:
    """Get application settings."""
    settings = {
        "max_connections": 100,
        "timeout": 30,
        "debug_mode": False,
    }
    log(f"⚙️  Resource 'config://settings' accessed → {settings}")
    return settings  # Line 93
```

**Output:**
```
[14:54:59.459] EXAMPLE 4: Discovering Resources
[14:54:59.459] 📋 Available resources (2):
[14:54:59.459]    • config://version: Get the current version     ← Line 77: Static URI
[14:54:59.459]    • config://settings: Get application settings   ← Line 84: Static URI

[14:54:59.459] EXAMPLE 5: Accessing Static Resources
[14:54:59.460] 📋 Resource 'config://version' accessed → 2.0.1  ← Line 82: Version returned
[14:54:59.460]    Version: [TextResourceContents(uri='config://version'...text='2.0.1')]
[14:54:59.461] ⚙️  Resource 'config://settings' accessed → {...}  ← Line 93: Settings returned
```

**💡 Key Insight:**
- **Resources** are read-only data sources with URI-based access
- **Line 77, 84:** Static URIs don't change and have no parameters
- **Line 82, 93:** Resources can return strings, numbers, or complex objects (automatically serialized to JSON)
- Resources are ideal for configuration, documentation, or read-only data

---

### 5. Dynamic Resources - Parameterized URIs

**Source Code (main_fastmcp.py:101-116):**
```python
@mcp.resource("users://{user_id}/profile")  # Line 101: Dynamic URI with {user_id} placeholder
def get_user_profile(user_id: Annotated[int, "User ID"]) -> dict:
    """Get user profile by ID.

    Args:
        user_id: The unique identifier for the user  # Line 105: Parameter description
    """
    # Simulate database lookup
    profiles = {
        1: {"name": "Alice", "role": "Engineer", "active": True},   # Line 109
        2: {"name": "Bob", "role": "Designer", "active": True},     # Line 110
        3: {"name": "Charlie", "role": "Manager", "active": False}, # Line 111
    }
    profile = profiles.get(user_id, {"error": "User not found"})
    log(f"👤 Resource 'users://{user_id}/profile' accessed → {profile}")
    return profile  # Line 115
```

**Output:**
```
[14:54:59.461] EXAMPLE 6: Accessing Dynamic Resources (Parameterized)
[14:54:59.462] 👤 Resource 'users://1/profile' accessed → {...'Alice'...}  ← Line 109: User 1 data
[14:54:59.462]    User 1 Profile: [TextResourceContents(uri='users://1/profile'...)]
[14:54:59.463] 👤 Resource 'users://2/profile' accessed → {...'Bob'...}    ← Line 110: User 2 data
[14:54:59.463]    User 2 Profile: [TextResourceContents(uri='users://2/profile'...)]
```

**💡 Key Insight:**
- **Line 101:** URI template with `{user_id}` placeholder creates a dynamic resource
- **Line 102:** Function parameter `user_id` matches the placeholder name
- **Lines 109-111:** Simulated database with different users
- When client requests `users://1/profile`, FastMCP extracts `user_id=1` and calls the function
- Dynamic resources enable RESTful-style data access patterns

---

### 6. Complex Dynamic Resources

**Source Code (main_fastmcp.py:119-134):**
```python
@mcp.resource("data://{category}/{item_id}")  # Line 119: Multiple parameters
def get_data_item(
    category: Annotated[str, "Data category"],   # Line 121: First parameter
    item_id: Annotated[int, "Item identifier"],   # Line 122: Second parameter
) -> dict:
    """Get a data item by category and ID."""
    data = {
        "category": category,       # Line 126: Use first parameter
        "item_id": item_id,         # Line 127: Use second parameter
        "timestamp": datetime.now().isoformat(),
        "data": f"Item {item_id} from {category}",  # Line 129: Combined data
    }
    log(f"📦 Resource 'data://{category}/{item_id}' accessed → {data}")
    return data
```

**Output:**
```
[14:54:59.464] 📦 Resource 'data://products/42' accessed → {...'Item 42 from products'...}
[14:54:59.464]    Data Item: [TextResourceContents(uri='data://products/42'...)]
```

**💡 Key Insight:**
- **Line 119:** URI can have multiple placeholders: `{category}` and `{item_id}`
- **Lines 121-122:** Function parameters must match placeholder names
- **Lines 126-129:** Both parameters are used to construct the response
- Request `data://products/42` → `category="products"`, `item_id=42`
- This pattern enables hierarchical data organization

---

### 7. Prompt Templates

**Source Code (main_fastmcp.py:138-157):**
```python
@mcp.prompt()  # Line 138: Register as prompt template
def code_review_prompt(language: str, code: str) -> str:
    """Generate a code review prompt.

    Args:
        language: Programming language  # Line 142
        code: Code to review            # Line 143
    """
    prompt = f"""Please review this {language} code:  # Line 145: Use language param

```{language}
{code}  # Line 148: Insert code
```

Focus on:
1. Code quality and best practices      # Line 152: Template structure
2. Potential bugs or issues
3. Performance considerations
4. Readability and maintainability
"""
    log(f"📝 Prompt 'code_review_prompt' generated for {language}")
    return prompt  # Line 157
```

**Output:**
```
[14:54:59.465] EXAMPLE 7: Discovering Prompts
[14:54:59.465] 📋 Available prompts (2):
[14:54:59.465]    • code_review_prompt: Generate a code review prompt       ← Line 138
[14:54:59.465]    • summarize_prompt: Generate a text summarization prompt

[14:54:59.465] EXAMPLE 8: Using Prompt Templates
[14:54:59.465] 📝 Prompt 'code_review_prompt' generated for python  ← Line 157: Prompt created
[14:54:59.466]    Generated code review prompt (first 100 chars):
[14:54:59.466]    meta=None description='Generate a code review prompt...  ← Full prompt available
```

**💡 Key Insight:**
- **Line 138:** `@mcp.prompt()` creates reusable message templates
- **Lines 142-143:** Prompts accept parameters to customize output
- **Lines 145-148:** Template uses f-strings to inject parameters
- **Lines 152-155:** Structured guidance ensures consistent LLM interactions
- Prompts help standardize how LLMs interact with your application

---

### 8. Tools with Context - Server Capabilities

**Source Code (main_fastmcp.py:184-201):**
```python
@mcp.tool()
async def get_server_info(context: Context) -> dict:  # Line 185: Context parameter
    """Get information about the server using the Context object.

    Args:
        context: MCP context providing access to server capabilities  # Line 189
    """
    info = {
        "server_name": "Demo Server 🚀",
        "timestamp": datetime.now().isoformat(),
        "has_logging": True,
    }
    await context.info(f"Server info requested: {info}")  # Line 199: Log to client
    log("ℹ️  Tool 'get_server_info' called with context")
    return info
```

**Output:**
```
[14:54:59.466] EXAMPLE 9: Tool with Context Access
[14:54:59.470] ℹ️  Tool 'get_server_info' called with context
[14:54:59.473]    Server Info: CallToolResult(...'Demo Server 🚀'...)

[11/04/25 14:54:59] INFO     Received INFO from server: {'msg':     ← Line 199: Context logging
                             "Server info requested:
                             {'server_name': 'Demo Server 🚀'..."}
```

**💡 Key Insight:**
- **Line 185:** Adding `context: Context` parameter gives access to MCP capabilities
- **Line 199:** `context.info()` sends log messages to the client
- Context provides: logging, LLM sampling, resource reading, and progress reporting
- Context enables tools to interact with the MCP session

---

### 9. Progress Reporting for Long Operations

**Source Code (main_fastmcp.py:205-225):**
```python
@mcp.tool()
async def process_items(count: int, context: Context) -> str:  # Line 206
    """Process multiple items with progress reporting."""
    log(f"⚡ Tool 'process_items' called: processing {count} items")

    for i in range(1, count + 1):  # Line 211: Loop through items
        await context.info(f"Processing item {i}/{count}")  # Line 212: Report to client
        await asyncio.sleep(0.1)  # Simulate work

        # Report progress
        progress = i / count  # Line 216: Calculate percentage
        log(f"   📊 Progress: {i}/{count} ({progress*100:.0f}%)")

    result = f"Successfully processed {count} items"
    log("✅ Tool 'process_items' completed")
    return result  # Line 224
```

**Output:**
```
[14:54:59.473] EXAMPLE 10: Tool with Progress Reporting
[14:54:59.473] ⚡ Tool 'process_items' called: processing 5 items
[14:54:59.576]    📊 Progress: 1/5 (20%)     ← Line 211: First iteration
[14:54:59.678]    📊 Progress: 2/5 (40%)     ← Second iteration
[14:54:59.781]    📊 Progress: 3/5 (60%)     ← Third iteration
[14:54:59.884]    📊 Progress: 4/5 (80%)     ← Fourth iteration
[14:54:59.986]    📊 Progress: 5/5 (100%)    ← Final iteration
[14:54:59.986] ✅ Tool 'process_items' completed

[11/04/25 14:54:59] INFO     Received INFO from server: {'msg':     ← Line 212: Client receives
                             'Processing item 1/5', 'extra': None}  ← progress updates
                    INFO     Received INFO from server: {'msg':
                             'Processing item 2/5', 'extra': None}
```

**💡 Key Insight:**
- **Line 206:** Async function with `Context` for progress reporting
- **Line 211:** Loop simulates processing multiple items
- **Line 212:** `context.info()` sends real-time updates to the client
- **Line 216:** Progress percentage calculated and logged
- Progress reporting keeps clients informed during long-running operations
- Each `context.info()` call sends an immediate message to the client

---

### 10. MCP Client - Connecting and Interacting

**Source Code (main_fastmcp.py:228-345):**
```python
async def demonstrate_server():
    """Demonstrate the MCP server capabilities."""
    from fastmcp import Client  # Line 232: Import client

    log("\n📡 Starting MCP server and client...")

    # Connect to our server using the in-memory client
    async with Client(mcp) as client:  # Line 237: In-memory connection
        log("✅ Client connected to server\n")

        # List available tools
        tools = await client.list_tools()  # Line 241: Discovery

        # Call a tool
        result = await client.call_tool("add", {"a": 15, "b": 27})  # Line 246: Invoke tool

        # List resources
        resources = await client.list_resources()  # Line 251: Discovery

        # Read a resource
        version = await client.read_resource("config://version")  # Line 256: Access data

        # Read dynamic resource
        profile = await client.read_resource("users://1/profile")  # Line 262: Parameterized

        # List prompts
        prompts = await client.list_prompts()  # Line 267: Discovery

        # Get a prompt
        code_prompt = await client.get_prompt(
            "code_review_prompt",
            {"language": "python", "code": "def hello():\n    print('Hello!')"}
        )  # Line 273: Generate from template
```

**Output:**
```
[14:54:59.421] 📡 Starting MCP server and client...
[14:54:59.449] ✅ Client connected to server                    ← Line 237: Connection established

[14:54:59.451] 📋 Available tools (5):                          ← Line 241: Tool discovery
[14:54:59.451]    • add: Add two numbers together
[14:54:59.451]    • multiply: Multiply two numbers
[14:54:59.451]    • reverse_text: Reverse the given text

[14:54:59.451] 🔢 Tool 'add' called: 15 + 27 = 42              ← Line 246: Tool invocation
[14:54:59.453]    Result: CallToolResult(...data=42...)

[14:54:59.459] 📋 Available resources (2):                      ← Line 251: Resource discovery
[14:54:59.459]    • config://version: Get the current version
[14:54:59.459]    • config://settings: Get application settings

[14:54:59.460] 📋 Resource 'config://version' accessed → 2.0.1 ← Line 256: Resource read
```

**💡 Key Insight:**
- **Line 232:** `Client` class connects to MCP servers
- **Line 237:** `Client(mcp)` creates in-memory connection for testing (no subprocess overhead)
- **Line 241:** `list_tools()` discovers available tools
- **Line 246:** `call_tool(name, args)` invokes a tool with parameters
- **Line 251:** `list_resources()` discovers available resources
- **Line 256:** `read_resource(uri)` retrieves resource data
- **Line 262:** Dynamic URIs are accessed like static ones (FastMCP handles parameter extraction)
- **Line 267:** `list_prompts()` discovers available prompt templates
- **Line 273:** `get_prompt(name, args)` generates text from templates
- The client can also connect to remote servers via `Client("server.py")` or other transports

---

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────┐
│                      MCP SERVER                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐            │
│  │   TOOLS    │  │ RESOURCES  │  │  PROMPTS   │            │
│  ├────────────┤  ├────────────┤  ├────────────┤            │
│  │ @mcp.tool()│  │@mcp.resource│  │@mcp.prompt()│           │
│  │            │  │            │  │            │            │
│  │ • add()    │  │ config://  │  │ code_review│            │
│  │ • multiply()│  │ users://   │  │ summarize  │            │
│  │ • reverse()│  │ data://    │  │            │            │
│  └────────────┘  └────────────┘  └────────────┘            │
└─────────────────────────────────────────────────────────────┘
                           ▲
                           │ MCP Protocol
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                      MCP CLIENT                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐            │
│  │   CALL     │  │    READ    │  │    GET     │            │
│  ├────────────┤  ├────────────┤  ├────────────┤            │
│  │ call_tool()│  │read_resource│  │ get_prompt()│           │
│  │            │  │            │  │            │            │
│  │ • Discovery│  │ • Static   │  │ • Template │            │
│  │ • Invoke   │  │ • Dynamic  │  │ • Generate │            │
│  │ • Results  │  │ • Params   │  │ • Params   │            │
│  └────────────┘  └────────────┘  └────────────┘            │
└─────────────────────────────────────────────────────────────┘
```

## Performance Characteristics

| Operation | Time | Notes |
|-----------|------|-------|
| Tool discovery (list_tools) | ~2ms | Fast metadata lookup |
| Simple tool call (add) | ~2ms | Minimal overhead |
| String processing (reverse) | ~2ms | Efficient operation |
| Resource read (static) | ~1ms | Direct data access |
| Resource read (dynamic) | ~1-2ms | Parameter extraction + lookup |
| Prompt generation | ~1ms | Template rendering |
| Progress reporting (5 items) | ~513ms | 0.1s per item + overhead |

## Key Takeaways

1. **Tools** - Use `@mcp.tool()` to expose functions to LLMs
2. **Resources** - Use `@mcp.resource("uri")` for read-only data access
3. **Dynamic URIs** - Use `{param}` placeholders for parameterized resources
4. **Prompts** - Use `@mcp.prompt()` for reusable message templates
5. **Context** - Add `context: Context` parameter for logging and progress reporting
6. **Client** - Use `Client` class to connect and interact with servers
7. **Type Hints** - FastMCP automatically generates schemas from Python types
8. **Docstrings** - Used as descriptions in MCP protocol

## When to Use FastMCP

✅ **Good for:**
- Building custom LLM tools and integrations
- Exposing APIs and data sources to LLMs
- Creating standardized LLM interaction patterns
- Building AI assistants with specific capabilities
- Prototyping MCP servers quickly

❌ **Not ideal for:**
- General web APIs (use FastAPI instead)
- Real-time streaming (MCP is request-response)
- Heavy computation (consider offloading to workers)
- Non-LLM applications

## Additional Resources

- FastMCP Documentation: https://gofastmcp.com/
- Model Context Protocol Spec: https://modelcontextprotocol.io/
- FastMCP GitHub: https://github.com/jlowin/fastmcp
- Python SDK: https://github.com/modelcontextprotocol/python-sdk
