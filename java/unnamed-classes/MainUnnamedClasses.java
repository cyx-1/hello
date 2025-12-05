// MainUnnamedClasses.java - Demonstrates Java's Unnamed Classes and Instance Main Methods
// This feature was introduced as a preview in Java 21 and finalized in Java 23
// Key benefits:
// 1. No need to declare an explicit class
// 2. main() can be an instance method (non-static)
// 3. Simplified syntax for beginners and quick prototyping

// Instance fields - can be used directly without 'static'
private String greeting = "Hello from Unnamed Classes!";
private int demonstrationStep = 0;

// Instance main method - note: NO 'static' keyword, NO 'String[] args' required
void main() {
    // Line 14: Starting the demonstration
    System.out.println("=== Java Unnamed Classes & Instance Main Methods Demo ===\n");

    // Line 17: Demonstrate instance field access
    demonstrateInstanceFields();

    // Line 20: Demonstrate instance methods
    demonstrateInstanceMethods();

    // Line 23: Demonstrate how this simplifies learning Java
    demonstrateSimplification();

    // Line 26: Show the actual class name
    demonstrateActualClassName();
}

// Instance method - can access instance fields directly
private void demonstrateInstanceFields() {
    demonstrationStep++;
    System.out.println("Step " + demonstrationStep + ": Instance Fields");
    System.out.println("  → Greeting field value: " + greeting);
    System.out.println("  → No 'static' keyword needed!");
    System.out.println();
}

// Instance method demonstrating object-oriented features
private void demonstrateInstanceMethods() {
    demonstrationStep++;
    System.out.println("Step " + demonstrationStep + ": Instance Methods");

    String message = createMessage("Unnamed Classes", "make Java simpler");
    System.out.println("  → " + message);

    // Call another instance method
    int result = calculate(5, 7);
    System.out.println("  → Calculation result: 5 + 7 = " + result);
    System.out.println();
}

private String createMessage(String subject, String verb) {
    return subject + " " + verb + "!";
}

private int calculate(int a, int b) {
    return a + b;
}

private void demonstrateSimplification() {
    demonstrationStep++;
    System.out.println("Step " + demonstrationStep + ": Code Simplification");
    System.out.println("  Traditional Java requires:");
    System.out.println("    public class HelloWorld {");
    System.out.println("        public static void main(String[] args) {");
    System.out.println("            System.out.println(\"Hello\");");
    System.out.println("        }");
    System.out.println("    }");
    System.out.println();
    System.out.println("  With Unnamed Classes, you can write:");
    System.out.println("    void main() {");
    System.out.println("        System.out.println(\"Hello\");");
    System.out.println("    }");
    System.out.println();
}

private void demonstrateActualClassName() {
    demonstrationStep++;
    System.out.println("Step " + demonstrationStep + ": Behind the Scenes");

    // The compiler creates a class with a special name
    System.out.println("  → Actual class name: " + this.getClass().getName());
    System.out.println("  → Is top-level class: " + (this.getClass().getEnclosingClass() == null));
    System.out.println("  → Package: " + (this.getClass().getPackage() != null ?
                                          this.getClass().getPackage().getName() : "default package"));
    System.out.println();

    System.out.println("Summary:");
    System.out.println("  ✓ No explicit class declaration needed");
    System.out.println("  ✓ main() is an instance method (non-static)");
    System.out.println("  ✓ Can use instance fields and methods");
    System.out.println("  ✓ Perfect for learning and quick prototypes");
    System.out.println("  ✓ Compiler generates the class structure automatically");
}
