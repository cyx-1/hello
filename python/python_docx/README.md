# python-docx Demonstration

A comprehensive demonstration of the `python-docx` library for creating and manipulating Microsoft Word documents programmatically in Python.

## Overview

This example showcases the core capabilities of python-docx, including:
- Creating new Word documents
- Adding and formatting headings
- Creating paragraphs with various text styles (bold, italic, underline, colors)
- Building bulleted and numbered lists
- Creating and populating tables
- Working with page layout and sections
- Saving documents to disk

## Requirements

- **Python**: 3.11 or higher
- **Library**: python-docx >= 1.1.0

The library uses inline script metadata for dependency management via `uv`.

## Running the Example

```bash
cd python/python_docx
uv run main_python_docx.py
```

## Source Code

The complete source code with line numbers:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-docx>=1.1.0",
# ]
# ///

"""
python-docx demonstration: Creating and manipulating Word documents
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH


def main():
    """Demonstrate python-docx capabilities."""
    print("=" * 70)
    print("python-docx Demonstration: Creating and Manipulating Word Documents")
    print("=" * 70)
    print()

    # Line 36: Create a new Document object
    print("[Line 36] Creating a new Word document...")
    document = Document()                                        # ← Line 36
    print("✓ Document created successfully")
    print()

    # Line 42: Add a title heading
    print("[Line 42] Adding a title heading...")
    title = document.add_heading(                                # ← Line 42
        "python-docx Feature Demonstration", level=0
    )
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER                  # ← Line 43
    print("✓ Title added: 'python-docx Feature Demonstration'")
    print()

    # Line 49: Add a regular paragraph with text formatting
    print("[Line 49] Adding a paragraph with formatted text...")
    intro = document.add_paragraph(                              # ← Line 49
        "This document demonstrates the "
    )
    intro.add_run("python-docx").bold = True                     # ← Line 50
    intro.add_run(" library for creating and manipulating Word documents. ")
    intro.add_run("It's powerful and easy to use!").italic = True  # ← Line 52
    print("✓ Paragraph added with bold and italic formatting")
    print()

    # Line 58: Add a section heading
    print("[Line 58] Adding section heading: 'Basic Text Formatting'...")
    document.add_heading("1. Basic Text Formatting", level=1)    # ← Line 58
    print("✓ Section heading added")
    print()

    # Line 64: Demonstrate various text formatting options
    print("[Line 64] Adding paragraph with various formatting options...")
    p = document.add_paragraph()                                 # ← Line 64
    p.add_run("Bold text").bold = True                           # ← Line 65
    p.add_run(", ")
    p.add_run("Italic text").italic = True                       # ← Line 67
    p.add_run(", ")
    p.add_run("Underlined text").underline = True                # ← Line 69
    p.add_run(", and ")
    colored_run = p.add_run("Colored text")                      # ← Line 71
    colored_run.font.color.rgb = RGBColor(255, 0, 0)             # ← Line 72 (Red)
    colored_run.font.size = Pt(14)                               # ← Line 73
    print("✓ Formatted text added: bold, italic, underline, color, and size")
    print()

    # Line 79: Add a heading for lists section
    print("[Line 79] Adding section heading: 'Lists'...")
    document.add_heading("2. Lists", level=1)                    # ← Line 79
    print("✓ Section heading added")
    print()

    # Line 85: Create a bulleted list
    print("[Line 85] Creating a bulleted list...")
    document.add_paragraph("Features of python-docx:")           # ← Line 85
    document.add_paragraph(                                      # ← Line 86-90
        "Create new documents", style="List Bullet"
    )
    document.add_paragraph(
        "Add headings and paragraphs", style="List Bullet"
    )
    document.add_paragraph(
        "Format text (bold, italic, etc.)", style="List Bullet"
    )
    document.add_paragraph("Create tables", style="List Bullet")
    document.add_paragraph("Insert images", style="List Bullet")
    print("✓ Bulleted list created with 5 items")
    print()

    # Line 96: Create a numbered list
    print("[Line 96] Creating a numbered list...")
    document.add_paragraph("Steps to use python-docx:")          # ← Line 96
    document.add_paragraph(                                      # ← Line 97-101
        "Install: pip install python-docx", style="List Number"
    )
    document.add_paragraph(
        "Import: from docx import Document", style="List Number"
    )
    document.add_paragraph(
        "Create: document = Document()", style="List Number"
    )
    document.add_paragraph(
        "Add content using various methods", style="List Number"
    )
    document.add_paragraph(
        "Save: document.save('filename.docx')", style="List Number"
    )
    print("✓ Numbered list created with 5 steps")
    print()

    # Line 107: Add a heading for tables section
    print("[Line 107] Adding section heading: 'Tables'...")
    document.add_heading("3. Tables", level=1)                   # ← Line 107
    print("✓ Section heading added")
    print()

    # Line 113: Create a table
    print("[Line 113] Creating a 4x3 table...")
    table = document.add_table(rows=4, cols=3)                   # ← Line 113
    table.style = "Light Grid Accent 1"                          # ← Line 114
    print("✓ Table created with 'Light Grid Accent 1' style")
    print()

    # Line 120: Populate table headers
    print("[Line 120] Populating table headers...")
    header_cells = table.rows[0].cells                           # ← Line 120
    header_cells[0].text = "Library"                             # ← Line 121
    header_cells[1].text = "Purpose"                             # ← Line 122
    header_cells[2].text = "Difficulty"                          # ← Line 123
    print("✓ Headers: Library, Purpose, Difficulty")
    print()

    # Line 129: Populate table data
    print("[Line 129] Populating table data...")
    data_rows = [                                                # ← Line 129
        ("python-docx", "Word documents", "Easy"),
        ("openpyxl", "Excel spreadsheets", "Easy"),
        ("PyPDF2", "PDF manipulation", "Medium"),
    ]

    for i, (lib, purpose, difficulty) in enumerate(data_rows, start=1):  # ← Line 135
        row_cells = table.rows[i].cells
        row_cells[0].text = lib
        row_cells[1].text = purpose
        row_cells[2].text = difficulty

    print(f"✓ Added {len(data_rows)} data rows to table")
    print()

    # Line 147: Add a heading for page layout section
    print("[Line 147] Adding section heading: 'Page Layout'...")
    document.add_heading("4. Page Layout and Sections", level=1)  # ← Line 146
    print("✓ Section heading added")
    print()

    # Line 153: Demonstrate section manipulation
    print("[Line 153] Adding information about current page layout...")
    section = document.sections[0]                               # ← Line 152
    p = document.add_paragraph(                                  # ← Line 153
        f"Page width: {section.page_width.inches:.2f} inches"
    )
    p.add_run(f"\nPage height: {section.page_height.inches:.2f} inches")     # ← Line 154
    p.add_run(f"\nTop margin: {section.top_margin.inches:.2f} inches")       # ← Line 155
    p.add_run(f"\nBottom margin: {section.bottom_margin.inches:.2f} inches") # ← Line 156
    p.add_run(f"\nLeft margin: {section.left_margin.inches:.2f} inches")     # ← Line 157
    p.add_run(f"\nRight margin: {section.right_margin.inches:.2f} inches")   # ← Line 158
    print("✓ Page layout information added")
    print()

    # Line 166: Add a conclusion heading
    print("[Line 166] Adding conclusion section...")
    document.add_heading("5. Conclusion", level=1)               # ← Line 164
    conclusion = document.add_paragraph(                         # ← Line 165
        "The python-docx library provides a comprehensive and intuitive API for "
        "creating and manipulating Word documents programmatically. It supports "
        "all common document elements and formatting options."
    )
    print("✓ Conclusion paragraph added")
    print()

    # Line 177: Save the document
    output_file = "python_docx_demo.docx"                        # ← Line 174
    print(f"[Line 177] Saving document to '{output_file}'...")
    document.save(output_file)                                   # ← Line 176
    print(f"✓ Document saved successfully to '{output_file}'")
    print()

    # Line 184: Display summary statistics
    print("=" * 70)
    print("Document Creation Summary")
    print("=" * 70)
    print(f"Total paragraphs: {len(document.paragraphs)}")       # ← Line 184
    print(f"Total tables: {len(document.tables)}")               # ← Line 185
    print(f"Total sections: {len(document.sections)}")           # ← Line 186
    print(f"Output file: {output_file}")
    print()
    print("✓ Document creation complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
```

## Program Output

```
======================================================================
python-docx Demonstration: Creating and Manipulating Word Documents
======================================================================

[Line 36] Creating a new Word document...
✓ Document created successfully

[Line 42] Adding a title heading...
✓ Title added: 'python-docx Feature Demonstration'

[Line 49] Adding a paragraph with formatted text...
✓ Paragraph added with bold and italic formatting

[Line 58] Adding section heading: 'Basic Text Formatting'...
✓ Section heading added

[Line 64] Adding paragraph with various formatting options...
✓ Formatted text added: bold, italic, underline, color, and size

[Line 79] Adding section heading: 'Lists'...
✓ Section heading added

[Line 85] Creating a bulleted list...
✓ Bulleted list created with 5 items

[Line 96] Creating a numbered list...
✓ Numbered list created with 5 steps

[Line 107] Adding section heading: 'Tables'...
✓ Section heading added

[Line 113] Creating a 4x3 table...
✓ Table created with 'Light Grid Accent 1' style

[Line 120] Populating table headers...
✓ Headers: Library, Purpose, Difficulty

[Line 129] Populating table data...
✓ Added 3 data rows to table

[Line 147] Adding section heading: 'Page Layout'...
✓ Section heading added

[Line 153] Adding information about current page layout...
✓ Page layout information added

[Line 166] Adding conclusion section...
✓ Conclusion paragraph added

[Line 177] Saving document to 'python_docx_demo.docx'...
✓ Document saved successfully to 'python_docx_demo.docx'

======================================================================
Document Creation Summary
======================================================================
Total paragraphs: 22
Total tables: 1
Total sections: 1
Output file: python_docx_demo.docx

✓ Document creation complete!
======================================================================
```

## Key Features Demonstrated

### 1. Document Creation (Line 36)
The script starts by creating a new `Document()` object, which represents an empty Word document in memory.

### 2. Adding Headings (Lines 42, 58, 79, 107, 146, 164)
- **Level 0** heading creates a title (largest)
- **Level 1** headings create major section headers
- Headings can be aligned using `WD_ALIGN_PARAGRAPH` constants

### 3. Text Formatting (Lines 49-73)
- **Bold**: `run.bold = True`
- **Italic**: `run.italic = True`
- **Underline**: `run.underline = True`
- **Color**: `run.font.color.rgb = RGBColor(r, g, b)`
- **Font size**: `run.font.size = Pt(size)`

### 4. Lists (Lines 85-101)
- **Bulleted lists**: Use `style="List Bullet"`
- **Numbered lists**: Use `style="List Number"`

### 5. Tables (Lines 113-139)
- Create tables with `add_table(rows, cols)`
- Apply styles: `table.style = "style_name"`
- Access cells: `table.rows[i].cells[j]`
- Populate cells: `cell.text = "value"`

### 6. Page Layout (Lines 152-158)
- Access section properties: `document.sections[0]`
- Read page dimensions and margins
- All measurements available in inches, centimeters, or points

### 7. Saving Documents (Line 176)
Save the document to disk using `document.save(filename)`, creating a `.docx` file.

## Output Files

Running this script generates:
- **python_docx_demo.docx**: A fully formatted Word document containing all demonstrated features

## Key Concepts

### Document Structure
A Word document consists of:
- **Sections**: Page layout containers (margins, size, orientation)
- **Paragraphs**: Text blocks (can contain multiple runs)
- **Runs**: Individual text segments with consistent formatting
- **Tables**: Grid structures for organizing data

### Inline Script Metadata
The script uses PEP 723 inline script metadata:
```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-docx>=1.1.0",
# ]
# ///
```
This allows `uv` to automatically manage dependencies without a separate `pyproject.toml` file.

## Use Cases

python-docx is ideal for:
- Automated report generation
- Document template population
- Batch document creation
- Converting data to formatted Word documents
- Creating standardized documentation

## Additional Resources

- [python-docx Documentation](https://python-docx.readthedocs.io/)
- [python-docx GitHub Repository](https://github.com/python-openxml/python-docx)
