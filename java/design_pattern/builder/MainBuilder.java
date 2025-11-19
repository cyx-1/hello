/**
 * Comprehensive demonstration of the Builder Pattern in Java
 *
 * The Builder pattern separates the construction of a complex object from its
 * representation, allowing the same construction process to create different representations.
 */

import java.util.ArrayList;
import java.util.List;

// Product class - Complex object to be built
class Computer {
    // Required parameters
    private String cpu;
    private String ram;

    // Optional parameters
    private String storage;
    private String gpu;
    private String coolingSystem;
    private String powerSupply;
    private String motherboard;
    private List<String> peripherals;
    private boolean hasWifi;
    private boolean hasBluetooth;

    // Private constructor - only accessible through Builder
    private Computer(ComputerBuilder builder) {
        this.cpu = builder.cpu;
        this.ram = builder.ram;
        this.storage = builder.storage;
        this.gpu = builder.gpu;
        this.coolingSystem = builder.coolingSystem;
        this.powerSupply = builder.powerSupply;
        this.motherboard = builder.motherboard;
        this.peripherals = builder.peripherals;
        this.hasWifi = builder.hasWifi;
        this.hasBluetooth = builder.hasBluetooth;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Computer Configuration:\n");
        sb.append("  CPU: ").append(cpu).append("\n");
        sb.append("  RAM: ").append(ram).append("\n");
        sb.append("  Storage: ").append(storage != null ? storage : "Not specified").append("\n");
        sb.append("  GPU: ").append(gpu != null ? gpu : "Integrated").append("\n");
        sb.append("  Cooling: ").append(coolingSystem != null ? coolingSystem : "Stock").append("\n");
        sb.append("  PSU: ").append(powerSupply != null ? powerSupply : "Standard").append("\n");
        sb.append("  Motherboard: ").append(motherboard != null ? motherboard : "Standard").append("\n");
        sb.append("  WiFi: ").append(hasWifi ? "Yes" : "No").append("\n");
        sb.append("  Bluetooth: ").append(hasBluetooth ? "Yes" : "No").append("\n");
        if (peripherals != null && !peripherals.isEmpty()) {
            sb.append("  Peripherals: ").append(String.join(", ", peripherals)).append("\n");
        }
        return sb.toString();
    }

    // Static Builder class
    public static class ComputerBuilder {
        // Required parameters
        private String cpu;
        private String ram;

        // Optional parameters with default values
        private String storage;
        private String gpu;
        private String coolingSystem;
        private String powerSupply;
        private String motherboard;
        private List<String> peripherals = new ArrayList<>();
        private boolean hasWifi = false;
        private boolean hasBluetooth = false;

        // Builder constructor with required parameters
        public ComputerBuilder(String cpu, String ram) {
            this.cpu = cpu;
            this.ram = ram;
        }

        // Builder methods for optional parameters (return this for chaining)
        public ComputerBuilder storage(String storage) {
            this.storage = storage;
            return this;
        }

        public ComputerBuilder gpu(String gpu) {
            this.gpu = gpu;
            return this;
        }

        public ComputerBuilder coolingSystem(String coolingSystem) {
            this.coolingSystem = coolingSystem;
            return this;
        }

        public ComputerBuilder powerSupply(String powerSupply) {
            this.powerSupply = powerSupply;
            return this;
        }

        public ComputerBuilder motherboard(String motherboard) {
            this.motherboard = motherboard;
            return this;
        }

        public ComputerBuilder addPeripheral(String peripheral) {
            this.peripherals.add(peripheral);
            return this;
        }

        public ComputerBuilder wifi(boolean hasWifi) {
            this.hasWifi = hasWifi;
            return this;
        }

        public ComputerBuilder bluetooth(boolean hasBluetooth) {
            this.hasBluetooth = hasBluetooth;
            return this;
        }

        // Build method to construct the final object
        public Computer build() {
            return new Computer(this);
        }
    }
}

// Director class - defines order of building steps
class ComputerDirector {

    public Computer buildGamingPC() {
        return new Computer.ComputerBuilder("Intel Core i9-13900K", "32GB DDR5")
            .storage("2TB NVMe SSD")
            .gpu("NVIDIA RTX 4090")
            .coolingSystem("360mm AIO Liquid Cooler")
            .powerSupply("1000W 80+ Platinum")
            .motherboard("ASUS ROG Maximus Z790")
            .wifi(true)
            .bluetooth(true)
            .addPeripheral("Mechanical Keyboard")
            .addPeripheral("Gaming Mouse")
            .addPeripheral("27\" 4K Monitor")
            .build();
    }

    public Computer buildOfficePC() {
        return new Computer.ComputerBuilder("Intel Core i5-13400", "16GB DDR4")
            .storage("512GB SSD")
            .motherboard("ASUS Prime B660")
            .wifi(true)
            .addPeripheral("Wireless Keyboard")
            .addPeripheral("Wireless Mouse")
            .addPeripheral("24\" Monitor")
            .build();
    }

