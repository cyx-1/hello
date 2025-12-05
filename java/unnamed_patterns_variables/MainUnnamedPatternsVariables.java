/**
 * Demonstration of Unnamed Patterns and Variables (JEP 443)
 * Introduced in Java 21 as a preview feature, finalized in Java 22
 *
 * Unnamed patterns and variables use underscore (_) to indicate
 * that a variable or pattern is intentionally unused.
 */
public class MainUnnamedPatternsVariables {

    // Sample classes for demonstration
    record Point(int x, int y) {}
    record Circle(Point center, double radius) {}
    record Rectangle(Point topLeft, Point bottomRight) {}
    record Triangle(Point p1, Point p2, Point p3) {}

    public static void main(String[] args) {
        System.out.println("=== Unnamed Patterns and Variables Demo ===\n");

        // Demo 1: Unnamed patterns in switch expressions
        demonstrateUnnamedPatternsInSwitch();

        // Demo 2: Unnamed patterns in instanceof
        demonstrateUnnamedPatternsInInstanceof();

        // Demo 3: Unnamed variables in try-with-resources
        demonstrateUnnamedVariablesInTry();

        // Demo 4: Unnamed variables in catch blocks
        demonstrateUnnamedVariablesInCatch();

        // Demo 5: Unnamed variables in lambda expressions
        demonstrateUnnamedVariablesInLambda();

        // Demo 6: Unnamed variables in for loops
        demonstrateUnnamedVariablesInForLoop();

        // Demo 7: Multiple unnamed variables
        demonstrateMultipleUnnamedVariables();
    }

    // Line 42: Demonstrate unnamed patterns in switch expressions
    static void demonstrateUnnamedPatternsInSwitch() {
        System.out.println("1. Unnamed Patterns in Switch Expressions");
        System.out.println("-".repeat(50));

        Object[] items = {
            42,
            "Hello",
            new Circle(new Point(0, 0), 5.0),
            new Rectangle(new Point(0, 0), new Point(10, 10)),
            3.14
        };

        for (Object item : items) {
            // Line 57: Using _ to ignore the matched value when we only care about the type
            String description = switch (item) {
                case Integer _ -> "Integer type (value ignored)";
                case String _ -> "String type (value ignored)";
                case Circle _ -> "Circle type (value ignored)";
                case Rectangle _ -> "Rectangle type (value ignored)";
                case Double _ -> "Double type (value ignored)";
                default -> "Unknown type";
            };
            System.out.println("  Item: " + item + " -> " + description);
        }
        System.out.println();
    }

    // Line 71: Demonstrate unnamed patterns in instanceof
    static void demonstrateUnnamedPatternsInInstanceof() {
        System.out.println("2. Unnamed Patterns in instanceof");
        System.out.println("-".repeat(50));

        Object obj = new Circle(new Point(5, 5), 10.0);

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
        System.out.println();
    }

    // Line 95: Demonstrate unnamed variables in try-with-resources
    static void demonstrateUnnamedVariablesInTry() {
        System.out.println("3. Unnamed Variables in Try-With-Resources");
        System.out.println("-".repeat(50));

        // Line 100: Using _ when we need to create a resource but don't use it
        try (var _ = new AutoCloseableResource("Resource-1");
             var _ = new AutoCloseableResource("Resource-2")) {
            System.out.println("  Resources created but variables not needed");
        }
        System.out.println();
    }

    // Line 108: Demonstrate unnamed variables in catch blocks
    static void demonstrateUnnamedVariablesInCatch() {
        System.out.println("4. Unnamed Variables in Catch Blocks");
        System.out.println("-".repeat(50));

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
        System.out.println();
    }

    // Line 125: Demonstrate unnamed variables in lambda expressions
    static void demonstrateUnnamedVariablesInLambda() {
        System.out.println("5. Unnamed Variables in Lambda Expressions");
        System.out.println("-".repeat(50));

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
        System.out.println();
    }

    // Line 149: Demonstrate unnamed variables in for loops
    static void demonstrateUnnamedVariablesInForLoop() {
        System.out.println("6. Unnamed Variables in For Loops");
        System.out.println("-".repeat(50));

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
        System.out.println();
    }

    // Line 171: Demonstrate multiple unnamed variables
    static void demonstrateMultipleUnnamedVariables() {
        System.out.println("7. Multiple Unnamed Variables");
        System.out.println("-".repeat(50));

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
        System.out.println();
    }

    // Helper class for try-with-resources demo
    static class AutoCloseableResource implements AutoCloseable {
        private final String name;

        // Line 199
        AutoCloseableResource(String name) {
            this.name = name;
            System.out.println("    Opening " + name);
        }

        @Override
        public void close() {
            System.out.println("    Closing " + name);  // Line 207
        }
    }
}
