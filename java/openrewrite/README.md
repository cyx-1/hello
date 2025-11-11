# Java OpenRewrite: Using Code to Modify Code

This example demonstrates OpenRewrite, a powerful tool that allows you to programmatically transform and refactor Java source code. OpenRewrite uses recipes and visitors to perform automated code modifications at scale.

## What is OpenRewrite?

OpenRewrite is a refactoring tool that:
- Parses Java code into an Abstract Syntax Tree (AST)
- Applies transformation recipes to the AST
- Generates modified source code while preserving formatting
- Enables "code that modifies code" through programmatic transformations

## Requirements

- **Java Version**: Java 17 or higher
- **OpenRewrite Version**: 8.40.2
- **Maven**: 3.6 or higher

## Source Code

### MainOpenRewrite.java

```java
1   import org.openrewrite.ExecutionContext;
2   import org.openrewrite.InMemoryExecutionContext;
3   import org.openrewrite.java.JavaParser;
4   import org.openrewrite.java.ChangeMethodName;
5   import org.openrewrite.java.ChangeType;
6   import org.openrewrite.Recipe;
7   import org.openrewrite.SourceFile;
8   import org.openrewrite.java.tree.J;
9
10  import java.nio.file.Paths;
11  import java.util.List;
12
13  /**
14   * Demonstrates OpenRewrite's ability to use code to modify code.
15   * This example shows how to programmatically transform Java source code
16   * using OpenRewrite recipes and visitors.
17   */
18  public class MainOpenRewrite {
19
20      public static void main(String[] args) {
21          System.out.println("=".repeat(80));
22          System.out.println("OpenRewrite: Using Code to Modify Code");
23          System.out.println("=".repeat(80));
24          System.out.println();
25
26          // Line 25-28: Define sample Java source code to transform
27          String originalSource = """
28              public class Example {
29                  public void process() {
30                      java.util.ArrayList<String> list = new java.util.ArrayList<>();
31                      list.add("Hello");
32                      System.out.println("Processing: " + list.get(0));
33                  }
34
35                  public void oldMethodName() {
36                      System.out.println("This method will be renamed");
37                  }
38              }
39              """;
40
41          System.out.println("ORIGINAL SOURCE CODE:");
42          System.out.println("-".repeat(80));
43          System.out.println(originalSource);
44          System.out.println();
45
46          // Line 45-47: Create a Java parser to parse the source code
47          ExecutionContext ctx = new InMemoryExecutionContext(t -> {
48              t.printStackTrace();
49          });
50
51          JavaParser javaParser = JavaParser.fromJavaVersion()
52              .build();
53
54          // Line 53-54: Parse the source code into an AST
55          List<SourceFile> sourceFiles = javaParser.parse(originalSource)
56              .toList();
57
58          if (sourceFiles.isEmpty()) {
59              System.err.println("Failed to parse source code");
60              return;
61          }
62
63          System.out.println("TRANSFORMATION 1: Change Method Name");
64          System.out.println("-".repeat(80));
65          // Line 65-68: Create a recipe to rename a method
66          Recipe renameMethodRecipe = new ChangeMethodName(
67              "Example oldMethodName()",
68              "newMethodName",
69              null,
70              null
71          );
72
73          // Line 73-74: Apply the recipe to transform the code
74          List<SourceFile> transformed1 = renameMethodRecipe.run(sourceFiles, ctx)
75              .getChangeset()
76              .getAllResults().stream()
77              .map(result -> result.getAfter())
78              .toList();
79
80          if (!transformed1.isEmpty()) {
81              System.out.println("Method 'oldMethodName' renamed to 'newMethodName':");
82              System.out.println(transformed1.get(0).printAll());
83          }
84          System.out.println();
85
86          System.out.println("TRANSFORMATION 2: Change Type Reference");
87          System.out.println("-".repeat(80));
88          // Line 89-92: Create a recipe to change ArrayList to LinkedList
89          Recipe changeTypeRecipe = new ChangeType(
90              "java.util.ArrayList",
91              "java.util.LinkedList",
92              null
93          );
94
95          // Line 97-98: Apply the type change recipe
96          List<SourceFile> transformed2 = changeTypeRecipe.run(sourceFiles, ctx)
97              .getChangeset()
98              .getAllResults().stream()
99              .map(result -> result.getAfter())
100         .toList();
101
102         if (!transformed2.isEmpty()) {
103             System.out.println("ArrayList changed to LinkedList:");
104             System.out.println(transformed2.get(0).printAll());
105         }
106         System.out.println();
107
108         System.out.println("TRANSFORMATION 3: Combined Transformations");
109         System.out.println("-".repeat(80));
110         // Line 113-116: Apply multiple recipes in sequence
111         List<SourceFile> currentFiles = sourceFiles;
112         currentFiles = renameMethodRecipe.run(currentFiles, ctx)
113             .getChangeset()
114             .getAllResults().stream()
115             .map(result -> result.getAfter())
116             .toList();
117
118         if (!currentFiles.isEmpty()) {
119             currentFiles = changeTypeRecipe.run(currentFiles, ctx)
120                 .getChangeset()
121                 .getAllResults().stream()
122                 .map(result -> result.getAfter())
123                 .toList();
124         }
125
126         if (!currentFiles.isEmpty()) {
127             System.out.println("Both transformations applied:");
128             System.out.println(currentFiles.get(0).printAll());
129         }
130         System.out.println();
131
132         System.out.println("=".repeat(80));
133         System.out.println("KEY CONCEPTS:");
134         System.out.println("=".repeat(80));
135         System.out.println("1. OpenRewrite parses Java code into an Abstract Syntax Tree (AST)");
136         System.out.println("2. Recipes define transformations to apply to the AST");
137         System.out.println("3. ExecutionContext manages the transformation execution");
138         System.out.println("4. Multiple recipes can be chained to perform complex refactorings");
139         System.out.println("5. All transformations preserve formatting and comments where possible");
140         System.out.println();
141         System.out.println("This demonstrates 'code modifying code' - using Java to programmatically");
142         System.out.println("transform and refactor other Java code automatically!");
143         System.out.println("=".repeat(80));
144     }
145 }
```

