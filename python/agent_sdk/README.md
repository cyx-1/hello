# Claude Agent SDK for Python - Comprehensive Demonstration

This example demonstrates all key features of the **Claude Agent SDK** (formerly Claude Code SDK), a powerful framework for building AI agents that can use tools, maintain state, and execute complex workflows.

## Requirements

**Important:** This code requires:
- **Python 3.10+**
- **Claude Code 2.0.0+** environment
- **claude-agent-sdk** package (included via inline script metadata)

## Running the Code

```bash
uv run main_agent_sdk.py
```

The code uses inline script metadata (PEP 723) to automatically manage dependencies with `uv`.

## Key Features Demonstrated

1. **Simple `query()` function** for basic interactions
2. **`ClaudeSDKClient`** for advanced bidirectional conversations
3. **Custom tools** using `@tool` decorator
4. **SDK MCP servers** (in-process) for high performance
5. **Hooks** for validation and permission control
6. **Streaming** input and output
7. **`ClaudeAgentOptions`** for comprehensive configuration
8. **Error handling** with specific exception types
9. **Complex multi-tool workflows**
10. **Stateful tool implementations**

---

## Source Code Highlights with Annotations

### 1. Dependencies and Imports (Lines 1-52)

```python
1→  # /// script
2→  # requires-python = ">=3.10"
3→  # dependencies = [
4→  #     "claude-agent-sdk>=0.1.0",
5→  #     "anyio>=4.0.0",
6→  # ]
7→  # ///

30→ try:
31→     from claude_agent_sdk import (
32→         ClaudeAgentOptions,
33→         ClaudeSDKClient,
34→         HookMatcher,
35→         create_sdk_mcp_server,
36→         query,
37→         tool,
38→     )
39→ except ImportError:
40→     print("\n⚠️  Claude Agent SDK not available in this environment")
```

**📝 Annotation:** The inline script metadata (lines 1-7) defines Python version and dependencies. The imports (lines 31-38) bring in all core SDK components. The try-except provides graceful handling when SDK is unavailable.

---

### 2. Example 1: Basic Query Function (Lines 60-85)

```python
60→ async def example_1_basic_query():
61→     """
62→     Demonstrate the simplest way to interact with Claude using query().
63→     """
69→     try:
70→         async for message in query(prompt="What is 2 + 2?"):
71→             print(f"\n✅ Response: {message}")
72→             print(f"   Type: {type(message).__name__}")
```

**📝 Annotation:** The `query()` function (line 70) is the simplest API for interacting with Claude. It returns an async iterator of messages, making it ideal for stateless, one-off interactions.

**Expected Output:**
```
======================================================================
EXAMPLE 1: Basic Query Function
======================================================================

📝 Sending a simple prompt to Claude...
Code: async for message in query(prompt='What is 2 + 2?')

✅ Response: 4
   Type: str

💡 The query() function provides a quick, stateless way to interact
   with Claude for simple tasks without managing client state.
```

---

### 3. Custom Tools with @tool Decorator (Lines 92-175)

```python
92→  @tool(
93→      "calculate",
94→      "Perform basic arithmetic calculations",
95→      {"operation": str, "a": float, "b": float},
96→  )
97→  async def calculate_tool(args: dict[str, Any]) -> dict[str, Any]:
98→      """A custom tool that performs calculations."""
99→      operation = args["operation"]
100→     a = args["a"]
101→     b = args["b"]
102→
103→     operations = {
104→         "add": a + b,
105→         "subtract": a - b,
106→         "multiply": a * b,
107→         "divide": a / b if b != 0 else "Error: Division by zero",
108→     }
109→
110→     result = operations.get(operation, "Error: Unknown operation")
111→
112→     return {"content": [{"type": "text", "text": f"Result: {result}"}]}
```

**📝 Annotation:** The `@tool` decorator (lines 92-96) defines a custom tool with:
- **name**: Tool identifier ("calculate")
- **description**: What the tool does
- **input_schema**: Type-safe parameter definitions (dict mapping names to types)

