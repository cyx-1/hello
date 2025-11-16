# Pydantic AI: Direct Model API Access

This demonstration shows how Pydantic AI doesn't abstract LLM requests into a single "lowest common denominator" API. Instead, it enables **direct access to provider-specific model APIs** while maintaining a model-agnostic interface.

## Philosophy

> "Why use the derivative when you can go straight to the source?"

Pydantic AI provides:
1. **Model-agnostic interface** - Easy to swap between providers
2. **Direct API access** - Full control over provider-specific features
3. **Type safety** - Pydantic-powered validation and IDE support

## Requirements

- Python >= 3.11
- pydantic-ai >= 0.2.0
- openai >= 1.0.0
- anthropic >= 0.40.0

## Running the Demo

```bash
uv run main_pydantic_ai_model_api.py
```

---

## Key Source Code Sections

### 1. Import Provider-Specific Settings (Lines 24-29)

```python
24: from pydantic_ai.settings import ModelSettings
25:
26: # Import provider-specific settings - THIS IS THE KEY POINT
27: # Each provider has its own settings class with provider-specific parameters
28: from pydantic_ai.models.openai import OpenAIModelSettings
29: from pydantic_ai.models.anthropic import AnthropicModelSettings
```

**Annotation**: The key insight is that Pydantic AI provides **separate settings classes for each provider**. These aren't just aliases - they contain provider-specific parameters that map directly to each provider's API.

---

### 2. Generic ModelSettings - Lowest Common Denominator (Lines 48-53)

```python
48:     # Generic settings that work across providers
49:     generic_settings = ModelSettings(
50:         max_tokens=150,
51:         temperature=0.7,
52:         top_p=0.9,
53:     )
```

**Output (Lines 1-9)**:
```
======================================================================
DEMO 1: Common ModelSettings (Generic/Abstracted)
======================================================================
Generic ModelSettings (works with any provider):
  max_tokens: 150
  temperature: 0.7
  top_p: 0.9

Limitation: Only common parameters, no provider-specific features
```

**Annotation**: Generic `ModelSettings` only supports parameters common to all providers. This is the "abstracted" approach - you lose access to unique provider capabilities.

---

### 3. OpenAI-Specific Settings - Direct API Access (Lines 71-86)

```python
71:     # OpenAI-specific settings - direct access to OpenAI API parameters
72:     openai_settings = OpenAIModelSettings(
73:         # Common parameters
74:         max_tokens=200,
75:         temperature=0.5,
76:         # OpenAI-SPECIFIC parameters - not available in other providers
77:         openai_reasoning_effort="high",      # For o1/o3 reasoning models
78:         openai_logprobs=True,                # Get log probabilities
79:         openai_top_logprobs=3,               # Top 3 token probabilities
80:         openai_user="user-123",              # Track end-user for abuse detection
81:         openai_service_tier="default",       # Service tier: auto, default, flex, priority
82:     )
```

**Output (Lines 11-24)**:
```
======================================================================
DEMO 2: OpenAI-Specific Settings (Direct API Access)
======================================================================
OpenAI-Specific Settings (Direct API Access):
  Common parameters:
    max_tokens: 200
    temperature: 0.5

  OpenAI-SPECIFIC parameters (not abstracted away):
    openai_reasoning_effort: high
    openai_logprobs: True
    openai_top_logprobs: 3
    openai_user: user-123
    openai_service_tier: default

Key Insight: These map DIRECTLY to OpenAI API parameters!
No abstraction layer - you're talking directly to OpenAI's API.
```

**Annotation**:
- **Line 77**: `openai_reasoning_effort` - Controls reasoning depth for o1/o3 models (OpenAI-only feature)
- **Line 78-79**: `openai_logprobs` and `openai_top_logprobs` - Get token probabilities for confidence analysis
- **Line 81**: `openai_service_tier` - Choose service tier (auto, default, flex, priority)

These parameters map **directly** to OpenAI's API. No abstraction layer is hiding these features from you.

---

### 4. Anthropic-Specific Settings - Extended Thinking (Lines 112-128)

```python
112:     # Anthropic-specific settings - direct access to Anthropic API parameters
113:     anthropic_settings = AnthropicModelSettings(
114:         # Common parameters
115:         max_tokens=50000,
116:         temperature=0.0,
117:         # Anthropic-SPECIFIC parameters
118:         anthropic_thinking={                  # Extended thinking (Claude specific!)
119:             "type": "enabled",
120:             "budget_tokens": 10000,
121:         },
122:         anthropic_cache_instructions=True,    # Cache system prompts
123:         anthropic_cache_tool_definitions=True, # Cache tool definitions
124:     )
```