## Expected Program Output

```
================================================================================
OpenRewrite: Using Code to Modify Code
================================================================================

ORIGINAL SOURCE CODE:
--------------------------------------------------------------------------------
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

TRANSFORMATION 1: Change Method Name
--------------------------------------------------------------------------------
Method 'oldMethodName' renamed to 'newMethodName':
public class Example {
    public void process() {
        java.util.ArrayList<String> list = new java.util.ArrayList<>();
        list.add("Hello");
        System.out.println("Processing: " + list.get(0));
    }

    public void newMethodName() {
        System.out.println("This method will be renamed");
    }
}

TRANSFORMATION 2: Change Type Reference
--------------------------------------------------------------------------------
ArrayList changed to LinkedList:
public class Example {
    public void process() {
        java.util.LinkedList<String> list = new java.util.LinkedList<>();
        list.add("Hello");
        System.out.println("Processing: " + list.get(0));
    }

    public void oldMethodName() {
        System.out.println("This method will be renamed");
    }
}

TRANSFORMATION 3: Combined Transformations
--------------------------------------------------------------------------------
Both transformations applied:
public class Example {
    public void process() {
        java.util.LinkedList<String> list = new java.util.LinkedList<>();
        list.add("Hello");
        System.out.println("Processing: " + list.get(0));
    }

    public void newMethodName() {
        System.out.println("This method will be renamed");
    }
}

================================================================================
KEY CONCEPTS:
================================================================================
1. OpenRewrite parses Java code into an Abstract Syntax Tree (AST)
2. Recipes define transformations to apply to the AST
3. ExecutionContext manages the transformation execution
4. Multiple recipes can be chained to perform complex refactorings
5. All transformations preserve formatting and comments where possible

This demonstrates 'code modifying code' - using Java to programmatically
transform and refactor other Java code automatically!
================================================================================
```

