# OpenPyXL - Excel File Generation with Styles, Charts, and More

This example demonstrates comprehensive Excel file generation using the `openpyxl` library in Python, showcasing various formatting options, formulas, and chart types.

## Requirements

- **Python**: 3.8 or higher
- **Library**: openpyxl >= 3.1.0

The script uses inline metadata for dependency management with `uv`.

## Running the Example

```bash
uv run main_openpyxl.py
```

The script will generate `openpyxl_demo.xlsx` containing 5 worksheets with different demonstrations.

## Program Output

```
============================================================
OpenPyXL Comprehensive Excel Generation Demo
============================================================
Creating 'Font Styles' sheet...
Creating 'Cell Styles' sheet...
Creating 'Data & Formulas' sheet...
Creating 'Charts' sheet...
  Adding Bar Chart...
  Adding Line Chart...
  Adding Pie Chart...
Creating 'Advanced Features' sheet...
============================================================
✓ Excel file created successfully: openpyxl_demo.xlsx
============================================================

Workbook contains the following sheets:
  1. Font Styles
  2. Cell Styles
  3. Data & Formulas
  4. Charts
  5. Advanced Features

Features demonstrated:
  • Font styles (bold, italic, colors, sizes)
  • Cell backgrounds and fills
  • Borders (thin, medium, thick, double, dotted)
  • Text alignment (horizontal & vertical)
  • Number formatting (currency, percentage, date)
  • Formulas (SUM, AVERAGE)
  • Charts (Bar, Line, Pie)
  • Merged cells
  • Text wrapping
  • Column widths and row heights
============================================================
```

**Output Annotation**: The program creates multiple sheets (lines 384-401 in source), each demonstrating different openpyxl capabilities. The console output provides a progress log and summary of features.

## Key Features and Source Code

### 1. Inline Script Metadata (Lines 2-5)

```python
# /// script
# dependencies = [
#   "openpyxl>=3.1.0",
# ]
# ///
```

**Purpose**: Defines dependencies for `uv` to automatically install when running the script.

---

### 2. Font Styling (Lines 43-75, Function: `demo_font_styles`)

```python
# Title with large bold font (Lines 48-52)
ws["A1"] = "Font Styles Demonstration"
ws["A1"].font = Font(name="Arial", size=20, bold=True, color="1F4E78")
ws.merge_cells("A1:D1")
ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

# Different font sizes (Lines 54-58)
ws["A3"] = "Font Sizes:"
ws["A3"].font = Font(bold=True, size=14)
for i, size in enumerate([8, 10, 12, 14, 16, 18, 20], start=4):
    ws[f"A{i}"] = f"Size {size} Font"
    ws[f"A{i}"].font = Font(size=size)

# Font styles (Lines 60-71)
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

# Different colors (Lines 73-79)
colors = [("FF0000", "Red"), ("00FF00", "Green"), ("0000FF", "Blue"),
          ("FF00FF", "Magenta"), ("00FFFF", "Cyan")]
for i, (color, name) in enumerate(colors, start=4):
    ws[f"E{i}"] = name
    ws[f"E{i}"].font = Font(color=color, bold=True, size=12)
```

**Console Output Correlation**: "Creating 'Font Styles' sheet..." (line 1 of output)

**Features Demonstrated**:
- Font properties: `name`, `size`, `bold`, `italic`, `underline`, `strike`, `color`
- Cell merging with `merge_cells()`
- Text alignment with `Alignment(horizontal, vertical)`
- Dynamic cell referencing with f-strings

---

### 3. Cell Backgrounds, Borders, and Alignment (Lines 87-172, Function: `demo_cell_styles`)

```python
# Background fills (Lines 100-115)
fills = [
    ("FFE699", "Yellow Fill"),
    ("C6EFCE", "Green Fill"),
    ("FFC7CE", "Red Fill"),
    ("BDD7EE", "Blue Fill"),
    ("E7E6E6", "Gray Fill")
]
for i, (color, label) in enumerate(fills, start=4):
    cell = ws[f"A{i}"]
    cell.value = label
    cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
    cell.border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin")
    )

# Different border styles (Lines 117-134)
border_styles = [
    ("thin", "Thin Border"),
    ("medium", "Medium Border"),
    ("thick", "Thick Border"),
    ("double", "Double Border"),
    ("dotted", "Dotted Border")
]
for i, (style, label) in enumerate(border_styles, start=4):
    cell = ws[f"C{i}"]
    cell.value = label
    cell.border = Border(
        left=Side(style=style),
        right=Side(style=style),
        top=Side(style=style),
        bottom=Side(style=style)
    )

# Alignment options (Lines 136-155)
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
    ws.row_dimensions[i].height = 30
```

