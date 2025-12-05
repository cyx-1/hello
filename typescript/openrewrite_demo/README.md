# OpenRewrite TypeScript Demonstration

This example demonstrates **OpenRewrite** for TypeScript - an automated refactoring tool that performs large-scale code transformations while preserving formatting and comments.

## What is OpenRewrite?

OpenRewrite is an automated refactoring ecosystem that uses the **Lossless Semantic Tree (LST)** to transform source code. For TypeScript/JavaScript, it provides:
- Automated code modernization
- Type-aware refactoring
- Preservation of code formatting and comments
- Composable transformation recipes
- Large-scale codebase migrations

## Requirements

**Requires:**
- Node.js >= 18.0.0
- TypeScript 5.3+
- Moderne CLI (for actual OpenRewrite transformations)

**Note:** OpenRewrite's TypeScript support is available through the [Moderne CLI](https://github.com/openrewrite/rewrite-javascript), not standard npm tooling.

## Running the Demo

```bash
npm install
npm start
```

## Important Source Code Sections

### 1. Code Before Transformation (Lines 16-89)

The `BeforeRefactoring` namespace (lines 16-89) demonstrates outdated TypeScript patterns:

#### Variable Declarations with `var` (Line 20-27)
```typescript
20: var counter = 0; // Should be 'let' or 'const'
21: var message = "Hello World"; // Should be 'const'
23: for (var i = 0; i < 3; i++) { // 'var' in loop
```
**Output:** Lines demonstrating the use of deprecated `var` keyword

#### Callback-style Promises (Lines 32-45)
```typescript
35: fetchUserData(1)
36:     .then(user => {
37:         console.log(`[Line 36] User fetched: ${user.name}`);
38:         return fetchUserOrders(user.id);
39:     })
40:     .then(orders => {
41:         console.log(`[Line 40] Orders count: ${orders.length}`);
42:     })
```
**Output:** Shows nested promise chains that should be async/await

#### String Concatenation (Lines 73-80)
```typescript
79: const greeting = "Hello, " + firstName + " " + lastName + "! You are " + age + " years old.";
```
**Output (Line 80):** `Hello, John Doe! You are 30 years old.`

### 2. Code After Transformation (Lines 95-166)

The `AfterRefactoring` namespace shows modernized code:

#### Modern Declarations (Lines 100-108)
```typescript
101: let counter = 0; // Changed from 'var' to 'let'
102: const message = "Hello World"; // Changed from 'var' to 'const'
104: for (let i = 0; i < 3; i++) { // Changed from 'var' to 'let'
```
**Output (Line 108):** `counter: 3, message: Hello World`

#### Async/Await Style (Lines 113-124)
```typescript
113: async function demonstrateAsyncAwait() {
116:     const user = await fetchUserData(1);
117:     console.log(`[Line 117] User fetched: ${user.name}`);
119:     const orders = await fetchUserOrders(user.id);
120:     console.log(`[Line 120] Orders count: ${orders.length}`);
```
**Output (Line 117):** `User fetched: Alice Johnson`
**Output (Line 120):** `Orders count: 3`

#### Template Literals (Lines 150-157)
```typescript
156: const greeting = `Hello, ${firstName} ${lastName}! You are ${age} years old.`;
```
**Output (Line 157):** `Hello, John Doe! You are 30 years old.`

### 3. Visitor Pattern Implementation (Lines 172-222)

The `TypeScriptRefactoringVisitor` class demonstrates how OpenRewrite analyzes code:

```typescript
177: visitSourceFile(sourceCode: string): void {
178:     console.log("[Line 178] Analyzing source code using Lossless Semantic Tree (LST)...");
180:     this.detectVarDeclarations(sourceCode);
181:     this.detectStringConcatenation(sourceCode);
182:     this.detectCallbackPromises(sourceCode);
183:     this.detectCommonJS(sourceCode);
```

**Output:**
```
[Line 177] === OpenRewrite Visitor Pattern ===
[Line 178] Analyzing source code using Lossless Semantic Tree (LST)...
[Line 186] Total transformations detected: 4
[Line 188] 1. Found 2 'var' declarations → Convert to 'let' or 'const'
[Line 188] 2. Found string concatenations → Convert to template literals
[Line 188] 3. Found promise chains → Convert to async/await
[Line 188] 4. Found 1 CommonJS requires → Convert to ES6 imports
```

### 4. Available Recipes (Lines 243-259)

OpenRewrite provides pre-built recipes for common transformations:

```typescript
246: const recipes = [
247:     "org.openrewrite.javascript.ConvertVarToLet",
248:     "org.openrewrite.javascript.UseTemplateLiterals",
249:     "org.openrewrite.javascript.ConvertToArrowFunctions",
250:     "org.openrewrite.javascript.CommonJSToESModule",
251:     "org.openrewrite.javascript.PromisesToAsyncAwait",
252:     "org.openrewrite.javascript.cleanup.AddOptionalChaining",
253:     "org.openrewrite.javascript.cleanup.RemoveUnusedImports",
254:     "org.openrewrite.codemods.ESLintTypeScriptDefaults"
255: ];
```

