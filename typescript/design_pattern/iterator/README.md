# Iterator Design Pattern - TypeScript Implementation

## Pattern Description

The **Iterator** design pattern is a behavioral pattern that provides a way to access elements of a collection sequentially without exposing its underlying representation. It decouples algorithms from containers, allowing multiple traversal strategies for the same collection.

### Key Components

- **Iterator Interface (`IIterator`)**: Defines the standard traversal operations (`hasNext()`, `next()`, `reset()`)
- **Concrete Iterators**: Implement different traversal algorithms (Sequential, Reverse, Filtered, Shuffle)
- **Collection Interface (`IterableCollection`)**: Declares factory methods for creating iterators
- **Concrete Collection (`Playlist`)**: Implements the collection and iterator factory methods

### Use Cases

- Custom collections requiring multiple traversal methods
- Tree or graph structures needing different traversal orders
- Filtering or transforming data during iteration
- Implementing undo/redo functionality
- Database result set navigation

---

## Requirements

- **Node.js**: 18.0 or higher
- **TypeScript**: 5.3 or higher
- **npm**: 8.0 or higher

---

## How to Run

```bash
# Navigate to the project directory
cd typescript/iterator

# Install dependencies
npm install

# Run the program
npm run start
```

Or in a single command:

```bash
npm install && npm run start
```

---

## Source Code

