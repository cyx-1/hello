/**
 * Comprehensive demonstration of the Facade Pattern in Java
 *
 * The Facade pattern provides a unified interface to a set of interfaces
 * in a subsystem. It defines a higher-level interface that makes the
 * subsystem easier to use.
 */

// Complex subsystem classes for Home Theater
class Amplifier {
    private String description;
    private int volume;

    public Amplifier(String description) {
        this.description = description;
    }

    public void on() {
        System.out.println("  [Amplifier] " + description + " is ON");
    }

    public void off() {
        System.out.println("  [Amplifier] " + description + " is OFF");
    }

    public void setVolume(int level) {
        this.volume = level;
        System.out.println("  [Amplifier] Setting volume to " + level);
    }

    public void setSurroundSound() {
        System.out.println("  [Amplifier] Surround sound enabled");
    }

    public void setStereoSound() {
        System.out.println("  [Amplifier] Stereo mode enabled");
    }
}

class DVDPlayer {
    private String description;
    private String currentMovie;

    public DVDPlayer(String description) {
        this.description = description;
    }

    public void on() {
        System.out.println("  [DVDPlayer] " + description + " is ON");
    }

    public void off() {
        System.out.println("  [DVDPlayer] " + description + " is OFF");
    }

    public void play(String movie) {
        this.currentMovie = movie;
        System.out.println("  [DVDPlayer] Playing \"" + movie + "\"");
    }

    public void stop() {
        System.out.println("  [DVDPlayer] Stopped \"" + currentMovie + "\"");
    }

    public void pause() {
        System.out.println("  [DVDPlayer] Paused \"" + currentMovie + "\"");
    }

    public void eject() {
        System.out.println("  [DVDPlayer] Ejecting disc");
    }
}

class Projector {
    private String description;

    public Projector(String description) {
        this.description = description;
    }

    public void on() {
        System.out.println("  [Projector] " + description + " is ON");
    }

    public void off() {
        System.out.println("  [Projector] " + description + " is OFF");
    }

    public void wideScreenMode() {
        System.out.println("  [Projector] Widescreen mode (16:9)");
    }

    public void tvMode() {
        System.out.println("  [Projector] TV mode (4:3)");
    }
}

class TheaterLights {
    private String description;

    public TheaterLights(String description) {
        this.description = description;
    }

    public void on() {
        System.out.println("  [Lights] " + description + " ON");
    }

    public void off() {
        System.out.println("  [Lights] " + description + " OFF");
    }

    public void dim(int level) {
        System.out.println("  [Lights] Dimming to " + level + "%");
    }
}

class Screen {
    private String description;

    public Screen(String description) {
        this.description = description;
    }

    public void up() {
        System.out.println("  [Screen] " + description + " going up");
    }

    public void down() {
        System.out.println("  [Screen] " + description + " going down");
    }
}

class PopcornMachine {
    private String description;

    public PopcornMachine(String description) {
        this.description = description;
    }

    public void on() {
        System.out.println("  [Popcorn] " + description + " is ON");
    }

    public void off() {
        System.out.println("  [Popcorn] " + description + " is OFF");
    }

    public void pop() {
        System.out.println("  [Popcorn] Popping popcorn!");
    }
}

// FACADE - simplifies the complex subsystem
class HomeTheaterFacade {
    private Amplifier amp;
    private DVDPlayer dvd;
    private Projector projector;
    private TheaterLights lights;
    private Screen screen;
    private PopcornMachine popcorn;

    public HomeTheaterFacade(Amplifier amp, DVDPlayer dvd, Projector projector,
                             TheaterLights lights, Screen screen, PopcornMachine popcorn) {
        this.amp = amp;
        this.dvd = dvd;
        this.projector = projector;
        this.lights = lights;
        this.screen = screen;
        this.popcorn = popcorn;
    }

    public void watchMovie(String movie) {
        System.out.println("Get ready to watch a movie...\n");
        popcorn.on();
        popcorn.pop();
        lights.dim(10);
        screen.down();
        projector.on();
        projector.wideScreenMode();
        amp.on();
        amp.setSurroundSound();
        amp.setVolume(5);
        dvd.on();
        dvd.play(movie);
    }

    public void endMovie() {
        System.out.println("\nShutting movie theater down...\n");
        popcorn.off();
        lights.on();
        screen.up();
        projector.off();
        amp.off();
        dvd.stop();
        dvd.eject();
        dvd.off();
    }

    public void listenToMusic(String track) {
        System.out.println("Setting up for music...\n");
        lights.dim(50);
        amp.on();
        amp.setStereoSound();
        amp.setVolume(8);
        System.out.println("  Playing track: " + track);
    }
}

// Another example: Computer startup

class CPU {
    public void freeze() {
        System.out.println("  [CPU] Freezing processor");
    }

    public void jump(long position) {
        System.out.println("  [CPU] Jumping to position " + position);
    }

    public void execute() {
        System.out.println("  [CPU] Executing instructions");
    }
}

class Memory {
    public void load(long position, byte[] data) {
        System.out.println("  [Memory] Loading data at position " + position);
    }
}

class HardDrive {
    public byte[] read(long lba, int size) {
        System.out.println("  [HardDrive] Reading " + size + " bytes from sector " + lba);
        return new byte[size];
    }
}

