/**
 * Interpreter Design Pattern Implementation
 *
 * This example demonstrates the Interpreter pattern by implementing
 * a simple mathematical expression language that supports:
 * - Numbers (terminal expression)
 * - Variables (terminal expression)
 * - Arithmetic operations: +, -, *, / (non-terminal expressions)
 * - Comparison operations: >, <, ==, != (non-terminal expressions)
 * - Logical operations: AND, OR (non-terminal expressions)
 */

// [Line 13] Context class stores variable bindings for expression evaluation
class Context {
    private variables: Map<string, number> = new Map();

    setVariable(name: string, value: number): void {
        this.variables.set(name, value);
    }

    getVariable(name: string): number {
        const value = this.variables.get(name);
        if (value === undefined) {
            throw new Error(`Undefined variable: ${name}`);
        }
        return value;
    }

    hasVariable(name: string): boolean {
        return this.variables.has(name);
    }

    getAllVariables(): Map<string, number> {
        return new Map(this.variables);
    }
}

// [Line 35] Abstract Expression interface - the core of the Interpreter pattern
interface Expression {
    interpret(context: Context): number;
    toString(): string;
}

// [Line 41] Boolean Expression interface for logical operations
interface BooleanExpression {
    interpret(context: Context): boolean;
    toString(): string;
}

// =============================================================================
// Terminal Expressions - represent leaf nodes in the abstract syntax tree
// =============================================================================

// [Line 50] NumberExpression - terminal expression for numeric literals
class NumberExpression implements Expression {
    constructor(private value: number) {}

    interpret(context: Context): number {
        return this.value;
    }

    toString(): string {
        return this.value.toString();
    }
}

// [Line 62] VariableExpression - terminal expression for variable references
class VariableExpression implements Expression {
    constructor(private name: string) {}

    interpret(context: Context): number {
        return context.getVariable(this.name);
    }

    toString(): string {
        return this.name;
    }
}

// =============================================================================
// Non-Terminal Expressions - arithmetic operations
// =============================================================================

// [Line 78] AddExpression - non-terminal expression for addition
class AddExpression implements Expression {
    constructor(
        private left: Expression,
        private right: Expression
    ) {}

    interpret(context: Context): number {
        return this.left.interpret(context) + this.right.interpret(context);
    }

    toString(): string {
        return `(${this.left.toString()} + ${this.right.toString()})`;
    }
}

// [Line 93] SubtractExpression - non-terminal expression for subtraction
class SubtractExpression implements Expression {
    constructor(
        private left: Expression,
        private right: Expression
    ) {}

    interpret(context: Context): number {
        return this.left.interpret(context) - this.right.interpret(context);
    }

    toString(): string {
        return `(${this.left.toString()} - ${this.right.toString()})`;
    }
}

// [Line 108] MultiplyExpression - non-terminal expression for multiplication
class MultiplyExpression implements Expression {
    constructor(
        private left: Expression,
        private right: Expression
    ) {}

    interpret(context: Context): number {
        return this.left.interpret(context) * this.right.interpret(context);
    }

    toString(): string {
        return `(${this.left.toString()} * ${this.right.toString()})`;
    }
}

// [Line 123] DivideExpression - non-terminal expression for division
class DivideExpression implements Expression {
    constructor(
        private left: Expression,
        private right: Expression
    ) {}

    interpret(context: Context): number {
        const divisor = this.right.interpret(context);
        if (divisor === 0) {
            throw new Error("Division by zero");
        }
        return this.left.interpret(context) / divisor;
    }

    toString(): string {
        return `(${this.left.toString()} / ${this.right.toString()})`;
    }
}

// =============================================================================
// Non-Terminal Expressions - comparison operations (return boolean as 0 or 1)
// =============================================================================

// [Line 146] GreaterThanExpression - comparison expression
class GreaterThanExpression implements BooleanExpression {
    constructor(
        private left: Expression,
        private right: Expression
    ) {}

    interpret(context: Context): boolean {
        return this.left.interpret(context) > this.right.interpret(context);
    }

