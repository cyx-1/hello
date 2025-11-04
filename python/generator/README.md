# Python Generator Functions - Comprehensive Demonstration

This project demonstrates the full capabilities of Python generator functions, from basic concepts to advanced patterns.

## Overview

Generator functions are a powerful Python feature that allows you to create iterators in an efficient, memory-friendly way. They use the `yield` keyword instead of `return` to produce a sequence of values over time, maintaining their state between calls.

## Requirements

- Python 3.10 or higher (for modern type hints with `|` union operator and `list[int]` syntax)
- No external dependencies required

## Running the Demo

```bash
uv run python main_generator.py
```

## Key Concepts Demonstrated

1. **Basic Generator Functions** - Understanding `yield` and lazy evaluation
2. **Memory Efficiency** - Generators vs Lists
3. **Generator Expressions** - Lazy evaluation syntax
4. **Generator State** - State preservation and exhaustion
5. **Infinite Generators** - Unbounded sequences
6. **Generator Delegation** - Using `yield from`
7. **Advanced Methods** - `send()`, `throw()`, `close()`
8. **Practical Patterns** - Data pipelines
9. **Return Values** - Capturing generator return values

---

## Detailed Walkthrough

### Section 1: Basic Generator Functions

**Source Code (lines 29-37):**
```python
def simple_generator() -> Generator[int, None, None]:
    """A simple generator that yields three values."""
    print("  [Generator] Starting execution")
    yield 1
    print("  [Generator] After first yield")
    yield 2
    print("  [Generator] After second yield")
    yield 3
    print("  [Generator] After third yield")
```

**Execution (lines 346-350):**
```python
gen = simple_generator()
print(f"Generator object: {gen}")
print("\nIterating through generator:")
for value in gen:
    print(f"  Received: {value}")
```

**Output:**
```
Creating a simple generator:
Generator object: <generator object simple_generator at 0x7ed6fa8dd9c0>

Iterating through generator:
  [Generator] Starting execution
  Received: 1
  [Generator] After first yield
  Received: 2
  [Generator] After second yield
  Received: 3
  [Generator] After third yield
```

**Key Observations:**
- Line 346: Creating a generator returns a generator object, NOT the values
- Line 349: The generator function only starts executing when we begin iteration
- Between yields (lines 32, 34, 36): Execution pauses and resumes, demonstrating stateful behavior

---

### Section 2: Memory Efficiency

**Source Code (lines 54-59):**
```python
def range_generator(n: int) -> Generator[int, None, None]:
    """Generator version of range - memory efficient."""
    i = 0
    while i < n:
        yield i
        i += 1
```

**Output:**
```
  Generator object size: 200 bytes
  List object size (100 items): 856 bytes
  Generator advantage: Constant memory regardless of range size!
```

**Key Observations:**
- Generator: Fixed ~200 bytes regardless of range size (even for 1,000,000 items)
- List: Memory grows linearly with number of elements
- Critical advantage: Generators compute values on-demand, ideal for large datasets

---

### Section 3: Generator Expressions

**Source Code (line 92):**
```python
gen_expr = (x * x for x in range(5))  # Parentheses = generator
```

vs

```python
list_comp = [x * x for x in range(5)]  # Brackets = list
```

**Output:**
```
  Generator expression: <generator object demonstrate_generator_expressions.<locals>.<genexpr> at 0x7ed6fa9a1e50>
  Type: <class 'generator'>
  Values: [0, 1, 4, 9, 16]

  List comprehension: [0, 1, 4, 9, 16]
  Type: <class 'list'>
```

**Key Observations:**
- Line 92: Generator expression uses `()` - creates generator object
- Line 98: List comprehension uses `[]` - creates list immediately
- Generator expression evaluates lazily; list comprehension evaluates eagerly

---

### Section 4: Generator State and Exhaustion

**Source Code (lines 40-46):**
```python
def countdown(n: int) -> Generator[int, None, None]:
    """Generator that counts down from n to 1."""
    print(f"  [Countdown] Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("  [Countdown] Finished!")
```

