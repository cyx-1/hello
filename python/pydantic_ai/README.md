# Pydantic AI Agent Framework Demonstration

This example illustrates the **Pydantic AI** agent framework and its key differentiated features compared to other Python agent frameworks like LangChain, LlamaIndex, and AutoGen.

## Overview

**Pydantic AI** is a Python agent framework built by the Pydantic team (creators of the validation library used by OpenAI SDK, Anthropic SDK, LangChain, and many others). It brings type safety, simplicity, and production-readiness to GenAI application development.

## Key Differentiated Features

### 1. **Type Safety Throughout**
- Full type hints with IDE autocomplete and static type checking
- Catch errors at write-time instead of runtime
- Structured outputs validated with Pydantic models

### 2. **Model-Agnostic Design**
- Supports 20+ LLM providers out-of-the-box
- Easy to switch between providers with one line change
- No vendor lock-in

### 3. **Dependency Injection**
- Clean separation of agent logic and runtime context
- Type-safe access to user info, database connections, etc.
- No global state or prop drilling

### 4. **Developer Experience**
- FastAPI-like simplicity
- Tools are just Python functions with type hints
- No complex abstractions or "stringly-typed" APIs

### 5. **Production-Ready**
- Durable execution (survives failures/restarts)
- Native observability with Pydantic Logfire
- Built-in retry logic and async-first design

## Installation & Requirements

This example requires **Python 3.9+** and uses inline script metadata for dependency management.

```bash
# Run with uv (recommended)
uv run python/pydantic_ai/main_pydantic_agent.py

# Or install dependencies manually
pip install "pydantic-ai>=0.0.14" "pydantic>=2.0.0"
python python/pydantic_ai/main_pydantic_agent.py
```

## Code Structure

### Lines 30-42: Type-Safe Structured Outputs

```python
class WeatherReport(BaseModel):
    """Structured weather report with validation."""

    location: str = Field(description="City and country")
    temperature: float = Field(description="Temperature in Celsius", ge=-100, le=60)
    conditions: str = Field(description="Weather conditions")
    humidity: int = Field(description="Humidity percentage", ge=0, le=100)
    forecast: str = Field(description="Brief forecast")
```

**Feature**: Unlike other frameworks that return untyped strings or dicts, Pydantic AI enforces output schemas at the type level using Pydantic models.

### Lines 44-49: User Profile for Dependency Injection

```python
class UserProfile(BaseModel):
    """User profile for dependency injection example."""

    user_id: str
    preferred_units: str = "celsius"
    location: Optional[str] = None
```

**Feature**: Runtime context (user info, DB connections) can be injected into agents and tools with full type safety.

### Lines 58-77: Tool Functions with Auto-Validation

```python
def get_current_temperature(location: str) -> dict[str, float | str]:
    """
    Simulated tool to get current temperature.

    In production, this would call a real weather API.
    Pydantic AI automatically validates inputs and outputs.
    """
    return {
        "location": location,
        "temperature": 22.5,
        "conditions": "Partly cloudy",
    }
```

**Feature**: Tools are simple Python functions with type hints. Pydantic AI handles validation, serialization, and LLM communication automatically.

### Lines 135-164: Demo 1 - Structured Output

```python
# Line 135: Create agent with output_type for structured output
agent = Agent(
    "test",  # Using test model for demonstration
    output_type=WeatherReport,
    instructions="You are a weather assistant...",
)

# Line 150: Run synchronously - result is fully typed
result = agent.run_sync("What's the weather in London?")

# Line 157: Access fields with full IDE autocomplete support
weather = result.output
print(f"  Location: {weather.location}")
print(f"  Temperature: {weather.temperature}°C")
```

**Output:**
```
======================================================================
DEMO 1: Type-Safe Structured Outputs
======================================================================

[Line 128-138] Creating agent with structured output type
Result type: WeatherReport
Model: test (no API key required for demo)

[Line 145] Running agent with query: 'What's the weather in London?'

Agent response type: WeatherReport
Response is validated: True

[Line 153] Accessing structured fields:
  Location: a
  Temperature: -100.0°C
  Conditions: a
  Humidity: 0%
  Forecast: a
```

**Annotation**: The agent automatically returns a validated `WeatherReport` object. The test model returns minimal valid data ('a' is the shortest valid string, -100 is the minimum valid temperature), demonstrating that validation constraints are enforced.

