# Mediator Design Pattern in TypeScript

The Mediator pattern defines an object that encapsulates how a set of objects interact. It promotes loose coupling by keeping objects from referring to each other explicitly, and lets you vary their interaction independently. Instead of components communicating directly, they communicate through a mediator, which coordinates their interactions.

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
2    * Mediator Design Pattern in TypeScript
3    *
4    * The Mediator pattern defines an object that encapsulates how a set of objects interact.
5    * It promotes loose coupling by keeping objects from referring to each other explicitly,
6    * and lets you vary their interaction independently.
7    */
8
9   // ============================================================
10  // Example 1: Chat Room (Classic Mediator Example)
11  // ============================================================
12
13  // Mediator Interface
14  interface ChatRoomMediator {
15      showMessage(user: User, message: string): void;
16      addUser(user: User): void;
17      sendPrivateMessage(from: User, to: string, message: string): void;
18  }
19
20  // Colleague - User class
21  class User {
22      private name: string;
23      private chatRoom: ChatRoomMediator;
24
25      constructor(name: string, chatRoom: ChatRoomMediator) {
26          this.name = name;
27          this.chatRoom = chatRoom;
28          this.chatRoom.addUser(this);
29          console.log(`[Line 27] User: ${name} joined the chat room`);
30      }
31
32      getName(): string {
33          return this.name;
34      }
35
36      send(message: string): void {
37          console.log(`[Line 34] ${this.name}: Sending message to chat room`);
38          this.chatRoom.showMessage(this, message);
39      }
40
41      sendPrivate(toUser: string, message: string): void {
42          console.log(`[Line 39] ${this.name}: Sending private message to ${toUser}`);
43          this.chatRoom.sendPrivateMessage(this, toUser, message);
44      }
45
46      receive(from: string, message: string): void {
47          console.log(`[Line 44] ${this.name}: Received from ${from} - "${message}"`);
48      }
49  }
50
51  // Concrete Mediator - ChatRoom
52  class ChatRoom implements ChatRoomMediator {
53      private users: Map<string, User> = new Map();
54
55      addUser(user: User): void {
56          this.users.set(user.getName(), user);
57          console.log(`[Line 54] ChatRoom: Registered user ${user.getName()}`);
58      }
59
60      showMessage(user: User, message: string): void {
61          const sender = user.getName();
62          const timestamp = new Date().toLocaleTimeString();
63          console.log(`[Line 60] ChatRoom: Broadcasting message from ${sender}`);
64
65          // Broadcast to all users except sender
66          this.users.forEach((recipient, name) => {
67              if (name !== sender) {
68                  console.log(`[Line 65]   -> Delivering to ${name}`);
69                  recipient.receive(sender, message);
70              }
71          });
72      }
73
74      sendPrivateMessage(from: User, toName: string, message: string): void {
75          const recipient = this.users.get(toName);
76          if (recipient) {
77              console.log(`[Line 74] ChatRoom: Routing private message from ${from.getName()} to ${toName}`);
78              recipient.receive(from.getName(), `[Private] ${message}`);
79          } else {
80              console.log(`[Line 77] ChatRoom: User ${toName} not found`);
81          }
82      }
83  }
84
85  // ============================================================
86  // Example 2: Air Traffic Control Tower
87  // ============================================================
88
89  // Mediator Interface for ATC
90  interface ATCMediator {
91      registerFlight(flight: Flight): void;
92      requestLanding(flight: Flight): boolean;
93      requestTakeoff(flight: Flight): boolean;
94      notifyFlights(message: string, excludeFlight?: Flight): void;
95  }
96
97  // Colleague - Flight class
98  class Flight {
99      private flightNumber: string;
100     private atc: ATCMediator;
101     private isOnGround: boolean;
102
103     constructor(flightNumber: string, atc: ATCMediator, onGround: boolean = false) {
104         this.flightNumber = flightNumber;
105         this.atc = atc;
106         this.isOnGround = onGround;
107         this.atc.registerFlight(this);
108         console.log(`[Line 102] Flight ${flightNumber}: Registered with ATC (${onGround ? 'on ground' : 'in air'})`);
109     }
110
111     getFlightNumber(): string {
112         return this.flightNumber;
113     }
114
115     getIsOnGround(): boolean {
116         return this.isOnGround;
117     }
118
119     setOnGround(value: boolean): void {
120         this.isOnGround = value;
121     }
122
123     requestLanding(): void {
124         console.log(`[Line 118] Flight ${this.flightNumber}: Requesting landing clearance`);
125         const approved = this.atc.requestLanding(this);
126         if (approved) {
127             console.log(`[Line 121] Flight ${this.flightNumber}: Landing approved, descending...`);
128             this.isOnGround = true;
129         } else {
130             console.log(`[Line 124] Flight ${this.flightNumber}: Landing denied, holding pattern`);
131         }
132     }
133
134     requestTakeoff(): void {
135         console.log(`[Line 129] Flight ${this.flightNumber}: Requesting takeoff clearance`);
136         const approved = this.atc.requestTakeoff(this);
137         if (approved) {
138             console.log(`[Line 132] Flight ${this.flightNumber}: Takeoff approved, ascending...`);
139             this.isOnGround = false;
140         } else {
141             console.log(`[Line 135] Flight ${this.flightNumber}: Takeoff denied, waiting at runway`);
142         }
143     }
144
145     receiveNotification(message: string): void {
146         console.log(`[Line 140] Flight ${this.flightNumber}: Received ATC notification - "${message}"`);
147     }
148 }
149
150 // Concrete Mediator - Control Tower
151 class ControlTower implements ATCMediator {
152     private flights: Map<string, Flight> = new Map();
153     private runwayAvailable: boolean = true;
154
155     registerFlight(flight: Flight): void {
156         this.flights.set(flight.getFlightNumber(), flight);
157         console.log(`[Line 151] ControlTower: Flight ${flight.getFlightNumber()} now under control`);
158     }
159
160     requestLanding(flight: Flight): boolean {
161         console.log(`[Line 155] ControlTower: Processing landing request from ${flight.getFlightNumber()}`);
162
163         if (!this.runwayAvailable) {
164             console.log(`[Line 158] ControlTower: Runway busy, denying landing for ${flight.getFlightNumber()}`);
165             return false;
166         }
167
168         this.runwayAvailable = false;
169         console.log(`[Line 163] ControlTower: Runway cleared for ${flight.getFlightNumber()} landing`);
170
171         // Notify other flights
172         this.notifyFlights(`Runway in use - ${flight.getFlightNumber()} landing`, flight);
173
174         // Simulate runway becoming available again
175         setTimeout(() => {
176             this.runwayAvailable = true;
177             console.log(`[Line 171] ControlTower: Runway now available`);
178         }, 0);
179
180         return true;
181     }
182
183     requestTakeoff(flight: Flight): boolean {
184         console.log(`[Line 178] ControlTower: Processing takeoff request from ${flight.getFlightNumber()}`);
185
186         if (!this.runwayAvailable) {
187             console.log(`[Line 181] ControlTower: Runway busy, denying takeoff for ${flight.getFlightNumber()}`);
188             return false;
189         }
190
191         if (!flight.getIsOnGround()) {
192             console.log(`[Line 186] ControlTower: ${flight.getFlightNumber()} is not on ground!`);
193             return false;
194         }
195
196         this.runwayAvailable = false;
197         console.log(`[Line 191] ControlTower: Runway cleared for ${flight.getFlightNumber()} takeoff`);
198
199         // Notify other flights
200         this.notifyFlights(`Runway in use - ${flight.getFlightNumber()} taking off`, flight);
201
202         // Simulate runway becoming available again
203         setTimeout(() => {
204             this.runwayAvailable = true;
205         }, 0);
206
207         return true;
208     }
209
210     notifyFlights(message: string, excludeFlight?: Flight): void {
211         console.log(`[Line 205] ControlTower: Broadcasting - "${message}"`);
212         this.flights.forEach((flight) => {
213             if (flight !== excludeFlight) {
214                 flight.receiveNotification(message);
215             }
216         });
217     }
218 }
219
220 // ============================================================
221 // Example 3: UI Dialog Components
222 // ============================================================
223
224 // Mediator Interface for Dialog
225 interface DialogMediator {
226     notify(sender: UIComponent, event: string): void;
227 }
228
229 // Abstract Colleague - UI Component
230 abstract class UIComponent {
231     protected dialog: DialogMediator;
232     protected name: string;
233
234     constructor(name: string, dialog: DialogMediator) {
235         this.name = name;
236         this.dialog = dialog;
237     }
238
239     getName(): string {
240         return this.name;
241     }
242 }
243
244 // Concrete Colleague - Checkbox
245 class Checkbox extends UIComponent {
246     private checked: boolean = false;
247
248     check(): void {
249         this.checked = true;
250         console.log(`[Line 240] Checkbox "${this.name}": Checked`);
251         this.dialog.notify(this, "check");
252     }
253
254     uncheck(): void {
255         this.checked = false;
256         console.log(`[Line 246] Checkbox "${this.name}": Unchecked`);
257         this.dialog.notify(this, "uncheck");
258     }
259
260     isChecked(): boolean {
261         return this.checked;
262     }
263 }
264
265 // Concrete Colleague - TextInput
266 class TextInput extends UIComponent {
267     private value: string = "";
268     private enabled: boolean = true;
269
270     setValue(value: string): void {
271         this.value = value;
272         console.log(`[Line 262] TextInput "${this.name}": Value set to "${value}"`);
273         this.dialog.notify(this, "input");
274     }
275
276     getValue(): string {
277         return this.value;
278     }
279
280     setEnabled(enabled: boolean): void {
281         this.enabled = enabled;
282         console.log(`[Line 272] TextInput "${this.name}": ${enabled ? 'Enabled' : 'Disabled'}`);
283     }
284
285     isEnabled(): boolean {
286         return this.enabled;
287     }
288 }
289
290 // Concrete Colleague - Button
291 class Button extends UIComponent {
292     private enabled: boolean = true;
293
294     click(): void {
295         if (this.enabled) {
296             console.log(`[Line 286] Button "${this.name}": Clicked`);
297             this.dialog.notify(this, "click");
298         } else {
299             console.log(`[Line 289] Button "${this.name}": Click ignored (disabled)`);
300         }
301     }
302
303     setEnabled(enabled: boolean): void {
304         this.enabled = enabled;
305         console.log(`[Line 295] Button "${this.name}": ${enabled ? 'Enabled' : 'Disabled'}`);
306     }
307 }
308
309 // Concrete Mediator - Registration Dialog
310 class RegistrationDialog implements DialogMediator {
311     private termsCheckbox: Checkbox;
312     private emailInput: TextInput;
313     private passwordInput: TextInput;
314     private submitButton: Button;
315
316     constructor() {
317         console.log("[Line 307] RegistrationDialog: Initializing components");
318         this.termsCheckbox = new Checkbox("Accept Terms", this);
319         this.emailInput = new TextInput("Email", this);
320         this.passwordInput = new TextInput("Password", this);
321         this.submitButton = new Button("Submit", this);
322
323         // Initial state
324         this.submitButton.setEnabled(false);
325         console.log("[Line 315] RegistrationDialog: Setup complete");
326     }
327
328     // ... getter methods ...
329
330     notify(sender: UIComponent, event: string): void {
331         console.log(`[Line 335] RegistrationDialog: Received "${event}" from "${sender.getName()}"`);
332
333         if (sender === this.termsCheckbox && event === "check") {
334             console.log("[Line 338] RegistrationDialog: Terms accepted, enabling inputs");
335             this.emailInput.setEnabled(true);
336             this.passwordInput.setEnabled(true);
337             this.validateForm();
338         }
339
340         if (sender === this.termsCheckbox && event === "uncheck") {
341             console.log("[Line 345] RegistrationDialog: Terms rejected, disabling form");
342             this.emailInput.setEnabled(false);
343             this.passwordInput.setEnabled(false);
344             this.submitButton.setEnabled(false);
345         }
346
347         if (sender === this.emailInput || sender === this.passwordInput) {
348             this.validateForm();
349         }
350
351         if (sender === this.submitButton && event === "click") {
352             console.log("[Line 356] RegistrationDialog: Form submitted!");
353             console.log(`[Line 357]   Email: ${this.emailInput.getValue()}`);
354             console.log(`[Line 358]   Password: ${"*".repeat(this.passwordInput.getValue().length)}`);
355         }
356     }
357
358     private validateForm(): void {
359         const isValid =
360             this.termsCheckbox.isChecked() &&
361             this.emailInput.getValue().length > 0 &&
362             this.passwordInput.getValue().length > 0;
363
364         console.log(`[Line 368] RegistrationDialog: Form validation - ${isValid ? 'valid' : 'invalid'}`);
365         this.submitButton.setEnabled(isValid);
366     }
367 }
```

## Program Output

```
=== Mediator Pattern Demonstration ===

