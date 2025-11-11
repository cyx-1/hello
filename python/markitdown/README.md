# Microsoft MarkItDown - Python Example

This example demonstrates Microsoft's **MarkItDown** library, a utility for converting various file formats and office documents to Markdown. MarkItDown is designed to prepare documents for LLM processing and text analysis pipelines.

## Requirements

- **Python Version**: Python 3.10 or higher
- **Library**: markitdown >= 0.0.1
- **Installation**: Dependencies are managed automatically via inline script metadata

## Running the Example

Using `uv` (recommended):
```bash
cd python/markitdown
uv run main_markitdown.py
```

## What is MarkItDown?

MarkItDown is a Python library developed by Microsoft that converts:
- **Documents**: PDF, DOCX, PPTX, XLSX, XLS
- **Images**: JPG, PNG
- **Audio**: WAV, MP3
- **Web**: HTML, ZIP archives

Key features:
- Preserves document structure (headings, lists, tables, links)
- In-memory processing (no temporary files)
- LLM-ready Markdown output
- MIT License

## Source Code Overview

### Initialization (Lines 45-48)

```python
45  # Line 45: Initialize MarkItDown converter
46  md = MarkItDown()
47
48  # Line 48: Sample HTML with various elements
```

**Explanation**: The converter is initialized with a simple `MarkItDown()` constructor. This instance can be reused for multiple conversions.

---

### Example 1: Basic HTML Conversion (Lines 72-87)

```python
72  # Line 72: Create a temporary HTML file
73  with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as tmp:
74      tmp.write(html_content)
75      tmp_path = tmp.name
76
77  try:
78      # Line 78: Convert HTML file to Markdown
79      result = md.convert(tmp_path)
...
87      # Line 87: Access the converted markdown text
88      print(result.text_content)
```

**Output (Lines 78-87)**:
```
[INPUT] HTML Content:
----------------------------------------------------------------------

    <!DOCTYPE html>
    <html>
    <head><title>Sample Document</title></head>
    <body>
        <h1>Welcome to MarkItDown</h1>
        <p>This is a <strong>powerful</strong> tool for converting documents to Markdown.</p>
...

[OUTPUT] Converted Markdown:
----------------------------------------------------------------------
# Welcome to MarkItDown

This is a **powerful** tool for converting documents to Markdown.

## Key Features

* Converts HTML to Markdown
* Preserves document structure
* Handles multiple formats
```

**Annotation**:
- **Line 73-75**: Creates a temporary HTML file using Python's `tempfile` module
- **Line 79**: The `convert()` method accepts a file path and returns a result object
- **Line 88**: The `result.text_content` property contains the converted Markdown text
- **Output**: Notice how `<h1>` becomes `#`, `<strong>` becomes `**`, and `<ul><li>` becomes `*` lists

---

### Example 2: Tables and Complex Structure (Lines 156-171)

```python
156  # Line 156: Create temporary file for table HTML
157  with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as tmp:
158      tmp.write(html_with_table)
159      tmp_path = tmp.name
160
161  try:
162      # Line 162: Convert to Markdown
163      result = md.convert(tmp_path)
...
171      # Line 171: Print converted markdown showing table structure
172      print(result.text_content)
```

**Input (Lines 104-142)**: HTML with table structure
```html
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
        ...
    </tbody>
</table>
```

**Output (Lines 162-171)**:
```
[OUTPUT] Markdown with Table:
----------------------------------------------------------------------
# Product Comparison

| Product | Price | Rating |
| --- | --- | --- |
| Product A | $99.99 | ⭐⭐⭐⭐⭐ |
| Product B | $149.99 | ⭐⭐⭐⭐ |
| Product C | $79.99 | ⭐⭐⭐⭐⭐ |

## Installation Steps

1. Install Python 3.10+
2. Run: `pip install markitdown`
3. Import and use:
   * Import the library
   * Create converter instance
   * Convert your files
```

**Annotation**:
- **Line 104-142**: HTML table with `<thead>`, `<tbody>`, `<th>`, and `<td>` elements
- **Line 163**: Single `convert()` call processes the entire document
- **Output**: HTML tables are converted to GitHub-flavored Markdown table format with `|` separators
- **Output**: Nested lists (`<ol>` with nested `<ul>`) are properly indented with numbers and bullets
- **Output**: Inline code (`<code>`) becomes backtick-wrapped text

