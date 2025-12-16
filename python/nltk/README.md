# NLTK (Natural Language Toolkit) Demonstration

This example demonstrates comprehensive Natural Language Processing (NLP) capabilities using NLTK, a leading platform for building Python programs to work with human language data.

## Running the Program

```bash
uv run --script main_nltk.py
```

## Features Demonstrated

1. **Tokenization** - Breaking text into sentences and words
2. **Stopwords Removal** - Filtering common words
3. **Stemming** - Reducing words to root form
4. **Lemmatization** - Finding dictionary form of words
5. **POS Tagging** - Part-of-speech identification
6. **Named Entity Recognition** - Identifying people, places, organizations
7. **Frequency Distribution** - Analyzing word occurrence
8. **Collocations** - Finding frequently co-occurring words
9. **Sentiment Analysis** - Determining text sentiment
10. **Complete Pipeline** - End-to-end text processing

## Source Code and Output Analysis

### 1. Tokenization (Lines 60-82)

**Source Code:**
```python
60:  def demonstrate_tokenization():
61:      """Demonstrate word and sentence tokenization"""
62:      print("=" * 80)
63:      print("1. TOKENIZATION")
64:      print("=" * 80)
65:
66:      text = "NLTK is amazing! It's a powerful library for natural language processing. Let's explore it."
67:      print(f"Original text:\n{text}\n")
68:
69:      # Sentence tokenization
70:      sentences = sent_tokenize(text)
71:      print("Sentence Tokenization:")
72:      for i, sentence in enumerate(sentences, 1):
73:          print(f"  Sentence {i}: {sentence}")
74:      print()
75:
76:      # Word tokenization
77:      words = word_tokenize(text)
78:      print(f"Word Tokenization:\n  {words}")
79:      print(f"  Total words: {len(words)}")
80:      print()
```

**Output:**
```
================================================================================
1. TOKENIZATION
================================================================================
Original text:
NLTK is amazing! It's a powerful library for natural language processing. Let's explore it.

Sentence Tokenization:
  Sentence 1: NLTK is amazing!
  Sentence 2: It's a powerful library for natural language processing.
  Sentence 3: Let's explore it.

Word Tokenization:
  ['NLTK', 'is', 'amazing', '!', 'It', "'s", 'a', 'powerful', 'library', 'for', 'natural', 'language', 'processing', '.', 'Let', "'s", 'explore', 'it', '.']
  Total words: 19
```

**Analysis:**
- Line 70: `sent_tokenize()` splits text into 3 sentences at punctuation boundaries
- Line 77: `word_tokenize()` creates 19 tokens including punctuation marks
- Note how contractions like "It's" and "Let's" are split into separate tokens

### 2. Stopwords Removal (Lines 84-103)

**Source Code:**
```python
84:  def demonstrate_stopwords():
85:      """Demonstrate stopwords removal"""
86:      print("=" * 80)
87:      print("2. STOPWORDS REMOVAL")
88:      print("=" * 80)
89:
90:      text = "This is an example sentence demonstrating the removal of stopwords from text."
91:      words = word_tokenize(text.lower())
92:      print(f"Original words:\n  {words}\n")
93:
94:      stop_words = set(stopwords.words('english'))
95:      print(f"Number of English stopwords: {len(stop_words)}")
96:      print(f"Sample stopwords: {list(stop_words)[:10]}\n")
97:
98:      filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
99:      print(f"Filtered words (without stopwords):\n  {filtered_words}")
100:     print()
```

**Output:**
```
================================================================================
2. STOPWORDS REMOVAL
================================================================================
Original words:
  ['this', 'is', 'an', 'example', 'sentence', 'demonstrating', 'the', 'removal', 'of', 'stopwords', 'from', 'text', '.']

Number of English stopwords: 198
Sample stopwords: ['nor', 'between', 'didn', 'same', 'down', 'further', 'his', 'each', 'does', 'are']

Filtered words (without stopwords):
  ['example', 'sentence', 'demonstrating', 'removal', 'stopwords', 'text']
```

**Analysis:**
- Line 94: NLTK provides 198 common English stopwords
- Line 98: Filtering removes words like "this", "is", "an", "the", "of", "from"
- Result: 13 tokens reduced to 6 meaningful words (54% reduction)