--- Chat Room Demo ---

[Line 54] ChatRoom: Registered user Alice
[Line 27] User: Alice joined the chat room
[Line 54] ChatRoom: Registered user Bob
[Line 27] User: Bob joined the chat room
[Line 54] ChatRoom: Registered user Charlie
[Line 27] User: Charlie joined the chat room

[Line 34] Alice: Sending message to chat room
[Line 60] ChatRoom: Broadcasting message from Alice
[Line 65]   -> Delivering to Bob
[Line 44] Bob: Received from Alice - "Hello everyone!"
[Line 65]   -> Delivering to Charlie
[Line 44] Charlie: Received from Alice - "Hello everyone!"

[Line 39] Bob: Sending private message to Alice
[Line 74] ChatRoom: Routing private message from Bob to Alice
[Line 44] Alice: Received from Bob - "[Private] Hey Alice, how are you?"

[Line 34] Charlie: Sending message to chat room
[Line 60] ChatRoom: Broadcasting message from Charlie
[Line 65]   -> Delivering to Alice
[Line 44] Alice: Received from Charlie - "Good morning!"
[Line 65]   -> Delivering to Bob
[Line 44] Bob: Received from Charlie - "Good morning!"

[Line 39] Bob: Sending private message to Dave
[Line 77] ChatRoom: User Dave not found


