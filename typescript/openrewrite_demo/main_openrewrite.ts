/**
 * OpenRewrite TypeScript Demonstration
 *
 * OpenRewrite is an automated refactoring tool that uses the Lossless Semantic Tree (LST)
 * to transform code while preserving formatting and comments.
 *
 * This demo illustrates common TypeScript refactoring patterns that OpenRewrite can perform
 * using the rewrite-javascript module.
 */

import * as ts from 'typescript';

// ============================================================================
// Section 1: Code Examples Before OpenRewrite Transformation
// ============================================================================

namespace BeforeRefactoring {
    // Example 1: Old-style var declarations (should be let/const)
    function demonstrateVarUsage() {
        console.log("[Line 19] === Before: Using 'var' declarations ===");
        var counter = 0; // Should be 'let' or 'const'
        var message = "Hello World"; // Should be 'const'

        for (var i = 0; i < 3; i++) { // 'var' in loop
            counter++;
        }

        console.log(`[Line 27] counter: ${counter}, message: ${message}`);
    }

    // Example 2: Callback-style promises (should be async/await)
    function demonstrateCallbackStyle() {
        console.log("\n[Line 32] === Before: Callback-style Promise ===");

        fetchUserData(1)
            .then(user => {
                console.log(`[Line 36] User fetched: ${user.name}`);
                return fetchUserOrders(user.id);
            })
            .then(orders => {
                console.log(`[Line 40] Orders count: ${orders.length}`);
            })
            .catch(error => {
                console.log(`[Line 43] Error: ${error}`);
            });
    }

    // Example 3: CommonJS require (should be ES6 import)
    function demonstrateCommonJS() {
        console.log("\n[Line 49] === Before: CommonJS require ===");
        // Simulated: const fs = require('fs');
        // Simulated: const path = require('path');
        console.log("[Line 52] Using CommonJS require statements");
    }

    // Example 4: Array.prototype methods with verbose syntax
    function demonstrateVerboseArrayOps() {
        console.log("\n[Line 57] === Before: Verbose array operations ===");

        const numbers = [1, 2, 3, 4, 5];

        // Verbose filter + map
        const result = numbers.filter(function(n) {
            return n % 2 === 0;
        }).map(function(n) {
            return n * 2;
        });

        console.log(`[Line 68] Filtered and mapped: ${result}`);
    }

    // Example 5: String concatenation (should be template literals)
    function demonstrateStringConcat() {
        console.log("\n[Line 73] === Before: String concatenation ===");

        const firstName = "John";
        const lastName = "Doe";
        const age = 30;

        const greeting = "Hello, " + firstName + " " + lastName + "! You are " + age + " years old.";
        console.log(`[Line 80] ${greeting}`);
    }

    export function runAll() {
        demonstrateVarUsage();
        demonstrateCallbackStyle();
        demonstrateCommonJS();
        demonstrateVerboseArrayOps();
        demonstrateStringConcat();
    }
}

// ============================================================================
// Section 2: Code Examples After OpenRewrite Transformation
// ============================================================================

namespace AfterRefactoring {
    // Example 1: Modern let/const declarations
    function demonstrateModernDeclarations() {
        console.log("\n[Line 100] === After: Using 'let' and 'const' ===");
        let counter = 0; // Changed from 'var' to 'let'
        const message = "Hello World"; // Changed from 'var' to 'const'

        for (let i = 0; i < 3; i++) { // Changed from 'var' to 'let'
            counter++;
        }

        console.log(`[Line 108] counter: ${counter}, message: ${message}`);
    }

    // Example 2: Async/await style
    async function demonstrateAsyncAwait() {
        console.log("\n[Line 113] === After: Async/await style ===");

        try {
            const user = await fetchUserData(1);
            console.log(`[Line 117] User fetched: ${user.name}`);

            const orders = await fetchUserOrders(user.id);
            console.log(`[Line 120] Orders count: ${orders.length}`);
        } catch (error) {
            console.log(`[Line 122] Error: ${error}`);
        }
    }

    // Example 3: ES6 imports
    function demonstrateES6Imports() {
        console.log("\n[Line 128] === After: ES6 imports ===");
        // Transformed: import * as fs from 'fs';
        // Transformed: import * as path from 'path';
        console.log("[Line 131] Using ES6 import statements");
    }