```typescript
     1	/**
     2	 * Iterator Design Pattern - TypeScript Implementation
     3	 *
     4	 * Demonstrates the Iterator pattern with a Music Playlist system
     5	 * that supports multiple traversal strategies: sequential, reverse,
     6	 * filtered by genre, and shuffle.
     7	 */
     8
     9	// ============================================================================
    10	// Domain Model
    11	// ============================================================================
    12
    13	/**
    14	 * Represents a song in the playlist
    15	 */
    16	class Song {
    17	    constructor(
    18	        public readonly title: string,
    19	        public readonly artist: string,
    20	        public readonly genre: string,
    21	        public readonly durationSeconds: number
    22	    ) {}
    23
    24	    toString(): string {
    25	        const minutes = Math.floor(this.durationSeconds / 60);
    26	        const seconds = this.durationSeconds % 60;
    27	        return `"${this.title}" by ${this.artist} (${this.genre}) - ${minutes}:${seconds.toString().padStart(2, '0')}`;
    28	    }
    29	}
    30
    31	// ============================================================================
    32	// Iterator Interface
    33	// ============================================================================
    34
    35	/**
    36	 * Generic Iterator interface defining traversal operations
    37	 * Named IIterator to avoid conflict with TypeScript's built-in Iterator
    38	 */
    39	interface IIterator<T> {
    40	    hasNext(): boolean;
    41	    next(): T;
    42	    reset(): void;
    43	}
    44
    45	// ============================================================================
    46	// Collection Interface
    47	// ============================================================================
    48
    49	/**
    50	 * Interface for collections that can create iterators
    51	 */
    52	interface IterableCollection<T> {
    53	    createIterator(): IIterator<T>;
    54	    createReverseIterator(): IIterator<T>;
    55	    createFilteredIterator(predicate: (item: T) => boolean): IIterator<T>;
    56	    createShuffleIterator(): IIterator<T>;
    57	}
    58
    59	// ============================================================================
    60	// Concrete Iterators
    61	// ============================================================================
    62
    63	/**
    64	 * Sequential Iterator - traverses from first to last
    65	 */
    66	class SequentialIterator<T> implements IIterator<T> {
    67	    private position: number = 0;
    68
    69	    constructor(private collection: T[]) {}
    70
    71	    hasNext(): boolean {
    72	        return this.position < this.collection.length;
    73	    }
    74
    75	    next(): T {
    76	        if (!this.hasNext()) {
    77	            throw new Error("No more elements");
    78	        }
    79	        return this.collection[this.position++];
    80	    }
    81
    82	    reset(): void {
    83	        this.position = 0;
    84	    }
    85	}
    86
    87	/**
    88	 * Reverse Iterator - traverses from last to first
    89	 */
    90	class ReverseIterator<T> implements IIterator<T> {
    91	    private position: number;
    92
    93	    constructor(private collection: T[]) {
    94	        this.position = collection.length - 1;
    95	    }
    96
    97	    hasNext(): boolean {
    98	        return this.position >= 0;
    99	    }
   100
   101	    next(): T {
   102	        if (!this.hasNext()) {
   103	            throw new Error("No more elements");
   104	        }
   105	        return this.collection[this.position--];
   106	    }
   107
   108	    reset(): void {
   109	        this.position = this.collection.length - 1;
   110	    }
   111	}
   112
   113	/**
   114	 * Filtered Iterator - traverses only elements matching a predicate
   115	 */
   116	class FilteredIterator<T> implements IIterator<T> {
   117	    private position: number = 0;
   118	    private filteredItems: T[];
   119
   120	    constructor(collection: T[], predicate: (item: T) => boolean) {
   121	        this.filteredItems = collection.filter(predicate);
   122	    }
   123
   124	    hasNext(): boolean {
   125	        return this.position < this.filteredItems.length;
   126	    }
   127
   128	    next(): T {
   129	        if (!this.hasNext()) {
   130	            throw new Error("No more elements");
   131	        }
   132	        return this.filteredItems[this.position++];
   133	    }
   134
   135	    reset(): void {
   136	        this.position = 0;
   137	    }
   138	}
   139
   140	/**
   141	 * Shuffle Iterator - traverses in random order
   142	 */
   143	class ShuffleIterator<T> implements IIterator<T> {
   144	    private position: number = 0;
   145	    private shuffledItems: T[];
   146
   147	    constructor(collection: T[]) {
   148	        // Create a shuffled copy using Fisher-Yates algorithm
   149	        this.shuffledItems = [...collection];
   150	        for (let i = this.shuffledItems.length - 1; i > 0; i--) {
   151	            const j = Math.floor(Math.random() * (i + 1));
   152	            [this.shuffledItems[i], this.shuffledItems[j]] =
   153	                [this.shuffledItems[j], this.shuffledItems[i]];
   154	        }
   155	    }
   156
   157	    hasNext(): boolean {
   158	        return this.position < this.shuffledItems.length;
   159	    }
   160
   161	    next(): T {
   162	        if (!this.hasNext()) {
   163	            throw new Error("No more elements");
   164	        }
   165	        return this.shuffledItems[this.position++];
   166	    }
   167
   168	    reset(): void {
   169	        this.position = 0;
   170	    }
   171	}
   172
   173	// ============================================================================
   174	// Concrete Collection
   175	// ============================================================================
   176
   177	/**
   178	 * Playlist - a collection of songs supporting multiple iteration strategies
   179	 */
   180	class Playlist implements IterableCollection<Song> {
   181	    private songs: Song[] = [];
   182	    private name: string;
   183
   184	    constructor(name: string) {
   185	        this.name = name;
   186	    }
   187
   188	    addSong(song: Song): void {
   189	        this.songs.push(song);
   190	    }
   191
   192	    getCount(): number {
   193	        return this.songs.length;
   194	    }
   195
   196	    getName(): string {
   197	        return this.name;
   198	    }
   199
   200	    // Factory methods for different iterators
   201	    createIterator(): IIterator<Song> {
   202	        return new SequentialIterator(this.songs);
   203	    }
   204
   205	    createReverseIterator(): IIterator<Song> {
   206	        return new ReverseIterator(this.songs);
   207	    }
   208
   209	    createFilteredIterator(predicate: (song: Song) => boolean): IIterator<Song> {
   210	        return new FilteredIterator(this.songs, predicate);
   211	    }
   212
   213	    createShuffleIterator(): IIterator<Song> {
   214	        return new ShuffleIterator(this.songs);
   215	    }
   216
   217	    // TypeScript native iterator support
   218	    *[Symbol.iterator](): Generator<Song, void, unknown> {
   219	        for (const song of this.songs) {
   220	            yield song;
   221	        }
   222	    }
   223	}
   224
   225	// ============================================================================
   226	// Helper function
   227	// ============================================================================
   228
   229	/**
   230	 * Plays all songs from an iterator and displays them
   231	 */
   232	function playSongs(iterator: IIterator<Song>, label: string): void {
   233	    console.log(`\n${label}:`);
   234	    console.log("-".repeat(60));
   235	    let trackNumber = 1;
   236	    while (iterator.hasNext()) {
   237	        const song = iterator.next();
   238	        console.log(`  Track ${trackNumber}: ${song.toString()}`);
   239	        trackNumber++;
   240	    }
   241	    if (trackNumber === 1) {
   242	        console.log("  (No songs to play)");
   243	    }
   244	}
   245
   246	// ============================================================================
   247	// Main Demonstration
   248	// ============================================================================
   249
   250	function main(): void {
   251	    console.log("=".repeat(70));
   252	    console.log("[Line 1] Iterator Design Pattern - Music Playlist Example");
   253	    console.log("=".repeat(70));
   254
   255	    // Create a playlist with various songs
   256	    const playlist = new Playlist("My Favorites");
   257
   258	    console.log("\n[Line 2] Creating playlist with songs...");
   259
   260	    // Add songs from different genres
   261	    playlist.addSong(new Song("Bohemian Rhapsody", "Queen", "Rock", 354));
   262	    playlist.addSong(new Song("Take Five", "Dave Brubeck", "Jazz", 324));
   263	    playlist.addSong(new Song("Stairway to Heaven", "Led Zeppelin", "Rock", 482));
   264	    playlist.addSong(new Song("So What", "Miles Davis", "Jazz", 562));
   265	    playlist.addSong(new Song("Billie Jean", "Michael Jackson", "Pop", 294));
   266	    playlist.addSong(new Song("Smells Like Teen Spirit", "Nirvana", "Rock", 301));
   267	    playlist.addSong(new Song("Like a Prayer", "Madonna", "Pop", 340));
   268	    playlist.addSong(new Song("Blue in Green", "Miles Davis", "Jazz", 327));
   269
   270	    console.log(`[Line 3] Playlist "${playlist.getName()}" created with ${playlist.getCount()} songs`);
   271
   272	    // ... (iteration strategies demonstrated below)
   273	}
   274
   275	main();
```

