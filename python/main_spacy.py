#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "spacy>=3.7.0",
# ]
# ///

"""
Comprehensive SpaCy NLP Demonstration
This script showcases various SpaCy features including:
- Loading language models
- Named Entity Recognition (NER)
- Part-of-Speech (POS) tagging
- Dependency parsing
- Token attributes
- Sentence segmentation
- Lemmatization
- Text similarity
"""

import spacy
import sys


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'=' * 80}")
    print(f"  {title}")
    print(f"{'=' * 80}\n")


def download_model_if_needed():
    """Check if the English model is installed"""
    try:
        spacy.load("en_core_web_sm")
        print("✓ SpaCy model 'en_core_web_sm' is already installed\n")
        return True
    except OSError:
        print("=" * 80)
        print("  MODEL NOT FOUND")
        print("=" * 80)
        print("\n⚠ The SpaCy language model 'en_core_web_sm' is not installed.")
        print("\nTo download and install the model, run:")
        print("  uv run --with spacy -m spacy download en_core_web_sm")
        print("\nOr in a standard Python environment:")
        print("  python -m spacy download en_core_web_sm")
        print("\nAlternatively, you can install it directly:")
        print("  uv pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl")
        print("\n" + "=" * 80)
        return False


def demonstrate_basic_processing(nlp):
    """Demonstrate basic text processing and token attributes"""
    print_section("1. BASIC TEXT PROCESSING & TOKEN ATTRIBUTES")

    text = "Apple Inc. is looking at buying U.K. startup for $1 billion in 2024."
    doc = nlp(text)

    print(f"Original text: {text}\n")
    print(f"{'Token':<15} {'Lemma':<15} {'POS':<10} {'Tag':<10} {'Dep':<10} {'Shape':<10} {'Is Alpha':<10} {'Is Stop'}")
    print("-" * 100)

    for token in doc:
        print(f"{token.text:<15} {token.lemma_:<15} {token.pos_:<10} {token.tag_:<10} "
              f"{token.dep_:<10} {token.shape_:<10} {str(token.is_alpha):<10} {token.is_stop}")


def demonstrate_named_entities(nlp):
    """Demonstrate Named Entity Recognition"""
    print_section("2. NAMED ENTITY RECOGNITION (NER)")

    text = ("Tesla CEO Elon Musk announced on Twitter that the company will open a new "
            "factory in Berlin, Germany next year. The facility will cost approximately "
            "€4 billion and create 12,000 jobs.")

    doc = nlp(text)

    print(f"Text: {text}\n")
    print(f"{'Entity':<20} {'Label':<15} {'Description'}")
    print("-" * 70)

    for ent in doc.ents:
        print(f"{ent.text:<20} {ent.label_:<15} {spacy.explain(ent.label_)}")


def demonstrate_dependency_parsing(nlp):
    """Demonstrate dependency parsing"""
    print_section("3. DEPENDENCY PARSING")

    text = "The quick brown fox jumps over the lazy dog."
    doc = nlp(text)

    print(f"Text: {text}\n")
    print(f"{'Token':<15} {'Dependency':<15} {'Head':<15} {'Head POS':<10} {'Children'}")
    print("-" * 80)

    for token in doc:
        children = ", ".join([child.text for child in token.children])
        print(f"{token.text:<15} {token.dep_:<15} {token.head.text:<15} "
              f"{token.head.pos_:<10} {children}")


def demonstrate_sentences(nlp):
    """Demonstrate sentence segmentation"""
    print_section("4. SENTENCE SEGMENTATION")

    text = ("SpaCy is an open-source library. It's designed for production use. "
            "You can use it to build information extraction systems. "
            "Or natural language understanding systems!")

    doc = nlp(text)

    print(f"Original text: {text}\n")
    print("Detected sentences:")
    print("-" * 80)

    for i, sent in enumerate(doc.sents, 1):
        print(f"{i}. {sent.text}")


def demonstrate_noun_chunks(nlp):
    """Demonstrate noun phrase extraction"""
    print_section("5. NOUN PHRASE EXTRACTION")

    text = ("The autonomous vehicles from the innovative tech company are revolutionizing "
            "the transportation industry with cutting-edge artificial intelligence.")

    doc = nlp(text)

    print(f"Text: {text}\n")
    print("Extracted noun phrases:")
    print("-" * 80)

    for chunk in doc.noun_chunks:
        print(f"  • {chunk.text:<40} (root: {chunk.root.text}, dependency: {chunk.root.dep_})")