--- Air Traffic Control Demo ---

[Line 151] ControlTower: Flight AA101 now under control
[Line 102] Flight AA101: Registered with ATC (in air)
[Line 151] ControlTower: Flight UA202 now under control
[Line 102] Flight UA202: Registered with ATC (on ground)
[Line 151] ControlTower: Flight DL303 now under control
[Line 102] Flight DL303: Registered with ATC (in air)

[Line 118] Flight AA101: Requesting landing clearance
[Line 155] ControlTower: Processing landing request from AA101
[Line 163] ControlTower: Runway cleared for AA101 landing
[Line 205] ControlTower: Broadcasting - "Runway in use - AA101 landing"
[Line 140] Flight UA202: Received ATC notification - "Runway in use - AA101 landing"
[Line 140] Flight DL303: Received ATC notification - "Runway in use - AA101 landing"
[Line 121] Flight AA101: Landing approved, descending...

[Line 118] Flight DL303: Requesting landing clearance
[Line 155] ControlTower: Processing landing request from DL303
[Line 158] ControlTower: Runway busy, denying landing for DL303
[Line 124] Flight DL303: Landing denied, holding pattern

[Line 129] Flight UA202: Requesting takeoff clearance
[Line 178] ControlTower: Processing takeoff request from UA202
[Line 181] ControlTower: Runway busy, denying takeoff for UA202
[Line 135] Flight UA202: Takeoff denied, waiting at runway


