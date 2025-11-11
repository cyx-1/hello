#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "rich>=13.0.0",
# ]
# ///

"""
Demonstration of the Rich Python library for creating beautiful CLI interfaces.
Showcases various features including text styling, tables, progress bars, panels, and more.
"""

import time
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.panel import Panel
from rich.syntax import Syntax
from rich.tree import Tree
from rich.markdown import Markdown
from rich import box
from rich.text import Text

console = Console()


def demo_basic_styling():
    """Demonstrate basic text styling and colors."""
    # Line 31-35: Basic rich text with markup
    console.print("\n[bold cyan]1. Basic Text Styling[/bold cyan]", style="on black")
    console.print("[bold red]Bold Red Text[/bold red]")
    console.print("[italic green]Italic Green Text[/italic green]")
    console.print(
        "[bold yellow on blue]Yellow on Blue Background[/bold yellow on blue]"
    )
    console.print("[link=https://github.com/Textualize/rich]Clickable Link[/link]")


def demo_tables():
    """Demonstrate rich tables with styling."""
    # Line 41-58: Creating a styled table
    console.print("\n[bold cyan]2. Rich Tables[/bold cyan]", style="on black")

    table = Table(
        title="Python Web Frameworks",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
    )
    table.add_column("Framework", style="cyan", justify="left")
    table.add_column("Type", style="green")
    table.add_column("Performance", justify="right", style="yellow")
    table.add_column("Async", justify="center")

    table.add_row("FastAPI", "Modern", "⭐⭐⭐⭐⭐", "✅")
    table.add_row("Flask", "Micro", "⭐⭐⭐⭐", "❌")
    table.add_row("Django", "Full-Stack", "⭐⭐⭐", "✅")
    table.add_row("Tornado", "Async", "⭐⭐⭐⭐", "✅")

    console.print(table)


def demo_progress_bars():
    """Demonstrate progress bars and spinners."""
    # Line 64-73: Progress bars with custom columns
    console.print("\n[bold cyan]3. Progress Bars[/bold cyan]", style="on black")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task1 = progress.add_task("[red]Downloading...", total=100)
        task2 = progress.add_task("[green]Processing...", total=100)
        task3 = progress.add_task("[cyan]Uploading...", total=100)

        while not progress.finished:
            progress.update(task1, advance=2.5)
            progress.update(task2, advance=1.5)
            progress.update(task3, advance=1.0)
            time.sleep(0.02)


def demo_panels():
    """Demonstrate panels and borders."""
    # Line 86-94: Creating styled panels
    console.print("\n[bold cyan]4. Panels and Borders[/bold cyan]", style="on black")

    console.print(
        Panel(
            "This is a [bold yellow]simple panel[/bold yellow]",
            title="Basic Panel",
            border_style="green",
        )
    )

    console.print(
        Panel.fit(
            "[bold red]Error:[/bold red] File not found!\n"
            "Please check the path and try again.",
            title="❌ Error Message",
            border_style="red",
            box=box.DOUBLE,
        )
    )


def demo_syntax_highlighting():
    """Demonstrate syntax highlighting for code."""
    # Line 100-115: Syntax highlighting for various languages
    console.print("\n[bold cyan]5. Syntax Highlighting[/bold cyan]", style="on black")

    python_code = '''
def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
print(f"Fibonacci(10) = {result}")
'''

    syntax = Syntax(python_code, "python", theme="monokai", line_numbers=True)
    console.print(Panel(syntax, title="Python Code", border_style="blue"))


def demo_tree_structure():
    """Demonstrate tree structures."""
    # Line 121-133: Creating hierarchical tree structures
    console.print("\n[bold cyan]6. Tree Structures[/bold cyan]", style="on black")

    tree = Tree("📁 [bold blue]Project Root", guide_style="bright_blue")

    src = tree.add("📁 [yellow]src")
    src.add("📄 main.py")
    src.add("📄 utils.py")

    tests = tree.add("📁 [yellow]tests")
    tests.add("📄 test_main.py")

    tree.add("📄 [green]README.md")
    tree.add("📄 requirements.txt")

    console.print(tree)


def demo_markdown():
    """Demonstrate markdown rendering."""
    # Line 141-151: Rendering markdown content
    console.print("\n[bold cyan]7. Markdown Rendering[/bold cyan]", style="on black")

    markdown_text = """
# Rich Library Features

## Key Capabilities
- **Beautiful Text**: Rich markup and styling
- **Tables**: Professional data presentation
- **Progress**: Visual feedback for operations
- *Syntax*: Code highlighting support
"""

    md = Markdown(markdown_text)
    console.print(Panel(md, border_style="magenta"))


def demo_advanced_text():
    """Demonstrate advanced text manipulation."""
    # Line 157-168: Advanced text features
    console.print(
        "\n[bold cyan]8. Advanced Text Features[/bold cyan]", style="on black"
    )

    text = Text()
    text.append("Rainbow ", style="bold")
    text.append("C", style="bold red")
    text.append("o", style="bold yellow")
    text.append("l", style="bold green")
    text.append("o", style="bold cyan")
    text.append("r", style="bold blue")
    text.append("s", style="bold magenta")
    text.append("! 🌈", style="bold")

    console.print(Panel(text, border_style="white"))


def main():
    """Run all demonstrations."""
    console.clear()

    # Line 178: Main header
    console.print(
        Panel.fit(
            "[bold white]Rich Library CLI Demonstration[/bold white]\n"
            "[italic]Creating Beautiful Command Line Interfaces with Python[/italic]",
            border_style="bright_blue",
            box=box.DOUBLE,
        )
    )

    # Run all demos
    demo_basic_styling()
    demo_tables()
    demo_progress_bars()
    demo_panels()
    demo_syntax_highlighting()
    demo_tree_structure()
    demo_markdown()
    demo_advanced_text()

    # Line 196: Footer
    console.print("\n" + "=" * 70)
    console.print("[bold green]✅ Demonstration Complete![/bold green]")
    console.print("[dim]Rich makes CLI applications beautiful and user-friendly.[/dim]")
    console.print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
