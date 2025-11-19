/**
 * Comprehensive demonstration of the Interpreter Pattern in Java
 *
 * The Interpreter pattern defines a grammatical representation for a language
 * and provides an interpreter to deal with this grammar.
 */

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

// Abstract Expression
interface Expression {
    int interpret(Map<String, Integer> context);
}

// Terminal Expression - represents a number
class NumberExpression implements Expression {
    private int number;

    public NumberExpression(int number) {
        this.number = number;
    }

    @Override
    public int interpret(Map<String, Integer> context) {
        return number;
    }
}

// Terminal Expression - represents a variable
class VariableExpression implements Expression {
    private String name;

    public VariableExpression(String name) {
        this.name = name;
    }

    @Override
    public int interpret(Map<String, Integer> context) {
        if (context.containsKey(name)) {
            return context.get(name);
        }
        return 0;
    }
}

// Non-terminal Expression - addition
class AddExpression implements Expression {
    private Expression left;
    private Expression right;

    public AddExpression(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public int interpret(Map<String, Integer> context) {
        return left.interpret(context) + right.interpret(context);
    }
}

// Non-terminal Expression - subtraction
class SubtractExpression implements Expression {
    private Expression left;
    private Expression right;

    public SubtractExpression(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public int interpret(Map<String, Integer> context) {
        return left.interpret(context) - right.interpret(context);
    }
}

// Non-terminal Expression - multiplication
class MultiplyExpression implements Expression {
    private Expression left;
    private Expression right;

    public MultiplyExpression(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public int interpret(Map<String, Integer> context) {
        return left.interpret(context) * right.interpret(context);
    }
}

// Non-terminal Expression - division
class DivideExpression implements Expression {
    private Expression left;
    private Expression right;