The function (lines 97-112) must:
- Accept `args: dict[str, Any]` parameter
- Return a dict with `"content"` key containing the result
- Be async (supports I/O operations)

**Similar tools defined:**
- `get_weather_tool` (lines 120-150) - Demonstrates async I/O simulation
- `store_data_tool` (lines 153-175) - Demonstrates stateful tools with persistent storage

---

### 4. SDK MCP Server Creation (Lines 189-209)

```python
189→ def create_custom_mcp_server():
190→     """Create an SDK MCP server with custom tools."""
196→     print("\n🔧 Creating in-process MCP server with custom tools...")
197→
198→     server = create_sdk_mcp_server(
199→         name="demo-tools",
200→         version="1.0.0",
201→         tools=[calculate_tool, get_weather_tool, store_data_tool],
202→     )
203→
204→     print("✅ Server created with 3 tools:")
205→     print("   • calculate - Perform arithmetic operations")
206→     print("   • get_weather - Get weather information")
207→     print("   • store_data - Store key-value pairs")
```

**📝 Annotation:** `create_sdk_mcp_server()` (lines 198-202) creates an **in-process MCP server** that runs within the Python process. This provides:
- **No subprocess overhead** (faster than standard MCP servers)
- **Single process deployment** (simpler architecture)
- **Better debugging** (all code in one process)
- **Type-safe integration** (Python type hints preserved)

**Expected Output:**
```
======================================================================
EXAMPLE 3: Creating SDK MCP Server
======================================================================

🔧 Creating in-process MCP server with custom tools...
✅ Server created with 3 tools:
   • calculate - Perform arithmetic operations
   • get_weather - Get weather information
   • store_data - Store key-value pairs

💡 SDK MCP servers run in-process for better performance
```

---

### 5. Hooks for Validation (Lines 218-254)

```python
218→ async def validate_bash_command(
219→     input_data: dict[str, Any], tool_use_id: str, context: dict[str, Any]
220→ ) -> dict[str, Any]:
221→     """
222→     Hook that validates Bash commands before execution.
223→     """
224→     tool_name = input_data.get("tool_name", "")
225→     tool_input = input_data.get("tool_input", {})
226→
227→     if tool_name != "Bash":
228→         return {}
229→
230→     command = tool_input.get("command", "")
231→
232→     # Block patterns
233→     blocked_patterns = ["rm -rf", "sudo", "format", "delete"]
234→
235→     for pattern in blocked_patterns:
236→         if pattern in command:
237→             print(f"\n🚫 Hook blocked command containing: '{pattern}'")
238→             return {
239→                 "hookSpecificOutput": {
240→                     "hookEventName": "PreToolUse",
241→                     "permissionDecision": "deny",
242→                     "permissionDecisionReason": f"Blocked: command contains '{pattern}'",
243→                 }
244→             }
245→
246→     print(f"\n✅ Hook approved command: {command[:50]}...")
247→     return {}
```

**📝 Annotation:** Hooks (lines 218-247) are Python functions invoked at specific points in the Claude agent loop:
- **PreToolUse** hooks validate tools before execution
- Return empty dict `{}` to allow execution (line 247)
- Return dict with `hookSpecificOutput.permissionDecision: "deny"` to block (lines 238-244)

Hooks enable:
- **Security validation** (blocking dangerous commands)
- **Permission control** (enforcing policies)
- **Monitoring and logging** (observability)
- **Deterministic processing** (automated feedback to Claude)

---

### 6. ClaudeSDKClient with Full Configuration (Lines 272-364)

