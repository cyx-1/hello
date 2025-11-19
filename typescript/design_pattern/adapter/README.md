# Adapter Design Pattern in TypeScript

The Adapter pattern allows incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces by wrapping one interface to make it compatible with another. This is particularly useful when integrating legacy systems or third-party libraries.

## Requirements

- Node.js 18+
- TypeScript 5.3+

## How to Run

```bash
npm install
npm run start
```

## Source Code

```typescript
1   /**
2    * Adapter Design Pattern in TypeScript
3    *
4    * The Adapter pattern allows incompatible interfaces to work together.
5    * It acts as a bridge between two incompatible interfaces by wrapping
6    * one interface to make it compatible with another.
7    */
8
9   // Target Interface - what the client expects
10  interface MediaPlayer {
11      play(audioType: string, fileName: string): void;
12  }
13
14  // Adaptee Interfaces - existing interfaces that need adapting
15  interface AdvancedMediaPlayer {
16      playVlc(fileName: string): void;
17      playMp4(fileName: string): void;
18  }
19
20  // Concrete Adaptee 1 - VLC Player
21  class VlcPlayer implements AdvancedMediaPlayer {
22      playVlc(fileName: string): void {
23          console.log(`[Line 22] VlcPlayer: Playing VLC file - ${fileName}`);
24      }
25
26      playMp4(fileName: string): void {
27          // Do nothing - VLC player doesn't play MP4
28      }
29  }
30
31  // Concrete Adaptee 2 - MP4 Player
32  class Mp4Player implements AdvancedMediaPlayer {
33      playVlc(fileName: string): void {
34          // Do nothing - MP4 player doesn't play VLC
35      }
36
37      playMp4(fileName: string): void {
38          console.log(`[Line 35] Mp4Player: Playing MP4 file - ${fileName}`);
39      }
40  }
41
42  // Adapter - bridges MediaPlayer and AdvancedMediaPlayer
43  class MediaAdapter implements MediaPlayer {
44      private advancedMusicPlayer: AdvancedMediaPlayer;
45
46      constructor(audioType: string) {
47          if (audioType === "vlc") {
48              this.advancedMusicPlayer = new VlcPlayer();
49              console.log("[Line 46] MediaAdapter: Created VlcPlayer adapter");
50          } else if (audioType === "mp4") {
51              this.advancedMusicPlayer = new Mp4Player();
52              console.log("[Line 49] MediaAdapter: Created Mp4Player adapter");
53          } else {
54              throw new Error(`Unsupported format: ${audioType}`);
55          }
56      }
57
58      play(audioType: string, fileName: string): void {
59          console.log(`[Line 55] MediaAdapter: Adapting ${audioType} format...`);
60          if (audioType === "vlc") {
61              this.advancedMusicPlayer.playVlc(fileName);
62          } else if (audioType === "mp4") {
63              this.advancedMusicPlayer.playMp4(fileName);
64          }
65      }
66  }
67
68  // Client - uses the Target interface
69  class AudioPlayer implements MediaPlayer {
70      play(audioType: string, fileName: string): void {
71          console.log(`\n[Line 66] AudioPlayer: Received request to play ${audioType} - ${fileName}`);
72
73          // Built-in support for MP3
74          if (audioType === "mp3") {
75              console.log(`[Line 70] AudioPlayer: Playing MP3 file natively - ${fileName}`);
76          }
77          // Use adapter for other formats
78          else if (audioType === "vlc" || audioType === "mp4") {
79              const mediaAdapter = new MediaAdapter(audioType);
80              mediaAdapter.play(audioType, fileName);
81          } else {
82              console.log(`[Line 77] AudioPlayer: Invalid media format - ${audioType}`);
83          }
84      }
85  }
86
87  // ============================================================
88  // Second Example: Payment Gateway Adapter
89  // ============================================================
90
91  // Target Interface - unified payment interface
92  interface PaymentProcessor {
93      processPayment(amount: number, currency: string): boolean;
94      getTransactionId(): string;
95  }
96
97  // Legacy Payment System (Adaptee)
98  class LegacyPaymentSystem {
99      private transactionCode: string = "";
100
101     makePayment(dollars: number, cents: number): number {
102         const total = dollars + cents / 100;
103         this.transactionCode = `LEGACY-${Date.now()}`;
104         console.log(`[Line 98] LegacyPaymentSystem: Processing $${total.toFixed(2)}`);
105         console.log(`[Line 99] LegacyPaymentSystem: Transaction code - ${this.transactionCode}`);
106         return 1; // 1 = success, 0 = failure
107     }
108
109     getCode(): string {
110         return this.transactionCode;
111     }
112 }
113
114 // Third-party Payment API (Another Adaptee)
115 class ThirdPartyPaymentAPI {
116     private txId: string = "";
117
118     pay(payload: { value: number; curr: string }): { success: boolean; id: string } {
119         this.txId = `3RD-${Math.random().toString(36).substr(2, 9).toUpperCase()}`;
120         console.log(`[Line 113] ThirdPartyPaymentAPI: Processing ${payload.value} ${payload.curr}`);
121         console.log(`[Line 114] ThirdPartyPaymentAPI: Transaction ID - ${this.txId}`);
122         return { success: true, id: this.txId };
123     }
124 }
125
126 // Adapter for Legacy Payment System
127 class LegacyPaymentAdapter implements PaymentProcessor {
128     private legacySystem: LegacyPaymentSystem;
129     private lastTransactionId: string = "";
130
131     constructor() {
132         this.legacySystem = new LegacyPaymentSystem();
133         console.log("[Line 125] LegacyPaymentAdapter: Initialized");
134     }
135
136     processPayment(amount: number, currency: string): boolean {
137         console.log(`[Line 129] LegacyPaymentAdapter: Converting ${amount} ${currency} to dollars/cents`);
138
139         // Convert to legacy format (dollars and cents)
140         const dollars = Math.floor(amount);
141         const cents = Math.round((amount - dollars) * 100);
142
143         const result = this.legacySystem.makePayment(dollars, cents);
144         this.lastTransactionId = this.legacySystem.getCode();
145
146         return result === 1;
147     }
148
149     getTransactionId(): string {
150         return this.lastTransactionId;
151     }
152 }
153
154 // Adapter for Third-party Payment API
155 class ThirdPartyPaymentAdapter implements PaymentProcessor {
156     private api: ThirdPartyPaymentAPI;
157     private lastTransactionId: string = "";
158
159     constructor() {
160         this.api = new ThirdPartyPaymentAPI();
161         console.log("[Line 152] ThirdPartyPaymentAdapter: Initialized");
162     }
163
164     processPayment(amount: number, currency: string): boolean {
165         console.log(`[Line 156] ThirdPartyPaymentAdapter: Creating payload for API`);
166
167         // Convert to third-party format
168         const payload = { value: amount, curr: currency };
169         const result = this.api.pay(payload);
170         this.lastTransactionId = result.id;
171
172         return result.success;
173     }
174
175     getTransactionId(): string {
176         return this.lastTransactionId;
177     }
178 }
```

