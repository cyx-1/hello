# Interpreter Design Pattern in Rust

## Description

The **Interpreter Design Pattern** is a behavioral design pattern that defines a grammatical representation for a language and provides an interpreter to evaluate sentences in that language. It's particularly useful for implementing domain-specific languages (DSLs), expression evaluators, and rule engines.

This implementation demonstrates a **boolean expression evaluator** that supports:
- **Terminal Expressions**: Constants (`true`/`false`) and Variables (looked up in context)
- **Non-terminal Expressions**: AND, OR, and NOT operations
- **Composite Structure**: Expressions can be nested to form complex boolean logic

### Key Components
- **Expression Trait**: Abstract interface that all expressions implement
- **Context**: Stores variable bindings for interpretation
- **Terminal Expressions**: Leaf nodes that return values directly
- **Non-terminal Expressions**: Composite nodes that combine other expressions

---

## Source Code

```rust
  1  // Interpreter Design Pattern in Rust
  2  // Implements a boolean expression evaluator with AND, OR, NOT operations
  3
  4  use std::collections::HashMap;
  5
  6  // Context holds variable bindings for interpretation
  7  type Context = HashMap<String, bool>;
  8
  9  // Abstract Expression trait - the core of the Interpreter pattern
 10  trait Expression {
 11      fn interpret(&self, context: &Context) -> bool;
 12      fn to_string(&self) -> String;
 13  }
 14
 15  // Terminal Expression: Constant (true or false)
 16  struct Constant {
 17      value: bool,
 18  }
 19
 20  impl Constant {
 21      fn new(value: bool) -> Box<dyn Expression> {
 22          println!("[Constant] Creating constant expression: {}", value);
 23          Box::new(Constant { value })
 24      }
 25  }
 26
 27  impl Expression for Constant {
 28      fn interpret(&self, _context: &Context) -> bool {
 29          println!("  -> Interpreting Constant: {}", self.value);
 30          self.value
 31      }
 32
 33      fn to_string(&self) -> String {
 34          self.value.to_string()
 35      }
 36  }
 37
 38  // Terminal Expression: Variable (looks up value in context)
 39  struct Variable {
 40      name: String,
 41  }
 42
 43  impl Variable {
 44      fn new(name: &str) -> Box<dyn Expression> {
 45          println!("[Variable] Creating variable expression: {}", name);
 46          Box::new(Variable {
 47              name: name.to_string(),
 48          })
 49      }
 50  }
 51
 52  impl Expression for Variable {
 53      fn interpret(&self, context: &Context) -> bool {
 54          let value = *context.get(&self.name).unwrap_or(&false);
 55          println!("  -> Interpreting Variable '{}': {}", self.name, value);
 56          value
 57      }
 58
 59      fn to_string(&self) -> String {
 60          self.name.clone()
 61      }
 62  }
 63
 64  // Non-terminal Expression: AND operation
 65  struct AndExpression {
 66      left: Box<dyn Expression>,
 67      right: Box<dyn Expression>,
 68  }
 69
 70  impl AndExpression {
 71      fn new(left: Box<dyn Expression>, right: Box<dyn Expression>) -> Box<dyn Expression> {
 72          println!("[AndExpression] Creating AND expression");
 73          Box::new(AndExpression { left, right })
 74      }
 75  }
 76
 77  impl Expression for AndExpression {
 78      fn interpret(&self, context: &Context) -> bool {
 79          println!("  -> Interpreting AND expression:");
 80          let left_val = self.left.interpret(context);
 81          let right_val = self.right.interpret(context);
 82          let result = left_val && right_val;
 83          println!("  -> AND result: {} && {} = {}", left_val, right_val, result);
 84          result
 85      }
 86
 87      fn to_string(&self) -> String {
 88          format!("({} AND {})", self.left.to_string(), self.right.to_string())
 89      }
 90  }
 91
 92  // Non-terminal Expression: OR operation
 93  struct OrExpression {
 94      left: Box<dyn Expression>,
 95      right: Box<dyn Expression>,
 96  }
 97
 98  impl OrExpression {
 99      fn new(left: Box<dyn Expression>, right: Box<dyn Expression>) -> Box<dyn Expression> {
100          println!("[OrExpression] Creating OR expression");
101          Box::new(OrExpression { left, right })
102      }
103  }
104
105  impl Expression for OrExpression {
106      fn interpret(&self, context: &Context) -> bool {
107          println!("  -> Interpreting OR expression:");
108          let left_val = self.left.interpret(context);
109          let right_val = self.right.interpret(context);
110          let result = left_val || right_val;
111          println!("  -> OR result: {} || {} = {}", left_val, right_val, result);
112          result
113      }
114
115      fn to_string(&self) -> String {
116          format!("({} OR {})", self.left.to_string(), self.right.to_string())
117      }
118  }
119
120  // Non-terminal Expression: NOT operation
121  struct NotExpression {
122      operand: Box<dyn Expression>,
123  }
124
125  impl NotExpression {
126      fn new(operand: Box<dyn Expression>) -> Box<dyn Expression> {
127          println!("[NotExpression] Creating NOT expression");
128          Box::new(NotExpression { operand })
129      }
130  }
131
132  impl Expression for NotExpression {
133      fn interpret(&self, context: &Context) -> bool {
134          println!("  -> Interpreting NOT expression:");
135          let val = self.operand.interpret(context);
136          let result = !val;
137          println!("  -> NOT result: !{} = {}", val, result);
138          result
139      }
140
141      fn to_string(&self) -> String {
142          format!("(NOT {})", self.operand.to_string())
143      }
144  }
145
146  fn main() {
147      println!("=== Interpreter Design Pattern Demo ===\n");
148
149      // Create context with variable bindings
150      println!("Step 1: Setting up context with variable bindings");
151      println!("------------------------------------------------");
152      let mut context: Context = HashMap::new();
153      context.insert("x".to_string(), true);
154      context.insert("y".to_string(), false);
155      context.insert("z".to_string(), true);
156      println!("Context: x = true, y = false, z = true\n");
157
158      // Example 1: Simple AND expression (x AND y)
159      println!("Step 2: Building expression: x AND y");
160      println!("------------------------------------");
161      let expr1 = AndExpression::new(Variable::new("x"), Variable::new("y"));
162      println!("Expression tree: {}\n", expr1.to_string());
163
164      println!("Step 3: Interpreting expression: x AND y");
165      println!("----------------------------------------");
166      let result1 = expr1.interpret(&context);
167      println!("Final result: {}\n", result1);
168
169      // Example 2: OR expression (x OR y)
170      println!("Step 4: Building expression: x OR y");
171      println!("-----------------------------------");
172      let expr2 = OrExpression::new(Variable::new("x"), Variable::new("y"));
173      println!("Expression tree: {}\n", expr2.to_string());
174
175      println!("Step 5: Interpreting expression: x OR y");
176      println!("---------------------------------------");
177      let result2 = expr2.interpret(&context);
178      println!("Final result: {}\n", result2);
179
180      // Example 3: NOT expression (NOT y)
181      println!("Step 6: Building expression: NOT y");
182      println!("----------------------------------");
183      let expr3 = NotExpression::new(Variable::new("y"));
184      println!("Expression tree: {}\n", expr3.to_string());
185
186      println!("Step 7: Interpreting expression: NOT y");
187      println!("--------------------------------------");
188      let result3 = expr3.interpret(&context);
189      println!("Final result: {}\n", result3);
190
191      // Example 4: Complex nested expression ((x AND z) OR (NOT y))
192      println!("Step 8: Building complex expression: (x AND z) OR (NOT y)");
193      println!("---------------------------------------------------------");
194      let expr4 = OrExpression::new(
195          AndExpression::new(Variable::new("x"), Variable::new("z")),
196          NotExpression::new(Variable::new("y")),
197      );
198      println!("Expression tree: {}\n", expr4.to_string());
199
200      println!("Step 9: Interpreting expression: (x AND z) OR (NOT y)");
201      println!("-----------------------------------------------------");
202      let result4 = expr4.interpret(&context);
203      println!("Final result: {}\n", result4);
204
205      // Example 5: Expression with constants ((true AND x) OR false)
206      println!("Step 10: Building expression with constants: (true AND x) OR false");
207      println!("------------------------------------------------------------------");
208      let expr5 = OrExpression::new(
209          AndExpression::new(Constant::new(true), Variable::new("x")),
210          Constant::new(false),
211      );
212      println!("Expression tree: {}\n", expr5.to_string());
213
214      println!("Step 11: Interpreting expression: (true AND x) OR false");
215      println!("--------------------------------------------------------");
216      let result5 = expr5.interpret(&context);
217      println!("Final result: {}\n", result5);
218
219      // Summary
220      println!("=== Summary of Results ===");
221      println!("Expression 1 (x AND y):                  {}", result1);
222      println!("Expression 2 (x OR y):                   {}", result2);
223      println!("Expression 3 (NOT y):                    {}", result3);
224      println!("Expression 4 ((x AND z) OR (NOT y)):     {}", result4);
225      println!("Expression 5 ((true AND x) OR false):    {}", result5);
226  }
```