    // Example 4: Concise arrow functions
    function demonstrateConciseArrayOps() {
        console.log("\n[Line 136] === After: Concise arrow functions ===");

        const numbers = [1, 2, 3, 4, 5];

        // Concise filter + map with arrow functions
        const result = numbers
            .filter(n => n % 2 === 0)
            .map(n => n * 2);

        console.log(`[Line 145] Filtered and mapped: ${result}`);
    }

    // Example 5: Template literals
    function demonstrateTemplateLiterals() {
        console.log("\n[Line 150] === After: Template literals ===");

        const firstName = "John";
        const lastName = "Doe";
        const age = 30;

        const greeting = `Hello, ${firstName} ${lastName}! You are ${age} years old.`;
        console.log(`[Line 157] ${greeting}`);
    }

    export function runAll() {
        demonstrateModernDeclarations();
        demonstrateAsyncAwait();
        demonstrateES6Imports();
        demonstrateConciseArrayOps();
        demonstrateTemplateLiterals();
    }
}

// ============================================================================
// Section 3: OpenRewrite Visitor Pattern Simulation
// ============================================================================

class TypeScriptRefactoringVisitor {
    private transformations: string[] = [];

    visitSourceFile(sourceCode: string): void {
        console.log("\n[Line 177] === OpenRewrite Visitor Pattern ===");
        console.log("[Line 178] Analyzing source code using Lossless Semantic Tree (LST)...");

        this.detectVarDeclarations(sourceCode);
        this.detectStringConcatenation(sourceCode);
        this.detectCallbackPromises(sourceCode);
        this.detectCommonJS(sourceCode);

        console.log(`\n[Line 186] Total transformations detected: ${this.transformations.length}`);
        this.transformations.forEach((t, i) => {
            console.log(`[Line 188] ${i + 1}. ${t}`);
        });
    }

    private detectVarDeclarations(code: string): void {
        const varMatches = code.match(/\bvar\s+\w+/g);
        if (varMatches) {
            this.transformations.push(`Found ${varMatches.length} 'var' declarations → Convert to 'let' or 'const'`);
        }
    }

    private detectStringConcatenation(code: string): void {
        const concatMatches = code.match(/"\s*\+\s*\w+\s*\+\s*"/g);
        if (concatMatches) {
            this.transformations.push(`Found string concatenations → Convert to template literals`);
        }
    }

    private detectCallbackPromises(code: string): void {
        const thenMatches = code.match(/\.then\s*\(/g);
        if (thenMatches && thenMatches.length > 1) {
            this.transformations.push(`Found promise chains → Convert to async/await`);
        }
    }

    private detectCommonJS(code: string): void {
        const requireMatches = code.match(/require\s*\(\s*['"][^'"]+['"]\s*\)/g);
        if (requireMatches) {
            this.transformations.push(`Found ${requireMatches.length} CommonJS requires → Convert to ES6 imports`);
        }
    }

    getTransformations(): string[] {
        return this.transformations;
    }
}

// ============================================================================
// Section 4: Demonstration of OpenRewrite Recipe Execution
// ============================================================================

class OpenRewriteRecipeEngine {
    executeRecipe(recipeName: string, code: string): void {
        console.log(`\n[Line 233] === Executing Recipe: ${recipeName} ===`);

        const visitor = new TypeScriptRefactoringVisitor();
        visitor.visitSourceFile(code);

        console.log(`[Line 238] Recipe '${recipeName}' completed successfully`);
        console.log("[Line 239] Generated patch file with transformations");
    }

    listAvailableRecipes(): void {
        console.log("\n[Line 243] === Available OpenRewrite Recipes for TypeScript ===");

        const recipes = [
            "org.openrewrite.javascript.ConvertVarToLet",
            "org.openrewrite.javascript.UseTemplateLiterals",
            "org.openrewrite.javascript.ConvertToArrowFunctions",
            "org.openrewrite.javascript.CommonJSToESModule",
            "org.openrewrite.javascript.PromisesToAsyncAwait",
            "org.openrewrite.javascript.cleanup.AddOptionalChaining",
            "org.openrewrite.javascript.cleanup.RemoveUnusedImports",
            "org.openrewrite.codemods.ESLintTypeScriptDefaults"
        ];

        recipes.forEach((recipe, index) => {
            console.log(`[Line 257] ${index + 1}. ${recipe}`);
        });
    }
}

// ============================================================================
// Helper Functions (Simulated async operations)
// ============================================================================

interface User {
    id: number;
    name: string;
    email: string;
}

interface Order {
    id: number;
    userId: number;
    product: string;
    amount: number;
}

function fetchUserData(userId: number): Promise<User> {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                id: userId,
                name: "Alice Johnson",
                email: "alice@example.com"
            });
        }, 100);
    });
}

