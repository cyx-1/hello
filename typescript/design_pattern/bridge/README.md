# Bridge Design Pattern - TypeScript Implementation

## Pattern Description

The **Bridge** design pattern is a structural pattern that separates an abstraction from its implementation so that both can vary independently. This pattern is particularly useful when:

- You want to avoid a permanent binding between an abstraction and its implementation
- Both the abstractions and their implementations should be extensible through subclassing
- Changes in the implementation should not impact the client code
- You want to share an implementation among multiple objects

### Key Components

1. **Abstraction**: Defines the abstraction's interface and maintains a reference to an object of type Implementor
2. **Refined Abstraction**: Extends the interface defined by Abstraction
3. **Implementor**: Defines the interface for implementation classes
4. **Concrete Implementor**: Implements the Implementor interface

### Real-World Example

This implementation demonstrates the Bridge pattern using:
- **Abstractions**: `RemoteControl` and `AdvancedRemoteControl`
- **Implementations**: `TV` and `Radio` devices

This allows any remote control type to work with any device type without creating separate classes for each combination.

---

## Requirements

- **Node.js**: 18.0 or higher
- **TypeScript**: 5.3 or higher
- **npm**: 8.0 or higher

---

## How to Run

```bash
# Navigate to the bridge pattern directory
cd typescript/bridge

# Install dependencies
npm install

# Run the program
npm run start
```

---

## Source Code

