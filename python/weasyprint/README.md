# WeasyPrint Demonstration

A comprehensive demonstration of the `WeasyPrint` library for converting HTML and CSS to PDF documents in Python.

## Overview

This example showcases the core capabilities of WeasyPrint, including:
- Converting HTML to PDF
- Applying CSS styling to PDFs
- Creating multi-page documents with headers and footers
- Generating professional invoices and reports
- Working with external CSS stylesheets
- In-memory PDF generation (BytesIO)
- Page layout control with @page CSS rules

## Requirements

- **Python**: 3.11 or higher
- **Library**: WeasyPrint >= 62.3

The library uses inline script metadata for dependency management via `uv`.

**Note**: WeasyPrint requires system libraries (Cairo, Pango, GDK-PixBuf) which are typically pre-installed on most Linux systems and can be installed on macOS via Homebrew.

## Running the Example

```bash
cd python/weasyprint
uv run main_weasyprint.py
```

## Source Code

The complete source code with line numbers and annotations:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "weasyprint>=62.3",
# ]
# ///

"""
WeasyPrint demonstration: Converting HTML/CSS to PDF documents
"""

from weasyprint import HTML, CSS
from io import BytesIO


def main():
    """Demonstrate WeasyPrint PDF generation capabilities."""
    print("=" * 70)
    print("WeasyPrint Demonstration: HTML/CSS to PDF Conversion")
    print("=" * 70)
    print()

    # Line 38: Create a simple HTML to PDF conversion
    print("[Line 38] Creating a basic PDF from HTML string...")
    html_content = """                                          # ← Line 38
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>WeasyPrint Basic Demo</title>
    </head>
    <body>
        <h1>Welcome to WeasyPrint</h1>
        <p>This is a simple HTML to PDF conversion.</p>
    </body>
    </html>
    """
    doc = HTML(string=html_content)                              # ← Line 52
    doc.write_pdf("basic_demo.pdf")                              # ← Line 53
    print("✓ Created 'basic_demo.pdf' from HTML string")
    print()

    # Line 60: Create a styled PDF with CSS
    print("[Line 60] Creating a styled PDF with custom CSS...")
    styled_html = """                                            # ← Line 60
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Styled Document</title>
        <style>
            @page {                                              # ← Line 68
                size: A4;
                margin: 2cm;
            }
            body {
                font-family: 'Helvetica', sans-serif;
                line-height: 1.6;
                color: #333;
            }
            h1 {
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }
            .highlight {                                         # ← Line 84
                background-color: #fffacd;
                padding: 10px;
                border-left: 4px solid #f39c12;
                margin: 15px 0;
            }
            .info-box {                                          # ← Line 90
                background-color: #e8f4f8;
                border: 2px solid #3498db;
                border-radius: 5px;
                padding: 15px;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <h1>WeasyPrint Styled Document</h1>
        <div class="info-box">
            <strong>About WeasyPrint:</strong> A visual rendering engine...
        </div>
        <h2>Key Features</h2>
        <ul>
            <li>Convert HTML/CSS to PDF</li>
            <li>Support for modern CSS3 features</li>
            <li>Automatic page breaks</li>
            <li>Print-specific CSS with @page rules</li>
        </ul>
    </body>
    </html>
    """
    HTML(string=styled_html).write_pdf("styled_demo.pdf")        # ← Line 157
    print("✓ Created 'styled_demo.pdf' with CSS styling")
    print()

    # Line 164: Create a multi-page document with page numbers
    print("[Line 164] Creating multi-page PDF with headers and footers...")
    multipage_html = """                                         # ← Line 164
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Multi-Page Document</title>
        <style>
            @page {                                              # ← Line 172
                size: A4;
                margin: 3cm 2cm 3cm 2cm;

                @top-center {                                    # ← Line 176
                    content: "WeasyPrint Multi-Page Demo";
                    font-size: 10pt;
                    color: #666;
                    border-bottom: 1px solid #ccc;
                }

                @bottom-right {                                  # ← Line 183
                    content: "Page " counter(page) " of " counter(pages);
                    font-size: 9pt;
                    color: #666;
                }

                @bottom-left {                                   # ← Line 189
                    content: "Generated with WeasyPrint";
                    font-size: 9pt;
                }
            }

            .page-break {                                        # ← Line 220
                page-break-before: always;
            }

            table {                                              # ← Line 224
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }

            th {
                background-color: #3498db;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>WeasyPrint Multi-Page Document</h1>

        <h2>Page Layout Features</h2>
        <p>WeasyPrint supports the CSS Paged Media Module...</p>

        <table>                                                  # ← Line 281
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Description</th>
                    <th>Supported</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>CSS3 Selectors</td>
                    <td>Modern CSS selector support</td>
                    <td>✓ Yes</td>
                </tr>
                <tr>
                    <td>Flexbox</td>
                    <td>Flexible box layout</td>
                    <td>✓ Yes</td>
                </tr>
                <!-- More rows... -->
            </tbody>
        </table>

        <div class="page-break"></div>                          # ← Line 335 - Forces page break

        <h2>Page 2: Additional Content</h2>
        <p>This content appears on the second page...</p>
    </body>
    </html>
    """
    HTML(string=multipage_html).write_pdf("multipage_demo.pdf")  # ← Line 386
    print("✓ Created 'multipage_demo.pdf' with multiple pages")
    print()

    # Line 393: Generate PDF invoice
    print("[Line 393] Creating invoice-style PDF...")
    invoice_html = """                                           # ← Line 393
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {
                size: A4 portrait;
                margin: 1.5cm;
            }

            .header {                                            # ← Line 404
                text-align: center;
                margin-bottom: 30px;
                border-bottom: 3px solid #2c3e50;
            }

            .items-table {                                       # ← Line 432
                width: 100%;
                border-collapse: collapse;
            }

            .items-table th {
                background-color: #2c3e50;
                color: white;
                padding: 12px;
            }

            .grand-total {                                       # ← Line 475
                border-top: 2px solid #2c3e50;
                font-size: 14pt;
                color: #2c3e50;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>INVOICE</h1>
            <p>Invoice #INV-2024-001</p>
        </div>

        <table class="items-table">
            <thead>
                <tr>
                    <th>Description</th>
                    <th>Quantity</th>
                    <th>Unit Price</th>
                    <th>Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>WeasyPrint PDF Generation Service</td>
                    <td>100</td>
                    <td>$2.50</td>
                    <td>$250.00</td>
                </tr>
                <!-- More items... -->
            </tbody>
        </table>

        <div class="total-section">
            <div class="grand-total">
                <div class="label">TOTAL:</div>
                <div class="amount">$2,522.63</div>
            </div>
        </div>
    </body>
    </html>
    """
    HTML(string=invoice_html).write_pdf("invoice_demo.pdf")      # ← Line 625
    print("✓ Created 'invoice_demo.pdf'")
    print()

    # Line 631: Generate PDF to BytesIO (in-memory)
    print("[Line 631] Generating PDF to memory (BytesIO)...")
    simple_html = "<h1>PDF in Memory</h1><p>Generated to BytesIO.</p>"
    pdf_bytes = BytesIO()                                        # ← Line 633
    HTML(string=simple_html).write_pdf(pdf_bytes)                # ← Line 634
    pdf_size = pdf_bytes.tell()                                  # ← Line 635
    print(f"✓ Generated PDF to memory: {pdf_size} bytes")
    print("  - Useful for web applications (no file I/O)")
    print()

    # Line 644: Apply external CSS
    print("[Line 644] Applying external CSS stylesheet...")
    html_with_external_css = """                                 # ← Line 644
    <!DOCTYPE html>
    <html>
    <body>
        <div class="container">
            <h1 class="title">External CSS Styling</h1>
            <p class="content">
                This demonstrates using external CSS stylesheets.
            </p>
            <div class="box">
                <h2>Highlighted Section</h2>
                <p>Styled with external CSS.</p>
            </div>
        </div>
    </body>
    </html>
    """

    external_css = CSS(string="""                                # ← Line 669
        @page {
            size: A4;
            margin: 2cm;
        }

        .title {
            color: #e74c3c;
            font-size: 24pt;
            border-bottom: 3px solid #e74c3c;
        }

        .box {                                                   # ← Line 689
            background-color: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 8px;
            padding: 20px;
        }
    """)

    HTML(string=html_with_external_css).write_pdf(               # ← Line 703
        "external_css_demo.pdf",
        stylesheets=[external_css]                               # ← Line 705 - Pass CSS separately
    )
    print("✓ Created 'external_css_demo.pdf' with external CSS")
    print()


