# Interpreter Design Pattern - TypeScript Implementation

## Pattern Description

The **Interpreter** design pattern is a behavioral pattern that defines a grammatical representation for a language and provides an interpreter to evaluate sentences in that language. It uses a class hierarchy to represent grammar rules, where each rule is represented by a class.

### Key Concepts

- **Abstract Syntax Tree (AST)**: Expressions are represented as a tree structure where each node is an expression
- **Terminal Expressions**: Leaf nodes that cannot be broken down further (e.g., numbers, variables)
- **Non-Terminal Expressions**: Composite nodes that contain other expressions (e.g., arithmetic operations)
- **Context**: Shared state that provides variable bindings for interpretation

### When to Use

- When you have a simple grammar that can be represented as a tree
- When efficiency is not a critical concern (pattern can be slow for complex grammars)
- When you need to interpret statements in a domain-specific language (DSL)

## Requirements

- **Node.js**: 18.0 or higher
- **TypeScript**: 5.3 or higher
- **tsx**: 4.7 or higher (for direct TypeScript execution)

## How to Run

```bash
# Install dependencies
npm install

# Run the demonstration
npm run start
```

## Source Code

```typescript
     1  /**
     2   * Interpreter Design Pattern Implementation
     3   *
     4   * This example demonstrates the Interpreter pattern by implementing
     5   * a simple mathematical expression language that supports:
     6   * - Numbers (terminal expression)
     7   * - Variables (terminal expression)
     8   * - Arithmetic operations: +, -, *, / (non-terminal expressions)
     9   * - Comparison operations: >, <, ==, != (non-terminal expressions)
    10   * - Logical operations: AND, OR (non-terminal expressions)
    11   */
    12
    13  // [Line 13] Context class stores variable bindings for expression evaluation
    14  class Context {
    15      private variables: Map<string, number> = new Map();
    16
    17      setVariable(name: string, value: number): void {
    18          this.variables.set(name, value);
    19      }
    20
    21      getVariable(name: string): number {
    22          const value = this.variables.get(name);
    23          if (value === undefined) {
    24              throw new Error(`Undefined variable: ${name}`);
    25          }
    26          return value;
    27      }
    28
    29      hasVariable(name: string): boolean {
    30          return this.variables.has(name);
    31      }
    32
    33      getAllVariables(): Map<string, number> {
    34          return new Map(this.variables);
    35      }
    36  }
    37
    38  // [Line 35] Abstract Expression interface - the core of the Interpreter pattern
    39  interface Expression {
    40      interpret(context: Context): number;
    41      toString(): string;
    42  }
    43
    44  // [Line 41] Boolean Expression interface for logical operations
    45  interface BooleanExpression {
    46      interpret(context: Context): boolean;
    47      toString(): string;
    48  }
    49
    50  // =============================================================================
    51  // Terminal Expressions - represent leaf nodes in the abstract syntax tree
    52  // =============================================================================
    53
    54  // [Line 50] NumberExpression - terminal expression for numeric literals
    55  class NumberExpression implements Expression {
    56      constructor(private value: number) {}
    57
    58      interpret(context: Context): number {
    59          return this.value;
    60      }
    61
    62      toString(): string {
    63          return this.value.toString();
    64      }
    65  }
    66
    67  // [Line 62] VariableExpression - terminal expression for variable references
    68  class VariableExpression implements Expression {
    69      constructor(private name: string) {}
    70
    71      interpret(context: Context): number {
    72          return context.getVariable(this.name);
    73      }
    74
    75      toString(): string {
    76          return this.name;
    77      }
    78  }
    79
    80  // =============================================================================
    81  // Non-Terminal Expressions - arithmetic operations
    82  // =============================================================================
    83
    84  // [Line 78] AddExpression - non-terminal expression for addition
    85  class AddExpression implements Expression {
    86      constructor(
    87          private left: Expression,
    88          private right: Expression
    89      ) {}
    90
    91      interpret(context: Context): number {
    92          return this.left.interpret(context) + this.right.interpret(context);
    93      }
    94
    95      toString(): string {
    96          return `(${this.left.toString()} + ${this.right.toString()})`;
    97      }
    98  }
    99
   100  // [Line 93] SubtractExpression - non-terminal expression for subtraction
   101  class SubtractExpression implements Expression {
   102      constructor(
   103          private left: Expression,
   104          private right: Expression
   105      ) {}
   106
   107      interpret(context: Context): number {
   108          return this.left.interpret(context) - this.right.interpret(context);
   109      }
   110
   111      toString(): string {
   112          return `(${this.left.toString()} - ${this.right.toString()})`;
   113      }
   114  }
   115
   116  // [Line 108] MultiplyExpression - non-terminal expression for multiplication
   117  class MultiplyExpression implements Expression {
   118      constructor(
   119          private left: Expression,
   120          private right: Expression
   121      ) {}
   122
   123      interpret(context: Context): number {
   124          return this.left.interpret(context) * this.right.interpret(context);
   125      }
   126
   127      toString(): string {
   128          return `(${this.left.toString()} * ${this.right.toString()})`;
   129      }
   130  }
   131
   132  // [Line 123] DivideExpression - non-terminal expression for division
   133  class DivideExpression implements Expression {
   134      constructor(
   135          private left: Expression,
   136          private right: Expression
   137      ) {}
   138
   139      interpret(context: Context): number {
   140          const divisor = this.right.interpret(context);
   141          if (divisor === 0) {
   142              throw new Error("Division by zero");
   143          }
   144          return this.left.interpret(context) / divisor;
   145      }
   146
   147      toString(): string {
   148          return `(${this.left.toString()} / ${this.right.toString()})`;
   149      }
   150  }
   151
   152  // =============================================================================
   153  // Non-Terminal Expressions - comparison operations (return boolean as 0 or 1)
   154  // =============================================================================
   155
   156  // [Line 146] GreaterThanExpression - comparison expression
   157  class GreaterThanExpression implements BooleanExpression {
   158      constructor(
   159          private left: Expression,
   160          private right: Expression
   161      ) {}
   162
   163      interpret(context: Context): boolean {
   164          return this.left.interpret(context) > this.right.interpret(context);
   165      }
   166
   167      toString(): string {
   168          return `(${this.left.toString()} > ${this.right.toString()})`;
   169      }
   170  }
   171
   172  // [Line 161] LessThanExpression - comparison expression
   173  class LessThanExpression implements BooleanExpression {
   174      constructor(
   175          private left: Expression,
   176          private right: Expression
   177      ) {}
   178
   179      interpret(context: Context): boolean {
   180          return this.left.interpret(context) < this.right.interpret(context);
   181      }
   182
   183      toString(): string {
   184          return `(${this.left.toString()} < ${this.right.toString()})`;
   185      }
   186  }
   187
   188  // [Line 176] EqualsExpression - comparison expression
   189  class EqualsExpression implements BooleanExpression {
   190      constructor(
   191          private left: Expression,
   192          private right: Expression
   193      ) {}
   194
   195      interpret(context: Context): boolean {
   196          return this.left.interpret(context) === this.right.interpret(context);
   197      }
   198
   199      toString(): string {
   200          return `(${this.left.toString()} == ${this.right.toString()})`;
   201      }
   202  }
   203
   204  // =============================================================================
   205  // Non-Terminal Expressions - logical operations
   206  // =============================================================================
   207
   208  // [Line 194] AndExpression - logical AND operation
   209  class AndExpression implements BooleanExpression {
   210      constructor(
   211          private left: BooleanExpression,
   212          private right: BooleanExpression
   213      ) {}
   214
   215      interpret(context: Context): boolean {
   216          return this.left.interpret(context) && this.right.interpret(context);
   217      }
   218
   219      toString(): string {
   220          return `(${this.left.toString()} AND ${this.right.toString()})`;
   221      }
   222  }
   223
   224  // [Line 209] OrExpression - logical OR operation
   225  class OrExpression implements BooleanExpression {
   226      constructor(
   227          private left: BooleanExpression,
   228          private right: BooleanExpression
   229      ) {}
   230
   231      interpret(context: Context): boolean {
   232          return this.left.interpret(context) || this.right.interpret(context);
   233      }
   234
   235      toString(): string {
   236          return `(${this.left.toString()} OR ${this.right.toString()})`;
   237      }
   238  }
   239
   240  // [Line 224] NotExpression - logical NOT operation
   241  class NotExpression implements BooleanExpression {
   242      constructor(private expression: BooleanExpression) {}
   243
   244      interpret(context: Context): boolean {
   245          return !this.expression.interpret(context);
   246      }
   247
   248      toString(): string {
   249          return `NOT(${this.expression.toString()})`;
   250      }
   251  }
```