### 3. Stemming - Porter Stemmer (Lines 105-121)

**Source Code:**
```python
105: def demonstrate_stemming():
106:     """Demonstrate stemming with Porter Stemmer"""
107:     print("=" * 80)
108:     print("3. STEMMING (Porter Stemmer)")
109:     print("=" * 80)
110:
111:     stemmer = PorterStemmer()
112:     words = ["running", "runs", "ran", "runner", "easily", "fairly", "connection", "connected", "connecting"]
113:
114:     print("Stemming reduces words to their root form:\n")
115:     for word in words:
116:         stemmed = stemmer.stem(word)
117:         print(f"  {word:15} -> {stemmed}")
118:     print()
```

**Output:**
```
================================================================================
3. STEMMING (Porter Stemmer)
================================================================================
Stemming reduces words to their root form:

  running         -> run
  runs            -> run
  ran             -> ran
  runner          -> runner
  easily          -> easili
  fairly          -> fairli
  connection      -> connect
  connected       -> connect
  connecting      -> connect
```

**Analysis:**
- Line 116: Porter Stemmer uses algorithmic rules, not a dictionary
- "running", "runs" → "run" (correct)
- "ran" → "ran" (unchanged, doesn't recognize irregular verb)
- "easily" → "easili" (crude but consistent result)
- Stemming is fast but less accurate than lemmatization

### 4. Lemmatization (Lines 123-143)

**Source Code:**
```python
123: def demonstrate_lemmatization():
124:     """Demonstrate lemmatization"""
125:     print("=" * 80)
126:     print("4. LEMMATIZATION")
127:     print("=" * 80)
128:
129:     lemmatizer = WordNetLemmatizer()
130:     words = [
131:         ("running", "v"), ("runs", "v"), ("ran", "v"),
132:         ("better", "a"), ("good", "a"),
133:         ("cacti", "n"), ("geese", "n"), ("feet", "n")
134:     ]
135:
136:     print("Lemmatization finds the dictionary form of words:\n")
137:     for word, pos in words:
138:         lemma = lemmatizer.lemmatize(word, pos=pos)
139:         print(f"  {word:15} ({pos}) -> {lemma}")
140:     print()
```

**Output:**
```
================================================================================
4. LEMMATIZATION
================================================================================
Lemmatization finds the dictionary form of words:

  running         (v) -> run
  runs            (v) -> run
  ran             (v) -> run
  better          (a) -> good
  good            (a) -> good
  cacti           (n) -> cactus
  geese           (n) -> goose
  feet            (n) -> foot
```

**Analysis:**
- Line 129: Uses WordNet dictionary for morphological analysis
- Line 138: Requires POS tag (v=verb, a=adjective, n=noun) for accuracy
- "ran" → "run" (correctly handles irregular verb, unlike stemming)
- "better" → "good" (understands comparative forms)
- "cacti" → "cactus", "geese" → "goose", "feet" → "foot" (handles irregular plurals)

### 5. Part-of-Speech (POS) Tagging (Lines 145-166)

**Source Code:**
```python
145: def demonstrate_pos_tagging():
146:     """Demonstrate Part-of-Speech tagging"""
147:     print("=" * 80)
148:     print("5. PART-OF-SPEECH (POS) TAGGING")
149:     print("=" * 80)
150:
151:     sentence = "The quick brown fox jumps over the lazy dog"
152:     words = word_tokenize(sentence)
153:     pos_tags = pos_tag(words)
154:
155:     print(f"Sentence: {sentence}\n")
156:     print("POS Tags:")
157:     for word, tag in pos_tags:
158:         print(f"  {word:10} -> {tag:5} ({get_pos_description(tag)})")
159:     print()
```

**Output:**
```
================================================================================
5. PART-OF-SPEECH (POS) TAGGING
================================================================================
Sentence: The quick brown fox jumps over the lazy dog

POS Tags:
  The        -> DT    (Determiner)
  quick      -> JJ    (Adjective)
  brown      -> NN    (Noun)
  fox        -> NN    (Noun)
  jumps      -> VBZ   (Verb 3rd person)
  over       -> IN    (Preposition)
  the        -> DT    (Determiner)
  lazy       -> JJ    (Adjective)
  dog        -> NN    (Noun)
```

**Analysis:**
- Line 153: `pos_tag()` uses a pre-trained model to identify grammatical roles
- "quick" and "lazy" correctly identified as adjectives (JJ)
- "jumps" identified as VBZ (3rd person singular present verb)
- Note: "brown" tagged as NN (noun) rather than JJ - can happen with ambiguous words
- POS tags use Penn Treebank tagset

### 6. Named Entity Recognition (Lines 168-188)

**Source Code:**
```python
168: def demonstrate_ner():
169:     """Demonstrate Named Entity Recognition"""
170:     print("=" * 80)
171:     print("6. NAMED ENTITY RECOGNITION (NER)")
172:     print("=" * 80)
173:
174:     sentence = "Apple Inc. was founded by Steve Jobs in Cupertino, California in 1976."
175:     words = word_tokenize(sentence)
176:     pos_tags = pos_tag(words)
177:     named_entities = ne_chunk(pos_tags)
178:
179:     print(f"Sentence: {sentence}\n")
180:     print("Named Entities:")
181:     for entity in named_entities:
182:         if hasattr(entity, 'label'):
183:             entity_text = ' '.join(word for word, tag in entity)
184:             print(f"  {entity_text:20} -> {entity.label()}")
185:     print()
```

**Output:**
```
================================================================================
6. NAMED ENTITY RECOGNITION (NER)
================================================================================
Sentence: Apple Inc. was founded by Steve Jobs in Cupertino, California in 1976.

Named Entities:
  Apple                -> PERSON
  Inc.                 -> ORGANIZATION
  Steve Jobs           -> PERSON
  Cupertino            -> GPE
  California           -> GPE
```

**Analysis:**
- Line 177: `ne_chunk()` identifies and classifies named entities
- GPE = Geopolitical Entity (cities, countries)
- "Apple" incorrectly tagged as PERSON (context-dependent challenge)
- "Inc." correctly identified as ORGANIZATION
- "Steve Jobs" correctly identified as PERSON
- Geographic entities "Cupertino" and "California" tagged as GPE

### 7. Frequency Distribution (Lines 190-211)

**Source Code:**
```python
190: def demonstrate_frequency_distribution():
191:     """Demonstrate frequency distribution"""
192:     print("=" * 80)
193:     print("7. FREQUENCY DISTRIBUTION")
194:     print("=" * 80)
195:
196:     text = """
197:     Natural language processing with NLTK is powerful. NLTK provides tools for processing.
198:     Processing text with NLTK enables many applications. Natural language is complex.
199:     """
200:
201:     words = word_tokenize(text.lower())
202:     words = [word for word in words if word.isalnum()]
203:
204:     freq_dist = FreqDist(words)
205:
206:     print("Top 10 most common words:")
207:     for word, frequency in freq_dist.most_common(10):
208:         print(f"  {word:15} -> {frequency} occurrences")
209:     print()
```

**Output:**
```
================================================================================
7. FREQUENCY DISTRIBUTION
================================================================================
Top 10 most common words:
  processing      -> 3 occurrences
  nltk            -> 3 occurrences
  natural         -> 2 occurrences
  language        -> 2 occurrences
  with            -> 2 occurrences
  is              -> 2 occurrences
  powerful        -> 1 occurrences
  provides        -> 1 occurrences
  tools           -> 1 occurrences
  for             -> 1 occurrences
```

**Analysis:**
- Line 204: `FreqDist()` creates a frequency distribution of tokens
- "processing" and "nltk" are most common (3 occurrences each)
- Line 207: `most_common(10)` returns top 10 words sorted by frequency
- Useful for identifying key topics and themes in text

### 8. Collocations (Lines 213-237)

**Source Code:**
```python
213: def demonstrate_collocations():
214:     """Demonstrate bigram collocations"""
215:     print("=" * 80)
216:     print("8. COLLOCATIONS (Bigrams)")
217:     print("=" * 80)
218:
219:     text = """
220:     Machine learning and artificial intelligence are transforming natural language processing.
221:     Deep learning models like neural networks enable better natural language understanding.
222:     Natural language processing applications include machine translation and text analysis.
223:     """
224:
225:     words = word_tokenize(text.lower())
226:     words = [word for word in words if word.isalnum()]
227:
228:     bigram_measures = BigramAssocMeasures()
229:     finder = BigramCollocationFinder.from_words(words)
230:     finder.apply_freq_filter(2)  # Only bigrams that appear at least 2 times
231:
232:     print("Top collocations (word pairs that frequently occur together):")
233:     for bigram, score in finder.score_ngrams(bigram_measures.raw_freq)[:10]:
234:         print(f"  {bigram[0]} {bigram[1]:20} -> score: {score:.4f}")
235:     print()
```

**Output:**
```
================================================================================
8. COLLOCATIONS (Bigrams)
================================================================================
Top collocations (word pairs that frequently occur together):
  natural language             -> score: 0.0968
  language processing           -> score: 0.0645
```

**Analysis:**
- Line 229: `BigramCollocationFinder` identifies frequently co-occurring word pairs
- Line 230: Filter requires bigrams to appear at least 2 times
- "natural language" appears 3 times in the text (highest score: 0.0968)
- "language processing" appears 2 times (score: 0.0645)
- Collocations help identify multi-word phrases and terminology

### 9. Sentiment Analysis (Lines 239-266)

**Source Code:**
```python
239: def demonstrate_sentiment_analysis():
240:     """Demonstrate sentiment analysis using VADER"""
241:     print("=" * 80)
242:     print("9. SENTIMENT ANALYSIS (VADER)")
243:     print("=" * 80)
244:
245:     sia = SentimentIntensityAnalyzer()
246:
247:     sentences = [
248:         "NLTK is an amazing library for NLP!",
249:         "I really hate bugs in my code.",
250:         "The weather today is okay, nothing special.",
251:         "This is the best natural language processing tool ever!",
252:         "The documentation could be better, but it's not terrible."
253:     ]
254:
255:     print("Analyzing sentiment of sentences:\n")
256:     for sentence in sentences:
257:         scores = sia.polarity_scores(sentence)
258:         sentiment = "positive" if scores['compound'] > 0.05 else "negative" if scores['compound'] < -0.05 else "neutral"
259:
260:         print(f"Sentence: {sentence}")
261:         print(f"  Scores: pos={scores['pos']:.3f}, neg={scores['neg']:.3f}, neu={scores['neu']:.3f}")
262:         print(f"  Compound: {scores['compound']:.3f} -> {sentiment.upper()}")
263:         print()
```

**Output:**
```
================================================================================
9. SENTIMENT ANALYSIS (VADER)
================================================================================
Analyzing sentiment of sentences:

Sentence: NLTK is an amazing library for NLP!
  Scores: pos=0.405, neg=0.000, neu=0.595
  Compound: 0.624 -> POSITIVE

Sentence: I really hate bugs in my code.
  Scores: pos=0.000, neg=0.444, neu=0.556
  Compound: -0.612 -> NEGATIVE

Sentence: The weather today is okay, nothing special.
  Scores: pos=0.207, neg=0.247, neu=0.546
  Compound: -0.092 -> NEGATIVE

Sentence: This is the best natural language processing tool ever!
  Scores: pos=0.500, neg=0.000, neu=0.500
  Compound: 0.790 -> POSITIVE

Sentence: The documentation could be better, but it's not terrible.
  Scores: pos=0.430, neg=0.000, neu=0.570
  Compound: 0.646 -> POSITIVE
```

**Analysis:**
- Line 245: VADER (Valence Aware Dictionary and sEntiment Reasoner) designed for social media text
- Line 257: Returns pos/neg/neu scores and compound score (-1 to +1)
- "amazing" → compound: 0.624 (POSITIVE)
- "hate" → compound: -0.612 (NEGATIVE)
- "okay, nothing special" → compound: -0.092 (slightly NEGATIVE)
- "best...ever!" → compound: 0.790 (strongly POSITIVE)
- Line 258: Compound > 0.05 = positive, < -0.05 = negative, else neutral

### 10. Complete Text Processing Pipeline (Lines 268-304)

**Source Code:**
```python
268: def demonstrate_text_processing_pipeline():
269:     """Demonstrate a complete text processing pipeline"""
270:     print("=" * 80)
271:     print("10. COMPLETE TEXT PROCESSING PIPELINE")
272:     print("=" * 80)
273:
274:     text = """
275:     The Natural Language Toolkit (NLTK) is a leading platform for building Python programs
276:     to work with human language data. It provides easy-to-use interfaces to over 50 corpora
277:     and lexical resources such as WordNet, along with a suite of text processing libraries.
278:     """
279:
280:     print(f"Original text:\n{text}\n")
281:
282:     # Step 1: Tokenization
283:     print("Step 1: Tokenization")
284:     words = word_tokenize(text.lower())
285:     print(f"  Tokens: {len(words)}")
286:
287:     # Step 2: Remove stopwords and non-alphabetic tokens
288:     print("Step 2: Remove stopwords and clean")
289:     stop_words = set(stopwords.words('english'))
290:     words = [word for word in words if word.isalnum() and word not in stop_words]
291:     print(f"  Cleaned tokens: {len(words)}")
292:
293:     # Step 3: Lemmatization
294:     print("Step 3: Lemmatization")
295:     lemmatizer = WordNetLemmatizer()
296:     words = [lemmatizer.lemmatize(word) for word in words]
297:     print(f"  Lemmatized: {words[:10]}...")
298:
299:     # Step 4: Frequency analysis
300:     print("Step 4: Frequency analysis")
301:     freq_dist = FreqDist(words)
302:     print("  Top 5 words:")
303:     for word, freq in freq_dist.most_common(5):
304:         print(f"    {word}: {freq}")
305:     print()
```

**Output:**
```
================================================================================
10. COMPLETE TEXT PROCESSING PIPELINE
================================================================================
Original text:

    The Natural Language Toolkit (NLTK) is a leading platform for building Python programs
    to work with human language data. It provides easy-to-use interfaces to over 50 corpora
    and lexical resources such as WordNet, along with a suite of text processing libraries.


Step 1: Tokenization
  Tokens: 46
Step 2: Remove stopwords and clean
  Cleaned tokens: 25
Step 3: Lemmatization
  Lemmatized: ['natural', 'language', 'toolkit', 'nltk', 'leading', 'platform', 'building', 'python', 'program', 'work']...
Step 4: Frequency analysis
  Top 5 words:
    language: 2
    natural: 1
    toolkit: 1
    nltk: 1
    leading: 1
```

**Analysis:**
- **Step 1** (Line 284): 46 tokens from original text
- **Step 2** (Lines 289-290): Remove stopwords → 25 tokens (46% reduction)
- **Step 3** (Line 296): Lemmatization normalizes word forms
- **Step 4** (Lines 301-304): "language" appears twice, most frequent term
- This pipeline demonstrates a typical NLP preprocessing workflow

## Version Requirements

- **Python**: 3.10 or higher
- **NLTK**: 3.9.1 or higher
- **NumPy**: 1.24.0 or higher (required for NER functionality)

## Dependencies

All dependencies are specified in the inline script metadata and automatically managed by `uv`:

```python
# dependencies = [
#     "nltk>=3.9.1",
#     "numpy>=1.24.0",
# ]
```

## NLTK Data Downloads

The script automatically downloads required NLTK data packages on first run:
- `punkt` - Sentence tokenizer
- `punkt_tab` - Punkt tokenizer tables
- `stopwords` - Common stopwords for multiple languages
- `wordnet` - Lexical database for lemmatization
- `averaged_perceptron_tagger` - POS tagger
- `averaged_perceptron_tagger_eng` - English POS tagger
- `maxent_ne_chunker` - Named entity chunker
- `maxent_ne_chunker_tab` - Named entity chunker tables
- `words` - Word list corpus
- `vader_lexicon` - Sentiment analysis lexicon

## Key Takeaways

1. **Tokenization** is the foundation - breaking text into processable units
2. **Stopwords removal** reduces noise and focuses on meaningful content
3. **Stemming** is fast but crude; **Lemmatization** is slower but more accurate
4. **POS tagging** enables understanding of grammatical structure
5. **NER** extracts structured information (names, places, organizations)
6. **Frequency analysis** identifies important terms and topics
7. **Collocations** find meaningful multi-word expressions
8. **Sentiment analysis** determines emotional tone
9. **Pipelines** combine multiple techniques for comprehensive text analysis

## Additional Resources

- Official NLTK Documentation: https://www.nltk.org/
- NLTK Book (free online): https://www.nltk.org/book/
- Penn Treebank POS Tags: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
