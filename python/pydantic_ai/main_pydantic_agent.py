#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pydantic-ai>=0.0.14",
#     "pydantic>=2.0.0",
# ]
# ///

"""
Pydantic AI Agent Framework Demonstration

This script illustrates the key differentiated features of Pydantic AI:
1. Type-safe structured outputs with Pydantic models
2. Tool registration with automatic validation
3. Dependency injection for runtime context
4. Model-agnostic design (works with test/mock models)
5. Async support with streaming

Key differentiators vs other frameworks:
- Full type safety (IDE autocomplete, static type checking)
- Built on proven Pydantic validation foundation
- No "stringly-typed" APIs - everything is validated
- Simple, Pythonic API design (FastAPI-like experience)
"""

import asyncio
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext


# ============================================================================
# Feature 1: Type-Safe Structured Outputs
# ============================================================================
# Unlike other frameworks that return raw strings or untyped dicts,
# Pydantic AI enforces output schemas at the type level


class WeatherReport(BaseModel):
    """Structured weather report with validation."""

    location: str = Field(description="City and country")
    temperature: float = Field(description="Temperature in Celsius", ge=-100, le=60)
    conditions: str = Field(description="Weather conditions")
    humidity: int = Field(description="Humidity percentage", ge=0, le=100)
    forecast: str = Field(description="Brief forecast")


class UserProfile(BaseModel):
    """User profile for dependency injection example."""

    user_id: str
    preferred_units: str = "celsius"
    location: Optional[str] = None


# ============================================================================
# Feature 2: Tool Registration with Automatic Validation
# ============================================================================
# Tools are just Python functions with type hints - Pydantic AI handles
# the validation, serialization, and LLM communication automatically


def get_current_temperature(location: str) -> dict[str, float | str]:
    """
    Simulated tool to get current temperature.

    In production, this would call a real weather API.
    Pydantic AI automatically validates inputs and outputs.
    """
    # Line 66: Simulated data - in production, call actual API
    return {
        "location": location,
        "temperature": 22.5,
        "conditions": "Partly cloudy",
    }


def get_forecast(location: str, days: int = 3) -> str:
    """
    Get weather forecast for specified days.

    Args:
        location: City name
        days: Number of days to forecast (1-7)

    Returns:
        Forecast description
    """
    # Line 85: Parameter validation happens automatically via type hints
    if days > 7:
        return "Forecast only available for up to 7 days"
    return f"Next {days} days in {location}: Mostly sunny with occasional clouds"


# ============================================================================
# Feature 3: Dependency Injection
# ============================================================================
# Pass runtime context (user info, DB connections, etc.) to agents and tools
# without cluttering function signatures or using global state


async def personalized_greeting(ctx: RunContext[UserProfile]) -> str:
    """
    Tool that accesses user context via dependency injection.

    The RunContext provides type-safe access to dependencies without
    passing them explicitly through every function call.
    """
    # Line 106: Access injected user profile with full type safety
    user = ctx.deps
    current_time = datetime.now().strftime("%H:%M")

    return (
        f"Hello user {user.user_id}! "
        f"Current time: {current_time}. "
        f"Your preferred units: {user.preferred_units}"
    )


# ============================================================================
# Example 1: Basic Agent with Structured Output
# ============================================================================


def demo_structured_output():
    """Demonstrate type-safe structured outputs."""
    print("\n" + "=" * 70)
    print("DEMO 1: Type-Safe Structured Outputs")
    print("=" * 70)

    # Line 128: Create agent with output_type for structured output
    # This ensures the LLM response conforms to WeatherReport schema
    agent = Agent(
        "test",  # Using test model for demonstration (no API key needed)
        output_type=WeatherReport,
        instructions=(
            "You are a weather assistant. Provide weather information "
            "in the structured format requested."
        ),
    )

    print("\n[Line 128-138] Creating agent with structured output type")
    print(f"Result type: {WeatherReport.__name__}")
    print("Model: test (no API key required for demo)\n")

    # Line 145: Run synchronously - result is fully typed
    result = agent.run_sync("What's the weather in London?")

    print("[Line 145] Running agent with query: 'What's the weather in London?'")
    print(f"\nAgent response type: {type(result.output).__name__}")
    print(f"Response is validated: {isinstance(result.output, WeatherReport)}")

    # Line 153: Access fields with full IDE autocomplete support
    weather = result.output
    print("\n[Line 153] Accessing structured fields:")
    print(f"  Location: {weather.location}")
    print(f"  Temperature: {weather.temperature}°C")
    print(f"  Conditions: {weather.conditions}")
    print(f"  Humidity: {weather.humidity}%")
    print(f"  Forecast: {weather.forecast}")