**Output:** Lists all 8 available transformation recipes (Lines 257)

## Program Output

### Part 1: Code Patterns Before OpenRewrite
```
[Line 19] === Before: Using 'var' declarations ===
[Line 27] counter: 3, message: Hello World
[Line 32] === Before: Callback-style Promise ===
[Line 57] === Before: Verbose array operations ===
[Line 68] Filtered and mapped: 4,8
[Line 73] === Before: String concatenation ===
[Line 80] Hello, John Doe! You are 30 years old.
```

### Part 2: Code Patterns After OpenRewrite
```
[Line 100] === After: Using 'let' and 'const' ===
[Line 108] counter: 3, message: Hello World
[Line 113] === After: Async/await style ===
[Line 117] User fetched: Alice Johnson
[Line 120] Orders count: 3
[Line 136] === After: Concise arrow functions ===
[Line 145] Filtered and mapped: 4,8
[Line 150] === After: Template literals ===
[Line 157] Hello, John Doe! You are 30 years old.
```

### Part 3: Visitor Pattern Analysis
The visitor detects 4 different transformation opportunities:
1. **2 'var' declarations** → Convert to 'let' or 'const'
2. **String concatenations** → Convert to template literals
3. **Promise chains** → Convert to async/await
4. **1 CommonJS require** → Convert to ES6 imports

### Part 4: Recipe Execution Summary

```
[Line 233] === Executing Recipe: org.openrewrite.javascript.ConvertVarToLet ===
[Line 238] Recipe 'org.openrewrite.javascript.ConvertVarToLet' completed successfully
[Line 239] Generated patch file with transformations
```

## How to Use OpenRewrite with TypeScript

### Step 1: Install Moderne CLI (Line 368)
```bash
npm install -g @moderne/cli
```

### Step 2: Create `rewrite.yml` Configuration (Line 371)
See the included `rewrite.yml` file for recipe definitions.

### Step 3: Run OpenRewrite (Line 374)
```bash
mod run . --recipe=org.openrewrite.javascript.ConvertVarToLet
```

### Step 4: Review Changes (Line 377)
OpenRewrite generates patches while preserving your code's formatting.

### Step 5: Apply Transformations (Line 380)
```bash
mod run . --recipe=YourRecipe --apply
```

## Key Benefits (Lines 382-387)

✅ **Automated large-scale refactoring** - Transform entire codebases automatically
✅ **Preserves code formatting and comments** - Lossless Semantic Tree maintains style
✅ **Type-aware transformations** - Understands TypeScript types
✅ **Composable recipes** - Combine multiple transformations
✅ **IDE integration support** - Works with popular development environments

## Example Files

### `example_before.ts`
Demonstrates anti-patterns and outdated syntax:
- Using `var` instead of `let`/`const`
- String concatenation instead of template literals
- Traditional function expressions vs arrow functions
- Promise chains vs async/await
- Verbose null checks vs optional chaining

### `example_after.ts`
Shows the same code after OpenRewrite modernization:
- Modern variable declarations
- Template literals
- Arrow functions
- Async/await
- Optional chaining

### `rewrite.yml`
Contains recipe configurations for:
- `TypeScriptModernization` - Comprehensive modernization suite
- `RemoveConsoleLogs` - Production cleanup
- `AddOptionalChaining` - Null safety improvements
- `TypeScriptCleanup` - Code quality improvements

## Architecture

OpenRewrite works through a **visitor pattern**:

1. **Parse** - Code is parsed into a Lossless Semantic Tree (LST)
2. **Visit** - Visitors traverse the tree looking for patterns
3. **Transform** - Matching patterns trigger transformations
4. **Output** - Modified tree is serialized back to code

This approach ensures:
- No information loss (comments, formatting preserved)
- Type-safe transformations
- Composable recipes
- Deterministic results

## Related Resources

- [OpenRewrite JavaScript/TypeScript](https://github.com/openrewrite/rewrite-javascript)
- [OpenRewrite Documentation](https://docs.openrewrite.org/)
- [Moderne CLI](https://github.com/openrewrite/rewrite)
- [OpenRewrite Codemods](https://github.com/openrewrite/rewrite-codemods)

## Note on TypeScript Support

**Important:** TypeScript/JavaScript support in OpenRewrite currently requires the **Moderne CLI** rather than standard npm build tools. The Moderne CLI is free for open-source repositories. For production use with closed-source repositories, a license may be required.

---

**Language Version:** TypeScript 5.3+
**OpenRewrite Support:** Via Moderne CLI and rewrite-javascript module
**Demo Type:** Simulation of OpenRewrite transformation patterns