```typescript
     1	/**
     2	 * Bridge Design Pattern - TypeScript Implementation
     3	 *
     4	 * The Bridge pattern separates an abstraction from its implementation
     5	 * so that both can vary independently. This example demonstrates
     6	 * remote controls (abstraction) operating different devices (implementation).
     7	 */
     8
     9	// =============================================================================
    10	// Implementation Interface - Device
    11	// =============================================================================
    12
    13	/**
    14	 * The Implementation interface declares methods common to all concrete
    15	 * implementation classes. It doesn't have to match the Abstraction's interface.
    16	 */
    17	interface Device {
    18	  isEnabled(): boolean;
    19	  enable(): void;
    20	  disable(): void;
    21	  getVolume(): number;
    22	  setVolume(volume: number): void;
    23	  getChannel(): number;
    24	  setChannel(channel: number): void;
    25	  getName(): string;
    26	}
    27
    28	// =============================================================================
    29	// Concrete Implementations - TV and Radio
    30	// =============================================================================
    31
    32	/**
    33	 * TV - A concrete implementation of the Device interface
    34	 */
    35	class TV implements Device {
    36	  private enabled: boolean = false;
    37	  private volume: number = 30;
    38	  private channel: number = 1;
    39
    40	  isEnabled(): boolean {
    41	    return this.enabled;
    42	  }
    43
    44	  enable(): void {
    45	    this.enabled = true;
    46	    console.log("[Line 42] TV: Powered ON");
    47	  }
    48
    49	  disable(): void {
    50	    this.enabled = false;
    51	    console.log("[Line 47] TV: Powered OFF");
    52	  }
    53
    54	  getVolume(): number {
    55	    return this.volume;
    56	  }
    57
    58	  setVolume(volume: number): void {
    59	    if (volume > 100) {
    60	      this.volume = 100;
    61	    } else if (volume < 0) {
    62	      this.volume = 0;
    63	    } else {
    64	      this.volume = volume;
    65	    }
    66	    console.log(`[Line 62] TV: Volume set to ${this.volume}`);
    67	  }
    68
    69	  getChannel(): number {
    70	    return this.channel;
    71	  }
    72
    73	  setChannel(channel: number): void {
    74	    this.channel = channel;
    75	    console.log(`[Line 70] TV: Channel set to ${this.channel}`);
    76	  }
    77
    78	  getName(): string {
    79	    return "TV";
    80	  }
    81	}
    82
    83	/**
    84	 * Radio - Another concrete implementation of the Device interface
    85	 */
    86	class Radio implements Device {
    87	  private enabled: boolean = false;
    88	  private volume: number = 20;
    89	  private channel: number = 88;
    90
    91	  isEnabled(): boolean {
    92	    return this.enabled;
    93	  }
    94
    95	  enable(): void {
    96	    this.enabled = true;
    97	    console.log("[Line 92] Radio: Powered ON");
    98	  }
    99
   100	  disable(): void {
   101	    this.enabled = false;
   102	    console.log("[Line 97] Radio: Powered OFF");
   103	  }
   104
   105	  getVolume(): number {
   106	    return this.volume;
   107	  }
   108
   109	  setVolume(volume: number): void {
   110	    if (volume > 100) {
   111	      this.volume = 100;
   112	    } else if (volume < 0) {
   113	      this.volume = 0;
   114	    } else {
   115	      this.volume = volume;
   116	    }
   117	    console.log(`[Line 112] Radio: Volume set to ${this.volume}`);
   118	  }
   119
   120	  getChannel(): number {
   121	    return this.channel;
   122	  }
   123
   124	  setChannel(channel: number): void {
   125	    this.channel = channel;
   126	    console.log(`[Line 120] Radio: Station set to ${this.channel} FM`);
   127	  }
   128
   129	  getName(): string {
   130	    return "Radio";
   131	  }
   132	}
   133
   134	// =============================================================================
   135	// Abstraction - RemoteControl
   136	// =============================================================================
   137
   138	/**
   139	 * The Abstraction defines the interface for the "control" part of the two
   140	 * class hierarchies. It maintains a reference to an object of the
   141	 * Implementation hierarchy and delegates all real work to this object.
   142	 */
   143	class RemoteControl {
   144	  protected device: Device;
   145
   146	  constructor(device: Device) {
   147	    this.device = device;
   148	    console.log(`[Line 142] RemoteControl: Created for ${device.getName()}`);
   149	  }
   150
   151	  togglePower(): void {
   152	    console.log(`[Line 146] RemoteControl: Toggle power button pressed`);
   153	    if (this.device.isEnabled()) {
   154	      this.device.disable();
   155	    } else {
   156	      this.device.enable();
   157	    }
   158	  }
   159
   160	  volumeDown(): void {
   161	    console.log(`[Line 155] RemoteControl: Volume down button pressed`);
   162	    this.device.setVolume(this.device.getVolume() - 10);
   163	  }
   164
   165	  volumeUp(): void {
   166	    console.log(`[Line 160] RemoteControl: Volume up button pressed`);
   167	    this.device.setVolume(this.device.getVolume() + 10);
   168	  }
   169
   170	  channelDown(): void {
   171	    console.log(`[Line 165] RemoteControl: Channel down button pressed`);
   172	    this.device.setChannel(this.device.getChannel() - 1);
   173	  }
   174
   175	  channelUp(): void {
   176	    console.log(`[Line 170] RemoteControl: Channel up button pressed`);
   177	    this.device.setChannel(this.device.getChannel() + 1);
   178	  }
   179
   180	  getStatus(): void {
   181	    console.log(`[Line 175] RemoteControl: Status - ${this.device.getName()} is ${this.device.isEnabled() ? "ON" : "OFF"}, Volume: ${this.device.getVolume()}, Channel: ${this.device.getChannel()}`);
   182	  }
   183	}
   184
   185	// =============================================================================
   186	// Refined Abstraction - AdvancedRemoteControl
   187	// =============================================================================
   188
   189	/**
   190	 * AdvancedRemoteControl extends the basic RemoteControl with additional features.
   191	 * This demonstrates that abstractions can be extended without affecting implementations.
   192	 */
   193	class AdvancedRemoteControl extends RemoteControl {
   194	  constructor(device: Device) {
   195	    super(device);
   196	    console.log(`[Line 191] AdvancedRemoteControl: Enhanced features enabled`);
   197	  }
   198
   199	  mute(): void {
   200	    console.log(`[Line 195] AdvancedRemoteControl: Mute button pressed`);
   201	    this.device.setVolume(0);
   202	  }
   203
   204	  setVolumeLevel(level: number): void {
   205	    console.log(`[Line 200] AdvancedRemoteControl: Setting exact volume to ${level}`);
   206	    this.device.setVolume(level);
   207	  }
   208
   209	  jumpToChannel(channel: number): void {
   210	    console.log(`[Line 205] AdvancedRemoteControl: Jumping to channel ${channel}`);
   211	    this.device.setChannel(channel);
   212	  }
   213
   214	  printDetailedStatus(): void {
   215	    const status = this.device.isEnabled() ? "ON" : "OFF";
   216	    console.log(`[Line 211] AdvancedRemoteControl: Detailed Status Report`);
   217	    console.log(`[Line 212]   - Device: ${this.device.getName()}`);
   218	    console.log(`[Line 213]   - Power: ${status}`);
   219	    console.log(`[Line 214]   - Volume: ${this.device.getVolume()}%`);
   220	    console.log(`[Line 215]   - Channel: ${this.device.getChannel()}`);
   221	  }
   222	}
   223
   224	// =============================================================================
   225	// Client Code - Demonstration
   226	// =============================================================================
   227
   228	function clientCode(): void {
   229	  console.log("=".repeat(60));
   230	  console.log("[Line 223] Bridge Pattern Demonstration");
   231	  console.log("=".repeat(60));
   232	  console.log();
   233
   234	  // Scenario 1: Basic Remote with TV
   235	  console.log("[Line 227] --- Scenario 1: Basic Remote with TV ---");
   236	  const tv = new TV();
   237	  const tvRemote = new RemoteControl(tv);
   238
   239	  tvRemote.togglePower();
   240	  tvRemote.volumeUp();
   241	  tvRemote.volumeUp();
   242	  tvRemote.channelUp();
   243	  tvRemote.getStatus();
   244	  tvRemote.togglePower();
   245	  console.log();
   246
   247	  // Scenario 2: Basic Remote with Radio
   248	  console.log("[Line 239] --- Scenario 2: Basic Remote with Radio ---");
   249	  const radio = new Radio();
   250	  const radioRemote = new RemoteControl(radio);
   251
   252	  radioRemote.togglePower();
   253	  radioRemote.volumeUp();
   254	  radioRemote.channelUp();
   255	  radioRemote.getStatus();
   256	  radioRemote.togglePower();
   257	  console.log();
   258
   259	  // Scenario 3: Advanced Remote with TV
   260	  console.log("[Line 250] --- Scenario 3: Advanced Remote with TV ---");
   261	  const tv2 = new TV();
   262	  const advancedTvRemote = new AdvancedRemoteControl(tv2);
   263
   264	  advancedTvRemote.togglePower();
   265	  advancedTvRemote.setVolumeLevel(75);
   266	  advancedTvRemote.jumpToChannel(42);
   267	  advancedTvRemote.printDetailedStatus();
   268	  advancedTvRemote.mute();
   269	  advancedTvRemote.printDetailedStatus();
   270	  console.log();
   271
   272	  // Scenario 4: Advanced Remote with Radio
   273	  console.log("[Line 262] --- Scenario 4: Advanced Remote with Radio ---");
   274	  const radio2 = new Radio();
   275	  const advancedRadioRemote = new AdvancedRemoteControl(radio2);
   276
   277	  advancedRadioRemote.togglePower();
   278	  advancedRadioRemote.setVolumeLevel(50);
   279	  advancedRadioRemote.jumpToChannel(101);
   280	  advancedRadioRemote.printDetailedStatus();
   281	  console.log();
   282
   283	  console.log("=".repeat(60));
   284	  console.log("[Line 272] Bridge Pattern Demonstration Complete");
   285	  console.log("=".repeat(60));
   286	}
   287
   288	// Run the demonstration
   289	clientCode();
```