# ============================================================================
# Example 2: Agent with Tools (Function Calling)
# ============================================================================


def demo_agent_with_tools():
    """Demonstrate tool registration and automatic validation."""
    print("\n" + "=" * 70)
    print("DEMO 2: Tool Registration with Auto-Validation")
    print("=" * 70)

    # Line 176: Create agent and register tools with decorator
    agent = Agent(
        "test",
        instructions="You are a helpful weather assistant with access to real-time data.",
    )

    # Line 183: Register tools - Pydantic AI handles validation automatically
    @agent.tool_plain
    def get_temperature(location: str) -> str:
        """Get current temperature for a location."""
        print(f"\n[Line 187] Tool called: get_temperature(location='{location}')")
        data = get_current_temperature(location)
        return f"Temperature in {data['location']}: {data['temperature']}°C, {data['conditions']}"

    @agent.tool_plain
    def get_weather_forecast(location: str, days: int = 3) -> str:
        """Get weather forecast."""
        print(f"\n[Line 193] Tool called: get_weather_forecast(location='{location}', days={days})")
        return get_forecast(location, days)

    print("\n[Line 183-195] Registered 2 tools with automatic validation:")
    print("  1. get_temperature(location: str)")
    print("  2. get_weather_forecast(location: str, days: int)")

    # Line 202: Agent automatically decides when to use tools
    result = agent.run_sync(
        "What's the temperature in Paris and what's the 5-day forecast?"
    )

    print("\n[Line 202] Running agent with query:")
    print("  'What's the temperature in Paris and what's the 5-day forecast?'")
    print(f"\nAgent response: {result.output}")


# ============================================================================
# Example 3: Dependency Injection
# ============================================================================


async def demo_dependency_injection():
    """Demonstrate dependency injection for runtime context."""
    print("\n" + "=" * 70)
    print("DEMO 3: Dependency Injection")
    print("=" * 70)

    # Line 224: Create agent with dependencies type parameter
    agent = Agent[UserProfile](  # Type parameter enables type checking
        "test",
        instructions="You are a personalized assistant.",
        deps_type=UserProfile,
    )

    # Line 231: Register tool that accesses injected dependencies
    @agent.tool
    async def get_personalized_greeting(ctx: RunContext[UserProfile]) -> str:
        """Get personalized greeting using injected user context."""
        print("\n[Line 235] Tool accessing injected dependency: UserProfile")
        return await personalized_greeting(ctx)

    print("\n[Line 224-230] Created agent with dependency injection:")
    print(f"  Dependencies type: {UserProfile.__name__}")
    print("  Tools can access user context without explicit parameter passing")

    # Line 244: Create user profile to inject
    user = UserProfile(
        user_id="user_123",
        preferred_units="celsius",
        location="San Francisco",
    )

    print(f"\n[Line 244] Created user profile: user_id={user.user_id}")

    # Line 253: Run with injected dependencies
    result = await agent.run(
        "Greet me and tell me my preferences",
        deps=user,  # Dependencies injected here
    )

    print("\n[Line 253] Running agent with injected user context")
    print(f"Agent response: {result.output}")


# ============================================================================
# Example 4: Model-Agnostic Design
# ============================================================================


