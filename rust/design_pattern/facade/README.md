# Facade Design Pattern in Rust

## Description

The **Facade Pattern** provides a simplified interface to a complex subsystem. It defines a higher-level interface that makes the subsystem easier to use by wrapping complicated functionality behind a single, easy-to-use API.

### When to Use
- When you need to provide a simple interface to a complex subsystem
- When there are many interdependent classes or complex operations
- When you want to layer your subsystems and reduce coupling

### Real-World Analogy
A home theater system is a perfect example: instead of turning on the TV, setting input, adjusting brightness, powering the sound system, setting volume, launching the streaming app, and dimming the lights separately, you press one "Watch Movie" button on a universal remote (the facade).

---

## Source Code

```rust
  1  // Facade Design Pattern in Rust
  2  // Demonstrates how a facade simplifies interaction with complex subsystems
  3
  4  // ============================================================================
  5  // Subsystem Components - Complex internal systems
  6  // ============================================================================
  7
  8  /// Television subsystem with multiple operations
  9  struct Television {
 10      brand: String,
 11  }
 12
 13  impl Television {
 14      fn new(brand: &str) -> Self {
 15          Television {
 16              brand: brand.to_string(),
 17          }
 18      }
 19
 20      fn turn_on(&self) {
 21          println!("  [TV] {} Television is turning ON", self.brand);
 22      }
 23
 24      fn turn_off(&self) {
 25          println!("  [TV] {} Television is turning OFF", self.brand);
 26      }
 27
 28      fn set_input(&self, input: &str) {
 29          println!("  [TV] Setting input source to: {}", input);
 30      }
 31
 32      fn set_brightness(&self, level: u8) {
 33          println!("  [TV] Adjusting brightness to {}%", level);
 34      }
 35  }
 36
 37  /// Sound system subsystem with audio controls
 38  struct SoundSystem {
 39      model: String,
 40  }
 41
 42  impl SoundSystem {
 43      fn new(model: &str) -> Self {
 44          SoundSystem {
 45              model: model.to_string(),
 46          }
 47      }
 48
 49      fn turn_on(&self) {
 50          println!("  [Audio] {} Sound System powering ON", self.model);
 51      }
 52
 53      fn turn_off(&self) {
 54          println!("  [Audio] {} Sound System powering OFF", self.model);
 55      }
 56
 57      fn set_volume(&self, level: u8) {
 58          println!("  [Audio] Setting volume to {}", level);
 59      }
 60
 61      fn set_surround_mode(&self, mode: &str) {
 62          println!("  [Audio] Surround mode set to: {}", mode);
 63      }
 64  }
 65
 66  /// Streaming player subsystem
 67  struct StreamingPlayer {
 68      service: String,
 69  }
 70
 71  impl StreamingPlayer {
 72      fn new(service: &str) -> Self {
 73          StreamingPlayer {
 74              service: service.to_string(),
 75          }
 76      }
 77
 78      fn turn_on(&self) {
 79          println!("  [Stream] {} Streaming Player starting", self.service);
 80      }
 81
 82      fn turn_off(&self) {
 83          println!("  [Stream] {} Streaming Player shutting down", self.service);
 84      }
 85
 86      fn login(&self) {
 87          println!("  [Stream] Logging into {} account", self.service);
 88      }
 89
 90      fn play(&self, content: &str) {
 91          println!("  [Stream] Now playing: {}", content);
 92      }
 93
 94      fn stop(&self) {
 95          println!("  [Stream] Playback stopped");
 96      }
 97  }
 98
 99  /// Room lighting subsystem
100  struct Lights {
101      room: String,
102  }
103
104  impl Lights {
105      fn new(room: &str) -> Self {
106          Lights {
107              room: room.to_string(),
108          }
109      }
110
111      fn dim(&self, level: u8) {
112          println!("  [Lights] {} lights dimmed to {}%", self.room, level);
113      }
114
115      fn on(&self) {
116          println!("  [Lights] {} lights turned ON (100%)", self.room);
117      }
118  }
119
120  // ============================================================================
121  // Facade - Simplified interface to the complex subsystems
122  // ============================================================================
123
124  /// HomeTheaterFacade provides a simple interface to control
125  /// all home theater components with single method calls
126  struct HomeTheaterFacade {
127      tv: Television,
128      sound: SoundSystem,
129      player: StreamingPlayer,
130      lights: Lights,
131  }
132
133  impl HomeTheaterFacade {
134      fn new() -> Self {
135          println!("=== Initializing Home Theater System ===\n");
136          HomeTheaterFacade {
137              tv: Television::new("Samsung"),
138              sound: SoundSystem::new("Sonos"),
139              player: StreamingPlayer::new("Netflix"),
140              lights: Lights::new("Living Room"),
141          }
142      }
143
144      /// Simple method to start movie night - hides all complexity
145      fn watch_movie(&self, movie: &str) {
146          println!(">>> Starting Movie Night: '{}' <<<\n", movie);
147
148          // Facade coordinates all subsystems
149          self.lights.dim(20);
150          self.tv.turn_on();
151          self.tv.set_input("HDMI-1");
152          self.tv.set_brightness(80);
153          self.sound.turn_on();
154          self.sound.set_volume(50);
155          self.sound.set_surround_mode("Cinema");
156          self.player.turn_on();
157          self.player.login();
158          self.player.play(movie);
159
160          println!("\n>>> Enjoy your movie! <<<\n");
161      }
162
163      /// Simple method to end movie night - hides shutdown complexity
164      fn end_movie(&self) {
165          println!(">>> Ending Movie Night <<<\n");
166
167          // Facade coordinates orderly shutdown
168          self.player.stop();
169          self.player.turn_off();
170          self.sound.turn_off();
171          self.tv.turn_off();
172          self.lights.on();
173
174          println!("\n>>> System shutdown complete <<<\n");
175      }
176
177      /// Simple method for music listening mode
178      fn listen_to_music(&self) {
179          println!(">>> Starting Music Mode <<<\n");
180
181          self.lights.dim(60);
182          self.sound.turn_on();
183          self.sound.set_volume(40);
184          self.sound.set_surround_mode("Stereo");
185
186          println!("\n>>> Music mode ready <<<\n");
187      }
188  }
189
190  // ============================================================================
191  // Main - Demonstrates facade usage
192  // ============================================================================
193
194  fn main() {
195      println!("============================================");
196      println!("   FACADE DESIGN PATTERN DEMONSTRATION");
197      println!("============================================\n");
198
199      // Create the facade - user only interacts with this
200      let home_theater = HomeTheaterFacade::new();
201
202      // Without facade: user would need to call 10+ methods manually
203      // With facade: single method call handles everything
204
205      println!("--------------------------------------------");
206      println!("Client calls: home_theater.watch_movie(...)");
207      println!("--------------------------------------------\n");
208
209      home_theater.watch_movie("The Matrix");
210
211      println!("--------------------------------------------");
212      println!("Client calls: home_theater.end_movie()");
213      println!("--------------------------------------------\n");
214
215      home_theater.end_movie();
216
217      println!("--------------------------------------------");
218      println!("Client calls: home_theater.listen_to_music()");
219      println!("--------------------------------------------\n");
220
221      home_theater.listen_to_music();
222
223      println!("============================================");
224      println!("   KEY INSIGHT: Facade Pattern");
225      println!("============================================");
226      println!("The client made only 3 simple calls, but the");
227      println!("facade coordinated 15+ subsystem operations!");
228      println!("============================================\n");
229  }
```