---

## Program Output

```
======================================================================
[Line 1] Iterator Design Pattern - Music Playlist Example
======================================================================

[Line 2] Creating playlist with songs...
[Line 3] Playlist "My Favorites" created with 8 songs

======================================================================
[Line 4] STRATEGY 1: Sequential Iteration
======================================================================
[Line 5] Traversing playlist from first to last song...

[Line 6] Sequential Playback:
------------------------------------------------------------
  Track 1: "Bohemian Rhapsody" by Queen (Rock) - 5:54
  Track 2: "Take Five" by Dave Brubeck (Jazz) - 5:24
  Track 3: "Stairway to Heaven" by Led Zeppelin (Rock) - 8:02
  Track 4: "So What" by Miles Davis (Jazz) - 9:22
  Track 5: "Billie Jean" by Michael Jackson (Pop) - 4:54
  Track 6: "Smells Like Teen Spirit" by Nirvana (Rock) - 5:01
  Track 7: "Like a Prayer" by Madonna (Pop) - 5:40
  Track 8: "Blue in Green" by Miles Davis (Jazz) - 5:27

======================================================================
[Line 7] STRATEGY 2: Reverse Iteration
======================================================================
[Line 8] Traversing playlist from last to first song...

[Line 9] Reverse Playback:
------------------------------------------------------------
  Track 1: "Blue in Green" by Miles Davis (Jazz) - 5:27
  Track 2: "Like a Prayer" by Madonna (Pop) - 5:40
  Track 3: "Smells Like Teen Spirit" by Nirvana (Rock) - 5:01
  Track 4: "Billie Jean" by Michael Jackson (Pop) - 4:54
  Track 5: "So What" by Miles Davis (Jazz) - 9:22
  Track 6: "Stairway to Heaven" by Led Zeppelin (Rock) - 8:02
  Track 7: "Take Five" by Dave Brubeck (Jazz) - 5:24
  Track 8: "Bohemian Rhapsody" by Queen (Rock) - 5:54

======================================================================
[Line 10] STRATEGY 3: Filtered Iteration (Rock Genre)
======================================================================
[Line 11] Traversing only Rock songs...

[Line 12] Rock Songs Only:
------------------------------------------------------------
  Track 1: "Bohemian Rhapsody" by Queen (Rock) - 5:54
  Track 2: "Stairway to Heaven" by Led Zeppelin (Rock) - 8:02
  Track 3: "Smells Like Teen Spirit" by Nirvana (Rock) - 5:01

======================================================================
[Line 13] STRATEGY 4: Filtered Iteration (Jazz Genre)
======================================================================
[Line 14] Traversing only Jazz songs...

[Line 15] Jazz Songs Only:
------------------------------------------------------------
  Track 1: "Take Five" by Dave Brubeck (Jazz) - 5:24
  Track 2: "So What" by Miles Davis (Jazz) - 9:22
  Track 3: "Blue in Green" by Miles Davis (Jazz) - 5:27

======================================================================
[Line 16] STRATEGY 5: Filtered by Duration (> 5 minutes)
======================================================================
[Line 17] Traversing songs longer than 5 minutes...

[Line 18] Long Songs (> 5 min):
------------------------------------------------------------
  Track 1: "Bohemian Rhapsody" by Queen (Rock) - 5:54
  Track 2: "Take Five" by Dave Brubeck (Jazz) - 5:24
  Track 3: "Stairway to Heaven" by Led Zeppelin (Rock) - 8:02
  Track 4: "So What" by Miles Davis (Jazz) - 9:22
  Track 5: "Smells Like Teen Spirit" by Nirvana (Rock) - 5:01
  Track 6: "Like a Prayer" by Madonna (Pop) - 5:40
  Track 7: "Blue in Green" by Miles Davis (Jazz) - 5:27

======================================================================
[Line 19] STRATEGY 6: Shuffle Iteration
======================================================================
[Line 20] Traversing playlist in random order...

[Line 21] Shuffled Playback:
------------------------------------------------------------
  Track 1: "Stairway to Heaven" by Led Zeppelin (Rock) - 8:02
  Track 2: "Billie Jean" by Michael Jackson (Pop) - 4:54
  Track 3: "Like a Prayer" by Madonna (Pop) - 5:40
  Track 4: "So What" by Miles Davis (Jazz) - 9:22
  Track 5: "Take Five" by Dave Brubeck (Jazz) - 5:24
  Track 6: "Blue in Green" by Miles Davis (Jazz) - 5:27
  Track 7: "Bohemian Rhapsody" by Queen (Rock) - 5:54
  Track 8: "Smells Like Teen Spirit" by Nirvana (Rock) - 5:01

======================================================================
[Line 22] BONUS: TypeScript Native Iterator (Symbol.iterator)
======================================================================
[Line 23] Using for...of loop with native iterator support...

[Line 24] Native Iterator Playback:
------------------------------------------------------------
  Track 1: "Bohemian Rhapsody" by Queen (Rock) - 5:54
  Track 2: "Take Five" by Dave Brubeck (Jazz) - 5:24
  Track 3: "Stairway to Heaven" by Led Zeppelin (Rock) - 8:02
  Track 4: "So What" by Miles Davis (Jazz) - 9:22
  Track 5: "Billie Jean" by Michael Jackson (Pop) - 4:54
  Track 6: "Smells Like Teen Spirit" by Nirvana (Rock) - 5:01
  Track 7: "Like a Prayer" by Madonna (Pop) - 5:40
  Track 8: "Blue in Green" by Miles Davis (Jazz) - 5:27

======================================================================
[Line 25] Iterator Reset Demonstration
======================================================================

[Line 26] First pass through Pop songs:
  - Billie Jean
  - Like a Prayer

[Line 27] Resetting iterator...

[Line 28] Second pass through Pop songs (after reset):
  - Billie Jean
  - Like a Prayer

======================================================================
[Line 29] Pattern Benefits Demonstrated:
======================================================================
[Line 30] 1. Single Responsibility: Collection stores, iterators traverse
[Line 31] 2. Open/Closed: New iterators without modifying collection
[Line 32] 3. Multiple traversals: Same collection, different strategies
[Line 33] 4. Uniform interface: All iterators share hasNext()/next()
[Line 34] 5. Encapsulation: Internal structure hidden from clients
======================================================================
```

