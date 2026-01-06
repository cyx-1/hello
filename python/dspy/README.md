# DSPy Framework Illustration

DSPy is a framework for algorithmically optimizing language model (LM) prompts and weights. Instead of manually crafting prompts, DSPy allows you to program with language models using declarative signatures and modular components.

## Overview

This example demonstrates:
1. **Basic Signatures and Predictors** - Defining input/output specifications
2. **Chain of Thought Reasoning** - Adding reasoning steps to predictions
3. **Multi-Step Pipelines** - Composing multiple modules together
4. **Typed Signatures** - Working with multiple inputs
5. **Custom Modules** - Building reusable DSPy components

## Requirements

- **Python Version**: Python 3.10+
- **Key Dependencies**:
  - `dspy-ai>=2.5.0` - The DSPy framework
  - `openai>=1.0.0` - OpenAI API client (or other LM providers)

## Running the Example

```bash
uv run python main_dspy.py
```

**Note**: Requires `OPENAI_API_KEY` environment variable or another configured LM provider.

## Source Code with Annotations

### Setup and Configuration (Lines 1-28)

```python
1   #!/usr/bin/env python3
2   # /// script
3   # dependencies = [
4   #     "dspy-ai>=2.5.0",
5   #     "openai>=1.0.0",
6   # ]
7   # ///
```

**Lines 2-7**: Inline script metadata for `uv` to automatically install dependencies

```python
23  def setup_language_model():
24      """Configure DSPy to use OpenAI's GPT model."""
25      lm = dspy.LM('openai/gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY'))
26      dspy.configure(lm=lm)
27      print("✓ Language model configured\n")
```

**Line 25**: Initialize a language model using DSPy's `LM` class
**Line 26**: Configure DSPy globally to use this model for all predictions

### Example 1: Basic Signature and Predictor (Lines 30-55)

```python
38  class GenerateAnswer(dspy.Signature):
39      """Answer questions with short factual answers."""
40      question = dspy.InputField()
41      answer = dspy.OutputField(desc="often between 1 and 5 words")
```

**Lines 38-41**: Define a DSPy **Signature** - this is a declarative specification of what the module should do
- The docstring (line 39) describes the task
- `InputField` (line 40) marks inputs to the module
- `OutputField` (line 41) marks expected outputs with constraints

```python
45  predictor = dspy.Predict(GenerateAnswer)
```

**Line 45**: Create a **Predict** module - the basic DSPy building block that uses the signature

```python
48  question = "What is the capital of France?"
49  result = predictor(question=question)
```

**Lines 48-49**: Execute the predictor with input

#### Example Output:

```
============================================================
EXAMPLE 1: Basic Signature and Predictor
============================================================
Question: What is the capital of France?
Answer: Paris
```

**Analysis**: The predictor uses the signature to understand it should provide a short, factual answer (1-5 words). DSPy automatically converts this into appropriate prompts for the LM.

### Example 2: Chain of Thought Reasoning (Lines 57-82)

```python
63  class AnalyzeQuestion(dspy.Signature):
64      """Analyze a question and provide a reasoned answer."""
65      question = dspy.InputField()
66      answer = dspy.OutputField(desc="detailed answer with reasoning")
```

**Lines 63-66**: Signature for a more complex reasoning task

```python
69  cot = dspy.ChainOfThought(AnalyzeQuestion)
```

**Line 69**: **ChainOfThought** is a more advanced module that:
- First generates a reasoning step (rationale)
- Then produces the final answer
- Improves accuracy for complex tasks

#### Example Output:

```
============================================================
EXAMPLE 2: Chain of Thought Reasoning
============================================================
Question: If a train travels 120 miles in 2 hours, what is its average speed?
Reasoning: To find average speed, we divide total distance by total time. Distance is 120 miles and time is 2 hours. 120 ÷ 2 = 60.
Answer: The average speed is 60 miles per hour (mph).
```

**Analysis**: Notice how `result.rationale` (line 76) contains the reasoning process, while `result.answer` (line 77) contains the final answer. The ChainOfThought module automatically prompted the LM to "think step by step".