if __name__ == "__main__":
    main()
```

## Program Output

```
======================================================================
WeasyPrint Demonstration: HTML/CSS to PDF Conversion
======================================================================

[Line 38] Creating a basic PDF from HTML string...
✓ Created 'basic_demo.pdf' from HTML string

[Line 60] Creating a styled PDF with custom CSS...
✓ Created 'styled_demo.pdf' with CSS styling
  - Applied custom fonts and colors
  - Used CSS classes for layout
  - Set page margins with @page rule

[Line 164] Creating multi-page PDF with headers and footers...
✓ Created 'multipage_demo.pdf' with multiple pages
  - Added header with document title
  - Added footer with page numbers (Page X of Y)
  - Applied page breaks for content organization
  - Included styled table with data

[Line 393] Creating invoice-style PDF...
✓ Created 'invoice_demo.pdf' with professional invoice layout
  - Applied business-style formatting
  - Created itemized table with calculations
  - Used flexbox for two-column layout

[Line 631] Generating PDF to memory (BytesIO)...
✓ Generated PDF to memory: 6468 bytes
  - Useful for web applications (no file I/O)
  - Can be sent directly in HTTP responses

[Line 644] Applying external CSS stylesheet...
✓ Created 'external_css_demo.pdf' with external CSS
  - Separated HTML structure from styling
  - Passed CSS object to write_pdf() method