    public Computer buildWorkstation() {
        return new Computer.ComputerBuilder("AMD Ryzen 9 7950X", "128GB DDR5 ECC")
            .storage("4TB NVMe SSD")
            .gpu("NVIDIA RTX A6000")
            .coolingSystem("Custom Loop Water Cooling")
            .powerSupply("1200W 80+ Titanium")
            .motherboard("ASUS Pro WS WRX80E")
            .wifi(true)
            .bluetooth(true)
            .addPeripheral("Professional Keyboard")
            .addPeripheral("3D Mouse")
            .addPeripheral("Dual 32\" 4K Monitors")
            .build();
    }

    public Computer buildBudgetPC() {
        return new Computer.ComputerBuilder("AMD Ryzen 5 5600G", "8GB DDR4")
            .storage("256GB SSD")
            .build();
    }
}

// Another example: HTTP Request Builder
class HttpRequest {
    private String url;
    private String method;
    private String body;
    private List<String> headers;
    private int timeout;
    private boolean followRedirects;

    private HttpRequest(Builder builder) {
        this.url = builder.url;
        this.method = builder.method;
        this.body = builder.body;
        this.headers = builder.headers;
        this.timeout = builder.timeout;
        this.followRedirects = builder.followRedirects;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("HTTP Request:\n");
        sb.append("  URL: ").append(url).append("\n");
        sb.append("  Method: ").append(method).append("\n");
        sb.append("  Timeout: ").append(timeout).append("ms\n");
        sb.append("  Follow Redirects: ").append(followRedirects).append("\n");
        if (!headers.isEmpty()) {
            sb.append("  Headers:\n");
            for (String header : headers) {
                sb.append("    - ").append(header).append("\n");
            }
        }
        if (body != null) {
            sb.append("  Body: ").append(body).append("\n");
        }
        return sb.toString();
    }

    public static class Builder {
        private String url;
        private String method = "GET";
        private String body;
        private List<String> headers = new ArrayList<>();
        private int timeout = 30000;
        private boolean followRedirects = true;

        public Builder(String url) {
            this.url = url;
        }

        public Builder method(String method) {
            this.method = method;
            return this;
        }

        public Builder body(String body) {
            this.body = body;
            return this;
        }

        public Builder addHeader(String header) {
            this.headers.add(header);
            return this;
        }

        public Builder timeout(int timeout) {
            this.timeout = timeout;
            return this;
        }

        public Builder followRedirects(boolean followRedirects) {
            this.followRedirects = followRedirects;
            return this;
        }

        public HttpRequest build() {
            return new HttpRequest(this);
        }
    }
}

public class MainBuilder {
    public static void main(String[] args) {
        System.out.println("=== Builder Pattern Demonstration ===\n");

        // Using Builder directly
        System.out.println("--- 1. Direct Builder Usage ---");
        Computer customPC = new Computer.ComputerBuilder("AMD Ryzen 7 7800X3D", "32GB DDR5")
            .storage("1TB NVMe SSD")
            .gpu("NVIDIA RTX 4070 Ti")
            .coolingSystem("Noctua NH-D15")
            .wifi(true)
            .bluetooth(true)
            .addPeripheral("Mechanical Keyboard")
            .addPeripheral("Gaming Headset")
            .build();
        System.out.println(customPC);

        // Using Director for predefined configurations
        System.out.println("--- 2. Using Director for Gaming PC ---");
        ComputerDirector director = new ComputerDirector();
        Computer gamingPC = director.buildGamingPC();
        System.out.println(gamingPC);

        System.out.println("--- 3. Using Director for Office PC ---");
        Computer officePC = director.buildOfficePC();
        System.out.println(officePC);

        System.out.println("--- 4. Using Director for Workstation ---");
        Computer workstation = director.buildWorkstation();
        System.out.println(workstation);

        System.out.println("--- 5. Using Director for Budget PC ---");
        Computer budgetPC = director.buildBudgetPC();
        System.out.println(budgetPC);

        // HTTP Request Builder example
        System.out.println("--- 6. HTTP Request Builder Example ---");
        HttpRequest getRequest = new HttpRequest.Builder("https://api.example.com/users")
            .method("GET")
            .addHeader("Accept: application/json")
            .addHeader("Authorization: Bearer token123")
            .timeout(5000)
            .build();
        System.out.println(getRequest);

        HttpRequest postRequest = new HttpRequest.Builder("https://api.example.com/users")
            .method("POST")
            .addHeader("Content-Type: application/json")
            .addHeader("Authorization: Bearer token123")
            .body("{\"name\": \"John\", \"email\": \"john@example.com\"}")
            .timeout(10000)
            .followRedirects(false)
            .build();
        System.out.println(postRequest);

        System.out.println("=== Summary ===");
        System.out.println("Builder pattern benefits:");
        System.out.println("  - Constructs complex objects step by step");
        System.out.println("  - Same construction process for different representations");
        System.out.println("  - Isolates complex construction code from business logic");
        System.out.println("  - Allows fluent API with method chaining");
        System.out.println("  - Makes optional parameters clear and manageable");
    }
}