function fetchUserOrders(userId: number): Promise<Order[]> {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve([
                { id: 1, userId, product: "Laptop", amount: 1200 },
                { id: 2, userId, product: "Mouse", amount: 25 },
                { id: 3, userId, product: "Keyboard", amount: 75 }
            ]);
        }, 100);
    });
}

// ============================================================================
// Main Demonstration
// ============================================================================

async function main(): Promise<void> {
    console.log("╔════════════════════════════════════════════════════════════════╗");
    console.log("║     OpenRewrite TypeScript Transformation Demonstration        ║");
    console.log("╚════════════════════════════════════════════════════════════════╝");

    console.log("\n[Line 316] OpenRewrite uses the Lossless Semantic Tree (LST) to:");
    console.log("[Line 317] 1. Parse source code while preserving all formatting");
    console.log("[Line 318] 2. Apply transformation recipes using visitors");
    console.log("[Line 319] 3. Generate refactored code with original style intact");

    // Part 1: Show code BEFORE refactoring
    console.log("\n" + "=".repeat(70));
    console.log("PART 1: CODE PATTERNS BEFORE OPENREWRITE TRANSFORMATION");
    console.log("=".repeat(70));
    BeforeRefactoring.runAll();

    // Part 2: Show code AFTER refactoring
    console.log("\n" + "=".repeat(70));
    console.log("PART 2: CODE PATTERNS AFTER OPENREWRITE TRANSFORMATION");
    console.log("=".repeat(70));
    await AfterRefactoring.runAll();

    // Part 3: Demonstrate visitor pattern
    console.log("\n" + "=".repeat(70));
    console.log("PART 3: OPENREWRITE VISITOR PATTERN");
    console.log("=".repeat(70));

    const sampleCode = `
        var counter = 0;
        var message = "Hello";
        const greeting = "Hello, " + firstName + " " + lastName;
        fetchData().then(data => process(data)).then(result => save(result));
        const fs = require('fs');
    `;

    const visitor = new TypeScriptRefactoringVisitor();
    visitor.visitSourceFile(sampleCode);

    // Part 4: List available recipes
    console.log("\n" + "=".repeat(70));
    console.log("PART 4: OPENREWRITE RECIPE ENGINE");
    console.log("=".repeat(70));

    const engine = new OpenRewriteRecipeEngine();
    engine.listAvailableRecipes();
    engine.executeRecipe("org.openrewrite.javascript.ConvertVarToLet", sampleCode);

    // Part 5: Summary
    console.log("\n" + "=".repeat(70));
    console.log("SUMMARY: HOW TO USE OPENREWRITE FOR TYPESCRIPT");
    console.log("=".repeat(70));

    console.log("\n[Line 367] Step 1: Install Moderne CLI");
    console.log("[Line 368]   npm install -g @moderne/cli");

    console.log("\n[Line 370] Step 2: Create rewrite.yml configuration");
    console.log("[Line 371]   Define recipes and transformation rules");

    console.log("\n[Line 373] Step 3: Run OpenRewrite");
    console.log("[Line 374]   mod run . --recipe=org.openrewrite.javascript.ConvertVarToLet");

    console.log("\n[Line 376] Step 4: Review changes");
    console.log("[Line 377]   OpenRewrite generates patches preserving formatting");

    console.log("\n[Line 379] Step 5: Apply transformations");
    console.log("[Line 380]   mod run . --recipe=YourRecipe --apply");

    console.log("\n[Line 382] ✅ Key Benefits:");
    console.log("[Line 383]   • Automated large-scale refactoring");
    console.log("[Line 384]   • Preserves code formatting and comments");
    console.log("[Line 385]   • Type-aware transformations");
    console.log("[Line 386]   • Composable recipes");
    console.log("[Line 387]   • IDE integration support");

    console.log("\n╔════════════════════════════════════════════════════════════════╗");
    console.log("║              End of OpenRewrite Demonstration                  ║");
    console.log("╚════════════════════════════════════════════════════════════════╝\n");
}

main();
