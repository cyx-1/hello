# Bridge Design Pattern in Rust

The Bridge pattern is a structural design pattern that separates an abstraction from its implementation so that the two can vary independently. This is particularly useful when you want to avoid a permanent binding between an abstraction and its implementation.

In this example, we demonstrate the pattern using a remote control (abstraction) and electronic devices (implementation). The remote control can work with any device that implements the `Device` trait, and we can create different types of remotes without modifying the device implementations.

## Source Code

```rust
  1  // Bridge Design Pattern in Rust
  2  // Separates abstraction from implementation so both can vary independently
  3
  4  use std::cell::RefCell;
  5
  6  // Implementation trait - defines the interface for implementation classes
  7  trait Device {
  8      fn is_enabled(&self) -> bool;
  9      fn enable(&mut self);
 10      fn disable(&mut self);
 11      fn get_volume(&self) -> u32;
 12      fn set_volume(&mut self, volume: u32);
 13      fn get_channel(&self) -> u32;
 14      fn set_channel(&mut self, channel: u32);
 15      fn get_name(&self) -> &str;
 16  }
 17
 18  // Concrete Implementation A - TV
 19  struct TV {
 20      enabled: bool,
 21      volume: u32,
 22      channel: u32,
 23  }
 24
 25  impl TV {
 26      fn new() -> Self {
 27          println!("[TV] Creating new TV device");
 28          TV {
 29              enabled: false,
 30              volume: 30,
 31              channel: 1,
 32          }
 33      }
 34  }
 35
 36  impl Device for TV {
 37      fn is_enabled(&self) -> bool {
 38          self.enabled
 39      }
 40
 41      fn enable(&mut self) {
 42          self.enabled = true;
 43          println!("[TV] Device enabled");
 44      }
 45
 46      fn disable(&mut self) {
 47          self.enabled = false;
 48          println!("[TV] Device disabled");
 49      }
 50
 51      fn get_volume(&self) -> u32 {
 52          self.volume
 53      }
 54
 55      fn set_volume(&mut self, volume: u32) {
 56          self.volume = volume.min(100);
 57          println!("[TV] Volume set to {}", self.volume);
 58      }
 59
 60      fn get_channel(&self) -> u32 {
 61          self.channel
 62      }
 63
 64      fn set_channel(&mut self, channel: u32) {
 65          self.channel = channel;
 66          println!("[TV] Channel set to {}", self.channel);
 67      }
 68
 69      fn get_name(&self) -> &str {
 70          "TV"
 71      }
 72  }
 73
 74  // Concrete Implementation B - Radio
 75  struct Radio {
 76      enabled: bool,
 77      volume: u32,
 78      channel: u32,
 79  }
 80
 81  impl Radio {
 82      fn new() -> Self {
 83          println!("[Radio] Creating new Radio device");
 84          Radio {
 85              enabled: false,
 86              volume: 20,
 87              channel: 88,
 88          }
 89      }
 90  }
 91
 92  impl Device for Radio {
 93      fn is_enabled(&self) -> bool {
 94          self.enabled
 95      }
 96
 97      fn enable(&mut self) {
 98          self.enabled = true;
 99          println!("[Radio] Device enabled");
100      }
101
102      fn disable(&mut self) {
103          self.enabled = false;
104          println!("[Radio] Device disabled");
105      }
106
107      fn get_volume(&self) -> u32 {
108          self.volume
109      }
110
111      fn set_volume(&mut self, volume: u32) {
112          self.volume = volume.min(100);
113          println!("[Radio] Volume set to {}", self.volume);
114      }
115
116      fn get_channel(&self) -> u32 {
117          self.channel
118      }
119
120      fn set_channel(&mut self, channel: u32) {
121          self.channel = channel;
122          println!("[Radio] Station set to {} FM", self.channel);
123      }
124
125      fn get_name(&self) -> &str {
126          "Radio"
127      }
128  }
129
130  // Abstraction - holds a reference to the implementation
131  struct RemoteControl {
132      device: RefCell<Box<dyn Device>>,
133  }
134
135  impl RemoteControl {
136      fn new(device: Box<dyn Device>) -> Self {
137          println!("Creating RemoteControl for {}", device.get_name());
138          RemoteControl {
139              device: RefCell::new(device),
140          }
141      }
142
143      fn toggle_power(&self) {
144          let mut device = self.device.borrow_mut();
145          if device.is_enabled() {
146              device.disable();
147          } else {
148              device.enable();
149          }
150      }
151
152      fn volume_up(&self) {
153          let mut device = self.device.borrow_mut();
154          let current = device.get_volume();
155          device.set_volume(current + 10);
156      }
157
158      fn volume_down(&self) {
159          let mut device = self.device.borrow_mut();
160          let current = device.get_volume();
161          if current >= 10 {
162              device.set_volume(current - 10);
163          } else {
164              device.set_volume(0);
165          }
166      }
167
168      fn channel_up(&self) {
169          let mut device = self.device.borrow_mut();
170          let current = device.get_channel();
171          device.set_channel(current + 1);
172      }
173
174      fn channel_down(&self) {
175          let mut device = self.device.borrow_mut();
176          let current = device.get_channel();
177          if current > 1 {
178              device.set_channel(current - 1);
179          }
180      }
181
182      fn get_device_name(&self) -> String {
183          self.device.borrow().get_name().to_string()
184      }
185  }
186
187  // Refined Abstraction - extends the base abstraction with additional features
188  struct AdvancedRemoteControl {
189      base: RemoteControl,
190  }
191
192  impl AdvancedRemoteControl {
193      fn new(device: Box<dyn Device>) -> Self {
194          println!("Creating AdvancedRemoteControl for {}", device.get_name());
195          AdvancedRemoteControl {
196              base: RemoteControl {
197                  device: RefCell::new(device),
198              },
199          }
200      }
201
202      fn toggle_power(&self) {
203          self.base.toggle_power();
204      }
205
206      fn volume_up(&self) {
207          self.base.volume_up();
208      }
209
210      fn volume_down(&self) {
211          self.base.volume_down();
212      }
213
214      fn mute(&self) {
215          let mut device = self.base.device.borrow_mut();
216          println!("[{}] Muting device", device.get_name());
217          device.set_volume(0);
218      }
219
220      fn set_channel_direct(&self, channel: u32) {
221          let mut device = self.base.device.borrow_mut();
222          println!("[{}] Setting channel directly to {}", device.get_name(), channel);
223          device.set_channel(channel);
224      }
225
226      fn get_device_name(&self) -> String {
227          self.base.get_device_name()
228      }
229  }
230
231  fn main() {
232      println!("=== Bridge Design Pattern Demo ===\n");
233
234      // Demo 1: Basic RemoteControl with TV
235      println!("--- Demo 1: Basic RemoteControl with TV ---");
236      let tv = Box::new(TV::new());
237      let tv_remote = RemoteControl::new(tv);
238
239      println!("\nOperating {} with basic remote:", tv_remote.get_device_name());
240      tv_remote.toggle_power();
241      tv_remote.volume_up();
242      tv_remote.volume_up();
243      tv_remote.channel_up();
244      tv_remote.toggle_power();
245
246      // Demo 2: Basic RemoteControl with Radio
247      println!("\n--- Demo 2: Basic RemoteControl with Radio ---");
248      let radio = Box::new(Radio::new());
249      let radio_remote = RemoteControl::new(radio);
250
251      println!("\nOperating {} with basic remote:", radio_remote.get_device_name());
252      radio_remote.toggle_power();
253      radio_remote.volume_up();
254      radio_remote.channel_up();
255      radio_remote.channel_up();
256
257      // Demo 3: AdvancedRemoteControl with TV
258      println!("\n--- Demo 3: AdvancedRemoteControl with TV ---");
259      let tv2 = Box::new(TV::new());
260      let advanced_remote = AdvancedRemoteControl::new(tv2);
261
262      println!("\nOperating {} with advanced remote:", advanced_remote.get_device_name());
263      advanced_remote.toggle_power();
264      advanced_remote.volume_up();
265      advanced_remote.set_channel_direct(42);
266      advanced_remote.mute();
267      advanced_remote.toggle_power();
268
269      // Demo 4: AdvancedRemoteControl with Radio
270      println!("\n--- Demo 4: AdvancedRemoteControl with Radio ---");
271      let radio2 = Box::new(Radio::new());
272      let advanced_radio_remote = AdvancedRemoteControl::new(radio2);
273
274      println!("\nOperating {} with advanced remote:", advanced_radio_remote.get_device_name());
275      advanced_radio_remote.toggle_power();
276      advanced_radio_remote.set_channel_direct(101);
277      advanced_radio_remote.volume_up();
278      advanced_radio_remote.mute();
279
280      println!("\n=== Bridge Pattern Demo Complete ===");
281  }
```

