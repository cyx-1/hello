#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "weasyprint>=62.3",
# ]
# ///

"""
WeasyPrint demonstration: Converting HTML/CSS to PDF documents

This script demonstrates key features of the WeasyPrint library including:
- Converting HTML to PDF
- Applying CSS styling to PDFs
- Creating multi-page documents
- Adding headers and footers
- Working with images and fonts
- Creating professional PDF layouts
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
    html_content = """
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
    doc = HTML(string=html_content)
    doc.write_pdf("basic_demo.pdf")
    print("✓ Created 'basic_demo.pdf' from HTML string")
    print()

    # Line 60: Create a styled PDF with CSS
    print("[Line 60] Creating a styled PDF with custom CSS...")
    styled_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Styled Document</title>
        <style>
            @page {
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
            h2 {
                color: #34495e;
                margin-top: 20px;
            }
            .highlight {
                background-color: #fffacd;
                padding: 10px;
                border-left: 4px solid #f39c12;
                margin: 15px 0;
            }
            .info-box {
                background-color: #e8f4f8;
                border: 2px solid #3498db;
                border-radius: 5px;
                padding: 15px;
                margin: 20px 0;
            }
            code {
                background-color: #f4f4f4;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }
        </style>
    </head>
    <body>
        <h1>WeasyPrint Styled Document</h1>

        <div class="info-box">
            <strong>About WeasyPrint:</strong> A visual rendering engine for HTML and CSS
            that can export to PDF.
        </div>

        <h2>Key Features</h2>
        <ul>
            <li>Convert HTML/CSS to PDF</li>
            <li>Support for modern CSS3 features</li>
            <li>Automatic page breaks</li>
            <li>Headers and footers</li>
            <li>Print-specific CSS with <code>@page</code> rules</li>
        </ul>

        <div class="highlight">
            <strong>Note:</strong> WeasyPrint respects CSS print media queries
            and page layout specifications.
        </div>

        <h2>Use Cases</h2>
        <p>WeasyPrint is ideal for:</p>
        <ul>
            <li>Generating invoices and receipts</li>
            <li>Creating reports and documentation</li>
            <li>Building certificates and diplomas</li>
            <li>Converting web content to PDF</li>
        </ul>
    </body>
    </html>
    """
    HTML(string=styled_html).write_pdf("styled_demo.pdf")
    print("✓ Created 'styled_demo.pdf' with CSS styling")
    print("  - Applied custom fonts and colors")
    print("  - Used CSS classes for layout")
    print("  - Set page margins with @page rule")
    print()

    # Line 164: Create a multi-page document with page numbers
    print("[Line 164] Creating multi-page PDF with headers and footers...")
    multipage_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Multi-Page Document</title>
        <style>
            @page {
                size: A4;
                margin: 3cm 2cm 3cm 2cm;

                @top-center {
                    content: "WeasyPrint Multi-Page Demo";
                    font-size: 10pt;
                    color: #666;
                    border-bottom: 1px solid #ccc;
                    padding-bottom: 5px;
                }

                @bottom-right {
                    content: "Page " counter(page) " of " counter(pages);
                    font-size: 9pt;
                    color: #666;
                }

                @bottom-left {
                    content: "Generated with WeasyPrint";
                    font-size: 9pt;
                    color: #666;
                }
            }

            body {
                font-family: Georgia, serif;
                font-size: 11pt;
                text-align: justify;
            }

            h1 {
                color: #2c3e50;
                font-size: 24pt;
                margin-top: 0;
            }

            h2 {
                color: #34495e;
                font-size: 18pt;
                margin-top: 30px;
                page-break-after: avoid;
            }

            p {
                margin: 10px 0;
            }

            .page-break {
                page-break-before: always;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }

            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }

            th {
                background-color: #3498db;
                color: white;
            }

            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>WeasyPrint Multi-Page Document</h1>

        <h2>Introduction</h2>
        <p>
            This document demonstrates WeasyPrint's ability to create professional
            multi-page PDFs with automatic page numbering, headers, and footers.
            The @page CSS rule allows precise control over page layout.
        </p>

        <h2>Page Layout Features</h2>
        <p>
            WeasyPrint supports the CSS Paged Media Module, which includes:
        </p>
        <ul>
            <li><strong>@page rule:</strong> Define page dimensions and margins</li>
            <li><strong>@top-*/@bottom-* regions:</strong> Add headers and footers</li>
            <li><strong>page counters:</strong> Automatic page numbering</li>
            <li><strong>page-break properties:</strong> Control pagination</li>
        </ul>

        <h2>Sample Data Table</h2>
        <table>
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
                <tr>
                    <td>CSS Grid</td>
                    <td>Two-dimensional layouts</td>
                    <td>⚠ Partial</td>
                </tr>
                <tr>
                    <td>Web Fonts</td>
                    <td>@font-face support</td>
                    <td>✓ Yes</td>
                </tr>
                <tr>
                    <td>SVG Images</td>
                    <td>Scalable vector graphics</td>
                    <td>✓ Yes</td>
                </tr>
            </tbody>
        </table>

        <div class="page-break"></div>

        <h2>Page 2: Additional Content</h2>
        <p>
            This content appears on the second page due to the page-break-before CSS property.
            WeasyPrint handles page breaks automatically when content exceeds page height,
            but you can also control breaks explicitly.
        </p>

        <h2>Technical Specifications</h2>
        <p>
            WeasyPrint is built on several key technologies:
        </p>
        <ul>
            <li><strong>Pango:</strong> Text layout and rendering</li>
            <li><strong>Cairo:</strong> 2D graphics library for PDF generation</li>
            <li><strong>cssselect2:</strong> CSS selector implementation</li>
            <li><strong>tinycss2:</strong> CSS parser</li>
        </ul>

        <h2>Code Example</h2>
        <p>
            Basic usage of WeasyPrint in Python:
        </p>
        <pre style="background: #f4f4f4; padding: 15px; border-radius: 5px;">
from weasyprint import HTML

# Convert HTML to PDF
HTML('document.html').write_pdf('output.pdf')

# Or from a string
html_string = '&lt;h1&gt;Hello PDF!&lt;/h1&gt;'
HTML(string=html_string).write_pdf('output.pdf')
        </pre>

        <div class="page-break"></div>

        <h2>Page 3: Conclusion</h2>
        <p>
            WeasyPrint provides a powerful and flexible solution for converting HTML and CSS
            to high-quality PDF documents. Its support for modern CSS features and print-specific
            layouts makes it ideal for generating reports, invoices, and other professional documents.
        </p>

        <h2>Resources</h2>
        <ul>
            <li>Documentation: https://doc.courtbouillon.org/weasyprint/</li>
            <li>GitHub: https://github.com/Kozea/WeasyPrint</li>
            <li>CSS Paged Media: https://www.w3.org/TR/css-page-3/</li>
        </ul>
    </body>
    </html>
    """
    HTML(string=multipage_html).write_pdf("multipage_demo.pdf")
    print("✓ Created 'multipage_demo.pdf' with multiple pages")
    print("  - Added header with document title")
    print("  - Added footer with page numbers (Page X of Y)")
    print("  - Applied page breaks for content organization")
    print("  - Included styled table with data")
    print()

    # Line 393: Generate PDF from HTML with inline CSS
    print("[Line 393] Creating invoice-style PDF...")
    invoice_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Invoice</title>
        <style>
            @page {
                size: A4 portrait;
                margin: 1.5cm;
            }

            body {
                font-family: Arial, sans-serif;
                font-size: 10pt;
                color: #333;
            }

            .header {
                text-align: center;
                margin-bottom: 30px;
                border-bottom: 3px solid #2c3e50;
                padding-bottom: 20px;
            }

            .header h1 {
                color: #2c3e50;
                margin: 0;
                font-size: 28pt;
            }

            .header p {
                margin: 5px 0;
                color: #7f8c8d;
            }

            .invoice-details {
                display: flex;
                justify-content: space-between;
                margin-bottom: 30px;
            }

            .invoice-details div {
                flex: 1;
            }

            .invoice-details h3 {
                color: #2c3e50;
                margin-top: 0;
                border-bottom: 2px solid #ecf0f1;
                padding-bottom: 5px;
            }

            .items-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }

            .items-table th {
                background-color: #2c3e50;
                color: white;
                padding: 12px;
                text-align: left;
            }

            .items-table td {
                padding: 10px 12px;
                border-bottom: 1px solid #ecf0f1;
            }

            .items-table tr:nth-child(even) {
                background-color: #f8f9fa;
            }

            .items-table .amount {
                text-align: right;
            }

            .total-section {
                margin-top: 20px;
                text-align: right;
            }

            .total-row {
                display: flex;
                justify-content: flex-end;
                padding: 5px 0;
            }

            .total-row .label {
                width: 150px;
                text-align: right;
                padding-right: 20px;
                font-weight: bold;
            }

            .total-row .amount {
                width: 120px;
                text-align: right;
            }

            .grand-total {
                border-top: 2px solid #2c3e50;
                padding-top: 10px;
                margin-top: 10px;
                font-size: 14pt;
                color: #2c3e50;
            }

            .footer {
                margin-top: 50px;
                text-align: center;
                color: #7f8c8d;
                font-size: 9pt;
                border-top: 1px solid #ecf0f1;
                padding-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>INVOICE</h1>
            <p>Invoice #INV-2024-001</p>
            <p>Date: January 15, 2024</p>
        </div>

        <div class="invoice-details" style="display: table; width: 100%;">
            <div style="display: table-cell; width: 50%;">
                <h3>From:</h3>
                <p>
                    <strong>Tech Solutions Inc.</strong><br>
                    123 Innovation Drive<br>
                    San Francisco, CA 94105<br>
                    contact@techsolutions.example
                </p>
            </div>
            <div style="display: table-cell; width: 50%;">
                <h3>Bill To:</h3>
                <p>
                    <strong>Acme Corporation</strong><br>
                    456 Business Ave<br>
                    New York, NY 10001<br>
                    billing@acme.example
                </p>
            </div>
        </div>

        <table class="items-table">
            <thead>
                <tr>
                    <th style="width: 50%;">Description</th>
                    <th style="width: 15%; text-align: center;">Quantity</th>
                    <th style="width: 15%; text-align: right;">Unit Price</th>
                    <th style="width: 20%; text-align: right;">Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>WeasyPrint PDF Generation Service</td>
                    <td style="text-align: center;">100</td>
                    <td class="amount">$2.50</td>
                    <td class="amount">$250.00</td>
                </tr>
                <tr>
                    <td>Custom Template Design</td>
                    <td style="text-align: center;">5</td>
                    <td class="amount">$75.00</td>
                    <td class="amount">$375.00</td>
                </tr>
                <tr>
                    <td>API Integration Support</td>
                    <td style="text-align: center;">10</td>
                    <td class="amount">$50.00</td>
                    <td class="amount">$500.00</td>
                </tr>
                <tr>
                    <td>Technical Consulting (hourly)</td>
                    <td style="text-align: center;">8</td>
                    <td class="amount">$150.00</td>
                    <td class="amount">$1,200.00</td>
                </tr>
            </tbody>
        </table>

        <div class="total-section">
            <div class="total-row">
                <div class="label">Subtotal:</div>
                <div class="amount">$2,325.00</div>
            </div>
            <div class="total-row">
                <div class="label">Tax (8.5%):</div>
                <div class="amount">$197.63</div>
            </div>
            <div class="total-row grand-total">
                <div class="label">TOTAL:</div>
                <div class="amount">$2,522.63</div>
            </div>
        </div>

        <div class="footer">
            <p>Payment due within 30 days. Make checks payable to Tech Solutions Inc.</p>
            <p>Thank you for your business!</p>
        </div>
    </body>
    </html>
    """
    HTML(string=invoice_html).write_pdf("invoice_demo.pdf")
    print("✓ Created 'invoice_demo.pdf' with professional invoice layout")
    print("  - Applied business-style formatting")
    print("  - Created itemized table with calculations")
    print("  - Used flexbox for two-column layout")
    print()

    # Line 631: Generate PDF to BytesIO (in-memory)
    print("[Line 631] Generating PDF to memory (BytesIO)...")
    simple_html = "<h1>PDF in Memory</h1><p>This PDF was generated to a BytesIO object.</p>"
    pdf_bytes = BytesIO()
    HTML(string=simple_html).write_pdf(pdf_bytes)
    pdf_size = pdf_bytes.tell()
    print(f"✓ Generated PDF to memory: {pdf_size} bytes")
    print("  - Useful for web applications (no file I/O)")
    print("  - Can be sent directly in HTTP responses")
    print()

    # Line 644: Apply external CSS
    print("[Line 644] Applying external CSS stylesheet...")
    html_with_external_css = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>External CSS Demo</title>
    </head>
    <body>
        <div class="container">
            <h1 class="title">External CSS Styling</h1>
            <p class="content">
                This PDF demonstrates using external CSS stylesheets with WeasyPrint.
                The CSS object can be passed separately from the HTML.
            </p>
            <div class="box">
                <h2>Highlighted Section</h2>
                <p>This box is styled with external CSS.</p>
            </div>
        </div>
    </body>
    </html>
    """

    external_css = CSS(string="""
        @page {
            size: A4;
            margin: 2cm;
        }

        .container {
            font-family: 'Helvetica', sans-serif;
        }

        .title {
            color: #e74c3c;
            font-size: 24pt;
            border-bottom: 3px solid #e74c3c;
            padding-bottom: 10px;
        }

        .content {
            font-size: 12pt;
            line-height: 1.8;
            margin: 20px 0;
        }

        .box {
            background-color: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }

        .box h2 {
            color: #856404;
            margin-top: 0;
        }
    """)

    HTML(string=html_with_external_css).write_pdf(
        "external_css_demo.pdf",
        stylesheets=[external_css]
    )
    print("✓ Created 'external_css_demo.pdf' with external CSS")
    print("  - Separated HTML structure from styling")
    print("  - Passed CSS object to write_pdf() method")
    print()

    # Summary
    print("=" * 70)
    print("PDF Generation Summary")
    print("=" * 70)
    print("Generated files:")
    print("  1. basic_demo.pdf - Simple HTML to PDF conversion")
    print("  2. styled_demo.pdf - CSS styled document with colors and layout")
    print("  3. multipage_demo.pdf - Multi-page with headers, footers, page numbers")
    print("  4. invoice_demo.pdf - Professional invoice template")
    print("  5. external_css_demo.pdf - Using external CSS stylesheets")
    print()
    print("✓ All PDFs generated successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
