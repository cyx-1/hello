# Unnamed Patterns and Variables in Java

This demonstration showcases the **Unnamed Patterns and Variables** feature introduced in Java 21 (JEP 443 - Preview) and finalized in Java 22.

## Overview

Unnamed patterns and variables use the underscore `_` to indicate that a variable or pattern is intentionally unused. This improves code readability by explicitly showing when a value is irrelevant to the logic.

## Requirements

**Required Java Version**: Java 21 or higher (with preview features enabled for Java 21, or Java 22+ for finalized feature)

## Running the Code

```bash
# Compile (Java 21 with preview)
javac --enable-preview --release 21 MainUnnamedPatternsVariables.java

# Run (Java 21 with preview)
java --enable-preview MainUnnamedPatternsVariables

# Or with Maven
mvn clean compile exec:java
```

## Key Source Code Sections

### 1. Unnamed Patterns in Switch Expressions (Lines 42-69)

```java
// Line 57: Using _ to ignore the matched value when we only care about the type
String description = switch (item) {
    case Integer _ -> "Integer type (value ignored)";
    case String _ -> "String type (value ignored)";
    case Circle _ -> "Circle type (value ignored)";
    case Rectangle _ -> "Rectangle type (value ignored)";
    case Double _ -> "Double type (value ignored)";
    default -> "Unknown type";
};
```

**Output:**
```
1. Unnamed Patterns in Switch Expressions
--------------------------------------------------
  Item: 42 -> Integer type (value ignored)
  Item: Hello -> String type (value ignored)
  Item: Circle[center=Point[x=0, y=0], radius=5.0] -> Circle type (value ignored)
  Item: Rectangle[topLeft=Point[x=0, y=0], bottomRight=Point[x=10, y=10]] -> Rectangle type (value ignored)
  Item: 3.14 -> Double type (value ignored)
```

**Annotation**: Lines 57-64 demonstrate type-only pattern matching. The underscore `_` explicitly indicates we only care about the type (Integer, String, Circle, etc.), not the actual value. This is cleaner than using a named variable that would go unused.

---

### 2. Unnamed Patterns in instanceof (Lines 71-93)

```java
// Line 78: Check type without binding to a variable
if (obj instanceof Circle _) {
    System.out.println("  Object is a Circle (but we don't need the value)");
}

// Line 83: Nested pattern with unnamed components
if (obj instanceof Circle(Point(int _, int _), double _)) {
    System.out.println("  Object is a Circle with Point and radius (all values ignored)");
}

// Line 88: Partial unnamed - keep some, ignore others
if (obj instanceof Circle(Point(int x, int _), double _)) {
    System.out.println("  Circle center x-coordinate: " + x);
}
```

**Output:**
```
2. Unnamed Patterns in instanceof
--------------------------------------------------
  Object is a Circle (but we don't need the value)
  Object is a Circle with Point and radius (all values ignored)
  Circle center x-coordinate: 5
```

**Annotation**:
- **Line 78**: Simple type check without needing to bind the matched object
- **Line 83**: Deconstructs a Circle record, but ignores all components (both Point coordinates and radius)
- **Line 88**: Selective extraction - only captures the x-coordinate while ignoring y and radius

---

### 3. Unnamed Variables in Try-With-Resources (Lines 95-107)

```java
// Line 100: Using _ when we need to create a resource but don't use it
try (var _ = new AutoCloseableResource("Resource-1");
     var _ = new AutoCloseableResource("Resource-2")) {
    System.out.println("  Resources created but variables not needed");
}
```

**Output:**
```
3. Unnamed Variables in Try-With-Resources
--------------------------------------------------
    Opening Resource-1
    Opening Resource-2
  Resources created but variables not needed
    Closing Resource-2
    Closing Resource-1
```

**Annotation**: Lines 100-102 show try-with-resources where we need the resources to be auto-closed but don't need to reference them within the block. The underscore makes it clear the variables are intentionally unused. Note the resources are closed in reverse order (LIFO).

---

### 4. Unnamed Variables in Catch Blocks (Lines 108-125)

```java
try {
    int result = 10 / 0;  // Line 114: Intentional division by zero
} catch (ArithmeticException _) {  // Line 115: Exception caught but not used
    System.out.println("  Caught ArithmeticException (exception object not needed)");
}

try {
    String s = null;
    s.length();  // Line 121: Intentional null pointer
} catch (NullPointerException _) {  // Line 122: Exception caught but not used
    System.out.println("  Caught NullPointerException (exception object not needed)");
}
```

**Output:**
```
4. Unnamed Variables in Catch Blocks
--------------------------------------------------
  Caught ArithmeticException (exception object not needed)
  Caught NullPointerException (exception object not needed)
```

**Annotation**: Lines 115 and 122 demonstrate catching exceptions when we only care about the exception type, not the exception object itself. This is common for simple error handling where the exception message or stack trace isn't needed.

---

### 5. Unnamed Variables in Lambda Expressions (Lines 126-146)

```java
// Line 130: Single unnamed parameter
java.util.function.Consumer<String> consumer1 = _ ->
    System.out.println("  Lambda with single unnamed parameter");
consumer1.accept("ignored value");

// Line 135: BiFunction where first parameter is unused
java.util.function.BiFunction<String, Integer, String> func =
    (_, count) -> "Count: " + count;
System.out.println("  " + func.apply("ignored", 42));

// Line 140: Multiple unnamed parameters
java.util.function.BiConsumer<String, String> consumer2 =
    (_, _) -> System.out.println("  Both parameters ignored");
consumer2.accept("first", "second");
```