    public DivideExpression(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public int interpret(Map<String, Integer> context) {
        int rightValue = right.interpret(context);
        if (rightValue == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return left.interpret(context) / rightValue;
    }
}

// Parser - converts string expression to Expression tree
class ExpressionParser {
    public Expression parse(String expression) {
        Stack<Expression> stack = new Stack<>();
        String[] tokens = expression.split(" ");

        for (String token : tokens) {
            if (isOperator(token)) {
                Expression right = stack.pop();
                Expression left = stack.pop();
                Expression operator = getOperatorExpression(token, left, right);
                stack.push(operator);
            } else if (isNumber(token)) {
                stack.push(new NumberExpression(Integer.parseInt(token)));
            } else {
                stack.push(new VariableExpression(token));
            }
        }

        return stack.pop();
    }

    private boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") ||
               token.equals("*") || token.equals("/");
    }

    private boolean isNumber(String token) {
        try {
            Integer.parseInt(token);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private Expression getOperatorExpression(String operator, Expression left, Expression right) {
        switch (operator) {
            case "+": return new AddExpression(left, right);
            case "-": return new SubtractExpression(left, right);
            case "*": return new MultiplyExpression(left, right);
            case "/": return new DivideExpression(left, right);
            default: throw new IllegalArgumentException("Unknown operator: " + operator);
        }
    }
}

// Boolean Expression example

interface BooleanExpression {
    boolean interpret(Map<String, Boolean> context);
}

class BooleanVariable implements BooleanExpression {
    private String name;

    public BooleanVariable(String name) {
        this.name = name;
    }

    @Override
    public boolean interpret(Map<String, Boolean> context) {
        return context.getOrDefault(name, false);
    }
}

class AndExpression implements BooleanExpression {
    private BooleanExpression left;
    private BooleanExpression right;

    public AndExpression(BooleanExpression left, BooleanExpression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public boolean interpret(Map<String, Boolean> context) {
        return left.interpret(context) && right.interpret(context);
    }
}

class OrExpression implements BooleanExpression {
    private BooleanExpression left;
    private BooleanExpression right;

    public OrExpression(BooleanExpression left, BooleanExpression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public boolean interpret(Map<String, Boolean> context) {
        return left.interpret(context) || right.interpret(context);
    }
}

class NotExpression implements BooleanExpression {
    private BooleanExpression expression;

    public NotExpression(BooleanExpression expression) {
        this.expression = expression;
    }

    @Override
    public boolean interpret(Map<String, Boolean> context) {
        return !expression.interpret(context);
    }
}

// SQL-like query interpreter

interface QueryExpression {
    boolean evaluate(Map<String, Object> row);
}

class EqualsExpression implements QueryExpression {
    private String column;
    private Object value;

    public EqualsExpression(String column, Object value) {
        this.column = column;
        this.value = value;
    }

    @Override
    public boolean evaluate(Map<String, Object> row) {
        return value.equals(row.get(column));
    }
}

class GreaterThanExpression implements QueryExpression {
    private String column;
    private int value;

    public GreaterThanExpression(String column, int value) {
        this.column = column;
        this.value = value;
    }

    @Override
    public boolean evaluate(Map<String, Object> row) {
        Object colValue = row.get(column);
        if (colValue instanceof Integer) {
            return (Integer) colValue > value;
        }
        return false;
    }
}

class QueryAndExpression implements QueryExpression {
    private QueryExpression left;
    private QueryExpression right;

    public QueryAndExpression(QueryExpression left, QueryExpression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public boolean evaluate(Map<String, Object> row) {
        return left.evaluate(row) && right.evaluate(row);
    }
}

public class MainInterpreter {
    public static void main(String[] args) {
        System.out.println("=== Interpreter Pattern Demonstration ===\n");

        // Mathematical expression interpreter
        System.out.println("--- 1. Mathematical Expression Interpreter ---");
        ExpressionParser parser = new ExpressionParser();
        Map<String, Integer> context = new HashMap<>();
        context.put("x", 10);
        context.put("y", 5);

        // Postfix notation: "x y + 3 *" means (x + y) * 3
        String expr1 = "x y + 3 *";
        Expression expression1 = parser.parse(expr1);
        int result1 = expression1.interpret(context);
        System.out.println("  Expression: (x + y) * 3 where x=10, y=5");
        System.out.println("  Result: " + result1);

        // "10 5 - 2 /" means (10 - 5) / 2
        String expr2 = "10 5 - 2 /";
        Expression expression2 = parser.parse(expr2);
        int result2 = expression2.interpret(context);
        System.out.println("  Expression: (10 - 5) / 2");
        System.out.println("  Result: " + result2);

        // "x x * y y * +" means x^2 + y^2
        String expr3 = "x x * y y * +";
        Expression expression3 = parser.parse(expr3);
        int result3 = expression3.interpret(context);
        System.out.println("  Expression: x^2 + y^2 where x=10, y=5");
        System.out.println("  Result: " + result3);
        System.out.println();

        // Boolean expression interpreter
        System.out.println("--- 2. Boolean Expression Interpreter ---");
        Map<String, Boolean> boolContext = new HashMap<>();
        boolContext.put("sunny", true);
        boolContext.put("warm", true);
        boolContext.put("weekend", false);

        // sunny AND warm
        BooleanExpression sunny = new BooleanVariable("sunny");
        BooleanExpression warm = new BooleanVariable("warm");
        BooleanExpression goodWeather = new AndExpression(sunny, warm);

        System.out.println("  sunny = true, warm = true, weekend = false");
        System.out.println("  sunny AND warm: " + goodWeather.interpret(boolContext));

        // (sunny AND warm) OR weekend
        BooleanExpression weekend = new BooleanVariable("weekend");
        BooleanExpression goOutside = new OrExpression(goodWeather, weekend);
        System.out.println("  (sunny AND warm) OR weekend: " + goOutside.interpret(boolContext));

        // NOT weekend
        BooleanExpression notWeekend = new NotExpression(weekend);
        System.out.println("  NOT weekend: " + notWeekend.interpret(boolContext));
        System.out.println();

        // SQL-like query interpreter
        System.out.println("--- 3. SQL-like Query Interpreter ---");

        // Sample data
        Map<String, Object> row1 = new HashMap<>();
        row1.put("name", "Alice");
        row1.put("age", 30);
        row1.put("department", "Engineering");

        Map<String, Object> row2 = new HashMap<>();
        row2.put("name", "Bob");
        row2.put("age", 25);
        row2.put("department", "Sales");

        Map<String, Object> row3 = new HashMap<>();
        row3.put("name", "Charlie");
        row3.put("age", 35);
        row3.put("department", "Engineering");

        // Query: department = 'Engineering' AND age > 28
        QueryExpression deptFilter = new EqualsExpression("department", "Engineering");
        QueryExpression ageFilter = new GreaterThanExpression("age", 28);
        QueryExpression query = new QueryAndExpression(deptFilter, ageFilter);

        System.out.println("  Query: department = 'Engineering' AND age > 28");
        System.out.println("  Alice (Engineering, 30): " + query.evaluate(row1));
        System.out.println("  Bob (Sales, 25): " + query.evaluate(row2));
        System.out.println("  Charlie (Engineering, 35): " + query.evaluate(row3));

        System.out.println("\n=== Summary ===");
        System.out.println("Interpreter pattern benefits:");
        System.out.println("  - Easy to change and extend grammar");
        System.out.println("  - Implementing grammar is straightforward");
        System.out.println("  - Adding new expressions is easy");
        System.out.println("\nBest used for:");
        System.out.println("  - Simple languages or expressions");
        System.out.println("  - When efficiency is not critical");
        System.out.println("  - Domain-specific languages (DSLs)");
    }
}
