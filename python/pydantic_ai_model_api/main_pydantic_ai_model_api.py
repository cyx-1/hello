# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pydantic-ai>=0.2.0",
#   "openai>=1.0.0",
#   "anthropic>=0.40.0",
# ]
# ///
"""
Pydantic AI: Direct Model API Access

This demonstrates how Pydantic AI doesn't abstract away model-specific features
into a lowest-common-denominator API. Instead, it provides:

1. A common interface for basic operations (model-agnostic)
2. Direct access to provider-specific settings through typed classes
3. Full control over each provider's unique capabilities

Philosophy: "Why use the derivative when you can go straight to the source?"
"""

from __future__ import annotations

from pydantic_ai.settings import ModelSettings

# Import provider-specific settings - THIS IS THE KEY POINT
# Each provider has its own settings class with provider-specific parameters
from pydantic_ai.models.openai import OpenAIModelSettings
from pydantic_ai.models.anthropic import AnthropicModelSettings


def demo_1_common_settings():
    """
    Demo 1: Common ModelSettings - Works across all providers

    These generic settings apply to multiple models but represent
    the "lowest common denominator" approach.
    """
    print("=" * 70)
    print("DEMO 1: Common ModelSettings (Generic/Abstracted)")
    print("=" * 70)

    # Generic settings that work across providers
    generic_settings = ModelSettings(
        max_tokens=150,
        temperature=0.7,
        top_p=0.9,
    )

    print("Generic ModelSettings (works with any provider):")
    print(f"  max_tokens: {generic_settings.get('max_tokens')}")
    print(f"  temperature: {generic_settings.get('temperature')}")
    print(f"  top_p: {generic_settings.get('top_p')}")
    print()
    print("Limitation: Only common parameters, no provider-specific features")
    print()


def demo_2_openai_specific_settings():
    """
    Demo 2: OpenAI-Specific Settings - Direct API Access

    OpenAIModelSettings provides access to OpenAI-specific features
    that don't exist in other providers.
    """
    print("=" * 70)
    print("DEMO 2: OpenAI-Specific Settings (Direct API Access)")
    print("=" * 70)

    # OpenAI-specific settings - direct access to OpenAI API parameters
    openai_settings = OpenAIModelSettings(
        # Common parameters
        max_tokens=200,
        temperature=0.5,
        # OpenAI-SPECIFIC parameters - not available in other providers
        openai_reasoning_effort="high",      # For o1/o3 reasoning models
        openai_logprobs=True,                # Get log probabilities
        openai_top_logprobs=3,               # Top 3 token probabilities
        openai_user="user-123",              # Track end-user for abuse detection
        openai_service_tier="default",       # Service tier: auto, default, flex, priority
    )

    print("OpenAI-Specific Settings (Direct API Access):")
    print("  Common parameters:")
    print(f"    max_tokens: {openai_settings.get('max_tokens')}")
    print(f"    temperature: {openai_settings.get('temperature')}")
    print()
    print("  OpenAI-SPECIFIC parameters (not abstracted away):")
    print(f"    openai_reasoning_effort: {openai_settings.get('openai_reasoning_effort')}")
    print(f"    openai_logprobs: {openai_settings.get('openai_logprobs')}")
    print(f"    openai_top_logprobs: {openai_settings.get('openai_top_logprobs')}")
    print(f"    openai_user: {openai_settings.get('openai_user')}")
    print(f"    openai_service_tier: {openai_settings.get('openai_service_tier')}")
    print()
    print("Key Insight: These map DIRECTLY to OpenAI API parameters!")
    print("No abstraction layer - you're talking directly to OpenAI's API.")
    print()


def demo_3_anthropic_specific_settings():
    """
    Demo 3: Anthropic-Specific Settings - Direct API Access

    AnthropicModelSettings provides access to Anthropic-specific features
    like extended thinking and prompt caching.
    """
    print("=" * 70)
    print("DEMO 3: Anthropic-Specific Settings (Direct API Access)")
    print("=" * 70)

    # Anthropic-specific settings - direct access to Anthropic API parameters
    anthropic_settings = AnthropicModelSettings(
        # Common parameters
        max_tokens=50000,
        temperature=0.0,
        # Anthropic-SPECIFIC parameters
        anthropic_thinking={                  # Extended thinking (Claude specific!)
            "type": "enabled",
            "budget_tokens": 10000,
        },
        anthropic_cache_instructions=True,    # Cache system prompts
        anthropic_cache_tool_definitions=True, # Cache tool definitions
    )

    print("Anthropic-Specific Settings (Direct API Access):")
    print("  Common parameters:")
    print(f"    max_tokens: {anthropic_settings.get('max_tokens')}")
    print(f"    temperature: {anthropic_settings.get('temperature')}")
    print()
    print("  Anthropic-SPECIFIC parameters (not abstracted away):")
    print(f"    anthropic_thinking: {anthropic_settings.get('anthropic_thinking')}")
    print(f"    anthropic_cache_instructions: {anthropic_settings.get('anthropic_cache_instructions')}")
    print(f"    anthropic_cache_tool_definitions: {anthropic_settings.get('anthropic_cache_tool_definitions')}")
    print()
    print("Key Insight: Extended thinking is Claude-ONLY feature!")
    print("You can't abstract this into a generic API without losing the feature.")
    print()


