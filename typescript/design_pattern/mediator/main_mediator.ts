/**
 * Mediator Design Pattern in TypeScript
 *
 * The Mediator pattern defines an object that encapsulates how a set of objects interact.
 * It promotes loose coupling by keeping objects from referring to each other explicitly,
 * and lets you vary their interaction independently.
 */

// ============================================================
// Example 1: Chat Room (Classic Mediator Example)
// ============================================================

// Mediator Interface
interface ChatRoomMediator {
    showMessage(user: User, message: string): void;
    addUser(user: User): void;
    sendPrivateMessage(from: User, to: string, message: string): void;
}

// Colleague - User class
class User {
    private name: string;
    private chatRoom: ChatRoomMediator;

    constructor(name: string, chatRoom: ChatRoomMediator) {
        this.name = name;
        this.chatRoom = chatRoom;
        this.chatRoom.addUser(this);
        console.log(`[Line 27] User: ${name} joined the chat room`);
    }

    getName(): string {
        return this.name;
    }

    send(message: string): void {
        console.log(`[Line 34] ${this.name}: Sending message to chat room`);
        this.chatRoom.showMessage(this, message);
    }

    sendPrivate(toUser: string, message: string): void {
        console.log(`[Line 39] ${this.name}: Sending private message to ${toUser}`);
        this.chatRoom.sendPrivateMessage(this, toUser, message);
    }

    receive(from: string, message: string): void {
        console.log(`[Line 44] ${this.name}: Received from ${from} - "${message}"`);
    }
}

// Concrete Mediator - ChatRoom
class ChatRoom implements ChatRoomMediator {
    private users: Map<string, User> = new Map();

    addUser(user: User): void {
        this.users.set(user.getName(), user);
        console.log(`[Line 54] ChatRoom: Registered user ${user.getName()}`);
    }

    showMessage(user: User, message: string): void {
        const sender = user.getName();
        const timestamp = new Date().toLocaleTimeString();
        console.log(`[Line 60] ChatRoom: Broadcasting message from ${sender}`);

        // Broadcast to all users except sender
        this.users.forEach((recipient, name) => {
            if (name !== sender) {
                console.log(`[Line 65]   -> Delivering to ${name}`);
                recipient.receive(sender, message);
            }
        });
    }

    sendPrivateMessage(from: User, toName: string, message: string): void {
        const recipient = this.users.get(toName);
        if (recipient) {
            console.log(`[Line 74] ChatRoom: Routing private message from ${from.getName()} to ${toName}`);
            recipient.receive(from.getName(), `[Private] ${message}`);
        } else {
            console.log(`[Line 77] ChatRoom: User ${toName} not found`);
        }
    }
}

// ============================================================
// Example 2: Air Traffic Control Tower
// ============================================================

// Mediator Interface for ATC
interface ATCMediator {
    registerFlight(flight: Flight): void;
    requestLanding(flight: Flight): boolean;
    requestTakeoff(flight: Flight): boolean;
    notifyFlights(message: string, excludeFlight?: Flight): void;
}

// Colleague - Flight class
class Flight {
    private flightNumber: string;
    private atc: ATCMediator;
    private isOnGround: boolean;

    constructor(flightNumber: string, atc: ATCMediator, onGround: boolean = false) {
        this.flightNumber = flightNumber;
        this.atc = atc;
        this.isOnGround = onGround;
        this.atc.registerFlight(this);
        console.log(`[Line 102] Flight ${flightNumber}: Registered with ATC (${onGround ? 'on ground' : 'in air'})`);
    }

    getFlightNumber(): string {
        return this.flightNumber;
    }

    getIsOnGround(): boolean {
        return this.isOnGround;
    }

    setOnGround(value: boolean): void {
        this.isOnGround = value;
    }

    requestLanding(): void {
        console.log(`[Line 118] Flight ${this.flightNumber}: Requesting landing clearance`);
        const approved = this.atc.requestLanding(this);
        if (approved) {
            console.log(`[Line 121] Flight ${this.flightNumber}: Landing approved, descending...`);
            this.isOnGround = true;
        } else {
            console.log(`[Line 124] Flight ${this.flightNumber}: Landing denied, holding pattern`);
        }
    }

    requestTakeoff(): void {
        console.log(`[Line 129] Flight ${this.flightNumber}: Requesting takeoff clearance`);
        const approved = this.atc.requestTakeoff(this);
        if (approved) {
            console.log(`[Line 132] Flight ${this.flightNumber}: Takeoff approved, ascending...`);
            this.isOnGround = false;
        } else {
            console.log(`[Line 135] Flight ${this.flightNumber}: Takeoff denied, waiting at runway`);
        }
    }

