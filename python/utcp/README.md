# UTCP (Universal Tool Calling Protocol) - Python Demonstration

UTCP is an open standard that enables AI agents to call any API directly, without the wrapper servers required by MCP (Model Context Protocol). This demonstration shows how UTCP eliminates the "wrapper tax" for lower latency and simpler architecture.

## Requirements

- **Python**: >= 3.10
- **Dependencies**: utcp, utcp-http, fastapi, uvicorn, httpx (automatically installed via inline script metadata)

## Running the Demo

```bash
uv run --script main_utcp.py
```

## Key Source Code Sections

### 1. UTCP Tool Server Setup (Lines 67-106)

The UTCP server exposes tools via a discovery endpoint that returns a JSON manifest:

```python
# Line 67-75: Create FastAPI app for UTCP server
app = FastAPI(
    title="UTCP Demo Server",
    description="Demonstrates UTCP tool exposure via HTTP protocol",
    version="1.0.0",
)

# Line 79-91: UTCP discovery endpoint - the core of UTCP
@app.get("/utcp", tags=["discovery"])
def utcp_discovery_endpoint():
    """
    UTCP discovery endpoint that returns the tool manifest.

    This is called once by clients to discover available tools.
    Unlike MCP, there's no persistent connection or proxy server.
    """
    print("[Server] UTCP manifest requested - returning tool definitions")
    manual = UtcpManual.create_from_decorators(manual_version="1.0.0")
    return manual  # Returns JSON manifest with all tool definitions
```

**Key Insight**: The `/utcp` endpoint serves a standardized JSON manifest describing all available tools. Clients fetch this once, then call tools directly - no persistent proxy connection needed.

### 2. Exposing Tools with @utcp_tool Decorator (Lines 94-136)

Tools are exposed using the `@utcp_tool` decorator with `HttpCallTemplate`:

```python
# Line 94-136: Weather service tool definition
@utcp_tool(
    tool_call_template=HttpCallTemplate(
        name="get_weather",
        url=f"{BASE_URL}/api/weather",  # Direct HTTP endpoint
        http_method="GET",
    ),
    tags=["weather", "external-service"],
)
@app.get("/api/weather", response_model=WeatherResponse, tags=["tools"])
def get_weather(
    location: str = Query(..., description="City name to get weather for"),
) -> WeatherResponse:
    """
    Get current weather conditions for a specified location.
    """
    print(f"[Server] Weather tool called for location: {location}")

    # Simulated weather data
    weather_data = {
        "new york": (22.5, "Partly Cloudy", 65, 12.3),
        "london": (15.2, "Rainy", 85, 18.7),
        "tokyo": (28.1, "Sunny", 70, 8.5),
    }
    # ... returns WeatherResponse
```

**Key Insight**: The `@utcp_tool` decorator registers the tool with UTCP while the function remains a standard FastAPI endpoint. The `HttpCallTemplate` specifies how to call the tool directly.

### 3. Client Tool Discovery (Lines 234-260)

The client discovers tools by fetching the UTCP manifest:

```python
# Line 234-260: Client discovers available tools
async with httpx.AsyncClient(timeout=10.0) as client:
    # Step 1: Discover available tools via UTCP manifest
    print("\n[Step 1] Discovering tools via UTCP manifest...")
    print(f"         Fetching: {BASE_URL}/utcp")

    discovery_response = await client.get(f"{BASE_URL}/utcp")
    manifest = discovery_response.json()

    # Extract tool information
    tools = manifest.get("tools", [])
    print(f"\n[Step 2] Found {len(tools)} tools in manifest:")
    for i, tool in enumerate(tools, 1):
        tool_name = tool.get("name", "unknown")
        print(f"         {i}. {tool_name}")
```

**Key Insight**: One HTTP GET request retrieves all tool definitions. The manifest includes tool names, descriptions, input schemas, and call templates.

### 4. Direct Tool Calling (Lines 262-294)

Tools are called directly via their native HTTP endpoints:

