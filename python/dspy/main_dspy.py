#!/usr/bin/env python3
# /// script
# dependencies = [
#     "dspy-ai>=2.5.0",
#     "openai>=1.0.0",
# ]
# ///

"""
DSPy Framework Illustration

This script demonstrates the core concepts of DSPy:
1. Signatures - defining input/output specifications
2. Predictors - basic DSPy modules
3. ChainOfThought - reasoning modules
4. Module composition - building complex pipelines
"""

import dspy
import os


def setup_language_model():
    """Configure DSPy to use OpenAI's GPT model."""
    # Line 24: Initialize OpenAI language model
    # Note: Requires OPENAI_API_KEY environment variable
    lm = dspy.LM('openai/gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY', 'dummy-key-for-demo'))
    dspy.configure(lm=lm)
    print("✓ Language model configured\n")


def example_1_basic_signature():
    """Example 1: Basic DSPy Signature and Predictor"""
    print("=" * 60)
    print("EXAMPLE 1: Basic Signature and Predictor")
    print("=" * 60)

    # Line 38-40: Define a signature - specifies what the module should do
    # Signature format: "input_field -> output_field" with descriptions
    class GenerateAnswer(dspy.Signature):
        """Answer questions with short factual answers."""
        question = dspy.InputField()
        answer = dspy.OutputField(desc="often between 1 and 5 words")

    # Line 45: Create a basic Predict module using the signature
    predictor = dspy.Predict(GenerateAnswer)

    # Line 48: Execute the predictor with a question
    question = "What is the capital of France?"
    result = predictor(question=question)

    print(f"Question: {question}")
    print(f"Answer: {result.answer}")
    print()


def example_2_chain_of_thought():
    """Example 2: Chain of Thought Reasoning"""
    print("=" * 60)
    print("EXAMPLE 2: Chain of Thought Reasoning")
    print("=" * 60)

    # Line 63-66: Define signature for reasoning task
    class AnalyzeQuestion(dspy.Signature):
        """Analyze a question and provide a reasoned answer."""
        question = dspy.InputField()
        answer = dspy.OutputField(desc="detailed answer with reasoning")

    # Line 69: ChainOfThought adds reasoning step before answering
    # This prompts the model to show its thinking process
    cot = dspy.ChainOfThought(AnalyzeQuestion)

    # Line 73: Execute with a question requiring reasoning
    question = "If a train travels 120 miles in 2 hours, what is its average speed?"
    result = cot(question=question)

    print(f"Question: {question}")
    print(f"Reasoning: {result.rationale}")
    print(f"Answer: {result.answer}")
    print()


def example_3_multi_step_pipeline():
    """Example 3: Multi-step Pipeline with Module Composition"""
    print("=" * 60)
    print("EXAMPLE 3: Multi-Step Pipeline")
    print("=" * 60)

    # Line 91-94: First step - generate a creative idea
    class GenerateIdea(dspy.Signature):
        """Generate a creative idea based on a topic."""
        topic = dspy.InputField()
        idea = dspy.OutputField(desc="a creative and novel idea")

    # Line 97-100: Second step - evaluate the idea
    class EvaluateIdea(dspy.Signature):
        """Evaluate an idea and provide feedback."""
        idea = dspy.InputField()
        evaluation = dspy.OutputField(desc="assessment of feasibility and impact")

    # Line 103-106: Create a pipeline by composing modules
    generate = dspy.Predict(GenerateIdea)
    evaluate = dspy.ChainOfThought(EvaluateIdea)

    topic = "sustainable urban transportation"

    # Line 109-110: Execute pipeline steps
    idea_result = generate(topic=topic)
    eval_result = evaluate(idea=idea_result.idea)

    print(f"Topic: {topic}")
    print(f"\nGenerated Idea: {idea_result.idea}")
    print(f"\nEvaluation Reasoning: {eval_result.rationale}")
    print(f"Evaluation: {eval_result.evaluation}")
    print()


def example_4_typed_signatures():
    """Example 4: Typed Predictors with Multiple Inputs"""
    print("=" * 60)
    print("EXAMPLE 4: Typed Signatures with Multiple Inputs")
    print("=" * 60)

    # Line 127-132: Multi-input signature for comparison tasks
    class CompareEntities(dspy.Signature):
        """Compare two entities and highlight key differences."""
        entity1 = dspy.InputField()
        entity2 = dspy.InputField()
        comparison = dspy.OutputField(desc="structured comparison")

    # Line 134: Using ChainOfThought for complex comparison
    compare = dspy.ChainOfThought(CompareEntities)

    # Line 137-138: Execute with two entities to compare
    result = compare(
        entity1="Python",
        entity2="Rust"
    )

    print("Comparing: Python vs Rust")
    print(f"\nReasoning: {result.rationale}")
    print(f"Comparison: {result.comparison}")
    print()


def example_5_custom_module():
    """Example 5: Creating a Custom DSPy Module"""
    print("=" * 60)
    print("EXAMPLE 5: Custom DSPy Module")
    print("=" * 60)

    # Line 157-172: Define a custom module by subclassing dspy.Module
    class BlogPostGenerator(dspy.Module):
        """Custom module that generates a blog post with title and content."""

        def __init__(self):
            super().__init__()
            # Line 163: Define sub-modules as attributes
            self.generate_title = dspy.Predict("topic -> title")
            self.generate_content = dspy.ChainOfThought("topic, title -> content")

        def forward(self, topic):
            """Forward method defines the module's execution logic."""
            # Line 168-170: Chain multiple predictions together
            title = self.generate_title(topic=topic).title
            content = self.generate_content(topic=topic, title=title).content
            return dspy.Prediction(title=title, content=content)

    # Line 173: Instantiate and use the custom module
    blog_gen = BlogPostGenerator()
    result = blog_gen(topic="The Future of AI in Healthcare")

    print("Topic: The Future of AI in Healthcare")
    print(f"\nGenerated Title: {result.title}")
    print(f"\nGenerated Content: {result.content}")
    print()


def main():
    """Main execution function."""
    print("\n" + "=" * 60)
    print("DSPy Framework Demonstration")
    print("=" * 60 + "\n")

    # Line 191: Setup the language model
    setup_language_model()

    # Line 194-198: Run all examples sequentially
    example_1_basic_signature()
    example_2_chain_of_thought()
    example_3_multi_step_pipeline()
    example_4_typed_signatures()
    example_5_custom_module()

    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
