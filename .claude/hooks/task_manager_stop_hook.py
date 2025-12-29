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
    log_message("./.claude/stop_hook.log", f"Writing {lines[task_index]} on {task_index} to plan.md")
    return lines


def extract_task_description(line):
    """Extract the task description from a markdown task line"""
    # Remove the checkbox part and get the description
    if '- [ ]' in line:
        return line.split('- [ ]', 1)[1].strip()
    elif '- [x]' in line:
        return line.split('- [x]', 1)[1].strip()
    return line.strip()


def log_message(log_file, message):
    """Write a timestamped message to the log file"""
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")


def main():
    project_root = None
    log_file = None
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())

        # Find project root first so we can set up logging
        project_root = find_project_root()
        if project_root:
            log_file = project_root / ".claude" / "stop_hook.log"
            # Ensure .claude directory exists
            log_file.parent.mkdir(parents=True, exist_ok=True)
        else:
            log_file = Path("stop_hook.log")

        log_message(log_file, "=" * 50)
        log_message(log_file, "Stop hook triggered")
        log_message(log_file, f"Working directory: {Path.cwd()}")
        log_message(log_file, f"Project root: {project_root}")

        # Log input data (excluding sensitive info)
        log_message(log_file, f"Input keys: {list(input_data.keys())}")
        if 'stop_hook_active' in input_data:
            log_message(log_file, f"stop_hook_active: {input_data.get('stop_hook_active')}")

        # Check if stop hook is already active (recursion prevention)
        if input_data.get('stop_hook_active') == True:
            log_message(log_file, "Stop hook already active, exiting to prevent recursion")
            sys.exit(0)

        if not project_root:
            # No plan.md found, exit normally
            log_message(log_file, "No plan.md found in directory tree, exiting")
            sys.exit(0)

        plan_file = project_root / "plan.md"
        log_message(log_file, f"Plan file: {plan_file}")

        # Read current plan
        lines = read_plan(plan_file)
        if lines is None:
            log_message(log_file, "Failed to read plan.md, exiting")
            sys.exit(0)

        log_message(log_file, f"Read {len(lines)} lines from plan.md")

        # Count tasks
        total_tasks = sum(1 for line in lines if '- [ ]' in line or '- [x]' in line)
        completed_tasks = sum(1 for line in lines if '- [x]' in line)
        log_message(log_file, f"Task status: {completed_tasks}/{total_tasks} completed")

        # Find the first incomplete task
        incomplete_index = find_first_incomplete_task(lines)
        log_message(log_file, f"First incomplete task index: {incomplete_index}")

        if incomplete_index is None:
            # No incomplete tasks, all done!
            log_message(log_file, "All tasks completed! Approving.")
            print(json.dumps({"decision": "approve", "reason": "All tasks in plan.md have been completed! 🎉"}))
            sys.exit(0)

        current_task = extract_task_description(lines[incomplete_index])
        log_message(log_file, f"Current task to mark complete: {current_task}")

        # Mark the current task as complete
        lines = mark_task_complete(lines, incomplete_index - 1)
        write_plan(plan_file, lines)
        log_message(log_file, f"Marked task {incomplete_index} as complete")

        # Check if there are more incomplete tasks
        next_incomplete = find_first_incomplete_task(lines)
        log_message(log_file, f"Next incomplete task index: {next_incomplete}")

        if next_incomplete is not None:
            # There are more tasks, continue with the next one
            next_task = extract_task_description(lines[next_incomplete])
            log_message(log_file, f"Next task: {next_task}")
            log_message(log_file, "Blocking to continue with next task")

            response = {
                "decision": "block",
                "reason": f"Task completed! Moving to next task: {next_task}",
                "systemMessage": f"Please continue with the next task from plan.md: {next_task}",
                "stop_hook_active": False,
            }
            print(json.dumps(response))
            sys.exit(2)
        else:
            # That was the last task!
            log_message(log_file, "Final task completed! All done.")
            print(json.dumps({"decision": "approve", "reason": "Final task completed! All tasks in plan.md are now done! 🎉"}))
            sys.exit(0)

    except Exception as e:
        # Log error but don't block
        import traceback

        error_log = project_root / ".claude" / "hook_errors.log" if project_root else Path("hook_errors.log")
        with open(error_log, 'a') as f:
            f.write(f"Stop hook error: {str(e)}\n")
            f.write(f"Traceback:\n{traceback.format_exc()}\n")
        if log_file:
            log_message(log_file, f"ERROR: {str(e)}")
        sys.exit(0)


if __name__ == "__main__":
    main()
