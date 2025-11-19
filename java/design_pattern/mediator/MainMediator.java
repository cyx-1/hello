/**
 * Comprehensive demonstration of the Mediator Pattern in Java
 *
 * The Mediator pattern defines an object that encapsulates how a set of objects
 * interact. It promotes loose coupling by keeping objects from referring to
 * each other explicitly.
 */

import java.util.ArrayList;
import java.util.List;

// Mediator interface
interface ChatMediator {
    void sendMessage(String message, User user);
    void addUser(User user);
}

// Concrete Mediator
class ChatRoom implements ChatMediator {
    private List<User> users = new ArrayList<>();

    @Override
    public void addUser(User user) {
        users.add(user);
        System.out.println("  [ChatRoom] " + user.getName() + " joined the chat");
    }

    @Override
    public void sendMessage(String message, User sender) {
        for (User user : users) {
            if (user != sender) {
                user.receive(message, sender.getName());
            }
        }
    }
}

// Colleague
abstract class User {
    protected ChatMediator mediator;
    protected String name;

    public User(ChatMediator mediator, String name) {
        this.mediator = mediator;
        this.name = name;
    }

    public String getName() { return name; }

    public abstract void send(String message);
    public abstract void receive(String message, String from);
}

// Concrete Colleagues
class ChatUser extends User {
    public ChatUser(ChatMediator mediator, String name) {
        super(mediator, name);
    }

    @Override
    public void send(String message) {
        System.out.println("  [" + name + "] Sending: " + message);
        mediator.sendMessage(message, this);
    }

    @Override
    public void receive(String message, String from) {
        System.out.println("  [" + name + "] Received from " + from + ": " + message);
    }
}

// Another example: Air Traffic Control

interface ATCMediator {
    void registerFlight(Flight flight);
    boolean requestLanding(Flight flight);
    void notifyDeparture(Flight flight);
}

class AirTrafficControl implements ATCMediator {
    private List<Flight> flights = new ArrayList<>();
    private boolean runwayFree = true;

    @Override
    public void registerFlight(Flight flight) {
        flights.add(flight);
        System.out.println("  [ATC] Registered flight: " + flight.getFlightNumber());
    }

    @Override
    public boolean requestLanding(Flight flight) {
        if (runwayFree) {
            runwayFree = false;
            System.out.println("  [ATC] " + flight.getFlightNumber() + " cleared for landing");
            return true;
        } else {
            System.out.println("  [ATC] " + flight.getFlightNumber() + " please hold, runway busy");
            return false;
        }
    }

    @Override
    public void notifyDeparture(Flight flight) {
        runwayFree = true;
        System.out.println("  [ATC] " + flight.getFlightNumber() + " has departed, runway is free");
        // Notify other waiting flights
        for (Flight f : flights) {
            if (f != flight && f.isWaiting()) {
                f.notifyRunwayFree();
            }
        }
    }
}

class Flight {
    private ATCMediator atc;
    private String flightNumber;
    private boolean waiting = false;

    public Flight(ATCMediator atc, String flightNumber) {
        this.atc = atc;
        this.flightNumber = flightNumber;
        atc.registerFlight(this);
    }

    public String getFlightNumber() { return flightNumber; }
    public boolean isWaiting() { return waiting; }

    public void requestLanding() {
        System.out.println("  [" + flightNumber + "] Requesting landing");
        if (!atc.requestLanding(this)) {
            waiting = true;
        }
    }

    public void notifyRunwayFree() {
        System.out.println("  [" + flightNumber + "] Notified runway is free, requesting landing");
        waiting = false;
        atc.requestLanding(this);
    }

    public void depart() {
        System.out.println("  [" + flightNumber + "] Taking off");
        atc.notifyDeparture(this);
    }
}

// Third example: Smart Home Mediator

interface SmartHomeMediator {
    void notify(SmartDevice sender, String event);
}

abstract class SmartDevice {
    protected SmartHomeMediator mediator;
    protected String name;

    public SmartDevice(SmartHomeMediator mediator, String name) {
        this.mediator = mediator;
        this.name = name;
    }

    public String getName() { return name; }
}

class SmartLight extends SmartDevice {
    private boolean on = false;

    public SmartLight(SmartHomeMediator mediator, String name) {
        super(mediator, name);
    }

    public void turnOn() {
        on = true;
        System.out.println("  [" + name + "] Light is ON");
        mediator.notify(this, "LIGHT_ON");
    }

    public void turnOff() {
        on = false;
        System.out.println("  [" + name + "] Light is OFF");
        mediator.notify(this, "LIGHT_OFF");
    }
}

class Thermostat extends SmartDevice {
    private int temperature = 70;