```python
# Line 265-272: Direct HTTP call to weather tool
print("\n[Tool Call 1: Weather Service]")
weather_response = await client.get(
    f"{BASE_URL}/api/weather", params={"location": "Tokyo"}
)
weather_data = weather_response.json()
print("Request:  GET /api/weather?location=Tokyo")
print(f"Response: {json.dumps(weather_data, indent=2)}")

# Line 275-282: Direct HTTP call to calculator tool
calc_response = await client.get(
    f"{BASE_URL}/api/calculate",
    params={"operation": "multiply", "a": 15.5, "b": 3.2},
)
calc_data = calc_response.json()
print("Request:  GET /api/calculate?operation=multiply&a=15.5&b=3.2")
```

**Key Insight**: No proxy layer! The client calls the tool endpoints directly using standard HTTP. This is the "no wrapper tax" advantage of UTCP.

### 5. Parallel Batch Operations (Lines 359-385)

UTCP enables efficient parallel tool calls:

```python
# Line 359-373: Parallel direct calls
start_time = time.time()

tasks = [
    client.get(f"{BASE_URL}/api/weather", params={"location": "New York"}),
    client.get(f"{BASE_URL}/api/weather", params={"location": "London"}),
    client.get(f"{BASE_URL}/api/calculate", params={"operation": "add", "a": 100, "b": 200}),
    client.get(f"{BASE_URL}/api/calculate", params={"operation": "divide", "a": 144, "b": 12}),
]

responses = await asyncio.gather(*tasks)
elapsed = time.time() - start_time

print(f"Executed 4 parallel tool calls in {elapsed:.3f} seconds:")
```

**Key Insight**: Without a proxy bottleneck, parallel requests go directly to endpoints. This reduces latency significantly compared to sequential proxy calls in MCP.

## Program Output

```
Adding tool: get_weather with call template: get_weather
Adding tool: calculate with call template: calculate
Adding tool: analyze_text with call template: analyze_text
======================================================================
UTCP (Universal Tool Calling Protocol) - Python Demonstration
An alternative to MCP that eliminates the wrapper server overhead
======================================================================

[Starting UTCP Server...]

======================================================================
UTCP CLIENT DEMONSTRATION
======================================================================

[Step 1] Discovering tools via UTCP manifest...
         Fetching: http://127.0.0.1:8765/utcp
[Server] UTCP manifest requested - returning tool definitions
```

**Lines 79-91 in action**: The server receives a manifest request and returns JSON tool definitions.

```json
[UTCP Manifest Structure]
{
  "utcp_version": "1.0.4",
  "manual_version": "1.0.0",
  "tools": [
    {
      "name": "get_weather",
      "description": "Get current weather conditions...",
      "inputs": {
        "title": "get_weather Input",
        "type": "object",
        "properties": {
          "location": {
            "description": "Auto-generated description for location",
            "type": "string"
          }
        }
      }
    }
    // ... more tools
  ]
}
```

**Manifest Structure**: Each tool includes name, description, input schema (JSON Schema format), and metadata - everything needed to call the tool.

```
[Step 2] Found 3 tools in manifest:
         1. get_weather: Get current weather conditions for a specified location...
         2. calculate: Perform basic mathematical calculations...
         3. analyze_text: Analyze text and return statistics...

----------------------------------------------------------------------
[Step 3] Calling tools DIRECTLY via native HTTP endpoints
         (This is the key UTCP advantage - no wrapper server!)
----------------------------------------------------------------------

[Tool Call 1: Weather Service]
[Server] Weather tool called for location: Tokyo
Request:  GET /api/weather?location=Tokyo
Response: {
  "location": "Tokyo",
  "temperature_celsius": 28.1,
  "conditions": "Sunny",
  "humidity_percent": 70,
  "wind_speed_kmh": 8.5
}
```

**Lines 94-136 & 265-272 in action**: Direct HTTP call to the weather endpoint, bypassing any proxy layer.

```
[Tool Call 2: Calculator Service]
[Server] Calculator tool called: 15.5 multiply 3.2
Request:  GET /api/calculate?operation=multiply&a=15.5&b=3.2
Response: {
  "operation": "multiply",
  "operands": [15.5, 3.2],
  "result": 49.6
}

[Tool Call 3: Text Analysis Service]
[Server] Text analysis tool called for: UTCP enables direct tool calling...
Request:  POST /api/analyze_text
Response: {
  "text": "UTCP enables direct tool calling. No wrappers needed. Simple and fast!",
  "word_count": 11,
  "char_count": 70,
  "sentence_count": 3,
  "avg_word_length": 5.45
}
```