    toString(): string {
        return `(${this.left.toString()} > ${this.right.toString()})`;
    }
}

// [Line 161] LessThanExpression - comparison expression
class LessThanExpression implements BooleanExpression {
    constructor(
        private left: Expression,
        private right: Expression
    ) {}

    interpret(context: Context): boolean {
        return this.left.interpret(context) < this.right.interpret(context);
    }

    toString(): string {
        return `(${this.left.toString()} < ${this.right.toString()})`;
    }
}

// [Line 176] EqualsExpression - comparison expression
class EqualsExpression implements BooleanExpression {
    constructor(
        private left: Expression,
        private right: Expression
    ) {}

    interpret(context: Context): boolean {
        return this.left.interpret(context) === this.right.interpret(context);
    }

    toString(): string {
        return `(${this.left.toString()} == ${this.right.toString()})`;
    }
}

// =============================================================================
// Non-Terminal Expressions - logical operations
// =============================================================================

// [Line 194] AndExpression - logical AND operation
class AndExpression implements BooleanExpression {
    constructor(
        private left: BooleanExpression,
        private right: BooleanExpression
    ) {}

    interpret(context: Context): boolean {
        return this.left.interpret(context) && this.right.interpret(context);
    }

    toString(): string {
        return `(${this.left.toString()} AND ${this.right.toString()})`;
    }
}

// [Line 209] OrExpression - logical OR operation
class OrExpression implements BooleanExpression {
    constructor(
        private left: BooleanExpression,
        private right: BooleanExpression
    ) {}

    interpret(context: Context): boolean {
        return this.left.interpret(context) || this.right.interpret(context);
    }

    toString(): string {
        return `(${this.left.toString()} OR ${this.right.toString()})`;
    }
}

// [Line 224] NotExpression - logical NOT operation
class NotExpression implements BooleanExpression {
    constructor(private expression: BooleanExpression) {}

    interpret(context: Context): boolean {
        return !this.expression.interpret(context);
    }

    toString(): string {
        return `NOT(${this.expression.toString()})`;
    }
}

// =============================================================================
// Client code - demonstrates the Interpreter pattern
// =============================================================================

