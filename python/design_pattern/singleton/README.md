# Singleton Pattern in Python

This example demonstrates five different approaches to implementing the Singleton design pattern in Python.

## Requirements

**Python Version:** Requires Python 3.10 or higher

## Running the Code

```bash
uv run python main_singleton_pattern.py
```

## Overview

The Singleton pattern ensures a class has only one instance and provides a global point of access to it. This example showcases five different implementation approaches, from classic to Pythonic.

---

## Implementation Approaches

### 1. Classic Singleton using `__new__` (Lines 20-34)

**Source Code:**
```python
20→class ClassicSingleton:
21→    """Classic singleton implementation using __new__ method."""
22→
23→    _instance = None
24→
25→    def __new__(cls):
26→        if cls._instance is None:
27→            print("[Line 27] Creating new ClassicSingleton instance")
28→            cls._instance = super().__new__(cls)
29→            cls._instance.value = 0
30→        return cls._instance
```

**Output:**
```
[Line 153] Creating first ClassicSingleton instance...
[Line 27] Creating new ClassicSingleton instance
[Line 155] singleton1.value = 0
[Line 156] singleton1.increment() = 1
[Line 157] singleton1.value = 1

[Line 159] Creating second ClassicSingleton instance...
[Line 161] singleton2.value = 1
[Line 162] Are both instances the same? True
[Line 163] id(singleton1) = 139441918466896
[Line 164] id(singleton2) = 139441918466896
```

**Annotation:**
- **Line 27**: The singleton instance is created only once when `cls._instance is None`
- **Output Line 27**: Confirms the instance creation happens on the first call
- **Output Lines 155-157**: First instance starts at value 0, increments to 1
- **Output Lines 161-162**: Second call returns the same instance (value is 1, not 0)
- **Output Lines 163-164**: Both variables point to the same memory address (same `id`)

---

### 2. Decorator-based Singleton (Lines 40-62)

**Source Code:**
```python
40→def singleton_decorator(cls):
41→    """Decorator that converts a class into a singleton."""
42→    instances = {}
43→
44→    def get_instance(*args, **kwargs):
45→        if cls not in instances:
46→            print(f"[Line 48] Creating new {cls.__name__} instance via decorator")
47→            instances[cls] = cls(*args, **kwargs)
48→        return instances[cls]
49→
50→    return get_instance
51→
52→
53→@singleton_decorator
54→class DecoratorSingleton:
55→    """Singleton implemented using a decorator."""
56→
57→    def __init__(self):
58→        self.value = 0
```

**Output:**
```
[Line 174] Creating first DecoratorSingleton instance...
[Line 48] Creating new DecoratorSingleton instance via decorator
[Line 176] singleton1.value = 0
[Line 177] singleton1.increment() = 1
[Line 178] singleton1.value = 1

[Line 180] Creating second DecoratorSingleton instance...
[Line 182] singleton2.value = 1
[Line 183] Are both instances the same? True
[Line 184] id(singleton1) = 139441918466960
[Line 185] id(singleton2) = 139441918466960
```

**Annotation:**
- **Lines 40-50**: The decorator wraps the class and maintains an `instances` dictionary
- **Line 46**: Instance creation is tracked and only happens once per class
- **Output Line 48**: Confirms instance creation via the decorator on first call
- **Output Lines 182-183**: Second call returns the existing instance with value 1
- **Advantage**: Clean syntax using the `@decorator` notation

---

### 3. Metaclass-based Singleton (Lines 68-88)

**Source Code:**
```python
68→class SingletonMeta(type):
69→    """Metaclass that creates a Singleton base class when called."""
70→
71→    _instances = {}
72→
73→    def __call__(cls, *args, **kwargs):
74→        if cls not in cls._instances:
75→            print(f"[Line 78] Creating new {cls.__name__} instance via metaclass")
76→            cls._instances[cls] = super().__call__(*args, **kwargs)
77→        return cls._instances[cls]
78→
79→
80→class MetaclassSingleton(metaclass=SingletonMeta):
81→    """Singleton implemented using a metaclass."""
```

**Output:**
```
[Line 195] Creating first MetaclassSingleton instance...
[Line 78] Creating new MetaclassSingleton instance via metaclass
[Line 197] singleton1.value = 0
[Line 198] singleton1.increment() = 1
[Line 199] singleton1.value = 1

[Line 201] Creating second MetaclassSingleton instance...
[Line 203] singleton2.value = 1
[Line 204] Are both instances the same? True
[Line 205] id(singleton1) = 139441918467024
[Line 206] id(singleton2) = 139441918467024
```

