#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "openai>=1.0.0",
# ]
# ///

"""
OpenRouter Python Demonstration

This script demonstrates how OpenRouter provides a unified API to connect
to various LLM providers including OpenAI, Anthropic, Meta, Google, and more.
"""

import os
from openai import OpenAI

# Line 19: Initialize OpenRouter client with API key
# OpenRouter uses OpenAI-compatible API, so we use the OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY", "demo-key-for-illustration"),
)

def demonstrate_model_selection():
    """Demonstrate connecting to different LLM providers through OpenRouter"""

    # Line 30: Define various models from different providers
    models = [
        {
            "name": "OpenAI GPT-4 Turbo",
            "id": "openai/gpt-4-turbo",
            "provider": "OpenAI"
        },
        {
            "name": "Anthropic Claude 3.5 Sonnet",
            "id": "anthropic/claude-3.5-sonnet",
            "provider": "Anthropic"
        },
        {
            "name": "Meta Llama 3.1 405B",
            "id": "meta-llama/llama-3.1-405b-instruct",
            "provider": "Meta"
        },
        {
            "name": "Google Gemini Pro 1.5",
            "id": "google/gemini-pro-1.5",
            "provider": "Google"
        },
        {
            "name": "Mistral Large",
            "id": "mistralai/mistral-large",
            "provider": "Mistral AI"
        }
    ]

    print("=" * 80)
    print("OpenRouter: Unified API for Multiple LLM Providers")
    print("=" * 80)
    print()

    # Line 65: Display available models
    print("Available Models Through OpenRouter:")
    print("-" * 80)
    for idx, model in enumerate(models, 1):
        print(f"{idx}. {model['name']}")
        print(f"   Provider: {model['provider']}")
        print(f"   Model ID: {model['id']}")
        print()

    # Line 75: Demonstrate the same API call structure for different models
    test_prompt = "Explain quantum computing in one sentence."

    print("=" * 80)
    print("Demonstrating Unified API: Same Code, Different Models")
    print("=" * 80)
    print(f"\nTest Prompt: '{test_prompt}'\n")

    # Line 83: Example API call structure (works for all models)
    print("Python Code Structure (works for ALL models above):")
    print("-" * 80)
    print("""
response = client.chat.completions.create(
    model="<any-model-id-from-above>",  # Line 88: Simply change model ID
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ],
    max_tokens=150
)
print(response.choices[0].message.content)
    """)

    # Line 97: Demonstrate model switching
    print("\n" + "=" * 80)
    print("Key Feature: Easy Model Switching")
    print("=" * 80)
    print("\nTo switch between providers, just change the model parameter:")
    print()

    for model in models[:3]:  # Show first 3 models
        print(f"# Using {model['provider']}: {model['name']}")
        print("response = client.chat.completions.create(")
        print(f"    model=\"{model['id']}\",  # Line 108: {model['provider']} model")
        print(f"    messages=[{{\"role\": \"user\", \"content\": \"{test_prompt}\"}}]")
        print(")")
        print()

    # Line 114: Show additional OpenRouter features
    print("=" * 80)
    print("OpenRouter Additional Features")
    print("=" * 80)
    print("""
1. Model Routing (Line 120):
   - Use 'auto' routing to automatically select the best model
   - Example: model="openrouter/auto"

2. Cost Tracking (Line 124):
   - OpenRouter provides cost information in response headers
   - Track spending across different providers

3. Fallback Models (Line 128):
   - Specify fallback models if primary model is unavailable
   - Example: models=["primary-model", "fallback-model"]

4. Provider Parameters (Line 132):
   - Pass provider-specific parameters through extra_body
   - Example: extra_body={"provider": {"order": ["OpenAI", "Anthropic"]}}

5. Unified Billing (Line 136):
   - Single API key for all providers
   - One bill instead of managing multiple provider accounts
    """)