---

## Program Output

```
=== Interpreter Design Pattern Demo ===

Step 1: Setting up context with variable bindings
------------------------------------------------
Context: x = true, y = false, z = true

Step 2: Building expression: x AND y
------------------------------------
[Variable] Creating variable expression: x
[Variable] Creating variable expression: y
[AndExpression] Creating AND expression
Expression tree: (x AND y)

Step 3: Interpreting expression: x AND y
----------------------------------------
  -> Interpreting AND expression:
  -> Interpreting Variable 'x': true
  -> Interpreting Variable 'y': false
  -> AND result: true && false = false
Final result: false

Step 4: Building expression: x OR y
-----------------------------------
[Variable] Creating variable expression: x
[Variable] Creating variable expression: y
[OrExpression] Creating OR expression
Expression tree: (x OR y)

Step 5: Interpreting expression: x OR y
---------------------------------------
  -> Interpreting OR expression:
  -> Interpreting Variable 'x': true
  -> Interpreting Variable 'y': false
  -> OR result: true || false = true
Final result: true

Step 6: Building expression: NOT y
----------------------------------
[Variable] Creating variable expression: y
[NotExpression] Creating NOT expression
Expression tree: (NOT y)

Step 7: Interpreting expression: NOT y
--------------------------------------
  -> Interpreting NOT expression:
  -> Interpreting Variable 'y': false
  -> NOT result: !false = true
Final result: true

Step 8: Building complex expression: (x AND z) OR (NOT y)
---------------------------------------------------------
[Variable] Creating variable expression: x
[Variable] Creating variable expression: z
[AndExpression] Creating AND expression
[Variable] Creating variable expression: y
[NotExpression] Creating NOT expression
[OrExpression] Creating OR expression
Expression tree: ((x AND z) OR (NOT y))

Step 9: Interpreting expression: (x AND z) OR (NOT y)
-----------------------------------------------------
  -> Interpreting OR expression:
  -> Interpreting AND expression:
  -> Interpreting Variable 'x': true
  -> Interpreting Variable 'z': true
  -> AND result: true && true = true
  -> Interpreting NOT expression:
  -> Interpreting Variable 'y': false
  -> NOT result: !false = true
  -> OR result: true || true = true
Final result: true

Step 10: Building expression with constants: (true AND x) OR false
------------------------------------------------------------------
[Constant] Creating constant expression: true
[Variable] Creating variable expression: x
[AndExpression] Creating AND expression
[Constant] Creating constant expression: false
[OrExpression] Creating OR expression
Expression tree: ((true AND x) OR false)

Step 11: Interpreting expression: (true AND x) OR false
--------------------------------------------------------
  -> Interpreting OR expression:
  -> Interpreting AND expression:
  -> Interpreting Constant: true
  -> Interpreting Variable 'x': true
  -> AND result: true && true = true
  -> Interpreting Constant: false
  -> OR result: true || false = true
Final result: true

=== Summary of Results ===
Expression 1 (x AND y):                  false
Expression 2 (x OR y):                   true
Expression 3 (NOT y):                    true
Expression 4 ((x AND z) OR (NOT y)):     true
Expression 5 ((true AND x) OR false):    true
```