**Output:**
```
  First iteration:
  [Countdown] Starting countdown from 3
    3
    2

  Second iteration (continuing from where we left off):
    1

  Trying to get another value (generator is exhausted):
  [Countdown] Finished!
    StopIteration exception raised - generator exhausted!
```

**Key Observations:**
- Lines 113-114: First two `next()` calls yield 3, 2
- Line 117: Third `next()` call continues from saved state, yields 1
- Line 121: Fourth `next()` call raises `StopIteration` - generator is exhausted
- Generator remembers its position between calls (line 45: `n` variable maintains state)

---

### Section 5: Infinite Generators

**Source Code (lines 139-144):**
```python
def fibonacci() -> Generator[int, None, None]:
    """Generator that produces infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:  # Infinite loop!
        yield a
        a, b = b, a + b
```

**Output:**
```
  First 10 Fibonacci numbers:
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Key Observations:**
- Line 142: `while True` creates an infinite generator
- Line 156: Safe to use - we control consumption with `range(10)`
- Practical use: Event streams, real-time data, mathematical sequences

---

### Section 6: Generator Delegation with `yield from`

**Source Code (lines 165-170):**
```python
def chain_generators(
    gen1: Generator[int, None, None], gen2: Generator[int, None, None]
) -> Generator[int, None, None]:
    """Chain two generators using yield from."""
    yield from gen1
    yield from gen2
```

**Output:**
```
  Chaining two generators with 'yield from':
    0
    1
    2
    0
    1
    2
```

**Key Observations:**
- Line 169: `yield from gen1` delegates to first generator entirely
- Line 170: Then delegates to second generator
- Produces values from both generators in sequence
- More efficient than manually looping and yielding

---

### Section 7: Advanced - `send()` Method

**Source Code (lines 189-198):**
```python
def echo_generator() -> Generator[str, str, None]:
    """Generator that can receive values via send()."""
    print("  [Echo] Generator started")
    try:
        while True:
            received = yield "Ready"  # Yields value AND receives input
            print(f"  [Echo] Received: {received}")
            yield f"Echo: {received}"
    except GeneratorExit:
        print("  [Echo] Generator closing")
```

**Execution (lines 206-217):**
```python
status = next(gen)           # Prime the generator
echo1 = gen.send("Hello")    # Send value to generator
status = next(gen)
echo2 = gen.send("World")
```

**Output:**
```
  [Echo] Generator started
  Status: Ready
  [Echo] Received: Hello
  Response: Echo: Hello
  Status: Ready
  [Echo] Received: World
  Response: Echo: World
  [Echo] Generator closing
```

**Key Observations:**
- Line 194: `received = yield "Ready"` - two-way communication
- Line 206: Must call `next()` first to prime generator
- Line 210: `send("Hello")` sends value to generator and resumes execution
- Line 195: Generator receives the sent value
- Enables coroutine-style programming

---

### Section 8: Advanced - `throw()` Method

**Source Code (lines 227-237):**
```python
def resilient_generator() -> Generator[int, None, None]:
    """Generator that can handle exceptions via throw()."""
    try:
        for i in range(5):
            print(f"  [Resilient] Yielding {i}")
            yield i
    except ValueError as e:
        print(f"  [Resilient] Caught ValueError: {e}")
        yield -1
    finally:
        print("  [Resilient] Cleanup in finally block")
```

**Execution (line 249):**
```python
value = gen.throw(ValueError, "Simulated error")
```

**Output:**
```
  [Resilient] Yielding 0
  Value: 0
  [Resilient] Yielding 1
  Value: 1

  Throwing ValueError into generator:
  [Resilient] Caught ValueError: Simulated error
  Generator recovered and yielded: -1
  [Resilient] Cleanup in finally block
```

**Key Observations:**
- Line 249: `throw()` injects exception into generator at yield point
- Line 233: Exception caught by try-except block inside generator
- Line 235: Generator recovers and yields -1
- Line 237: Finally block executes for cleanup
- Use case: Error handling in pipelines

---

### Section 9: Practical Use Case - Data Pipeline

**Source Code (lines 260-305):**
```python
def read_numbers(data: list[str]) -> Generator[str, None, None]:
    """Stage 1: Read data."""
    for item in data:
        yield item

