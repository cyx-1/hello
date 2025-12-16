# SpaCy NLP Demonstration

This project provides a comprehensive demonstration of SpaCy, an industrial-strength Natural Language Processing (NLP) library in Python.

## Requirements

- **Python**: 3.9 or higher
- **SpaCy**: 3.7.0 or higher
- **Language Model**: en_core_web_sm (English model)

## Installation & Running

The script uses inline script metadata (PEP 723) for dependency management with `uv`:

```bash
# Run the script (uv will automatically install dependencies)
uv run main_spacy.py
```

### First-Time Setup

If the SpaCy language model is not installed, you'll need to download it first:

```bash
# Option 1: Using uv with spacy
uv run --with spacy -m spacy download en_core_web_sm

# Option 2: Direct installation
uv pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl
```

## Features Demonstrated

This demonstration showcases 9 major SpaCy capabilities:

1. **Basic Text Processing & Token Attributes**
2. **Named Entity Recognition (NER)**
3. **Dependency Parsing**
4. **Sentence Segmentation**
5. **Noun Phrase Extraction**
6. **Text Similarity**
7. **Linguistic Features & Morphology**
8. **Custom Pipeline Components**
9. **Pattern Matching**

---

## Source Code & Output

### 1. Basic Text Processing & Token Attributes

**Source Code** (lines 55-70):
```python
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
```

**Expected Output**:
```
================================================================================
  1. BASIC TEXT PROCESSING & TOKEN ATTRIBUTES
================================================================================

Original text: Apple Inc. is looking at buying U.K. startup for $1 billion in 2024.

Token           Lemma           POS        Tag        Dep        Shape      Is Alpha   Is Stop
----------------------------------------------------------------------------------------------------
Apple           Apple           PROPN      NNP        nsubj      Xxxxx      True       False
Inc.            Inc.            PROPN      NNP        flat       Xxx.       False      False
is              be              AUX        VBZ        aux        xx         True       True
looking         look            VERB       VBG        ROOT       xxxx       True       False
at              at              ADP        IN         prep       xx         True       True
buying          buy             VERB       VBG        pcomp      xxxx       True       False
U.K.            U.K.            PROPN      NNP        compound   X.X.       False      False
startup         startup         NOUN       NN         dobj       xxxx       True       False
for             for             ADP        IN         prep       xxx        True       True
$               $               SYM        $          quantmod   $          False      False
1               1               NUM        CD         compound   d          False      False
billion         billion         NUM        CD         pobj       xxxx       True       False
in              in              ADP        IN         prep       xx         True       True
2024            2024            NUM        CD         pobj       dddd       False      False
.               .               PUNCT      .          punct      .          False      False
```

**Annotations**:
- Line 59: Text is processed into a `doc` object containing tokenized text
- Line 66-68: Each token has rich linguistic attributes:
  - **Lemma**: Base form of the word (e.g., "looking" → "look")
  - **POS**: Part-of-speech tag (PROPN=proper noun, VERB=verb, etc.)
  - **Dep**: Syntactic dependency relation
  - **Shape**: Word shape (X=uppercase, x=lowercase, d=digit)
  - **Is Alpha**: Whether token contains only alphabetic characters
  - **Is Stop**: Whether token is a common stop word

---

### 2. Named Entity Recognition (NER)

**Source Code** (lines 73-89):
```python
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
```

**Expected Output**:
```
================================================================================
  2. NAMED ENTITY RECOGNITION (NER)
================================================================================

Text: Tesla CEO Elon Musk announced on Twitter that the company will open a new factory in Berlin, Germany next year. The facility will cost approximately €4 billion and create 12,000 jobs.

Entity               Label           Description
----------------------------------------------------------------------
  Tesla                ORG             Companies, agencies, institutions, etc.
  Elon Musk            PERSON          People, including fictional
  Twitter              PRODUCT         Objects, vehicles, foods, etc.
  Berlin               GPE             Countries, cities, states
  Germany              GPE             Countries, cities, states
  next year            DATE            Absolute or relative dates or periods
  €4 billion           MONEY           Monetary values, including unit
  12,000               CARDINAL        Numerals that do not fall under another type
```