---

## Code Annotations

### Key Sections Explained

#### Lines 6-7: Context Type Definition
The `Context` type alias defines a `HashMap<String, bool>` that stores variable bindings. This allows the interpreter to look up variable values during evaluation.

#### Lines 9-13: Abstract Expression Trait
The `Expression` trait is the core abstraction of the Interpreter pattern. It defines:
- `interpret()`: Evaluates the expression given a context
- `to_string()`: Returns a string representation of the expression

All concrete expressions implement this trait, enabling polymorphic behavior through trait objects (`Box<dyn Expression>`).

#### Lines 15-36: Constant (Terminal Expression)
The `Constant` struct represents literal boolean values. As a terminal expression, it returns its value directly without further interpretation. The `_context` parameter is unused since constants don't depend on variable bindings.

#### Lines 38-62: Variable (Terminal Expression)
The `Variable` struct looks up its value in the context. It demonstrates how terminal expressions can interact with the environment. Note the use of `unwrap_or(&false)` to provide a default value for undefined variables.

#### Lines 64-90: AndExpression (Non-terminal Expression)
The `AndExpression` combines two sub-expressions with logical AND. It:
1. Recursively interprets the left operand
2. Recursively interprets the right operand
3. Combines results with `&&`

This demonstrates how non-terminal expressions compose other expressions.