def demo_model_agnostic():
    """Demonstrate support for different model providers."""
    print("\n" + "=" * 70)
    print("DEMO 4: Model-Agnostic Design")
    print("=" * 70)

    print("\n[Feature] Pydantic AI supports 20+ model providers:")
    print("  - OpenAI: 'openai:gpt-4'")
    print("  - Anthropic: 'anthropic:claude-sonnet-4-0'")
    print("  - Google: 'google-gla:gemini-1.5-pro'")
    print("  - AWS Bedrock: 'bedrock:anthropic.claude-v2'")
    print("  - Azure: 'azure:gpt-4'")
    print("  - Groq: 'groq:mixtral-8x7b-32768'")
    print("  - Local models via Ollama: 'ollama:llama2'")
    print("  - Custom models: Implement ModelInterface")

    # Line 288: Same code works with any provider - just change model string
    providers = [
        ("test", "Test model (for demo, no API key)"),
        # Uncomment to use real providers (requires API keys):
        # ("openai:gpt-4o-mini", "OpenAI GPT-4"),
        # ("anthropic:claude-sonnet-4-0", "Anthropic Claude"),
    ]

    for model_name, description in providers:
        print(f"\n[Line 288] Creating agent with model: {model_name}")
        print(f"  Description: {description}")

        agent = Agent(
            model_name,
            instructions="You are a helpful assistant.",
        )

        # Same code works across all providers
        result = agent.run_sync("Hello, what model are you?")
        print(f"  Response: {result.output}")


# ============================================================================
# Example 5: Key Differentiators Summary
# ============================================================================


def demo_differentiators():
    """Highlight what makes Pydantic AI unique."""
    print("\n" + "=" * 70)
    print("PYDANTIC AI KEY DIFFERENTIATORS")
    print("=" * 70)

    differentiators = [
        (
            "1. Type Safety",
            "Full type hints throughout - catch errors at write-time, not runtime.\n"
            "   IDE autocomplete works perfectly. Static type checkers (mypy, pyright) supported.",
        ),
        (
            "2. Pydantic Foundation",
            "Built on Pydantic (used by OpenAI SDK, Anthropic SDK, LangChain, etc).\n"
            "   Proven validation, serialization, and documentation generation.",
        ),
        (
            "3. Model-Agnostic",
            "20+ providers supported out-of-box. Switch providers with one line.\n"
            "   No vendor lock-in. Easy to add custom model implementations.",
        ),
        (
            "4. Dependency Injection",
            "Clean separation of agent logic and runtime context (user info, DB, etc).\n"
            "   No global state, no prop drilling. Type-safe context access.",
        ),
        (
            "5. Production-Ready",
            "Durable execution (survives failures/restarts). Native observability.\n"
            "   Built-in retry logic, streaming support, async-first design.",
        ),
        (
            "6. Developer Experience",
            "FastAPI-like simplicity. Tools are just functions with type hints.\n"
            "   No complex abstractions. Python-native patterns throughout.",
        ),
        (
            "7. Validation Everywhere",
            "Tool inputs/outputs validated automatically. Structured outputs enforced.\n"
            "   No 'stringly-typed' APIs. Invalid data caught immediately.",
        ),
    ]

    for title, description in differentiators:
        print(f"\n{title}")
        print(description)


# ============================================================================
# Main Execution
# ============================================================================


def main():
    """Run all demonstrations."""
    print("=" * 70)
    print("PYDANTIC AI AGENT FRAMEWORK DEMONSTRATION")
    print("=" * 70)
    print("\nThis demo showcases Pydantic AI's differentiated features:")
    print("- Type-safe structured outputs")
    print("- Automatic tool validation")
    print("- Dependency injection")
    print("- Model-agnostic design")
    print("- Production-ready patterns")

    # Run synchronous demos
    demo_structured_output()
    demo_agent_with_tools()
    demo_model_agnostic()
    demo_differentiators()

    # Run async demo
    print("\n" + "=" * 70)
    print("Running async demo...")
    print("=" * 70)
    asyncio.run(demo_dependency_injection())

    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. Pydantic AI brings type safety to agent development")
    print("2. Tools are simple Python functions - no complex abstractions")
    print("3. Works with any LLM provider (20+ supported)")
    print("4. Built on proven Pydantic validation (used by major libraries)")
    print("5. Production-ready with durable execution and observability")
    print("\nTo use with real models, set environment variables:")
    print("  export OPENAI_API_KEY='your-key'")
    print("  export ANTHROPIC_API_KEY='your-key'")
    print("Then change 'test' to 'openai:gpt-4o' or 'anthropic:claude-sonnet-4-0'")


if __name__ == "__main__":
    main()