def parse_numbers(data: Generator[str, None, None]) -> Generator[int, None, None]:
    """Stage 2: Parse strings to integers."""
    for item in data:
        try:
            yield int(item)
        except ValueError:
            print(f"  [Pipeline] Skipping invalid number: {item}")

def filter_even(numbers: Generator[int, None, None]) -> Generator[int, None, None]:
    """Stage 3: Filter even numbers."""
    for num in numbers:
        if num % 2 == 0:
            yield num

def square_numbers(numbers: Generator[int, None, None]) -> Generator[int, None, None]:
    """Stage 4: Square the numbers."""
    for num in numbers:
        yield num * num
```

**Execution (lines 295-304):**
```python
data = ["1", "2", "3", "invalid", "4", "5", "6"]

stage1 = read_numbers(data)
stage2 = parse_numbers(stage1)
stage3 = filter_even(stage2)
stage4 = square_numbers(stage3)

for result in stage4:
    print(f"    {result}")
```

**Output:**
```
  Input data: ['1', '2', '3', 'invalid', '4', '5', '6']

  Pipeline: Read -> Parse -> Filter Even -> Square
  Results:
    4
  [Pipeline] Skipping invalid number: invalid
    16
    36
```

**Key Observations:**
- Lines 295-298: Pipeline built by chaining generators (no execution yet)
- Line 303: Execution triggered by final `for` loop - lazy evaluation
- Each value flows through entire pipeline: "2" → parse → filter → square → 4
- Line 272: Invalid data skipped gracefully
- Memory efficient: Only one item processed at a time
- Results: 2²=4, 4²=16, 6²=36 (odd numbers filtered out)

---

### Section 10: Generator Return Values

**Source Code (lines 312-316):**
```python
def generator_with_return(n: int) -> Generator[int, None, str]:
    """Generator that yields values and returns a final result."""
    for i in range(n):
        yield i
    return f"Generated {n} values"  # Return value after yields
```

**Execution (lines 324-329):**
```python
try:
    while True:
        value = next(gen)
        print(f"    {value}")
except StopIteration as e:
    print(f"\n  Return value captured from StopIteration: '{e.value}'")
```

**Output:**
```
  Yielded values:
    0
    1
    2

  Return value captured from StopIteration: 'Generated 3 values'
```

**Key Observations:**
- Line 316: `return` statement in generator provides a final value
- Lines 314-315: Generator yields 0, 1, 2 first
- Line 328: Return value captured from `StopIteration.value` attribute
- Type hint line 312: `Generator[int, None, str]` - yields int, returns str
- Useful for summary statistics or cleanup messages

---

## Summary of Generator Advantages

1. **Memory Efficiency**: Constant memory usage regardless of sequence size
2. **Lazy Evaluation**: Values computed on-demand, not all at once
3. **Infinite Sequences**: Can represent unbounded data streams
4. **State Preservation**: Maintains local variables between yields
5. **Pipeline Composition**: Clean, modular data processing
6. **Two-way Communication**: `send()` enables coroutines
7. **Exception Handling**: `throw()` for error injection
8. **Cleaner Code**: More readable than manual iterator classes

## When to Use Generators

- Processing large files (read line-by-line)
- Streaming data (network, sensors)
- Mathematical sequences (Fibonacci, primes)
- Data transformation pipelines
- Memory-constrained environments
- Infinite sequences
- Coroutine-based concurrency patterns

## Version Requirements

This code uses Python 3.10+ features:
- Modern type hints: `list[int]` instead of `List[int]`
- Union types with `|` operator (though not used here, the style aligns with 3.10+)
- Full `typing.Generator` support

To run with earlier Python versions (3.7-3.9), change:
- `list[int]` → `List[int]` (import from `typing`)
- `list[str]` → `List[str]`
