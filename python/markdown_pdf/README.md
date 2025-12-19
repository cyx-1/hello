# Markdown to PDF Generation using Python

This example demonstrates how to convert Markdown content to PDF using Python's `markdown` and `weasyprint` libraries.

## Overview

The script performs a three-step conversion process:
1. **Markdown → HTML**: Convert Markdown to HTML using the `markdown` library
2. **HTML → Styled HTML**: Apply CSS styling for professional PDF output
3. **Styled HTML → PDF**: Convert HTML to PDF using the `weasyprint` library

## Running the Code

```bash
uv run main_markdown_pdf.py
```

**Note**: This script uses inline script metadata (PEP 723) to specify dependencies. The `uv` tool automatically installs required packages (`markdown>=3.5` and `weasyprint>=60.0`) when running the script.

## Dependencies

As specified in the inline script metadata (lines 2-8):
- **Python**: >= 3.10
- **markdown**: >= 3.5 (converts Markdown to HTML)
- **weasyprint**: >= 60.0 (converts HTML to PDF)

## Source Code Structure

### 1. Inline Dependencies Declaration (Lines 2-8)

```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "markdown>=3.5",
#     "weasyprint>=60.0",
# ]
# ///
```

**Purpose**: Declares dependencies using PEP 723 inline script metadata, allowing `uv` to automatically manage dependencies without a `pyproject.toml` file.

### 2. Imports (Lines 17-19)

```python
import markdown
from weasyprint import HTML, CSS
from pathlib import Path
```

- **Line 17**: Import `markdown` for Markdown to HTML conversion
- **Line 18**: Import `HTML` and `CSS` from `weasyprint` for PDF generation
- **Line 19**: Import `Path` for file path handling

### 3. Creating Sample Markdown Content (Lines 22-64)

```python
def create_sample_markdown() -> str:
    """Create sample Markdown content for demonstration."""
    return """# Markdown to PDF Generation

## Introduction

This document demonstrates **Markdown to PDF** conversion using Python.

### Features

- **Bold text** and *italic text*
- Bullet points and numbered lists
- Code blocks and inline code
- Tables and links
...
"""
```

**Purpose**: Generates sample Markdown content with various formatting elements (headers, lists, tables, code blocks, links) to demonstrate the conversion capabilities.

### 4. Converting Markdown to HTML (Lines 67-95)

```python
def markdown_to_html(markdown_content: str) -> str:
    # Line 78: Convert markdown to HTML using extensions for better formatting
    md = markdown.Markdown(extensions=["extra", "codehilite", "tables"])
    html_body = md.convert(markdown_content)

    # Line 82: Wrap in proper HTML structure
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Markdown to PDF</title>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    return html_template
```

**Key Points**:
- **Line 78**: Creates a `Markdown` instance with extensions:
  - `extra`: Enables extra features (fenced code blocks, tables, etc.)
  - `codehilite`: Syntax highlighting for code blocks
  - `tables`: Table support
- **Line 79**: Converts Markdown text to HTML body
- **Lines 82-93**: Wraps the HTML body in a complete HTML document structure

### 5. Converting HTML to PDF with Styling (Lines 98-177)

```python
def html_to_pdf(html_content: str, output_path: str) -> None:
    # Line 107: Define CSS styles for the PDF
    css_style = CSS(
        string="""
        @page {
            size: A4;
            margin: 2cm;
        }
        body {
            font-family: Arial, sans-serif;
            font-size: 12pt;
            line-height: 1.6;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
        ...
        """
    )

    # Line 177: Convert HTML to PDF with styling
    HTML(string=html_content).write_pdf(output_path, stylesheets=[css_style])
```

**Key Points**:
- **Lines 107-174**: Define comprehensive CSS styling:
  - **Lines 109-112**: Page setup (A4 size, 2cm margins)
  - **Lines 113-118**: Body text styling
  - **Lines 119-133**: Header styles (h1, h2, h3) with colors and borders
  - **Lines 134-146**: Code and pre-formatted text styling
  - **Lines 147-163**: Table styling with alternating row colors
  - **Lines 164-172**: Link and horizontal rule styling
- **Line 177**: Converts HTML to PDF using WeasyPrint with applied styles

### 6. Main Function - Orchestrating the Conversion (Lines 180-228)

```python
def main():
    # Line 188: Create sample Markdown content
    markdown_content = create_sample_markdown()

    # Line 199: Convert Markdown to HTML
    html_content = markdown_to_html(markdown_content)

    # Line 203: Save HTML for inspection
    html_output = Path("output.html")
    html_output.write_text(html_content, encoding="utf-8")

    # Line 210: Convert HTML to PDF
    pdf_output = Path("output.pdf")
    html_to_pdf(html_content, str(pdf_output))

    # Line 215: Display file information
    file_size = pdf_output.stat().st_size
    print(f"✓ PDF file size: {file_size:,} bytes ({file_size / 1024:.2f} KB)")
```

