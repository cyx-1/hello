# Facade Design Pattern in TypeScript

The Facade pattern provides a simplified interface to a complex subsystem. It hides the complexity of the subsystem and provides a single unified interface that is easier to use for clients. This is particularly useful when working with complex libraries, frameworks, or systems with many interdependent components.

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
2    * Facade Design Pattern in TypeScript
3    *
4    * The Facade pattern provides a simplified interface to a complex subsystem.
5    * It hides the complexity of the subsystem and provides a single unified
6    * interface that is easier to use for clients.
7    */
8
9   // ============================================================
10  // Subsystem Classes - Complex components that the Facade simplifies
11  // ============================================================
12
13  // Subsystem 1: Television
14  class Television {
15      private isOn: boolean = false;
16      private channel: number = 1;
17
18      on(): void {
19          this.isOn = true;
20          console.log("[Line 18] Television: Powering on");
21      }
22
23      off(): void {
24          this.isOn = false;
25          console.log("[Line 23] Television: Powering off");
26      }
27
28      setInputChannel(channel: number): void {
29          this.channel = channel;
30          console.log(`[Line 28] Television: Setting input channel to ${channel}`);
31      }
32  }
33
34  // Subsystem 2: Sound System
35  class SoundSystem {
36      private volume: number = 0;
37      private surroundMode: boolean = false;
38
39      on(): void {
40          console.log("[Line 37] SoundSystem: Powering on amplifier");
41      }
42
43      off(): void {
44          console.log("[Line 41] SoundSystem: Powering off amplifier");
45      }
46
47      setVolume(level: number): void {
48          this.volume = level;
49          console.log(`[Line 46] SoundSystem: Setting volume to ${level}`);
50      }
51
52      setSurroundSound(enabled: boolean): void {
53          this.surroundMode = enabled;
54          const mode = enabled ? "surround" : "stereo";
55          console.log(`[Line 52] SoundSystem: Setting audio mode to ${mode}`);
56      }
57  }
58
59  // Subsystem 3: Streaming Player
60  class StreamingPlayer {
61      private currentMovie: string = "";
62
63      on(): void {
64          console.log("[Line 60] StreamingPlayer: Starting streaming device");
65      }
66
67      off(): void {
68          console.log("[Line 64] StreamingPlayer: Shutting down streaming device");
69      }
70
71      play(movie: string): void {
72          this.currentMovie = movie;
73          console.log(`[Line 69] StreamingPlayer: Playing "${movie}"`);
74      }
75
76      pause(): void {
77          console.log(`[Line 73] StreamingPlayer: Pausing "${this.currentMovie}"`);
78      }
79
80      stop(): void {
81          console.log(`[Line 77] StreamingPlayer: Stopping "${this.currentMovie}"`);
82          this.currentMovie = "";
83      }
84  }
85
86  // Subsystem 4: Room Lights
87  class RoomLights {
88      private brightness: number = 100;
89
90      on(): void {
91          this.brightness = 100;
92          console.log("[Line 87] RoomLights: Turning lights on");
93      }
94
95      off(): void {
96          this.brightness = 0;
97          console.log("[Line 92] RoomLights: Turning lights off");
98      }
99
100     dim(level: number): void {
101         this.brightness = level;
102         console.log(`[Line 97] RoomLights: Dimming lights to ${level}%`);
103     }
104 }
105
106 // Subsystem 5: Popcorn Machine
107 class PopcornMachine {
108     on(): void {
109         console.log("[Line 104] PopcornMachine: Turning on popcorn machine");
110     }
111
112     off(): void {
113         console.log("[Line 108] PopcornMachine: Turning off popcorn machine");
114     }
115
116     pop(): void {
117         console.log("[Line 112] PopcornMachine: Popping popcorn!");
118     }
119 }
120
121 // ============================================================
122 // Facade Class - Provides simplified interface to the subsystems
123 // ============================================================
124
125 class HomeTheaterFacade {
126     private tv: Television;
127     private soundSystem: SoundSystem;
128     private streamingPlayer: StreamingPlayer;
129     private lights: RoomLights;
130     private popcorn: PopcornMachine;
131
132     constructor(
133         tv: Television,
134         soundSystem: SoundSystem,
135         streamingPlayer: StreamingPlayer,
136         lights: RoomLights,
137         popcorn: PopcornMachine
138     ) {
139         this.tv = tv;
140         this.soundSystem = soundSystem;
141         this.streamingPlayer = streamingPlayer;
142         this.lights = lights;
143         this.popcorn = popcorn;
144         console.log("[Line 136] HomeTheaterFacade: Home theater system initialized");
145     }
146
147     // Simplified method to start watching a movie
148     watchMovie(movie: string): void {
149         console.log(`\n[Line 141] HomeTheaterFacade: Preparing to watch "${movie}"...`);
150         console.log("----------------------------------------");
151
152         this.popcorn.on();
153         this.popcorn.pop();
154         this.lights.dim(10);
155         this.tv.on();
156         this.tv.setInputChannel(3);
157         this.soundSystem.on();
158         this.soundSystem.setVolume(25);
159         this.soundSystem.setSurroundSound(true);
160         this.streamingPlayer.on();
161         this.streamingPlayer.play(movie);
162
163         console.log("----------------------------------------");
164         console.log(`[Line 156] HomeTheaterFacade: Enjoy your movie!`);
165     }
166
167     // Simplified method to pause the movie
168     pauseMovie(): void {
169         console.log("\n[Line 161] HomeTheaterFacade: Pausing movie...");
170         this.streamingPlayer.pause();
171         this.lights.dim(50);
172     }
173
174     // Simplified method to end movie watching
175     endMovie(): void {
176         console.log("\n[Line 168] HomeTheaterFacade: Shutting down home theater...");
177         console.log("----------------------------------------");
178
179         this.streamingPlayer.stop();
180         this.streamingPlayer.off();
181         this.soundSystem.off();
182         this.tv.off();
183         this.lights.on();
184         this.popcorn.off();
185
186         console.log("----------------------------------------");
187         console.log("[Line 179] HomeTheaterFacade: Home theater shutdown complete");
188     }
189 }
```

## Program Output

```
=== Facade Pattern Demonstration ===