**Lines 140-196 in action**: Different HTTP methods (GET, POST) supported natively.

```
======================================================================
UTCP vs MCP ARCHITECTURE COMPARISON
======================================================================

┌─────────────────────────────────────────────────────────────────────┐
│                        MCP (Model Context Protocol)                │
├─────────────────────────────────────────────────────────────────────┤
│  AI Agent  →  MCP Client  →  MCP Server  →  Wrapper  →  Real API  │
│                                                                     │
│  Problems:                                                          │
│  • Extra latency from proxy layer                                   │
│  • Must maintain wrapper servers                                    │
│  • Persistent connections required                                  │
│  • Additional infrastructure overhead                               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                 UTCP (Universal Tool Calling Protocol)             │
├─────────────────────────────────────────────────────────────────────┤
│  AI Agent  →  UTCP Client  →  Real API (Direct!)                   │
│                                                                     │
│  Advantages:                                                        │
│  • Direct API calls - no wrapper tax                                │
│  • JSON manifest for tool discovery                                 │
│  • Multi-protocol support (HTTP, gRPC, WebSocket, CLI)             │
│  • Stateless discovery - fetch manifest once, call anywhere        │
└─────────────────────────────────────────────────────────────────────┘
```

**Core UTCP Philosophy**: Eliminate intermediaries and call APIs directly using their native protocols.

```
======================================================================
BATCH OPERATIONS DEMONSTRATION
======================================================================

UTCP allows parallel direct calls without proxy bottlenecks:

[Server] Weather tool called for location: New York
[Server] Weather tool called for location: London
[Server] Calculator tool called: 100.0 add 200.0
[Server] Calculator tool called: 144.0 divide 12.0
Executed 4 parallel tool calls in 0.011 seconds:
  1. Weather: New York = 22.5°C
  2. Weather: London = 15.2°C
  3. Calculate: [100.0, 200.0] add = 300.0
  4. Calculate: [144.0, 12.0] divide = 12.0

======================================================================
UTCP DEMONSTRATION COMPLETE
======================================================================

[Shutting down UTCP Server...]
[Server stopped]
```

**Lines 359-385 in action**: Four parallel HTTP requests executed in ~11ms with no proxy overhead.

## UTCP Key Concepts

| Concept | Description | Source Code Reference |
|---------|-------------|----------------------|
| **UTCP Manual** | JSON manifest describing all available tools | Line 88: `UtcpManual.create_from_decorators()` |
| **Tool Call Template** | Defines how to invoke a tool (HTTP, CLI, etc.) | Lines 96-100: `HttpCallTemplate()` |
| **Discovery Endpoint** | Single endpoint returning the complete manifest | Line 79: `@app.get("/utcp")` |
| **Direct Calling** | Tools called via native protocols, no proxy | Lines 267-269: `client.get(f"{BASE_URL}/api/weather")` |
| **@utcp_tool Decorator** | Registers function as UTCP tool | Lines 94-104: `@utcp_tool(tool_call_template=...)` |

## When to Use UTCP vs MCP

| Use Case | UTCP | MCP |
|----------|------|-----|
| Low-latency requirements | ✅ Direct calls | ❌ Proxy overhead |
| Multi-protocol APIs | ✅ Native support | ⚠️ Wrapper needed |
| Stateless architecture | ✅ Fetch manifest once | ❌ Persistent connection |
| Simple deployment | ✅ Just expose /utcp | ❌ Maintain MCP server |
| Existing MCP tools | ✅ MCP plugin available | ✅ Native |
| Complex orchestration | ⚠️ Client responsibility | ✅ Server handles |

## Resources

- **Official Documentation**: https://www.utcp.io/
- **Python Package**: https://pypi.org/project/utcp/
- **GitHub Repository**: https://github.com/universal-tool-calling-protocol/python-utcp
- **Protocol Specification**: https://www.utcp.io/about/RFC

## Version Information

- **UTCP Protocol Version**: 1.0.4
- **Python Package**: utcp >= 1.0.0, utcp-http >= 1.0.0
- **Python Requirement**: >= 3.10