    receiveNotification(message: string): void {
        console.log(`[Line 140] Flight ${this.flightNumber}: Received ATC notification - "${message}"`);
    }
}

// Concrete Mediator - Control Tower
class ControlTower implements ATCMediator {
    private flights: Map<string, Flight> = new Map();
    private runwayAvailable: boolean = true;

    registerFlight(flight: Flight): void {
        this.flights.set(flight.getFlightNumber(), flight);
        console.log(`[Line 151] ControlTower: Flight ${flight.getFlightNumber()} now under control`);
    }

    requestLanding(flight: Flight): boolean {
        console.log(`[Line 155] ControlTower: Processing landing request from ${flight.getFlightNumber()}`);

        if (!this.runwayAvailable) {
            console.log(`[Line 158] ControlTower: Runway busy, denying landing for ${flight.getFlightNumber()}`);
            return false;
        }

        this.runwayAvailable = false;
        console.log(`[Line 163] ControlTower: Runway cleared for ${flight.getFlightNumber()} landing`);

        // Notify other flights
        this.notifyFlights(`Runway in use - ${flight.getFlightNumber()} landing`, flight);

        // Simulate runway becoming available again
        setTimeout(() => {
            this.runwayAvailable = true;
            console.log(`[Line 171] ControlTower: Runway now available`);
        }, 0);

        return true;
    }

    requestTakeoff(flight: Flight): boolean {
        console.log(`[Line 178] ControlTower: Processing takeoff request from ${flight.getFlightNumber()}`);

        if (!this.runwayAvailable) {
            console.log(`[Line 181] ControlTower: Runway busy, denying takeoff for ${flight.getFlightNumber()}`);
            return false;
        }

        if (!flight.getIsOnGround()) {
            console.log(`[Line 186] ControlTower: ${flight.getFlightNumber()} is not on ground!`);
            return false;
        }

        this.runwayAvailable = false;
        console.log(`[Line 191] ControlTower: Runway cleared for ${flight.getFlightNumber()} takeoff`);

        // Notify other flights
        this.notifyFlights(`Runway in use - ${flight.getFlightNumber()} taking off`, flight);

        // Simulate runway becoming available again
        setTimeout(() => {
            this.runwayAvailable = true;
        }, 0);

        return true;
    }

    notifyFlights(message: string, excludeFlight?: Flight): void {
        console.log(`[Line 205] ControlTower: Broadcasting - "${message}"`);
        this.flights.forEach((flight) => {
            if (flight !== excludeFlight) {
                flight.receiveNotification(message);
            }
        });
    }
}

// ============================================================
// Example 3: UI Dialog Components
// ============================================================

// Mediator Interface for Dialog
interface DialogMediator {
    notify(sender: UIComponent, event: string): void;
}

// Abstract Colleague - UI Component
abstract class UIComponent {
    protected dialog: DialogMediator;
    protected name: string;

    constructor(name: string, dialog: DialogMediator) {
        this.name = name;
        this.dialog = dialog;
    }

    getName(): string {
        return this.name;
    }
}

// Concrete Colleague - Checkbox
class Checkbox extends UIComponent {
    private checked: boolean = false;

    check(): void {
        this.checked = true;
        console.log(`[Line 240] Checkbox "${this.name}": Checked`);
        this.dialog.notify(this, "check");
    }

    uncheck(): void {
        this.checked = false;
        console.log(`[Line 246] Checkbox "${this.name}": Unchecked`);
        this.dialog.notify(this, "uncheck");
    }

    isChecked(): boolean {
        return this.checked;
    }
}

// Concrete Colleague - TextInput
class TextInput extends UIComponent {
    private value: string = "";
    private enabled: boolean = true;

    setValue(value: string): void {
        this.value = value;
        console.log(`[Line 262] TextInput "${this.name}": Value set to "${value}"`);
        this.dialog.notify(this, "input");
    }

    getValue(): string {
        return this.value;
    }

    setEnabled(enabled: boolean): void {
        this.enabled = enabled;
        console.log(`[Line 272] TextInput "${this.name}": ${enabled ? 'Enabled' : 'Disabled'}`);
    }

    isEnabled(): boolean {
        return this.enabled;
    }
}

// Concrete Colleague - Button
class Button extends UIComponent {
    private enabled: boolean = true;

    click(): void {
        if (this.enabled) {
            console.log(`[Line 286] Button "${this.name}": Clicked`);
            this.dialog.notify(this, "click");
        } else {
            console.log(`[Line 289] Button "${this.name}": Click ignored (disabled)`);
        }
    }

