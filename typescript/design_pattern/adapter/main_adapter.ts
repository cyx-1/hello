/**
 * Adapter Design Pattern in TypeScript
 *
 * The Adapter pattern allows incompatible interfaces to work together.
 * It acts as a bridge between two incompatible interfaces by wrapping
 * one interface to make it compatible with another.
 */

// Target Interface - what the client expects
interface MediaPlayer {
    play(audioType: string, fileName: string): void;
}

// Adaptee Interfaces - existing interfaces that need adapting
interface AdvancedMediaPlayer {
    playVlc(fileName: string): void;
    playMp4(fileName: string): void;
}

// Concrete Adaptee 1 - VLC Player
class VlcPlayer implements AdvancedMediaPlayer {
    playVlc(fileName: string): void {
        console.log(`[Line 22] VlcPlayer: Playing VLC file - ${fileName}`);
    }

    playMp4(fileName: string): void {
        // Do nothing - VLC player doesn't play MP4
    }
}

// Concrete Adaptee 2 - MP4 Player
class Mp4Player implements AdvancedMediaPlayer {
    playVlc(fileName: string): void {
        // Do nothing - MP4 player doesn't play VLC
    }

    playMp4(fileName: string): void {
        console.log(`[Line 35] Mp4Player: Playing MP4 file - ${fileName}`);
    }
}

// Adapter - bridges MediaPlayer and AdvancedMediaPlayer
class MediaAdapter implements MediaPlayer {
    private advancedMusicPlayer: AdvancedMediaPlayer;

    constructor(audioType: string) {
        if (audioType === "vlc") {
            this.advancedMusicPlayer = new VlcPlayer();
            console.log("[Line 46] MediaAdapter: Created VlcPlayer adapter");
        } else if (audioType === "mp4") {
            this.advancedMusicPlayer = new Mp4Player();
            console.log("[Line 49] MediaAdapter: Created Mp4Player adapter");
        } else {
            throw new Error(`Unsupported format: ${audioType}`);
        }
    }

    play(audioType: string, fileName: string): void {
        console.log(`[Line 55] MediaAdapter: Adapting ${audioType} format...`);
        if (audioType === "vlc") {
            this.advancedMusicPlayer.playVlc(fileName);
        } else if (audioType === "mp4") {
            this.advancedMusicPlayer.playMp4(fileName);
        }
    }
}

// Client - uses the Target interface
class AudioPlayer implements MediaPlayer {
    play(audioType: string, fileName: string): void {
        console.log(`\n[Line 66] AudioPlayer: Received request to play ${audioType} - ${fileName}`);

        // Built-in support for MP3
        if (audioType === "mp3") {
            console.log(`[Line 70] AudioPlayer: Playing MP3 file natively - ${fileName}`);
        }
        // Use adapter for other formats
        else if (audioType === "vlc" || audioType === "mp4") {
            const mediaAdapter = new MediaAdapter(audioType);
            mediaAdapter.play(audioType, fileName);
        } else {
            console.log(`[Line 77] AudioPlayer: Invalid media format - ${audioType}`);
        }
    }
}

// ============================================================
// Second Example: Payment Gateway Adapter
// ============================================================

// Target Interface - unified payment interface
interface PaymentProcessor {
    processPayment(amount: number, currency: string): boolean;
    getTransactionId(): string;
}

// Legacy Payment System (Adaptee)
class LegacyPaymentSystem {
    private transactionCode: string = "";

    makePayment(dollars: number, cents: number): number {
        const total = dollars + cents / 100;
        this.transactionCode = `LEGACY-${Date.now()}`;
        console.log(`[Line 98] LegacyPaymentSystem: Processing $${total.toFixed(2)}`);
        console.log(`[Line 99] LegacyPaymentSystem: Transaction code - ${this.transactionCode}`);
        return 1; // 1 = success, 0 = failure
    }

    getCode(): string {
        return this.transactionCode;
    }
}

// Third-party Payment API (Another Adaptee)
class ThirdPartyPaymentAPI {
    private txId: string = "";