---

## Code Analysis and Annotations

### Pattern Structure Overview

| Component | Source Lines | Description |
|-----------|--------------|-------------|
| `Song` class | 16-29 | Domain model representing a song with title, artist, genre, duration |
| `IIterator<T>` interface | 39-43 | Generic iterator contract with `hasNext()`, `next()`, `reset()` |
| `IterableCollection<T>` | 52-57 | Collection interface with factory methods for creating iterators |
| `SequentialIterator<T>` | 66-85 | Traverses elements from first to last |
| `ReverseIterator<T>` | 90-111 | Traverses elements from last to first |
| `FilteredIterator<T>` | 116-138 | Traverses only elements matching a predicate |
| `ShuffleIterator<T>` | 143-171 | Traverses elements in random order using Fisher-Yates |
| `Playlist` class | 180-223 | Concrete collection implementing multiple iterator factories |

### Output to Source Code Correlation

#### Initialization Phase

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| [Line 1] | 251-253 | Prints header banner for the demonstration |
| [Line 2] | 258 | Announces playlist creation |
| [Line 3] | 270 | Confirms 8 songs added to "My Favorites" playlist (lines 261-268) |

#### Strategy 1: Sequential Iteration

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| [Line 4-5] | 274-277 | Section header for sequential strategy |
| [Line 6] | 279-280 | Creates `SequentialIterator` via `createIterator()` (line 201-203) |
| Tracks 1-8 | 232-240 | `playSongs()` iterates using `hasNext()`/`next()` pattern |