### Lines 178-208: Demo 2 - Tool Registration

```python
# Line 178: Create agent and register tools with decorator
agent = Agent(
    "test",
    instructions="You are a helpful weather assistant...",
)

# Line 184: Register tools - Pydantic AI handles validation automatically
@agent.tool_plain
def get_temperature(location: str) -> str:
    """Get current temperature for a location."""
    data = get_current_temperature(location)
    return f"Temperature in {data['location']}: {data['temperature']}°C"

@agent.tool_plain
def get_weather_forecast(location: str, days: int = 3) -> str:
    """Get weather forecast."""
    return get_forecast(location, days)
```

**Output:**
```
======================================================================
DEMO 2: Tool Registration with Auto-Validation
======================================================================

[Line 183-195] Registered 2 tools with automatic validation:
  1. get_temperature(location: str)
  2. get_weather_forecast(location: str, days: int)

[Line 187] Tool called: get_temperature(location='a')

[Line 193] Tool called: get_weather_forecast(location='a', days=3)

[Line 202] Running agent with query:
  'What's the temperature in Paris and what's the 5-day forecast?'

Agent response: {"get_temperature":"Temperature in a: 22.5°C, Partly cloudy","get_weather_forecast":"Next 3 days in a: Mostly sunny with occasional clouds"}
```

**Annotation**: The `@agent.tool_plain` decorator registers simple functions as tools. The agent automatically validates inputs (line 187, 193) and calls the appropriate tools. The test model calls both tools and returns their results as a dict.

### Lines 222-256: Demo 3 - Dependency Injection

```python
# Line 222: Create agent with dependencies type parameter
agent = Agent[UserProfile](  # Type parameter enables type checking
    "test",
    instructions="You are a personalized assistant.",
    deps_type=UserProfile,
)

# Line 229: Register tool that accesses injected dependencies
@agent.tool
async def get_personalized_greeting(ctx: RunContext[UserProfile]) -> str:
    """Get personalized greeting using injected user context."""
    return await personalized_greeting(ctx)

# Line 244: Create user profile to inject
user = UserProfile(
    user_id="user_123",
    preferred_units="celsius",
    location="San Francisco",
)

# Line 253: Run with injected dependencies
result = await agent.run(
    "Greet me and tell me my preferences",
    deps=user,  # Dependencies injected here
)
```

**Output:**
```
======================================================================
DEMO 3: Dependency Injection
======================================================================

[Line 224-230] Created agent with dependency injection:
  Dependencies type: UserProfile
  Tools can access user context without explicit parameter passing

[Line 244] Created user profile: user_id=user_123

[Line 235] Tool accessing injected dependency: UserProfile

[Line 253] Running agent with injected user context
Agent response: {"get_personalized_greeting":"Hello user user_123! Current time: 11:38. Your preferred units: celsius"}
```

**Annotation**: The `RunContext[UserProfile]` parameter (line 231) provides type-safe access to the injected user profile. The framework automatically passes the user context to tools that need it, without explicit parameter passing in the agent's run call.

### Lines 270-299: Demo 4 - Model-Agnostic Design

```python
providers = [
    ("test", "Test model (for demo, no API key)"),
    # Uncomment to use real providers (requires API keys):
    # ("openai:gpt-4o-mini", "OpenAI GPT-4"),
    # ("anthropic:claude-sonnet-4-0", "Anthropic Claude"),
]

for model_name, description in providers:
    agent = Agent(
        model_name,
        instructions="You are a helpful assistant.",
    )

    # Same code works across all providers
    result = agent.run_sync("Hello, what model are you?")
    print(f"  Response: {result.output}")
```

**Output:**
```
======================================================================
DEMO 4: Model-Agnostic Design
======================================================================

[Feature] Pydantic AI supports 20+ model providers:
  - OpenAI: 'openai:gpt-4'
  - Anthropic: 'anthropic:claude-sonnet-4-0'
  - Google: 'google-gla:gemini-1.5-pro'
  - AWS Bedrock: 'bedrock:anthropic.claude-v2'
  - Azure: 'azure:gpt-4'
  - Groq: 'groq:mixtral-8x7b-32768'
  - Local models via Ollama: 'ollama:llama2'
  - Custom models: Implement ModelInterface

[Line 288] Creating agent with model: test
  Description: Test model (for demo, no API key)
  Response: success (no tool calls)
```