## Program Output

```
=== Bridge Design Pattern Demo ===

--- Demo 1: Basic RemoteControl with TV ---
[TV] Creating new TV device
Creating RemoteControl for TV

Operating TV with basic remote:
[TV] Device enabled
[TV] Volume set to 40
[TV] Volume set to 50
[TV] Channel set to 2
[TV] Device disabled

--- Demo 2: Basic RemoteControl with Radio ---
[Radio] Creating new Radio device
Creating RemoteControl for Radio

Operating Radio with basic remote:
[Radio] Device enabled
[Radio] Volume set to 30
[Radio] Station set to 89 FM
[Radio] Station set to 90 FM

--- Demo 3: AdvancedRemoteControl with TV ---
[TV] Creating new TV device
Creating AdvancedRemoteControl for TV

Operating TV with advanced remote:
[TV] Device enabled
[TV] Volume set to 40
[TV] Setting channel directly to 42
[TV] Channel set to 42
[TV] Muting device
[TV] Volume set to 0
[TV] Device disabled

--- Demo 4: AdvancedRemoteControl with Radio ---
[Radio] Creating new Radio device
Creating AdvancedRemoteControl for Radio

Operating Radio with advanced remote:
[Radio] Device enabled
[Radio] Setting channel directly to 101
[Radio] Station set to 101 FM
[Radio] Volume set to 30
[Radio] Muting device
[Radio] Volume set to 0

=== Bridge Pattern Demo Complete ===
```

