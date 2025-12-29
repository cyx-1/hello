# Task Manager Stop Hook

## Overview

This stop hook automatically manages tasks defined in `plan.md` at the project root. After each task completion, it:

1. Marks the current task as done in `plan.md`
2. Picks up the next incomplete task
3. Continues working until all tasks are marked complete

## How It Works

### Execution Flow

1. **After Claude finishes a response**, the stop hook executes
2. **Finds the first incomplete task** in `plan.md` (marked with `- [ ]`)
3. **Marks it as complete** (changes to `- [x]`)
4. **Checks for more tasks**:
   - If more tasks exist: Returns `continue` with the next task description
   - If no more tasks: Approves and stops

### plan.md Format

The `plan.md` file should use standard Markdown task list format:

```markdown
# Task Plan

## Tasks

- [ ] Task 1: Description of first task
- [ ] Task 2: Description of second task
- [ ] Task 3: Description of third task
```

As tasks complete, they're automatically marked:

```markdown
- [x] Task 1: Description of first task  ✅ Done
- [ ] Task 2: Description of second task  ⬅ Next
- [ ] Task 3: Description of third task
```

## Configuration

The hook is configured in `.claude/settings.local.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/task_manager_stop_hook.py"
          }
        ]
      }
    ]
  }
}
```

## Features

- ✅ **Automatic task progression**: No manual intervention needed
- ✅ **Clear visibility**: All tasks tracked in `plan.md`
- ✅ **Recursion prevention**: Won't trigger on its own continuations
- ✅ **Error handling**: Logs errors without blocking Claude
- ✅ **Project-aware**: Finds `plan.md` automatically
- ✅ **Completion celebration**: Shows success message when all tasks done

## Usage

1. Create a `plan.md` file in your project root with your tasks
2. Start working with Claude as normal
3. The stop hook will automatically:
   - Mark completed tasks
   - Move to the next task
   - Continue until all tasks are done

## Example Workflow

**Initial plan.md:**
```markdown
- [ ] Create Python script
- [ ] Add type hints
- [ ] Run linter
- [ ] Create README
```

**After Claude finishes creating the script:**
```markdown
- [x] Create Python script
- [ ] Add type hints  ⬅ Hook automatically continues with this
- [ ] Run linter
- [ ] Create README
```

The hook will automatically prompt Claude to work on "Add type hints" next.

## Error Logging

Errors are logged to `.claude/hook_errors.log` for debugging without blocking execution.

## Customization

You can modify `task_manager_stop_hook.py` to:
- Change the task format
- Add task priorities
- Include time tracking
- Send notifications
- Integrate with external tools
