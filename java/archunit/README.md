# ArchUnit Java Example

This example demonstrates **ArchUnit**, a Java library for testing and enforcing architectural rules in your codebase. ArchUnit allows you to write unit tests that check your architecture constraints, ensuring that your code follows the intended design patterns.

## Overview

ArchUnit enables you to:
- Enforce naming conventions
- Control dependencies between classes and packages
- Validate layered architecture
- Check class modifiers and field visibility
- Prevent circular dependencies
- Create custom architecture rules

## Requirements

- **Java 17** or higher
- **Maven** for dependency management
- **ArchUnit 1.3.0** (specified in pom.xml)

## Running the Example

```bash
cd java/archunit
mvn clean compile exec:java
```

## Source Code

### MainArchUnit.java (lines 1-90)

```java
     1  import com.tngtech.archunit.core.domain.JavaClasses;
     2  import com.tngtech.archunit.core.importer.ClassFileImporter;
     3  import com.tngtech.archunit.lang.ArchRule;
     4
     5  import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;
     6  import static com.tngtech.archunit.library.Architectures.layeredArchitecture;
```

**Lines 1-6**: Import ArchUnit core classes for:
- `JavaClasses`: Represents imported Java classes
- `ClassFileImporter`: Imports classes from the classpath
- `ArchRule`: Defines architecture rules
- Static imports for rule definition DSL

```java
    17  public class MainArchUnit {
    18
    19      // Example package structure for demonstration
    20      public static class SampleClasses {
    21
    22          // Controller Layer
    23          public static class UserController {
    24              private UserService userService;
    25
    26              public void handleRequest() {
    27                  System.out.println("Controller: Handling user request");
    28                  userService.processUser();
    29              }
    30          }
```

**Lines 22-30**: Define a sample Controller class that depends on a Service class, representing a typical layered architecture pattern.

```java
    44          // Service Layer
    45          public static class UserService {
    46              private UserRepository userRepository;
    47
    48              public void processUser() {
    49                  System.out.println("Service: Processing user");
    50                  userRepository.save();
    51              }
    52          }
```

**Lines 44-52**: Define a Service layer class that depends on a Repository, following the common three-tier architecture.

```java
    83      // Line 83-84: Import all classes from the current package
    84      JavaClasses importedClasses = new ClassFileImporter()
    85              .importPackages("MainArchUnit");
```

**Lines 84-85**: Import all classes for analysis using ArchUnit's `ClassFileImporter`. This scans the bytecode to analyze the structure.

### Rule 1: Naming Convention for Controllers (lines 90-103)

```java
    90      // Line 90-93: Rule 1 - Classes ending with 'Controller' should be in controller package
    91      ArchRule controllerNamingRule = classes()
    92              .that().haveSimpleNameEndingWith("Controller")
    93              .should().resideInAPackage("..controller..")
    94              .as("Controllers should reside in a controller package");
    95
    96      try {
    97          controllerNamingRule.check(importedClasses);
    98          System.out.println("✓ Controller naming rule: PASSED");
    99      } catch (AssertionError e) {
   100          System.out.println("✗ Controller naming rule: FAILED");
   101          System.out.println("  Reason: " + e.getMessage().split("\n")[0]);
   102      }
```

**Lines 91-94**: Define a rule that checks if classes with names ending in "Controller" are placed in a "controller" package. The `..` notation means any package depth.

**Lines 96-102**: Execute the rule and catch violations. This demonstrates ArchUnit's try-catch pattern for rule validation.

### Rule 2: Service Layer Naming (lines 106-119)

```java
   106      // Line 106-109: Rule 2 - Classes ending with 'Service' should be in service package
   107      ArchRule serviceNamingRule = classes()
   108              .that().haveSimpleNameEndingWith("Service")
   109              .should().resideInAPackage("..service..")
   110              .as("Services should reside in a service package");
```

**Lines 107-110**: Similar to Rule 1, but checks Service class placement.

### Rule 3: Repository Dependency Constraint (lines 126-142)

