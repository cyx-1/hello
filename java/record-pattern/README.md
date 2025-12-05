# Java Record Pattern Demonstration

This project demonstrates the **Record Pattern** feature in Java, which allows pattern matching to deconstruct record instances directly in pattern matching contexts.

## Requirements

**This code requires Java 21 or later.** Record patterns were introduced as a preview feature in Java 19 and became a finalized feature in Java 21.

## Running the Code

```bash
# Compile and run
javac MainRecordPattern.java
java MainRecordPattern

# Or using Maven
mvn clean compile exec:java
```

## Key Features Demonstrated

1. Basic record pattern matching with `instanceof`
2. Record patterns in switch expressions
3. Nested record pattern deconstruction
4. Pattern matching with guards (when clauses)
5. Exhaustive pattern matching with sealed types

---

## Source Code and Output Correlation

### 1. Record and Sealed Interface Definitions

**Source Code (Lines 3-9):**
```java
3     // Sealed interface for shape hierarchy
4     sealed interface Shape permits Circle, Rectangle, Point {}
5
6     // Define record types implementing Shape
7     record Point(int x, int y) implements Shape {}
8     record Circle(Point center, int radius) implements Shape {}
9     record Rectangle(Point topLeft, Point bottomRight) implements Shape {}
```

**Explanation:**
- Line 4: A **sealed interface** restricts which classes can implement it, enabling exhaustive pattern matching
- Lines 7-9: **Records** are immutable data carriers with automatically generated constructors, getters, equals, hashCode, and toString
- Records work seamlessly with pattern matching to deconstruct their components

---

### 2. Basic Record Pattern with instanceof

**Source Code (Lines 14-18, 61-65):**
```java
14         // Example 1: Basic Record Pattern with instanceof
15         System.out.println("1. Basic Record Pattern with instanceof:");
16         Point p1 = new Point(10, 20);
17         basicRecordPattern(p1);

...

61     static void basicRecordPattern(Object obj) {
62         if (obj instanceof Point(int x, int y)) {
63             System.out.println("  Point coordinates: x=" + x + ", y=" + y);
64         }
65     }
```

**Output:**
```
1. Basic Record Pattern with instanceof:
  Point coordinates: x=10, y=20
```

**Explanation:**
- Line 16: Creates a Point with coordinates (10, 20)
- Line 62: **Record pattern `Point(int x, int y)`** both tests if `obj` is a Point AND extracts its components
- The pattern automatically deconstructs the Point, binding `x=10` and `y=20`
- Without record patterns, you would need: `if (obj instanceof Point p)` then `p.x()` and `p.y()`

---

### 3. Record Patterns in Switch Expressions

**Source Code (Lines 20-29, 68-76):**
```java
20         // Example 2: Record Pattern in Switch Expression
21         System.out.println("2. Record Pattern in Switch Expression:");
22         Shape circle = new Circle(new Point(0, 0), 5);
23         Shape rectangle = new Rectangle(new Point(0, 0), new Point(10, 10));
24         Shape point = new Point(5, 5);
25
26         System.out.println("Circle area: " + calculateArea(circle));
27         System.out.println("Rectangle area: " + calculateArea(rectangle));
28         System.out.println("Point area: " + calculateArea(point));

...

68     static double calculateArea(Shape shape) {
69         return switch (shape) {
70             case Circle(Point center, int radius) ->
71                 Math.PI * radius * radius;
72             case Rectangle(Point(int x1, int y1), Point(int x2, int y2)) ->
73                 Math.abs((x2 - x1) * (y2 - y1));
74             case Point p -> 0.0;
75         };
76     }
```

**Output:**
```
2. Record Pattern in Switch Expression:
Circle area: 78.53981633974483
Rectangle area: 100.0
Point area: 0.0
```

**Explanation:**
- Line 22: Circle at origin (0,0) with radius 5
- Line 23: Rectangle from (0,0) to (10,10)
- Line 70: Pattern `Circle(Point center, int radius)` extracts the radius directly (5), calculating π×5² ≈ 78.54
- Line 72: **Nested pattern** `Rectangle(Point(int x1, int y1), Point(int x2, int y2))` deconstructs BOTH Point records within Rectangle
  - Extracts x1=0, y1=0 from topLeft and x2=10, y2=10 from bottomRight
  - Calculates area: |10-0| × |10-0| = 100
- Line 74: The switch is **exhaustive** because Shape is sealed and all cases are covered

---

### 4. Nested Record Pattern Extraction

**Source Code (Lines 31-35, 79-85):**
```java
31         // Example 3: Nested Record Patterns
32         System.out.println("3. Nested Record Patterns:");
33         Circle c1 = new Circle(new Point(3, 4), 10);
34         nestedRecordPattern(c1);

...

79     static void nestedRecordPattern(Circle circle) {
80         // Direct nested pattern matching
81         if (circle instanceof Circle(Point(int x, int y), int r)) {
82             System.out.println("  Circle with center at (" + x + ", " + y + ") and radius " + r);
83             System.out.println("  Distance from origin: " + Math.sqrt(x*x + y*y));
84         }
85     }
```

**Output:**
```
3. Nested Record Patterns:
  Circle with center at (3, 4) and radius 10
  Distance from origin: 5.0
```

**Explanation:**
- Line 33: Circle with center Point(3, 4) and radius 10
- Line 81: **Nested pattern** `Circle(Point(int x, int y), int r)` deconstructs in one step:
  - Extracts x=3, y=4 from the nested Point record
  - Extracts r=10 from the Circle
- Line 83: Calculates distance: √(3²+4²) = √25 = 5.0
- This demonstrates the power of record patterns: deep deconstruction in a single, readable pattern

---