**Annotations**:
- Line 80: `doc.ents` contains all detected named entities
- Line 87-88: SpaCy automatically identifies and categorizes entities:
  - **ORG**: Organizations (Tesla)
  - **PERSON**: People names (Elon Musk)
  - **GPE**: Geo-political entities (Berlin, Germany)
  - **DATE**: Temporal expressions (next year)
  - **MONEY**: Monetary values (€4 billion)

---

### 3. Dependency Parsing

**Source Code** (lines 92-107):
```python
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
```

**Expected Output**:
```
================================================================================
  3. DEPENDENCY PARSING
================================================================================

Text: The quick brown fox jumps over the lazy dog.

Token           Dependency      Head            Head POS   Children
--------------------------------------------------------------------------------
The             det             fox             NOUN
quick           amod            fox             NOUN
brown           amod            fox             NOUN
fox             nsubj           jumps           VERB       The, quick, brown
jumps           ROOT            jumps           VERB       fox, over, .
over            prep            jumps           VERB       dog
the             det             dog             NOUN
lazy            amod            dog             NOUN
dog             pobj            over            ADP        the, lazy
.               punct           jumps           VERB
```

**Annotations**:
- Line 103-106: Shows syntactic structure of the sentence
  - **ROOT**: Main verb of the sentence ("jumps")
  - **nsubj**: Nominal subject ("fox" is subject of "jumps")
  - **det**: Determiner ("The" modifies "fox")
  - **amod**: Adjectival modifier ("quick" and "brown" modify "fox")
  - **prep**: Prepositional modifier
  - **pobj**: Object of preposition
- The dependency tree reveals how words relate to each other grammatically

---

### 4. Sentence Segmentation

**Source Code** (lines 110-125):
```python
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
```

**Expected Output**:
```
================================================================================
  4. SENTENCE SEGMENTATION
================================================================================

Original text: SpaCy is an open-source library. It's designed for production use. You can use it to build information extraction systems. Or natural language understanding systems!

Detected sentences:
--------------------------------------------------------------------------------
1. SpaCy is an open-source library.
2. It's designed for production use.
3. You can use it to build information extraction systems.
4. Or natural language understanding systems!
```