--- Home Theater Facade Demo ---
[Line 136] HomeTheaterFacade: Home theater system initialized

[Line 141] HomeTheaterFacade: Preparing to watch "The Matrix"...
----------------------------------------
[Line 104] PopcornMachine: Turning on popcorn machine
[Line 112] PopcornMachine: Popping popcorn!
[Line 97] RoomLights: Dimming lights to 10%
[Line 18] Television: Powering on
[Line 28] Television: Setting input channel to 3
[Line 37] SoundSystem: Powering on amplifier
[Line 46] SoundSystem: Setting volume to 25
[Line 52] SoundSystem: Setting audio mode to surround
[Line 60] StreamingPlayer: Starting streaming device
[Line 69] StreamingPlayer: Playing "The Matrix"
----------------------------------------
[Line 156] HomeTheaterFacade: Enjoy your movie!

[Line 161] HomeTheaterFacade: Pausing movie...
[Line 73] StreamingPlayer: Pausing "The Matrix"
[Line 97] RoomLights: Dimming lights to 50%

[Line 168] HomeTheaterFacade: Shutting down home theater...
----------------------------------------
[Line 77] StreamingPlayer: Stopping "The Matrix"
[Line 64] StreamingPlayer: Shutting down streaming device
[Line 41] SoundSystem: Powering off amplifier
[Line 23] Television: Powering off
[Line 87] RoomLights: Turning lights on
[Line 108] PopcornMachine: Turning off popcorn machine
----------------------------------------
[Line 179] HomeTheaterFacade: Home theater shutdown complete

[Line 184] HomeTheaterFacade: Setting up music mode...
----------------------------------------
[Line 97] RoomLights: Dimming lights to 60%
[Line 37] SoundSystem: Powering on amplifier
[Line 46] SoundSystem: Setting volume to 15
[Line 52] SoundSystem: Setting audio mode to stereo
----------------------------------------
[Line 193] HomeTheaterFacade: Music mode ready

[Line 198] HomeTheaterFacade: Ending music mode...
[Line 41] SoundSystem: Powering off amplifier
[Line 87] RoomLights: Turning lights on
[Line 201] HomeTheaterFacade: Music mode ended


--- Computer Startup Facade Demo ---
[Line 250] ComputerFacade: Computer components initialized

[Line 254] ComputerFacade: Starting computer...
----------------------------------------
[Line 212] CPU: Freezing processor
[Line 235] HardDrive: Reading 1024 bytes from sector 0
[Line 227] Memory: Loading "BootData[sector:0,size:1024]" at address 0
[Line 216] CPU: Jumping to address 0
[Line 220] CPU: Executing instructions
----------------------------------------
[Line 264] ComputerFacade: Computer started successfully

[Line 268] ComputerFacade: Shutting down computer...
[Line 269] ComputerFacade: Saving state and powering off


--- Without Facade (Direct Subsystem Control) ---
[Line 318] Direct control requires managing each subsystem:

Manually setting up movie (verbose and error-prone):
[Line 104] PopcornMachine: Turning on popcorn machine
[Line 112] PopcornMachine: Popping popcorn!
[Line 97] RoomLights: Dimming lights to 10%
[Line 18] Television: Powering on
[Line 28] Television: Setting input channel to 3
[Line 37] SoundSystem: Powering on amplifier
[Line 46] SoundSystem: Setting volume to 25
[Line 52] SoundSystem: Setting audio mode to surround
[Line 60] StreamingPlayer: Starting streaming device
[Line 69] StreamingPlayer: Playing "Inception"