## Program Output

```
=== Adapter Pattern Demonstration ===

--- Media Player Adapter Demo ---

[Line 66] AudioPlayer: Received request to play mp3 - song.mp3
[Line 70] AudioPlayer: Playing MP3 file natively - song.mp3

[Line 66] AudioPlayer: Received request to play mp4 - video.mp4
[Line 49] MediaAdapter: Created Mp4Player adapter
[Line 55] MediaAdapter: Adapting mp4 format...
[Line 35] Mp4Player: Playing MP4 file - video.mp4

[Line 66] AudioPlayer: Received request to play vlc - movie.vlc
[Line 46] MediaAdapter: Created VlcPlayer adapter
[Line 55] MediaAdapter: Adapting vlc format...
[Line 22] VlcPlayer: Playing VLC file - movie.vlc

[Line 66] AudioPlayer: Received request to play avi - clip.avi
[Line 77] AudioPlayer: Invalid media format - avi


--- Payment Gateway Adapter Demo ---

Processing payment through Legacy System:
[Line 125] LegacyPaymentAdapter: Initialized
[Line 129] LegacyPaymentAdapter: Converting 99.99 USD to dollars/cents
[Line 98] LegacyPaymentSystem: Processing $99.99
[Line 99] LegacyPaymentSystem: Transaction code - LEGACY-1763512747633
[Line 191] Payment successful: true
[Line 192] Transaction ID: LEGACY-1763512747633

Processing payment through Third-party API:
[Line 152] ThirdPartyPaymentAdapter: Initialized
[Line 156] ThirdPartyPaymentAdapter: Creating payload for API
[Line 113] ThirdPartyPaymentAPI: Processing 149.5 EUR
[Line 114] ThirdPartyPaymentAPI: Transaction ID - 3RD-GXLNU4456
[Line 198] Payment successful: true
[Line 199] Transaction ID: 3RD-GXLNU4456

--- Unified Interface Demonstration ---
[Line 125] LegacyPaymentAdapter: Initialized
[Line 152] ThirdPartyPaymentAdapter: Initialized

Processing multiple payments through unified interface:
[Line 129] LegacyPaymentAdapter: Converting 50 USD to dollars/cents
[Line 98] LegacyPaymentSystem: Processing $50.00
[Line 99] LegacyPaymentSystem: Transaction code - LEGACY-1763512747634
[Line 211] Processor 1 - Success: true, ID: LEGACY-1763512747634
[Line 156] ThirdPartyPaymentAdapter: Creating payload for API
[Line 113] ThirdPartyPaymentAPI: Processing 50 USD
[Line 114] ThirdPartyPaymentAPI: Transaction ID - 3RD-YJXM3LR24
[Line 211] Processor 2 - Success: true, ID: 3RD-YJXM3LR24

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Pattern Components

#### Target Interface (Lines 10-12, 92-95)
- Defines the interface that the client expects
- `MediaPlayer` expects a simple `play(audioType, fileName)` method
- `PaymentProcessor` expects `processPayment(amount, currency)` and `getTransactionId()`

#### Adaptee (Lines 21-40, 98-124)
- The existing classes with incompatible interfaces
- `VlcPlayer` and `Mp4Player` have different method signatures
- `LegacyPaymentSystem` uses `dollars/cents` and returns status codes
- `ThirdPartyPaymentAPI` uses payload objects and returns result objects

#### Adapter (Lines 43-66, 127-177)
- Implements the Target interface and wraps the Adaptee
- `MediaAdapter` translates `play()` calls to `playVlc()` or `playMp4()`
- `LegacyPaymentAdapter` converts `amount` to `dollars/cents` format
- `ThirdPartyPaymentAdapter` creates payload objects for the API

### Output Correlation

| Output Line | Source Line | Explanation |
|-------------|-------------|-------------|
| `AudioPlayer: Playing MP3 file natively` | Line 75 | No adapter needed for MP3 |
| `MediaAdapter: Created Mp4Player adapter` | Line 51-52 | Adapter instantiates appropriate player |
| `MediaAdapter: Adapting mp4 format...` | Line 59 | Adapter translates the call |
| `Mp4Player: Playing MP4 file` | Line 38 | Actual playback through adaptee |
| `Invalid media format - avi` | Line 82 | Unsupported format handled gracefully |
| `Converting 99.99 USD to dollars/cents` | Line 137 | Adapter performs data transformation |
| `LegacyPaymentSystem: Processing $99.99` | Line 104 | Legacy system receives converted data |

### Why Adapter Works

1. **Interface Translation**: The adapter translates between incompatible interfaces
   - `play("mp4", "video.mp4")` → `playMp4("video.mp4")`
   - `processPayment(99.99, "USD")` → `makePayment(99, 99)`

2. **Encapsulation**: Client code doesn't know about the adaptee's specific interface
   - `AudioPlayer` doesn't know `VlcPlayer` exists
   - Payment processing code uses unified `PaymentProcessor` interface

3. **Polymorphism**: Both adapters can be stored in the same array (Lines 203-206)
   - Enables uniform processing regardless of underlying implementation

### Key Transformations Demonstrated

#### Media Player Example
- Client uses: `play(audioType: string, fileName: string)`
- VLC uses: `playVlc(fileName: string)`
- MP4 uses: `playMp4(fileName: string)`

#### Payment Gateway Example
- Client uses: `processPayment(amount: number, currency: string)`
- Legacy uses: `makePayment(dollars: number, cents: number)` returns `number`
- Third-party uses: `pay(payload: {value, curr})` returns `{success, id}`

### Use Cases

- **Legacy System Integration**: Wrap old systems with modern interfaces
- **Third-party Library Integration**: Create consistent API for different libraries
- **Testing**: Create test adapters that mimic production systems
- **API Versioning**: Support multiple API versions through adapters
- **Cross-platform Compatibility**: Adapt platform-specific APIs to common interface
