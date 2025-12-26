#!/usr/bin/env python3
# /// script
# dependencies = [
#   "click>=8.1.0",
# ]
# ///
"""Comprehensive demonstration of Click - a Python package for creating CLI tools.

This example showcases:
- Basic commands and command groups
- Options, arguments, and flags
- Different parameter types
- Prompts and confirmations
- File handling
- Context passing between commands
- Custom validation
"""

import click


# Line 24: Context object for sharing data between commands
class AppContext:
    """Custom context object to share data between commands."""

    def __init__(self):
        self.verbose = False
        self.config_file = None


# Line 32: Main command group - entry point for CLI
@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--config", type=click.Path(), help="Path to config file")
@click.pass_context
def cli(ctx, verbose, config):
    """A comprehensive CLI tool built with Click.

    This demonstrates various Click features including commands,
    options, arguments, and more.
    """
    # Line 43: Store context for use in subcommands
    ctx.obj = AppContext()
    ctx.obj.verbose = verbose
    ctx.obj.config_file = config

    if verbose:
        click.echo("Verbose mode enabled")
        if config:
            click.echo(f"Using config file: {config}")


# Line 53: Simple command with arguments
@cli.command()
@click.argument("name")
@click.argument("count", type=int, default=1)
def greet(name, count):
    """Greet someone COUNT times.

    NAME is the person to greet (required)
    COUNT is the number of times to greet (default: 1)
    """
    # Line 63: Loop to greet multiple times
    for i in range(count):
        click.echo(f"Hello, {name}! (greeting {i + 1}/{count})")


# Line 68: Command with various option types
@cli.command()
@click.option("--name", prompt="Your name", help="The person to greet")
@click.option("--age", type=int, prompt="Your age", help="Your age")
@click.option(
    "--favorite-color",
    type=click.Choice(["red", "green", "blue"]),
    prompt="Favorite color",
    help="Your favorite color",
)
@click.option("--subscribe", is_flag=True, help="Subscribe to newsletter")
@click.pass_obj
def profile(obj, name, age, favorite_color, subscribe):
    """Create a user profile with interactive prompts."""
    # Line 81: Display profile information
    if obj.verbose:
        click.echo("=== Creating User Profile ===")

    click.echo("\nProfile Information:")
    click.echo(f"  Name: {name}")
    click.echo(f"  Age: {age}")
    click.echo(f"  Favorite Color: {favorite_color}")
    click.echo(f"  Newsletter: {'Subscribed' if subscribe else 'Not subscribed'}")


# Line 92: Command with file handling
@cli.command()
@click.argument("input_file", type=click.File("r"))
@click.argument("output_file", type=click.File("w"), required=False)
@click.option("--uppercase", is_flag=True, help="Convert to uppercase")
def process(input_file, output_file, uppercase):
    """Process a text file.

    INPUT_FILE: File to read from (use '-' for stdin)
    OUTPUT_FILE: File to write to (optional, defaults to stdout)
    """
    # Line 104: Read and process file content
    content = input_file.read()

    if uppercase:
        content = content.upper()

    # Line 110: Write to output (file or stdout)
    if output_file:
        output_file.write(content)
        click.echo(f"Processed content written to {output_file.name}", err=True)
    else:
        click.echo(content)


# Line 117: Command with confirmation prompt
@cli.command()
@click.argument("items", nargs=-1, required=True)
@click.option("--force", is_flag=True, help="Skip confirmation")
@click.pass_obj
def delete(obj, items, force):
    """Delete one or more items (with confirmation).

    ITEMS: One or more items to delete
    """
    # Line 126: Display items to be deleted
    click.echo(f"Items to delete: {', '.join(items)}")

    # Line 129: Confirmation prompt (unless --force is used)
    if not force:
        if not click.confirm("Are you sure you want to delete these items?"):
            click.echo("Deletion cancelled.")
            return

    # Line 135: Simulate deletion with progress
    with click.progressbar(items, label="Deleting items") as bar:
        for item in bar:
            # Simulate some work
            import time

            time.sleep(0.3)

    click.secho("✓ All items deleted successfully!", fg="green", bold=True)