[Line 338] Notice how the facade simplifies all of this!
         With facade: homeTheater.watchMovie('Inception')
         Without facade: 10+ individual method calls

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Pattern Components

#### Subsystem Classes (Lines 14-119)
- Individual components with their own complex interfaces
- **Television**: Power control, channel selection
- **SoundSystem**: Volume, surround sound modes
- **StreamingPlayer**: Play, pause, stop functionality
- **RoomLights**: On, off, dimming
- **PopcornMachine**: On, off, popping

#### Facade Class (Lines 125-188)
- Wraps all subsystem instances
- Provides high-level operations: `watchMovie()`, `pauseMovie()`, `endMovie()`
- Coordinates subsystems in the correct order
- Hides complexity from clients

### Output Correlation - watchMovie() Operation

| Output | Source Line | Subsystem | Purpose |
|--------|-------------|-----------|---------|
| `Preparing to watch "The Matrix"...` | Line 141 | Facade | Announces operation start |
| `Turning on popcorn machine` | Line 104 | PopcornMachine | Prepare snacks first |
| `Popping popcorn!` | Line 112 | PopcornMachine | Make popcorn while other systems start |
| `Dimming lights to 10%` | Line 97 | RoomLights | Create theater atmosphere |
| `Powering on` | Line 18 | Television | Turn on display |
| `Setting input channel to 3` | Line 28 | Television | Select streaming input |
| `Powering on amplifier` | Line 37 | SoundSystem | Enable audio |
| `Setting volume to 25` | Line 46 | SoundSystem | Set comfortable volume |
| `Setting audio mode to surround` | Line 52 | SoundSystem | Enable immersive audio |
| `Starting streaming device` | Line 60 | StreamingPlayer | Initialize player |
| `Playing "The Matrix"` | Line 69 | StreamingPlayer | Start the movie |
| `Enjoy your movie!` | Line 156 | Facade | Confirms setup complete |

### Output Correlation - endMovie() Operation

| Output | Source Line | Subsystem | Purpose |
|--------|-------------|-----------|---------|
| `Shutting down home theater...` | Line 168 | Facade | Announces shutdown |
| `Stopping "The Matrix"` | Line 77 | StreamingPlayer | Stop playback |
| `Shutting down streaming device` | Line 64 | StreamingPlayer | Turn off player |
| `Powering off amplifier` | Line 41 | SoundSystem | Disable audio |
| `Powering off` | Line 23 | Television | Turn off display |
| `Turning lights on` | Line 87 | RoomLights | Restore room lighting |
| `Turning off popcorn machine` | Line 108 | PopcornMachine | Final cleanup |
| `Home theater shutdown complete` | Line 179 | Facade | Confirms shutdown |

### Computer Startup Facade Correlation

| Output | Source Line | Subsystem | Purpose |
|--------|-------------|-----------|---------|
| `Freezing processor` | Line 212 | CPU | Halt current operations |
| `Reading 1024 bytes from sector 0` | Line 235 | HardDrive | Load boot sector |
| `Loading "BootData..." at address 0` | Line 227 | Memory | Store boot data in RAM |
| `Jumping to address 0` | Line 216 | CPU | Point to boot code |
| `Executing instructions` | Line 220 | CPU | Begin execution |

### Why Facade Works

1. **Simplification**: Complex multi-step operations become single method calls
   - `homeTheater.watchMovie("The Matrix")` replaces 10+ individual calls
   - `computer.start()` handles CPU, Memory, and HardDrive coordination

2. **Encapsulation**: Clients don't need to know subsystem details
   - No need to know correct order of operations
   - No need to understand individual component APIs

3. **Reduced Dependencies**: Client code only depends on the facade
   - Changes to subsystems don't affect client code
   - Easy to swap implementations

4. **Coordination**: Facade ensures correct sequence and configuration
   - Lights dim before movie starts
   - Popcorn machine starts early (takes time)
   - Components shut down in correct order

### Comparison: With vs Without Facade

#### With Facade (Lines 299-306)
```typescript
homeTheater.watchMovie("The Matrix");
homeTheater.pauseMovie();
homeTheater.endMovie();
```

#### Without Facade (Lines 318-336)
```typescript
manualPopcorn.on();
manualPopcorn.pop();
manualLights.dim(10);
manualTv.on();
manualTv.setInputChannel(3);
manualSound.on();
manualSound.setVolume(25);
manualSound.setSurroundSound(true);
manualPlayer.on();
manualPlayer.play("Inception");
// And similar complexity for pause and end...
```

### Use Cases

- **Complex Subsystem Integration**: Simplify access to libraries with many classes
- **Legacy System Wrapping**: Provide modern API for older code
- **Layer Separation**: Create clear boundaries between application layers
- **API Design**: Expose simplified interface to external clients
- **Testing**: Create facade that can be easily mocked
- **Configuration Management**: Centralize default settings for subsystems