def demo_4_contrast_with_abstraction():
    """
    Demo 4: Contrast with a hypothetical "fully abstracted" approach

    Shows why NOT abstracting everything is actually better.
    """
    print("=" * 70)
    print("DEMO 4: Why Direct API Access > Full Abstraction")
    print("=" * 70)

    print("HYPOTHETICAL: If Pydantic AI used a 'lowest common denominator' API:")
    print()
    print("  # This WOULD NOT exist:")
    print("  settings = GenericSettings(")
    print("      max_tokens=100,")
    print("      temperature=0.5,")
    print("      # NO access to:")
    print("      # - OpenAI's reasoning_effort (o1/o3 models)")
    print("      # - OpenAI's logprobs")
    print("      # - Anthropic's extended thinking")
    print("      # - Anthropic's prompt caching")
    print("      # - Gemini's safety settings")
    print("      # - etc.")
    print("  )")
    print()

    print("REALITY: Pydantic AI gives you BOTH:")
    print()
    print("  1. Model-Agnostic Interface (swap models easily):")
    print("     agent = Agent('openai:gpt-4o')  # Easy to switch")
    print("     agent = Agent('anthropic:claude-3-5-sonnet')  # Just change string")
    print()

    print("  2. Provider-Specific Power (direct API access):")
    print("     # OpenAI's unique features")
    print("     openai_settings = OpenAIModelSettings(")
    print("         openai_reasoning_effort='high',")
    print("         openai_logprobs=True")
    print("     )")
    print()
    print("     # Anthropic's unique features")
    print("     anthropic_settings = AnthropicModelSettings(")
    print("         anthropic_thinking={'type': 'enabled', 'budget_tokens': 10000}")
    print("     )")
    print()

    print("The BEST of both worlds!")
    print()


def demo_5_agent_with_provider_settings():
    """
    Demo 5: Using provider-specific settings with an Agent

    Shows how to use these settings in practice.
    """
    print("=" * 70)
    print("DEMO 5: Agent Configuration with Provider-Specific Settings")
    print("=" * 70)

    # Example 1: OpenAI Agent with OpenAI-specific settings
    print("OpenAI Agent with direct API access:")
    print()
    print("  from pydantic_ai import Agent")
    print("  from pydantic_ai.models.openai import OpenAIModelSettings")
    print()
    print("  agent = Agent('openai:gpt-4o')")
    print()
    print("  # Run with OpenAI-specific features")
    print("  result = await agent.run(")
    print("      'Analyze this complex problem',")
    print("      model_settings=OpenAIModelSettings(")
    print("          openai_reasoning_effort='high',  # Reasoning model feature")
    print("          openai_logprobs=True,            # Get probabilities")
    print("          openai_service_tier='priority',  # Priority processing")
    print("      )")
    print("  )")
    print()

    # Example 2: Anthropic Agent with Anthropic-specific settings
    print("Anthropic Agent with direct API access:")
    print()
    print("  from pydantic_ai import Agent")
    print("  from pydantic_ai.models.anthropic import AnthropicModelSettings")
    print()
    print("  agent = Agent('anthropic:claude-3-5-sonnet-latest')")
    print()
    print("  # Run with Anthropic-specific features")
    print("  result = await agent.run(")
    print("      'Solve this step by step',")
    print("      model_settings=AnthropicModelSettings(")
    print("          anthropic_thinking={              # Extended thinking!")
    print("              'type': 'enabled',")
    print("              'budget_tokens': 16000,")
    print("          },")
    print("          anthropic_cache_instructions=True,  # Prompt caching")
    print("      )")
    print("  )")
    print()

    print("Notice: SAME Agent class, but provider-specific settings!")
    print("You're not limited by abstraction - you have FULL API control.")
    print()