    setEnabled(enabled: boolean): void {
        this.enabled = enabled;
        console.log(`[Line 295] Button "${this.name}": ${enabled ? 'Enabled' : 'Disabled'}`);
    }
}

// Concrete Mediator - Registration Dialog
class RegistrationDialog implements DialogMediator {
    private termsCheckbox: Checkbox;
    private emailInput: TextInput;
    private passwordInput: TextInput;
    private submitButton: Button;

    constructor() {
        console.log("[Line 307] RegistrationDialog: Initializing components");
        this.termsCheckbox = new Checkbox("Accept Terms", this);
        this.emailInput = new TextInput("Email", this);
        this.passwordInput = new TextInput("Password", this);
        this.submitButton = new Button("Submit", this);

        // Initial state
        this.submitButton.setEnabled(false);
        console.log("[Line 315] RegistrationDialog: Setup complete");
    }

    getTermsCheckbox(): Checkbox {
        return this.termsCheckbox;
    }

    getEmailInput(): TextInput {
        return this.emailInput;
    }

    getPasswordInput(): TextInput {
        return this.passwordInput;
    }

    getSubmitButton(): Button {
        return this.submitButton;
    }

    notify(sender: UIComponent, event: string): void {
        console.log(`[Line 335] RegistrationDialog: Received "${event}" from "${sender.getName()}"`);

        if (sender === this.termsCheckbox && event === "check") {
            console.log("[Line 338] RegistrationDialog: Terms accepted, enabling inputs");
            this.emailInput.setEnabled(true);
            this.passwordInput.setEnabled(true);
            this.validateForm();
        }

        if (sender === this.termsCheckbox && event === "uncheck") {
            console.log("[Line 345] RegistrationDialog: Terms rejected, disabling form");
            this.emailInput.setEnabled(false);
            this.passwordInput.setEnabled(false);
            this.submitButton.setEnabled(false);
        }

        if (sender === this.emailInput || sender === this.passwordInput) {
            this.validateForm();
        }

        if (sender === this.submitButton && event === "click") {
            console.log("[Line 356] RegistrationDialog: Form submitted!");
            console.log(`[Line 357]   Email: ${this.emailInput.getValue()}`);
            console.log(`[Line 358]   Password: ${"*".repeat(this.passwordInput.getValue().length)}`);
        }
    }

    private validateForm(): void {
        const isValid =
            this.termsCheckbox.isChecked() &&
            this.emailInput.getValue().length > 0 &&
            this.passwordInput.getValue().length > 0;

        console.log(`[Line 368] RegistrationDialog: Form validation - ${isValid ? 'valid' : 'invalid'}`);
        this.submitButton.setEnabled(isValid);
    }
}

// Demonstration
function main(): void {
    console.log("=== Mediator Pattern Demonstration ===");

    // Demo 1: Chat Room
    console.log("\n--- Chat Room Demo ---\n");

    const chatRoom = new ChatRoom();

    const alice = new User("Alice", chatRoom);
    const bob = new User("Bob", chatRoom);
    const charlie = new User("Charlie", chatRoom);

    console.log("");
    alice.send("Hello everyone!");

    console.log("");
    bob.sendPrivate("Alice", "Hey Alice, how are you?");

    console.log("");
    charlie.send("Good morning!");

    console.log("");
    bob.sendPrivate("Dave", "Are you there?"); // User not found

    // Demo 2: Air Traffic Control
    console.log("\n\n--- Air Traffic Control Demo ---\n");

    const tower = new ControlTower();

    const flight101 = new Flight("AA101", tower, false); // In air
    const flight202 = new Flight("UA202", tower, true);  // On ground
    const flight303 = new Flight("DL303", tower, false); // In air

    console.log("");
    flight101.requestLanding();  // Should be approved

    console.log("");
    flight303.requestLanding();  // Should be denied (runway busy initially, then ok)

    console.log("");
    flight202.requestTakeoff();  // Should be approved

    // Demo 3: UI Dialog
    console.log("\n\n--- UI Dialog Demo ---\n");

    const dialog = new RegistrationDialog();

    console.log("\nTrying to submit without accepting terms:");
    dialog.getSubmitButton().click(); // Should be ignored

    console.log("\nAccepting terms:");
    dialog.getTermsCheckbox().check();

    console.log("\nFilling in form:");
    dialog.getEmailInput().setValue("user@example.com");
    dialog.getPasswordInput().setValue("secret123");

    console.log("\nSubmitting form:");
    dialog.getSubmitButton().click();

    console.log("\nUnchecking terms:");
    dialog.getTermsCheckbox().uncheck();

    console.log("\nTrying to submit after unchecking terms:");
    dialog.getSubmitButton().click();

    console.log("\n=== End of Demonstration ===");
}

main();