--- UI Dialog Demo ---

[Line 307] RegistrationDialog: Initializing components
[Line 295] Button "Submit": Disabled
[Line 315] RegistrationDialog: Setup complete

Trying to submit without accepting terms:
[Line 289] Button "Submit": Click ignored (disabled)

Accepting terms:
[Line 240] Checkbox "Accept Terms": Checked
[Line 335] RegistrationDialog: Received "check" from "Accept Terms"
[Line 338] RegistrationDialog: Terms accepted, enabling inputs
[Line 272] TextInput "Email": Enabled
[Line 272] TextInput "Password": Enabled
[Line 368] RegistrationDialog: Form validation - invalid
[Line 295] Button "Submit": Disabled

Filling in form:
[Line 262] TextInput "Email": Value set to "user@example.com"
[Line 335] RegistrationDialog: Received "input" from "Email"
[Line 368] RegistrationDialog: Form validation - invalid
[Line 295] Button "Submit": Disabled
[Line 262] TextInput "Password": Value set to "secret123"
[Line 335] RegistrationDialog: Received "input" from "Password"
[Line 368] RegistrationDialog: Form validation - valid
[Line 295] Button "Submit": Enabled

Submitting form:
[Line 286] Button "Submit": Clicked
[Line 335] RegistrationDialog: Received "click" from "Submit"
[Line 356] RegistrationDialog: Form submitted!
[Line 357]   Email: user@example.com
[Line 358]   Password: *********

Unchecking terms:
[Line 246] Checkbox "Accept Terms": Unchecked
[Line 335] RegistrationDialog: Received "uncheck" from "Accept Terms"
[Line 345] RegistrationDialog: Terms rejected, disabling form
[Line 272] TextInput "Email": Disabled
[Line 272] TextInput "Password": Disabled
[Line 295] Button "Submit": Disabled

Trying to submit after unchecking terms:
[Line 289] Button "Submit": Click ignored (disabled)

