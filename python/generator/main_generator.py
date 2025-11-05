"""
Python Generator Functions Demonstration

This module demonstrates various capabilities of Python generator functions including:
- Basic generator functions with yield
- Generator expressions
- Memory efficiency compared to lists
- Generator state and iteration
- Advanced generator methods: send(), throw(), close()
- Practical use cases: infinite sequences, pipelines, coroutines
"""

import sys
from typing import Generator


def section_header(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


# ============================================================================
# SECTION 1: Basic Generator Functions
# ============================================================================


def simple_generator() -> Generator[int, None, None]:
    """A simple generator that yields three values."""
    print("  [Generator] Starting execution")
    yield 1
    print("  [Generator] After first yield")
    yield 2
    print("  [Generator] After second yield")
    yield 3
    print("  [Generator] After third yield")


def countdown(n: int) -> Generator[int, None, None]:
    """Generator that counts down from n to 1."""
    print(f"  [Countdown] Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("  [Countdown] Finished!")


# ============================================================================
# SECTION 2: Generator vs List - Memory Efficiency
# ============================================================================


def range_generator(n: int) -> Generator[int, None, None]:
    """Generator version of range - memory efficient."""
    i = 0
    while i < n:
        yield i
        i += 1


def range_list(n: int) -> list[int]:
    """List version of range - stores all values in memory."""
    return list(range(n))


def demonstrate_memory_efficiency() -> None:
    """Show memory difference between generator and list."""
    n = 1000000

    # Generator size
    gen = range_generator(n)
    gen_size = sys.getsizeof(gen)

    # List size (using smaller sample to avoid memory issues)
    small_list = range_list(100)
    list_size = sys.getsizeof(small_list)

    print(f"  Generator object size: {gen_size} bytes")
    print(f"  List object size (100 items): {list_size} bytes")
    print("  Generator advantage: Constant memory regardless of range size!")


# ============================================================================
# SECTION 3: Generator Expressions
# ============================================================================


def demonstrate_generator_expressions() -> None:
    """Show generator expressions vs list comprehensions."""
    # Generator expression (lazy evaluation)
    gen_expr = (x * x for x in range(5))
    print(f"  Generator expression: {gen_expr}")
    print(f"  Type: {type(gen_expr)}")
    print(f"  Values: {list(gen_expr)}")

    # List comprehension (eager evaluation)
    list_comp = [x * x for x in range(5)]
    print(f"\n  List comprehension: {list_comp}")
    print(f"  Type: {type(list_comp)}")


# ============================================================================
# SECTION 4: Generator State and Exhaustion
# ============================================================================


def demonstrate_generator_state() -> None:
    """Show how generators maintain state and can be exhausted."""
    gen = countdown(3)

    print("  First iteration:")
    print(f"    {next(gen)}")
    print(f"    {next(gen)}")

    print("\n  Second iteration (continuing from where we left off):")
    print(f"    {next(gen)}")

    print("\n  Trying to get another value (generator is exhausted):")
    try:
        print(f"    {next(gen)}")
    except StopIteration:
        print("    StopIteration exception raised - generator exhausted!")


# ============================================================================
# SECTION 5: Infinite Generators
# ============================================================================


def infinite_sequence(start: int = 0) -> Generator[int, None, None]:
    """Generator that produces an infinite sequence of numbers."""
    num = start
    while True:
        yield num
        num += 1


def fibonacci() -> Generator[int, None, None]:
    """Generator that produces infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def demonstrate_infinite_generators() -> None:
    """Show infinite generators with limited consumption."""
    print("  First 5 natural numbers:")
    gen = infinite_sequence()
    for i in range(5):
        print(f"    {next(gen)}")

    print("\n  First 10 Fibonacci numbers:")
    fib = fibonacci()
    fib_list = [next(fib) for _ in range(10)]
    print(f"    {fib_list}")


# ============================================================================
# SECTION 6: Generator Delegation with yield from
# ============================================================================


def chain_generators(
    gen1: Generator[int, None, None], gen2: Generator[int, None, None]
) -> Generator[int, None, None]:
    """Chain two generators using yield from."""
    yield from gen1
    yield from gen2


def demonstrate_yield_from() -> None:
    """Demonstrate yield from for generator delegation."""
    gen1 = range_generator(3)
    gen2 = range_generator(3)

    print("  Chaining two generators with 'yield from':")
    chained = chain_generators(gen1, gen2)
    for value in chained:
        print(f"    {value}")


# ============================================================================
# SECTION 7: Advanced Generator Methods - send()
# ============================================================================


def echo_generator() -> Generator[str, str, None]:
    """Generator that can receive values via send()."""
    print("  [Echo] Generator started")
    try:
        while True:
            received = yield "Ready"
            print(f"  [Echo] Received: {received}")
            yield f"Echo: {received}"
    except GeneratorExit:
        print("  [Echo] Generator closing")


def demonstrate_send() -> None:
    """Demonstrate the send() method for two-way communication."""
    gen = echo_generator()

    # Prime the generator
    status = next(gen)
    print(f"  Status: {status}")

    # Send values
    echo1 = gen.send("Hello")
    print(f"  Response: {echo1}")

    status = next(gen)
    print(f"  Status: {status}")

    echo2 = gen.send("World")
    print(f"  Response: {echo2}")

    gen.close()


# ============================================================================
# SECTION 8: Advanced Generator Methods - throw()
# ============================================================================


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


def demonstrate_throw() -> None:
    """Demonstrate the throw() method for exception injection."""
    gen = resilient_generator()

    print(f"  Value: {next(gen)}")
    print(f"  Value: {next(gen)}")

    print("\n  Throwing ValueError into generator:")
    try:
        value = gen.throw(ValueError, "Simulated error")
        print(f"  Generator recovered and yielded: {value}")
    except StopIteration:
        print("  Generator stopped after handling exception")


# ============================================================================
# SECTION 9: Practical Use Case - Data Pipeline
# ============================================================================


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


def demonstrate_pipeline() -> None:
    """Demonstrate a data processing pipeline using generators."""
    data = ["1", "2", "3", "invalid", "4", "5", "6"]

    print(f"  Input data: {data}\n")

    # Build pipeline
    stage1 = read_numbers(data)
    stage2 = parse_numbers(stage1)
    stage3 = filter_even(stage2)
    stage4 = square_numbers(stage3)

    # Execute pipeline (lazy evaluation - only happens when we iterate)
    print("  Pipeline: Read -> Parse -> Filter Even -> Square")
    print("  Results:")
    for result in stage4:
        print(f"    {result}")


# ============================================================================
# SECTION 10: Generator Return Values
# ============================================================================


def generator_with_return(n: int) -> Generator[int, None, str]:
    """Generator that yields values and returns a final result."""
    for i in range(n):
        yield i
    return f"Generated {n} values"


def demonstrate_return_value() -> None:
    """Show how to capture a generator's return value."""
    gen = generator_with_return(3)

    print("  Yielded values:")
    try:
        while True:
            value = next(gen)
            print(f"    {value}")
    except StopIteration as e:
        print(f"\n  Return value captured from StopIteration: '{e.value}'")


# ============================================================================
# MAIN EXECUTION
# ============================================================================


def main() -> None:
    """Run all generator demonstrations."""
    print("\n" + "=" * 70)
    print("  PYTHON GENERATOR FUNCTIONS - COMPREHENSIVE DEMONSTRATION")
    print("=" * 70)

    # Section 1: Basics
    section_header("1. Basic Generator Functions")
    print("Creating a simple generator:")
    gen = simple_generator()
    print(f"Generator object: {gen}")
    print("\nIterating through generator:")
    for value in gen:
        print(f"  Received: {value}")

    # Section 2: Memory Efficiency
    section_header("2. Generator vs List - Memory Efficiency")
    demonstrate_memory_efficiency()

    # Section 3: Generator Expressions
    section_header("3. Generator Expressions")
    demonstrate_generator_expressions()

    # Section 4: State
    section_header("4. Generator State and Exhaustion")
    demonstrate_generator_state()

    # Section 5: Infinite Generators
    section_header("5. Infinite Generators")
    demonstrate_infinite_generators()

    # Section 6: yield from
    section_header("6. Generator Delegation with 'yield from'")
    demonstrate_yield_from()

    # Section 7: send()
    section_header("7. Advanced: send() Method")
    demonstrate_send()

    # Section 8: throw()
    section_header("8. Advanced: throw() Method")
    demonstrate_throw()

    # Section 9: Pipeline
    section_header("9. Practical Use Case - Data Pipeline")
    demonstrate_pipeline()

    # Section 10: Return Values
    section_header("10. Generator Return Values")
    demonstrate_return_value()

    print("\n" + "=" * 70)
    print("  DEMONSTRATION COMPLETE")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
