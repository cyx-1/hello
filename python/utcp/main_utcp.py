# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "utcp>=1.0.0",
#     "utcp-http>=1.0.0",
#     "fastapi>=0.100.0",
#     "uvicorn>=0.23.0",
#     "httpx>=0.24.0",
# ]
# ///
"""
UTCP (Universal Tool Calling Protocol) Demonstration

UTCP is an open standard that lets AI agents call any API directly,
without the wrapper servers required by MCP (Model Context Protocol).

Key differences from MCP:
- No proxy layer: Direct communication with native APIs
- Lower latency: Eliminates the "wrapper tax"
- Multi-protocol: Supports HTTP, gRPC, WebSocket, CLI natively
- JSON manifest: Simple tool discovery via standardized manifest
"""

import asyncio
import json
import multiprocessing
import time

import httpx
import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel
from utcp.data.utcp_manual import UtcpManual
from utcp.python_specific_tooling.tool_decorator import utcp_tool
from utcp_http.http_call_template import HttpCallTemplate

# Configuration
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8765
BASE_URL = f"http://{SERVER_HOST}:{SERVER_PORT}"


# =============================================================================
# PART 1: UTCP SERVER IMPLEMENTATION
# =============================================================================


class WeatherResponse(BaseModel):
    """Response model for weather data."""

    location: str
    temperature_celsius: float
    conditions: str
    humidity_percent: int
    wind_speed_kmh: float


class CalculationResponse(BaseModel):
    """Response model for calculator operations."""

    operation: str
    operands: list[float]
    result: float


class TextAnalysisResponse(BaseModel):
    """Response model for text analysis."""

    text: str
    word_count: int
    char_count: int
    sentence_count: int
    avg_word_length: float


# Create FastAPI app for UTCP server
app = FastAPI(
    title="UTCP Demo Server",
    description="Demonstrates UTCP tool exposure via HTTP protocol",
    version="1.0.0",
)


# UTCP Discovery Endpoint - This is the key differentiator from MCP
# The server exposes a manifest (manual) that describes all available tools
@app.get("/utcp", tags=["discovery"])
def utcp_discovery_endpoint():
    """
    UTCP discovery endpoint that returns the tool manifest.

    This is called once by clients to discover available tools.
    Unlike MCP, there's no persistent connection or proxy server.
    """
    print("[Server] UTCP manifest requested - returning tool definitions")
    manual = UtcpManual.create_from_decorators(manual_version="1.0.0")
    return manual


