import org.openrewrite.ExecutionContext;
import org.openrewrite.InMemoryExecutionContext;
import org.openrewrite.java.JavaParser;
import org.openrewrite.java.ChangeMethodName;
import org.openrewrite.java.ChangeType;
import org.openrewrite.Recipe;
import org.openrewrite.SourceFile;
import org.openrewrite.java.tree.J;

import java.nio.file.Paths;
import java.util.List;

/**
 * Demonstrates OpenRewrite's ability to use code to modify code.
 * This example shows how to programmatically transform Java source code
 * using OpenRewrite recipes and visitors.
 */
public class MainOpenRewrite {

    public static void main(String[] args) {
        System.out.println("=".repeat(80));
        System.out.println("OpenRewrite: Using Code to Modify Code");
        System.out.println("=".repeat(80));
        System.out.println();

        // Line 25-28: Define sample Java source code to transform
        String originalSource = """
            public class Example {
                public void process() {
                    java.util.ArrayList<String> list = new java.util.ArrayList<>();
                    list.add("Hello");
                    System.out.println("Processing: " + list.get(0));
                }

                public void oldMethodName() {
                    System.out.println("This method will be renamed");
                }
            }
            """;

        System.out.println("ORIGINAL SOURCE CODE:");
        System.out.println("-".repeat(80));
        System.out.println(originalSource);
        System.out.println();

        // Line 45-47: Create a Java parser to parse the source code
        ExecutionContext ctx = new InMemoryExecutionContext(t -> {
            t.printStackTrace();
        });

        JavaParser javaParser = JavaParser.fromJavaVersion()
            .build();

        // Line 53-54: Parse the source code into an AST
        List<SourceFile> sourceFiles = javaParser.parse(originalSource)
            .toList();

        if (sourceFiles.isEmpty()) {
            System.err.println("Failed to parse source code");
            return;
        }

        System.out.println("TRANSFORMATION 1: Change Method Name");
        System.out.println("-".repeat(80));
        // Line 65-68: Create a recipe to rename a method
        Recipe renameMethodRecipe = new ChangeMethodName(
            "Example oldMethodName()",
            "newMethodName",
            null,
            null
        );

        // Line 73-74: Apply the recipe to transform the code
        List<SourceFile> transformed1 = renameMethodRecipe.run(sourceFiles, ctx)
            .getChangeset()
            .getAllResults().stream()
            .map(result -> result.getAfter())
            .toList();

        if (!transformed1.isEmpty()) {
            System.out.println("Method 'oldMethodName' renamed to 'newMethodName':");
            System.out.println(transformed1.get(0).printAll());
        }
        System.out.println();

        System.out.println("TRANSFORMATION 2: Change Type Reference");
        System.out.println("-".repeat(80));
        // Line 89-92: Create a recipe to change ArrayList to LinkedList
        Recipe changeTypeRecipe = new ChangeType(
            "java.util.ArrayList",
            "java.util.LinkedList",
            null
        );

        // Line 97-98: Apply the type change recipe
        List<SourceFile> transformed2 = changeTypeRecipe.run(sourceFiles, ctx)
            .getChangeset()
            .getAllResults().stream()
            .map(result -> result.getAfter())
            .toList();

        if (!transformed2.isEmpty()) {
            System.out.println("ArrayList changed to LinkedList:");
            System.out.println(transformed2.get(0).printAll());
        }
        System.out.println();

        System.out.println("TRANSFORMATION 3: Combined Transformations");
        System.out.println("-".repeat(80));
        // Line 113-116: Apply multiple recipes in sequence
        List<SourceFile> currentFiles = sourceFiles;
        currentFiles = renameMethodRecipe.run(currentFiles, ctx)
            .getChangeset()
            .getAllResults().stream()
            .map(result -> result.getAfter())
            .toList();

        if (!currentFiles.isEmpty()) {
            currentFiles = changeTypeRecipe.run(currentFiles, ctx)
                .getChangeset()
                .getAllResults().stream()
                .map(result -> result.getAfter())
                .toList();
        }

        if (!currentFiles.isEmpty()) {
            System.out.println("Both transformations applied:");
            System.out.println(currentFiles.get(0).printAll());
        }
        System.out.println();

        System.out.println("=".repeat(80));
        System.out.println("KEY CONCEPTS:");
        System.out.println("=".repeat(80));
        System.out.println("1. OpenRewrite parses Java code into an Abstract Syntax Tree (AST)");
        System.out.println("2. Recipes define transformations to apply to the AST");
        System.out.println("3. ExecutionContext manages the transformation execution");
        System.out.println("4. Multiple recipes can be chained to perform complex refactorings");
        System.out.println("5. All transformations preserve formatting and comments where possible");
        System.out.println();
        System.out.println("This demonstrates 'code modifying code' - using Java to programmatically");
        System.out.println("transform and refactor other Java code automatically!");
        System.out.println("=".repeat(80));
    }
}