**Output:**
```
5. Unnamed Variables in Lambda Expressions
--------------------------------------------------
  Lambda with single unnamed parameter
  Count: 42
  Both parameters ignored
```

**Annotation**:
- **Line 132**: Single-parameter lambda where the parameter is unused
- **Line 138**: BiFunction that only uses the second parameter (count), first is ignored
- **Line 143**: BiConsumer that ignores both parameters entirely

---

### 6. Unnamed Variables in For Loops (Lines 148-172)

```java
// Line 154: Enhanced for loop with unnamed variable
int[] numbers = {1, 2, 3, 4, 5};
int sum = 0;
System.out.println("  Processing array (elements ignored, just counting):");
for (int _ : numbers) {
    sum++;  // Line 159: Just counting, not using the values
}
System.out.println("    Array has " + sum + " elements");

// Line 163: Multiple unnamed variables in nested loops
System.out.println("  Nested loops with unnamed variables:");
for (String _ : new String[]{"A", "B", "C"}) {
    for (int _ : numbers) {
        System.out.print("*");  // Line 167: Both loop variables unused
    }
    System.out.println();
}
```

**Output:**
```
6. Unnamed Variables in For Loops
--------------------------------------------------
  Processing array (elements ignored, just counting):
    Array has 5 elements
  Nested loops with unnamed variables:
*****
*****
*****
```

**Annotation**:
- **Lines 158-161**: Enhanced for-loop that only counts elements without using their values
- **Lines 165-170**: Nested loops where both loop variables are unused - we're just using the loops for iteration count

**Note**: Unnamed variables can only be used in the declaration part of enhanced for-loops, not in traditional for-loop conditions or increment expressions.

---

### 7. Multiple Unnamed Variables (Lines 174-193)

```java
record Coordinate(int x, int y, int z) {}

Coordinate coord = new Coordinate(10, 20, 30);

// Line 180: Extract only the middle value
if (coord instanceof Coordinate(int _, int y, int _)) {
    System.out.println("  Y-coordinate: " + y + " (x and z ignored)");
}

// Line 185: Nested structures with multiple unnamed patterns
record Box(Coordinate position, String label) {}
Box box = new Box(new Coordinate(1, 2, 3), "Package");

if (box instanceof Box(Coordinate(int _, int y, int _), String _)) {
    System.out.println("  Box Y-position: " + y + " (other fields ignored)");
}
```

**Output:**
```
7. Multiple Unnamed Variables
--------------------------------------------------
  Y-coordinate: 20 (x and z ignored)
  Box Y-position: 2 (other fields ignored)
```

**Annotation**:
- **Line 180**: Demonstrates selective component extraction from a record - captures only the y-coordinate
- **Line 189**: Shows nested pattern matching with multiple levels of unnamed components - extracts only the y-coordinate from a Box's nested Coordinate while ignoring everything else

---

## Key Benefits

1. **Improved Readability**: Makes it explicit when a variable is intentionally unused
2. **Cleaner Code**: No need for dummy variable names like `ignored`, `unused`, or `temp`
3. **Pattern Matching**: Works seamlessly with record patterns and instanceof
4. **Compiler Support**: The compiler treats `_` as a special symbol, preventing accidental usage

## Complete Program Output

```
=== Unnamed Patterns and Variables Demo ===

1. Unnamed Patterns in Switch Expressions
--------------------------------------------------
  Item: 42 -> Integer type (value ignored)
  Item: Hello -> String type (value ignored)
  Item: Circle[center=Point[x=0, y=0], radius=5.0] -> Circle type (value ignored)
  Item: Rectangle[topLeft=Point[x=0, y=0], bottomRight=Point[x=10, y=10]] -> Rectangle type (value ignored)
  Item: 3.14 -> Double type (value ignored)

2. Unnamed Patterns in instanceof
--------------------------------------------------
  Object is a Circle (but we don't need the value)
  Object is a Circle with Point and radius (all values ignored)
  Circle center x-coordinate: 5

3. Unnamed Variables in Try-With-Resources
--------------------------------------------------
    Opening Resource-1
    Opening Resource-2
  Resources created but variables not needed
    Closing Resource-2
    Closing Resource-1

4. Unnamed Variables in Catch Blocks
--------------------------------------------------
  Caught ArithmeticException (exception object not needed)
  Caught NullPointerException (exception object not needed)

5. Unnamed Variables in Lambda Expressions
--------------------------------------------------
  Lambda with single unnamed parameter
  Count: 42
  Both parameters ignored

6. Unnamed Variables in For Loops
--------------------------------------------------
  Processing array (elements ignored, just counting):
    Array has 5 elements
  Nested loops with unnamed variables:
*****
*****
*****

7. Multiple Unnamed Variables
--------------------------------------------------
  Y-coordinate: 20 (x and z ignored)
  Box Y-position: 2 (other fields ignored)
```

## References

- [JEP 443: Unnamed Patterns and Variables (Preview)](https://openjdk.org/jeps/443) - Java 21
- [JEP 456: Unnamed Variables & Patterns](https://openjdk.org/jeps/456) - Java 22 (Finalized)