## Program Output

```
======================================================================
Interpreter Design Pattern - Mathematical Expression Language
======================================================================

[Line 245] Creating context with variables:
  x = 10
  y = 5
  z = 3

----------------------------------------------------------------------
Demo 1: Simple Arithmetic Expressions
----------------------------------------------------------------------

[Line 264] Expression: (x + y)
  Result: 15

[Line 273] Expression: ((x * y) - z)
  Result: 47

[Line 285] Expression: ((x + y) * z)
  Result: 45

[Line 297] Expression: ((x / y) + z)
  Result: 5

----------------------------------------------------------------------
Demo 2: Complex Nested Expressions
----------------------------------------------------------------------

[Line 316] Expression: (((x + y) * z) / (x - y))
  Result: 9

[Line 334] Expression: ((x + 100) * 2)
  Result: 220

----------------------------------------------------------------------
Demo 3: Boolean/Comparison Expressions
----------------------------------------------------------------------

[Line 353] Expression: (x > y)
  Result: true

[Line 362] Expression: (y < z)
  Result: false

[Line 371] Expression: (x == 10)
  Result: true

----------------------------------------------------------------------
Demo 4: Logical Expressions
----------------------------------------------------------------------

[Line 387] Expression: ((x > y) AND (y > z))
  Result: true

[Line 401] Expression: ((x < y) OR (x > z))
  Result: true

[Line 415] Expression: NOT((x < y))
  Result: true

----------------------------------------------------------------------
Demo 5: Dynamic Variable Changes
----------------------------------------------------------------------

[Line 433] Expression: ((x + y) * 2)

[Line 445] With x=10, y=5:
  Result: 30

[Line 450] After changing variables to x=20, y=10:
  Result: 60

[Line 457] After changing variables to x=100, y=50:
  Result: 300

----------------------------------------------------------------------
Demo 6: Error Handling
----------------------------------------------------------------------

[Line 471] Expression: (10 / 0)
  Error: Division by zero

[Line 483] Expression: undefined_var
  Error: Undefined variable: undefined_var

======================================================================
Pattern Summary:
======================================================================

The Interpreter pattern allows you to:
  1. Define a grammar for a simple language
  2. Represent sentences in that language as abstract syntax trees
  3. Interpret (evaluate) those sentences using recursive traversal

Key participants in this implementation:
  - Context: Stores variable bindings (x, y, z)
  - Expression: Abstract interface for all expressions
  - Terminal Expressions: NumberExpression, VariableExpression
  - Non-terminal Expressions: Add, Subtract, Multiply, Divide,
    GreaterThan, LessThan, Equals, And, Or, Not
```

