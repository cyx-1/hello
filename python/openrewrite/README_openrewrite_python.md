# OpenRewrite Python Demo: Automated Code Refactoring

This example demonstrates OpenRewrite's recipe-based approach to automated Python code refactoring using AST (Abstract Syntax Tree) transformations.

## Overview

**OpenRewrite** is an automated refactoring framework that applies "recipes" (transformation rules) to source code. While the full OpenRewrite Python support requires the **Moderne CLI**, this demo illustrates the core concepts using Python's built-in `ast` module.

## Important Source Code

### Recipe 1: Replace Built-in Shadowing (Lines 49-61)

```python
49  | class ReplaceBuiltinShadowingVisitor(ast.NodeTransformer):
50  |     """
51  |     Recipe: Replace variable names that shadow built-in functions.
52  |     Example: Renames 'sum' to 'total' to avoid shadowing built-in sum()
53  |     """
54  |
55  |     def __init__(self):
56  |         self.replacements = {"sum": "total"}
57  |
58  |     def visit_Name(self, node: ast.Name) -> Any:
59  |         if node.id in self.replacements:
60  |             node.id = self.replacements[node.id]
61  |         return node
```

**What it does:** This visitor pattern traverses the AST and renames variables that shadow Python built-ins. Line 59-60 checks each name node and replaces it according to the mapping.

### Recipe 2: Simplify Boolean Comparisons (Lines 64-86)

```python
64  | class SimplifyComparisonVisitor(ast.NodeTransformer):
65  |     """
66  |     Recipe: Simplify boolean comparisons.
67  |     Example: 'x == True' becomes 'x', 'x == False' becomes 'not x'
68  |     """
69  |
70  |     def visit_Compare(self, node: ast.Compare) -> Any:
71  |         self.generic_visit(node)
72  |
73  |         # Check for 'x == True' or 'x == False' patterns
74  |         if (
75  |             len(node.ops) == 1
76  |             and isinstance(node.ops[0], ast.Eq)
77  |             and len(node.comparators) == 1
78  |         ):
79  |             comparator = node.comparators[0]
80  |
81  |             # x == True -> x
82  |             if isinstance(comparator, ast.Constant) and comparator.value is True:
83  |                 return node.left
84  |
85  |             # x == False -> not x
86  |             if isinstance(comparator, ast.Constant) and comparator.value is False:
87  |                 return ast.UnaryOp(op=ast.Not(), operand=node.left)
88  |
89  |         return node
```

**What it does:** Lines 82-83 detect `x == True` patterns and replace them with just `x`. Lines 86-87 detect `x == False` and replace with `not x`, following Python best practices.

### Recipe 3: Use List Comprehension (Lines 92-150)

```python
92  | class UseListComprehensionVisitor(ast.NodeTransformer):
93  |     """
94  |     Recipe: Convert simple for-loops with append to list comprehensions.
95  |     Example: Transforms manual iteration patterns to more Pythonic list comprehensions
96  |     """
97  |
98  |     def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
99  |         self.generic_visit(node)
100 |
101 |         # Look for pattern: result = []; for i in range(len(x)): result.append(x[i] * 2)
102 |         if len(node.body) >= 2:
103 |             # Check if first statement is result = []
104 |             first_stmt = node.body[0]
105 |             if isinstance(first_stmt, ast.Assign) and len(first_stmt.targets) == 1:
106 |                 target = first_stmt.targets[0]
107 |                 if (
108 |                     isinstance(target, ast.Name)
109 |                     and isinstance(first_stmt.value, ast.List)
110 |                     and len(first_stmt.value.elts) == 0
111 |                 ):
112 |                     result_name = target.id
113 |
114 |                     # Check if second statement is the for loop
115 |                     second_stmt = node.body[1]
116 |                     if isinstance(second_stmt, ast.For):
117 |                         self._try_convert_to_comprehension(
118 |                             node, result_name, first_stmt, second_stmt
119 |                         )
120 |
121 |         return node
122 |
123 |     def _try_convert_to_comprehension(
124 |         self, func_node, result_name, assign_stmt, for_stmt
125 |     ):
126 |         """Helper to convert specific for-loop patterns to list comprehensions"""
127 |         # Check if for loop body is: result.append(...)
128 |         if (
129 |             len(for_stmt.body) == 1
130 |             and isinstance(for_stmt.body[0], ast.Expr)
131 |             and isinstance(for_stmt.body[0].value, ast.Call)
132 |         ):
133 |             call = for_stmt.body[0].value
134 |             if (
135 |                 isinstance(call.func, ast.Attribute)
136 |                 and call.func.attr == "append"
137 |                 and isinstance(call.func.value, ast.Name)
138 |                 and call.func.value.id == result_name
139 |                 and len(call.args) == 1
140 |             ):
141 |                 # Pattern matched! Replace with list comprehension
142 |                 # result = [expr for var in iter]
143 |                 comprehension = ast.ListComp(
144 |                     elt=call.args[0],
145 |                     generators=[
146 |                         ast.comprehension(
147 |                             target=for_stmt.target,
148 |                             iter=for_stmt.iter,
149 |                             ifs=[],
150 |                             is_async=0,
151 |                         )
152 |                     ],
153 |                 )
154 |
155 |                 new_assign = ast.Assign(
156 |                     targets=[ast.Name(id=result_name, ctx=ast.Store())],
157 |                     value=comprehension,
158 |                 )
159 |
160 |                 # Replace the two statements with single list comprehension
161 |                 idx = func_node.body.index(assign_stmt)
162 |                 func_node.body[idx] = new_assign
163 |                 func_node.body.remove(for_stmt)
```