#### Lines 92-118: OrExpression (Non-terminal Expression)
Similar to `AndExpression` but uses logical OR (`||`) to combine operands.

#### Lines 120-144: NotExpression (Non-terminal Expression)
A unary operator that negates its single operand with `!`.

#### Lines 146-226: Main Function
Demonstrates the pattern with five progressively complex examples:
1. Simple AND between two variables
2. Simple OR between two variables
3. NOT of a single variable
4. Nested expression with AND, OR, and NOT
5. Expression mixing constants and variables

---

### Output to Source Code Correlation

| Output Section | Source Lines | Description |
|----------------|--------------|-------------|
| Context setup | 150-156 | Creates HashMap with x=true, y=false, z=true |
| Variable creation messages | 44-45 | Printed when `Variable::new()` is called |
| Constant creation messages | 21-22 | Printed when `Constant::new()` is called |
| AND expression creation | 71-72 | Printed when `AndExpression::new()` is called |
| OR expression creation | 99-100 | Printed when `OrExpression::new()` is called |
| NOT expression creation | 126-127 | Printed when `NotExpression::new()` is called |
| Variable interpretation | 53-56 | Looks up value in context and prints result |
| Constant interpretation | 28-30 | Returns stored value directly |
| AND interpretation | 78-84 | Interprets both operands, applies `&&` |
| OR interpretation | 106-112 | Interprets both operands, applies `||` |
| NOT interpretation | 133-138 | Interprets operand, applies `!` |
| Final results summary | 220-225 | Prints all five expression results |

---

### Key Characteristics of the Interpreter Pattern in Rust

1. **Trait Objects for Polymorphism**
   - Uses `Box<dyn Expression>` to store heterogeneous expression types
   - Enables runtime polymorphism through dynamic dispatch
   - All expressions can be treated uniformly through the `Expression` trait

2. **Composite Pattern Integration**
   - Non-terminal expressions contain `Box<dyn Expression>` fields
   - Creates tree structures where nodes can be terminals or composites
   - Recursive `interpret()` calls traverse the expression tree

3. **Ownership and Memory Safety**
   - `Box` provides heap allocation and single ownership
   - Expression trees are automatically deallocated when dropped
   - No manual memory management required

4. **Type Safety with Flexibility**
   - Trait bounds ensure only valid expressions can be composed
   - Context type is strongly typed (`HashMap<String, bool>`)
   - Compile-time guarantees prevent type errors

5. **Extensibility**
   - New expression types can be added without modifying existing code
   - Simply implement the `Expression` trait for new operations
   - Could easily add XOR, NAND, or other boolean operations

6. **Use Cases**
   - DSL (Domain-Specific Language) implementation
   - Rule engines and business logic evaluation
   - Mathematical expression parsers
   - Query language interpreters
   - Configuration file parsers

7. **Trade-offs**
   - **Pros**: Clean separation of concerns, easy to extend grammar
   - **Cons**: Can be inefficient for complex grammars (consider parser generators instead)
   - Best suited for simple, well-defined grammars

---

## Build and Run

```bash
# Compile
rustc main_interpreter.rs -o main_interpreter.exe

# Run
./main_interpreter.exe
```

No external dependencies required - uses only the Rust standard library.