**Workflow**:
1. **Line 188**: Creates sample Markdown content
2. **Line 199**: Converts Markdown to HTML
3. **Lines 203-205**: Saves HTML to `output.html` for inspection
4. **Lines 209-211**: Converts HTML to PDF and saves as `output.pdf`
5. **Lines 214-216**: Displays file size information

## Program Output

When you run the script, you'll see the following output:

```
============================================================
Markdown to PDF Generation Example
============================================================

[Step 1] Creating sample Markdown content...
✓ Created 735 characters of Markdown

[Step 2] Markdown Preview (first 200 chars):
------------------------------------------------------------
# Markdown to PDF Generation

## Introduction

This document demonstrates **Markdown to PDF** conversion using Python.

### Features

- **Bold text** and *italic text*
- Bullet points and numbered lis...
------------------------------------------------------------

[Step 3] Converting Markdown to HTML...
✓ Generated HTML with 1211 characters
✓ Saved HTML to: /home/user/hello/python/markdown_pdf/output.html

[Step 4] Converting HTML to PDF...
✓ Generated PDF: /home/user/hello/python/markdown_pdf/output.pdf
✓ PDF file size: 16,148 bytes (15.77 KB)

============================================================
Conversion completed successfully!
============================================================

Generated files:
  - HTML: /home/user/hello/python/markdown_pdf/output.html
  - PDF:  /home/user/hello/python/markdown_pdf/output.pdf
```

## Output Files

The script generates two files:

1. **output.html**: Intermediate HTML file with the converted Markdown content
2. **output.pdf**: Final PDF file with professional styling

## Code-to-Output Correlation

| Source Code Line | Output Line | Description |
|-----------------|-------------|-------------|
| Line 188 | "[Step 1] Creating sample..." | Creates 735 characters of Markdown content |
| Line 189 | "✓ Created 735 characters..." | Reports Markdown content size |
| Line 194 | "# Markdown to PDF Generation..." | Displays preview of Markdown content |
| Line 199 | "[Step 3] Converting..." | Initiates Markdown to HTML conversion |
| Line 200 | "✓ Generated HTML with 1211..." | Reports HTML size (1211 characters) |
| Line 204 | "✓ Saved HTML to: ..." | Confirms HTML file saved to disk |
| Line 210 | "[Step 4] Converting..." | Initiates HTML to PDF conversion |
| Line 211 | "✓ Generated PDF: ..." | Confirms PDF file created |
| Line 216 | "✓ PDF file size: 16,148 bytes..." | Reports final PDF size (15.77 KB) |

## Key Features Demonstrated

1. **PEP 723 Inline Dependencies**: Modern dependency management without `pyproject.toml`
2. **Markdown Extensions**: Enhanced formatting with `extra`, `codehilite`, and `tables`
3. **CSS Styling**: Professional PDF output with custom fonts, colors, and layout
4. **Type Hints**: Modern Python with type annotations for better code quality
5. **Path Handling**: Uses `pathlib.Path` for cross-platform file operations
6. **Progress Reporting**: Clear console output showing conversion steps

## Version Requirements

**Important**: This code requires:
- **Python 3.10 or higher** (for modern type hints and syntax)
- **markdown 3.5 or higher** (for the latest Markdown features)
- **weasyprint 60.0 or higher** (for improved PDF rendering)

The `weasyprint` library may also require system-level dependencies:
- **Linux**: `libpango-1.0-0`, `libpangocairo-1.0-0`, `libgdk-pixbuf2.0-0`
- **macOS**: `cairo`, `pango`, `gdk-pixbuf` (via Homebrew)
- **Windows**: Usually works out of the box with the Python package

## Customization Options

You can customize the PDF output by modifying:

1. **Page Layout** (Lines 109-112): Change page size, margins, orientation
2. **Typography** (Lines 113-118): Adjust fonts, sizes, line height
3. **Colors** (Lines 119-172): Modify color scheme for headers, links, tables
4. **Markdown Content** (Lines 22-64): Change the content to convert

## Alternative Approaches

Other Python libraries for Markdown to PDF conversion include:
- **pdfkit**: Requires external `wkhtmltopdf` binary (not pure Python)
- **reportlab** + **markdown**: More low-level control but more complex
- **pypandoc**: Requires external `pandoc` installation

This example uses **markdown + weasyprint** because it's a pure Python solution that doesn't require external binaries, making it easier to deploy and use.
