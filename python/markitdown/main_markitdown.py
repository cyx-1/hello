#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "markitdown>=0.0.1",
# ]
# ///

"""
Microsoft MarkItDown Python Example

MarkItDown is a utility for converting various files and office documents to Markdown.
This example demonstrates key features:
1. Converting HTML content to Markdown
2. Converting text content to Markdown
3. Preserving document structure (headings, lists, tables, links)
4. Working with in-memory content
5. Demonstrating different content types

Requirements: Python 3.10 or higher
"""

from markitdown import MarkItDown
import tempfile
import os


def print_section(title: str):
    """Helper function to print section headers."""
    print("\n" + "=" * 70)
    print(f"{title}")
    print("=" * 70)


def example1_html_to_markdown():
    """
    Example 1: Convert HTML content to Markdown
    Demonstrates basic HTML to Markdown conversion.
    """
    print_section("EXAMPLE 1: HTML to Markdown Conversion")

    # Line 45: Initialize MarkItDown converter
    md = MarkItDown()

    # Line 48: Sample HTML with various elements
    html_content = """
    <!DOCTYPE html>
    <html>
    <head><title>Sample Document</title></head>
    <body>
        <h1>Welcome to MarkItDown</h1>
        <p>This is a <strong>powerful</strong> tool for converting documents to Markdown.</p>

        <h2>Key Features</h2>
        <ul>
            <li>Converts HTML to Markdown</li>
            <li>Preserves document structure</li>
            <li>Handles multiple formats</li>
        </ul>

        <h2>Why Use MarkItDown?</h2>
        <p>MarkItDown makes it easy to prepare documents for LLMs and text analysis.</p>

        <p>Visit <a href="https://github.com/microsoft/markitdown">GitHub</a> for more info.</p>
    </body>
    </html>
    """

    # Line 72: Create a temporary HTML file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as tmp:
        tmp.write(html_content)
        tmp_path = tmp.name

    try:
        # Line 78: Convert HTML file to Markdown
        result = md.convert(tmp_path)

        print("\n[INPUT] HTML Content:")
        print("-" * 70)
        print(html_content[:300] + "...")

        print("\n[OUTPUT] Converted Markdown:")
        print("-" * 70)
        # Line 87: Access the converted markdown text
        print(result.text_content)
    finally:
        # Line 90: Clean up temporary file
        os.unlink(tmp_path)


def example2_complex_html_with_table():
    """
    Example 2: Convert HTML with tables and formatting
    Demonstrates table conversion and complex structure preservation.
    """
    print_section("EXAMPLE 2: HTML with Tables and Advanced Formatting")

    md = MarkItDown()

    # Line 104: HTML with table, code, and nested lists
    html_with_table = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Product Comparison</h1>

        <table border="1">
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Rating</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Product A</td>
                    <td>$99.99</td>
                    <td>⭐⭐⭐⭐⭐</td>
                </tr>
                <tr>
                    <td>Product B</td>
                    <td>$149.99</td>
                    <td>⭐⭐⭐⭐</td>
                </tr>
                <tr>
                    <td>Product C</td>
                    <td>$79.99</td>
                    <td>⭐⭐⭐⭐⭐</td>
                </tr>
            </tbody>
        </table>

        <h2>Installation Steps</h2>
        <ol>
            <li>Install Python 3.10+</li>
            <li>Run: <code>pip install markitdown</code></li>
            <li>Import and use:
                <ul>
                    <li>Import the library</li>
                    <li>Create converter instance</li>
                    <li>Convert your files</li>
                </ul>
            </li>
        </ol>
    </body>
    </html>
    """

    # Line 156: Create temporary file for table HTML
    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as tmp:
        tmp.write(html_with_table)
        tmp_path = tmp.name

    try:
        # Line 162: Convert to Markdown
        result = md.convert(tmp_path)

        print("\n[INPUT] HTML with Table:")
        print("-" * 70)
        print(html_with_table[:400] + "...")

        print("\n[OUTPUT] Markdown with Table:")
        print("-" * 70)
        # Line 171: Print converted markdown showing table structure
        print(result.text_content)
    finally:
        os.unlink(tmp_path)


def example3_plain_text():
    """
    Example 3: Convert plain text content
    Demonstrates handling of plain text files.
    """
    print_section("EXAMPLE 3: Plain Text File Conversion")

    md = MarkItDown()

    # Line 186: Sample plain text content
    text_content = """MarkItDown - Document Converter

This is a plain text file that will be converted to Markdown.

Features:
- Fast conversion
- Multiple format support
- LLM-ready output

