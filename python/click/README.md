# Click - Python CLI Tool Framework

This example demonstrates the Click library, a powerful Python package for creating beautiful command-line interfaces with minimal code.

## Overview

Click is a composable command-line interface creation kit that uses decorators to turn functions into CLI commands. It supports:
- Command groups and subcommands
- Various parameter types (options, arguments, flags)
- Interactive prompts and confirmations
- File handling
- Context passing between commands
- Input validation and custom types
- Styled terminal output

## Key Source Code Features

### 1. Command Groups and Context (Lines 22-50)

```python
# Line 22: Context object for sharing data between commands
class AppContext:
    """Custom context object to share data between commands."""
    def __init__(self):
        self.verbose = False
        self.config_file = None

# Line 30: Main command group - entry point for CLI
@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.option('--config', type=click.Path(), help='Path to config file')
@click.pass_context
def cli(ctx, verbose, config):
    # Line 41: Store context for use in subcommands
    ctx.obj = AppContext()
    ctx.obj.verbose = verbose
    ctx.obj.config_file = config
```

**Output when using verbose flag:**
```
$ uv run main_click.py --verbose greet "Bob"

Verbose mode enabled
Hello, Bob! (greeting 1/1)
```

The `@click.group()` decorator (line 30) creates a command group that serves as the entry point, while `@click.pass_context` (line 34) enables sharing state between commands through the context object defined at line 22.

---

### 2. Simple Commands with Arguments (Lines 51-63)

```python
# Line 51: Simple command with arguments
@cli.command()
@click.argument('name')
@click.argument('count', type=int, default=1)
def greet(name, count):
    """Greet someone COUNT times."""
    # Line 61: Loop to greet multiple times
    for i in range(count):
        click.echo(f"Hello, {name}! (greeting {i + 1}/{count})")
```

**Output:**
```
$ uv run main_click.py greet Alice 3

Hello, Alice! (greeting 1/3)
Hello, Alice! (greeting 2/3)
Hello, Alice! (greeting 3/3)
```

The `@click.argument()` decorator (lines 52-53) defines positional arguments. The `count` argument has a default value of 1 and is automatically converted to an integer by Click.

---

### 3. Interactive Prompts with Type Choices (Lines 66-86)

```python
# Line 66: Command with various option types
@cli.command()
@click.option('--name', prompt='Your name', help='The person to greet')
@click.option('--age', type=int, prompt='Your age', help='Your age')
@click.option('--favorite-color',
              type=click.Choice(['red', 'green', 'blue']),
              prompt='Favorite color',
              help='Your favorite color')
@click.option('--subscribe', is_flag=True, help='Subscribe to newsletter')
@click.pass_obj
def profile(obj, name, age, favorite_color, subscribe):
    # Line 79: Display profile information
    click.echo("\nProfile Information:")
    click.echo(f"  Name: {name}")
    click.echo(f"  Age: {age}")
    click.echo(f"  Favorite Color: {favorite_color}")
    click.echo(f"  Newsletter: {'Subscribed' if subscribe else 'Not subscribed'}")
```

**Output:**
```
$ uv run main_click.py profile

Your name: John
Your age: 25
Favorite color (red, green, blue): blue

Profile Information:
  Name: John
  Age: 25
  Favorite Color: blue
  Newsletter: Not subscribed
```

The `prompt` parameter (lines 68-72) makes Click automatically prompt for input if not provided. The `click.Choice()` type (line 70) restricts input to predefined values.

---

### 4. File Handling with stdin/stdout (Lines 90-112)

```python
# Line 90: Command with file handling
@cli.command()
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'), required=False)
@click.option('--uppercase', is_flag=True, help='Convert to uppercase')
def process(input_file, output_file, uppercase):
    """Process a text file."""
    # Line 102: Read and process file content
    content = input_file.read()

    if uppercase:
        content = content.upper()

    # Line 108: Write to output (file or stdout)
    if output_file:
        output_file.write(content)
        click.echo(f"Processed content written to {output_file.name}", err=True)
    else:
        click.echo(content)
```

