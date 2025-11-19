/**
 * Iterator Design Pattern - TypeScript Implementation
 *
 * Demonstrates the Iterator pattern with a Music Playlist system
 * that supports multiple traversal strategies: sequential, reverse,
 * filtered by genre, and shuffle.
 */

// ============================================================================
// Domain Model
// ============================================================================

/**
 * Represents a song in the playlist
 */
class Song {
    constructor(
        public readonly title: string,
        public readonly artist: string,
        public readonly genre: string,
        public readonly durationSeconds: number
    ) {}

    toString(): string {
        const minutes = Math.floor(this.durationSeconds / 60);
        const seconds = this.durationSeconds % 60;
        return `"${this.title}" by ${this.artist} (${this.genre}) - ${minutes}:${seconds.toString().padStart(2, '0')}`;
    }
}

// ============================================================================
// Iterator Interface
// ============================================================================

/**
 * Generic Iterator interface defining traversal operations
 * Named IIterator to avoid conflict with TypeScript's built-in Iterator
 */
interface IIterator<T> {
    hasNext(): boolean;
    next(): T;
    reset(): void;
}

// ============================================================================
// Collection Interface
// ============================================================================

/**
 * Interface for collections that can create iterators
 */
interface IterableCollection<T> {
    createIterator(): IIterator<T>;
    createReverseIterator(): IIterator<T>;
    createFilteredIterator(predicate: (item: T) => boolean): IIterator<T>;
    createShuffleIterator(): IIterator<T>;
}

// ============================================================================
// Concrete Iterators
// ============================================================================

/**
 * Sequential Iterator - traverses from first to last
 */
class SequentialIterator<T> implements IIterator<T> {
    private position: number = 0;

    constructor(private collection: T[]) {}

    hasNext(): boolean {
        return this.position < this.collection.length;
    }

    next(): T {
        if (!this.hasNext()) {
            throw new Error("No more elements");
        }
        return this.collection[this.position++];
    }

    reset(): void {
        this.position = 0;
    }
}

/**
 * Reverse Iterator - traverses from last to first
 */
class ReverseIterator<T> implements IIterator<T> {
    private position: number;

    constructor(private collection: T[]) {
        this.position = collection.length - 1;
    }

    hasNext(): boolean {
        return this.position >= 0;
    }

    next(): T {
        if (!this.hasNext()) {
            throw new Error("No more elements");
        }
        return this.collection[this.position--];
    }

    reset(): void {
        this.position = this.collection.length - 1;
    }
}

/**
 * Filtered Iterator - traverses only elements matching a predicate
 */
class FilteredIterator<T> implements IIterator<T> {
    private position: number = 0;
    private filteredItems: T[];

    constructor(collection: T[], predicate: (item: T) => boolean) {
        this.filteredItems = collection.filter(predicate);
    }

    hasNext(): boolean {
        return this.position < this.filteredItems.length;
    }

    next(): T {
        if (!this.hasNext()) {
            throw new Error("No more elements");
        }
        return this.filteredItems[this.position++];
    }

    reset(): void {
        this.position = 0;
    }
}

/**
 * Shuffle Iterator - traverses in random order
 */
class ShuffleIterator<T> implements IIterator<T> {
    private position: number = 0;
    private shuffledItems: T[];

    constructor(collection: T[]) {
        // Create a shuffled copy using Fisher-Yates algorithm
        this.shuffledItems = [...collection];
        for (let i = this.shuffledItems.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.shuffledItems[i], this.shuffledItems[j]] =
                [this.shuffledItems[j], this.shuffledItems[i]];
        }
    }

    hasNext(): boolean {
        return this.position < this.shuffledItems.length;
    }

    next(): T {
        if (!this.hasNext()) {
            throw new Error("No more elements");
        }
        return this.shuffledItems[this.position++];
    }

    reset(): void {
        this.position = 0;
    }
}

// ============================================================================
// Concrete Collection
// ============================================================================

/**
 * Playlist - a collection of songs supporting multiple iteration strategies
 */