### Example 3: Multi-Step Pipeline (Lines 84-119)

```python
91  class GenerateIdea(dspy.Signature):
92      """Generate a creative idea based on a topic."""
93      topic = dspy.InputField()
94      idea = dspy.OutputField(desc="a creative and novel idea")
95
96  class EvaluateIdea(dspy.Signature):
97      """Evaluate an idea and provide feedback."""
98      idea = dspy.InputField()
99      evaluation = dspy.OutputField(desc="assessment of feasibility and impact")
```

**Lines 91-99**: Define two separate signatures for different steps in a pipeline

```python
103 generate = dspy.Predict(GenerateIdea)
104 evaluate = dspy.ChainOfThought(EvaluateIdea)
105
106 topic = "sustainable urban transportation"
107
108 idea_result = generate(topic=topic)
109 eval_result = evaluate(idea=idea_result.idea)
```

**Lines 103-109**: Create a **pipeline** by chaining modules together:
1. First module generates an idea
2. Second module evaluates that idea
3. Output of first module feeds into second module

#### Example Output:

```
============================================================
EXAMPLE 3: Multi-Step Pipeline
============================================================
Topic: sustainable urban transportation

Generated Idea: Implement a network of underground automated electric pods that run on magnetic levitation tracks, connecting major city hubs with residential areas, powered entirely by rooftop solar panels.

Evaluation Reasoning: This idea combines multiple proven technologies (maglev, electric vehicles, solar power) in a novel way. The underground aspect addresses surface congestion. However, infrastructure cost would be extremely high, and underground construction faces geological challenges. The solar power requirement would need substantial surface area.

Evaluation: Highly innovative but faces significant implementation barriers. Feasibility is moderate (requires 10-15 year timeline and billions in investment). Environmental impact would be strongly positive. Social impact could be transformative for urban mobility if successfully implemented.
```

**Analysis**: This demonstrates **modular composition** - a key DSPy concept. Each module has a single responsibility, and they can be combined into complex workflows.

### Example 4: Typed Signatures with Multiple Inputs (Lines 121-147)

```python
127 class CompareEntities(dspy.Signature):
128     """Compare two entities and highlight key differences."""
129     entity1 = dspy.InputField()
130     entity2 = dspy.InputField()
131     comparison = dspy.OutputField(desc="structured comparison")
```

**Lines 127-131**: Signatures can have **multiple input fields**

```python
137 result = compare(
138     entity1="Python",
139     entity2="Rust"
140 )
```

**Lines 137-140**: Pass multiple named arguments to the predictor

#### Example Output:

```
============================================================
EXAMPLE 4: Typed Signatures with Multiple Inputs
============================================================
Comparing: Python vs Rust

Reasoning: These are both popular programming languages but serve different niches. Python emphasizes readability and rapid development, while Rust focuses on performance and memory safety. I should compare them across key dimensions like performance, learning curve, use cases, and ecosystem.

Comparison:
- Performance: Rust is significantly faster (compiled, zero-cost abstractions) vs Python (interpreted, dynamic typing)
- Memory Safety: Rust has compile-time memory safety guarantees vs Python relies on garbage collection
- Learning Curve: Python is beginner-friendly with simple syntax vs Rust has steep learning curve (ownership, lifetimes)
- Use Cases: Python excels in data science, ML, scripting vs Rust for systems programming, embedded systems, performance-critical applications
- Ecosystem: Python has mature, extensive libraries vs Rust's ecosystem is growing rapidly but smaller
- Development Speed: Python enables rapid prototyping vs Rust requires more upfront design
```

**Analysis**: Multiple inputs allow for comparative analysis, relationship mapping, and other multi-entity tasks.

### Example 5: Custom DSPy Module (Lines 149-177)