## Code Analysis and Annotations

### Pattern Participants

| Participant | Class/Interface | Description |
|-------------|-----------------|-------------|
| AbstractExpression | `Expression`, `BooleanExpression` | Declares the abstract interpret operation (Lines 39-48) |
| TerminalExpression | `NumberExpression`, `VariableExpression` | Implements interpret for terminal symbols (Lines 55-78) |
| NonTerminalExpression | `AddExpression`, `SubtractExpression`, etc. | Implements interpret for grammar rules (Lines 85-250) |
| Context | `Context` | Contains global information for the interpreter (Lines 14-36) |
| Client | `main()` | Builds and interprets the abstract syntax tree (Lines 239-511) |

### Terminal vs Non-Terminal Expressions

| Type | Classes | Lines | Description |
|------|---------|-------|-------------|
| Terminal | `NumberExpression` | 55-65 | Returns literal numeric value |
| Terminal | `VariableExpression` | 68-78 | Looks up variable in context |
| Non-Terminal | `AddExpression` | 85-98 | Recursively interprets left and right, then adds |
| Non-Terminal | `SubtractExpression` | 101-114 | Recursively interprets left and right, then subtracts |
| Non-Terminal | `MultiplyExpression` | 117-130 | Recursively interprets left and right, then multiplies |
| Non-Terminal | `DivideExpression` | 133-150 | Recursively interprets with division by zero check |
| Non-Terminal | `GreaterThanExpression` | 157-170 | Compares two expressions |
| Non-Terminal | `LessThanExpression` | 173-186 | Compares two expressions |
| Non-Terminal | `EqualsExpression` | 189-202 | Checks equality of two expressions |
| Non-Terminal | `AndExpression` | 209-222 | Logical AND of two boolean expressions |
| Non-Terminal | `OrExpression` | 225-238 | Logical OR of two boolean expressions |
| Non-Terminal | `NotExpression` | 241-250 | Logical negation of a boolean expression |