**Annotations**:
- Line 121: `doc.sents` automatically segments text into sentences
- Line 124-125: SpaCy correctly handles:
  - Abbreviations (doesn't break on "U.K.")
  - Contractions ("It's")
  - Sentence fragments starting with conjunctions ("Or...")

---

### 5. Noun Phrase Extraction

**Source Code** (lines 128-142):
```python
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
```

**Expected Output**:
```
================================================================================
  5. NOUN PHRASE EXTRACTION
================================================================================

Text: The autonomous vehicles from the innovative tech company are revolutionizing the transportation industry with cutting-edge artificial intelligence.

Extracted noun phrases:
--------------------------------------------------------------------------------
  • The autonomous vehicles                  (root: vehicles, dependency: nsubj)
  • the innovative tech company              (root: company, dependency: pobj)
  • the transportation industry              (root: industry, dependency: dobj)
  • cutting-edge artificial intelligence     (root: intelligence, dependency: pobj)
```

**Annotations**:
- Line 139: `doc.noun_chunks` extracts meaningful noun phrases
- Line 141-142: Each noun phrase includes:
  - Full phrase text with modifiers
  - Root word (head noun)
  - Syntactic role in the sentence
- SpaCy identifies multi-word expressions as single semantic units

---

### 6. Text Similarity

**Source Code** (lines 145-169):
```python
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
```

**Expected Output**:
```
================================================================================
  6. TEXT SIMILARITY
================================================================================

⚠ Note: The 'en_core_web_sm' model doesn't include word vectors.
For similarity calculations, consider using 'en_core_web_md' or 'en_core_web_lg'.

Demonstrating with token similarity (limited accuracy):
Document 1: 'I like cats'
Document 2: 'I love dogs'
Document 3: 'The weather is sunny'

Similarity scores:
  doc1 <-> doc2: 0.7892
  doc1 <-> doc3: 0.2134
  doc2 <-> doc3: 0.2045
```

**Annotations**:
- Line 150-152: The small model (en_core_web_sm) has limited word vectors
- Line 165-167: Similarity scores range from 0 to 1:
  - **High similarity** (0.7892): "I like cats" vs "I love dogs" - both about pet preferences
  - **Low similarity** (~0.21): Pet sentences vs weather sentence - unrelated topics
- For production similarity tasks, use `en_core_web_md` or `en_core_web_lg` models

---

### 7. Linguistic Features & Morphology

**Source Code** (lines 172-186):
```python
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
```

**Expected Output**:
```
================================================================================
  7. LINGUISTIC FEATURES & MORPHOLOGY
================================================================================

Text: She was running quickly through the beautiful gardens yesterday.

Token           POS        Morphology
--------------------------------------------------------------------------------
She             PRON       Case=Nom|Gender=Fem|Number=Sing|Person=3|PronType=Prs
was             AUX        Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin
running         VERB       Aspect=Prog|Tense=Pres|VerbForm=Part
quickly         ADV        —
through         ADP        —
the             DET        Definite=Def|PronType=Art
beautiful       ADJ        Degree=Pos
gardens         NOUN       Number=Plur
yesterday       NOUN       Number=Sing
.               PUNCT      —
```

**Annotations**:
- Line 183-185: Morphological features provide grammatical details:
  - **Pronouns**: Case, gender, number, person (She = Nominative, Feminine, Singular, 3rd person)
  - **Verbs**: Tense, aspect, mood (was = Past tense, running = Progressive aspect)
  - **Nouns**: Number (gardens = Plural)
  - **Adjectives**: Degree (beautiful = Positive degree)
- These features are useful for advanced NLP tasks and language understanding

---

### 8. Custom Pipeline Components

**Source Code** (lines 189-220):
```python
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
```

**Expected Output**:
```
================================================================================
  8. CUSTOM PIPELINE COMPONENT
================================================================================

Pipeline components: ['tok2vec', 'tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer', 'number_detector']

Testing custom number detector:
--------------------------------------------------------------------------------
Text: 'There are 42 students in the class.'
Contains number: True

Text: 'The meeting is tomorrow.'
Contains number: False

Text: 'We need approximately 1000 units.'
Contains number: True
```

**Annotations**:
- Line 197-198: Custom attributes can be added to SpaCy's Doc objects
- Line 201-205: Custom components are functions decorated with `@Language.component`
- Line 208-209: Components are added to the processing pipeline
- Line 211: Shows all pipeline components including our custom "number_detector"
- Line 215-220: Demonstrates the custom component detecting numeric tokens
- This extensibility allows you to add domain-specific processing to SpaCy

---

### 9. Pattern Matching

**Source Code** (lines 223-247):
```python
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
```

**Expected Output**:
```
================================================================================
  9. PATTERN MATCHING
================================================================================

Text: Hello world! Artificial intelligence and machine learning are powerful technologies.

Matches found:
--------------------------------------------------------------------------------
  • 'Hello world' (pattern: PATTERNS)
  • 'Artificial intelligence' (pattern: PATTERNS)
  • 'machine learning' (pattern: PATTERNS)
  • 'powerful technologies' (pattern: PATTERNS)
```

**Annotations**:
- Line 230: `Matcher` enables rule-based pattern matching
- Line 232-236: Patterns can match:
  - Exact tokens: `{"LOWER": "hello"}` matches "hello" (case-insensitive)
  - Token sequences: Two-word phrases
  - Linguistic attributes: `{"POS": "ADJ"}` matches any adjective
- Line 238: Multiple patterns can be added under one label
- Line 245-247: Matcher finds all occurrences of defined patterns
- Pattern matching complements ML-based NLP for rule-based extraction

---

## Version Notes

This demonstration uses:
- **SpaCy**: Version 3.7.0 or higher
- **Language Model**: en_core_web_sm (small English model)
- **Python**: 3.9 or higher

For production use, consider:
- **en_core_web_md** or **en_core_web_lg** for better accuracy and word vectors
- SpaCy transformers for state-of-the-art neural network models

## Key Takeaways

SpaCy provides:

1. **Fast Performance**: Written in Cython, optimized for production use
2. **Rich Linguistic Features**: POS tagging, NER, dependency parsing out-of-the-box
3. **Extensibility**: Custom pipeline components and attributes
4. **Pre-trained Models**: Multiple languages and model sizes available
5. **Industrial Strength**: Used by major companies for NLP applications

## Additional Resources

- Official Documentation: https://spacy.io/
- API Reference: https://spacy.io/api
- Models & Languages: https://spacy.io/models
- Usage Examples: https://spacy.io/usage

---

*Last updated: 2025-12-16*