class Playlist implements IterableCollection<Song> {
    private songs: Song[] = [];
    private name: string;

    constructor(name: string) {
        this.name = name;
    }

    addSong(song: Song): void {
        this.songs.push(song);
    }

    getCount(): number {
        return this.songs.length;
    }

    getName(): string {
        return this.name;
    }

    // Factory methods for different iterators
    createIterator(): IIterator<Song> {
        return new SequentialIterator(this.songs);
    }

    createReverseIterator(): IIterator<Song> {
        return new ReverseIterator(this.songs);
    }

    createFilteredIterator(predicate: (song: Song) => boolean): IIterator<Song> {
        return new FilteredIterator(this.songs, predicate);
    }

    createShuffleIterator(): IIterator<Song> {
        return new ShuffleIterator(this.songs);
    }

    // TypeScript native iterator support
    *[Symbol.iterator](): Generator<Song, void, unknown> {
        for (const song of this.songs) {
            yield song;
        }
    }
}

// ============================================================================
// Helper function
// ============================================================================

/**
 * Plays all songs from an iterator and displays them
 */
function playSongs(iterator: IIterator<Song>, label: string): void {
    console.log(`\n${label}:`);
    console.log("-".repeat(60));
    let trackNumber = 1;
    while (iterator.hasNext()) {
        const song = iterator.next();
        console.log(`  Track ${trackNumber}: ${song.toString()}`);
        trackNumber++;
    }
    if (trackNumber === 1) {
        console.log("  (No songs to play)");
    }
}

// ============================================================================
// Main Demonstration
// ============================================================================