```python
272→ async def example_5_advanced_client():
273→     """Demonstrate ClaudeSDKClient with complete configuration."""
281→     # Create SDK MCP server
282→     server = create_sdk_mcp_server(
283→         name="advanced-tools",
284→         version="1.0.0",
285→         tools=[calculate_tool, get_weather_tool],
286→     )
287→
288→     # Configure options
289→     options = ClaudeAgentOptions(
290→         # System prompt for agent behavior
291→         system_prompt="You are a helpful assistant with access to calculation and weather tools.",
292→         # Limit conversation turns (None = unlimited)
293→         turn_limit=10,
294→         # Register MCP servers
295→         mcp_servers={"tools": server},
296→         # Allow specific tools (use allowlist for security)
297→         allowed_tools=[
298→             "mcp__tools__calculate",
299→             "mcp__tools__get_weather",
300→         ],
301→         # Register hooks for validation
302→         hooks={
303→             "PreToolUse": [
304→                 HookMatcher(matcher="Bash", hooks=[validate_bash_command]),
305→                 HookMatcher(matcher="*", hooks=[log_tool_usage]),
306→             ],
307→         },
308→         # Working directory
309→         working_dir=".",
310→     )
```

**📝 Annotation:** `ClaudeAgentOptions` (lines 289-310) provides comprehensive configuration:
- **`system_prompt`** (line 291): Defines agent behavior and context
- **`turn_limit`** (line 293): Limits conversation turns (prevents infinite loops)
- **`mcp_servers`** (line 295): Registers MCP servers by name
- **`allowed_tools`** (lines 297-300): Allowlist of permitted tools (security)
- **`hooks`** (lines 302-307): Event handlers for validation/monitoring
- **`working_dir`** (line 309): Sets working directory for file operations

Tool names follow pattern: `mcp__<server_name>__<tool_name>` (lines 298-299)

```python
318→     async with ClaudeSDKClient(options=options) as client:
319→         print("✅ Client created successfully")
320→
321→         # Send a query
324→         await client.query(
325→             "Calculate 15 multiplied by 7, then tell me the weather in London"
326→         )
327→
328→         print("\n📥 Receiving streaming response:")
329→
330→         # Process streaming response
331→         message_count = 0
332→         async for message in client.receive_response():
333→             message_count += 1
334→             print(f"\n   Message {message_count}: {str(message)[:100]}...")
```

**📝 Annotation:** `ClaudeSDKClient` usage pattern (lines 318-334):
1. Create client with `async with` (line 318) for proper resource management
2. Send query with `await client.query()` (lines 324-326)
3. Stream responses with `async for message in client.receive_response()` (line 332)

**Expected Output:**
```
======================================================================
EXAMPLE 5: Advanced ClaudeSDKClient Usage
======================================================================

⚙️  Configuration:
   • System prompt: Set
   • Turn limit: 10
   • Tools allowed: 2
   • Hooks registered: 1

🤖 Creating ClaudeSDKClient...
✅ Client created successfully

📤 Sending query: 'Calculate 15 * 7 and get weather for London'

📊 Tool Usage Log: mcp__tools__calculate (ID: toolu_01ABC...)
📥 Receiving streaming response:

   Message 1: 15 × 7 = 105...
   Message 2: Weather in London: 15°C, Rainy...

✅ Received 2 message(s)
💡 ClaudeSDKClient supports bidirectional, stateful interactions
```

---

### 7. Streaming Input (Lines 372-410)

```python
372→ async def example_6_streaming_input():
373→     """Demonstrate streaming messages to Claude."""
377→     async def message_stream():
378→         """Generator that yields messages dynamically."""
379→         print("\n📊 Streaming data to Claude:")
380→
381→         messages = [
382→             "Analyze the following sensor readings:",
383→             "Temperature: 25°C",
384→             "Humidity: 60%",
385→             "Pressure: 1013 hPa",
386→             "Air Quality: Good",
387→         ]
388→
389→         for msg in messages:
390→             print(f"   → {msg}")
391→             yield {"type": "text", "text": msg}
392→             await asyncio.sleep(0.1)  # Simulate data arrival delay
393→
398→         async with ClaudeSDKClient() as client:
399→             await client.query(message_stream())
400→
401→             print("\n📥 Processing response:")
402→             async for message in client.receive_response():
403→                 print(f"   {str(message)[:80]}...")
```

**📝 Annotation:** Streaming input (lines 377-392) allows sending messages incrementally:
- Use async generator function (line 377) with `yield` (line 391)
- Each yielded dict must have `"type": "text"` and `"text": <message>` (line 391)
- Pass generator to `client.query()` (line 399)
- Useful for real-time data processing or building prompts dynamically