---

### Example 3: Plain Text Conversion (Lines 199-214)

```python
199  # Line 199: Create temporary text file
200  with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
201      tmp.write(text_content)
202      tmp_path = tmp.name
203
204  try:
205      # Line 205: Convert text file
206      result = md.convert(tmp_path)
...
214      # Line 214: Display converted content
215      print(result.text_content)
```

**Output (Lines 205-214)**:
```
[INPUT] Plain Text Content:
----------------------------------------------------------------------
MarkItDown - Document Converter

This is a plain text file that will be converted to Markdown.

Features:
- Fast conversion
- Multiple format support
- LLM-ready output

For more information, see the documentation.

[OUTPUT] Converted Markdown:
----------------------------------------------------------------------
MarkItDown - Document Converter

This is a plain text file that will be converted to Markdown.

Features:
- Fast conversion
- Multiple format support
- LLM-ready output

For more information, see the documentation.
```

**Annotation**:
- **Line 186-197**: Plain text content with dashes for bullets
- **Line 206**: MarkItDown handles plain text files seamlessly
- **Output**: Plain text is preserved as-is, which is already valid Markdown
- **Output**: The dash-based list format is recognized as Markdown bullets

---

### Example 4: Rich HTML with Multiple Elements (Lines 302-324)

```python
302  # Line 302: Create temporary rich HTML file
303  with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as tmp:
304      tmp.write(rich_html)
305      tmp_path = tmp.name
306
307  try:
308      # Line 308: Convert rich HTML
309      result = md.convert(tmp_path)
...
317      # Line 317: Display full conversion result
318      print(result.text_content)
319
320      # Line 320: Show metadata if available
321      print("\n[METADATA]")
322      print("-" * 70)
323      print(f"Content length: {len(result.text_content)} characters")
324      print(f"Estimated lines: {len(result.text_content.splitlines())}")
```

**Input (Lines 229-300)**: Comprehensive HTML with:
- Headings (`<h1>`, `<h2>`)
- Emphasis (`<em>`, `<strong>`)
- Tables with multiple columns
- Ordered lists (`<ol>`)
- Unordered lists (`<ul>`)
- Code blocks (`<pre><code>`)
- Blockquotes (`<blockquote>`)
- Links (`<a href>`)

**Output (Lines 308-324)**:
```
[OUTPUT] Fully Converted Markdown:
----------------------------------------------------------------------
# MarkItDown Documentation

## Overview

MarkItDown is a *Python utility* developed by **Microsoft**
for converting various file formats to Markdown.

## Supported Formats

| Category | Formats |
| --- | --- |
| Documents | PDF, DOCX, PPTX, XLSX |
| Media | JPG, PNG, WAV, MP3 |
| Web | HTML, ZIP |

## Quick Start

1. **Install:** `pip install markitdown`
2. **Import:** `from markitdown import MarkItDown`
3. **Convert:** `md = MarkItDown(); result = md.convert('file.pdf')`

## Benefits

* Preserves document structure
* In-memory processing (no temp files)
* LLM-ready output
* MIT License

## Example Code

```
from markitdown import MarkItDown

# Create converter
md = MarkItDown()

# Convert file
result = md.convert('document.pdf')

# Access markdown
print(result.text_content)
```

> "MarkItDown makes document conversion simple and efficient." - Microsoft

## Links

For more information:

* [GitHub Repository](https://github.com/microsoft/markitdown)
* [PyPI Package](https://pypi.org/project/markitdown/)

[METADATA]
----------------------------------------------------------------------
Content length: 1017 characters
Estimated lines: 51
```

**Annotation**:
- **Line 229**: Rich HTML with comprehensive document elements
- **Line 309**: Single `convert()` call processes all elements
- **Line 318**: `result.text_content` contains the fully converted Markdown
- **Line 323-324**: Metadata extraction showing content statistics
- **Output**: `<em>` becomes `*italic*`, `<strong>` becomes `**bold**`
- **Output**: `<pre><code>` becomes fenced code blocks with triple backticks
- **Output**: `<blockquote>` becomes `>` prefixed text
- **Output**: `<a href="...">text</a>` becomes `[text](url)` format
- **Output**: All structure, formatting, and links are perfectly preserved