**Output (using stdin with '-'):**
```
$ echo "hello world" | uv run main_click.py process - --uppercase

HELLO WORLD
```

Click's `click.File()` type (lines 92-93) handles file opening/closing automatically and supports `-` for stdin/stdout, making it easy to build Unix-style pipeline tools.

---

### 5. Confirmation Prompts and Progress Bars (Lines 115-140)

```python
# Line 115: Command with confirmation prompt
@cli.command()
@click.argument('items', nargs=-1, required=True)
@click.option('--force', is_flag=True, help='Skip confirmation')
@click.pass_obj
def delete(obj, items, force):
    """Delete one or more items (with confirmation)."""
    # Line 124: Display items to be deleted
    click.echo(f"Items to delete: {', '.join(items)}")

    # Line 127: Confirmation prompt (unless --force is used)
    if not force:
        if not click.confirm('Are you sure you want to delete these items?'):
            click.echo('Deletion cancelled.')
            return

    # Line 133: Simulate deletion with progress
    with click.progressbar(items, label='Deleting items') as bar:
        for item in bar:
            # Simulate some work
            import time
            time.sleep(0.3)
```

**Output:**
```
$ uv run main_click.py delete file1.txt file2.txt

Items to delete: file1.txt, file2.txt
Are you sure you want to delete these items? [y/N]: n
Deletion cancelled.
```

The `nargs=-1` parameter (line 116) allows accepting multiple arguments, while `click.confirm()` (line 128) provides yes/no confirmation prompts. The `click.progressbar()` (line 133) creates visual progress indicators.

---

### 6. Nested Command Groups (Lines 160-203)

```python
# Line 160: Nested command group for database operations
@cli.group()
def database():
    """Database management commands."""
    pass

# Line 166: Subcommand under database group
@database.command()
@click.option('--host', default='localhost', help='Database host')
@click.option('--port', default=5432, type=int, help='Database port')
@click.option('--db-name', default='mydb', help='Database name')
def connect(host, port, db_name):
    """Connect to a database."""
    # Line 174: Display connection info
    click.echo("Connecting to database:")
    click.echo(f"  Host: {host}")
    click.echo(f"  Port: {port}")
    click.echo(f"  Database: {db_name}")
    click.secho("✓ Connected successfully!", fg='green')
```

**Output (help for database subcommands):**
```
$ uv run main_click.py database --help

Usage: main_click.py database [OPTIONS] COMMAND [ARGS]...

  Database management commands.

Options:
  --help  Show this message and exit.

Commands:
  connect  Connect to a database.
  query    Query a database table.
```

**Output (database connect):**
```
$ uv run main_click.py database connect --host db.example.com --port 3306

Connecting to database:
  Host: db.example.com
  Port: 3306
  Database: mydb
✓ Connected successfully!
```

Command groups can be nested (line 160) to create subcommands like `database connect` and `database query`, allowing for organized, hierarchical CLI structures.

---

### 7. Type Validation with Ranges (Lines 207-228)

```python
# Line 207: Command with custom validation
@cli.command()
@click.option('--port', type=click.IntRange(1, 65535), default=8080,
              help='Port number (1-65535)')
@click.option('--workers', type=click.IntRange(min=1), default=4,
              help='Number of workers (minimum 1)')
@click.option('--timeout', type=click.FloatRange(min=0.1), default=30.0,
              help='Timeout in seconds')
def serve(port, workers, timeout):
    """Start a web server with validation."""
    # Line 220: Display server configuration
    click.echo("Starting server with configuration:")
    click.echo(f"  Port: {port}")
    click.echo(f"  Workers: {workers}")
    click.echo(f"  Timeout: {timeout}s")
    click.secho("✓ Server started successfully!", fg='green')
```

**Output:**
```
$ uv run main_click.py serve --port 3000 --workers 8 --timeout 60

Starting server with configuration:
  Port: 3000
  Workers: 8
  Timeout: 60.0s
✓ Server started successfully!
```