### 5. Pattern Matching with Guards (when clauses)

**Source Code (Lines 37-43, 88-100):**
```java
37         // Example 4: Pattern Matching with Guards
38         System.out.println("4. Pattern Matching with Guards:");
39         describePoint(new Point(0, 0));
40         describePoint(new Point(5, 0));
41         describePoint(new Point(0, 7));
42         describePoint(new Point(3, 4));

...

88     static void describePoint(Point point) {
89         String description = switch (point) {
90             case Point(int x, int y) when x == 0 && y == 0 ->
91                 "  Origin point (0, 0)";
92             case Point(int x, int y) when x == 0 ->
93                 "  Point on Y-axis: (0, " + y + ")";
94             case Point(int x, int y) when y == 0 ->
95                 "  Point on X-axis: (" + x + ", 0)";
96             case Point(int x, int y) ->
97                 "  Point in quadrant: (" + x + ", " + y + ")";
98         };
99         System.out.println(description);
100    }
```

**Output:**
```
4. Pattern Matching with Guards:
  Origin point (0, 0)
  Point on X-axis: (5, 0)
  Point on Y-axis: (0, 7)
  Point in quadrant: (3, 4)
```

**Explanation:**
- Lines 90-97: **Guard clauses** (when conditions) refine pattern matching
- Line 39: Point(0, 0) matches line 90 (when x == 0 && y == 0) → "Origin point"
- Line 40: Point(5, 0) matches line 94 (when y == 0) → "Point on X-axis"
- Line 41: Point(0, 7) matches line 92 (when x == 0) → "Point on Y-axis"
- Line 42: Point(3, 4) falls through to line 96 (no guard) → "Point in quadrant"
- Guards are evaluated in order; the first matching pattern+guard wins

---

### 6. Complex Nested Patterns with Guards

**Source Code (Lines 45-51, 103-110):**
```java
45         // Example 5: Complex Nested Patterns
46         System.out.println("5. Complex Nested Patterns:");
47         Circle c2 = new Circle(new Point(0, 0), 5);
48         Circle c3 = new Circle(new Point(10, 10), 3);
49         checkCircleAtOrigin(c2);
50         checkCircleAtOrigin(c3);

...

103    static void checkCircleAtOrigin(Circle circle) {
104        switch (circle) {
105            case Circle(Point(int x, int y), int r) when x == 0 && y == 0 ->
106                System.out.println("  Circle centered at origin with radius " + r);
107            case Circle(Point(int x, int y), int r) ->
108                System.out.println("  Circle centered at (" + x + ", " + y + ") with radius " + r);
109        }
110    }
```

**Output:**
```
5. Complex Nested Patterns:
  Circle centered at origin with radius 5
  Circle centered at (10, 10) with radius 3
```

**Explanation:**
- Line 47: Circle at (0, 0) with radius 5
- Line 48: Circle at (10, 10) with radius 3
- Line 105: Combines **nested pattern** with **guard** to check if center is at origin
  - Circle from line 47 matches this case (x=0, y=0, r=5)
- Line 107: Catch-all for other circles
  - Circle from line 48 matches here (x=10, y=10, r=3)

---

### 7. Comprehensive Pattern Matching

**Source Code (Lines 53-58, 113-125):**
```java
53         // Example 6: Switch with Multiple Patterns
54         System.out.println("6. Switch with Multiple Patterns:");
55         printShapeInfo(new Point(1, 2));
56         printShapeInfo(new Circle(new Point(5, 5), 10));
57         printShapeInfo(new Rectangle(new Point(0, 0), new Point(20, 15)));

...

113    static void printShapeInfo(Shape shape) {
114        String info = switch (shape) {
115            case Point(int x, int y) ->
116                String.format("  Point at (%d, %d)", x, y);
117            case Circle(Point(int cx, int cy), int r) ->
118                String.format("  Circle: center=(%d, %d), radius=%d, area=%.2f",
119                    cx, cy, r, Math.PI * r * r);
120            case Rectangle(Point(int x1, int y1), Point(int x2, int y2)) ->
121                String.format("  Rectangle: corners=(%d, %d) to (%d, %d), area=%d",
122                    x1, y1, x2, y2, Math.abs((x2-x1)*(y2-y1)));
123        };
124        System.out.println(info);
125    }
```

**Output:**
```
6. Switch with Multiple Patterns:
  Point at (1, 2)
  Circle: center=(5, 5), radius=10, area=314.16
  Rectangle: corners=(0, 0) to (20, 15), area=300
```

**Explanation:**
- Line 55: Point(1, 2) → matches line 115, extracts x=1, y=2
- Line 56: Circle with center (5,5), radius 10 → matches line 117
  - Nested pattern extracts cx=5, cy=5, r=10
  - Calculates area: π×10² ≈ 314.16
- Line 57: Rectangle (0,0) to (20,15) → matches line 120
  - Double-nested pattern extracts all four coordinates: x1=0, y1=0, x2=20, y2=15
  - Calculates area: |20-0| × |15-0| = 300

---

## Benefits of Record Patterns

1. **Conciseness**: Extract multiple components in one pattern instead of multiple accessor calls
2. **Readability**: Pattern structure mirrors the record structure
3. **Type Safety**: Compiler ensures patterns match the record definition
4. **Exhaustiveness**: With sealed types, compiler verifies all cases are handled
5. **Nested Deconstruction**: Deep extraction without intermediate variables

## Version Note

This demonstration uses **Java 21** features:
- **Record Patterns** (finalized in Java 21, preview in Java 19-20)
- **Pattern Matching for Switch** (finalized in Java 21)
- **Sealed Types** (finalized in Java 17)

Attempting to compile with earlier versions will result in compilation errors.
