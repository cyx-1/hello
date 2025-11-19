#!/usr/bin/env python3
"""
Singleton Pattern Demonstration in Python

This script demonstrates various ways to implement the Singleton pattern in Python,
including classic __new__, decorator-based, metaclass-based, and thread-safe approaches.
"""

# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

import threading


# ============================================================================
# Approach 1: Classic Singleton using __new__
# ============================================================================
class ClassicSingleton:
    """Classic singleton implementation using __new__ method."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("[Line 27] Creating new ClassicSingleton instance")
            cls._instance = super().__new__(cls)
            cls._instance.value = 0
        return cls._instance

    def increment(self):
        self.value += 1
        return self.value


# ============================================================================
# Approach 2: Decorator-based Singleton
# ============================================================================
def singleton_decorator(cls):
    """Decorator that converts a class into a singleton."""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            print(f"[Line 48] Creating new {cls.__name__} instance via decorator")
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton_decorator
class DecoratorSingleton:
    """Singleton implemented using a decorator."""

    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value


# ============================================================================
# Approach 3: Metaclass-based Singleton
# ============================================================================
class SingletonMeta(type):
    """Metaclass that creates a Singleton base class when called."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"[Line 78] Creating new {cls.__name__} instance via metaclass")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MetaclassSingleton(metaclass=SingletonMeta):
    """Singleton implemented using a metaclass."""

    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value


# ============================================================================
# Approach 4: Thread-Safe Singleton
# ============================================================================
class ThreadSafeSingleton:
    """Thread-safe singleton implementation using locks."""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double-checked locking pattern
                if cls._instance is None:
                    print("[Line 111] Creating new ThreadSafeSingleton instance")
                    cls._instance = super().__new__(cls)
                    cls._instance.value = 0
        return cls._instance

    def increment(self):
        with self._lock:
            self.value += 1
            return self.value


# ============================================================================
# Approach 5: Module-level Singleton (Pythonic way)
# ============================================================================
class _ModuleSingleton:
    """Internal class for module-level singleton."""

    def __init__(self):
        print("[Line 131] Creating module-level singleton instance")
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value


# This instance is created once when the module is imported
module_singleton = _ModuleSingleton()


# ============================================================================
# Demonstration Functions
# ============================================================================
def demonstrate_classic_singleton():
    """Demonstrate classic singleton behavior."""
    print("\n" + "=" * 70)
    print("1. CLASSIC SINGLETON DEMONSTRATION")
    print("=" * 70)

    print("\n[Line 153] Creating first ClassicSingleton instance...")
    singleton1 = ClassicSingleton()
    print(f"[Line 155] singleton1.value = {singleton1.value}")
    print(f"[Line 156] singleton1.increment() = {singleton1.increment()}")
    print(f"[Line 157] singleton1.value = {singleton1.value}")

    print("\n[Line 159] Creating second ClassicSingleton instance...")
    singleton2 = ClassicSingleton()
    print(f"[Line 161] singleton2.value = {singleton2.value}")
    print(f"[Line 162] Are both instances the same? {singleton1 is singleton2}")
    print(f"[Line 163] id(singleton1) = {id(singleton1)}")
    print(f"[Line 164] id(singleton2) = {id(singleton2)}")


def demonstrate_decorator_singleton():
    """Demonstrate decorator-based singleton behavior."""
    print("\n" + "=" * 70)
    print("2. DECORATOR-BASED SINGLETON DEMONSTRATION")
    print("=" * 70)

    print("\n[Line 174] Creating first DecoratorSingleton instance...")
    singleton1 = DecoratorSingleton()
    print(f"[Line 176] singleton1.value = {singleton1.value}")
    print(f"[Line 177] singleton1.increment() = {singleton1.increment()}")
    print(f"[Line 178] singleton1.value = {singleton1.value}")

    print("\n[Line 180] Creating second DecoratorSingleton instance...")
    singleton2 = DecoratorSingleton()
    print(f"[Line 182] singleton2.value = {singleton2.value}")
    print(f"[Line 183] Are both instances the same? {singleton1 is singleton2}")
    print(f"[Line 184] id(singleton1) = {id(singleton1)}")
    print(f"[Line 185] id(singleton2) = {id(singleton2)}")