# Line 144: Command with password prompt
@cli.command()
@click.option("--username", prompt=True, help="Username")
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    help="Password",
)
def login(username, password):
    """Login with username and password.

    Demonstrates secure password input (hidden and confirmed).
    """
    # Line 153: Simulate login
    click.echo(f"\nAttempting login for user: {username}")
    click.echo(f"Password length: {len(password)} characters")

    if len(password) >= 8:
        click.secho("✓ Login successful!", fg="green")
    else:
        click.secho("✗ Password too short (minimum 8 characters)", fg="red")


# Line 162: Nested command group for database operations
@cli.group()
def database():
    """Database management commands."""
    pass


# Line 168: Subcommand under database group
@database.command()
@click.option("--host", default="localhost", help="Database host")
@click.option("--port", default=5432, type=int, help="Database port")
@click.option("--db-name", default="mydb", help="Database name")
def connect(host, port, db_name):
    """Connect to a database."""
    # Line 176: Display connection info
    click.echo("Connecting to database:")
    click.echo(f"  Host: {host}")
    click.echo(f"  Port: {port}")
    click.echo(f"  Database: {db_name}")
    click.secho("✓ Connected successfully!", fg="green")


# Line 184: Another database subcommand
@database.command()
@click.option("--table", required=True, help="Table name")
@click.option(
    "--format",
    type=click.Choice(["json", "csv", "table"]),
    default="table",
    help="Output format",
)
def query(table, format):
    """Query a database table."""
    # Line 191: Simulate query results
    click.echo(f"Querying table: {table}")
    click.echo(f"Output format: {format}")

    # Line 195: Sample data output
    if format == "table":
        click.echo("\n┌────┬──────────┬─────┐")
        click.echo("│ ID │ Name     │ Age │")
        click.echo("├────┼──────────┼─────┤")
        click.echo("│ 1  │ Alice    │ 30  │")
        click.echo("│ 2  │ Bob      │ 25  │")
        click.echo("└────┴──────────┴─────┘")
    elif format == "json":
        click.echo(
            '[{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]'
        )
    else:
        click.echo("id,name,age\n1,Alice,30\n2,Bob,25")


# Line 209: Command with custom validation
@cli.command()
@click.option(
    "--port", type=click.IntRange(1, 65535), default=8080, help="Port number (1-65535)"
)
@click.option(
    "--workers",
    type=click.IntRange(min=1),
    default=4,
    help="Number of workers (minimum 1)",
)
@click.option(
    "--timeout", type=click.FloatRange(min=0.1), default=30.0, help="Timeout in seconds"
)
def serve(port, workers, timeout):
    """Start a web server with validation.

    Demonstrates range validation for different numeric types.
    """
    # Line 222: Display server configuration
    click.echo("Starting server with configuration:")
    click.echo(f"  Port: {port}")
    click.echo(f"  Workers: {workers}")
    click.echo(f"  Timeout: {timeout}s")
    click.secho("✓ Server started successfully!", fg="green")


# Line 230: Command demonstrating styled output
@cli.command()
def styles():
    """Demonstrate Click's styled output capabilities."""
    # Line 234: Various text styling options
    click.echo("\n=== Text Styling Examples ===\n")

    click.secho("This is red text", fg="red")
    click.secho("This is green text", fg="green")
    click.secho("This is blue text", fg="blue")
    click.secho("This is yellow text", fg="yellow")

    click.echo()
    click.secho("This is bold text", bold=True)
    click.secho("This is underlined text", underline=True)
    click.secho("This is bold + red text", fg="red", bold=True)

    click.echo()
    click.secho("✓ Success message", fg="green", bold=True)
    click.secho("⚠ Warning message", fg="yellow", bold=True)
    click.secho("✗ Error message", fg="red", bold=True)
    click.secho("ℹ Info message", fg="blue", bold=True)


# Line 253: Command with multiple value option
@cli.command()
@click.option(
    "--tag", "-t", multiple=True, help="Add tags (can be used multiple times)"
)
@click.option("--exclude", multiple=True, help="Exclude patterns")
def search(tag, exclude):
    """Search with multiple tags and exclusions.

    Demonstrates options that can be specified multiple times.
    """
    # Line 261: Display search criteria
    click.echo("Search criteria:")
    if tag:
        click.echo(f"  Tags: {', '.join(tag)}")
    else:
        click.echo("  Tags: (none)")

    if exclude:
        click.echo(f"  Exclude: {', '.join(exclude)}")
    else:
        click.echo("  Exclude: (none)")


# Line 273: Entry point for the CLI
if __name__ == "__main__":
    # Line 275: Run the CLI
    cli()