**What it does:** This more complex recipe detects the pattern of initializing an empty list (lines 105-111), then appending to it in a loop (lines 128-140). Lines 143-153 create a list comprehension AST node to replace both statements with a single, more Pythonic expression.

### Main Recipe Application (Lines 166-187)

```python
166 | def apply_recipes(source_code: str) -> tuple[str, list[str]]:
167 |     """
168 |     Apply multiple OpenRewrite-style recipes to the source code.
169 |
170 |     Args:
171 |         source_code: Python source code to refactor
172 |
173 |     Returns:
174 |         Tuple of (refactored_code, list_of_applied_recipes)
175 |     """
176 |     # Parse source code into AST
177 |     tree = ast.parse(source_code)
178 |
179 |     # Track which recipes were applied
180 |     applied_recipes = []
181 |
182 |     # Recipe 1: Replace built-in shadowing
183 |     recipe1 = ReplaceBuiltinShadowingVisitor()
184 |     tree = recipe1.visit(tree)
185 |     applied_recipes.append("ReplaceBuiltinShadowing")
186 |
187 |     # Recipe 2: Simplify boolean comparisons
188 |     recipe2 = SimplifyComparisonVisitor()
189 |     tree = recipe2.visit(tree)
190 |     applied_recipes.append("SimplifyBooleanComparisons")
191 |
192 |     # Recipe 3: Use list comprehensions
193 |     recipe3 = UseListComprehensionVisitor()
194 |     tree = recipe3.visit(tree)
195 |     applied_recipes.append("UseListComprehension")
196 |
197 |     # Fix missing locations in AST (required for unparsing)
198 |     ast.fix_missing_locations(tree)
199 |
200 |     # Generate refactored source code from transformed AST
201 |     refactored_code = ast.unparse(tree)
202 |
203 |     return refactored_code, applied_recipes
```

**What it does:** Line 177 parses source into AST. Lines 183-195 sequentially apply each recipe transformer to the AST. Line 198 fixes AST node locations (required after modifications). Line 201 converts the transformed AST back to Python source code.

## Program Output

```
================================================================================
OpenRewrite Python Demo: Automated Code Refactoring
================================================================================

📚 About OpenRewrite for Python:
   OpenRewrite is an automated refactoring framework
   Python support requires: Moderne CLI (https://docs.moderne.io/)
   This demo simulates the recipe concept using Python's AST module

📝 ORIGINAL SOURCE CODE:
--------------------------------------------------------------------------------
  1 | def calculate_total(items):
  2 |     sum = 0
  3 |     for item in items:
  4 |         sum = sum + item
  5 |     return sum
  6 |
  7 | def process_data(data):
  8 |     result = []
  9 |     for i in range(len(data)):
 10 |         result.append(data[i] * 2)
 11 |     return result
 12 |
 13 | def check_value(x):
 14 |     if x == True:
 15 |         return "yes"
 16 |     elif x == False:
 17 |         return "no"
 18 |     else:
 19 |         return "unknown"

🔧 APPLYING RECIPES:
--------------------------------------------------------------------------------
  1. ReplaceBuiltinShadowing
  2. SimplifyBooleanComparisons
  3. UseListComprehension

✨ REFACTORED SOURCE CODE:
--------------------------------------------------------------------------------
  1 | def calculate_total(items):
  2 |     total = 0
  3 |     for item in items:
  4 |         total = total + item
  5 |     return total
  6 |
  7 | def process_data(data):
  8 |     result = [data[i] * 2 for i in range(len(data))]
  9 |     return result
 10 |
  11 | def check_value(x):
  12 |     if x:
  13 |         return 'yes'
  14 |     elif not x:
  15 |         return 'no'
  16 |     else:
  17 |         return 'unknown'

📖 TRANSFORMATIONS APPLIED:
--------------------------------------------------------------------------------
1. ReplaceBuiltinShadowing (Lines 1-5):
   Before: sum = 0; sum = sum + item
   After:  total = 0; total = total + item
   Reason: Avoid shadowing built-in sum() function

2. SimplifyBooleanComparisons (Lines 13-18):
   Before: if x == True: ... elif x == False:
   After:  if x: ... elif not x:
   Reason: Direct boolean evaluation is more Pythonic

3. UseListComprehension (Lines 7-11):
   Before: result = []; for i in range(len(data)): result.append(...)
   After:  result = [data[i] * 2 for i in range(len(data))]
   Reason: List comprehensions are more concise and faster

🚀 USING REAL OPENREWRITE FOR PYTHON:
--------------------------------------------------------------------------------
1. Install Moderne CLI:
   curl -L https://pkgs.moderne.io/install.sh | sh

2. Run a recipe on your Python project:
   mod run . --recipe <RecipeName>

3. Available at: https://github.com/openrewrite/rewrite-python
================================================================================
```

