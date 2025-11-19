# Builder Design Pattern

The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

## How to Run

```bash
uv run python main_builder.py
```

## Key Source Code

### Product Class (lines 18-39)

The `Computer` class represents the complex object being built:

```python
18: @dataclass
19: class Computer:
20:     """Product class representing a computer with various components."""
21:
22:     cpu: str = ""
23:     memory: str = ""
24:     storage: str = ""
25:     gpu: str = ""
26:     os: str = ""
27:     extras: list[str] = field(default_factory=list)
```

### Builder Class (lines 42-82)

The `ComputerBuilder` provides methods for step-by-step construction with method chaining:

```python
42: class ComputerBuilder:
43:     """Builder class for constructing Computer objects step by step."""
44:
45:     def __init__(self) -> None:
46:         self._computer = Computer()
47:
48:     def set_cpu(self, cpu: str) -> ComputerBuilder:
49:         """Set the CPU component."""
50:         self._computer.cpu = cpu
51:         return self  # Returns self for method chaining
...
78:     def build(self) -> Computer:
79:         """Build and return the final Computer object."""
80:         computer = self._computer
81:         self._computer = Computer()  # Reset for next build
82:         return computer
```

### Director Class (lines 85-126)

The `ComputerDirector` encapsulates predefined construction sequences:

```python
85: class ComputerDirector:
86:     """Director class that defines construction sequences for common configurations."""
87:
88:     def __init__(self, builder: ComputerBuilder) -> None:
89:         self._builder = builder
90:
91:     def build_gaming_pc(self) -> Computer:
92:         """Build a high-end gaming PC configuration."""
93:         return (
94:             self._builder.set_cpu("Intel Core i9-13900K")
95:             .set_memory("64GB DDR5")
96:             .set_storage("2TB NVMe SSD")
97:             .set_gpu("NVIDIA RTX 4090")
98:             .set_os("Windows 11 Pro")
99:             .add_extra("RGB Lighting")
100:            .add_extra("Liquid Cooling")
101:            .build()
102:        )
```

### Usage Examples (lines 136-168)

```python
136:    builder = ComputerBuilder()
137:    director = ComputerDirector(builder)
138:
139:    # Build predefined configurations using Director
140:    print("\n[1] Building Gaming PC using Director:")
141:    print("-" * 40)
142:    gaming_pc = director.build_gaming_pc()  # Uses predefined sequence
...
155:    # Build custom configuration using Builder directly (without Director)
156:    print("\n[4] Building Custom PC using Builder directly:")
157:    print("-" * 40)
158:    custom_pc = (
159:        builder.set_cpu("Apple M2 Ultra")
160:        .set_memory("192GB Unified Memory")
161:        .set_storage("8TB SSD")
162:        .set_gpu("Apple M2 Ultra GPU (76-core)")
163:        .set_os("macOS Sonoma")
164:        .add_extra("Thunderbolt 4 Ports")
165:        .add_extra("Wi-Fi 6E")
166:        .build()
167:    )
```

## Program Output

```
============================================================
BUILDER DESIGN PATTERN DEMONSTRATION
============================================================

[1] Building Gaming PC using Director:
----------------------------------------
Computer Configuration:
  CPU: Intel Core i9-13900K
  Memory: 64GB DDR5
  Storage: 2TB NVMe SSD
  GPU: NVIDIA RTX 4090
  OS: Windows 11 Pro
  Extras: RGB Lighting, Liquid Cooling

[2] Building Office PC using Director:
----------------------------------------
Computer Configuration:
  CPU: Intel Core i5-13400
  Memory: 16GB DDR4
  Storage: 512GB SSD
  GPU: Integrated Graphics
  OS: Windows 11 Home

[3] Building Workstation using Director:
----------------------------------------
Computer Configuration:
  CPU: AMD Ryzen Threadripper PRO 5995WX
  Memory: 256GB ECC DDR4
  Storage: 4TB NVMe SSD RAID
  GPU: NVIDIA RTX A6000
  OS: Ubuntu 22.04 LTS
  Extras: 10GbE Network Card, Redundant PSU

[4] Building Custom PC using Builder directly:
----------------------------------------
Computer Configuration:
  CPU: Apple M2 Ultra
  Memory: 192GB Unified Memory
  Storage: 8TB SSD
  GPU: Apple M2 Ultra GPU (76-core)
  OS: macOS Sonoma
  Extras: Thunderbolt 4 Ports, Wi-Fi 6E

============================================================
Key Benefits of Builder Pattern:
============================================================
• Separates complex object construction from representation
• Enables step-by-step construction with method chaining
• Director provides predefined construction sequences
• Same builder can create different product variations
• Encapsulates construction logic, improving maintainability
============================================================
```

## Output Analysis

### Output Correlation with Source Code

| Output Section | Source Lines | Description |
|----------------|--------------|-------------|
| Gaming PC output | 91-102 | `build_gaming_pc()` chains all setter methods with gaming components |
| Office PC output | 104-113 | `build_office_pc()` uses minimal components (no extras) |
| Workstation output | 115-126 | `build_workstation()` includes professional extras like 10GbE |
| Custom PC output | 158-167 | Direct builder usage without Director for custom configs |

### Key Observations

1. **Method Chaining (lines 48-51, 94-101)**: Each setter returns `self`, enabling fluent API calls like `.set_cpu().set_memory().build()`

2. **Builder Reset (lines 80-81)**: After `build()`, the builder resets to a new Computer, allowing reuse for multiple builds

3. **Director Encapsulation (lines 85-126)**: Common configurations are encapsulated in the Director, while custom builds can use the Builder directly (lines 158-167)

4. **Optional Components (line 27)**: The `extras` list shows how builders handle optional/multiple values gracefully

## Requirements

- Python >= 3.10 (uses modern type hints with `list[str]` syntax)