---

### Main Function (Lines 342-369)

```python
342  # Line 342: Run Example 1 - Basic HTML
343  example1_html_to_markdown()
344
345  # Line 345: Run Example 2 - HTML with tables
346  example2_complex_html_with_table()
347
348  # Line 348: Run Example 3 - Plain text
349  example3_plain_text()
350
351  # Line 351: Run Example 4 - Rich HTML
352  example4_rich_html_document()
...
369  # Line 369: Execute main function
370  main()
```

**Output (Full Program)**:
```
======================================================================
Microsoft MarkItDown - Python Document Converter Examples
======================================================================

MarkItDown converts various formats to Markdown for LLM processing.
This demo shows HTML conversion capabilities.
...
======================================================================
All Examples Completed Successfully!
======================================================================

Key Takeaways:
  • MarkItDown preserves document structure
  • Tables, lists, and formatting are maintained
  • Output is LLM-ready Markdown
  • Supports multiple file formats (PDF, DOCX, PPTX, XLSX, images, audio)
  • Requires Python 3.10 or higher

For more formats (PDF, DOCX, etc.), install: pip install 'markitdown[all]'
```

**Annotation**:
- **Lines 342-352**: All four examples are executed sequentially
- **Line 370**: Entry point when script is run directly
- **Output**: Complete demonstration showing all conversion capabilities
- **Output**: Final summary provides key information about the library

---

## Key Features Demonstrated

### 1. Structure Preservation
- **Headings**: HTML `<h1>` to `<h6>` → Markdown `#` to `######`
- **Lists**: Ordered `<ol>` and unordered `<ul>` → Numbered and bulleted lists
- **Tables**: HTML tables → GitHub-flavored Markdown tables
- **Links**: `<a href>` → `[text](url)` format

### 2. Formatting Retention
- **Bold**: `<strong>` or `<b>` → `**text**`
- **Italic**: `<em>` or `<i>` → `*text*`
- **Code**: `<code>` → `` `code` ``
- **Code blocks**: `<pre><code>` → Fenced code blocks

### 3. Advanced Elements
- **Blockquotes**: `<blockquote>` → `>` prefixed lines
- **Nested lists**: Properly indented with correct markers
- **Emoji support**: Unicode characters preserved (⭐)
- **Table formatting**: Clean, readable Markdown tables

### 4. In-Memory Processing
- Uses temporary files for demonstration purposes
- MarkItDown processes files without creating intermediate files
- Efficient for large-scale document processing

## Use Cases

1. **LLM Document Preparation**: Convert documents to Markdown for feeding to language models
2. **Content Migration**: Convert legacy HTML/Office documents to Markdown
3. **Documentation Processing**: Standardize documentation across formats
4. **Data Pipeline**: Integrate document conversion into text analysis workflows

## Additional Formats

While this example focuses on HTML, MarkItDown supports many formats:

```bash
# For full format support (PDF, Office docs, images, audio)
pip install 'markitdown[all]'
```

Then you can convert:
```python
md = MarkItDown()

# Convert PDF
pdf_result = md.convert('document.pdf')

# Convert Word document
docx_result = md.convert('report.docx')

# Convert PowerPoint
pptx_result = md.convert('presentation.pptx')

# Convert Excel
xlsx_result = md.convert('data.xlsx')

# Convert image (extracts text via OCR)
jpg_result = md.convert('screenshot.jpg')
```

## Version Requirements

**IMPORTANT**: This example requires:
- **Python 3.10 or higher**: MarkItDown uses modern Python features
- **markitdown library**: Installed automatically via inline script metadata

## Resources

- **GitHub**: https://github.com/microsoft/markitdown
- **PyPI**: https://pypi.org/project/markitdown/
- **License**: MIT

## Summary

This example demonstrates Microsoft MarkItDown's capabilities through four progressively complex examples:
1. **Basic HTML**: Simple structure conversion
2. **Tables**: Complex table and nested list handling
3. **Plain Text**: Text file processing
4. **Rich HTML**: Comprehensive document element conversion

The output shows how MarkItDown preserves structure, formatting, and content while producing clean, LLM-ready Markdown.
