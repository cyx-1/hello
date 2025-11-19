# Interpreter Pattern

The Interpreter pattern defines a grammatical representation for a language and provides an interpreter to deal with this grammar. It's used to interpret sentences in a language by representing each grammar rule as a class.

**Requires Python 3.10+** (uses union types with `|` syntax and modern type hints)

## Key Source Code

### Context for Variables

```python:main_interpreter.py startLine=25 endLine=43
class Context:
    """Context containing variables and state for interpretation."""

    def __init__(self):
        self._variables: dict[str, Any] = {}

    def set_variable(self, name: str, value: Any) -> None:
        self._variables[name] = value

    def get_variable(self, name: str) -> Any:
        if name not in self._variables:
            raise ValueError(f"Undefined variable: {name}")
        return self._variables[name]

    def has_variable(self, name: str) -> bool:
        return name in self._variables

    def get_all_variables(self) -> dict[str, Any]:
        return self._variables.copy()
```

### Abstract Expression Interface

```python:main_interpreter.py startLine=46 endLine=56
class Expression(ABC):
    """Abstract expression in the grammar."""

    @abstractmethod
    def interpret(self, context: Context) -> Any:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
```

### Terminal Expressions

```python:main_interpreter.py startLine=60 endLine=83
class NumberExpression(Expression):
    """Terminal expression for numbers."""

    def __init__(self, value: float):
        self._value = value

    def interpret(self, context: Context) -> float:
        return self._value

    def __str__(self) -> str:
        return str(self._value)


class VariableExpression(Expression):
    """Terminal expression for variables."""

    def __init__(self, name: str):
        self._name = name

    def interpret(self, context: Context) -> Any:
        return context.get_variable(self._name)

    def __str__(self) -> str:
        return self._name
```

### Nonterminal Expression (Arithmetic)

```python:main_interpreter.py startLine=100 endLine=111
class AddExpression(Expression):
    """Addition of two expressions."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> float:
        return self._left.interpret(context) + self._right.interpret(context)

    def __str__(self) -> str:
        return f"({self._left} + {self._right})"
```

### Conditional Expression

```python:main_interpreter.py startLine=245 endLine=262
class IfExpression(Expression):
    """Conditional expression: if condition then expr1 else expr2."""

    def __init__(
        self, condition: Expression, then_expr: Expression, else_expr: Expression
    ):
        self._condition = condition
        self._then_expr = then_expr
        self._else_expr = else_expr

    def interpret(self, context: Context) -> Any:
        if self._condition.interpret(context):
            return self._then_expr.interpret(context)
        else:
            return self._else_expr.interpret(context)

    def __str__(self) -> str:
        return f"(IF {self._condition} THEN {self._then_expr} ELSE {self._else_expr})"
```

### Expression Parser

```python:main_interpreter.py startLine=310 endLine=323
    def _parse_expression(self) -> Expression:
        """Parse addition/subtraction."""
        left = self._parse_term()

        while self._pos < len(self._tokens) and self._tokens[self._pos] in "+-":
            op = self._tokens[self._pos]
            self._pos += 1
            right = self._parse_term()
            if op == "+":
                left = AddExpression(left, right)
            else:
                left = SubtractExpression(left, right)

        return left
```

## Program Output

```
============================================================
Interpreter Pattern - Expression Evaluator Demo
============================================================

--- Manual Expression Building ---
Expression: ((x + y) * 2)
Variables: {'x': 10, 'y': 5}
Result: 30

Expression: ((x > y) AND (y > 0))
Result: True

--- Parsed Expressions ---
2 + 3                = 5.0
10 - 4 * 2           = 2.0
(10 - 4) * 2         = 12.0
x + y * 2            = 20.0
100 / (x + y)        = 6.666666666666667

--- Conditional Expressions ---
Expression: (IF (x > 5) THEN (x * 2) ELSE (x + 10))
With x=10: 20
With x=3: 13

--- Complex Boolean Expression ---
Loan eligibility: (((age > 17) AND (income > 30000)) OR (credit_score > 700))
Variables: age=25, income=50000, credit_score=720
Eligible: True

--- Dynamic Variable Updates ---
Expression: a * b + 10
  a=5, b=3: result=25.0
  a=10, b=3: result=40.0
  a=15, b=3: result=55.0

--- Error Handling ---
Division error: Division by zero
Variable error: Unknown character: _

============================================================
Benefits of Interpreter Pattern:
============================================================
1. Easy to change and extend grammar
2. Implementing grammar is straightforward
3. Adding new expressions is easy
4. Grammar represented by class hierarchy

============================================================
Use Cases:
============================================================
1. SQL parsing
2. Regular expressions
3. Configuration languages
4. Mathematical expressions
5. Domain-specific languages
```

## Output Analysis

### Manual Expression Building (Lines 376-390)
- Expression tree built at lines 376-379: `MultiplyExpression(AddExpression(...), NumberExpression(2))`
- `interpret()` calls propagate through tree recursively
- `(x + y) * 2` evaluates as: VariableExpression("x").interpret() returns 10, VariableExpression("y").interpret() returns 5, AddExpression returns 15, MultiplyExpression returns 30

### Boolean Expression (Lines 385-390)
- `AndExpression` at line 210-211 short-circuits if first operand is false
- Nested `GreaterThanExpression` at lines 167-168 compare variable values
- Result is boolean True (10 > 5 is true AND 5 > 0 is true)

### Parsed Expressions (Lines 396-407)
- Parser respects operator precedence: `10 - 4 * 2` = 2.0 (multiply first)
- Parentheses override precedence: `(10 - 4) * 2` = 12.0
- Variables resolved from context: `x + y * 2` uses x=10, y=5

### Parser Implementation (Lines 310-323)
- `_parse_expression()` handles lowest precedence (+, -)
- `_parse_term()` at lines 325-338 handles higher precedence (*, /)
- Recursive descent parsing builds AST bottom-up

### Conditional Expressions (Lines 413-423)
- `IfExpression` at lines 255-259 evaluates condition first
- With x=10: condition `x > 5` is true, evaluates `x * 2` = 20
- With x=3: condition false, evaluates `x + 10` = 13

### Complex Boolean Expression (Lines 432-440)
- Loan eligibility combines multiple conditions with OR
- `OrExpression` at line 224-225 returns true if either operand is true
- Demonstrates real-world rule engine use case

### Dynamic Variable Updates (Lines 448-456)
- Same expression tree re-evaluated with different variable values
- Context lookup at line 80 (`context.get_variable()`) resolves current value
- Shows expression reusability without rebuilding AST

### Error Handling (Lines 461-471)
- `DivideExpression` at line 151-152 checks for division by zero
- `Context.get_variable()` at line 35-36 raises for undefined variables
- Note: Parser error for underscore in variable name (tokenizer limitation)

## Usage

```bash
uv run python main_interpreter.py
```
