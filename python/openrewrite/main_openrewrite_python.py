#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""
OpenRewrite Python Demo: Automated Code Refactoring

This demonstrates the concept of OpenRewrite's recipe-based refactoring for Python.
Note: Actual OpenRewrite Python support requires Moderne CLI (https://docs.moderne.io/)

This example uses Python's AST module to simulate how OpenRewrite recipes work:
- Parse source code into an Abstract Syntax Tree (AST)
- Apply transformation recipes to the AST
- Generate modified source code from the transformed AST
"""

import ast
from typing import Any


# Sample source code to refactor (before transformation)
SAMPLE_CODE = """
def calculate_total(items):
    sum = 0
    for item in items:
        sum = sum + item
    return sum

def process_data(data):
    result = []
    for i in range(len(data)):
        result.append(data[i] * 2)
    return result

def check_value(x):
    if x == True:
        return "yes"
    elif x == False:
        return "no"
    else:
        return "unknown"
"""


class ReplaceBuiltinShadowingVisitor(ast.NodeTransformer):
    """
    Recipe: Replace variable names that shadow built-in functions.
    Example: Renames 'sum' to 'total' to avoid shadowing built-in sum()
    """

    def __init__(self):
        self.replacements = {"sum": "total"}

    def visit_Name(self, node: ast.Name) -> Any:
        if node.id in self.replacements:
            node.id = self.replacements[node.id]
        return node


class SimplifyComparisonVisitor(ast.NodeTransformer):
    """
    Recipe: Simplify boolean comparisons.
    Example: 'x == True' becomes 'x', 'x == False' becomes 'not x'
    """

    def visit_Compare(self, node: ast.Compare) -> Any:
        self.generic_visit(node)

        # Check for 'x == True' or 'x == False' patterns
        if (
            len(node.ops) == 1
            and isinstance(node.ops[0], ast.Eq)
            and len(node.comparators) == 1
        ):
            comparator = node.comparators[0]

            # x == True -> x
            if isinstance(comparator, ast.Constant) and comparator.value is True:
                return node.left

            # x == False -> not x
            if isinstance(comparator, ast.Constant) and comparator.value is False:
                return ast.UnaryOp(op=ast.Not(), operand=node.left)

        return node


class UseListComprehensionVisitor(ast.NodeTransformer):
    """
    Recipe: Convert simple for-loops with append to list comprehensions.
    Example: Transforms manual iteration patterns to more Pythonic list comprehensions
    """

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        self.generic_visit(node)

        # Look for pattern: result = []; for i in range(len(x)): result.append(x[i] * 2)
        if len(node.body) >= 2:
            # Check if first statement is result = []
            first_stmt = node.body[0]
            if isinstance(first_stmt, ast.Assign) and len(first_stmt.targets) == 1:
                target = first_stmt.targets[0]
                if (
                    isinstance(target, ast.Name)
                    and isinstance(first_stmt.value, ast.List)
                    and len(first_stmt.value.elts) == 0
                ):
                    result_name = target.id

                    # Check if second statement is the for loop
                    second_stmt = node.body[1]
                    if isinstance(second_stmt, ast.For):
                        self._try_convert_to_comprehension(
                            node, result_name, first_stmt, second_stmt
                        )

        return node

    def _try_convert_to_comprehension(
        self, func_node, result_name, assign_stmt, for_stmt
    ):
        """Helper to convert specific for-loop patterns to list comprehensions"""
        # Check if for loop body is: result.append(...)
        if (
            len(for_stmt.body) == 1
            and isinstance(for_stmt.body[0], ast.Expr)
            and isinstance(for_stmt.body[0].value, ast.Call)
        ):
            call = for_stmt.body[0].value
            if (
                isinstance(call.func, ast.Attribute)
                and call.func.attr == "append"
                and isinstance(call.func.value, ast.Name)
                and call.func.value.id == result_name
                and len(call.args) == 1
            ):
                # Pattern matched! Replace with list comprehension
                # result = [expr for var in iter]
                comprehension = ast.ListComp(
                    elt=call.args[0],
                    generators=[
                        ast.comprehension(
                            target=for_stmt.target,
                            iter=for_stmt.iter,
                            ifs=[],
                            is_async=0,
                        )
                    ],
                )

                new_assign = ast.Assign(
                    targets=[ast.Name(id=result_name, ctx=ast.Store())],
                    value=comprehension,
                )

                # Replace the two statements with single list comprehension
                idx = func_node.body.index(assign_stmt)
                func_node.body[idx] = new_assign
                func_node.body.remove(for_stmt)


def apply_recipes(source_code: str) -> tuple[str, list[str]]:
    """
    Apply multiple OpenRewrite-style recipes to the source code.

    Args:
        source_code: Python source code to refactor

    Returns:
        Tuple of (refactored_code, list_of_applied_recipes)
    """
    # Parse source code into AST
    tree = ast.parse(source_code)

    # Track which recipes were applied
    applied_recipes = []

    # Recipe 1: Replace built-in shadowing
    recipe1 = ReplaceBuiltinShadowingVisitor()
    tree = recipe1.visit(tree)
    applied_recipes.append("ReplaceBuiltinShadowing")

    # Recipe 2: Simplify boolean comparisons
    recipe2 = SimplifyComparisonVisitor()
    tree = recipe2.visit(tree)
    applied_recipes.append("SimplifyBooleanComparisons")

    # Recipe 3: Use list comprehensions
    recipe3 = UseListComprehensionVisitor()
    tree = recipe3.visit(tree)
    applied_recipes.append("UseListComprehension")

    # Fix missing locations in AST (required for unparsing)
    ast.fix_missing_locations(tree)

    # Generate refactored source code from transformed AST
    refactored_code = ast.unparse(tree)

    return refactored_code, applied_recipes


def main():
    """Demonstrate OpenRewrite-style Python refactoring"""
    print("=" * 80)
    print("OpenRewrite Python Demo: Automated Code Refactoring")
    print("=" * 80)
    print()

    # Line 193: Display information about actual OpenRewrite
    print("📚 About OpenRewrite for Python:")
    print("   OpenRewrite is an automated refactoring framework")
    print("   Python support requires: Moderne CLI (https://docs.moderne.io/)")
    print("   This demo simulates the recipe concept using Python's AST module")
    print()

    # Line 200: Show original source code
    print("📝 ORIGINAL SOURCE CODE:")
    print("-" * 80)
    for i, line in enumerate(SAMPLE_CODE.strip().split("\n"), 1):
        print(f"{i:3d} | {line}")
    print()

    # Line 207: Apply refactoring recipes
    print("🔧 APPLYING RECIPES:")
    print("-" * 80)
    refactored_code, recipes = apply_recipes(SAMPLE_CODE)

    for i, recipe in enumerate(recipes, 1):
        print(f"  {i}. {recipe}")
    print()

    # Line 216: Show refactored source code
    print("✨ REFACTORED SOURCE CODE:")
    print("-" * 80)
    for i, line in enumerate(refactored_code.strip().split("\n"), 1):
        print(f"{i:3d} | {line}")
    print()

    # Line 223: Explain transformations
    print("📖 TRANSFORMATIONS APPLIED:")
    print("-" * 80)
    print("1. ReplaceBuiltinShadowing (Lines 1-5):")
    print("   Before: sum = 0; sum = sum + item")
    print("   After:  total = 0; total = total + item")
    print("   Reason: Avoid shadowing built-in sum() function")
    print()

    print("2. SimplifyBooleanComparisons (Lines 13-18):")
    print("   Before: if x == True: ... elif x == False:")
    print("   After:  if x: ... elif not x:")
    print("   Reason: Direct boolean evaluation is more Pythonic")
    print()

    print("3. UseListComprehension (Lines 7-11):")
    print("   Before: result = []; for i in range(len(data)): result.append(...)")
    print("   After:  result = [data[i] * 2 for i in range(len(data))]")
    print("   Reason: List comprehensions are more concise and faster")
    print()

    # Line 244: Show how to use real OpenRewrite
    print("🚀 USING REAL OPENREWRITE FOR PYTHON:")
    print("-" * 80)
    print("1. Install Moderne CLI:")
    print("   curl -L https://pkgs.moderne.io/install.sh | sh")
    print()
    print("2. Run a recipe on your Python project:")
    print("   mod run . --recipe <RecipeName>")
    print()
    print("3. Available at: https://github.com/openrewrite/rewrite-python")
    print("=" * 80)


if __name__ == "__main__":
    main()