function main(): void {
    console.log("=".repeat(70));
    console.log("[Line 1] Iterator Design Pattern - Music Playlist Example");
    console.log("=".repeat(70));

    // Create a playlist with various songs
    const playlist = new Playlist("My Favorites");

    console.log("\n[Line 2] Creating playlist with songs...");

    // Add songs from different genres
    playlist.addSong(new Song("Bohemian Rhapsody", "Queen", "Rock", 354));
    playlist.addSong(new Song("Take Five", "Dave Brubeck", "Jazz", 324));
    playlist.addSong(new Song("Stairway to Heaven", "Led Zeppelin", "Rock", 482));
    playlist.addSong(new Song("So What", "Miles Davis", "Jazz", 562));
    playlist.addSong(new Song("Billie Jean", "Michael Jackson", "Pop", 294));
    playlist.addSong(new Song("Smells Like Teen Spirit", "Nirvana", "Rock", 301));
    playlist.addSong(new Song("Like a Prayer", "Madonna", "Pop", 340));
    playlist.addSong(new Song("Blue in Green", "Miles Davis", "Jazz", 327));

    console.log(`[Line 3] Playlist "${playlist.getName()}" created with ${playlist.getCount()} songs`);

    // ========================================================================
    // Strategy 1: Sequential Iteration
    // ========================================================================
    console.log("\n" + "=".repeat(70));
    console.log("[Line 4] STRATEGY 1: Sequential Iteration");
    console.log("=".repeat(70));
    console.log("[Line 5] Traversing playlist from first to last song...");

    const sequentialIterator = playlist.createIterator();
    playSongs(sequentialIterator, "[Line 6] Sequential Playback");

    // ========================================================================
    // Strategy 2: Reverse Iteration
    // ========================================================================
    console.log("\n" + "=".repeat(70));
    console.log("[Line 7] STRATEGY 2: Reverse Iteration");
    console.log("=".repeat(70));
    console.log("[Line 8] Traversing playlist from last to first song...");

    const reverseIterator = playlist.createReverseIterator();
    playSongs(reverseIterator, "[Line 9] Reverse Playback");

    // ========================================================================
    // Strategy 3: Filtered Iteration (Rock songs only)
    // ========================================================================
    console.log("\n" + "=".repeat(70));
    console.log("[Line 10] STRATEGY 3: Filtered Iteration (Rock Genre)");
    console.log("=".repeat(70));
    console.log("[Line 11] Traversing only Rock songs...");

    const rockIterator = playlist.createFilteredIterator(
        (song) => song.genre === "Rock"
    );
    playSongs(rockIterator, "[Line 12] Rock Songs Only");

    // ========================================================================
    // Strategy 4: Filtered Iteration (Jazz songs only)
    // ========================================================================
    console.log("\n" + "=".repeat(70));
    console.log("[Line 13] STRATEGY 4: Filtered Iteration (Jazz Genre)");
    console.log("=".repeat(70));
    console.log("[Line 14] Traversing only Jazz songs...");

    const jazzIterator = playlist.createFilteredIterator(
        (song) => song.genre === "Jazz"
    );
    playSongs(jazzIterator, "[Line 15] Jazz Songs Only");

    // ========================================================================
    // Strategy 5: Filtered by Duration (songs longer than 5 minutes)
    // ========================================================================
    console.log("\n" + "=".repeat(70));
    console.log("[Line 16] STRATEGY 5: Filtered by Duration (> 5 minutes)");
    console.log("=".repeat(70));
    console.log("[Line 17] Traversing songs longer than 5 minutes...");

    const longSongsIterator = playlist.createFilteredIterator(
        (song) => song.durationSeconds > 300
    );
    playSongs(longSongsIterator, "[Line 18] Long Songs (> 5 min)");

    // ========================================================================
    // Strategy 6: Shuffle Iteration
    // ========================================================================
    console.log("\n" + "=".repeat(70));
    console.log("[Line 19] STRATEGY 6: Shuffle Iteration");
    console.log("=".repeat(70));
    console.log("[Line 20] Traversing playlist in random order...");

    const shuffleIterator = playlist.createShuffleIterator();
    playSongs(shuffleIterator, "[Line 21] Shuffled Playback");

    // ========================================================================
    // TypeScript Native Iterator (for...of)
    // ========================================================================
    console.log("\n" + "=".repeat(70));
    console.log("[Line 22] BONUS: TypeScript Native Iterator (Symbol.iterator)");
    console.log("=".repeat(70));
    console.log("[Line 23] Using for...of loop with native iterator support...");

    console.log("\n[Line 24] Native Iterator Playback:");
    console.log("-".repeat(60));
    let nativeTrackNumber = 1;
    for (const song of playlist) {
        console.log(`  Track ${nativeTrackNumber}: ${song.toString()}`);
        nativeTrackNumber++;
    }

    // ========================================================================
    // Iterator Reset Demonstration
    // ========================================================================
    console.log("\n" + "=".repeat(70));
    console.log("[Line 25] Iterator Reset Demonstration");
    console.log("=".repeat(70));

    const resetIterator = playlist.createFilteredIterator(
        (song) => song.genre === "Pop"
    );

    console.log("\n[Line 26] First pass through Pop songs:");
    while (resetIterator.hasNext()) {
        console.log(`  - ${resetIterator.next().title}`);
    }

    console.log("\n[Line 27] Resetting iterator...");
    resetIterator.reset();

    console.log("\n[Line 28] Second pass through Pop songs (after reset):");
    while (resetIterator.hasNext()) {
        console.log(`  - ${resetIterator.next().title}`);
    }

    // ========================================================================
    // Summary
    // ========================================================================
    console.log("\n" + "=".repeat(70));
    console.log("[Line 29] Pattern Benefits Demonstrated:");
    console.log("=".repeat(70));
    console.log("[Line 30] 1. Single Responsibility: Collection stores, iterators traverse");
    console.log("[Line 31] 2. Open/Closed: New iterators without modifying collection");
    console.log("[Line 32] 3. Multiple traversals: Same collection, different strategies");
    console.log("[Line 33] 4. Uniform interface: All iterators share hasNext()/next()");
    console.log("[Line 34] 5. Encapsulation: Internal structure hidden from clients");
    console.log("=".repeat(70));
}

// Run the demonstration
main();
