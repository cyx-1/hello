# Builder Pattern

The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

## How to Run

```bash
cd java/builder
mvn compile exec:java
```

## Key Source Code

### Product Class with Private Constructor (Lines 14-67)
```java
class Computer {
    // Required and optional parameters
    private String cpu;
    private String ram;
    private String storage;
    private String gpu;
    // ...

    // Private constructor - only accessible through Builder
    private Computer(ComputerBuilder builder) {
        this.cpu = builder.cpu;
        this.ram = builder.ram;
        // ...
    }
}
```

### Builder Class with Fluent Methods (Lines 69-119)
```java
public static class ComputerBuilder {
    // Required parameters in constructor
    public ComputerBuilder(String cpu, String ram) {
        this.cpu = cpu;
        this.ram = ram;
    }

    // Fluent methods for optional parameters
    public ComputerBuilder storage(String storage) {
        this.storage = storage;
        return this;
    }

    public ComputerBuilder gpu(String gpu) {
        this.gpu = gpu;
        return this;
    }

    // Build method constructs final object
    public Computer build() {
        return new Computer(this);
    }
}
```

### Director Class (Lines 124-169)
```java
class ComputerDirector {
    public Computer buildGamingPC() {
        return new Computer.ComputerBuilder("Intel Core i9-13900K", "32GB DDR5")
            .storage("2TB NVMe SSD")
            .gpu("NVIDIA RTX 4090")
            .coolingSystem("360mm AIO Liquid Cooler")
            .wifi(true)
            .build();
    }
}
```

## Program Output

```
=== Builder Pattern Demonstration ===

--- 1. Direct Builder Usage ---
Computer Configuration:
  CPU: AMD Ryzen 7 7800X3D
  RAM: 32GB DDR5
  Storage: 1TB NVMe SSD
  GPU: NVIDIA RTX 4070 Ti
  Cooling: Noctua NH-D15
  PSU: Standard
  Motherboard: Standard
  WiFi: Yes
  Bluetooth: Yes
  Peripherals: Mechanical Keyboard, Gaming Headset

--- 2. Using Director for Gaming PC ---
Computer Configuration:
  CPU: Intel Core i9-13900K
  RAM: 32GB DDR5
  Storage: 2TB NVMe SSD
  GPU: NVIDIA RTX 4090
  Cooling: 360mm AIO Liquid Cooler
  PSU: 1000W 80+ Platinum
  Motherboard: ASUS ROG Maximus Z790
  WiFi: Yes
  Bluetooth: Yes
  Peripherals: Mechanical Keyboard, Gaming Mouse, 27" 4K Monitor

--- 3. Using Director for Office PC ---
Computer Configuration:
  CPU: Intel Core i5-13400
  RAM: 16GB DDR4
  Storage: 512GB SSD
  GPU: Integrated
  Cooling: Stock
  PSU: Standard
  Motherboard: ASUS Prime B660
  WiFi: Yes
  Bluetooth: No
  Peripherals: Wireless Keyboard, Wireless Mouse, 24" Monitor

--- 5. Using Director for Budget PC ---
Computer Configuration:
  CPU: AMD Ryzen 5 5600G
  RAM: 8GB DDR4
  Storage: 256GB SSD
  GPU: Integrated
  Cooling: Stock
  PSU: Standard
  Motherboard: Standard
  WiFi: No
  Bluetooth: No

--- 6. HTTP Request Builder Example ---
HTTP Request:
  URL: https://api.example.com/users
  Method: GET
  Timeout: 5000ms
  Follow Redirects: true
  Headers:
    - Accept: application/json
    - Authorization: Bearer token123

HTTP Request:
  URL: https://api.example.com/users
  Method: POST
  Timeout: 10000ms
  Follow Redirects: false
  Headers:
    - Content-Type: application/json
    - Authorization: Bearer token123
  Body: {"name": "John", "email": "john@example.com"}

=== Summary ===
Builder pattern benefits:
  - Constructs complex objects step by step
  - Same construction process for different representations
  - Isolates complex construction code from business logic
  - Allows fluent API with method chaining
  - Makes optional parameters clear and manageable
```

## Output Analysis

| Output Section | Source Code Reference | Explanation |
|----------------|----------------------|-------------|
| Direct Builder Usage | Lines 243-253 | Method chaining creates customized Computer |
| Gaming PC | Lines 125-137 | Director provides predefined high-end configuration |
| Office PC | Lines 139-149 | Director provides standard business configuration |
| Budget PC | Lines 161-165 | Minimal configuration with only required params |
| HTTP Request | Lines 224-240 | Alternative Builder example with defaults |

## Pattern Benefits

1. **Step-by-Step Construction**: Build complex objects incrementally
2. **Fluent Interface**: Method chaining improves readability
3. **Immutable Objects**: Products can be made immutable
4. **Clear Parameter Intent**: Named methods vs constructor overloading
5. **Director Reusability**: Predefined configurations encapsulate common builds

## Requirements

- Java 17 or higher
- Maven 3.x