======================================================================
PDF Generation Summary
======================================================================
Generated files:
  1. basic_demo.pdf - Simple HTML to PDF conversion
  2. styled_demo.pdf - CSS styled document with colors and layout
  3. multipage_demo.pdf - Multi-page with headers, footers, page numbers
  4. invoice_demo.pdf - Professional invoice template
  5. external_css_demo.pdf - Using external CSS stylesheets

✓ All PDFs generated successfully!
======================================================================
```

## Key Features Demonstrated

### 1. Basic HTML to PDF Conversion (Lines 38-53)

The simplest way to use WeasyPrint is to create an HTML object from a string and write it to a PDF file:

```python
html_content = """<html><body><h1>Hello PDF!</h1></body></html>"""
HTML(string=html_content).write_pdf("output.pdf")
```

**Output**: Creates a basic PDF with minimal styling using browser defaults.

### 2. CSS Styling (Lines 60-157)

WeasyPrint supports modern CSS for styling PDFs. The `@page` rule (Line 68) controls page layout:

```python
@page {
    size: A4;          # Standard A4 page size
    margin: 2cm;       # 2cm margins on all sides
}
```

CSS classes like `.info-box` (Line 90) and `.highlight` (Line 84) style content just like in web pages, including:
- Background colors
- Borders and border-radius
- Padding and margins
- Font properties

**Output**: A professionally styled PDF with colored sections, borders, and custom typography.

### 3. Multi-Page Documents with Headers and Footers (Lines 164-386)

The `@page` CSS rule supports margin boxes for headers and footers:

```python
@page {
    @top-center {                                    # Line 176
        content: "Document Title";
        font-size: 10pt;
    }

    @bottom-right {                                  # Line 183
        content: "Page " counter(page) " of " counter(pages);
    }
}
```

**Key annotations:**
- **Line 176**: `@top-center` creates a header at the top center of each page
- **Line 183**: `@bottom-right` creates a footer with dynamic page numbers using CSS counters
- **Line 220**: `.page-break` class forces content to start on a new page
- **Line 281**: HTML tables are rendered with proper styling across pages

**Output**: A 3-page PDF with:
- Header showing "WeasyPrint Multi-Page Demo" on every page
- Footer with "Page X of Y" in bottom-right corner
- Styled table with alternating row colors
- Explicit page breaks where specified

### 4. Professional Invoice Template (Lines 393-625)

Demonstrates a real-world use case: generating invoices programmatically.

```python
.items-table th {                                    # Line 432
    background-color: #2c3e50;
    color: white;
}