---

## Program Output

```
============================================
   FACADE DESIGN PATTERN DEMONSTRATION
============================================

=== Initializing Home Theater System ===

--------------------------------------------
Client calls: home_theater.watch_movie(...)
--------------------------------------------

>>> Starting Movie Night: 'The Matrix' <<<

  [Lights] Living Room lights dimmed to 20%
  [TV] Samsung Television is turning ON
  [TV] Setting input source to: HDMI-1
  [TV] Adjusting brightness to 80%
  [Audio] Sonos Sound System powering ON
  [Audio] Setting volume to 50
  [Audio] Surround mode set to: Cinema
  [Stream] Netflix Streaming Player starting
  [Stream] Logging into Netflix account
  [Stream] Now playing: The Matrix

>>> Enjoy your movie! <<<

--------------------------------------------
Client calls: home_theater.end_movie()
--------------------------------------------

>>> Ending Movie Night <<<

  [Stream] Playback stopped
  [Stream] Netflix Streaming Player shutting down
  [Audio] Sonos Sound System powering OFF
  [TV] Samsung Television is turning OFF
  [Lights] Living Room lights turned ON (100%)

>>> System shutdown complete <<<

--------------------------------------------
Client calls: home_theater.listen_to_music()
--------------------------------------------

>>> Starting Music Mode <<<

  [Lights] Living Room lights dimmed to 60%
  [Audio] Sonos Sound System powering ON
  [Audio] Setting volume to 40
  [Audio] Surround mode set to: Stereo

>>> Music mode ready <<<

============================================
   KEY INSIGHT: Facade Pattern
============================================
The client made only 3 simple calls, but the
facade coordinated 15+ subsystem operations!
============================================
```

---

## Code Annotations

### Key Sections Explained

#### Subsystem Components (Lines 8-118)

- **Lines 9-35**: `Television` struct represents one complex subsystem with multiple operations (`turn_on`, `turn_off`, `set_input`, `set_brightness`). Each operation prints to show when it executes.

- **Lines 38-64**: `SoundSystem` struct provides audio controls. Note how each subsystem is independent and knows nothing about the others.

- **Lines 67-97**: `StreamingPlayer` struct handles content streaming with operations like `login`, `play`, `stop`. These would be tedious for clients to coordinate manually.

