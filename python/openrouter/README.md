# OpenRouter Python Demonstration

This demonstration shows how OpenRouter provides a unified API to connect to various Large Language Models (LLMs) from different providers including OpenAI, Anthropic, Meta, Google, and more.

## Requirements

- **Python**: >= 3.9
- **Dependencies**: `openai>=1.0.0` (automatically installed via inline script metadata)
- **API Key**: OpenRouter API key (get one at https://openrouter.ai/)

## What is OpenRouter?

OpenRouter is a unified API gateway that provides access to 100+ LLM models from different providers through a single, consistent API interface. Instead of managing multiple API keys and learning different API formats for each provider, you can use one API format (OpenAI-compatible) to access all models.

## Running the Demo

```bash
# Set your OpenRouter API key (optional for demo)
export OPENROUTER_API_KEY="your-api-key-here"

# Run the demonstration
uv run --script main_openrouter.py
```

## Key Source Code Sections

### 1. Client Initialization (Lines 19-24)

```python
# Line 19: Initialize OpenRouter client with API key
# OpenRouter uses OpenAI-compatible API, so we use the OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY", "demo-key-for-illustration"),
)
```

**Explanation**: The key to using OpenRouter is simply changing the `base_url` parameter to point to OpenRouter's API endpoint. The rest of the code uses the standard OpenAI client library, making it compatible with existing OpenAI code.

### 2. Multiple Provider Models (Lines 30-58)

```python
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
```

**Explanation**: This demonstrates the variety of models available through OpenRouter. Each model follows the format `provider/model-name`, making it easy to identify and switch between providers.

### 3. Unified API Structure (Lines 83-95)

```python
# Line 83: Example API call structure (works for all models)
response = client.chat.completions.create(
    model="<any-model-id-from-above>",  # Line 88: Simply change model ID
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ],
    max_tokens=150
)
print(response.choices[0].message.content)
```

**Explanation**: This is the core feature of OpenRouter - the same API call structure works for ALL models. You only need to change the `model` parameter to switch between providers like OpenAI, Anthropic, Meta, Google, etc.

### 4. Practical Reusable Function (Lines 151-168)

```python
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
```

**Explanation**: This function demonstrates model-agnostic code. The same function can query any LLM provider by simply passing different model IDs. This makes it easy to:
- Compare responses from different models
- Switch providers without code changes
- Implement fallback strategies
- A/B test different models

## Program Output

```
████████████████████████████████████████████████████████████████████████████████
█                                                                              █
█                        OpenRouter Python Demonstration                       █
█                     Unified API for Multiple LLM Providers                   █
█                                                                              █
████████████████████████████████████████████████████████████████████████████████

================================================================================
OpenRouter: Unified API for Multiple LLM Providers
================================================================================

Available Models Through OpenRouter:
--------------------------------------------------------------------------------
1. OpenAI GPT-4 Turbo
   Provider: OpenAI
   Model ID: openai/gpt-4-turbo

2. Anthropic Claude 3.5 Sonnet
   Provider: Anthropic
   Model ID: anthropic/claude-3.5-sonnet

3. Meta Llama 3.1 405B
   Provider: Meta
   Model ID: meta-llama/llama-3.1-405b-instruct

4. Google Gemini Pro 1.5
   Provider: Google
   Model ID: google/gemini-pro-1.5

5. Mistral Large
   Provider: Mistral AI
   Model ID: mistralai/mistral-large
```

**Output Annotation (Lines 65-73 → Output Lines 9-26)**: This section displays the variety of models available through OpenRouter. Notice how models from different providers (OpenAI, Anthropic, Meta, Google, Mistral) are all accessible through the same API.

```
================================================================================
Demonstrating Unified API: Same Code, Different Models
================================================================================

Test Prompt: 'Explain quantum computing in one sentence.'

Python Code Structure (works for ALL models above):
--------------------------------------------------------------------------------

response = client.chat.completions.create(
    model="<any-model-id-from-above>",  # Line 88: Simply change model ID
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ],
    max_tokens=150
)
print(response.choices[0].message.content)
```

**Output Annotation (Lines 83-95 → Output Lines 28-44)**: This shows the actual code structure that works across all providers. The key insight is that you only change the `model` parameter - everything else remains the same.

```
================================================================================
Key Feature: Easy Model Switching
================================================================================

To switch between providers, just change the model parameter:

# Using OpenAI: OpenAI GPT-4 Turbo
response = client.chat.completions.create(
    model="openai/gpt-4-turbo",  # Line 108: OpenAI model
    messages=[{"role": "user", "content": "Explain quantum computing in one sentence."}]
)

# Using Anthropic: Anthropic Claude 3.5 Sonnet
response = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",  # Line 108: Anthropic model
    messages=[{"role": "user", "content": "Explain quantum computing in one sentence."}]
)

# Using Meta: Meta Llama 3.1 405B
response = client.chat.completions.create(
    model="meta-llama/llama-3.1-405b-instruct",  # Line 108: Meta model
    messages=[{"role": "user", "content": "Explain quantum computing in one sentence."}]
)
```

**Output Annotation (Lines 97-107 → Output Lines 46-67)**: This demonstrates the power of OpenRouter. The exact same code structure is used for three different providers. This makes it trivial to:
- Switch providers based on cost
- Implement fallback strategies
- Compare model outputs
- Avoid vendor lock-in

```
================================================================================
OpenRouter Additional Features
================================================================================

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
```

**Output Annotation (Lines 114-141 → Output Lines 69-90)**: This section highlights advanced OpenRouter features:
- **Auto-routing**: Let OpenRouter choose the best model for your request
- **Cost tracking**: Monitor spending across providers in one place
- **Fallbacks**: Automatically switch to backup models if primary is unavailable
- **Provider control**: Fine-tune which providers to prefer
- **Simplified billing**: One invoice instead of managing multiple provider accounts

```
================================================================================
Practical Example: Multi-Model Query
================================================================================

Function Definition (Lines 151-168):
--------------------------------------------------------------------------------

def query_model(model_id: str, prompt: str) -> str:
    response = client.chat.completions.create(
        model=model_id,  # Line 175: Works with ANY OpenRouter model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message.content


Usage Examples:
--------------------------------------------------------------------------------

# Line 185: Query OpenAI's GPT-4
result1 = query_model("openai/gpt-4-turbo", "What is AI?")

# Line 188: Query Anthropic's Claude (same function!)
result2 = query_model("anthropic/claude-3.5-sonnet", "What is AI?")

# Line 191: Query Meta's Llama (same function!)
result3 = query_model("meta-llama/llama-3.1-405b-instruct", "What is AI?")

# Line 194: Compare responses from different models
for model, result in [("GPT-4", result1), ("Claude", result2), ("Llama", result3)]:
    print(f"{model}: {result}")
```

**Output Annotation (Lines 151-199 → Output Lines 92-118)**: This practical example shows how to build model-agnostic applications. The same `query_model()` function works with ANY model on OpenRouter, enabling:
- **Easy experimentation**: Try different models without changing your code
- **Model comparison**: Test multiple models with the same prompt
- **Production flexibility**: Switch models based on cost, performance, or availability

```
================================================================================
OpenRouter Setup Instructions
================================================================================

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
```

**Output Annotation (Lines 202-231 → Output Lines 120-145)**: Step-by-step setup instructions showing how simple it is to start using OpenRouter. You only need:
1. An OpenRouter API key
2. The OpenAI Python library
3. Change the base URL to OpenRouter's endpoint

```
================================================================================
Summary: Why Use OpenRouter?
================================================================================

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
```

**Output Annotation (Lines 250-268 → Output Lines 147-163)**: This summary captures the core value proposition of OpenRouter:

1. **Developer Experience**: Write code once, use with any model
2. **Flexibility**: Switch providers without code changes
3. **Cost Optimization**: Easily compare and use the most cost-effective model
4. **Reliability**: Implement fallback strategies across providers
5. **Future-proof**: Access new models as they're released without API changes

## Key Benefits Demonstrated

### 1. Unified API Interface
Instead of learning multiple APIs:
```python
# Without OpenRouter - different APIs for each provider
openai_client.chat.completions.create(...)      # OpenAI format
anthropic_client.messages.create(...)            # Anthropic format
cohere_client.chat(...)                          # Cohere format
```

With OpenRouter - one API for all:
```python
# With OpenRouter - same API for all providers
client.chat.completions.create(model="openai/gpt-4-turbo", ...)
client.chat.completions.create(model="anthropic/claude-3.5-sonnet", ...)
client.chat.completions.create(model="cohere/command-r-plus", ...)
```

### 2. Easy Provider Switching
Change one parameter to switch providers:
```python
# Today: Using GPT-4
response = client.chat.completions.create(
    model="openai/gpt-4-turbo",
    messages=[{"role": "user", "content": prompt}]
)

# Tomorrow: Switch to Claude (no other code changes needed!)
response = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",
    messages=[{"role": "user", "content": prompt}]
)
```

### 3. Cost Optimization
Compare costs across providers easily:
```python
# Try different models to find the best price/performance ratio
models_to_test = [
    "openai/gpt-4-turbo",              # Premium
    "anthropic/claude-3.5-sonnet",     # Premium
    "meta-llama/llama-3.1-70b",        # Mid-tier
    "google/gemini-flash-1.5",         # Budget
]

for model in models_to_test:
    # Same code, different costs
    response = query_model(model, prompt)
```

### 4. Fallback Strategy
Implement reliability through fallbacks:
```python
def query_with_fallback(prompt: str) -> str:
    # Try primary model first
    models = [
        "openai/gpt-4-turbo",           # Primary
        "anthropic/claude-3.5-sonnet",  # Fallback 1
        "meta-llama/llama-3.1-405b"     # Fallback 2
    ]

    for model in models:
        try:
            return query_model(model, prompt)
        except Exception:
            continue  # Try next model

    raise Exception("All models failed")
```

## Use Cases

1. **Model Comparison**: Test the same prompt across multiple models to find the best one
2. **Cost Optimization**: Switch to cheaper models for simple tasks
3. **High Availability**: Fallback to alternative providers if primary is down
4. **Experimentation**: Try new models without changing your codebase
5. **Multi-Model Applications**: Use different models for different features (e.g., GPT-4 for reasoning, Claude for writing, Llama for summarization)

## Additional Resources

- **OpenRouter Documentation**: https://openrouter.ai/docs
- **Available Models & Pricing**: https://openrouter.ai/models
- **OpenAI Python Library**: https://github.com/openai/openai-python

## Technical Notes

- **API Compatibility**: OpenRouter uses the OpenAI API format, making it compatible with existing OpenAI code
- **Authentication**: Uses a single API key for all providers via the `Authorization: Bearer` header
- **Response Format**: Returns responses in OpenAI's format, ensuring compatibility with existing tools
- **Rate Limiting**: Each provider has its own rate limits, enforced by OpenRouter
- **Cost Tracking**: Response headers include cost information for billing tracking

---

*This demonstration uses Python 3.9+ and the OpenAI Python library (>=1.0.0). The code runs via uv with inline script metadata for dependency management.*