For more information, see the documentation.
"""

    # Line 199: Create temporary text file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tmp:
        tmp.write(text_content)
        tmp_path = tmp.name

    try:
        # Line 205: Convert text file
        result = md.convert(tmp_path)

        print("\n[INPUT] Plain Text Content:")
        print("-" * 70)
        print(text_content)

        print("\n[OUTPUT] Converted Markdown:")
        print("-" * 70)
        # Line 214: Display converted content
        print(result.text_content)
    finally:
        os.unlink(tmp_path)


def example4_rich_html_document():
    """
    Example 4: Convert rich HTML document with various elements
    Demonstrates comprehensive HTML element handling.
    """
    print_section("EXAMPLE 4: Rich HTML Document with Multiple Elements")

    md = MarkItDown()

    # Line 229: Comprehensive HTML example
    rich_html = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>MarkItDown Documentation</h1>

        <h2>Overview</h2>
        <p>MarkItDown is a <em>Python utility</em> developed by <strong>Microsoft</strong>
        for converting various file formats to Markdown.</p>

        <h2>Supported Formats</h2>
        <table>
            <tr>
                <th>Category</th>
                <th>Formats</th>
            </tr>
            <tr>
                <td>Documents</td>
                <td>PDF, DOCX, PPTX, XLSX</td>
            </tr>
            <tr>
                <td>Media</td>
                <td>JPG, PNG, WAV, MP3</td>
            </tr>
            <tr>
                <td>Web</td>
                <td>HTML, ZIP</td>
            </tr>
        </table>

        <h2>Quick Start</h2>
        <ol>
            <li><strong>Install:</strong> <code>pip install markitdown</code></li>
            <li><strong>Import:</strong> <code>from markitdown import MarkItDown</code></li>
            <li><strong>Convert:</strong> <code>md = MarkItDown(); result = md.convert('file.pdf')</code></li>
        </ol>

        <h2>Benefits</h2>
        <ul>
            <li>Preserves document structure</li>
            <li>In-memory processing (no temp files)</li>
            <li>LLM-ready output</li>
            <li>MIT License</li>
        </ul>

        <h2>Example Code</h2>
        <pre><code>
from markitdown import MarkItDown

# Create converter
md = MarkItDown()

# Convert file
result = md.convert('document.pdf')

# Access markdown
print(result.text_content)
        </code></pre>

        <blockquote>
            <p>"MarkItDown makes document conversion simple and efficient." - Microsoft</p>
        </blockquote>

        <h2>Links</h2>
        <p>For more information:</p>
        <ul>
            <li><a href="https://github.com/microsoft/markitdown">GitHub Repository</a></li>
            <li><a href="https://pypi.org/project/markitdown/">PyPI Package</a></li>
        </ul>
    </body>
    </html>
    """

    # Line 302: Create temporary rich HTML file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False) as tmp:
        tmp.write(rich_html)
        tmp_path = tmp.name

    try:
        # Line 308: Convert rich HTML
        result = md.convert(tmp_path)

        print("\n[INPUT] Rich HTML Document (first 500 chars):")
        print("-" * 70)
        print(rich_html[:500] + "...")

        print("\n[OUTPUT] Fully Converted Markdown:")
        print("-" * 70)
        # Line 317: Display full conversion result
        print(result.text_content)

        # Line 320: Show metadata if available
        print("\n[METADATA]")
        print("-" * 70)
        print(f"Content length: {len(result.text_content)} characters")
        print(f"Estimated lines: {len(result.text_content.splitlines())}")
    finally:
        os.unlink(tmp_path)


def main():
    """
    Main entry point for MarkItDown examples.
    Demonstrates various document conversion scenarios.
    """
    print("\n" + "=" * 70)
    print("Microsoft MarkItDown - Python Document Converter Examples")
    print("=" * 70)
    print("\nMarkItDown converts various formats to Markdown for LLM processing.")
    print("This demo shows HTML conversion capabilities.")

    # Line 342: Run Example 1 - Basic HTML
    example1_html_to_markdown()

    # Line 345: Run Example 2 - HTML with tables
    example2_complex_html_with_table()

    # Line 348: Run Example 3 - Plain text
    example3_plain_text()

    # Line 351: Run Example 4 - Rich HTML
    example4_rich_html_document()

    print("\n" + "=" * 70)
    print("All Examples Completed Successfully!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  • MarkItDown preserves document structure")
    print("  • Tables, lists, and formatting are maintained")
    print("  • Output is LLM-ready Markdown")
    print("  • Supports multiple file formats (PDF, DOCX, PPTX, XLSX, images, audio)")
    print("  • Requires Python 3.10 or higher")
    print(
        "\nFor more formats (PDF, DOCX, etc.), install: pip install 'markitdown[all]'"
    )


if __name__ == "__main__":
    # Line 369: Execute main function
    main()