- **Lines 100-118**: `Lights` struct controls room lighting. Even this simple subsystem requires coordination with other systems for proper ambiance.

#### Facade Implementation (Lines 126-188)

- **Lines 126-131**: The `HomeTheaterFacade` struct owns all four subsystems. This composition is key to the pattern - the facade encapsulates the subsystems.

- **Lines 134-142**: The `new()` constructor initializes all subsystems with sensible defaults. Clients don't need to know about individual component brands or settings.

- **Lines 145-161**: `watch_movie()` is the core facade method. It coordinates **10 operations** across 4 subsystems with a single call. Notice the logical ordering: lights first, then TV, sound, and finally streaming.

- **Lines 164-175**: `end_movie()` provides orderly shutdown. The facade ensures proper sequence (stop content before turning off devices, lights last).

- **Lines 178-187**: `listen_to_music()` demonstrates that facades can offer multiple simplified operations for different use cases.

#### Client Code (Lines 194-229)

- **Line 200**: Client creates only the facade, not individual subsystems.

- **Lines 209, 215, 221**: The client makes just 3 simple calls. Compare this to the 15+ subsystem method calls that would be needed without the facade.

---

### Output to Source Code Correlation

| Output Line | Source Line | Explanation |
|------------|-------------|-------------|
| `=== Initializing Home Theater System ===` | 135 | Facade constructor prints initialization message |
| `[Lights] Living Room lights dimmed to 20%` | 149 -> 112 | `watch_movie` calls `lights.dim()` which prints at line 112 |
| `[TV] Samsung Television is turning ON` | 150 -> 21 | `watch_movie` calls `tv.turn_on()` which prints at line 21 |
| `[TV] Setting input source to: HDMI-1` | 151 -> 29 | `watch_movie` calls `tv.set_input()` which prints at line 29 |
| `[TV] Adjusting brightness to 80%` | 152 -> 33 | `watch_movie` calls `tv.set_brightness()` which prints at line 33 |
| `[Audio] Sonos Sound System powering ON` | 153 -> 50 | `watch_movie` calls `sound.turn_on()` which prints at line 50 |
| `[Audio] Setting volume to 50` | 154 -> 58 | `watch_movie` calls `sound.set_volume()` which prints at line 58 |
| `[Audio] Surround mode set to: Cinema` | 155 -> 62 | `watch_movie` calls `sound.set_surround_mode()` which prints at line 62 |
| `[Stream] Netflix Streaming Player starting` | 156 -> 79 | `watch_movie` calls `player.turn_on()` which prints at line 79 |
| `[Stream] Logging into Netflix account` | 157 -> 87 | `watch_movie` calls `player.login()` which prints at line 87 |
| `[Stream] Now playing: The Matrix` | 158 -> 91 | `watch_movie` calls `player.play()` which prints at line 91 |
| `[Stream] Playback stopped` | 168 -> 95 | `end_movie` calls `player.stop()` which prints at line 95 |
| `[Stream] Netflix Streaming Player shutting down` | 169 -> 83 | `end_movie` calls `player.turn_off()` which prints at line 83 |
| `[Audio] Sonos Sound System powering OFF` | 170 -> 54 | `end_movie` calls `sound.turn_off()` which prints at line 54 |
| `[TV] Samsung Television is turning OFF` | 171 -> 25 | `end_movie` calls `tv.turn_off()` which prints at line 25 |
| `[Lights] Living Room lights turned ON (100%)` | 172 -> 116 | `end_movie` calls `lights.on()` which prints at line 116 |

---

## Key Characteristics of Facade Pattern in Rust

### 1. **Composition Over Inheritance**
The facade uses composition (lines 127-130), owning instances of each subsystem. This is idiomatic Rust and provides clear ownership semantics.

### 2. **Encapsulation**
Subsystems are private to the facade struct. Clients cannot access `Television`, `SoundSystem`, etc. directly - they must use the facade's simplified methods.

### 3. **Single Responsibility**
Each subsystem handles only its own concerns. The facade's responsibility is coordination, not implementation of actual functionality.

### 4. **No Trait Required**
Unlike some patterns (Strategy, Observer), Facade doesn't require a trait definition. The pattern is structural, not behavioral.

### 5. **Reduces Dependencies**
Client code only depends on `HomeTheaterFacade`. Changes to subsystem internals don't affect clients as long as the facade interface remains stable.

### 6. **Optional Access**
While this example hides subsystems completely, facades can optionally expose subsystems for clients who need fine-grained control:
```rust
impl HomeTheaterFacade {
    fn get_sound_system(&self) -> &SoundSystem {
        &self.sound
    }
}
```

### 7. **Memory Safety**
Rust's ownership system ensures the facade owns its subsystems, preventing dangling references and use-after-free bugs that can occur in C++ facade implementations.

---

## Build and Run

```bash
# Compile
rustc main_facade.rs -o main_facade.exe

# Run
./main_facade.exe
```

No external dependencies required. Compatible with Rust stable (1.0+).