def demo_6_settings_inheritance():
    """
    Demo 6: Type safety and settings inheritance

    Provider-specific settings inherit from common settings.
    """
    print("=" * 70)
    print("DEMO 6: Settings Inheritance and Type Safety")
    print("=" * 70)

    print("Settings Hierarchy (Pydantic-powered type safety):")
    print()
    print("  ModelSettings (Base)")
    print("      |")
    print("      |-- Common: max_tokens, temperature, top_p, seed, etc.")
    print("      |")
    print("      +-- OpenAIModelSettings (extends base)")
    print("      |       |-- openai_reasoning_effort")
    print("      |       |-- openai_logprobs")
    print("      |       |-- openai_top_logprobs")
    print("      |       |-- openai_user")
    print("      |       |-- openai_service_tier")
    print("      |       +-- openai_prediction")
    print("      |")
    print("      +-- AnthropicModelSettings (extends base)")
    print("      |       |-- anthropic_thinking")
    print("      |       |-- anthropic_cache_instructions")
    print("      |       +-- anthropic_cache_tool_definitions")
    print("      |")
    print("      +-- GeminiModelSettings (extends base)")
    print("              |-- gemini_safety_settings")
    print("              +-- gemini_generation_config")
    print()

    print("Benefits of this approach:")
    print("  1. Type-safe: IDE autocompletion for provider-specific options")
    print("  2. Validated: Pydantic validates all parameters")
    print("  3. Documented: Each setting is typed and documented")
    print("  4. No guessing: You know exactly what each provider supports")
    print()


def demo_7_real_world_example():
    """
    Demo 7: Real-world use case showing the value of direct API access
    """
    print("=" * 70)
    print("DEMO 7: Real-World Use Case")
    print("=" * 70)

    print("Scenario: Building a code review system")
    print()

    print("WITH Full Abstraction (limiting):")
    print("  settings = GenericSettings(max_tokens=1000, temperature=0)")
    print("  # Can't use Claude's extended thinking for deep analysis")
    print("  # Can't use OpenAI's logprobs to measure confidence")
    print("  # Stuck with generic features only")
    print()

    print("WITH Pydantic AI's Direct Access (empowering):")
    print()
    print("  # For CRITICAL code reviews - use Claude's extended thinking")
    print("  critical_review_settings = AnthropicModelSettings(")
    print("      anthropic_thinking={")
    print("          'type': 'enabled',")
    print("          'budget_tokens': 20000,  # Deep analysis")
    print("      },")
    print("      max_tokens=10000,")
    print("  )")
    print()
    print("  # For QUICK reviews - use OpenAI with confidence scoring")
    print("  quick_review_settings = OpenAIModelSettings(")
    print("      openai_logprobs=True,       # Confidence metrics")
    print("      openai_top_logprobs=5,      # Top 5 alternatives")
    print("      max_tokens=500,")
    print("  )")
    print()
    print("  # For COST-OPTIMIZED reviews - use OpenAI flex tier")
    print("  batch_review_settings = OpenAIModelSettings(")
    print("      openai_service_tier='flex',  # Lower cost, higher latency OK")
    print("      max_tokens=2000,")
    print("  )")
    print()

    print("Result: Use the RIGHT tool for the job, with FULL power!")
    print()


def main():
    """Main entry point demonstrating Pydantic AI's direct API access philosophy."""
    print("\n" + "=" * 70)
    print("  PYDANTIC AI: DIRECT MODEL API ACCESS")
    print("  'Why use the derivative when you can go straight to the source?'")
    print("=" * 70 + "\n")

    # Run all demonstrations
    demo_1_common_settings()
    demo_2_openai_specific_settings()
    demo_3_anthropic_specific_settings()
    demo_4_contrast_with_abstraction()
    demo_5_agent_with_provider_settings()
    demo_6_settings_inheritance()
    demo_7_real_world_example()

    # Summary
    print("=" * 70)
    print("SUMMARY: Pydantic AI's Approach to Model APIs")
    print("=" * 70)
    print()
    print("1. NOT a 'lowest common denominator' abstraction")
    print("   - Other libraries: Force you into a generic API")
    print("   - Pydantic AI: Gives you direct access to each provider's API")
    print()
    print("2. Provider-specific TypedDict settings classes")
    print("   - OpenAIModelSettings: reasoning_effort, logprobs, service_tier")
    print("   - AnthropicModelSettings: thinking, cache_instructions")
    print("   - Each provider's unique features are DIRECTLY accessible")
    print()
    print("3. Best of both worlds")
    print("   - Model-agnostic: Easy to swap between providers")
    print("   - Provider-specific: Full access to unique capabilities")
    print()
    print("4. Type-safe and validated (Pydantic-powered)")
    print("   - IDE autocompletion for all settings")
    print("   - Runtime validation of parameters")
    print("   - Clear documentation of what each provider supports")
    print()
    print("Philosophy: Don't hide the API - EMBRACE it with type safety!")
    print()


if __name__ == "__main__":
    main()