def demonstrate_metaclass_singleton():
    """Demonstrate metaclass-based singleton behavior."""
    print("\n" + "=" * 70)
    print("3. METACLASS-BASED SINGLETON DEMONSTRATION")
    print("=" * 70)

    print("\n[Line 195] Creating first MetaclassSingleton instance...")
    singleton1 = MetaclassSingleton()
    print(f"[Line 197] singleton1.value = {singleton1.value}")
    print(f"[Line 198] singleton1.increment() = {singleton1.increment()}")
    print(f"[Line 199] singleton1.value = {singleton1.value}")

    print("\n[Line 201] Creating second MetaclassSingleton instance...")
    singleton2 = MetaclassSingleton()
    print(f"[Line 203] singleton2.value = {singleton2.value}")
    print(f"[Line 204] Are both instances the same? {singleton1 is singleton2}")
    print(f"[Line 205] id(singleton1) = {id(singleton1)}")
    print(f"[Line 206] id(singleton2) = {id(singleton2)}")


def demonstrate_thread_safe_singleton():
    """Demonstrate thread-safe singleton behavior."""
    print("\n" + "=" * 70)
    print("4. THREAD-SAFE SINGLETON DEMONSTRATION")
    print("=" * 70)

    print("\n[Line 216] Creating first ThreadSafeSingleton instance...")
    singleton1 = ThreadSafeSingleton()
    print(f"[Line 218] singleton1.value = {singleton1.value}")
    print(f"[Line 219] singleton1.increment() = {singleton1.increment()}")
    print(f"[Line 220] singleton1.value = {singleton1.value}")

    print("\n[Line 222] Creating second ThreadSafeSingleton instance...")
    singleton2 = ThreadSafeSingleton()
    print(f"[Line 224] singleton2.value = {singleton2.value}")
    print(f"[Line 225] Are both instances the same? {singleton1 is singleton2}")
    print(f"[Line 226] id(singleton1) = {id(singleton1)}")
    print(f"[Line 227] id(singleton2) = {id(singleton2)}")

    # Test thread safety
    print("\n[Line 230] Testing thread safety with 100 increments across 10 threads...")

    def increment_multiple_times():
        singleton = ThreadSafeSingleton()
        for _ in range(10):
            singleton.increment()

    threads = []
    for i in range(10):
        thread = threading.Thread(target=increment_multiple_times)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_singleton = ThreadSafeSingleton()
    print(f"[Line 247] Final value after concurrent increments: {final_singleton.value}")
    print("[Line 248] Expected value: 102 (1 from line 219 + 1 from setup + 100 from threads)")


def demonstrate_module_singleton():
    """Demonstrate module-level singleton behavior."""
    print("\n" + "=" * 70)
    print("5. MODULE-LEVEL SINGLETON DEMONSTRATION (Pythonic)")
    print("=" * 70)

    print("\n[Line 257] Accessing module_singleton (already created at import time)...")
    print(f"[Line 258] module_singleton.value = {module_singleton.value}")
    print(f"[Line 259] module_singleton.increment() = {module_singleton.increment()}")
    print(f"[Line 260] module_singleton.value = {module_singleton.value}")

    print("\n[Line 262] Accessing module_singleton again...")
    # In a real scenario, you would import this from the module
    singleton_ref = module_singleton
    print(f"[Line 265] singleton_ref.value = {singleton_ref.value}")
    print(f"[Line 266] Are both references the same? {module_singleton is singleton_ref}")
    print(f"[Line 267] id(module_singleton) = {id(module_singleton)}")
    print(f"[Line 268] id(singleton_ref) = {id(singleton_ref)}")


def main():
    """Main function to run all demonstrations."""
    print("=" * 70)
    print("SINGLETON PATTERN DEMONSTRATION IN PYTHON")
    print("=" * 70)
    print("\nThis script demonstrates 5 different approaches to implement")
    print("the Singleton pattern in Python:")
    print("  1. Classic Singleton using __new__")
    print("  2. Decorator-based Singleton")
    print("  3. Metaclass-based Singleton")
    print("  4. Thread-Safe Singleton")
    print("  5. Module-level Singleton (Pythonic way)")

    demonstrate_classic_singleton()
    demonstrate_decorator_singleton()
    demonstrate_metaclass_singleton()
    demonstrate_thread_safe_singleton()
    demonstrate_module_singleton()

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  • Classic __new__: Simple but can be subverted")
    print("  • Decorator: Clean syntax, wraps the class")
    print("  • Metaclass: Powerful, controls class creation")
    print("  • Thread-Safe: Essential for multi-threaded applications")
    print("  • Module-level: Most Pythonic, leverages module import system")
    print("\nRecommendation: Use module-level singleton for most Python applications")
    print("=" * 70)


if __name__ == "__main__":
    main()