## Annotations: Correlating Source Code and Output

### 1. Built-in Shadowing Transformation (Source Lines 49-61 → Output Lines 1-5)

**Source Code (Lines 49-61):** The `ReplaceBuiltinShadowingVisitor` class defines the transformation rule.

**Original Code (Output Lines 2, 4):**
```python
  2 |     sum = 0
  4 |     sum = sum + item
```

**Refactored Code (Output Lines 2, 4):**
```python
  2 |     total = 0
  4 |     total = total + item
```

**Transformation:** The recipe detected that `sum` shadows Python's built-in `sum()` function and renamed it to `total`. This is applied by the visitor's `visit_Name` method at source line 58-61.

### 2. Boolean Comparison Simplification (Source Lines 64-89 → Output Lines 11-17)

**Source Code (Lines 64-89):** The `SimplifyComparisonVisitor` class implements the transformation.

**Original Code (Output Lines 14, 16):**
```python
 14 |     if x == True:
 16 |     elif x == False:
```

**Refactored Code (Output Lines 12, 14):**
```python
 12 |     if x:
 14 |     elif not x:
```

**Transformation:** The recipe at source lines 82-87 detects explicit comparisons to `True`/`False` and simplifies them. Line 82 handles `== True` → direct boolean, line 86 handles `== False` → `not` operator.

### 3. List Comprehension Conversion (Source Lines 92-163 → Output Line 8)

**Source Code (Lines 92-163):** The `UseListComprehensionVisitor` class performs complex pattern matching.

**Original Code (Output Lines 8-10):**
```python
  8 |     result = []
  9 |     for i in range(len(data)):
 10 |         result.append(data[i] * 2)
```

**Refactored Code (Output Line 8):**
```python
  8 |     result = [data[i] * 2 for i in range(len(data))]
```

**Transformation:** The recipe matches the pattern at source lines 105-119 (empty list initialization followed by for-loop with append), then constructs a list comprehension at lines 143-153. Two statements become one elegant expression.

## Version Requirements

- **Python:** 3.12 or higher (uses inline script metadata format)
- **OpenRewrite Python (actual):** Requires Moderne CLI
- **This demo:** Uses only Python standard library (`ast` module)

## Running the Demo

```bash
uv run python main_openrewrite_python.py
```

## Using Real OpenRewrite for Python

For production use with actual OpenRewrite:

1. **Install Moderne CLI:**
   ```bash
   curl -L https://pkgs.moderne.io/install.sh | sh
   ```

2. **Run recipes on your project:**
   ```bash
   mod run . --recipe <RecipeName>
   ```

3. **Explore available recipes:**
   - Visit: https://docs.moderne.io/
   - Repository: https://github.com/openrewrite/rewrite-python

## Key Concepts

- **Recipes:** Transformation rules that modify code (like the three visitor classes in this demo)
- **AST (Abstract Syntax Tree):** Structured representation of source code that enables programmatic transformations
- **Visitor Pattern:** Design pattern used to traverse and modify AST nodes
- **Moderne CLI:** Required tooling for running OpenRewrite on Python projects

## References

- [OpenRewrite Documentation](https://docs.openrewrite.org/)
- [OpenRewrite Python Repository](https://github.com/openrewrite/rewrite-python)
- [Moderne CLI Documentation](https://docs.moderne.io/user-documentation/moderne-cli/getting-started/cli-intro/)
- [Python AST Module](https://docs.python.org/3/library/ast.html)