### Output to Source Code Correlation

| Output Line | Source Reference | Calculation | Result |
|-------------|------------------|-------------|--------|
| `[Line 264] Expression: (x + y)` | Lines 264-268 | 10 + 5 | 15 |
| `[Line 273] Expression: ((x * y) - z)` | Lines 273-280 | (10 * 5) - 3 | 47 |
| `[Line 285] Expression: ((x + y) * z)` | Lines 285-292 | (10 + 5) * 3 | 45 |
| `[Line 297] Expression: ((x / y) + z)` | Lines 297-304 | (10 / 5) + 3 | 5 |
| `[Line 316] Expression: (((x + y) * z) / (x - y))` | Lines 316-329 | ((10 + 5) * 3) / (10 - 5) | 9 |
| `[Line 334] Expression: ((x + 100) * 2)` | Lines 334-341 | (10 + 100) * 2 | 220 |
| `[Line 353] Expression: (x > y)` | Lines 353-358 | 10 > 5 | true |
| `[Line 362] Expression: (y < z)` | Lines 362-367 | 5 < 3 | false |
| `[Line 371] Expression: (x == 10)` | Lines 371-376 | 10 == 10 | true |
| `[Line 387] Expression: ((x > y) AND (y > z))` | Lines 387-397 | (10 > 5) AND (5 > 3) | true |
| `[Line 401] Expression: ((x < y) OR (x > z))` | Lines 401-411 | (10 < 5) OR (10 > 3) | true |
| `[Line 415] Expression: NOT((x < y))` | Lines 415-421 | NOT(10 < 5) | true |

### Dynamic Variable Changes Correlation

| Output Reference | Variable Values | Expression | Result |
|------------------|-----------------|------------|--------|
| `[Line 445]` | x=10, y=5 | ((x + y) * 2) = ((10 + 5) * 2) | 30 |
| `[Line 450]` | x=20, y=10 | ((x + y) * 2) = ((20 + 10) * 2) | 60 |
| `[Line 457]` | x=100, y=50 | ((x + y) * 2) = ((100 + 50) * 2) | 300 |

### Error Handling Correlation

| Output Reference | Source Lines | Error Type | Error Message |
|------------------|--------------|------------|---------------|
| `[Line 471]` | 471-478 | Division by zero | `Error: Division by zero` |
| `[Line 483]` | 483-489 | Undefined variable | `Error: Undefined variable: undefined_var` |

## Key Implementation Notes

### Recursive Interpretation

The core of the Interpreter pattern is the recursive `interpret()` method. Non-terminal expressions call `interpret()` on their child expressions:

```typescript
// AddExpression.interpret() - Line 91-92
interpret(context: Context): number {
    return this.left.interpret(context) + this.right.interpret(context);
}
```

### Context for State Management

The Context class (Lines 14-36) stores variable bindings that can be accessed during interpretation:

```typescript
// Setting variables - Line 245-248
context.setVariable("x", 10);
context.setVariable("y", 5);
context.setVariable("z", 3);
```

### Expression Reusability

Once an expression tree is built, it can be evaluated multiple times with different variable values (Demo 5, Lines 433-461). This demonstrates the separation between expression structure and evaluation context.

## Advantages and Disadvantages

### Advantages

1. **Easy to extend**: New expressions can be added by creating new classes
2. **Grammar representation**: Each grammar rule maps to a class
3. **Flexible evaluation**: Same expression can be evaluated with different contexts

### Disadvantages

1. **Complex grammars**: Pattern becomes unwieldy for complex grammars
2. **Performance**: Can be slow due to recursive calls and object creation
3. **No parsing**: This pattern doesn't handle parsing text into AST (requires separate parser)

## Related Patterns

- **Composite**: The AST is essentially a Composite structure
- **Flyweight**: Can be used to share terminal symbols
- **Iterator**: Can be used to traverse the AST
- **Visitor**: Alternative for adding operations to the AST without modifying node classes