**Analysis**: The `SequentialIterator` (lines 66-85) maintains a `position` counter starting at 0, incrementing with each `next()` call. Songs appear in insertion order.

#### Strategy 2: Reverse Iteration

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| [Line 7-8] | 285-288 | Section header for reverse strategy |
| [Line 9] | 290-291 | Creates `ReverseIterator` via `createReverseIterator()` (line 205-207) |
| Tracks 1-8 | 232-240 | Same `playSongs()` function, different iterator |

**Analysis**: The `ReverseIterator` (lines 90-111) initializes `position` to `length - 1` and decrements with each `next()` call. Output shows songs in reverse order: "Blue in Green" appears first instead of last.

#### Strategy 3: Filtered Iteration (Rock)

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| [Line 10-11] | 296-299 | Section header for Rock filtering |
| [Line 12] | 301-304 | Creates `FilteredIterator` with genre predicate (line 209-211) |
| Tracks 1-3 | 232-240 | Only 3 Rock songs: Bohemian Rhapsody, Stairway to Heaven, Smells Like Teen Spirit |

**Analysis**: The `FilteredIterator` (lines 116-138) pre-filters the collection in constructor (line 121) using `Array.filter()`. Only songs with `genre === "Rock"` are included.

#### Strategy 4: Filtered Iteration (Jazz)

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| [Line 13-14] | 310-313 | Section header for Jazz filtering |
| [Line 15] | 315-318 | Creates iterator with Jazz genre predicate |
| Tracks 1-3 | 232-240 | 3 Jazz songs: Take Five, So What, Blue in Green |

**Analysis**: Same `FilteredIterator` class reused with different predicate, demonstrating the Open/Closed principle.

#### Strategy 5: Filtered by Duration

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| [Line 16-17] | 324-327 | Section header for duration filtering |
| [Line 18] | 329-332 | Creates iterator with `durationSeconds > 300` predicate |
| Tracks 1-7 | 232-240 | 7 songs longer than 5 minutes (Billie Jean excluded at 4:54) |