---

## Program Output

```
============================================================
[Line 223] Bridge Pattern Demonstration
============================================================

[Line 227] --- Scenario 1: Basic Remote with TV ---
[Line 142] RemoteControl: Created for TV
[Line 146] RemoteControl: Toggle power button pressed
[Line 42] TV: Powered ON
[Line 160] RemoteControl: Volume up button pressed
[Line 62] TV: Volume set to 40
[Line 160] RemoteControl: Volume up button pressed
[Line 62] TV: Volume set to 50
[Line 170] RemoteControl: Channel up button pressed
[Line 70] TV: Channel set to 2
[Line 175] RemoteControl: Status - TV is ON, Volume: 50, Channel: 2
[Line 146] RemoteControl: Toggle power button pressed
[Line 47] TV: Powered OFF

[Line 239] --- Scenario 2: Basic Remote with Radio ---
[Line 142] RemoteControl: Created for Radio
[Line 146] RemoteControl: Toggle power button pressed
[Line 92] Radio: Powered ON
[Line 160] RemoteControl: Volume up button pressed
[Line 112] Radio: Volume set to 30
[Line 170] RemoteControl: Channel up button pressed
[Line 120] Radio: Station set to 89 FM
[Line 175] RemoteControl: Status - Radio is ON, Volume: 30, Channel: 89
[Line 146] RemoteControl: Toggle power button pressed
[Line 97] Radio: Powered OFF

[Line 250] --- Scenario 3: Advanced Remote with TV ---
[Line 142] RemoteControl: Created for TV
[Line 191] AdvancedRemoteControl: Enhanced features enabled
[Line 146] RemoteControl: Toggle power button pressed
[Line 42] TV: Powered ON
[Line 200] AdvancedRemoteControl: Setting exact volume to 75
[Line 62] TV: Volume set to 75
[Line 205] AdvancedRemoteControl: Jumping to channel 42
[Line 70] TV: Channel set to 42
[Line 211] AdvancedRemoteControl: Detailed Status Report
[Line 212]   - Device: TV
[Line 213]   - Power: ON
[Line 214]   - Volume: 75%
[Line 215]   - Channel: 42
[Line 195] AdvancedRemoteControl: Mute button pressed
[Line 62] TV: Volume set to 0
[Line 211] AdvancedRemoteControl: Detailed Status Report
[Line 212]   - Device: TV
[Line 213]   - Power: ON
[Line 214]   - Volume: 0%
[Line 215]   - Channel: 42

[Line 262] --- Scenario 4: Advanced Remote with Radio ---
[Line 142] RemoteControl: Created for Radio
[Line 191] AdvancedRemoteControl: Enhanced features enabled
[Line 146] RemoteControl: Toggle power button pressed
[Line 92] Radio: Powered ON
[Line 200] AdvancedRemoteControl: Setting exact volume to 50
[Line 112] Radio: Volume set to 50
[Line 205] AdvancedRemoteControl: Jumping to channel 101
[Line 120] Radio: Station set to 101 FM
[Line 211] AdvancedRemoteControl: Detailed Status Report
[Line 212]   - Device: Radio
[Line 213]   - Power: ON
[Line 214]   - Volume: 50%
[Line 215]   - Channel: 101

============================================================
[Line 272] Bridge Pattern Demonstration Complete
============================================================
```