// Computer Facade
class ComputerFacade {
    private static final long BOOT_ADDRESS = 0x0000;
    private static final long BOOT_SECTOR = 0;
    private static final int SECTOR_SIZE = 512;

    private CPU cpu;
    private Memory memory;
    private HardDrive hardDrive;

    public ComputerFacade() {
        this.cpu = new CPU();
        this.memory = new Memory();
        this.hardDrive = new HardDrive();
    }

    public void start() {
        System.out.println("Starting computer...\n");
        cpu.freeze();
        byte[] bootData = hardDrive.read(BOOT_SECTOR, SECTOR_SIZE);
        memory.load(BOOT_ADDRESS, bootData);
        cpu.jump(BOOT_ADDRESS);
        cpu.execute();
        System.out.println("\n  Computer started successfully!");
    }
}

// Third example: Order processing

class Inventory {
    public boolean checkStock(String productId) {
        System.out.println("  [Inventory] Checking stock for " + productId);
        return true; // Simplified
    }

    public void updateStock(String productId, int quantity) {
        System.out.println("  [Inventory] Updating stock: " + productId + " -" + quantity);
    }
}

class Payment {
    public boolean processPayment(String orderId, double amount) {
        System.out.println("  [Payment] Processing $" + String.format("%.2f", amount) + " for order " + orderId);
        return true; // Simplified
    }

    public void refund(String orderId) {
        System.out.println("  [Payment] Refunding order " + orderId);
    }
}

class Shipping {
    public String createShipment(String orderId, String address) {
        System.out.println("  [Shipping] Creating shipment for " + orderId + " to " + address);
        return "TRACK-" + orderId;
    }

    public void cancelShipment(String trackingId) {
        System.out.println("  [Shipping] Cancelling shipment " + trackingId);
    }
}

class Notification {
    public void sendOrderConfirmation(String email, String orderId) {
        System.out.println("  [Notification] Sending confirmation to " + email + " for " + orderId);
    }

    public void sendShippingUpdate(String email, String trackingId) {
        System.out.println("  [Notification] Sending shipping update to " + email + ": " + trackingId);
    }
}

// Order Facade
class OrderFacade {
    private Inventory inventory;
    private Payment payment;
    private Shipping shipping;
    private Notification notification;

    public OrderFacade() {
        this.inventory = new Inventory();
        this.payment = new Payment();
        this.shipping = new Shipping();
        this.notification = new Notification();
    }

    public boolean placeOrder(String orderId, String productId, int quantity,
                               double amount, String email, String address) {
        System.out.println("Processing order " + orderId + "...\n");

        // Check inventory
        if (!inventory.checkStock(productId)) {
            System.out.println("  Order failed: Out of stock");
            return false;
        }

        // Process payment
        if (!payment.processPayment(orderId, amount)) {
            System.out.println("  Order failed: Payment declined");
            return false;
        }

        // Update inventory
        inventory.updateStock(productId, quantity);

        // Create shipment
        String trackingId = shipping.createShipment(orderId, address);

        // Send notifications
        notification.sendOrderConfirmation(email, orderId);
        notification.sendShippingUpdate(email, trackingId);

        System.out.println("\n  Order " + orderId + " completed successfully!");
        return true;
    }
}

public class MainFacade {
    public static void main(String[] args) {
        System.out.println("=== Facade Pattern Demonstration ===\n");

        // Home Theater example
        System.out.println("--- 1. Home Theater Facade ---");

        Amplifier amp = new Amplifier("Top-O-Line Amplifier");
        DVDPlayer dvd = new DVDPlayer("Sony DVD Player");
        Projector projector = new Projector("Epson HD Projector");
        TheaterLights lights = new TheaterLights("Theater Ceiling Lights");
        Screen screen = new Screen("120-inch Screen");
        PopcornMachine popcorn = new PopcornMachine("Popcorn Maker");

        HomeTheaterFacade homeTheater = new HomeTheaterFacade(
            amp, dvd, projector, lights, screen, popcorn
        );

        homeTheater.watchMovie("Inception");
        homeTheater.endMovie();
        System.out.println();

        // Computer startup example
        System.out.println("--- 2. Computer Startup Facade ---");
        ComputerFacade computer = new ComputerFacade();
        computer.start();
        System.out.println();

        // Order processing example
        System.out.println("--- 3. E-Commerce Order Facade ---");
        OrderFacade orderSystem = new OrderFacade();
        orderSystem.placeOrder(
            "ORD-12345",
            "PROD-789",
            2,
            99.99,
            "customer@example.com",
            "123 Main St, City, State 12345"
        );

        System.out.println("\n=== Summary ===");
        System.out.println("Facade pattern benefits:");
        System.out.println("  - Simplifies complex subsystem interface");
        System.out.println("  - Reduces dependencies on subsystem internals");
        System.out.println("  - Wraps poorly-designed APIs with better ones");
        System.out.println("  - Provides context-specific interface to generic functionality");
        System.out.println("\nKey points:");
        System.out.println("  - Facade doesn't prevent direct subsystem access if needed");
        System.out.println("  - Can have multiple facades for different use cases");
        System.out.println("  - Subsystem classes are unaware of facade");
    }
}
