# Rich Library - Beautiful Command Line Interfaces

This example demonstrates the [Rich](https://github.com/Textualize/rich) Python library, which enables developers to create stunning, professional-looking command-line interfaces with minimal effort.

## Overview

Rich is a Python library for writing rich text (with color and style) to the terminal, and for displaying advanced content such as tables, markdown, and syntax-highlighted code.

## Running the Example

```bash
uv run --script main_rich_cli.py
```

## Source Code

### Dependencies and Setup (Lines 1-25)

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "rich>=13.0.0",
# ]
# ///

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
```

**Lines 2-7:** Inline script metadata using PEP 723 format, allowing `uv` to automatically manage dependencies.

**Lines 15-23:** Import various Rich components for different visualization types.

**Line 25:** Create the main Console object for rendering output.

---

### Feature 1: Basic Text Styling (Lines 28-37)

```python
def demo_basic_styling():
    """Demonstrate basic text styling and colors."""
    console.print("\n[bold cyan]1. Basic Text Styling[/bold cyan]", style="on black")
    console.print("[bold red]Bold Red Text[/bold red]")
    console.print("[italic green]Italic Green Text[/italic green]")
    console.print("[bold yellow on blue]Yellow on Blue Background[/bold yellow on blue]")
    console.print("[link=https://github.com/Textualize/rich]Clickable Link[/link]")
```

**Output:**
```
1. Basic Text Styling
Bold Red Text
Italic Green Text
Yellow on Blue Background
Clickable Link
```

**Lines 32-37:** Rich uses BBCode-style markup tags to apply styling:
- `[bold red]` creates bold red text
- `[italic green]` creates italic green text
- `[bold yellow on blue]` applies yellow text on blue background
- `[link=URL]` creates clickable hyperlinks in supported terminals

---

### Feature 2: Rich Tables (Lines 40-61)

```python
def demo_tables():
    """Demonstrate rich tables with styling."""
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
```

**Output:**
```
             Python Web Frameworks
╭───────────┬────────────┬─────────────┬───────╮
│ Framework │ Type       │ Performance │ Async │
├───────────┼────────────┼─────────────┼───────┤
│ FastAPI   │ Modern     │  ⭐⭐⭐⭐⭐ │  ✅   │
│ Flask     │ Micro      │    ⭐⭐⭐⭐ │  ❌   │
│ Django    │ Full-Stack │      ⭐⭐⭐ │  ✅   │
│ Tornado   │ Async      │    ⭐⭐⭐⭐ │  ✅   │
╰───────────┴────────────┴─────────────┴───────╯
```

**Lines 45-50:** Create a Table with title, rounded box style, and magenta headers.

**Lines 51-54:** Define columns with individual styling and text alignment (left, right, center).

**Lines 56-59:** Add data rows with emoji and Unicode symbols for visual appeal.

**Line 61:** Render the fully-styled table to the console.

---

### Feature 3: Progress Bars (Lines 64-84)

```python
def demo_progress_bars():
    """Demonstrate progress bars and spinners."""
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
```

**Output:**
```
  Downloading... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%
  Processing...  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%
  Uploading...   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%
```

**Lines 69-74:** Configure Progress display with custom columns: spinner, description, bar, and percentage.

**Lines 76-78:** Create three simultaneous progress tasks with different colors.

**Lines 80-84:** Update tasks at different rates, demonstrating concurrent progress tracking.

---

### Feature 4: Panels and Borders (Lines 87-108)

```python
def demo_panels():
    """Demonstrate panels and borders."""
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
```

**Output:**
```
╭──────────────────────────────── Basic Panel ─────────────────────────────────╮
│ This is a simple panel                                                       │
╰──────────────────────────────────────────────────────────────────────────────╯
╔══════════ ❌ Error Message ══════════╗
║ Error: File not found!               ║
║ Please check the path and try again. ║
╚══════════════════════════════════════╝
```

**Lines 92-98:** Create a basic panel with green border and styled content.

**Lines 100-108:** Use `Panel.fit()` for auto-sizing and double-line box style, perfect for error messages.

---

### Feature 5: Syntax Highlighting (Lines 111-128)

```python
def demo_syntax_highlighting():
    """Demonstrate syntax highlighting for code."""
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
```

**Output:**
```
╭──────────────────────────────── Python Code ─────────────────────────────────╮
│    1                                                                         │
│    2 def fibonacci(n):                                                       │
│    3     """Calculate nth Fibonacci number."""                               │
│    4     if n <= 1:                                                          │
│    5         return n                                                        │
│    6     return fibonacci(n-1) + fibonacci(n-2)                              │
│    7                                                                         │
│    8 result = fibonacci(10)                                                  │
│    9 print(f"Fibonacci(10) = {result}")                                      │
│   10                                                                         │
╰──────────────────────────────────────────────────────────────────────────────╯
```

**Line 127:** Create Syntax object with language detection, theme selection, and line numbers.

**Line 128:** Wrap syntax-highlighted code in a panel for clean presentation.

**Rich supports dozens of languages** including Python, JavaScript, Java, Rust, Go, SQL, and more.

---

### Feature 6: Tree Structures (Lines 131-148)

```python
def demo_tree_structure():
    """Demonstrate tree structures."""
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
```

**Output:**
```
📁 Project Root
├── 📁 src
│   ├── 📄 main.py
│   └── 📄 utils.py
├── 📁 tests
│   └── 📄 test_main.py
├── 📄 README.md
└── 📄 requirements.txt
```

**Line 136:** Create root Tree node with emoji and styling.

**Lines 138-146:** Build hierarchical structure by adding child nodes.

**Perfect for displaying:** Directory structures, JSON data, organizational charts, dependency trees.

---

### Feature 7: Markdown Rendering (Lines 151-167)

```python
def demo_markdown():
    """Demonstrate markdown rendering."""
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
```

**Output:**
```
╭──────────────────────────────────────────────────────────────────────────────╮
│ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ │
│ ┃                          Rich Library Features                           ┃ │
│ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ │
│                                                                              │
│                                                                              │
│                               Key Capabilities                               │
│                                                                              │
│  • Beautiful Text: Rich markup and styling                                   │
│  • Tables: Professional data presentation                                    │
│  • Progress: Visual feedback for operations                                  │
│  • Syntax: Code highlighting support                                         │
╰──────────────────────────────────────────────────────────────────────────────╯
```

**Line 166:** Parse markdown string into Rich-renderable format.

**Line 167:** Display formatted markdown with all styling preserved.

**Supported markdown features:** Headers, lists, bold, italic, code blocks, links, and more.

---

### Feature 8: Advanced Text Manipulation (Lines 170-187)

```python
def demo_advanced_text():
    """Demonstrate advanced text manipulation."""
    console.print("\n[bold cyan]8. Advanced Text Features[/bold cyan]", style="on black")

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
```

**Output:**
```
╭──────────────────────────────────────────────────────────────────────────────╮
│ Rainbow Colors! 🌈                                                           │
╰──────────────────────────────────────────────────────────────────────────────╯
```

**Lines 177-185:** Build Text object programmatically, applying different styles to individual characters.

**Programmatic styling allows:** Dynamic text generation, per-character control, conditional formatting.

---

## Key Features Demonstrated

1. **Text Styling** (Lines 28-37): BBCode-style markup for colors, styles, and links
2. **Tables** (Lines 40-61): Professional data presentation with borders and alignment
3. **Progress Bars** (Lines 64-84): Visual feedback for long-running operations
4. **Panels** (Lines 87-108): Bordered containers for content organization
5. **Syntax Highlighting** (Lines 111-128): Code display with themes and line numbers
6. **Tree Structures** (Lines 131-148): Hierarchical data visualization
7. **Markdown Rendering** (Lines 151-167): Convert markdown to styled terminal output
8. **Advanced Text** (Lines 170-187): Programmatic text construction with granular styling

## Requirements

- Python 3.10 or higher
- Rich library version 13.0.0 or higher (automatically installed by `uv`)

## Benefits of Rich

- **Zero Configuration**: Works out of the box with sensible defaults
- **Unicode Support**: Full emoji and special character support
- **Terminal Detection**: Automatically adapts to terminal capabilities
- **Performance**: Optimized rendering engine
- **Extensible**: Create custom renderables and themes
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Use Cases

- **CLI Applications**: Make command-line tools more user-friendly
- **Log Viewers**: Colorize and structure log output
- **Development Tools**: Build better debugging and monitoring tools
- **Data Visualization**: Display complex data structures clearly
- **Installation Wizards**: Create interactive setup experiences

## Additional Resources

- [Rich Documentation](https://rich.readthedocs.io/)
- [GitHub Repository](https://github.com/Textualize/rich)
- [Rich Examples Gallery](https://github.com/Textualize/rich/tree/master/examples)