function main(): void {
    console.log("=".repeat(70));
    console.log("Interpreter Design Pattern - Mathematical Expression Language");
    console.log("=".repeat(70));
    console.log();

    // [Line 245] Create context and set up variables
    const context = new Context();
    context.setVariable("x", 10);
    context.setVariable("y", 5);
    context.setVariable("z", 3);

    console.log("[Line 245] Creating context with variables:");
    console.log(`  x = ${context.getVariable("x")}`);
    console.log(`  y = ${context.getVariable("y")}`);
    console.log(`  z = ${context.getVariable("z")}`);
    console.log();

    // ==========================================================================
    // Demo 1: Simple arithmetic expressions
    // ==========================================================================
    console.log("-".repeat(70));
    console.log("Demo 1: Simple Arithmetic Expressions");
    console.log("-".repeat(70));
    console.log();

    // [Line 264] Expression: x + y (10 + 5)
    const expr1 = new AddExpression(
        new VariableExpression("x"),
        new VariableExpression("y")
    );
    console.log(`[Line 264] Expression: ${expr1.toString()}`);
    console.log(`  Result: ${expr1.interpret(context)}`);
    console.log();

    // [Line 273] Expression: x * y - z (10 * 5 - 3)
    const expr2 = new SubtractExpression(
        new MultiplyExpression(
            new VariableExpression("x"),
            new VariableExpression("y")
        ),
        new VariableExpression("z")
    );
    console.log(`[Line 273] Expression: ${expr2.toString()}`);
    console.log(`  Result: ${expr2.interpret(context)}`);
    console.log();

    // [Line 285] Expression: (x + y) * z ((10 + 5) * 3)
    const expr3 = new MultiplyExpression(
        new AddExpression(
            new VariableExpression("x"),
            new VariableExpression("y")
        ),
        new VariableExpression("z")
    );
    console.log(`[Line 285] Expression: ${expr3.toString()}`);
    console.log(`  Result: ${expr3.interpret(context)}`);
    console.log();

    // [Line 297] Expression: x / y + z (10 / 5 + 3)
    const expr4 = new AddExpression(
        new DivideExpression(
            new VariableExpression("x"),
            new VariableExpression("y")
        ),
        new VariableExpression("z")
    );
    console.log(`[Line 297] Expression: ${expr4.toString()}`);
    console.log(`  Result: ${expr4.interpret(context)}`);
    console.log();

    // ==========================================================================
    // Demo 2: Complex nested expressions
    // ==========================================================================
    console.log("-".repeat(70));
    console.log("Demo 2: Complex Nested Expressions");
    console.log("-".repeat(70));
    console.log();

    // [Line 316] Expression: ((x + y) * z) / (x - y) (((10 + 5) * 3) / (10 - 5))
    const expr5 = new DivideExpression(
        new MultiplyExpression(
            new AddExpression(
                new VariableExpression("x"),
                new VariableExpression("y")
            ),
            new VariableExpression("z")
        ),
        new SubtractExpression(
            new VariableExpression("x"),
            new VariableExpression("y")
        )
    );
    console.log(`[Line 316] Expression: ${expr5.toString()}`);
    console.log(`  Result: ${expr5.interpret(context)}`);
    console.log();

    // [Line 334] Expression with literals: (x + 100) * 2
    const expr6 = new MultiplyExpression(
        new AddExpression(
            new VariableExpression("x"),
            new NumberExpression(100)
        ),
        new NumberExpression(2)
    );
    console.log(`[Line 334] Expression: ${expr6.toString()}`);
    console.log(`  Result: ${expr6.interpret(context)}`);
    console.log();

    // ==========================================================================
    // Demo 3: Boolean/Comparison expressions
    // ==========================================================================
    console.log("-".repeat(70));
    console.log("Demo 3: Boolean/Comparison Expressions");
    console.log("-".repeat(70));
    console.log();

    // [Line 353] Comparison: x > y (10 > 5)
    const boolExpr1 = new GreaterThanExpression(
        new VariableExpression("x"),
        new VariableExpression("y")
    );
    console.log(`[Line 353] Expression: ${boolExpr1.toString()}`);
    console.log(`  Result: ${boolExpr1.interpret(context)}`);
    console.log();

    // [Line 362] Comparison: y < z (5 < 3)
    const boolExpr2 = new LessThanExpression(
        new VariableExpression("y"),
        new VariableExpression("z")
    );
    console.log(`[Line 362] Expression: ${boolExpr2.toString()}`);
    console.log(`  Result: ${boolExpr2.interpret(context)}`);
    console.log();

    // [Line 371] Comparison: x == 10
    const boolExpr3 = new EqualsExpression(
        new VariableExpression("x"),
        new NumberExpression(10)
    );
    console.log(`[Line 371] Expression: ${boolExpr3.toString()}`);
    console.log(`  Result: ${boolExpr3.interpret(context)}`);
    console.log();

    // ==========================================================================
    // Demo 4: Logical expressions
    // ==========================================================================
    console.log("-".repeat(70));
    console.log("Demo 4: Logical Expressions");
    console.log("-".repeat(70));
    console.log();

    // [Line 387] Logical AND: (x > y) AND (y > z)
    const logicalExpr1 = new AndExpression(
        new GreaterThanExpression(
            new VariableExpression("x"),
            new VariableExpression("y")
        ),
        new GreaterThanExpression(
            new VariableExpression("y"),
            new VariableExpression("z")
        )
    );
    console.log(`[Line 387] Expression: ${logicalExpr1.toString()}`);
    console.log(`  Result: ${logicalExpr1.interpret(context)}`);
    console.log();

    // [Line 401] Logical OR: (x < y) OR (x > z)
    const logicalExpr2 = new OrExpression(
        new LessThanExpression(
            new VariableExpression("x"),
            new VariableExpression("y")
        ),
        new GreaterThanExpression(
            new VariableExpression("x"),
            new VariableExpression("z")
        )
    );
    console.log(`[Line 401] Expression: ${logicalExpr2.toString()}`);
    console.log(`  Result: ${logicalExpr2.interpret(context)}`);
    console.log();

    // [Line 415] Logical NOT: NOT(x < y)
    const logicalExpr3 = new NotExpression(
        new LessThanExpression(
            new VariableExpression("x"),
            new VariableExpression("y")
        )
    );
    console.log(`[Line 415] Expression: ${logicalExpr3.toString()}`);
    console.log(`  Result: ${logicalExpr3.interpret(context)}`);
    console.log();

    // ==========================================================================
    // Demo 5: Dynamic variable changes
    // ==========================================================================
    console.log("-".repeat(70));
    console.log("Demo 5: Dynamic Variable Changes");
    console.log("-".repeat(70));
    console.log();

    // [Line 433] Reuse expression with different variable values
    const reusableExpr = new MultiplyExpression(
        new AddExpression(
            new VariableExpression("x"),
            new VariableExpression("y")
        ),
        new NumberExpression(2)
    );

    console.log(`[Line 433] Expression: ${reusableExpr.toString()}`);
    console.log();

    // [Line 445] First evaluation with x=10, y=5
    console.log(`[Line 445] With x=${context.getVariable("x")}, y=${context.getVariable("y")}:`);
    console.log(`  Result: ${reusableExpr.interpret(context)}`);
    console.log();

    // [Line 450] Change variables and re-evaluate
    context.setVariable("x", 20);
    context.setVariable("y", 10);
    console.log(`[Line 450] After changing variables to x=${context.getVariable("x")}, y=${context.getVariable("y")}:`);
    console.log(`  Result: ${reusableExpr.interpret(context)}`);
    console.log();

    // [Line 457] Change again
    context.setVariable("x", 100);
    context.setVariable("y", 50);
    console.log(`[Line 457] After changing variables to x=${context.getVariable("x")}, y=${context.getVariable("y")}:`);
    console.log(`  Result: ${reusableExpr.interpret(context)}`);
    console.log();

    // ==========================================================================
    // Demo 6: Error handling
    // ==========================================================================
    console.log("-".repeat(70));
    console.log("Demo 6: Error Handling");
    console.log("-".repeat(70));
    console.log();

    // [Line 471] Division by zero error
    const zeroDivExpr = new DivideExpression(
        new NumberExpression(10),
        new NumberExpression(0)
    );
    console.log(`[Line 471] Expression: ${zeroDivExpr.toString()}`);
    try {
        zeroDivExpr.interpret(context);
    } catch (error) {
        console.log(`  Error: ${(error as Error).message}`);
    }
    console.log();

    // [Line 483] Undefined variable error
    const undefinedVarExpr = new VariableExpression("undefined_var");
    console.log(`[Line 483] Expression: ${undefinedVarExpr.toString()}`);
    try {
        undefinedVarExpr.interpret(context);
    } catch (error) {
        console.log(`  Error: ${(error as Error).message}`);
    }
    console.log();

    console.log("=".repeat(70));
    console.log("Pattern Summary:");
    console.log("=".repeat(70));
    console.log();
    console.log("The Interpreter pattern allows you to:");
    console.log("  1. Define a grammar for a simple language");
    console.log("  2. Represent sentences in that language as abstract syntax trees");
    console.log("  3. Interpret (evaluate) those sentences using recursive traversal");
    console.log();
    console.log("Key participants in this implementation:");
    console.log("  - Context: Stores variable bindings (x, y, z)");
    console.log("  - Expression: Abstract interface for all expressions");
    console.log("  - Terminal Expressions: NumberExpression, VariableExpression");
    console.log("  - Non-terminal Expressions: Add, Subtract, Multiply, Divide,");
    console.log("    GreaterThan, LessThan, Equals, And, Or, Not");
    console.log();
}

// Run the demonstration
main();