**Output (Lines 26-39)**:
```
======================================================================
DEMO 3: Anthropic-Specific Settings (Direct API Access)
======================================================================
Anthropic-Specific Settings (Direct API Access):
  Common parameters:
    max_tokens: 50000
    temperature: 0.0

  Anthropic-SPECIFIC parameters (not abstracted away):
    anthropic_thinking: {'type': 'enabled', 'budget_tokens': 10000}
    anthropic_cache_instructions: True
    anthropic_cache_tool_definitions: True

Key Insight: Extended thinking is Claude-ONLY feature!
You can't abstract this into a generic API without losing the feature.
```

**Annotation**:
- **Lines 118-121**: `anthropic_thinking` - Enable Claude's extended thinking with token budget (Anthropic-only feature)
- **Line 122**: `anthropic_cache_instructions` - Cache system prompts for cost savings
- **Line 123**: `anthropic_cache_tool_definitions` - Cache tool definitions

Extended thinking is a Claude-exclusive feature. A generic abstraction layer would **hide this capability entirely**.

---

### 5. Settings Inheritance Hierarchy (Output Lines 93-109)

```
Settings Hierarchy (Pydantic-powered type safety):

  ModelSettings (Base)
      |
      |-- Common: max_tokens, temperature, top_p, seed, etc.
      |
      +-- OpenAIModelSettings (extends base)
      |       |-- openai_reasoning_effort
      |       |-- openai_logprobs
      |       |-- openai_top_logprobs
      |       |-- openai_user
      |       |-- openai_service_tier
      |       +-- openai_prediction
      |
      +-- AnthropicModelSettings (extends base)
      |       |-- anthropic_thinking
      |       |-- anthropic_cache_instructions
      |       +-- anthropic_cache_tool_definitions
      |
      +-- GeminiModelSettings (extends base)
              |-- gemini_safety_settings
              +-- gemini_generation_config
```

**Annotation**: Each provider-specific settings class **extends** the base `ModelSettings`, adding provider-specific parameters. This gives you:
- Type safety with IDE autocompletion
- Validation of all parameters
- Clear documentation of what each provider supports

---

## Real-World Use Case (Output Lines 111-143)

```
Scenario: Building a code review system

WITH Full Abstraction (limiting):
  settings = GenericSettings(max_tokens=1000, temperature=0)
  # Can't use Claude's extended thinking for deep analysis
  # Can't use OpenAI's logprobs to measure confidence
  # Stuck with generic features only

WITH Pydantic AI's Direct Access (empowering):

  # For CRITICAL code reviews - use Claude's extended thinking
  critical_review_settings = AnthropicModelSettings(
      anthropic_thinking={
          'type': 'enabled',
          'budget_tokens': 20000,  # Deep analysis
      },
      max_tokens=10000,
  )

  # For QUICK reviews - use OpenAI with confidence scoring
  quick_review_settings = OpenAIModelSettings(
      openai_logprobs=True,       # Confidence metrics
      openai_top_logprobs=5,      # Top 5 alternatives
      max_tokens=500,
  )

  # For COST-OPTIMIZED reviews - use OpenAI flex tier
  batch_review_settings = OpenAIModelSettings(
      openai_service_tier='flex',  # Lower cost, higher latency OK
      max_tokens=2000,
  )
```

**Annotation**: Direct API access lets you use the **right tool for the right job**:
- Critical reviews: Leverage Claude's extended thinking for deep analysis
- Quick reviews: Use OpenAI's logprobs for confidence metrics
- Cost-optimized: Use OpenAI's flex tier for batch processing

---

## Summary (Output Lines 145-167)

```
======================================================================
SUMMARY: Pydantic AI's Approach to Model APIs
======================================================================

1. NOT a 'lowest common denominator' abstraction
   - Other libraries: Force you into a generic API
   - Pydantic AI: Gives you direct access to each provider's API

2. Provider-specific TypedDict settings classes
   - OpenAIModelSettings: reasoning_effort, logprobs, service_tier
   - AnthropicModelSettings: thinking, cache_instructions
   - Each provider's unique features are DIRECTLY accessible

3. Best of both worlds
   - Model-agnostic: Easy to swap between providers
   - Provider-specific: Full access to unique capabilities

4. Type-safe and validated (Pydantic-powered)
   - IDE autocompletion for all settings
   - Runtime validation of parameters
   - Clear documentation of what each provider supports

Philosophy: Don't hide the API - EMBRACE it with type safety!
```

---

## Key Takeaways

1. **Direct API Access**: Provider-specific settings classes (e.g., `OpenAIModelSettings`, `AnthropicModelSettings`) map directly to provider APIs
2. **No Feature Loss**: Unlike generic abstractions, you can access unique features like Claude's extended thinking or OpenAI's logprobs
3. **Type Safety**: All settings are typed and validated by Pydantic
4. **Model Agnostic Core**: The `Agent` class remains model-agnostic while allowing provider-specific configurations
5. **Best of Both Worlds**: Easy to swap providers + full access to each provider's unique capabilities

## Version Notes

- Requires pydantic-ai >= 0.2.0 for provider-specific settings support
- OpenAI reasoning settings require o1/o3 models
- Anthropic thinking requires claude-3.5-sonnet-latest or newer