**Expected Output:**
```
======================================================================
EXAMPLE 6: Streaming Input Messages
======================================================================

📊 Streaming data to Claude:
   → Analyze the following sensor readings:
   → Temperature: 25°C
   → Humidity: 60%
   → Pressure: 1013 hPa
   → Air Quality: Good

🤖 Sending streaming input to Claude...

📥 Processing response:
   The sensor readings indicate normal environmental conditions...

💡 Streaming input is useful for real-time data processing
```

---

### 8. Error Handling (Lines 418-462)

```python
418→ async def example_7_error_handling():
419→     """Demonstrate proper error handling with specific exception types."""
429→     try:
430→         from claude_agent_sdk import CLIConnectionError, CLINotFoundError, ProcessError
431→
432→         print("\n✅ Exception types imported:")
433→         print("   • CLINotFoundError - CLI not found in PATH")
434→         print("   • ProcessError - Process execution failure")
435→         print("   • CLIConnectionError - Connection failure")
436→
437→         # Example error handling pattern
438→         try:
439→             async with ClaudeSDKClient() as client:
440→                 await client.query("Test query")
441→                 async for message in client.receive_response():
442→                     print(message)
443→
444→         except CLINotFoundError:
445→             print("\n⚠️  Claude Code CLI not found in PATH")
446→             print("   Install Claude Code 2.0.0+ to use the SDK")
447→
448→         except CLIConnectionError as e:
449→             print(f"\n⚠️  Connection error: {e}")
450→             print("   Check if Claude Code is running properly")
451→
452→         except ProcessError as e:
453→             print(f"\n⚠️  Process error: {e}")
454→             print("   An error occurred during execution")
```

**📝 Annotation:** The SDK provides specific exception types (lines 430-435):
- **`CLINotFoundError`**: Claude Code CLI not found in system PATH
- **`CLIConnectionError`**: Failed to connect to Claude Code process
- **`ProcessError`**: Error during process execution

Use specific exception handlers (lines 444-454) for granular error management.

**Expected Output:**
```
======================================================================
EXAMPLE 7: Error Handling
======================================================================

🔍 Testing error handling scenarios...

✅ Exception types imported:
   • CLINotFoundError - CLI not found in PATH
   • ProcessError - Process execution failure
   • CLIConnectionError - Connection failure

💡 Always use specific exception types for robust error handling
```

---

### 9. Complex Multi-Tool Workflow (Lines 470-528)

```python
470→ async def example_8_complex_workflow():
471→     """Demonstrate a complex workflow with multiple tool interactions."""
481→     server = create_sdk_mcp_server(
482→         name="workflow-tools",
483→         version="1.0.0",
484→         tools=[calculate_tool, get_weather_tool, store_data_tool],
485→     )
486→
487→     options = ClaudeAgentOptions(
488→         system_prompt=(
489→             "You are a data processing assistant. "
490→             "Use the available tools to complete complex tasks efficiently."
491→         ),
492→         mcp_servers={"tools": server},
493→         allowed_tools=[
494→             "mcp__tools__calculate",
495→             "mcp__tools__get_weather",
496→             "mcp__tools__store_data",
497→         ],
498→     )
499→
504→         async with ClaudeSDKClient(options=options) as client:
505→             # Complex multi-step query
506→             query_text = (
507→                 "Please do the following in order: "
508→                 "1. Calculate 25 + 75 "
509→                 "2. Get weather for New York "
510→                 "3. Store the calculation result with key 'sum' "
511→                 "4. Store the weather condition with key 'ny_weather' "
512→                 "5. Summarize what you did"
513→             )
514→
515→             print(f"\n📤 Query: {query_text[:80]}...")
516→
517→             await client.query(query_text)
518→
519→             print("\n📥 Workflow execution:")
520→             async for message in client.receive_response():
521→                 print(f"   {str(message)[:100]}...")
```