    pay(payload: { value: number; curr: string }): { success: boolean; id: string } {
        this.txId = `3RD-${Math.random().toString(36).substr(2, 9).toUpperCase()}`;
        console.log(`[Line 113] ThirdPartyPaymentAPI: Processing ${payload.value} ${payload.curr}`);
        console.log(`[Line 114] ThirdPartyPaymentAPI: Transaction ID - ${this.txId}`);
        return { success: true, id: this.txId };
    }
}

// Adapter for Legacy Payment System
class LegacyPaymentAdapter implements PaymentProcessor {
    private legacySystem: LegacyPaymentSystem;
    private lastTransactionId: string = "";

    constructor() {
        this.legacySystem = new LegacyPaymentSystem();
        console.log("[Line 125] LegacyPaymentAdapter: Initialized");
    }

    processPayment(amount: number, currency: string): boolean {
        console.log(`[Line 129] LegacyPaymentAdapter: Converting ${amount} ${currency} to dollars/cents`);

        // Convert to legacy format (dollars and cents)
        const dollars = Math.floor(amount);
        const cents = Math.round((amount - dollars) * 100);

        const result = this.legacySystem.makePayment(dollars, cents);
        this.lastTransactionId = this.legacySystem.getCode();

        return result === 1;
    }

    getTransactionId(): string {
        return this.lastTransactionId;
    }
}

// Adapter for Third-party Payment API
class ThirdPartyPaymentAdapter implements PaymentProcessor {
    private api: ThirdPartyPaymentAPI;
    private lastTransactionId: string = "";

    constructor() {
        this.api = new ThirdPartyPaymentAPI();
        console.log("[Line 152] ThirdPartyPaymentAdapter: Initialized");
    }

    processPayment(amount: number, currency: string): boolean {
        console.log(`[Line 156] ThirdPartyPaymentAdapter: Creating payload for API`);

        // Convert to third-party format
        const payload = { value: amount, curr: currency };
        const result = this.api.pay(payload);
        this.lastTransactionId = result.id;

        return result.success;
    }

    getTransactionId(): string {
        return this.lastTransactionId;
    }
}

// Demonstration
function main(): void {
    console.log("=== Adapter Pattern Demonstration ===");

    // Demo 1: Media Player Adapter
    console.log("\n--- Media Player Adapter Demo ---");

    const audioPlayer = new AudioPlayer();

    audioPlayer.play("mp3", "song.mp3");
    audioPlayer.play("mp4", "video.mp4");
    audioPlayer.play("vlc", "movie.vlc");
    audioPlayer.play("avi", "clip.avi");

    // Demo 2: Payment Gateway Adapter
    console.log("\n\n--- Payment Gateway Adapter Demo ---");

    // Using Legacy Payment System through adapter
    console.log("\nProcessing payment through Legacy System:");
    const legacyAdapter: PaymentProcessor = new LegacyPaymentAdapter();
    const legacySuccess = legacyAdapter.processPayment(99.99, "USD");
    console.log(`[Line 191] Payment successful: ${legacySuccess}`);
    console.log(`[Line 192] Transaction ID: ${legacyAdapter.getTransactionId()}`);

    // Using Third-party API through adapter
    console.log("\nProcessing payment through Third-party API:");
    const thirdPartyAdapter: PaymentProcessor = new ThirdPartyPaymentAdapter();
    const thirdPartySuccess = thirdPartyAdapter.processPayment(149.50, "EUR");
    console.log(`[Line 198] Payment successful: ${thirdPartySuccess}`);
    console.log(`[Line 199] Transaction ID: ${thirdPartyAdapter.getTransactionId()}`);

    // Both adapters implement the same interface
    console.log("\n--- Unified Interface Demonstration ---");
    const processors: PaymentProcessor[] = [
        new LegacyPaymentAdapter(),
        new ThirdPartyPaymentAdapter()
    ];

    console.log("\nProcessing multiple payments through unified interface:");
    processors.forEach((processor, index) => {
        const success = processor.processPayment(50.00, "USD");
        console.log(`[Line 211] Processor ${index + 1} - Success: ${success}, ID: ${processor.getTransactionId()}`);
    });

    console.log("\n=== End of Demonstration ===");
}

main();