**Console Output Correlation**: "Creating 'Cell Styles' sheet..." (line 2 of output)

**Features Demonstrated**:
- `PatternFill` for background colors (solid fill type)
- `Border` with `Side` for different border styles
- `Alignment` for horizontal and vertical positioning
- Row height adjustment with `row_dimensions[].height`

---

### 4. Data Entry, Formulas, and Number Formatting (Lines 178-252, Function: `demo_data_and_formulas`)

```python
# Sample sales data (Lines 193-199)
products_data = [
    ["Laptop", 15000, 18000, 22000, 25000],
    ["Desktop", 12000, 13500, 14000, 16000],
    ["Tablet", 8000, 9500, 11000, 12500],
    ["Phone", 20000, 22000, 24000, 28000],
    ["Monitor", 5000, 5500, 6000, 7000],
]

# Add data with currency formatting (Lines 201-218)
for row_idx, product_data in enumerate(products_data, start=4):
    ws.cell(row=row_idx, column=1, value=product_data[0])

    # Add quarterly sales with currency format
    for col_idx, value in enumerate(product_data[1:], start=2):
        cell = ws.cell(row=row_idx, column=col_idx, value=value)
        cell.number_format = numbers.FORMAT_CURRENCY_USD_SIMPLE

    # Add Total formula (sum of Q1-Q4) (Lines 220-223)
    total_cell = ws.cell(row=row_idx, column=6, value=f"=SUM(B{row_idx}:E{row_idx})")
    total_cell.number_format = numbers.FORMAT_CURRENCY_USD_SIMPLE
    total_cell.font = Font(bold=True)

    # Add Average formula (Lines 225-227)
    avg_cell = ws.cell(row=row_idx, column=7, value=f"=AVERAGE(B{row_idx}:E{row_idx})")
    avg_cell.number_format = numbers.FORMAT_CURRENCY_USD_SIMPLE

# Grand Total row (Lines 229-242)
ws["A9"] = "Grand Total"
for col_idx in range(2, 7):
    col_letter = get_column_letter(col_idx)
    cell = ws.cell(row=9, column=col_idx, value=f"=SUM({col_letter}4:{col_letter}8)")
    cell.number_format = numbers.FORMAT_CURRENCY_USD_SIMPLE
    cell.font = Font(bold=True)
    cell.border = Border(
        top=Side(style="double"),
        bottom=Side(style="double")
    )
```

**Console Output Correlation**: "Creating 'Data & Formulas' sheet..." (line 3 of output)

**Features Demonstrated**:
- Dynamic cell value assignment with `ws.cell(row, column, value)`
- Excel formulas: `SUM()`, `AVERAGE()`
- Currency formatting with `numbers.FORMAT_CURRENCY_USD_SIMPLE`
- Dynamic formula generation using f-strings
- `get_column_letter()` utility for converting column index to letter

---

### 5. Charts - Bar, Line, and Pie (Lines 258-319, Function: `demo_charts`)

```python
# Bar Chart (Lines 272-285)
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

# Line Chart (Lines 287-299)
line_chart = LineChart()
line_chart.title = "Sales Trend - Top 3 Products"
line_chart.style = 12
line_chart.y_axis.title = "Sales ($)"
line_chart.x_axis.title = "Quarter"

data = Reference(data_ws, min_col=2, min_row=3, max_row=6, max_col=5)
categories = Reference(data_ws, min_col=2, min_row=3, max_col=5)

line_chart.add_data(data, titles_from_data=True, from_rows=False)
line_chart.set_categories(categories)

ws.add_chart(line_chart, "A20")

# Pie Chart (Lines 301-311)
pie_chart = PieChart()
pie_chart.title = "Total Sales Distribution by Product"
pie_chart.style = 10

data = Reference(data_ws, min_col=6, min_row=4, max_row=8)
categories = Reference(data_ws, min_col=1, min_row=4, max_row=8)

pie_chart.add_data(data)
pie_chart.set_categories(categories)

ws.add_chart(pie_chart, "K3")
```

**Console Output Correlation**:
- "Creating 'Charts' sheet..." (line 4 of output)
- "  Adding Bar Chart..." (line 5 of output)
- "  Adding Line Chart..." (line 6 of output)
- "  Adding Pie Chart..." (line 7 of output)