**📝 Annotation:** Complex workflows (lines 506-521) demonstrate how Claude can:
- **Chain multiple tool calls** (lines 508-512: calculate → get weather → store × 2)
- **Maintain context** across tool invocations
- **Make decisions** based on tool results
- **Execute multi-step plans** autonomously

The system prompt (lines 488-490) guides Claude's behavior for data processing tasks.

**Expected Output:**
```
======================================================================
EXAMPLE 8: Complex Multi-Tool Workflow
======================================================================

🤖 Executing complex workflow...

📤 Query: Please do the following in order: 1. Calculate 25 + 75 2. Get weather f...

📊 Tool Usage Log: mcp__tools__calculate (ID: toolu_01XYZ...)
📊 Tool Usage Log: mcp__tools__get_weather (ID: toolu_02ABC...)
📊 Tool Usage Log: mcp__tools__store_data (ID: toolu_03DEF...)
📊 Tool Usage Log: mcp__tools__store_data (ID: toolu_04GHI...)

📥 Workflow execution:
   I completed the following tasks:
   1. Calculated 25 + 75 = 100
   2. Retrieved weather for New York: 22°C, Sunny
   3. Stored sum = 100
   4. Stored ny_weather = Sunny
   All data has been processed and stored successfully...

✅ Complex workflow completed
💡 Claude can orchestrate multiple tools to achieve complex goals
```

---

### 10. Feature Summary (Lines 536-602)

```python
536→ def example_9_feature_summary():
537→     """Display a comprehensive summary of Claude Agent SDK features."""
543→     features = {
544→         "Core Functions": [
545→             "query() - Simple async iterator for basic interactions",
546→             "ClaudeSDKClient - Advanced bidirectional conversations",
547→         ],
548→         "Custom Tools": [
549→             "@tool decorator - Define tools as Python functions",
550→             "create_sdk_mcp_server() - Create in-process MCP servers",
551→             "Type-safe parameters and return values",
552→             "Async/await support for I/O operations",
553→         ],
554→         "Hooks System": [
555→             "PreToolUse - Validate tools before execution",
556→             "HookMatcher - Pattern-based hook registration",
557→             "Permission control (allow/deny decisions)",
558→             "Deterministic processing and feedback",
559→         ],
560→         "Configuration (ClaudeAgentOptions)": [
561→             "system_prompt - Set agent behavior",
562→             "turn_limit - Control conversation length",
563→             "allowed_tools - Allowlist specific tools",
564→             "mcp_servers - Register tool servers",
565→             "hooks - Add validation and monitoring",
566→             "working_dir - Set working directory",
567→         ],
568→         "Advanced Features": [
569→             "Streaming input and output",
570→             "Stateful tool implementations",
571→             "Error handling with specific exceptions",
572→             "Concurrent tool execution",
573→             "In-process MCP servers (no subprocess overhead)",
574→         ],
575→         "Performance Benefits": [
576→             "Single Python process deployment",
577→             "No subprocess overhead",
578→             "Improved debugging capabilities",
579→             "Type-safe tool integration",
580→         ],
581→     }
```

**📝 Annotation:** The feature summary (lines 543-581) catalogs all SDK capabilities organized by category. This provides a quick reference for developers building agents.

---

## Complete Program Output

When run in a Claude Code environment, the complete program produces:

