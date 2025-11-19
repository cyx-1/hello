// Interpreter Design Pattern in Rust
// Implements a boolean expression evaluator with AND, OR, NOT operations

use std::collections::HashMap;

// Context holds variable bindings for interpretation
type Context = HashMap<String, bool>;

// Abstract Expression trait - the core of the Interpreter pattern
trait Expression {
    fn interpret(&self, context: &Context) -> bool;
    fn to_string(&self) -> String;
}

// Terminal Expression: Constant (true or false)
struct Constant {
    value: bool,
}

impl Constant {
    fn new(value: bool) -> Box<dyn Expression> {
        println!("[Constant] Creating constant expression: {}", value);
        Box::new(Constant { value })
    }
}

impl Expression for Constant {
    fn interpret(&self, _context: &Context) -> bool {
        println!("  -> Interpreting Constant: {}", self.value);
        self.value
    }

    fn to_string(&self) -> String {
        self.value.to_string()
    }
}

// Terminal Expression: Variable (looks up value in context)
struct Variable {
    name: String,
}

impl Variable {
    fn new(name: &str) -> Box<dyn Expression> {
        println!("[Variable] Creating variable expression: {}", name);
        Box::new(Variable {
            name: name.to_string(),
        })
    }
}

impl Expression for Variable {
    fn interpret(&self, context: &Context) -> bool {
        let value = *context.get(&self.name).unwrap_or(&false);
        println!("  -> Interpreting Variable '{}': {}", self.name, value);
        value
    }

    fn to_string(&self) -> String {
        self.name.clone()
    }
}

// Non-terminal Expression: AND operation
struct AndExpression {
    left: Box<dyn Expression>,
    right: Box<dyn Expression>,
}

impl AndExpression {
    fn new(left: Box<dyn Expression>, right: Box<dyn Expression>) -> Box<dyn Expression> {
        println!("[AndExpression] Creating AND expression");
        Box::new(AndExpression { left, right })
    }
}

impl Expression for AndExpression {
    fn interpret(&self, context: &Context) -> bool {
        println!("  -> Interpreting AND expression:");
        let left_val = self.left.interpret(context);
        let right_val = self.right.interpret(context);
        let result = left_val && right_val;
        println!("  -> AND result: {} && {} = {}", left_val, right_val, result);
        result
    }

    fn to_string(&self) -> String {
        format!("({} AND {})", self.left.to_string(), self.right.to_string())
    }
}

// Non-terminal Expression: OR operation
struct OrExpression {
    left: Box<dyn Expression>,
    right: Box<dyn Expression>,
}

impl OrExpression {
    fn new(left: Box<dyn Expression>, right: Box<dyn Expression>) -> Box<dyn Expression> {
        println!("[OrExpression] Creating OR expression");
        Box::new(OrExpression { left, right })
    }
}

impl Expression for OrExpression {
    fn interpret(&self, context: &Context) -> bool {
        println!("  -> Interpreting OR expression:");
        let left_val = self.left.interpret(context);
        let right_val = self.right.interpret(context);
        let result = left_val || right_val;
        println!("  -> OR result: {} || {} = {}", left_val, right_val, result);
        result
    }

    fn to_string(&self) -> String {
        format!("({} OR {})", self.left.to_string(), self.right.to_string())
    }
}

// Non-terminal Expression: NOT operation
struct NotExpression {
    operand: Box<dyn Expression>,
}

impl NotExpression {
    fn new(operand: Box<dyn Expression>) -> Box<dyn Expression> {
        println!("[NotExpression] Creating NOT expression");
        Box::new(NotExpression { operand })
    }
}

impl Expression for NotExpression {
    fn interpret(&self, context: &Context) -> bool {
        println!("  -> Interpreting NOT expression:");
        let val = self.operand.interpret(context);
        let result = !val;
        println!("  -> NOT result: !{} = {}", val, result);
        result
    }

    fn to_string(&self) -> String {
        format!("(NOT {})", self.operand.to_string())
    }
}

fn main() {
    println!("=== Interpreter Design Pattern Demo ===\n");

    // Create context with variable bindings
    println!("Step 1: Setting up context with variable bindings");
    println!("------------------------------------------------");
    let mut context: Context = HashMap::new();
    context.insert("x".to_string(), true);
    context.insert("y".to_string(), false);
    context.insert("z".to_string(), true);
    println!("Context: x = true, y = false, z = true\n");

    // Example 1: Simple AND expression (x AND y)
    println!("Step 2: Building expression: x AND y");
    println!("------------------------------------");
    let expr1 = AndExpression::new(Variable::new("x"), Variable::new("y"));
    println!("Expression tree: {}\n", expr1.to_string());

    println!("Step 3: Interpreting expression: x AND y");
    println!("----------------------------------------");
    let result1 = expr1.interpret(&context);
    println!("Final result: {}\n", result1);

    // Example 2: OR expression (x OR y)
    println!("Step 4: Building expression: x OR y");
    println!("-----------------------------------");
    let expr2 = OrExpression::new(Variable::new("x"), Variable::new("y"));
    println!("Expression tree: {}\n", expr2.to_string());

    println!("Step 5: Interpreting expression: x OR y");
    println!("---------------------------------------");
    let result2 = expr2.interpret(&context);
    println!("Final result: {}\n", result2);

    // Example 3: NOT expression (NOT y)
    println!("Step 6: Building expression: NOT y");
    println!("----------------------------------");
    let expr3 = NotExpression::new(Variable::new("y"));
    println!("Expression tree: {}\n", expr3.to_string());

    println!("Step 7: Interpreting expression: NOT y");
    println!("--------------------------------------");
    let result3 = expr3.interpret(&context);
    println!("Final result: {}\n", result3);

    // Example 4: Complex nested expression ((x AND z) OR (NOT y))
    println!("Step 8: Building complex expression: (x AND z) OR (NOT y)");
    println!("---------------------------------------------------------");
    let expr4 = OrExpression::new(
        AndExpression::new(Variable::new("x"), Variable::new("z")),
        NotExpression::new(Variable::new("y")),
    );
    println!("Expression tree: {}\n", expr4.to_string());

    println!("Step 9: Interpreting expression: (x AND z) OR (NOT y)");
    println!("-----------------------------------------------------");
    let result4 = expr4.interpret(&context);
    println!("Final result: {}\n", result4);

    // Example 5: Expression with constants ((true AND x) OR false)
    println!("Step 10: Building expression with constants: (true AND x) OR false");
    println!("------------------------------------------------------------------");
    let expr5 = OrExpression::new(
        AndExpression::new(Constant::new(true), Variable::new("x")),
        Constant::new(false),
    );
    println!("Expression tree: {}\n", expr5.to_string());

    println!("Step 11: Interpreting expression: (true AND x) OR false");
    println!("--------------------------------------------------------");
    let result5 = expr5.interpret(&context);
    println!("Final result: {}\n", result5);

    // Summary
    println!("=== Summary of Results ===");
    println!("Expression 1 (x AND y):                  {}", result1);
    println!("Expression 2 (x OR y):                   {}", result2);
    println!("Expression 3 (NOT y):                    {}", result3);
    println!("Expression 4 ((x AND z) OR (NOT y)):     {}", result4);
    println!("Expression 5 ((true AND x) OR false):    {}", result5);
}
