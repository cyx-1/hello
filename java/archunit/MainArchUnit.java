import com.tngtech.archunit.core.domain.JavaClasses;
import com.tngtech.archunit.core.importer.ClassFileImporter;
import com.tngtech.archunit.lang.ArchRule;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.*;
import static com.tngtech.archunit.library.Architectures.layeredArchitecture;

/**
 * ArchUnit Example - Testing Architecture Rules
 *
 * This example demonstrates how to use ArchUnit to enforce architectural
 * constraints and design rules in Java applications.
 */
public class MainArchUnit {

    // Example package structure for demonstration
    public static class SampleClasses {

        // Controller Layer
        public static class UserController {
            private UserService userService;

            public void handleRequest() {
                System.out.println("Controller: Handling user request");
                userService.processUser();
            }
        }

        public static class OrderController {
            private OrderService orderService;

            public void handleRequest() {
                System.out.println("Controller: Handling order request");
                orderService.processOrder();
            }
        }

        // Service Layer
        public static class UserService {
            private UserRepository userRepository;

            public void processUser() {
                System.out.println("Service: Processing user");
                userRepository.save();
            }
        }

        public static class OrderService {
            private OrderRepository orderRepository;

            public void processOrder() {
                System.out.println("Service: Processing order");
                orderRepository.save();
            }
        }

        // Repository Layer
        public static class UserRepository {
            public void save() {
                System.out.println("Repository: Saving user to database");
            }
        }

        public static class OrderRepository {
            public void save() {
                System.out.println("Repository: Saving order to database");
            }
        }