**Features Demonstrated**:
- `BarChart`, `LineChart`, `PieChart` creation
- Chart configuration: `title`, `style`, axis labels
- `Reference` for linking chart data to worksheet ranges
- `add_data()` with `titles_from_data` parameter
- `set_categories()` for chart labels
- Chart sizing with `height` and `width`
- Chart positioning with `add_chart(chart, cell_location)`

---

### 6. Advanced Features - Merged Cells, Text Wrapping, Number Formats (Lines 325-376, Function: `demo_advanced_features`)

```python
# Merged cells (Lines 338-349)
ws.merge_cells("A4:B5")
ws["A4"] = "This is a merged cell spanning 2 columns and 2 rows"
ws["A4"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
ws["A4"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
ws["A4"].border = Border(
    left=Side(style="medium"),
    right=Side(style="medium"),
    top=Side(style="medium"),
    bottom=Side(style="medium")
)

# Wrapped text (Lines 351-361)
ws["A8"] = "This is a long text that will wrap within the cell. " \
           "Text wrapping is useful when you have lengthy content..."
ws["A8"].alignment = Alignment(wrap_text=True, vertical="top")
ws.row_dimensions[8].height = 60
ws.merge_cells("A8:D8")

# Number formatting examples (Lines 363-376)
formats = [
    ("Currency", 1234.56, numbers.FORMAT_CURRENCY_USD_SIMPLE),
    ("Percentage", 0.856, numbers.FORMAT_PERCENTAGE_00),
    ("Date", 45000, numbers.FORMAT_DATE_XLSX14),
    ("Number (2 decimals)", 1234.5678, "0.00"),
    ("Accounting", 9876.54, "_($* #,##0.00_);_($* (#,##0.00);_($* \"-\"??_);_(@_)"),
]

for row_idx, (fmt_type, value, number_format) in enumerate(formats, start=12):
    ws.cell(row=row_idx, column=1, value=fmt_type)
    ws.cell(row=row_idx, column=2, value=value)

    formatted_cell = ws.cell(row=row_idx, column=3, value=value)
    formatted_cell.number_format = number_format
```

**Console Output Correlation**: "Creating 'Advanced Features' sheet..." (line 8 of output)

**Features Demonstrated**:
- Cell merging with `merge_cells(range)`
- Text wrapping with `Alignment(wrap_text=True)`
- Row height adjustment for wrapped text
- Multiple number formats:
  - Currency: `FORMAT_CURRENCY_USD_SIMPLE`
  - Percentage: `FORMAT_PERCENTAGE_00`
  - Date: `FORMAT_DATE_XLSX14`
  - Custom formats: `"0.00"` for decimals
  - Accounting format with custom string

---

### 7. Workbook Management and Saving (Lines 383-427, Function: `main`)

```python
# Create workbook (Line 387)
wb = Workbook()

# Remove default sheet (Lines 389-390)
default_sheet = wb.active
wb.remove(default_sheet)

# Create demonstration sheets (Lines 392-396)
demo_font_styles(wb)
demo_cell_styles(wb)
data_ws = demo_data_and_formulas(wb)
demo_charts(wb, data_ws)
demo_advanced_features(wb)

# Save workbook (Lines 398-399)
output_file = "openpyxl_demo.xlsx"
wb.save(output_file)

# Print summary (Lines 401-427)
print(f"✓ Excel file created successfully: {output_file}")
print("\nWorkbook contains the following sheets:")
for idx, sheet in enumerate(wb.sheetnames, 1):
    print(f"  {idx}. {sheet}")
```

**Console Output Correlation**:
- "✓ Excel file created successfully: openpyxl_demo.xlsx" (line 10 of output)
- Sheet listing (lines 13-17 of output)
- Features summary (lines 19-29 of output)

**Features Demonstrated**:
- `Workbook()` creation
- Removing default sheet with `remove()`
- Passing worksheet references between functions
- Saving with `wb.save(filename)`
- Accessing sheet names with `wb.sheetnames`

---

## Summary

This example demonstrates the full capabilities of openpyxl for generating professional Excel files:

1. **Fonts & Text**: Multiple sizes, styles (bold, italic, underline, strikethrough), and colors
2. **Cell Formatting**: Background fills, various border styles, alignment options
3. **Data & Formulas**: Currency formatting, SUM/AVERAGE formulas, dynamic formula generation
4. **Charts**: Bar, Line, and Pie charts with data references from other sheets
5. **Advanced**: Merged cells, text wrapping, custom number formats
6. **Layout**: Column widths, row heights, sheet management

All features work together to create a comprehensive, multi-sheet Excel workbook suitable for reports, dashboards, and data presentations.