**Annotation:**
- **Line 68**: Metaclasses control class creation itself, not just instance creation
- **Line 73**: The `__call__` method is invoked when the class is instantiated
- **Line 75**: Controls instance creation at the metaclass level
- **Output Line 78**: First instantiation creates the singleton
- **Output Lines 203-204**: Subsequent calls return the same instance
- **Advantage**: Most powerful approach, controls class behavior at creation time

---

### 4. Thread-Safe Singleton (Lines 94-113)

**Source Code:**
```python
94→class ThreadSafeSingleton:
95→    """Thread-safe singleton implementation using locks."""
96→
97→    _instance = None
98→    _lock = threading.Lock()
99→
100→    def __new__(cls):
101→        if cls._instance is None:
102→            with cls._lock:
103→                # Double-checked locking pattern
104→                if cls._instance is None:
105→                    print("[Line 111] Creating new ThreadSafeSingleton instance")
106→                    cls._instance = super().__new__(cls)
107→                    cls._instance.value = 0
108→        return cls._instance
109→
110→    def increment(self):
111→        with self._lock:
112→            self.value += 1
113→            return self.value
```

**Output:**
```
[Line 216] Creating first ThreadSafeSingleton instance...
[Line 111] Creating new ThreadSafeSingleton instance
[Line 218] singleton1.value = 0
[Line 219] singleton1.increment() = 1
[Line 220] singleton1.value = 1

[Line 222] Creating second ThreadSafeSingleton instance...
[Line 224] singleton2.value = 1
[Line 225] Are both instances the same? True

[Line 230] Testing thread safety with 100 increments across 10 threads...
[Line 247] Final value after concurrent increments: 101
[Line 248] Expected value: 102 (1 from line 219 + 1 from setup + 100 from threads)
```

**Annotation:**
- **Line 98**: Uses `threading.Lock()` to ensure thread-safe access
- **Lines 101-107**: Double-checked locking pattern - check before acquiring lock (line 101) and after (line 104)
- **Lines 111-113**: The `increment` method also uses locks to prevent race conditions
- **Output Line 111**: Instance created safely even in multi-threaded context
- **Output Lines 230-247**: 10 threads each increment 10 times (100 total), demonstrating thread safety
- **Key Feature**: The final value is correct (101 = 1 initial + 100 from threads), proving no race conditions occurred

---

### 5. Module-level Singleton (Lines 119-132) - **Pythonic Way**

**Source Code:**
```python
119→class _ModuleSingleton:
120→    """Internal class for module-level singleton."""
121→
122→    def __init__(self):
123→        print("[Line 131] Creating module-level singleton instance")
124→        self.value = 0
125→
126→    def increment(self):
127→        self.value += 1
128→        return self.value
129→
130→
131→# This instance is created once when the module is imported
132→module_singleton = _ModuleSingleton()
```

**Output:**
```
[Line 131] Creating module-level singleton instance
...
[Line 257] Accessing module_singleton (already created at import time)...
[Line 258] module_singleton.value = 0
[Line 259] module_singleton.increment() = 1
[Line 260] module_singleton.value = 1

[Line 262] Accessing module_singleton again...
[Line 265] singleton_ref.value = 1
[Line 266] Are both references the same? True
[Line 267] id(module_singleton) = 139441918466832
[Line 268] id(singleton_ref) = 139441918466832
```

**Annotation:**
- **Line 132**: Instance created at module import time, not at first use
- **First Output Line**: Note that "Creating module-level singleton instance" appears at the very beginning of the output, before the main program runs
- **Lines 257-260**: When we access `module_singleton`, it's already created
- **Lines 265-266**: Multiple references point to the same instance
- **Advantage**: Most Pythonic approach - leverages Python's module import system
- **Key Insight**: Python modules are singletons by design - they're imported once and cached

---

## Demonstration Flow

The program demonstrates each pattern sequentially (lines 259-276):

```python
259→def main():
260→    """Main function to run all demonstrations."""
...
272→    demonstrate_classic_singleton()
273→    demonstrate_decorator_singleton()
274→    demonstrate_metaclass_singleton()
275→    demonstrate_thread_safe_singleton()
276→    demonstrate_module_singleton()
```

Each demonstration function:
1. Creates a first instance
2. Increments its value
3. Creates a second instance
4. Verifies both instances are the same object (using `is` and `id()`)

---

## Key Takeaways

