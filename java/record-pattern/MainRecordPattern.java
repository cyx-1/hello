public class MainRecordPattern {

    // Sealed interface for shape hierarchy
    sealed interface Shape permits Circle, Rectangle, Point {}

    // Define record types implementing Shape
    record Point(int x, int y) implements Shape {}
    record Circle(Point center, int radius) implements Shape {}
    record Rectangle(Point topLeft, Point bottomRight) implements Shape {}

    public static void main(String[] args) {
        System.out.println("=== Java Record Pattern Demonstration ===\n");

        // Example 1: Basic Record Pattern with instanceof
        System.out.println("1. Basic Record Pattern with instanceof:");
        Point p1 = new Point(10, 20);
        basicRecordPattern(p1);
        System.out.println();

        // Example 2: Record Pattern in Switch Expression
        System.out.println("2. Record Pattern in Switch Expression:");
        Shape circle = new Circle(new Point(0, 0), 5);
        Shape rectangle = new Rectangle(new Point(0, 0), new Point(10, 10));
        Shape point = new Point(5, 5);

        System.out.println("Circle area: " + calculateArea(circle));
        System.out.println("Rectangle area: " + calculateArea(rectangle));
        System.out.println("Point area: " + calculateArea(point));
        System.out.println();

        // Example 3: Nested Record Patterns
        System.out.println("3. Nested Record Patterns:");
        Circle c1 = new Circle(new Point(3, 4), 10);
        nestedRecordPattern(c1);
        System.out.println();

        // Example 4: Pattern Matching with Guards
        System.out.println("4. Pattern Matching with Guards:");
        describePoint(new Point(0, 0));
        describePoint(new Point(5, 0));
        describePoint(new Point(0, 7));
        describePoint(new Point(3, 4));
        System.out.println();

        // Example 5: Complex Nested Patterns
        System.out.println("5. Complex Nested Patterns:");
        Circle c2 = new Circle(new Point(0, 0), 5);
        Circle c3 = new Circle(new Point(10, 10), 3);
        checkCircleAtOrigin(c2);
        checkCircleAtOrigin(c3);
        System.out.println();

        // Example 6: Switch with Multiple Patterns
        System.out.println("6. Switch with Multiple Patterns:");
        printShapeInfo(new Point(1, 2));
        printShapeInfo(new Circle(new Point(5, 5), 10));
        printShapeInfo(new Rectangle(new Point(0, 0), new Point(20, 15)));
    }

    // Line 67: Basic record pattern matching
    static void basicRecordPattern(Object obj) {
        if (obj instanceof Point(int x, int y)) {
            System.out.println("  Point coordinates: x=" + x + ", y=" + y);
        }
    }

    // Line 74: Switch expression with record patterns
    static double calculateArea(Shape shape) {
        return switch (shape) {
            case Circle(Point center, int radius) ->
                Math.PI * radius * radius;
            case Rectangle(Point(int x1, int y1), Point(int x2, int y2)) ->
                Math.abs((x2 - x1) * (y2 - y1));
            case Point p -> 0.0;
        };
    }

    // Line 85: Nested record pattern extraction
    static void nestedRecordPattern(Circle circle) {
        // Direct nested pattern matching
        if (circle instanceof Circle(Point(int x, int y), int r)) {
            System.out.println("  Circle with center at (" + x + ", " + y + ") and radius " + r);
            System.out.println("  Distance from origin: " + Math.sqrt(x*x + y*y));
        }
    }

    // Line 94: Pattern matching with guards (when clauses)
    static void describePoint(Point point) {
        String description = switch (point) {
            case Point(int x, int y) when x == 0 && y == 0 ->
                "  Origin point (0, 0)";
            case Point(int x, int y) when x == 0 ->
                "  Point on Y-axis: (0, " + y + ")";
            case Point(int x, int y) when y == 0 ->
                "  Point on X-axis: (" + x + ", 0)";
            case Point(int x, int y) ->
                "  Point in quadrant: (" + x + ", " + y + ")";
        };
        System.out.println(description);
    }

    // Line 109: Complex nested pattern with specific values
    static void checkCircleAtOrigin(Circle circle) {
        switch (circle) {
            case Circle(Point(int x, int y), int r) when x == 0 && y == 0 ->
                System.out.println("  Circle centered at origin with radius " + r);
            case Circle(Point(int x, int y), int r) ->
                System.out.println("  Circle centered at (" + x + ", " + y + ") with radius " + r);
        }
    }

    // Line 119: Comprehensive shape information
    static void printShapeInfo(Shape shape) {
        String info = switch (shape) {
            case Point(int x, int y) ->
                String.format("  Point at (%d, %d)", x, y);
            case Circle(Point(int cx, int cy), int r) ->
                String.format("  Circle: center=(%d, %d), radius=%d, area=%.2f",
                    cx, cy, r, Math.PI * r * r);
            case Rectangle(Point(int x1, int y1), Point(int x2, int y2)) ->
                String.format("  Rectangle: corners=(%d, %d) to (%d, %d), area=%d",
                    x1, y1, x2, y2, Math.abs((x2-x1)*(y2-y1)));
        };
        System.out.println(info);
    }
}