---

## Code Analysis and Annotations

### Pattern Structure Overview

| Component | Class | Role |
|-----------|-------|------|
| Implementor Interface | `Device` (Lines 17-26) | Defines the interface for all devices |
| Concrete Implementor A | `TV` (Lines 35-81) | TV-specific implementation |
| Concrete Implementor B | `Radio` (Lines 86-132) | Radio-specific implementation |
| Abstraction | `RemoteControl` (Lines 143-183) | Basic remote control interface |
| Refined Abstraction | `AdvancedRemoteControl` (Lines 193-222) | Extended remote with additional features |

---

### Scenario 1: Basic Remote with TV

| Output Line Reference | Source Line | Description |
|-----------------------|-------------|-------------|
| `[Line 142] RemoteControl: Created for TV` | 148 | RemoteControl constructor stores the TV device reference |
| `[Line 146] RemoteControl: Toggle power button pressed` | 152 | Abstraction receives user command |
| `[Line 42] TV: Powered ON` | 46 | Implementation (TV) executes the actual power-on logic |
| `[Line 160] RemoteControl: Volume up button pressed` | 166 | Abstraction receives volume up command |
| `[Line 62] TV: Volume set to 40` | 66 | TV increases volume from 30 to 40 (first press) |
| `[Line 62] TV: Volume set to 50` | 66 | TV increases volume from 40 to 50 (second press) |
| `[Line 170] RemoteControl: Channel up button pressed` | 176 | Abstraction receives channel up command |
| `[Line 70] TV: Channel set to 2` | 75 | TV changes from channel 1 to channel 2 |
| `[Line 175] RemoteControl: Status...` | 181 | Abstraction queries implementation state and reports |
| `[Line 47] TV: Powered OFF` | 51 | Implementation executes power-off logic |

