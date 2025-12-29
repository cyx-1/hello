#!/usr/bin/env python3
"""
Stop hook that manages tasks in plan.md.
After each task completes:
1. Marks the current task as done in plan.md
2. Picks up the next incomplete task
3. Continues until all tasks are complete
"""

import json
import sys
import os
from pathlib import Path


def find_project_root():
    """Find the project root by looking for plan.md"""
    current = Path.cwd()

    # Check current directory first
    if (current / "plan.md").exists():
        return current

    # Walk up the directory tree
    for parent in current.parents:
        if (parent / "plan.md").exists():
            return parent

    return None


def read_plan(plan_file):
    """Read the plan.md file and return its lines"""
    try:
        with open(plan_file, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return None


def write_plan(plan_file, lines):
    """Write updated lines back to plan.md"""
    with open(plan_file, 'w') as f:
        f.writelines(lines)


def find_first_incomplete_task(lines):
    """Find the index of the first incomplete task"""
    for i, line in enumerate(lines):
        if line.strip().startswith('- [ ]'):
            return i
    return None


def mark_task_complete(lines, task_index):
    """Mark a task as complete by changing [ ] to [x]"""
    line = lines[task_index]
    lines[task_index] = line.replace('- [ ]', '- [x]', 1)
    return lines


def extract_task_description(line):
    """Extract the task description from a markdown task line"""
    # Remove the checkbox part and get the description
    if '- [ ]' in line:
        return line.split('- [ ]', 1)[1].strip()
    elif '- [x]' in line:
        return line.split('- [x]', 1)[1].strip()
    return line.strip()


def main():
    project_root = None
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())

        # Check if stop hook is already active (recursion prevention)
        if input_data.get('stop_hook_active') == True:
            sys.exit(0)

        # Find project root
        project_root = find_project_root()
        if not project_root:
            # No plan.md found, exit normally
            sys.exit(0)

        plan_file = project_root / "plan.md"

        # Read current plan
        lines = read_plan(plan_file)
        if lines is None:
            sys.exit(0)

        # Find the first incomplete task
        incomplete_index = find_first_incomplete_task(lines)

        if incomplete_index is None:
            # No incomplete tasks, all done!
            print(json.dumps({"decision": "approve", "reason": "All tasks in plan.md have been completed! 🎉"}))
            sys.exit(0)

        # Mark the current task as complete
        lines = mark_task_complete(lines, incomplete_index)
        write_plan(plan_file, lines)

        # Check if there are more incomplete tasks
        next_incomplete = find_first_incomplete_task(lines)

        if next_incomplete is not None:
            # There are more tasks, continue with the next one
            next_task = extract_task_description(lines[next_incomplete])

            response = {
                "decision": "approve",
                "reason": f"Task completed! Moving to next task: {next_task}",
                "systemMessage": f"Please continue with the next task from plan.md: {next_task}",
            }
            print(json.dumps(response))
            sys.exit(2)
        else:
            # That was the last task!
            print(json.dumps({"decision": "approve", "reason": "Final task completed! All tasks in plan.md are now done! 🎉"}))
            sys.exit(0)

    except Exception as e:
        # Log error but don't block
        error_log = project_root / ".claude" / "hook_errors.log" if project_root else Path("hook_errors.log")
        with open(error_log, 'a') as f:
            f.write(f"Stop hook error: {str(e)}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
