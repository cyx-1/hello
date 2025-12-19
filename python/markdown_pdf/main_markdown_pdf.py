#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "markdown>=3.5",
#     "weasyprint>=60.0",
# ]
# ///

"""
Markdown to PDF Generation Example

This script demonstrates how to convert Markdown content to PDF using
the markdown and weasyprint libraries.
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path


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

### Code Example

```python
def hello_world():
    print("Hello, World!")
```

### Table Example

| Library    | Purpose           | Version |
|-----------|-------------------|---------|
| markdown  | MD to HTML        | 3.5+    |
| weasyprint| HTML to PDF       | 60.0+   |

### Numbered List

1. First item
2. Second item
3. Third item

### Links

Visit [Python.org](https://www.python.org) for more information.

---

**Generated using Python markdown and weasyprint libraries**
"""


def markdown_to_html(markdown_content: str) -> str:
    """
    Convert Markdown content to HTML.

    Args:
        markdown_content: The Markdown text to convert

    Returns:
        HTML string with proper structure
    """
    # Line 70: Convert markdown to HTML using extensions for better formatting
    md = markdown.Markdown(extensions=["extra", "codehilite", "tables"])
    html_body = md.convert(markdown_content)

    # Line 74: Wrap in proper HTML structure
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


def html_to_pdf(html_content: str, output_path: str) -> None:
    """
    Convert HTML content to PDF.

    Args:
        html_content: The HTML string to convert
        output_path: Path where the PDF should be saved
    """
    # Line 100: Define CSS styles for the PDF
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
        h2 {
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 8px;
            margin-top: 20px;
        }
        h3 {
            color: #7f8c8d;
            margin-top: 15px;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #3498db;
            overflow-x: auto;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #3498db;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        hr {
            border: none;
            border-top: 2px solid #bdc3c7;
            margin: 30px 0;
        }
    """
    )

    # Line 169: Convert HTML to PDF with styling
    HTML(string=html_content).write_pdf(output_path, stylesheets=[css_style])


def main():
    """Main function to demonstrate Markdown to PDF conversion."""
    print("=" * 60)
    print("Markdown to PDF Generation Example")
    print("=" * 60)

    # Line 179: Create sample Markdown content
    print("\n[Step 1] Creating sample Markdown content...")
    markdown_content = create_sample_markdown()
    print(f"✓ Created {len(markdown_content)} characters of Markdown")

    # Line 184: Preview first few lines
    print("\n[Step 2] Markdown Preview (first 200 chars):")
    print("-" * 60)
    print(markdown_content[:200] + "...")
    print("-" * 60)

    # Line 190: Convert Markdown to HTML
    print("\n[Step 3] Converting Markdown to HTML...")
    html_content = markdown_to_html(markdown_content)
    print(f"✓ Generated HTML with {len(html_content)} characters")

    # Line 195: Save HTML for inspection
    html_output = Path("output.html")
    html_output.write_text(html_content, encoding="utf-8")
    print(f"✓ Saved HTML to: {html_output.absolute()}")

    # Line 200: Convert HTML to PDF
    print("\n[Step 4] Converting HTML to PDF...")
    pdf_output = Path("output.pdf")
    html_to_pdf(html_content, str(pdf_output))
    print(f"✓ Generated PDF: {pdf_output.absolute()}")

    # Line 206: Display file information
    if pdf_output.exists():
        file_size = pdf_output.stat().st_size
        print(f"✓ PDF file size: {file_size:,} bytes ({file_size / 1024:.2f} KB)")

    print("\n" + "=" * 60)
    print("Conversion completed successfully!")
    print("=" * 60)

    print("\nGenerated files:")
    print(f"  - HTML: {html_output.absolute()}")
    print(f"  - PDF:  {pdf_output.absolute()}")


if __name__ == "__main__":
    main()