## Code Annotations

### Key Sections Explained

**Lines 7-16: Implementation Trait (Device)**
The `Device` trait defines the implementation interface that all concrete devices must follow. This is the "Implementation" side of the Bridge pattern. It declares methods for power control, volume, and channel management.

**Lines 18-72: Concrete Implementation A (TV)**
The `TV` struct is a concrete implementation of the `Device` trait. It maintains its own state (enabled, volume, channel) and provides TV-specific behavior in its method implementations. Note the default volume of 30 and channel 1 (lines 30-31).

**Lines 74-128: Concrete Implementation B (Radio)**
The `Radio` struct is another concrete implementation with its own behavior. It differs from TV in its output messages (e.g., "Station set to X FM" vs "Channel set to X") and default values (volume 20, channel 88 for FM).

**Lines 130-185: Abstraction (RemoteControl)**
The `RemoteControl` struct is the abstraction that bridges to any device implementation. Key points:
- Line 132: Uses `RefCell<Box<dyn Device>>` to hold a trait object, enabling runtime polymorphism and interior mutability
- Lines 143-150: `toggle_power()` demonstrates how the abstraction uses the implementation's methods
- The abstraction provides higher-level operations (volume_up/down, channel_up/down) built on the implementation's primitives

**Lines 187-229: Refined Abstraction (AdvancedRemoteControl)**
Extends the base abstraction with additional features:
- Line 189: Contains the base `RemoteControl` (composition over inheritance)
- Lines 214-218: `mute()` - new feature that sets volume to 0
- Lines 220-224: `set_channel_direct()` - new feature for direct channel input
- Demonstrates how abstractions can be extended without affecting implementations

**Lines 231-281: Main Function Demos**
Four demonstrations showing different abstraction-implementation combinations:
- Demo 1 (lines 234-244): Basic remote with TV
- Demo 2 (lines 246-255): Basic remote with Radio
- Demo 3 (lines 257-267): Advanced remote with TV
- Demo 4 (lines 269-278): Advanced remote with Radio

### Output to Source Code Correlation

| Output Line | Source Line(s) | Description |
|-------------|----------------|-------------|
| `[TV] Creating new TV device` | 27 | TV constructor prints device creation |
| `Creating RemoteControl for TV` | 137 | RemoteControl constructor identifies device |
| `[TV] Device enabled` | 43 | TV's enable() method called via toggle_power() |
| `[TV] Volume set to 40` | 57 | set_volume() called by volume_up() (30+10=40) |
| `[TV] Volume set to 50` | 57 | Second volume_up() call (40+10=50) |
| `[TV] Channel set to 2` | 66 | set_channel() via channel_up() (1+1=2) |
| `[TV] Device disabled` | 48 | TV's disable() via toggle_power() |
| `[Radio] Creating new Radio device` | 83 | Radio constructor |
| `[Radio] Volume set to 30` | 113 | Radio volume_up (20+10=30) |
| `[Radio] Station set to 89 FM` | 122 | Radio-specific channel message (88+1=89) |
| `Creating AdvancedRemoteControl for TV` | 194 | Advanced remote identifies device |
| `[TV] Setting channel directly to 42` | 222 | AdvancedRemote's set_channel_direct() |
| `[TV] Muting device` | 216 | AdvancedRemote's mute() feature |
| `[TV] Volume set to 0` | 57 | mute() sets volume to 0 |

### Key Characteristics of Bridge Pattern in Rust

1. **Trait Objects for Implementation**: Using `Box<dyn Device>` enables runtime polymorphism, allowing any type implementing `Device` to be used with the same abstraction.

2. **Interior Mutability with RefCell**: Since Rust's ownership rules prevent direct mutation through shared references, `RefCell<Box<dyn Device>>` provides interior mutability, allowing the abstraction to mutate the implementation at runtime.

3. **Composition over Inheritance**: Rust doesn't have classical inheritance. The `AdvancedRemoteControl` composes a `RemoteControl` rather than extending it, which is more idiomatic in Rust.

4. **Separation of Concerns**: The pattern cleanly separates what the abstraction does (RemoteControl operations) from how it's done (Device-specific implementations).

5. **Open/Closed Principle**: New devices can be added by implementing the `Device` trait, and new remotes can be created by composing `RemoteControl` - all without modifying existing code.

6. **No Unsafe Code Required**: The entire pattern is implemented using safe Rust, demonstrating that complex patterns can be expressed within Rust's safety guarantees.

### When to Use This Pattern

- When you want to avoid permanent binding between abstraction and implementation
- When both abstractions and implementations should be extensible independently
- When changes in the implementation should not affect client code
- When you want to share an implementation among multiple objects
