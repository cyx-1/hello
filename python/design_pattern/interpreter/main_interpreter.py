# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Interpreter Pattern

The Interpreter pattern defines a grammatical representation for a language
and provides an interpreter to deal with this grammar. It's used to interpret
sentences in a language.

Key Components:
- AbstractExpression: Declares interpret operation
- TerminalExpression: Implements interpret for terminal symbols
- NonterminalExpression: Implements interpret for grammar rules
- Context: Contains information global to the interpreter
- Client: Builds abstract syntax tree and invokes interpret
"""

from abc import ABC, abstractmethod
from typing import Any


# Context for interpretation
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


# Abstract Expression
class Expression(ABC):
    """Abstract expression in the grammar."""

    @abstractmethod
    def interpret(self, context: Context) -> Any:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


# Terminal Expressions
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


class BooleanExpression(Expression):
    """Terminal expression for booleans."""

    def __init__(self, value: bool):
        self._value = value

    def interpret(self, context: Context) -> bool:
        return self._value

    def __str__(self) -> str:
        return str(self._value).lower()


# Nonterminal Expressions - Arithmetic
class AddExpression(Expression):
    """Addition of two expressions."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> float:
        return self._left.interpret(context) + self._right.interpret(context)

    def __str__(self) -> str:
        return f"({self._left} + {self._right})"


class SubtractExpression(Expression):
    """Subtraction of two expressions."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> float:
        return self._left.interpret(context) - self._right.interpret(context)

    def __str__(self) -> str:
        return f"({self._left} - {self._right})"


class MultiplyExpression(Expression):
    """Multiplication of two expressions."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> float:
        return self._left.interpret(context) * self._right.interpret(context)

    def __str__(self) -> str:
        return f"({self._left} * {self._right})"


class DivideExpression(Expression):
    """Division of two expressions."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> float:
        divisor = self._right.interpret(context)
        if divisor == 0:
            raise ValueError("Division by zero")
        return self._left.interpret(context) / divisor

    def __str__(self) -> str:
        return f"({self._left} / {self._right})"


# Nonterminal Expressions - Comparison
class GreaterThanExpression(Expression):
    """Greater than comparison."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> bool:
        return self._left.interpret(context) > self._right.interpret(context)

    def __str__(self) -> str:
        return f"({self._left} > {self._right})"


class LessThanExpression(Expression):
    """Less than comparison."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> bool:
        return self._left.interpret(context) < self._right.interpret(context)

    def __str__(self) -> str:
        return f"({self._left} < {self._right})"


class EqualsExpression(Expression):
    """Equality comparison."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> bool:
        return self._left.interpret(context) == self._right.interpret(context)

    def __str__(self) -> str:
        return f"({self._left} == {self._right})"


