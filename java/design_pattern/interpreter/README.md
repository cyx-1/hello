# Interpreter Pattern

Defines a grammatical representation for a language and provides an interpreter to deal with this grammar.

## How to Run
```bash
cd java/interpreter
mvn compile exec:java
```

## Key Source Code

### Expression Interface (Lines 11-13)
```java
interface Expression {
    int interpret(Map<String, Integer> context);
}
```

### Non-terminal Expression (Lines 42-53)
```java
class AddExpression implements Expression {
    private Expression left;
    private Expression right;

    @Override
    public int interpret(Map<String, Integer> context) {
        return left.interpret(context) + right.interpret(context);
    }
}
```

## Program Output
```
--- 1. Mathematical Expression Interpreter ---
  Expression: (x + y) * 3 where x=10, y=5
  Result: 45
  Expression: x^2 + y^2 where x=10, y=5
  Result: 125

--- 2. Boolean Expression Interpreter ---
  sunny = true, warm = true, weekend = false
  sunny AND warm: true
  (sunny AND warm) OR weekend: true
  NOT weekend: true

--- 3. SQL-like Query Interpreter ---
  Query: department = 'Engineering' AND age > 28
  Alice (Engineering, 30): true
  Bob (Sales, 25): false
  Charlie (Engineering, 35): true
```

## Pattern Benefits
- Easy to change and extend grammar
- Implementing grammar is straightforward
- Good for simple DSLs

## Requirements
- Java 17 or higher
- Maven 3.x
