#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "nltk>=3.9.1",
#     "numpy>=1.24.0",
# ]
# ///

"""
Comprehensive NLTK (Natural Language Toolkit) Demonstration

This script showcases various NLTK capabilities including:
- Tokenization (word and sentence)
- Stopwords removal
- Stemming and Lemmatization
- Part-of-Speech (POS) tagging
- Named Entity Recognition (NER)
- Frequency distributions
- Collocations
- Sentiment analysis
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.probability import FreqDist
from nltk import pos_tag, ne_chunk
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.sentiment import SentimentIntensityAnalyzer


def download_nltk_data():
    """Download required NLTK data packages"""
    print("=" * 80)
    print("DOWNLOADING NLTK DATA")
    print("=" * 80)

    required_packages = [
        "punkt",
        "stopwords",
        "wordnet",
        "averaged_perceptron_tagger",
        "maxent_ne_chunker",
        "maxent_ne_chunker_tab",
        "words",
        "vader_lexicon",
        "punkt_tab",
        "averaged_perceptron_tagger_eng",
    ]

    for package in required_packages:
        try:
            nltk.download(package, quiet=True)
            print(f"✓ Downloaded: {package}")
        except Exception as e:
            print(f"✗ Failed to download {package}: {e}")
    print()


def demonstrate_tokenization():
    """Demonstrate word and sentence tokenization"""
    print("=" * 80)
    print("1. TOKENIZATION")
    print("=" * 80)

    text = "NLTK is amazing! It's a powerful library for natural language processing. Let's explore it."
    print(f"Original text:\n{text}\n")

    # Sentence tokenization
    sentences = sent_tokenize(text)
    print("Sentence Tokenization:")
    for i, sentence in enumerate(sentences, 1):
        print(f"  Sentence {i}: {sentence}")
    print()

    # Word tokenization
    words = word_tokenize(text)
    print(f"Word Tokenization:\n  {words}")
    print(f"  Total words: {len(words)}")
    print()


def demonstrate_stopwords():
    """Demonstrate stopwords removal"""
    print("=" * 80)
    print("2. STOPWORDS REMOVAL")
    print("=" * 80)

    text = (
        "This is an example sentence demonstrating the removal of stopwords from text."
    )
    words = word_tokenize(text.lower())
    print(f"Original words:\n  {words}\n")

    stop_words = set(stopwords.words("english"))
    print(f"Number of English stopwords: {len(stop_words)}")
    print(f"Sample stopwords: {list(stop_words)[:10]}\n")

    filtered_words = [
        word for word in words if word.isalnum() and word not in stop_words
    ]
    print(f"Filtered words (without stopwords):\n  {filtered_words}")
    print()


def demonstrate_stemming():
    """Demonstrate stemming with Porter Stemmer"""
    print("=" * 80)
    print("3. STEMMING (Porter Stemmer)")
    print("=" * 80)

    stemmer = PorterStemmer()
    words = [
        "running",
        "runs",
        "ran",
        "runner",
        "easily",
        "fairly",
        "connection",
        "connected",
        "connecting",
    ]

    print("Stemming reduces words to their root form:\n")
    for word in words:
        stemmed = stemmer.stem(word)
        print(f"  {word:15} -> {stemmed}")
    print()


def demonstrate_lemmatization():
    """Demonstrate lemmatization"""
    print("=" * 80)
    print("4. LEMMATIZATION")
    print("=" * 80)

    lemmatizer = WordNetLemmatizer()
    words = [
        ("running", "v"),
        ("runs", "v"),
        ("ran", "v"),
        ("better", "a"),
        ("good", "a"),
        ("cacti", "n"),
        ("geese", "n"),
        ("feet", "n"),
    ]

    print("Lemmatization finds the dictionary form of words:\n")
    for word, pos in words:
        lemma = lemmatizer.lemmatize(word, pos=pos)
        print(f"  {word:15} ({pos}) -> {lemma}")
    print()


def demonstrate_pos_tagging():
    """Demonstrate Part-of-Speech tagging"""
    print("=" * 80)
    print("5. PART-OF-SPEECH (POS) TAGGING")
    print("=" * 80)

    sentence = "The quick brown fox jumps over the lazy dog"
    words = word_tokenize(sentence)
    pos_tags = pos_tag(words)

    print(f"Sentence: {sentence}\n")
    print("POS Tags:")
    for word, tag in pos_tags:
        print(f"  {word:10} -> {tag:5} ({get_pos_description(tag)})")
    print()


def get_pos_description(tag):
    """Get human-readable description of POS tag"""
    pos_descriptions = {
        "NN": "Noun",
        "NNS": "Noun plural",
        "NNP": "Proper noun",
        "VB": "Verb base",
        "VBD": "Verb past",
        "VBZ": "Verb 3rd person",
        "JJ": "Adjective",
        "JJR": "Adjective comparative",
        "DT": "Determiner",
        "IN": "Preposition",
        "RB": "Adverb",
        "PRP": "Pronoun",
        "CC": "Conjunction",
    }
    return pos_descriptions.get(tag, "Other")


def demonstrate_ner():
    """Demonstrate Named Entity Recognition"""
    print("=" * 80)
    print("6. NAMED ENTITY RECOGNITION (NER)")
    print("=" * 80)

    sentence = "Apple Inc. was founded by Steve Jobs in Cupertino, California in 1976."
    words = word_tokenize(sentence)
    pos_tags = pos_tag(words)
    named_entities = ne_chunk(pos_tags)

    print(f"Sentence: {sentence}\n")
    print("Named Entities:")
    for entity in named_entities:
        if hasattr(entity, "label"):
            entity_text = " ".join(word for word, tag in entity)
            print(f"  {entity_text:20} -> {entity.label()}")
    print()


def demonstrate_frequency_distribution():
    """Demonstrate frequency distribution"""
    print("=" * 80)
    print("7. FREQUENCY DISTRIBUTION")
    print("=" * 80)

    text = """
    Natural language processing with NLTK is powerful. NLTK provides tools for processing.
    Processing text with NLTK enables many applications. Natural language is complex.
    """

    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum()]

    freq_dist = FreqDist(words)

    print("Top 10 most common words:")
    for word, frequency in freq_dist.most_common(10):
        print(f"  {word:15} -> {frequency} occurrences")
    print()


def demonstrate_collocations():
    """Demonstrate bigram collocations"""
    print("=" * 80)
    print("8. COLLOCATIONS (Bigrams)")
    print("=" * 80)

    text = """
    Machine learning and artificial intelligence are transforming natural language processing.
    Deep learning models like neural networks enable better natural language understanding.
    Natural language processing applications include machine translation and text analysis.
    """

    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum()]

    bigram_measures = BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(words)
    finder.apply_freq_filter(2)  # Only bigrams that appear at least 2 times

    print("Top collocations (word pairs that frequently occur together):")
    for bigram, score in finder.score_ngrams(bigram_measures.raw_freq)[:10]:
        print(f"  {bigram[0]} {bigram[1]:20} -> score: {score:.4f}")
    print()


def demonstrate_sentiment_analysis():
    """Demonstrate sentiment analysis using VADER"""
    print("=" * 80)
    print("9. SENTIMENT ANALYSIS (VADER)")
    print("=" * 80)

    sia = SentimentIntensityAnalyzer()

    sentences = [
        "NLTK is an amazing library for NLP!",
        "I really hate bugs in my code.",
        "The weather today is okay, nothing special.",
        "This is the best natural language processing tool ever!",
        "The documentation could be better, but it's not terrible.",
    ]

    print("Analyzing sentiment of sentences:\n")
    for sentence in sentences:
        scores = sia.polarity_scores(sentence)
        sentiment = (
            "positive"
            if scores["compound"] > 0.05
            else "negative"
            if scores["compound"] < -0.05
            else "neutral"
        )

        print(f"Sentence: {sentence}")
        print(
            f"  Scores: pos={scores['pos']:.3f}, neg={scores['neg']:.3f}, neu={scores['neu']:.3f}"
        )
        print(f"  Compound: {scores['compound']:.3f} -> {sentiment.upper()}")
        print()


def demonstrate_text_processing_pipeline():
    """Demonstrate a complete text processing pipeline"""
    print("=" * 80)
    print("10. COMPLETE TEXT PROCESSING PIPELINE")
    print("=" * 80)

    text = """
    The Natural Language Toolkit (NLTK) is a leading platform for building Python programs
    to work with human language data. It provides easy-to-use interfaces to over 50 corpora
    and lexical resources such as WordNet, along with a suite of text processing libraries.
    """

    print(f"Original text:\n{text}\n")

    # Step 1: Tokenization
    print("Step 1: Tokenization")
    words = word_tokenize(text.lower())
    print(f"  Tokens: {len(words)}")

    # Step 2: Remove stopwords and non-alphabetic tokens
    print("Step 2: Remove stopwords and clean")
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    print(f"  Cleaned tokens: {len(words)}")

    # Step 3: Lemmatization
    print("Step 3: Lemmatization")
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    print(f"  Lemmatized: {words[:10]}...")

    # Step 4: Frequency analysis
    print("Step 4: Frequency analysis")
    freq_dist = FreqDist(words)
    print("  Top 5 words:")
    for word, freq in freq_dist.most_common(5):
        print(f"    {word}: {freq}")
    print()


def main():
    """Main function to run all demonstrations"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "NLTK COMPREHENSIVE DEMONSTRATION" + " " * 26 + "║")
    print("╚" + "=" * 78 + "╝")
    print()

    # Download required data
    download_nltk_data()

    # Run all demonstrations
    demonstrate_tokenization()
    demonstrate_stopwords()
    demonstrate_stemming()
    demonstrate_lemmatization()
    demonstrate_pos_tagging()
    demonstrate_ner()
    demonstrate_frequency_distribution()
    demonstrate_collocations()
    demonstrate_sentiment_analysis()
    demonstrate_text_processing_pipeline()

    print("=" * 80)
    print("DEMONSTRATION COMPLETE")
    print("=" * 80)
    print("\nNLTK provides powerful tools for natural language processing!")
    print("Visit https://www.nltk.org/ for more information.")
    print()


if __name__ == "__main__":
    main()