**Key Insight**: The RemoteControl abstraction delegates all device-specific operations to the TV implementation. The abstraction only knows about the Device interface, not the concrete TV class.

---

### Scenario 2: Basic Remote with Radio

| Output Line Reference | Source Line | Description |
|-----------------------|-------------|-------------|
| `[Line 142] RemoteControl: Created for Radio` | 148 | Same RemoteControl class now works with Radio |
| `[Line 92] Radio: Powered ON` | 97 | Radio's power-on implementation (different from TV) |
| `[Line 112] Radio: Volume set to 30` | 117 | Radio starts at volume 20, increases to 30 |
| `[Line 120] Radio: Station set to 89 FM` | 126 | Radio shows FM frequency instead of TV channel |
| `[Line 97] Radio: Powered OFF` | 102 | Radio's power-off implementation |

**Key Insight**: The same RemoteControl class works with both TV and Radio without modification. This demonstrates the Bridge pattern's power - the abstraction (remote) is completely decoupled from the implementation (device).

---

### Scenario 3: Advanced Remote with TV

| Output Line Reference | Source Line | Description |
|-----------------------|-------------|-------------|
| `[Line 191] AdvancedRemoteControl: Enhanced features enabled` | 196 | Refined abstraction adds new capabilities |
| `[Line 200] AdvancedRemoteControl: Setting exact volume to 75` | 205 | New feature: direct volume control |
| `[Line 205] AdvancedRemoteControl: Jumping to channel 42` | 210 | New feature: direct channel jump |
| `[Line 211-215] Detailed Status Report` | 216-220 | New feature: detailed device status |
| `[Line 195] AdvancedRemoteControl: Mute button pressed` | 200 | New feature: one-touch mute |

**Key Insight**: AdvancedRemoteControl extends the abstraction hierarchy without changing the implementation hierarchy. The TV class remains unchanged while we add new control features.

---

### Scenario 4: Advanced Remote with Radio

| Output Line Reference | Source Line | Description |
|-----------------------|-------------|-------------|
| `[Line 142] + [Line 191]` | 148, 196 | Both parent and child constructors execute |
| `[Line 120] Radio: Station set to 101 FM` | 126 | Advanced remote's jumpToChannel works with Radio |
| `[Line 212-215] Device: Radio, Volume: 50%, Channel: 101` | 217-220 | Same status method shows Radio-specific data |

**Key Insight**: The AdvancedRemoteControl works seamlessly with Radio, demonstrating that both hierarchies (abstraction and implementation) can be extended independently.

---

### Bridge Pattern Benefits Demonstrated

| Benefit | How It's Shown in This Example |
|---------|--------------------------------|
| **Decoupling** | RemoteControl doesn't know if it's controlling TV or Radio |
| **Single Responsibility** | Abstractions handle user interface; implementations handle device logic |
| **Open/Closed Principle** | New devices (e.g., SmartSpeaker) can be added without changing remotes |
| **Extensibility** | AdvancedRemoteControl adds features without modifying TV or Radio |
| **Composition over Inheritance** | RemoteControl composes Device rather than extending it |

---

### Without Bridge Pattern (Problem)

If we didn't use the Bridge pattern, we'd need:
- `TVRemoteControl`
- `RadioRemoteControl`
- `AdvancedTVRemoteControl`
- `AdvancedRadioRemoteControl`
- ... and more for each new device!

This creates a **class explosion** problem: M abstractions x N implementations = M*N classes.

### With Bridge Pattern (Solution)

- 2 abstraction classes (RemoteControl, AdvancedRemoteControl)
- 2 implementation classes (TV, Radio)
- Total: **4 classes** instead of 4+ classes

Adding a new device requires only 1 new class, not rewriting all remotes.

---

## Version Requirements

This code requires:
- **TypeScript 5.3+**: For modern type inference and strict mode support
- **Node.js 18+**: For ES2020 module support and modern JavaScript features
- **@types/node 20+**: For console and process type definitions