Click provides `IntRange()` and `FloatRange()` types (lines 208-213) for automatic validation of numeric inputs, ensuring values fall within specified bounds.

---

### 8. Styled Terminal Output (Lines 230-251)

```python
# Line 230: Command demonstrating styled output
@cli.command()
def styles():
    """Demonstrate Click's styled output capabilities."""
    # Line 232: Various text styling options
    click.echo("\n=== Text Styling Examples ===\n")

    click.secho("This is red text", fg='red')
    click.secho("This is green text", fg='green')
    click.secho("This is blue text", fg='blue')
    click.secho("This is yellow text", fg='yellow')

    click.echo()
    click.secho("This is bold text", bold=True)
    click.secho("This is underlined text", underline=True)
    click.secho("This is bold + red text", fg='red', bold=True)

    click.echo()
    click.secho("✓ Success message", fg='green', bold=True)
    click.secho("⚠ Warning message", fg='yellow', bold=True)
    click.secho("✗ Error message", fg='red', bold=True)
    click.secho("ℹ Info message", fg='blue', bold=True)
```

**Output:**
```
$ uv run main_click.py styles

=== Text Styling Examples ===

This is red text         (displayed in red)
This is green text       (displayed in green)
This is blue text        (displayed in blue)
This is yellow text      (displayed in yellow)

This is bold text        (displayed in bold)
This is underlined text  (displayed underlined)
This is bold + red text  (displayed bold and red)

✓ Success message        (green and bold)
⚠ Warning message        (yellow and bold)
✗ Error message          (red and bold)
ℹ Info message           (blue and bold)
```

`click.secho()` (lines 236-250) provides easy text styling with colors and formatting, making CLI output more readable and user-friendly.

---

### 9. Multiple Value Options (Lines 253-270)

```python
# Line 253: Command with multiple value option
@cli.command()
@click.option('--tag', '-t', multiple=True, help='Add tags (can be used multiple times)')
@click.option('--exclude', multiple=True, help='Exclude patterns')
def search(tag, exclude):
    """Search with multiple tags and exclusions."""
    # Line 259: Display search criteria
    click.echo("Search criteria:")
    if tag:
        click.echo(f"  Tags: {', '.join(tag)}")
    else:
        click.echo("  Tags: (none)")

    if exclude:
        click.echo(f"  Exclude: {', '.join(exclude)}")
    else:
        click.echo("  Exclude: (none)")
```

**Output:**
```
$ uv run main_click.py search -t python -t cli --exclude test

Search criteria:
  Tags: python, cli
  Exclude: test
```

The `multiple=True` parameter (lines 254-255) allows options to be specified multiple times, collecting all values into a tuple.

---

## Running the Example

Execute the main script using uv:

```bash
uv run python/click/main_click.py --help
```

View help for any command:
```bash
uv run python/click/main_click.py greet --help
uv run python/click/main_click.py database --help
```

## Dependencies

This example requires:
- **click >= 8.1.0** - The Click library for creating CLI applications

Dependencies are specified using inline script metadata (PEP 723) at the top of the file and automatically managed by `uv run`.

## Key Takeaways

1. **Decorators**: Click uses decorators (`@click.command()`, `@click.option()`, `@click.argument()`) to transform regular Python functions into CLI commands
2. **Type Safety**: Built-in type conversion and validation (lines 208-213) prevent invalid inputs
3. **Composability**: Command groups (lines 30, 160) enable building complex, hierarchical CLI structures
4. **User Experience**: Interactive prompts (lines 68-72), confirmations (line 128), progress bars (line 133), and styled output (lines 236-250) create polished CLIs
5. **Context Sharing**: The context object (lines 22-26) enables sharing state between commands
6. **File Handling**: Automatic file handling (lines 92-93) with stdin/stdout support makes building pipeline tools simple

Click is the foundation for many popular Python CLI tools and provides a production-ready framework for building command-line applications.