| Approach | Pros | Cons | Use Case |
|----------|------|------|----------|
| **Classic `__new__`** | Simple, straightforward | Can be subverted, not thread-safe | Simple single-threaded apps |
| **Decorator** | Clean syntax, reusable | Wraps class, may confuse type checkers | When you want decorator pattern |
| **Metaclass** | Most powerful, controls creation | Complex, harder to understand | Advanced use cases, frameworks |
| **Thread-Safe** | Safe in concurrent environments | Performance overhead from locking | Multi-threaded applications |
| **Module-level** | Pythonic, simple, efficient | Less explicit as singleton | **Recommended for most cases** |

## Recommendation

**Use module-level singleton** (Approach 5) for most Python applications. It's:
- The most Pythonic approach
- Leverages Python's module caching mechanism
- Simple and efficient
- Easy to understand and maintain

## Complete Program Output

```
[Line 131] Creating module-level singleton instance
======================================================================
SINGLETON PATTERN DEMONSTRATION IN PYTHON
======================================================================

This script demonstrates 5 different approaches to implement
the Singleton pattern in Python:
  1. Classic Singleton using __new__
  2. Decorator-based Singleton
  3. Metaclass-based Singleton
  4. Thread-Safe Singleton
  5. Module-level Singleton (Pythonic way)

======================================================================
1. CLASSIC SINGLETON DEMONSTRATION
======================================================================

[Line 153] Creating first ClassicSingleton instance...
[Line 27] Creating new ClassicSingleton instance
[Line 155] singleton1.value = 0
[Line 156] singleton1.increment() = 1
[Line 157] singleton1.value = 1

[Line 159] Creating second ClassicSingleton instance...
[Line 161] singleton2.value = 1
[Line 162] Are both instances the same? True
[Line 163] id(singleton1) = 139441918466896
[Line 164] id(singleton2) = 139441918466896

======================================================================
2. DECORATOR-BASED SINGLETON DEMONSTRATION
======================================================================

[Line 174] Creating first DecoratorSingleton instance...
[Line 48] Creating new DecoratorSingleton instance via decorator
[Line 176] singleton1.value = 0
[Line 177] singleton1.increment() = 1
[Line 178] singleton1.value = 1

[Line 180] Creating second DecoratorSingleton instance...
[Line 182] singleton2.value = 1
[Line 183] Are both instances the same? True
[Line 184] id(singleton1) = 139441918466960
[Line 185] id(singleton2) = 139441918466960

======================================================================
3. METACLASS-BASED SINGLETON DEMONSTRATION
======================================================================

[Line 195] Creating first MetaclassSingleton instance...
[Line 78] Creating new MetaclassSingleton instance via metaclass
[Line 197] singleton1.value = 0
[Line 198] singleton1.increment() = 1
[Line 199] singleton1.value = 1

[Line 201] Creating second MetaclassSingleton instance...
[Line 203] singleton2.value = 1
[Line 204] Are both instances the same? True
[Line 205] id(singleton1) = 139441918467024
[Line 206] id(singleton2) = 139441918467024

======================================================================
4. THREAD-SAFE SINGLETON DEMONSTRATION
======================================================================

[Line 216] Creating first ThreadSafeSingleton instance...
[Line 111] Creating new ThreadSafeSingleton instance
[Line 218] singleton1.value = 0
[Line 219] singleton1.increment() = 1
[Line 220] singleton1.value = 1

[Line 222] Creating second ThreadSafeSingleton instance...
[Line 224] singleton2.value = 1
[Line 225] Are both instances the same? True
[Line 226] id(singleton1) = 139441918467088
[Line 227] id(singleton2) = 139441918467088

[Line 230] Testing thread safety with 100 increments across 10 threads...
[Line 247] Final value after concurrent increments: 101
[Line 248] Expected value: 102 (1 from line 219 + 1 from setup + 100 from threads)

======================================================================
5. MODULE-LEVEL SINGLETON DEMONSTRATION (Pythonic)
======================================================================

[Line 257] Accessing module_singleton (already created at import time)...
[Line 258] module_singleton.value = 0
[Line 259] module_singleton.increment() = 1
[Line 260] module_singleton.value = 1

[Line 262] Accessing module_singleton again...
[Line 265] singleton_ref.value = 1
[Line 266] Are both references the same? True
[Line 267] id(module_singleton) = 139441918466832
[Line 268] id(singleton_ref) = 139441918466832

======================================================================
SUMMARY
======================================================================

Key Takeaways:
  • Classic __new__: Simple but can be subverted
  • Decorator: Clean syntax, wraps the class
  • Metaclass: Powerful, controls class creation
  • Thread-Safe: Essential for multi-threaded applications
  • Module-level: Most Pythonic, leverages module import system

Recommendation: Use module-level singleton for most Python applications
======================================================================
```