def demonstrate_similarity(nlp):
    """Demonstrate text similarity (requires medium or large model with vectors)"""
    print_section("6. TEXT SIMILARITY")

    # Check if model has word vectors
    if not nlp.meta.get("vectors", {}).get("width", 0):
        print("⚠ Note: The 'en_core_web_sm' model doesn't include word vectors.")
        print("For similarity calculations, consider using 'en_core_web_md' or 'en_core_web_lg'.\n")
        print("Demonstrating with token similarity (limited accuracy):")

    doc1 = nlp("I like cats")
    doc2 = nlp("I love dogs")
    doc3 = nlp("The weather is sunny")

    print(f"Document 1: '{doc1.text}'")
    print(f"Document 2: '{doc2.text}'")
    print(f"Document 3: '{doc3.text}'\n")

    print("Similarity scores:")
    print(f"  doc1 <-> doc2: {doc1.similarity(doc2):.4f}")
    print(f"  doc1 <-> doc3: {doc1.similarity(doc3):.4f}")
    print(f"  doc2 <-> doc3: {doc2.similarity(doc3):.4f}")


def demonstrate_linguistic_features(nlp):
    """Demonstrate advanced linguistic features"""
    print_section("7. LINGUISTIC FEATURES & MORPHOLOGY")

    text = "She was running quickly through the beautiful gardens yesterday."
    doc = nlp(text)

    print(f"Text: {text}\n")
    print(f"{'Token':<15} {'POS':<10} {'Morphology'}")
    print("-" * 80)

    for token in doc:
        morph = str(token.morph) if token.morph else "—"
        print(f"{token.text:<15} {token.pos_:<10} {morph}")


def demonstrate_custom_attributes(nlp):
    """Demonstrate custom pipeline component"""
    print_section("8. CUSTOM PIPELINE COMPONENT")

    from spacy.language import Language
    from spacy.tokens import Doc

    # Register custom attribute
    if not Doc.has_extension("has_number"):
        Doc.set_extension("has_number", default=False)

    # Create custom component
    @Language.component("number_detector")
    def number_detector_component(doc):
        """Custom component to detect if document contains numbers"""
        doc._.has_number = any(token.like_num for token in doc)
        return doc

    # Add component to pipeline if not already there
    if "number_detector" not in nlp.pipe_names:
        nlp.add_pipe("number_detector", last=True)

    print("Pipeline components:", nlp.pipe_names)
    print()

    texts = [
        "There are 42 students in the class.",
        "The meeting is tomorrow.",
        "We need approximately 1000 units."
    ]

    print("Testing custom number detector:")
    print("-" * 80)
    for text in texts:
        doc = nlp(text)
        print(f"Text: '{text}'")
        print(f"Contains number: {doc._.has_number}\n")


def demonstrate_matcher(nlp):
    """Demonstrate pattern matching"""
    print_section("9. PATTERN MATCHING")

    from spacy.matcher import Matcher

    matcher = Matcher(nlp.vocab)

    # Define patterns
    patterns = [
        [{"LOWER": "hello"}, {"LOWER": "world"}],
        [{"LOWER": "artificial"}, {"LOWER": "intelligence"}],
        [{"POS": "ADJ"}, {"POS": "NOUN"}]
    ]

    matcher.add("PATTERNS", patterns)

    text = "Hello world! Artificial intelligence and machine learning are powerful technologies."
    doc = nlp(text)

    print(f"Text: {text}\n")
    print("Matches found:")
    print("-" * 80)

    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        print(f"  • '{span.text}' (pattern: {nlp.vocab.strings[match_id]})")


def main():
    """Main function to run all demonstrations"""
    print("=" * 80)
    print("  COMPREHENSIVE SPACY NLP DEMONSTRATION")
    print("=" * 80)

    # Check if model is available
    if not download_model_if_needed():
        print("\nExiting. Please install the model first.")
        sys.exit(1)

    # Load the English NLP model
    print("Loading SpaCy model...")
    nlp = spacy.load("en_core_web_sm")
    print(f"✓ Loaded model: {nlp.meta['name']} (version {nlp.meta['version']})")
    print(f"  Language: {nlp.meta['lang']}")
    print(f"  Pipeline: {nlp.pipe_names}")

    # Run all demonstrations
    demonstrate_basic_processing(nlp)
    demonstrate_named_entities(nlp)
    demonstrate_dependency_parsing(nlp)
    demonstrate_sentences(nlp)
    demonstrate_noun_chunks(nlp)
    demonstrate_similarity(nlp)
    demonstrate_linguistic_features(nlp)
    demonstrate_custom_attributes(nlp)
    demonstrate_matcher(nlp)

    print_section("DEMONSTRATION COMPLETE")
    print("For more information, visit: https://spacy.io/")
    print()


if __name__ == "__main__":
    main()