```python
157 class BlogPostGenerator(dspy.Module):
158     """Custom module that generates a blog post with title and content."""
159
160     def __init__(self):
161         super().__init__()
162         # Line 163: Define sub-modules as attributes
163         self.generate_title = dspy.Predict("topic -> title")
164         self.generate_content = dspy.ChainOfThought("topic, title -> content")
165
166     def forward(self, topic):
167         """Forward method defines the module's execution logic."""
168         # Line 168-170: Chain multiple predictions together
169         title = self.generate_title(topic=topic).title
170         content = self.generate_content(topic=topic, title=title).content
171         return dspy.Prediction(title=title, content=content)
```

**Lines 157-171**: Create a **custom DSPy module** by:
1. Subclassing `dspy.Module` (line 157)
2. Defining sub-modules in `__init__` (lines 163-164)
3. Implementing `forward()` method with execution logic (lines 166-171)

**Line 163**: DSPy supports **string-based signature syntax** for concise definitions: `"input1, input2 -> output"`

```python
173 blog_gen = BlogPostGenerator()
174 result = blog_gen(topic="The Future of AI in Healthcare")
```

**Lines 173-174**: Custom modules are used just like built-in ones

#### Example Output:

```
============================================================
EXAMPLE 5: Custom DSPy Module
============================================================
Topic: The Future of AI in Healthcare

Generated Title: Transforming Patient Care: How AI is Revolutionizing Healthcare Delivery

Generated Content: Artificial intelligence is poised to fundamentally reshape healthcare over the next decade. From diagnostic assistance to personalized treatment plans, AI systems are already demonstrating capabilities that augment and enhance medical professionals' expertise. Machine learning algorithms can now detect patterns in medical imaging that human eyes might miss, while natural language processing helps physicians navigate vast medical literature in seconds. However, the true transformation lies not in AI replacing doctors, but in creating a collaborative ecosystem where technology handles data-intensive tasks, freeing clinicians to focus on patient relationships and complex decision-making. Privacy, bias, and regulatory challenges remain, but the trajectory is clear: AI will become an indispensable partner in delivering better, more accessible healthcare to all.
```

**Analysis**: Custom modules encapsulate complex logic and can be:
- Reused across different projects
- Optimized as a single unit
- Tested independently
- Composed with other modules

## Key DSPy Concepts Illustrated

### 1. Signatures (Declarative Specifications)
Instead of writing prompts, you declare what you want:
```python
class TaskName(dspy.Signature):
    """What the task does"""
    input_field = dspy.InputField()
    output_field = dspy.OutputField(desc="constraints")
```

### 2. Modules (Building Blocks)
- `dspy.Predict` - Basic prediction
- `dspy.ChainOfThought` - Adds reasoning step
- `dspy.Module` - Base class for custom modules

### 3. Composition (Building Pipelines)
Modules can be chained together:
```python
step1 = dspy.Predict(Signature1)
step2 = dspy.ChainOfThought(Signature2)
result = step2(input=step1(input=data).output)
```

### 4. Optimization (Not shown in this example)
DSPy can automatically optimize prompts using:
- `dspy.BootstrapFewShot` - Learn from examples
- `dspy.BootstrapFewShotWithRandomSearch` - Search for better prompts
- `dspy.LabeledFewShot` - Use labeled training data

## Why Use DSPy?

1. **Declarative Programming**: Specify *what* you want, not *how* to prompt
2. **Modularity**: Build reusable components that compose cleanly
3. **Optimization**: Automatically improve prompts with data
4. **Maintainability**: Changes to signatures don't require rewriting prompts
5. **Model Agnostic**: Works with OpenAI, Anthropic, local models, etc.

## Running the Code

The code is self-contained and can be run with:

```bash
# Set your API key
export OPENAI_API_KEY="your-key-here"

# Run with uv (automatically installs dependencies)
uv run python main_dspy.py
```

Alternative LM providers can be configured:
```python
# Anthropic Claude
lm = dspy.LM('anthropic/claude-3-5-sonnet-20241022', api_key=os.getenv('ANTHROPIC_API_KEY'))

# Local model via Ollama
lm = dspy.LM('ollama/llama2')
```

---

*Last updated: 2026-01-06*
