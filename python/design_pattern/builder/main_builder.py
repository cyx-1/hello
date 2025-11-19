# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Builder Design Pattern Implementation

The Builder pattern separates the construction of a complex object from its
representation, allowing the same construction process to create different
representations. This is useful when an object has many optional parameters
or when the construction process involves multiple steps.
"""

from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Computer:
    """Product class representing a computer with various components."""

    cpu: str = ""
    memory: str = ""
    storage: str = ""
    gpu: str = ""
    os: str = ""
    extras: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        parts = [
            f"CPU: {self.cpu}",
            f"Memory: {self.memory}",
            f"Storage: {self.storage}",
            f"GPU: {self.gpu}",
            f"OS: {self.os}",
        ]
        if self.extras:
            parts.append(f"Extras: {', '.join(self.extras)}")
        return "\n  ".join(["Computer Configuration:"] + parts)


class ComputerBuilder:
    """Builder class for constructing Computer objects step by step."""

    def __init__(self) -> None:
        self._computer = Computer()

    def set_cpu(self, cpu: str) -> ComputerBuilder:
        """Set the CPU component."""
        self._computer.cpu = cpu
        return self

    def set_memory(self, memory: str) -> ComputerBuilder:
        """Set the memory component."""
        self._computer.memory = memory
        return self

    def set_storage(self, storage: str) -> ComputerBuilder:
        """Set the storage component."""
        self._computer.storage = storage
        return self

    def set_gpu(self, gpu: str) -> ComputerBuilder:
        """Set the GPU component."""
        self._computer.gpu = gpu
        return self

    def set_os(self, os: str) -> ComputerBuilder:
        """Set the operating system."""
        self._computer.os = os
        return self

    def add_extra(self, extra: str) -> ComputerBuilder:
        """Add an extra component."""
        self._computer.extras.append(extra)
        return self

    def build(self) -> Computer:
        """Build and return the final Computer object."""
        computer = self._computer
        self._computer = Computer()  # Reset for next build
        return computer


class ComputerDirector:
    """Director class that defines construction sequences for common configurations."""

    def __init__(self, builder: ComputerBuilder) -> None:
        self._builder = builder

    def build_gaming_pc(self) -> Computer:
        """Build a high-end gaming PC configuration."""
        return (
            self._builder.set_cpu("Intel Core i9-13900K")
            .set_memory("64GB DDR5")
            .set_storage("2TB NVMe SSD")
            .set_gpu("NVIDIA RTX 4090")
            .set_os("Windows 11 Pro")
            .add_extra("RGB Lighting")
            .add_extra("Liquid Cooling")
            .build()
        )

    def build_office_pc(self) -> Computer:
        """Build a standard office PC configuration."""
        return (
            self._builder.set_cpu("Intel Core i5-13400")
            .set_memory("16GB DDR4")
            .set_storage("512GB SSD")
            .set_gpu("Integrated Graphics")
            .set_os("Windows 11 Home")
            .build()
        )

    def build_workstation(self) -> Computer:
        """Build a professional workstation configuration."""
        return (
            self._builder.set_cpu("AMD Ryzen Threadripper PRO 5995WX")
            .set_memory("256GB ECC DDR4")
            .set_storage("4TB NVMe SSD RAID")
            .set_gpu("NVIDIA RTX A6000")
            .set_os("Ubuntu 22.04 LTS")
            .add_extra("10GbE Network Card")
            .add_extra("Redundant PSU")
            .build()
        )


def main() -> None:
    """Demonstrate the Builder pattern with various computer configurations."""
    print("=" * 60)
    print("BUILDER DESIGN PATTERN DEMONSTRATION")
    print("=" * 60)

    # Create builder and director
    builder = ComputerBuilder()
    director = ComputerDirector(builder)

    # Build predefined configurations using Director
    print("\n[1] Building Gaming PC using Director:")
    print("-" * 40)
    gaming_pc = director.build_gaming_pc()
    print(gaming_pc)

    print("\n[2] Building Office PC using Director:")
    print("-" * 40)
    office_pc = director.build_office_pc()
    print(office_pc)

    print("\n[3] Building Workstation using Director:")
    print("-" * 40)
    workstation = director.build_workstation()
    print(workstation)

    # Build custom configuration using Builder directly (without Director)
    print("\n[4] Building Custom PC using Builder directly:")
    print("-" * 40)
    custom_pc = (
        builder.set_cpu("Apple M2 Ultra")
        .set_memory("192GB Unified Memory")
        .set_storage("8TB SSD")
        .set_gpu("Apple M2 Ultra GPU (76-core)")
        .set_os("macOS Sonoma")
        .add_extra("Thunderbolt 4 Ports")
        .add_extra("Wi-Fi 6E")
        .build()
    )
    print(custom_pc)

    print("\n" + "=" * 60)
    print("Key Benefits of Builder Pattern:")
    print("=" * 60)
    print("• Separates complex object construction from representation")
    print("• Enables step-by-step construction with method chaining")
    print("• Director provides predefined construction sequences")
    print("• Same builder can create different product variations")
    print("• Encapsulates construction logic, improving maintainability")
    print("=" * 60)


if __name__ == "__main__":
    main()