# Tool 1: Weather Service
@utcp_tool(
    tool_call_template=HttpCallTemplate(
        name="get_weather",
        url=f"{BASE_URL}/api/weather",
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

    This tool simulates fetching weather data from an external service.
    In production, this would call a real weather API.
    """
    print(f"[Server] Weather tool called for location: {location}")

    # Simulated weather data based on location
    weather_data = {
        "new york": (22.5, "Partly Cloudy", 65, 12.3),
        "london": (15.2, "Rainy", 85, 18.7),
        "tokyo": (28.1, "Sunny", 70, 8.5),
        "sydney": (19.8, "Clear", 55, 15.2),
    }

    temp, cond, hum, wind = weather_data.get(
        location.lower(), (20.0, "Unknown", 50, 10.0)
    )

    return WeatherResponse(
        location=location,
        temperature_celsius=temp,
        conditions=cond,
        humidity_percent=hum,
        wind_speed_kmh=wind,
    )


# Tool 2: Calculator Service
@utcp_tool(
    tool_call_template=HttpCallTemplate(
        name="calculate",
        url=f"{BASE_URL}/api/calculate",
        http_method="GET",
    ),
    tags=["math", "utility"],
)
@app.get("/api/calculate", response_model=CalculationResponse, tags=["tools"])
def calculate(
    operation: str = Query(
        ..., description="Math operation: add, subtract, multiply, divide"
    ),
    a: float = Query(..., description="First operand"),
    b: float = Query(..., description="Second operand"),
) -> CalculationResponse:
    """
    Perform basic mathematical calculations.

    Supports addition, subtraction, multiplication, and division.
    """
    print(f"[Server] Calculator tool called: {a} {operation} {b}")

    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else float("inf"),
    }

    op_func = operations.get(operation.lower())
    if not op_func:
        raise ValueError(f"Unknown operation: {operation}")

    result = op_func(a, b)

    return CalculationResponse(operation=operation, operands=[a, b], result=result)


# Tool 3: Text Analysis Service
@utcp_tool(
    tool_call_template=HttpCallTemplate(
        name="analyze_text",
        url=f"{BASE_URL}/api/analyze_text",
        http_method="POST",
    ),
    tags=["nlp", "text-processing"],
)
@app.post("/api/analyze_text", response_model=TextAnalysisResponse, tags=["tools"])
def analyze_text(text: str) -> TextAnalysisResponse:
    """
    Analyze text and return statistics.

    Computes word count, character count, sentence count, and average word length.
    """
    print(f"[Server] Text analysis tool called for: {text[:50]}...")

    words = text.split()
    sentences = text.count(".") + text.count("!") + text.count("?")
    if sentences == 0:
        sentences = 1

    avg_word_len = sum(len(word) for word in words) / len(words) if words else 0

    return TextAnalysisResponse(
        text=text,
        word_count=len(words),
        char_count=len(text),
        sentence_count=sentences,
        avg_word_length=round(avg_word_len, 2),
    )


def run_server():
    """Run the UTCP server in a separate process."""
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT, log_level="warning")


# =============================================================================
# PART 2: UTCP CLIENT IMPLEMENTATION
# =============================================================================


async def demonstrate_utcp_client():
    """
    Demonstrate how a UTCP client discovers and calls tools.

    Key UTCP Concepts:
    1. Tool Discovery: Client fetches JSON manifest from /utcp endpoint
    2. Direct Calls: Tools are called directly via native HTTP endpoints
    3. No Proxy: Unlike MCP, there's no intermediate server layer
    """
    print("\n" + "=" * 70)
    print("UTCP CLIENT DEMONSTRATION")
    print("=" * 70)

    async with httpx.AsyncClient(timeout=10.0) as client:
        # Step 1: Discover available tools via UTCP manifest
        print("\n[Step 1] Discovering tools via UTCP manifest...")
        print(f"         Fetching: {BASE_URL}/utcp")

        discovery_response = await client.get(f"{BASE_URL}/utcp")
        manifest = discovery_response.json()

        print("\n[UTCP Manifest Structure]")
        print(json.dumps(manifest, indent=2, default=str)[:1500])
        if len(json.dumps(manifest)) > 1500:
            print("... (truncated)")

        # Extract tool information from manifest
        tools = manifest.get("tools", [])
        print(f"\n[Step 2] Found {len(tools)} tools in manifest:")
        for i, tool in enumerate(tools, 1):
            tool_name = tool.get("name", "unknown")
            tool_desc = tool.get("description", "No description")[:60]
            print(f"         {i}. {tool_name}: {tool_desc}...")

        # Step 3: Call tools directly (no proxy!)
        print("\n" + "-" * 70)
        print("[Step 3] Calling tools DIRECTLY via native HTTP endpoints")
        print("         (This is the key UTCP advantage - no wrapper server!)")
        print("-" * 70)

        # Call Weather Tool
        print("\n[Tool Call 1: Weather Service]")
        weather_response = await client.get(
            f"{BASE_URL}/api/weather", params={"location": "Tokyo"}
        )
        weather_data = weather_response.json()
        print("Request:  GET /api/weather?location=Tokyo")
        print(f"Response: {json.dumps(weather_data, indent=2)}")

        # Call Calculator Tool
        print("\n[Tool Call 2: Calculator Service]")
        calc_response = await client.get(
            f"{BASE_URL}/api/calculate",
            params={"operation": "multiply", "a": 15.5, "b": 3.2},
        )
        calc_data = calc_response.json()
        print("Request:  GET /api/calculate?operation=multiply&a=15.5&b=3.2")
        print(f"Response: {json.dumps(calc_data, indent=2)}")

        # Call Text Analysis Tool
        print("\n[Tool Call 3: Text Analysis Service]")
        sample_text = (
            "UTCP enables direct tool calling. No wrappers needed. Simple and fast!"
        )
        analysis_response = await client.post(
            f"{BASE_URL}/api/analyze_text", params={"text": sample_text}
        )
        analysis_data = analysis_response.json()
        print(f'Request:  POST /api/analyze_text (text="{sample_text}")')
        print(f"Response: {json.dumps(analysis_data, indent=2)}")

        # Step 4: Show UTCP vs MCP comparison
        print("\n" + "=" * 70)
        print("UTCP vs MCP ARCHITECTURE COMPARISON")
        print("=" * 70)

        comparison = """
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
"""
        print(comparison)

        # Step 5: Show how an AI agent would use UTCP
        print("=" * 70)
        print("EXAMPLE: HOW AN AI AGENT USES UTCP")
        print("=" * 70)

        agent_flow = """
1. Agent receives user request: "What's the weather in London?"

2. Agent discovers tools (one-time fetch):
   manifest = await fetch("http://service.com/utcp")
   # Returns JSON with all tool definitions

3. Agent selects appropriate tool from manifest:
   tool = find_tool(manifest, "get_weather")
   # Tool includes: name, description, parameters, endpoint

4. Agent calls tool DIRECTLY:
   result = await http_get("http://service.com/api/weather?location=London")
   # Direct HTTP call - no proxy, no wrapper!

5. Agent uses result in response:
   "The weather in London is 15.2°C and Rainy with 85% humidity."
"""
        print(agent_flow)

        # Demonstrate batch operations (another UTCP advantage)
        print("=" * 70)
        print("BATCH OPERATIONS DEMONSTRATION")
        print("=" * 70)
        print("\nUTCP allows parallel direct calls without proxy bottlenecks:\n")

        start_time = time.time()

        # Parallel tool calls
        tasks = [
            client.get(f"{BASE_URL}/api/weather", params={"location": "New York"}),
            client.get(f"{BASE_URL}/api/weather", params={"location": "London"}),
            client.get(
                f"{BASE_URL}/api/calculate",
                params={"operation": "add", "a": 100, "b": 200},
            ),
            client.get(
                f"{BASE_URL}/api/calculate",
                params={"operation": "divide", "a": 144, "b": 12},
            ),
        ]

        responses = await asyncio.gather(*tasks)
        elapsed = time.time() - start_time

        print(f"Executed 4 parallel tool calls in {elapsed:.3f} seconds:")
        for i, resp in enumerate(responses, 1):
            data = resp.json()
            if "temperature_celsius" in data:
                print(
                    f"  {i}. Weather: {data['location']} = {data['temperature_celsius']}°C"
                )
            else:
                print(
                    f"  {i}. Calculate: {data['operands']} {data['operation']} = {data['result']}"
                )

        print("\n" + "=" * 70)
        print("UTCP DEMONSTRATION COMPLETE")
        print("=" * 70)


# =============================================================================
# PART 3: MAIN EXECUTION
# =============================================================================


def main():
    """Main entry point for UTCP demonstration."""
    print("=" * 70)
    print("UTCP (Universal Tool Calling Protocol) - Python Demonstration")
    print("An alternative to MCP that eliminates the wrapper server overhead")
    print("=" * 70)

    # Start server in separate process
    print("\n[Starting UTCP Server...]")
    server_process = multiprocessing.Process(target=run_server)
    server_process.start()

    # Give server time to start
    time.sleep(2)

    try:
        # Run client demonstration
        asyncio.run(demonstrate_utcp_client())
    finally:
        # Cleanup
        print("\n[Shutting down UTCP Server...]")
        server_process.terminate()
        server_process.join(timeout=5)
        print("[Server stopped]")


if __name__ == "__main__":
    main()