## Code Annotations and Explanation

### Initial Setup (Lines 26-56)

**Lines 27-39**: Define the original Java source code as a string
- This is the code we want to transform
- Contains an `ArrayList` declaration (line 30)
- Contains a method named `oldMethodName` (line 35)

**Lines 47-49**: Create an ExecutionContext
- ExecutionContext manages the transformation execution
- Handles errors and provides runtime context for recipes

**Lines 51-56**: Parse the source code
- `JavaParser.fromJavaVersion().build()` creates a parser for the current Java version
- `parse(originalSource)` converts the string into an Abstract Syntax Tree (AST)
- The AST is represented as a list of `SourceFile` objects

### Transformation 1: Method Renaming (Lines 63-84)

**Lines 66-71**: Create a ChangeMethodName recipe
- `"Example oldMethodName()"` - the method signature to find
- `"newMethodName"` - the new name for the method
- This recipe will find the method and rename it throughout the codebase

**Lines 74-78**: Apply the recipe
- `renameMethodRecipe.run(sourceFiles, ctx)` executes the transformation
- `.getChangeset()` retrieves the changes made
- `.getAllResults()` gets all modified files
- `.map(result -> result.getAfter())` extracts the transformed source code

**Output**: The method `oldMethodName` is renamed to `newMethodName` (see line 35 → line 35 in output)

### Transformation 2: Type Change (Lines 86-106)

**Lines 89-93**: Create a ChangeType recipe
- `"java.util.ArrayList"` - the type to find and replace
- `"java.util.LinkedList"` - the replacement type
- This recipe changes all references to ArrayList to LinkedList

**Lines 96-100**: Apply the type change recipe
- Same pattern as Transformation 1
- Walks the AST and replaces type references

**Output**: All `ArrayList` references become `LinkedList` (see line 30 in original → line 30 in output)

### Transformation 3: Combined Changes (Lines 108-130)

**Lines 112-124**: Chain multiple transformations
- First apply the method rename recipe
- Then apply the type change recipe to the already-transformed code
- This demonstrates how multiple refactorings can be composed

**Output**: Both changes are applied together:
- `ArrayList` → `LinkedList`
- `oldMethodName` → `newMethodName`

## Key Concepts

1. **Abstract Syntax Tree (AST)**: OpenRewrite parses code into a tree structure representing the program's syntax
2. **Recipes**: Reusable transformations that can be applied to any codebase
3. **Immutability**: Each transformation creates a new version of the code, leaving the original unchanged
4. **Composition**: Multiple recipes can be chained together for complex refactorings
5. **Type-Safe**: All transformations are type-aware and maintain code correctness

## Running the Example

To run this example:

```bash
cd java/openrewrite
mvn clean compile exec:java
```

Or compile and run manually:

```bash
mvn compile
mvn exec:java -Dexec.mainClass="MainOpenRewrite"
```

## Real-World Use Cases

OpenRewrite is used for:
- **Framework Migrations**: Automatically upgrade Spring Boot, Jakarta EE, etc.
- **Dependency Updates**: Update library APIs when dependencies change
- **Code Modernization**: Convert old patterns to modern Java idioms
- **Security Fixes**: Apply security patches across entire codebases
- **Style Enforcement**: Standardize code formatting and conventions
- **Refactoring at Scale**: Rename, move, or restructure code across thousands of files

## Why OpenRewrite?

Traditional find-and-replace is fragile and can break code. OpenRewrite:
- Understands Java syntax and semantics
- Maintains type correctness
- Preserves comments and formatting
- Works across entire projects consistently
- Can be automated in CI/CD pipelines

This demonstration shows the fundamental concept: **using code to intelligently modify other code** - the essence of automated refactoring!