```java
   126      // Line 126-130: Rule 3 - Repository classes should not depend on Service classes
   127      ArchRule repositoryDependencyRule = noClasses()
   128              .that().haveSimpleNameEndingWith("Repository")
   129              .should().dependOnClassesThat().haveSimpleNameEndingWith("Service")
   130              .as("Repositories should not depend on services")
   131              .because("This would create a circular dependency");
   132
   133      try {
   134          repositoryDependencyRule.check(importedClasses);
   135          System.out.println("✓ Repository dependency rule: PASSED");
   136          System.out.println("  Repositories do not depend on Services");
   137      } catch (AssertionError e) {
   138          System.out.println("✗ Repository dependency rule: FAILED");
   139          System.out.println("  Reason: " + e.getMessage().split("\n")[0]);
   140      }
```

**Lines 127-131**: This rule prevents circular dependencies by ensuring Repositories don't depend on Services. The `because()` clause provides reasoning for the rule.

### Rule 4: Utility Class Access Control (lines 144-160)

```java
   144      // Line 144-148: Rule 4 - Classes with 'Utils' in name should only be accessed by specific layers
   145      ArchRule utilsAccessRule = classes()
   146              .that().haveSimpleNameContaining("Utils")
   147              .should().onlyBeAccessed().byClassesThat()
   148              .haveSimpleNameEndingWith("Service")
   149              .as("Utility classes should only be accessed by service layer");
```

**Lines 145-149**: Enforce that utility classes can only be accessed by the Service layer, preventing direct access from Controllers or Repositories.

### Rule 5: Layered Architecture Validation (lines 166-186)

```java
   166      // Line 166-174: Rule 5 - Enforce layered architecture
   167      ArchRule layeredArchitectureRule = layeredArchitecture()
   168              .consideringAllDependencies()
   169              .layer("Controller").definedBy("..controller..")
   170              .layer("Service").definedBy("..service..")
   171              .layer("Repository").definedBy("..repository..")
   172              .whereLayer("Controller").mayNotBeAccessedByAnyLayer()
   173              .whereLayer("Service").mayOnlyBeAccessedByLayers("Controller")
   174              .whereLayer("Repository").mayOnlyBeAccessedByLayers("Service")
   175              .as("Layered architecture should be respected");
```

**Lines 167-175**: This is ArchUnit's most powerful feature - defining and enforcing a complete layered architecture with:
- **Layer definitions**: Controller, Service, Repository
- **Access rules**: Controller → Service → Repository (one-way flow)
- Prevents layer violations like Repository → Service or Service → Controller

### Rule 6: Class Modifier Constraints (lines 192-205)

```java
   192      // Line 192-195: Rule 6 - Utility classes should be final
   193      ArchRule utilsFinalRule = classes()
   194              .that().haveSimpleNameContaining("Utils")
   195              .should().haveModifier(com.tngtech.archunit.core.domain.JavaModifier.FINAL)
   196              .as("Utility classes should be final");
```

**Lines 193-196**: Enforce that utility classes are declared final to prevent inheritance, following best practices for utility class design.

### Rule 7: Field Visibility Rules (lines 211-226)

```java
   211      // Line 211-214: Rule 7 - Fields should not be public
   212      ArchRule noPublicFieldsRule = noFields()
   213              .that().areDeclaredInClassesThat().haveSimpleNameEndingWith("Service")
   214              .should().bePublic()
   215              .as("Service classes should not have public fields");
```

**Lines 212-215**: Ensure proper encapsulation by preventing public fields in Service classes.

## Expected Output

```
======================================================================
ArchUnit Example - Testing Architecture Rules
======================================================================

1. NAMING CONVENTION RULES
----------------------------------------------------------------------
✗ Controller naming rule: FAILED
  Reason: Architecture Violation [Priority: MEDIUM] - Rule 'Controllers should reside in a controller package' was violated

✗ Service naming rule: FAILED
  Reason: Architecture Violation [Priority: MEDIUM] - Rule 'Services should reside in a service package' was violated

2. DEPENDENCY RULES
----------------------------------------------------------------------
✓ Repository dependency rule: PASSED
  Repositories do not depend on Services

✗ Utils access rule: FAILED
  Reason: Architecture Violation [Priority: MEDIUM] - Rule 'Utility classes should only be accessed by service layer' was violated

3. LAYERED ARCHITECTURE RULES
----------------------------------------------------------------------
✗ Layered architecture rule: FAILED
  Reason: Architecture Violation [Priority: MEDIUM] - Rule 'Layered architecture should be respected' was violated

4. CLASS MODIFIER RULES
----------------------------------------------------------------------
✗ Utils final rule: FAILED
  Reason: Utility classes should be declared final

5. FIELD RULES
----------------------------------------------------------------------
✓ No public fields rule: PASSED
  Service classes do not expose public fields

======================================================================
SUMMARY
======================================================================
ArchUnit allows you to:
  • Enforce naming conventions
  • Control dependencies between classes/packages
  • Validate layered architecture
  • Check class modifiers and field visibility
  • Prevent circular dependencies
  • Create custom architecture rules

Note: Some rules intentionally fail in this demo to show both
      passing and failing scenarios.
======================================================================
```