        // Utility classes
        public static class StringUtils {
            public static String formatString(String input) {
                return input.toUpperCase();
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("ArchUnit Example - Testing Architecture Rules");
        System.out.println("=".repeat(70));
        System.out.println();

        // Line 83-84: Import all classes from the current package
        JavaClasses importedClasses = new ClassFileImporter()
                .importPackages("MainArchUnit");

        System.out.println("1. NAMING CONVENTION RULES");
        System.out.println("-".repeat(70));

        // Line 90-93: Rule 1 - Classes ending with 'Controller' should be in controller package
        ArchRule controllerNamingRule = classes()
                .that().haveSimpleNameEndingWith("Controller")
                .should().resideInAPackage("..controller..")
                .as("Controllers should reside in a controller package");

        try {
            controllerNamingRule.check(importedClasses);
            System.out.println("✓ Controller naming rule: PASSED");
        } catch (AssertionError e) {
            System.out.println("✗ Controller naming rule: FAILED");
            System.out.println("  Reason: " + e.getMessage().split("\n")[0]);
        }
        System.out.println();

        // Line 106-109: Rule 2 - Classes ending with 'Service' should be in service package
        ArchRule serviceNamingRule = classes()
                .that().haveSimpleNameEndingWith("Service")
                .should().resideInAPackage("..service..")
                .as("Services should reside in a service package");

        try {
            serviceNamingRule.check(importedClasses);
            System.out.println("✓ Service naming rule: PASSED");
        } catch (AssertionError e) {
            System.out.println("✗ Service naming rule: FAILED");
            System.out.println("  Reason: " + e.getMessage().split("\n")[0]);
        }
        System.out.println();

        System.out.println("2. DEPENDENCY RULES");
        System.out.println("-".repeat(70));

        // Line 126-130: Rule 3 - Repository classes should not depend on Service classes
        ArchRule repositoryDependencyRule = noClasses()
                .that().haveSimpleNameEndingWith("Repository")
                .should().dependOnClassesThat().haveSimpleNameEndingWith("Service")
                .as("Repositories should not depend on services")
                .because("This would create a circular dependency");

        try {
            repositoryDependencyRule.check(importedClasses);
            System.out.println("✓ Repository dependency rule: PASSED");
            System.out.println("  Repositories do not depend on Services");
        } catch (AssertionError e) {
            System.out.println("✗ Repository dependency rule: FAILED");
            System.out.println("  Reason: " + e.getMessage().split("\n")[0]);
        }
        System.out.println();

        // Line 144-148: Rule 4 - Classes with 'Utils' in name should only be accessed by specific layers
        ArchRule utilsAccessRule = classes()
                .that().haveSimpleNameContaining("Utils")
                .should().onlyBeAccessed().byClassesThat()
                .haveSimpleNameEndingWith("Service")
                .as("Utility classes should only be accessed by service layer");

        try {
            utilsAccessRule.check(importedClasses);
            System.out.println("✓ Utils access rule: PASSED");
            System.out.println("  Utility classes are accessed only by services");
        } catch (AssertionError e) {
            System.out.println("✗ Utils access rule: FAILED");
            System.out.println("  Reason: " + e.getMessage().split("\n")[0]);
        }
        System.out.println();

        System.out.println("3. LAYERED ARCHITECTURE RULES");
        System.out.println("-".repeat(70));

        // Line 166-174: Rule 5 - Enforce layered architecture
        ArchRule layeredArchitectureRule = layeredArchitecture()
                .consideringAllDependencies()
                .layer("Controller").definedBy("..controller..")
                .layer("Service").definedBy("..service..")
                .layer("Repository").definedBy("..repository..")
                .whereLayer("Controller").mayNotBeAccessedByAnyLayer()
                .whereLayer("Service").mayOnlyBeAccessedByLayers("Controller")
                .whereLayer("Repository").mayOnlyBeAccessedByLayers("Service")
                .as("Layered architecture should be respected");

        try {
            layeredArchitectureRule.check(importedClasses);
            System.out.println("✓ Layered architecture rule: PASSED");
            System.out.println("  Layer dependencies are properly enforced");
        } catch (AssertionError e) {
            System.out.println("✗ Layered architecture rule: FAILED");
            System.out.println("  Reason: " + e.getMessage().split("\n")[0]);
        }
        System.out.println();

        System.out.println("4. CLASS MODIFIER RULES");
        System.out.println("-".repeat(70));

        // Line 192-195: Rule 6 - Utility classes should be final
        ArchRule utilsFinalRule = classes()
                .that().haveSimpleNameContaining("Utils")
                .should().haveModifier(com.tngtech.archunit.core.domain.JavaModifier.FINAL)
                .as("Utility classes should be final");

        try {
            utilsFinalRule.check(importedClasses);
            System.out.println("✓ Utils final rule: PASSED");
        } catch (AssertionError e) {
            System.out.println("✗ Utils final rule: FAILED");
            System.out.println("  Reason: Utility classes should be declared final");
        }
        System.out.println();

        System.out.println("5. FIELD RULES");
        System.out.println("-".repeat(70));

        // Line 211-214: Rule 7 - Fields should not be public
        ArchRule noPublicFieldsRule = noFields()
                .that().areDeclaredInClassesThat().haveSimpleNameEndingWith("Service")
                .should().bePublic()
                .as("Service classes should not have public fields");

        try {
            noPublicFieldsRule.check(importedClasses);
            System.out.println("✓ No public fields rule: PASSED");
            System.out.println("  Service classes do not expose public fields");
        } catch (AssertionError e) {
            System.out.println("✗ No public fields rule: FAILED");
            System.out.println("  Reason: " + e.getMessage().split("\n")[0]);
        }
        System.out.println();

        System.out.println("=".repeat(70));
        System.out.println("SUMMARY");
        System.out.println("=".repeat(70));
        System.out.println("ArchUnit allows you to:");
        System.out.println("  • Enforce naming conventions");
        System.out.println("  • Control dependencies between classes/packages");
        System.out.println("  • Validate layered architecture");
        System.out.println("  • Check class modifiers and field visibility");
        System.out.println("  • Prevent circular dependencies");
        System.out.println("  • Create custom architecture rules");
        System.out.println();
        System.out.println("Note: Some rules intentionally fail in this demo to show both");
        System.out.println("      passing and failing scenarios.");
        System.out.println("=".repeat(70));
    }
}