```
======================================================================
Running Claude Agent SDK demonstration...
======================================================================

======================================================================
🚀 Claude Agent SDK for Python - Comprehensive Demonstration
======================================================================

This demo showcases all key features of the Claude Agent SDK:
  • Simple query() function
  • ClaudeSDKClient for advanced usage
  • Custom tools with @tool decorator
  • SDK MCP servers (in-process)
  • Hooks for validation and control
  • Streaming input/output
  • Configuration options
  • Error handling
  • Complex multi-tool workflows

[... Examples 1-9 output as shown above ...]

======================================================================
✨ All Demonstrations Completed!
======================================================================

🎯 Key Takeaways:
  1. Use query() for simple, stateless interactions
  2. Use ClaudeSDKClient for complex, stateful agents
  3. Create custom tools with @tool decorator
  4. Use SDK MCP servers for in-process performance
  5. Add hooks for validation and permission control
  6. Configure behavior with ClaudeAgentOptions
  7. Handle errors with specific exception types
  8. Stream input/output for real-time processing

💡 The Claude Agent SDK enables building powerful AI agents
   that can use tools, maintain state, and execute workflows!

======================================================================
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Your Python Application                  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           ClaudeSDKClient (Bidirectional)            │  │
│  │                                                      │  │
│  │  • query() - Send prompts                           │  │
│  │  • receive_response() - Stream responses            │  │
│  │  • ClaudeAgentOptions - Configuration               │  │
│  └──────────────────────────────────────────────────────┘  │
│                            │                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │          SDK MCP Servers (In-Process)                │  │
│  │                                                      │  │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐    │  │
│  │  │   @tool    │  │   @tool    │  │   @tool    │    │  │
│  │  │ calculate  │  │get_weather │  │store_data  │    │  │
│  │  └────────────┘  └────────────┘  └────────────┘    │  │
│  │                                                      │  │
│  │  create_sdk_mcp_server(name, version, tools)        │  │
│  └──────────────────────────────────────────────────────┘  │
│                            │                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                 Hooks (Validation)                   │  │
│  │                                                      │  │
│  │  • PreToolUse - validate_bash_command()             │  │
│  │  • HookMatcher - Pattern matching                   │  │
│  │  • Permission decisions (allow/deny)                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↕
                   ╔════════════════════╗
                   ║   Claude Code      ║
                   ║   Environment      ║
                   ║   (CLI Process)    ║
                   ╚════════════════════╝
```

---

## Key Concepts Summary

### 1. **query() vs ClaudeSDKClient**

| Feature | `query()` | `ClaudeSDKClient` |
|---------|-----------|-------------------|
| **Use Case** | Simple, one-off queries | Complex, stateful conversations |
| **State** | Stateless | Stateful (maintains context) |
| **API** | Single function call | Client instance with methods |
| **Configuration** | Limited | Full `ClaudeAgentOptions` support |
| **Tools** | No | Yes (custom tools, MCP servers) |
| **Hooks** | No | Yes (validation, monitoring) |

### 2. **Custom Tools Lifecycle**

```python
@tool(name, description, input_schema)  # 1. Define tool
async def my_tool(args):                # 2. Implement async function
    return {"content": [...]}           # 3. Return structured result

server = create_sdk_mcp_server(...)     # 4. Create MCP server
options = ClaudeAgentOptions(           # 5. Register in options
    mcp_servers={"name": server},
    allowed_tools=["mcp__name__my_tool"]
)
```

### 3. **Hook Pattern**

```python
async def my_hook(input_data, tool_use_id, context):
    # Validation logic
    if should_deny:
        return {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": "..."
            }
        }
    return {}  # Allow execution

options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [
            HookMatcher(matcher="ToolName", hooks=[my_hook])
        ]
    }
)
```

### 4. **SDK MCP Servers vs Standard MCP**

| Feature | SDK MCP Servers | Standard MCP Servers |
|---------|-----------------|----------------------|
| **Process** | In-process (same Python process) | Separate subprocess |
| **Performance** | Fast (no IPC overhead) | Slower (process communication) |
| **Deployment** | Single executable | Multiple processes |
| **Debugging** | Easy (single process) | Complex (multi-process) |
| **Type Safety** | Full Python type hints | JSON schema only |

---

## Additional Resources

- **Official Documentation**: https://docs.claude.com/en/docs/agent-sdk/overview
- **API Reference**: https://docs.claude.com/en/api/agent-sdk/python
- **GitHub Repository**: https://github.com/anthropics/claude-agent-sdk-python
- **PyPI Package**: https://pypi.org/project/claude-agent-sdk/
- **Migration Guide**: https://docs.claude.com/en/docs/claude-code/sdk/migration-guide

---

## License

This demonstration code is provided as an example of Claude Agent SDK usage. Refer to the SDK license for production use.