## Output Analysis

### ✗ Failed Rules (Intentional for demonstration)

1. **Controller naming rule** (Line 91-94): FAILED because `UserController` and `OrderController` are not in a `..controller..` package - they're nested classes in the main class for demo purposes.

2. **Service naming rule** (Line 107-110): FAILED because `UserService` and `OrderService` are not in a `..service..` package structure.

3. **Utils access rule** (Line 145-149): FAILED (if StringUtils were accessed improperly) - demonstrates access control enforcement.

4. **Layered architecture rule** (Line 167-175): FAILED because the nested class structure doesn't match the defined layer packages.

5. **Utils final rule** (Line 193-196): FAILED because `StringUtils` is not declared as `final`.

### ✓ Passed Rules

1. **Repository dependency rule** (Line 127-131): PASSED because Repository classes correctly don't depend on Service classes, preventing circular dependencies.

2. **No public fields rule** (Line 212-215): PASSED because Service classes properly use private fields for encapsulation.

## Real-World Usage

In a production environment, you would:

1. **Organize classes into proper packages**:
   ```
   com.example.controller/
   com.example.service/
   com.example.repository/
   ```

2. **Write ArchUnit tests as JUnit tests**:
   ```java
   @Test
   public void servicesCanOnlyBeAccessedByControllers() {
       layeredArchitectureRule.check(importedClasses);
   }
   ```

3. **Run tests in CI/CD** to enforce architecture rules automatically

4. **Customize rules** for your specific architecture patterns

## Key Concepts

### ArchRule DSL
ArchUnit uses a fluent API:
- `classes().that()...should()...` - Define rules about classes
- `noClasses().that()...should()...` - Define negative rules
- `fields().that()...should()...` - Define rules about fields
- `methods().that()...should()...` - Define rules about methods

### Package Matchers
- `..` - Any number of packages
- `*` - Single package wildcard
- `..controller..` - Any package containing "controller"

### Best Practices

1. **Start with layer rules** - Define and enforce your architecture layers first
2. **Add naming conventions** - Ensure consistent naming across the codebase
3. **Prevent circular dependencies** - Use dependency rules to maintain clean architecture
4. **Enforce encapsulation** - Check field visibility and class modifiers
5. **Make rules fail fast** - Run ArchUnit tests in CI/CD pipelines

## Benefits

- **Automated architecture enforcement** - No manual code reviews needed for architecture violations
- **Living documentation** - Architecture rules serve as executable documentation
- **Catch violations early** - Prevent architecture drift before it becomes technical debt
- **Team alignment** - Ensure all developers follow the same architectural patterns
- **Refactoring safety** - Detect when refactoring breaks architectural constraints

## Common Use Cases

1. **Layered architecture** - Enforce 3-tier, hexagonal, or clean architecture
2. **Module boundaries** - Prevent unwanted dependencies between modules
3. **Coding standards** - Enforce naming conventions and class design patterns
4. **Framework constraints** - Ensure Spring/Jakarta EE annotations are used correctly
5. **Security rules** - Verify security-sensitive classes are properly protected

## Additional Resources

- [ArchUnit Official Documentation](https://www.archunit.org/)
- [ArchUnit GitHub Repository](https://github.com/TNG/ArchUnit)
- [ArchUnit User Guide](https://www.archunit.org/userguide/html/000_Index.html)

---

**Note**: This example uses nested classes for simplicity. In a real application, classes would be organized into proper package structures to satisfy the architecture rules.