# Nonterminal Expressions - Logical
class AndExpression(Expression):
    """Logical AND."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> bool:
        return bool(self._left.interpret(context) and self._right.interpret(context))

    def __str__(self) -> str:
        return f"({self._left} AND {self._right})"


class OrExpression(Expression):
    """Logical OR."""

    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> bool:
        return bool(self._left.interpret(context) or self._right.interpret(context))

    def __str__(self) -> str:
        return f"({self._left} OR {self._right})"


class NotExpression(Expression):
    """Logical NOT."""

    def __init__(self, expression: Expression):
        self._expression = expression

    def interpret(self, context: Context) -> bool:
        return not self._expression.interpret(context)

    def __str__(self) -> str:
        return f"(NOT {self._expression})"


# Conditional Expression
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


# Simple parser for demonstration
class SimpleExpressionParser:
    """Simple parser to build expression tree from infix notation."""

    def __init__(self):
        self._pos = 0
        self._tokens: list[str] = []

    def parse(self, expression: str) -> Expression:
        """Parse a simple mathematical expression."""
        # Tokenize
        self._tokens = self._tokenize(expression)
        self._pos = 0

        if not self._tokens:
            raise ValueError("Empty expression")

        return self._parse_expression()

    def _tokenize(self, expr: str) -> list[str]:
        """Simple tokenizer."""
        tokens = []
        i = 0
        while i < len(expr):
            if expr[i].isspace():
                i += 1
            elif expr[i] in "+-*/()":
                tokens.append(expr[i])
                i += 1
            elif expr[i].isdigit() or expr[i] == ".":
                j = i
                while j < len(expr) and (expr[j].isdigit() or expr[j] == "."):
                    j += 1
                tokens.append(expr[i:j])
                i = j
            elif expr[i].isalpha():
                j = i
                while j < len(expr) and expr[j].isalnum():
                    j += 1
                tokens.append(expr[i:j])
                i = j
            else:
                raise ValueError(f"Unknown character: {expr[i]}")
        return tokens

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

    def _parse_term(self) -> Expression:
        """Parse multiplication/division."""
        left = self._parse_factor()

        while self._pos < len(self._tokens) and self._tokens[self._pos] in "*/":
            op = self._tokens[self._pos]
            self._pos += 1
            right = self._parse_factor()
            if op == "*":
                left = MultiplyExpression(left, right)
            else:
                left = DivideExpression(left, right)

        return left

    def _parse_factor(self) -> Expression:
        """Parse number, variable, or parenthesized expression."""
        if self._pos >= len(self._tokens):
            raise ValueError("Unexpected end of expression")

        token = self._tokens[self._pos]

        if token == "(":
            self._pos += 1
            expr = self._parse_expression()
            if self._pos >= len(self._tokens) or self._tokens[self._pos] != ")":
                raise ValueError("Missing closing parenthesis")
            self._pos += 1
            return expr
        elif token[0].isdigit() or (token[0] == "." and len(token) > 1):
            self._pos += 1
            return NumberExpression(float(token))
        elif token[0].isalpha():
            self._pos += 1
            return VariableExpression(token)
        else:
            raise ValueError(f"Unexpected token: {token}")


def main() -> None:
    print("=" * 60)
    print("Interpreter Pattern - Expression Evaluator Demo")
    print("=" * 60)

    # Demo 1: Building expressions manually
    print("\n--- Manual Expression Building ---")
    context = Context()
    context.set_variable("x", 10)
    context.set_variable("y", 5)

    # Expression: (x + y) * 2
    expr = MultiplyExpression(
        AddExpression(VariableExpression("x"), VariableExpression("y")),
        NumberExpression(2),
    )
    print(f"Expression: {expr}")
    print(f"Variables: {context.get_all_variables()}")
    print(f"Result: {expr.interpret(context)}")

    # Expression: x > y AND y > 0
    expr2 = AndExpression(
        GreaterThanExpression(VariableExpression("x"), VariableExpression("y")),
        GreaterThanExpression(VariableExpression("y"), NumberExpression(0)),
    )
    print(f"\nExpression: {expr2}")
    print(f"Result: {expr2.interpret(context)}")

    # Demo 2: Using parser
    print("\n--- Parsed Expressions ---")
    parser = SimpleExpressionParser()

    expressions = [
        "2 + 3",
        "10 - 4 * 2",
        "(10 - 4) * 2",
        "x + y * 2",
        "100 / (x + y)",
    ]

    for expr_str in expressions:
        expr = parser.parse(expr_str)
        result = expr.interpret(context)
        print(f"{expr_str:20} = {result}")

    # Demo 3: Conditional expressions
    print("\n--- Conditional Expressions ---")

    # if x > 5 then x * 2 else x + 10
    conditional = IfExpression(
        GreaterThanExpression(VariableExpression("x"), NumberExpression(5)),
        MultiplyExpression(VariableExpression("x"), NumberExpression(2)),
        AddExpression(VariableExpression("x"), NumberExpression(10)),
    )

    print(f"Expression: {conditional}")
    print(f"With x=10: {conditional.interpret(context)}")

    context.set_variable("x", 3)
    print(f"With x=3: {conditional.interpret(context)}")

    # Demo 4: Complex boolean expression
    print("\n--- Complex Boolean Expression ---")
    context.set_variable("age", 25)
    context.set_variable("income", 50000)
    context.set_variable("credit_score", 720)

    # (age >= 18 AND income > 30000) OR credit_score > 700
    loan_eligible = OrExpression(
        AndExpression(
            GreaterThanExpression(VariableExpression("age"), NumberExpression(17)),
            GreaterThanExpression(VariableExpression("income"), NumberExpression(30000)),
        ),
        GreaterThanExpression(
            VariableExpression("credit_score"), NumberExpression(700)
        ),
    )

    print(f"Loan eligibility: {loan_eligible}")
    print("Variables: age=25, income=50000, credit_score=720")
    print(f"Eligible: {loan_eligible.interpret(context)}")

    # Demo 5: Variable updates
    print("\n--- Dynamic Variable Updates ---")
    context.set_variable("a", 5)
    context.set_variable("b", 3)

    expr = parser.parse("a * b + 10")
    print("Expression: a * b + 10")

    for a_val in [5, 10, 15]:
        context.set_variable("a", a_val)
        print(f"  a={a_val}, b=3: result={expr.interpret(context)}")

    # Demo 6: Error handling
    print("\n--- Error Handling ---")

    try:
        expr = parser.parse("10 / 0")
        expr.interpret(context)
    except ValueError as e:
        print(f"Division error: {e}")

    try:
        expr = parser.parse("undefined_var + 1")
        expr.interpret(context)
    except ValueError as e:
        print(f"Variable error: {e}")

    print("\n" + "=" * 60)
    print("Benefits of Interpreter Pattern:")
    print("=" * 60)
    print("1. Easy to change and extend grammar")
    print("2. Implementing grammar is straightforward")
    print("3. Adding new expressions is easy")
    print("4. Grammar represented by class hierarchy")

    print("\n" + "=" * 60)
    print("Use Cases:")
    print("=" * 60)
    print("1. SQL parsing")
    print("2. Regular expressions")
    print("3. Configuration languages")
    print("4. Mathematical expressions")
    print("5. Domain-specific languages")


if __name__ == "__main__":
    main()
