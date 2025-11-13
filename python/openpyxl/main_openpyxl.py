#!/usr/bin/env python3
# /// script
# dependencies = [
#   "openpyxl>=3.1.0",
# ]
# ///

"""
Comprehensive demonstration of openpyxl features for Excel file generation.
This script showcases fonts, styles, charts, formulas, and more.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, numbers
from openpyxl.chart import BarChart, LineChart, PieChart, Reference
from openpyxl.utils import get_column_letter


def create_styled_header(ws, row, headers, fill_color="4472C4"):
    """Create a styled header row with formatting."""
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num, value=header)
        cell.font = Font(bold=True, color="FFFFFF", size=12)
        cell.fill = PatternFill(
            start_color=fill_color, end_color=fill_color, fill_type="solid"
        )
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = Border(
            left=Side(style="thin"),
            right=Side(style="thin"),
            top=Side(style="thin"),
            bottom=Side(style="thin"),
        )


def demo_font_styles(wb):
    """Demonstrate various font styles and formatting."""
    print("Creating 'Font Styles' sheet...")
    ws = wb.create_sheet("Font Styles", 0)

    # Title with large bold font
    ws["A1"] = "Font Styles Demonstration"
    ws["A1"].font = Font(name="Arial", size=20, bold=True, color="1F4E78")
    ws.merge_cells("A1:D1")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

    # Different font sizes
    ws["A3"] = "Font Sizes:"
    ws["A3"].font = Font(bold=True, size=14)
    for i, size in enumerate([8, 10, 12, 14, 16, 18, 20], start=4):
        ws[f"A{i}"] = f"Size {size} Font"
        ws[f"A{i}"].font = Font(size=size)

    # Font styles
    ws["C3"] = "Font Styles:"
    ws["C3"].font = Font(bold=True, size=14)
    ws["C4"] = "Bold Text"
    ws["C4"].font = Font(bold=True)
    ws["C5"] = "Italic Text"
    ws["C5"].font = Font(italic=True)
    ws["C6"] = "Bold Italic"
    ws["C6"].font = Font(bold=True, italic=True)
    ws["C7"] = "Underlined Text"
    ws["C7"].font = Font(underline="single")
    ws["C8"] = "Strikethrough Text"
    ws["C8"].font = Font(strike=True)

    # Different colors
    ws["E3"] = "Font Colors:"
    ws["E3"].font = Font(bold=True, size=14)
    colors = [
        ("FF0000", "Red"),
        ("00FF00", "Green"),
        ("0000FF", "Blue"),
        ("FF00FF", "Magenta"),
        ("00FFFF", "Cyan"),
    ]
    for i, (color, name) in enumerate(colors, start=4):
        ws[f"E{i}"] = name
        ws[f"E{i}"].font = Font(color=color, bold=True, size=12)

    # Set column widths
    for col in ["A", "C", "E"]:
        ws.column_dimensions[col].width = 20


def demo_cell_styles(wb):
    """Demonstrate cell backgrounds, borders, and alignment."""
    print("Creating 'Cell Styles' sheet...")
    ws = wb.create_sheet("Cell Styles")

    # Title
    ws["A1"] = "Cell Styles Demonstration"
    ws["A1"].font = Font(size=18, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill(
        start_color="4472C4", end_color="4472C4", fill_type="solid"
    )
    ws.merge_cells("A1:F1")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 30

    # Background fills
    ws["A3"] = "Background Fills:"
    ws["A3"].font = Font(bold=True, size=12)
    fills = [
        ("FFE699", "Yellow Fill"),
        ("C6EFCE", "Green Fill"),
        ("FFC7CE", "Red Fill"),
        ("BDD7EE", "Blue Fill"),
        ("E7E6E6", "Gray Fill"),
    ]
    for i, (color, label) in enumerate(fills, start=4):
        cell = ws[f"A{i}"]
        cell.value = label
        cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
        cell.border = Border(
            left=Side(style="thin"),
            right=Side(style="thin"),
            top=Side(style="thin"),
            bottom=Side(style="thin"),
        )

    # Different border styles
    ws["C3"] = "Border Styles:"
    ws["C3"].font = Font(bold=True, size=12)
    border_styles = [
        ("thin", "Thin Border"),
        ("medium", "Medium Border"),
        ("thick", "Thick Border"),
        ("double", "Double Border"),
        ("dotted", "Dotted Border"),
    ]
    for i, (style, label) in enumerate(border_styles, start=4):
        cell = ws[f"C{i}"]
        cell.value = label
        cell.border = Border(
            left=Side(style=style),
            right=Side(style=style),
            top=Side(style=style),
            bottom=Side(style=style),
        )
        cell.alignment = Alignment(horizontal="center")

    # Alignment options
    ws["E3"] = "Alignment Options:"
    ws["E3"].font = Font(bold=True, size=12)
    ws.merge_cells("E3:F3")

    alignments = [
        ("left", "top", "Left-Top"),
        ("center", "center", "Center-Center"),
        ("right", "bottom", "Right-Bottom"),
        ("center", "top", "Center-Top"),
    ]
    for i, (h_align, v_align, label) in enumerate(alignments, start=4):
        cell = ws[f"E{i}"]
        cell.value = label
        cell.alignment = Alignment(horizontal=h_align, vertical=v_align)
        cell.border = Border(
            left=Side(style="thin"),
            right=Side(style="thin"),
            top=Side(style="thin"),
            bottom=Side(style="thin"),
        )
        ws.row_dimensions[i].height = 30
        ws.merge_cells(f"E{i}:F{i}")

    # Set column widths
    for col in ["A", "C", "E"]:
        ws.column_dimensions[col].width = 20
    ws.column_dimensions["F"].width = 5


def demo_data_and_formulas(wb):
    """Demonstrate data entry, formulas, and number formatting."""
    print("Creating 'Data & Formulas' sheet...")
    ws = wb.create_sheet("Data & Formulas")

    # Title
    ws["A1"] = "Sales Data with Formulas"
    ws["A1"].font = Font(size=16, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill(
        start_color="4472C4", end_color="4472C4", fill_type="solid"
    )
    ws.merge_cells("A1:E1")
    ws["A1"].alignment = Alignment(horizontal="center")

    # Headers
    headers = [
        "Product",
        "Q1 Sales",
        "Q2 Sales",
        "Q3 Sales",
        "Q4 Sales",
        "Total",
        "Average",
    ]
    create_styled_header(ws, 3, headers)

    # Sample data
    products_data = [
        ["Laptop", 15000, 18000, 22000, 25000],
        ["Desktop", 12000, 13500, 14000, 16000],
        ["Tablet", 8000, 9500, 11000, 12500],
        ["Phone", 20000, 22000, 24000, 28000],
        ["Monitor", 5000, 5500, 6000, 7000],
    ]

    # Add data with currency formatting
    for row_idx, product_data in enumerate(products_data, start=4):
        ws.cell(row=row_idx, column=1, value=product_data[0])

        # Add quarterly sales with currency format
        for col_idx, value in enumerate(product_data[1:], start=2):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.number_format = numbers.FORMAT_CURRENCY_USD_SIMPLE
            cell.border = Border(
                left=Side(style="thin"),
                right=Side(style="thin"),
                top=Side(style="thin"),
                bottom=Side(style="thin"),
            )

        # Add Total formula (sum of Q1-Q4)
        total_cell = ws.cell(
            row=row_idx, column=6, value=f"=SUM(B{row_idx}:E{row_idx})"
        )
        total_cell.number_format = numbers.FORMAT_CURRENCY_USD_SIMPLE
        total_cell.font = Font(bold=True)
        total_cell.fill = PatternFill(
            start_color="E7E6E6", end_color="E7E6E6", fill_type="solid"
        )

        # Add Average formula
        avg_cell = ws.cell(
            row=row_idx, column=7, value=f"=AVERAGE(B{row_idx}:E{row_idx})"
        )
        avg_cell.number_format = numbers.FORMAT_CURRENCY_USD_SIMPLE
        avg_cell.fill = PatternFill(
            start_color="BDD7EE", end_color="BDD7EE", fill_type="solid"
        )

    # Add Grand Total row
    ws["A9"] = "Grand Total"
    ws["A9"].font = Font(bold=True, size=12)
    ws["A9"].fill = PatternFill(
        start_color="FFE699", end_color="FFE699", fill_type="solid"
    )

    for col_idx in range(2, 7):
        col_letter = get_column_letter(col_idx)
        cell = ws.cell(
            row=9, column=col_idx, value=f"=SUM({col_letter}4:{col_letter}8)"
        )
        cell.number_format = numbers.FORMAT_CURRENCY_USD_SIMPLE
        cell.font = Font(bold=True)
        cell.fill = PatternFill(
            start_color="FFE699", end_color="FFE699", fill_type="solid"
        )
        cell.border = Border(top=Side(style="double"), bottom=Side(style="double"))

    # Set column widths
    ws.column_dimensions["A"].width = 15
    for col in ["B", "C", "D", "E", "F", "G"]:
        ws.column_dimensions[col].width = 12

    return ws


def demo_charts(wb, data_ws):
    """Demonstrate various chart types."""
    print("Creating 'Charts' sheet...")
    ws = wb.create_sheet("Charts")

    # Title
    ws["A1"] = "Chart Demonstrations"
    ws["A1"].font = Font(size=18, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill(
        start_color="4472C4", end_color="4472C4", fill_type="solid"
    )
    ws.merge_cells("A1:H1")
    ws["A1"].alignment = Alignment(horizontal="center")

    # Bar Chart - Quarterly Sales by Product
    print("  Adding Bar Chart...")
    bar_chart = BarChart()
    bar_chart.title = "Quarterly Sales by Product"
    bar_chart.style = 10
    bar_chart.y_axis.title = "Sales ($)"
    bar_chart.x_axis.title = "Products"

    # Data for bar chart from Data & Formulas sheet
    data = Reference(data_ws, min_col=2, min_row=3, max_row=8, max_col=5)
    categories = Reference(data_ws, min_col=1, min_row=4, max_row=8)

    bar_chart.add_data(data, titles_from_data=True)
    bar_chart.set_categories(categories)
    bar_chart.height = 10
    bar_chart.width = 20

    ws.add_chart(bar_chart, "A3")

    # Line Chart - Trend over quarters for top 3 products
    print("  Adding Line Chart...")
    line_chart = LineChart()
    line_chart.title = "Sales Trend - Top 3 Products"
    line_chart.style = 12
    line_chart.y_axis.title = "Sales ($)"
    line_chart.x_axis.title = "Quarter"

    data = Reference(data_ws, min_col=2, min_row=3, max_row=6, max_col=5)
    categories = Reference(data_ws, min_col=2, min_row=3, max_col=5)

    line_chart.add_data(data, titles_from_data=True, from_rows=False)
    line_chart.set_categories(categories)
    line_chart.height = 10
    line_chart.width = 20

    ws.add_chart(line_chart, "A20")

    # Pie Chart - Total sales by product
    print("  Adding Pie Chart...")
    pie_chart = PieChart()
    pie_chart.title = "Total Sales Distribution by Product"
    pie_chart.style = 10

    data = Reference(data_ws, min_col=6, min_row=4, max_row=8)
    categories = Reference(data_ws, min_col=1, min_row=4, max_row=8)

    pie_chart.add_data(data)
    pie_chart.set_categories(categories)
    pie_chart.height = 10
    pie_chart.width = 15

    ws.add_chart(pie_chart, "K3")


def demo_advanced_features(wb):
    """Demonstrate merged cells, wrapped text, and conditional formatting."""
    print("Creating 'Advanced Features' sheet...")
    ws = wb.create_sheet("Advanced Features")

    # Title
    ws["A1"] = "Advanced Features"
    ws["A1"].font = Font(size=18, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill(
        start_color="4472C4", end_color="4472C4", fill_type="solid"
    )
    ws.merge_cells("A1:D1")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 30

    # Merged cells example
    ws["A3"] = "Merged Cells Example:"
    ws["A3"].font = Font(bold=True, size=12)

    ws.merge_cells("A4:B5")
    ws["A4"] = "This is a merged cell spanning 2 columns and 2 rows"
    ws["A4"].alignment = Alignment(
        horizontal="center", vertical="center", wrap_text=True
    )
    ws["A4"].fill = PatternFill(
        start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"
    )
    ws["A4"].border = Border(
        left=Side(style="medium"),
        right=Side(style="medium"),
        top=Side(style="medium"),
        bottom=Side(style="medium"),
    )

    # Wrapped text example
    ws["A7"] = "Text Wrapping:"
    ws["A7"].font = Font(bold=True, size=12)

    ws["A8"] = (
        "This is a long text that will wrap within the cell. "
        "Text wrapping is useful when you have lengthy content that needs to be visible without expanding the column width."
    )
    ws["A8"].alignment = Alignment(wrap_text=True, vertical="top")
    ws["A8"].border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )
    ws.row_dimensions[8].height = 60
    ws.merge_cells("A8:D8")

    # Number formatting examples
    ws["A10"] = "Number Formatting:"
    ws["A10"].font = Font(bold=True, size=12)

    headers = ["Format Type", "Value", "Formatted Result"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=11, column=col_num, value=header)
        cell.font = Font(bold=True)
        cell.fill = PatternFill(
            start_color="BDD7EE", end_color="BDD7EE", fill_type="solid"
        )

    formats = [
        ("Currency", 1234.56, numbers.FORMAT_CURRENCY_USD_SIMPLE),
        ("Percentage", 0.856, numbers.FORMAT_PERCENTAGE_00),
        ("Date", 45000, numbers.FORMAT_DATE_XLSX14),
        ("Number (2 decimals)", 1234.5678, "0.00"),
        ("Accounting", 9876.54, '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'),
    ]

    for row_idx, (fmt_type, value, number_format) in enumerate(formats, start=12):
        ws.cell(row=row_idx, column=1, value=fmt_type)
        ws.cell(row=row_idx, column=2, value=value)

        formatted_cell = ws.cell(row=row_idx, column=3, value=value)
        formatted_cell.number_format = number_format
        formatted_cell.fill = PatternFill(
            start_color="E7E6E6", end_color="E7E6E6", fill_type="solid"
        )

    # Set column widths
    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 15
    ws.column_dimensions["C"].width = 20
    ws.column_dimensions["D"].width = 15


def main():
    """Main function to create comprehensive Excel workbook."""
    print("=" * 60)
    print("OpenPyXL Comprehensive Excel Generation Demo")
    print("=" * 60)

    # Create workbook
    wb = Workbook()

    # Remove default sheet
    default_sheet = wb.active
    wb.remove(default_sheet)

    # Create demonstration sheets
    demo_font_styles(wb)
    demo_cell_styles(wb)
    data_ws = demo_data_and_formulas(wb)
    demo_charts(wb, data_ws)
    demo_advanced_features(wb)

    # Save workbook
    output_file = "openpyxl_demo.xlsx"
    wb.save(output_file)

    print("=" * 60)
    print(f"✓ Excel file created successfully: {output_file}")
    print("=" * 60)
    print("\nWorkbook contains the following sheets:")
    for idx, sheet in enumerate(wb.sheetnames, 1):
        print(f"  {idx}. {sheet}")

    print("\nFeatures demonstrated:")
    print("  • Font styles (bold, italic, colors, sizes)")
    print("  • Cell backgrounds and fills")
    print("  • Borders (thin, medium, thick, double, dotted)")
    print("  • Text alignment (horizontal & vertical)")
    print("  • Number formatting (currency, percentage, date)")
    print("  • Formulas (SUM, AVERAGE)")
    print("  • Charts (Bar, Line, Pie)")
    print("  • Merged cells")
    print("  • Text wrapping")
    print("  • Column widths and row heights")
    print("=" * 60)


if __name__ == "__main__":
    main()