**Annotation**: The same agent code works with any supported provider - just change the model string. This demonstrates vendor independence and flexibility.

### Lines 307-360: Demo 5 - Key Differentiators

```
======================================================================
PYDANTIC AI KEY DIFFERENTIATORS
======================================================================

1. Type Safety
Full type hints throughout - catch errors at write-time, not runtime.
   IDE autocomplete works perfectly. Static type checkers (mypy, pyright) supported.

2. Pydantic Foundation
Built on Pydantic (used by OpenAI SDK, Anthropic SDK, LangChain, etc).
   Proven validation, serialization, and documentation generation.

3. Model-Agnostic
20+ providers supported out-of-box. Switch providers with one line.
   No vendor lock-in. Easy to add custom model implementations.

4. Dependency Injection
Clean separation of agent logic and runtime context (user info, DB, etc).
   No global state, no prop drilling. Type-safe context access.

5. Production-Ready
Durable execution (survives failures/restarts). Native observability.
   Built-in retry logic, streaming support, async-first design.

6. Developer Experience
FastAPI-like simplicity. Tools are just functions with type hints.
   No complex abstractions. Python-native patterns throughout.

7. Validation Everywhere
Tool inputs/outputs validated automatically. Structured outputs enforced.
   No 'stringly-typed' APIs. Invalid data caught immediately.
```

## Comparison with Other Frameworks

| Feature | Pydantic AI | LangChain | LlamaIndex | AutoGen |
|---------|-------------|-----------|------------|---------|
| **Type Safety** | ✅ Full (Pydantic models) | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial |
| **Structured Outputs** | ✅ Native with validation | ⚠️ Via output parsers | ⚠️ Limited | ❌ Manual |
| **Model-Agnostic** | ✅ 20+ providers | ✅ Many providers | ✅ Many providers | ⚠️ OpenAI-focused |
| **Dependency Injection** | ✅ Native | ❌ Manual | ❌ Manual | ❌ Manual |
| **Tool Definition** | ✅ Simple functions | ⚠️ Custom classes | ⚠️ Custom classes | ⚠️ Custom classes |
| **Production Features** | ✅ Durable execution | ⚠️ Via extensions | ⚠️ Limited | ❌ Research-focused |
| **Learning Curve** | ✅ Low (FastAPI-like) | ⚠️ Medium-High | ⚠️ Medium | ⚠️ Medium |
| **Validation** | ✅ Automatic (Pydantic) | ⚠️ Manual | ⚠️ Manual | ⚠️ Manual |

## Using with Real LLM Providers

To use with actual LLM providers instead of the test model:

```bash
# Set API keys
export OPENAI_API_KEY='your-openai-key'
export ANTHROPIC_API_KEY='your-anthropic-key'

# Run the demo (will use real models)
uv run python/pydantic_ai/main_pydantic_agent.py
```

Then modify the code to use real models:

```python
# Instead of "test", use:
agent = Agent(
    "openai:gpt-4o",  # OpenAI
    # "anthropic:claude-sonnet-4-0",  # Anthropic
    # "google-gla:gemini-1.5-pro",  # Google
    # "bedrock:anthropic.claude-v2",  # AWS Bedrock
    output_type=WeatherReport,
)
```

## Version Requirements

- **Python**: 3.9+
- **pydantic-ai**: 0.0.14+ (uses `output_type`, `instructions`, and `result.output` API)
- **pydantic**: 2.0.0+

**Note**: This code uses the latest Pydantic AI API (as of 2025). Older versions used `result_type` instead of `output_type` and `system_prompt` instead of `instructions`.

## Key Takeaways

1. **Type Safety**: Pydantic AI brings compile-time safety to agent development through full type hints and Pydantic validation
2. **Simplicity**: Tools are just Python functions - no complex abstractions or custom classes needed
3. **Flexibility**: Works with any LLM provider (20+ supported) - no vendor lock-in
4. **Production-Ready**: Built-in durable execution, observability, and retry logic
5. **Proven Foundation**: Built on Pydantic, the validation library used by major LLM SDKs

## References

- **Official Documentation**: https://ai.pydantic.dev/
- **GitHub Repository**: https://github.com/pydantic/pydantic-ai
- **Pydantic**: https://docs.pydantic.dev/
- **Pydantic Logfire** (Observability): https://pydantic.dev/logfire

## License

This demonstration code is provided as an educational example. Pydantic AI is MIT licensed.