**Analysis**: Demonstrates that predicates can filter on any Song property, not just genre. The flexibility comes from accepting a generic `(item: T) => boolean` function.

#### Strategy 6: Shuffle Iteration

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| [Line 19-20] | 338-341 | Section header for shuffle strategy |
| [Line 21] | 343-344 | Creates `ShuffleIterator` via `createShuffleIterator()` (line 213-215) |
| Tracks 1-8 | 232-240 | All 8 songs in random order |

**Analysis**: The `ShuffleIterator` (lines 143-171) creates a shuffled copy using the Fisher-Yates algorithm (lines 150-154). Each run produces different output.

#### TypeScript Native Iterator

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| [Line 22-23] | 350-353 | Section header for native iterator |
| [Line 24] | 355-361 | Uses `for...of` loop with `Symbol.iterator` |
| Tracks 1-8 | 218-222 | Generator function yields songs sequentially |

**Analysis**: The `Playlist` class implements `Symbol.iterator` (lines 217-222) as a generator function, enabling native TypeScript/JavaScript iteration syntax.

#### Iterator Reset Demonstration

| Output Line | Source Lines | Explanation |
|-------------|--------------|-------------|
| [Line 25] | 367-368 | Section header for reset demo |
| [Line 26] | 370-373 | First traversal of Pop songs |
| [Line 27] | 375 | Calls `reset()` on the iterator |
| [Line 28] | 378-381 | Second traversal produces same output |

**Analysis**: The `reset()` method (line 135-137 in FilteredIterator) sets `position` back to 0, allowing the iterator to be reused without creating a new instance.

### Key Design Pattern Benefits

| Output Line | Benefit | Explanation |
|-------------|---------|-------------|
| [Line 30] | Single Responsibility | `Playlist` stores data; iterators handle traversal logic |
| [Line 31] | Open/Closed | New iterators (e.g., `AlphabeticalIterator`) can be added without modifying `Playlist` |
| [Line 32] | Multiple Traversals | Same collection supports 6 different iteration strategies |
| [Line 33] | Uniform Interface | All iterators share `hasNext()`/`next()` contract (lines 39-43) |
| [Line 34] | Encapsulation | Client code never accesses `songs[]` array directly |

### Iterator Algorithm Comparison

| Iterator Type | Time Complexity | Space Complexity | Use Case |
|---------------|-----------------|------------------|----------|
| Sequential | O(n) | O(1) | Default forward traversal |
| Reverse | O(n) | O(1) | LIFO processing, undo operations |
| Filtered | O(n) | O(k) where k = matched items | Subset traversal, search results |
| Shuffle | O(n) | O(n) | Random playback, sampling |

---

## Design Pattern Principles Applied

1. **Single Responsibility Principle**: Each iterator class handles one traversal strategy
2. **Open/Closed Principle**: New iterators can be added without modifying existing code
3. **Interface Segregation**: `IIterator` defines minimal necessary methods
4. **Dependency Inversion**: Client code depends on `IIterator` interface, not concrete classes
5. **Encapsulation**: Internal `songs[]` array is never exposed to clients

---

## Extending the Pattern

To add a new iteration strategy (e.g., alphabetical by title):

```typescript
class AlphabeticalIterator implements IIterator<Song> {
    private position: number = 0;
    private sortedItems: Song[];

    constructor(collection: Song[]) {
        this.sortedItems = [...collection].sort((a, b) =>
            a.title.localeCompare(b.title)
        );
    }

    hasNext(): boolean {
        return this.position < this.sortedItems.length;
    }

    next(): Song {
        if (!this.hasNext()) throw new Error("No more elements");
        return this.sortedItems[this.position++];
    }

    reset(): void {
        this.position = 0;
    }
}
```

Then add to `Playlist`:

```typescript
createAlphabeticalIterator(): IIterator<Song> {
    return new AlphabeticalIterator(this.songs);
}
```

---

## Version Notes

- This implementation requires **TypeScript 5.3+** for proper `Generator` type support
- The `IIterator` interface is named to avoid conflict with TypeScript's built-in `Iterator` type
- Uses ES2022 target for modern JavaScript features