def demonstrate_practical_example():
    """Show a practical example of using OpenRouter"""

    print("\n" + "=" * 80)
    print("Practical Example: Multi-Model Query")
    print("=" * 80)
    print()

    # Line 151: Practical function that can work with any model
    def query_model(model_id: str, prompt: str) -> str:
        """Generic function that works with any OpenRouter model"""
        try:
            # Line 155: Standard OpenAI-compatible API call
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.7
            )
            # Line 164: Extract response text
            return response.choices[0].message.content
        except Exception as e:
            # Line 167: Handle errors gracefully
            return f"Error: {str(e)}"

    print("Function Definition (Lines 151-168):")
    print("-" * 80)
    print("""
def query_model(model_id: str, prompt: str) -> str:
    response = client.chat.completions.create(
        model=model_id,  # Line 175: Works with ANY OpenRouter model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message.content
    """)

    print("\n" + "Usage Examples:")
    print("-" * 80)
    print("""
# Line 185: Query OpenAI's GPT-4
result1 = query_model("openai/gpt-4-turbo", "What is AI?")

# Line 188: Query Anthropic's Claude (same function!)
result2 = query_model("anthropic/claude-3.5-sonnet", "What is AI?")

# Line 191: Query Meta's Llama (same function!)
result3 = query_model("meta-llama/llama-3.1-405b-instruct", "What is AI?")

# Line 194: Compare responses from different models
for model, result in [("GPT-4", result1), ("Claude", result2), ("Llama", result3)]:
    print(f"{model}: {result}")
    """)

def demonstrate_setup():
    """Show how to set up OpenRouter"""

    print("\n" + "=" * 80)
    print("OpenRouter Setup Instructions")
    print("=" * 80)
    print("""
Step 1: Get API Key (Line 208)
   - Visit https://openrouter.ai/
   - Sign up for an account
   - Navigate to API Keys section
   - Generate a new API key

Step 2: Set Environment Variable (Line 214)
   export OPENROUTER_API_KEY="your-api-key-here"

Step 3: Install Dependencies (Line 217)
   uv run python main_openrouter.py

Step 4: Use in Your Code (Line 220)
   from openai import OpenAI

   client = OpenAI(
       base_url="https://openrouter.ai/api/v1",
       api_key=os.environ.get("OPENROUTER_API_KEY")
   )

That's it! You can now access 100+ models from different providers.
    """)

def main():
    """Main demonstration function"""
    print("\n")
    print("█" * 80)
    print("█" + " " * 78 + "█")
    print("█" + "  OpenRouter Python Demonstration".center(78) + "█")
    print("█" + "  Unified API for Multiple LLM Providers".center(78) + "█")
    print("█" + " " * 78 + "█")
    print("█" * 80)
    print()

    # Line 246: Call demonstration functions
    demonstrate_model_selection()
    demonstrate_practical_example()
    demonstrate_setup()

    # Line 250: Summary
    print("\n" + "=" * 80)
    print("Summary: Why Use OpenRouter?")
    print("=" * 80)
    print("""
✓ Unified API: One API format for 100+ models from different providers
✓ Easy Switching: Change models by updating a single parameter
✓ Cost Effective: Compare prices and use the most cost-effective model
✓ Redundancy: Fallback to other models if primary is unavailable
✓ Simplified Billing: One API key and bill for all providers
✓ No Lock-in: Switch providers anytime without changing your code
✓ Latest Models: Access to newest models as soon as they're released

OpenRouter abstracts away provider-specific APIs, making it easy to:
- Experiment with different models
- Build model-agnostic applications
- Compare model performance
- Optimize costs across providers
    """)

    print("\n" + "=" * 80)
    print("For more information:")
    print("  Documentation: https://openrouter.ai/docs")
    print("  Model List: https://openrouter.ai/models")
    print("  Pricing: https://openrouter.ai/models (includes cost per model)")
    print("=" * 80)
    print()

if __name__ == "__main__":
    # Line 280: Entry point
    main()