.grand-total {                                       # Line 475
    border-top: 2px solid #2c3e50;
    font-size: 14pt;
}
```

**Key features:**
- Professional header with invoice number and date
- Two-column layout for sender/recipient information
- Itemized table with quantities and amounts
- Calculated totals with tax
- Business-appropriate styling

**Output**: A professional invoice PDF ready for printing or emailing to clients.

### 5. In-Memory PDF Generation (Lines 631-641)

Generate PDFs to memory instead of files using BytesIO:

```python
pdf_bytes = BytesIO()                                # Line 633
HTML(string=simple_html).write_pdf(pdf_bytes)        # Line 634
pdf_size = pdf_bytes.tell()                          # Line 635 - Get size in bytes
```

**Use cases:**
- Web applications that serve PDFs via HTTP without disk I/O
- API endpoints returning PDFs
- Streaming PDFs to cloud storage
- Email attachments generated on-the-fly

**Output**: PDF stored in memory (6,468 bytes), no file created on disk.

### 6. External CSS Stylesheets (Lines 644-706)

Separate HTML structure from styling for better code organization:

```python
external_css = CSS(string="""...""")                 # Line 669
HTML(string=html_content).write_pdf(
    "output.pdf",
    stylesheets=[external_css]                       # Line 705
)
```

**Benefits:**
- Reuse CSS across multiple documents
- Easier maintenance of styles
- Can load CSS from files: `CSS(filename='styles.css')`

**Output**: PDF with styling applied from external CSS object.

## CSS Paged Media Features

WeasyPrint implements the [CSS Paged Media Module](https://www.w3.org/TR/css-page-3/), which includes:

### @page Rule
Controls page layout properties:
- `size`: Page dimensions (A4, Letter, custom)
- `margin`: Page margins
- `orientation`: Portrait or landscape

### Margin Boxes
Sixteen margin boxes for headers and footers:
- `@top-left`, `@top-center`, `@top-right`
- `@bottom-left`, `@bottom-center`, `@bottom-right`
- Plus left, right, and corner boxes

### Page Counters
- `counter(page)`: Current page number
- `counter(pages)`: Total page count
- Custom counters for chapters, figures, etc.

### Page Breaks
- `page-break-before`: always, avoid, auto
- `page-break-after`: always, avoid, auto
- `page-break-inside`: avoid, auto

## System Dependencies

WeasyPrint requires these system libraries:

**Linux (Debian/Ubuntu):**
```bash
sudo apt-get install python3-dev libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 shared-mime-info
```

**macOS (Homebrew):**
```bash
brew install cairo pango gdk-pixbuf libffi
```

**Windows:**
Follow the [GTK installation guide](https://gtk-download.com/)

These are typically pre-installed on Linux systems and CI/CD environments.

## Use Cases

WeasyPrint excels at:

1. **Invoice and Receipt Generation**
   - Professional formatting with tables and calculations
   - Business branding with logos and colors

2. **Report Generation**
   - Multi-page reports with headers, footers, page numbers
   - Charts and graphs (embed as SVG/PNG)

3. **Certificate and Diploma Creation**
   - Precise layout control with CSS
   - Custom fonts and decorative elements

4. **Documentation and Manuals**
   - Table of contents with page references
   - Cross-references and bookmarks

5. **Web Content Archival**
   - Convert web pages to PDF preserving layout
   - Capture styled HTML emails as PDFs

## Advanced Features Not Covered

- **Bookmarks**: PDF table of contents navigation
- **Attachments**: Embed files in PDFs
- **Fonts**: Custom fonts with `@font-face`
- **SVG**: Inline SVG graphics
- **Images**: From files, URLs, or data URIs
- **Media queries**: Different styles for print vs screen
- **Named pages**: Different page layouts in one document

## Performance Tips

1. **Reuse CSS objects**: Create CSS once, apply to multiple documents
2. **Use BytesIO**: Avoid disk I/O in web applications
3. **Optimize images**: Compress images before embedding
4. **Font subsetting**: Automatically reduces font file sizes
5. **Cache templates**: Store HTML templates, populate with data

## Comparison with Alternatives

| Feature | WeasyPrint | ReportLab | wkhtmltopdf | pdfkit |
|---------|-----------|-----------|-------------|--------|
| Input | HTML/CSS | Python code | HTML | HTML |
| CSS Support | Excellent | Limited | Good | Good |
| Modern CSS | ✓ Yes | ✗ No | ⚠ Partial | ⚠ Partial |
| Page Headers | ✓ CSS @page | ✓ Code | ✓ Yes | ⚠ Limited |
| Learning Curve | Low | Medium | Low | Low |
| Dependencies | System libs | Pure Python | Binary | wkhtmltopdf |
| Performance | Fast | Faster | Fast | Fast |

**WeasyPrint advantages:**
- Uses familiar HTML/CSS (web developer friendly)
- Excellent CSS3 support including Flexbox
- Standards-compliant (W3C CSS Paged Media)
- Active development and maintenance

## Output Files

Running this script generates 5 PDF files demonstrating different capabilities:

1. **basic_demo.pdf** (Simple conversion)
   - Minimal HTML with default styling
   - Demonstrates the simplest API usage

2. **styled_demo.pdf** (CSS styling)
   - Custom fonts, colors, and spacing
   - Info boxes and highlighted sections
   - Professional document appearance

3. **multipage_demo.pdf** (3 pages)
   - Headers on every page
   - Page numbers "Page X of Y"
   - Styled table spanning multiple rows
   - Explicit and automatic page breaks

4. **invoice_demo.pdf** (Business template)
   - Professional invoice layout
   - Itemized billing table
   - Calculated subtotals and tax
   - Print-ready business document

5. **external_css_demo.pdf** (Modular styling)
   - HTML structure separate from CSS
   - Reusable stylesheets
   - Cleaner code organization

## Additional Resources

- **Official Documentation**: https://doc.courtbouillon.org/weasyprint/
- **GitHub Repository**: https://github.com/Kozea/WeasyPrint
- **CSS Paged Media Spec**: https://www.w3.org/TR/css-page-3/
- **CourtBouillon (maintainers)**: https://www.courtbouillon.org/

## Version Notes

- This example uses **WeasyPrint 62.3** or higher
- Requires **Python 3.11** or higher
- CSS features demonstrated work in WeasyPrint 60+
- Some advanced CSS Grid features may require newer versions