=== End of Demonstration ===
[Line 171] ControlTower: Runway now available
```

## Code Analysis and Annotations

### Pattern Components

#### Mediator Interface (Lines 14-18, 90-95, 225-227)
- Defines the communication protocol between colleagues
- `ChatRoomMediator` handles message broadcasting and private messaging
- `ATCMediator` manages runway access and flight notifications
- `DialogMediator` coordinates UI component interactions

#### Colleague Classes (Lines 21-48, 98-147, 230-306)
- Components that communicate through the mediator, not directly with each other
- `User` sends messages through ChatRoom
- `Flight` requests landing/takeoff through ControlTower
- `UIComponent` subclasses notify DialogMediator of state changes

#### Concrete Mediator (Lines 52-82, 151-217, 310-366)
- Implements the coordination logic
- `ChatRoom` routes messages to appropriate users
- `ControlTower` manages runway access and broadcasts notifications
- `RegistrationDialog` coordinates form validation and state

### Output Correlation

#### Chat Room Example

| Output | Source Line | Explanation |
|--------|-------------|-------------|
| `ChatRoom: Registered user Alice` | Line 54 | Mediator acknowledges user registration |
| `Alice: Sending message to chat room` | Line 34 | User delegates message delivery to mediator |
| `ChatRoom: Broadcasting message from Alice` | Line 60 | Mediator coordinates message distribution |
| `-> Delivering to Bob` | Line 65 | Mediator iterates through recipients |
| `Bob: Received from Alice` | Line 44 | Recipient receives through mediator |
| `ChatRoom: Routing private message` | Line 74 | Mediator handles point-to-point routing |
| `ChatRoom: User Dave not found` | Line 77 | Mediator handles error gracefully |

#### Air Traffic Control Example

| Output | Source Line | Explanation |
|--------|-------------|-------------|
| `ControlTower: Flight AA101 now under control` | Line 151 | Mediator tracks all flights |
| `Flight AA101: Requesting landing clearance` | Line 118 | Colleague requests action through mediator |
| `ControlTower: Processing landing request` | Line 155 | Mediator evaluates request |
| `ControlTower: Runway cleared for AA101` | Line 163 | Mediator grants access to shared resource |
| `ControlTower: Broadcasting` | Line 205 | Mediator notifies other flights |
| `Flight UA202: Received ATC notification` | Line 140 | Colleagues receive broadcasts |
| `ControlTower: Runway busy, denying` | Line 158/181 | Mediator prevents conflicts |

#### UI Dialog Example

| Output | Source Line | Explanation |
|--------|-------------|-------------|
| `RegistrationDialog: Initializing components` | Line 307 | Mediator creates and owns components |
| `Button "Submit": Disabled` | Line 295 | Mediator sets initial state |
| `Checkbox "Accept Terms": Checked` | Line 240 | Component notifies mediator of change |
| `RegistrationDialog: Received "check"` | Line 335 | Mediator receives notification |
| `Terms accepted, enabling inputs` | Line 338 | Mediator coordinates related components |
| `Form validation - valid/invalid` | Line 368 | Mediator evaluates overall state |
| `Form submitted!` | Line 356 | Mediator handles final action |

### Why Mediator Works

1. **Decoupling**: Components don't reference each other directly
   - Alice doesn't need to know about Bob or Charlie
   - Flight AA101 doesn't coordinate directly with UA202
   - Checkbox doesn't know about the Submit button

2. **Centralized Control**: Complex interactions are managed in one place
   - Chat message routing logic is in ChatRoom
   - Runway conflict resolution is in ControlTower
   - Form validation rules are in RegistrationDialog

3. **Single Responsibility**: Each component handles its own state
   - Users manage their name and receive messages
   - Flights track their position (ground/air)
   - UI components handle their enabled/value state

4. **Open/Closed Principle**: New colleagues can be added without changing existing ones
   - Add new User without modifying existing users
   - Add new Flight without changing other flights
   - Add new UI components without changing existing ones

### Key Interactions Demonstrated

#### Broadcast Communication (Chat Room)
```
User.send() -> ChatRoom.showMessage() -> [forEach User] User.receive()
```

#### Shared Resource Management (ATC)
```
Flight.requestLanding() -> ControlTower.requestLanding() -> check runway -> notify others
```

#### State Coordination (UI Dialog)
```
Checkbox.check() -> Dialog.notify() -> enable inputs -> validateForm() -> enable/disable button
```

### Use Cases

- **Chat Applications**: Message routing, user management, chat rooms
- **Traffic Control Systems**: Air traffic, train scheduling, resource allocation
- **UI Frameworks**: Form validation, dialog boxes, wizard workflows
- **Event Systems**: Event dispatching, publish-subscribe patterns
- **Workflow Engines**: Task coordination, process orchestration
- **Game Development**: Entity interaction, collision detection coordination
- **IoT Systems**: Device communication, sensor data aggregation