    public Thermostat(SmartHomeMediator mediator, String name) {
        super(mediator, name);
    }

    public void setTemperature(int temp) {
        temperature = temp;
        System.out.println("  [" + name + "] Temperature set to " + temp + "°F");
        mediator.notify(this, "TEMP_CHANGE");
    }

    public int getTemperature() { return temperature; }
}

class SecuritySystem extends SmartDevice {
    private boolean armed = false;

    public SecuritySystem(SmartHomeMediator mediator, String name) {
        super(mediator, name);
    }

    public void arm() {
        armed = true;
        System.out.println("  [" + name + "] Security system ARMED");
        mediator.notify(this, "SECURITY_ARMED");
    }

    public void disarm() {
        armed = false;
        System.out.println("  [" + name + "] Security system DISARMED");
        mediator.notify(this, "SECURITY_DISARMED");
    }
}

class CoffeeMaker extends SmartDevice {
    public CoffeeMaker(SmartHomeMediator mediator, String name) {
        super(mediator, name);
    }

    public void startBrewing() {
        System.out.println("  [" + name + "] Starting to brew coffee");
    }
}

class SmartHomeController implements SmartHomeMediator {
    private SmartLight light;
    private Thermostat thermostat;
    private SecuritySystem security;
    private CoffeeMaker coffeeMaker;

    public void setDevices(SmartLight light, Thermostat thermostat,
                          SecuritySystem security, CoffeeMaker coffeeMaker) {
        this.light = light;
        this.thermostat = thermostat;
        this.security = security;
        this.coffeeMaker = coffeeMaker;
    }

    @Override
    public void notify(SmartDevice sender, String event) {
        switch (event) {
            case "SECURITY_DISARMED":
                // When security is disarmed (someone came home)
                System.out.println("  [Controller] Welcome home! Adjusting settings...");
                light.turnOn();
                thermostat.setTemperature(72);
                coffeeMaker.startBrewing();
                break;

            case "SECURITY_ARMED":
                // When security is armed (leaving home)
                System.out.println("  [Controller] Goodbye! Saving energy...");
                light.turnOff();
                thermostat.setTemperature(65);
                break;
        }
    }
}

public class MainMediator {
    public static void main(String[] args) {
        System.out.println("=== Mediator Pattern Demonstration ===\n");

        // Chat room example
        System.out.println("--- 1. Chat Room Mediator ---");

        ChatMediator chatRoom = new ChatRoom();

        User alice = new ChatUser(chatRoom, "Alice");
        User bob = new ChatUser(chatRoom, "Bob");
        User charlie = new ChatUser(chatRoom, "Charlie");

        chatRoom.addUser(alice);
        chatRoom.addUser(bob);
        chatRoom.addUser(charlie);

        System.out.println();
        alice.send("Hello everyone!");
        System.out.println();
        bob.send("Hi Alice!");
        System.out.println();

        // Air Traffic Control example
        System.out.println("--- 2. Air Traffic Control Mediator ---");

        ATCMediator atc = new AirTrafficControl();

        Flight flight1 = new Flight(atc, "AA123");
        Flight flight2 = new Flight(atc, "UA456");
        Flight flight3 = new Flight(atc, "DL789");

        System.out.println();
        flight1.requestLanding();
        flight2.requestLanding();  // Will be put on hold
        flight3.requestLanding();  // Will be put on hold

        System.out.println();
        flight1.depart();  // Frees runway, notifies waiting flights
        System.out.println();

        // Smart Home example
        System.out.println("--- 3. Smart Home Mediator ---");

        SmartHomeController controller = new SmartHomeController();

        SmartLight light = new SmartLight(controller, "Living Room Light");
        Thermostat thermostat = new Thermostat(controller, "Main Thermostat");
        SecuritySystem security = new SecuritySystem(controller, "Home Security");
        CoffeeMaker coffeeMaker = new CoffeeMaker(controller, "Kitchen Coffee Maker");

        controller.setDevices(light, thermostat, security, coffeeMaker);

        System.out.println("\nComing home (disarming security):");
        security.disarm();

        System.out.println("\nLeaving home (arming security):");
        security.arm();

        System.out.println("\n=== Summary ===");
        System.out.println("Mediator pattern benefits:");
        System.out.println("  - Reduces coupling between colleagues");
        System.out.println("  - Centralizes complex communication logic");
        System.out.println("  - Simplifies object protocols");
        System.out.println("  - Easier to understand object interactions");
        System.out.println("\nConsiderations:");
        System.out.println("  - Mediator can become complex (God Object)");
        System.out.println("  - One-to-many becomes many-to-one");
    }
}
