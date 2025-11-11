# Bokeh Visualization Demonstration

This example demonstrates the powerful interactive visualization capabilities of the Bokeh Python library. Bokeh creates interactive, browser-based visualizations that support panning, zooming, and hover tooltips.

## Requirements

- Python >= 3.10
- Bokeh >= 3.3.0

## Running the Example

```bash
uv run main_bokeh.py
```

This will generate an interactive HTML file named `bokeh_visualization_demo.html` containing all visualizations.

## Key Source Code Sections

### 1. Inline Script Metadata (Lines 2-9)

```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "bokeh>=3.3.0",
#     "numpy>=1.24.0",
#     "pandas>=2.0.0",
# ]
# ///
```

**Purpose**: Specifies dependencies using PEP 723 inline script metadata format, allowing `uv` to automatically manage the environment.

---

### 2. Interactive Scatter Plot (Lines 31-86)

```python
def create_scatter_plot():
    """Create an interactive scatter plot with hover tooltips."""
    print("[Line 35] Creating scatter plot with 500 random data points...")

    # Generate random data
    n = 500
    x = np.random.random(n) * 100
    y = np.random.random(n) * 100
    colors = np.random.choice(Category20_20, n)
    sizes = np.random.randint(10, 30, n)

    # Create ColumnDataSource for easier data management
    source = ColumnDataSource(data=dict(
        x=x,
        y=y,
        colors=colors,
        sizes=sizes,
        desc=[f"Point {i+1}" for i in range(n)]
    ))
```

**Key Features**:
- **ColumnDataSource** (Lines 45-52): Central data structure in Bokeh that allows efficient updates and enables data sharing between glyphs
- **HoverTool** (Lines 72-77): Provides interactive tooltips showing data values when hovering over points
- **Interactive Tools** (Line 61): Enables pan, zoom, box selection, and reset functionality

**Output Reference**:
```
[Line 35] Creating scatter plot with 500 random data points...
[Line 85] Scatter plot created with 500 points and interactive hover tooltips
```

---

### 3. Multi-Line Plot with Trigonometric Functions (Lines 89-124)

```python
def create_line_plot():
    """Create a multi-line plot with time series data."""
    print("[Line 91] Creating line plot with trigonometric functions...")

    # Generate data
    x = np.linspace(0, 4 * np.pi, 200)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)
    # Clip tan values for better visualization
    y_tan = np.clip(y_tan, -5, 5)

    # Plot multiple lines
    p.line(x, y_sin, legend_label="sin(x)", line_width=2, color="navy", alpha=0.8)
    p.line(x, y_cos, legend_label="cos(x)", line_width=2, color="red", alpha=0.8)
    p.line(x, y_tan, legend_label="tan(x) [clipped]", line_width=2, color="green", alpha=0.8)
```

**Key Features**:
- **Multiple Line Renderers** (Lines 113-115): Demonstrates plotting multiple series on the same figure
- **Legend Interactivity** (Line 118): `click_policy="hide"` allows clicking legend items to show/hide lines
- **Custom Styling** (Line 120): Background fill color for enhanced appearance

**Output Reference**:
```
[Line 91] Creating line plot with trigonometric functions...
[Line 122] Line plot created with sin, cos, and tan functions
```

---

### 4. Grouped Bar Chart (Lines 126-172)

```python
def create_bar_chart():
    """Create a styled bar chart."""
    print("[Line 128] Creating bar chart with sample data...")

    categories = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
    revenue = [45000, 52000, 48000, 63000]
    expenses = [32000, 35000, 31000, 42000]

    # Add bars
    p.vbar(
        x=[i - 0.2 for i in range(len(categories))],
        top=revenue,
        width=0.35,
        legend_label="Revenue",
        color="#1f77b4",
        alpha=0.8
    )
```

**Key Features**:
- **Grouped Bars** (Lines 147-165): Offset x-positions to create side-by-side bars for comparison
- **Categorical X-axis** (Line 137): Using `x_range` with categories instead of numeric values
- **Grid Customization** (Line 168): Remove vertical grid lines for cleaner appearance

**Output Reference**:
```
[Line 128] Creating bar chart with sample data...
[Line 170] Bar chart created with 4 quarters of financial data
```

---

### 5. Time Series Visualization (Lines 174-217)

```python
def create_time_series():
    """Create a time series visualization."""
    print("[Line 176] Creating time series plot with stock-like data...")

    # Generate time series data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    base_price = 100
    prices = base_price + np.cumsum(np.random.randn(len(dates)) * 2)
    volume = np.random.randint(1000000, 5000000, len(dates))

    p = figure(
        width=600,
        height=400,
        title="Stock Price Simulation - 2024",
        x_axis_type="datetime",
        tools="pan,wheel_zoom,box_zoom,reset,save"
    )
```

**Key Features**:
- **Datetime Axis** (Line 194): `x_axis_type="datetime"` automatically formats dates appropriately
- **Pandas Integration** (Line 181): Using pandas date_range for easy date generation
- **Custom Tooltip Formatting** (Lines 203-207): Using formatters to display dates and currency properly

**Output Reference**:
```
[Line 176] Creating time series plot with stock-like data...
[Line 215] Time series created with 366 days of simulated stock data
```

---

### 6. Correlation Heatmap (Lines 219-279)

```python
def create_heatmap():
    """Create a heatmap visualization."""
    print("[Line 221] Creating heatmap with correlation matrix...")

    categories = ['Feature A', 'Feature B', 'Feature C', 'Feature D', 'Feature E']

    # Create correlation matrix
    for i, cat1 in enumerate(categories):
        for j, cat2 in enumerate(categories):
            x_labels.append(cat1)
            y_labels.append(cat2)
            # Generate correlation-like values
            if i == j:
                corr = 1.0
            else:
                corr = np.random.uniform(0.3, 0.9) if np.random.random() > 0.5 else np.random.uniform(-0.3, 0.3)
            correlation_values.append(corr)
            # Map correlation to color index
            color_idx = int((corr + 1) / 2 * (len(Viridis256) - 1))
            colors_list.append(Viridis256[color_idx])
```

**Key Features**:
- **Rectangle Glyphs** (Line 267): Using `rect()` to create heatmap cells
- **Color Mapping** (Lines 243-245): Mapping correlation values to Viridis color palette
- **Axis Rotation** (Line 276): Rotating x-axis labels for readability

**Output Reference**:
```
[Line 221] Creating heatmap with correlation matrix...
[Line 277] Heatmap created with 5x5 correlation matrix
```

---

### 7. Stacked Area Chart (Lines 281-320)

```python
def create_area_chart():
    """Create a stacked area chart."""
    print("[Line 283] Creating stacked area chart...")

    # Generate data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    product_a = [20, 25, 30, 28, 35, 40, 38, 42, 45, 48, 50, 55]
    product_b = [15, 18, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45]
    product_c = [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38]

    # Create stacked areas
    p.varea(x=list(range(len(months))), y1=0, y2=product_c, alpha=0.7, color="#3b5b92", legend_label="Product C")

    product_b_stacked = [product_c[i] + product_b[i] for i in range(len(months))]
    p.varea(x=list(range(len(months))), y1=product_c, y2=product_b_stacked, alpha=0.7, color="#e8743b", legend_label="Product B")
```

**Key Features**:
- **varea Glyphs** (Lines 302-309): Vertical area charts with y1 and y2 bounds for stacking
- **Cumulative Stacking** (Lines 305, 308): Each area builds on the previous one to show total composition
- **Custom Tick Labels** (Lines 312-313): Mapping numeric indices to month names

**Output Reference**:
```
[Line 283] Creating stacked area chart...
[Line 318] Stacked area chart created with 12 months of product sales
```

---

### 8. Grid Layout and Output (Lines 322-381)

```python
def main():
    """Main function to create and save all visualizations."""
    # Create all plots
    scatter = create_scatter_plot()
    line = create_line_plot()
    bar = create_bar_chart()
    timeseries = create_time_series()
    heatmap = create_heatmap()
    area = create_area_chart()

    # Create grid layout
    print("[Line 349] Arranging plots in grid layout...")
    grid = gridplot(
        [[scatter, line],
         [bar, timeseries],
         [heatmap, area]],
        sizing_mode='fixed',
        toolbar_location='right'
    )

    # Output to file
    output_filename = "bokeh_visualization_demo.html"
    print(f"[Line 360] Saving all visualizations to '{output_filename}'...")
    output_file(output_filename)
    save(grid)
```

**Key Features**:
- **gridplot** (Lines 351-356): Arranges multiple plots in a 3×2 grid layout
- **output_file** (Line 362): Specifies the HTML output file
- **save** (Line 363): Saves all plots to the HTML file

---

## Complete Program Output

```
======================================================================
BOKEH VISUALIZATION DEMONSTRATION
======================================================================

[Line 327] Starting visualization generation...

[Line 35] Creating scatter plot with 500 random data points...
[Line 85] Scatter plot created with 500 points and interactive hover tooltips

[Line 91] Creating line plot with trigonometric functions...
[Line 122] Line plot created with sin, cos, and tan functions

[Line 128] Creating bar chart with sample data...
[Line 170] Bar chart created with 4 quarters of financial data

[Line 176] Creating time series plot with stock-like data...
[Line 215] Time series created with 366 days of simulated stock data

[Line 221] Creating heatmap with correlation matrix...
[Line 277] Heatmap created with 5x5 correlation matrix

[Line 283] Creating stacked area chart...
[Line 318] Stacked area chart created with 12 months of product sales

[Line 349] Arranging plots in grid layout...
[Line 360] Saving all visualizations to 'bokeh_visualization_demo.html'...

======================================================================
VISUALIZATION COMPLETE
======================================================================
Output file: bokeh_visualization_demo.html

Summary:
  ✓ Interactive scatter plot with 500 points and hover tooltips
  ✓ Multi-line plot showing trigonometric functions
  ✓ Grouped bar chart with quarterly financial data
  ✓ Time series plot with 365 days of simulated stock prices
  ✓ Heatmap showing 5x5 correlation matrix
  ✓ Stacked area chart with 12 months of product sales

Open 'bokeh_visualization_demo.html' in a web browser to view the interactive visualizations.
======================================================================
```

## Output-to-Code Correlation

The output demonstrates the execution flow of the program:

1. **Lines 327-349**: Main function initialization and sequential plot creation
2. **Lines 35, 85**: Scatter plot creation with data generation and rendering
3. **Lines 91, 122**: Multi-line plot with three trigonometric functions
4. **Lines 128, 170**: Bar chart with quarterly financial data
5. **Lines 176, 215**: Time series with a full year of daily stock prices
6. **Lines 221, 277**: Heatmap generation with correlation matrix
7. **Lines 283, 318**: Stacked area chart with monthly product sales
8. **Lines 349, 360**: Final grid layout assembly and file output

Each plot function logs its start (at the beginning) and completion (at the end), making it easy to trace execution and debug if needed.

## Bokeh Features Demonstrated

### Interactive Features
- **Pan/Zoom**: All plots support pan and zoom interactions
- **Hover Tooltips**: Scatter plot and time series show detailed data on hover
- **Legend Interactivity**: Clicking legend items toggles visibility of data series
- **Toolbar**: Standard Bokeh toolbar with pan, zoom, reset, and save tools

### Visualization Types
- **Scatter Plot**: Shows relationships between two variables with size and color encoding
- **Line Plot**: Displays continuous data, ideal for functions and trends
- **Bar Chart**: Compares categorical data with grouped bars
- **Time Series**: Specialized for temporal data with datetime axis
- **Heatmap**: Shows correlation/intensity using color gradients
- **Area Chart**: Displays composition over time with stacked areas

### Styling & Customization
- **Color Palettes**: Category20_20 for discrete colors, Viridis256 for continuous gradients
- **Custom Colors**: Hex color codes for precise color control
- **Alpha Transparency**: Creates visual depth and shows overlapping data
- **Background Colors**: Enhanced readability with custom backgrounds
- **Grid Layouts**: Professional multi-plot arrangements

## Version Requirements

This example uses:
- **Bokeh 3.3.0+**: Required for the latest features and stability
- **Python 3.10+**: For modern Python features and type hints
- **NumPy 1.24.0+**: For numerical operations
- **Pandas 2.0.0+**: For date range generation and data handling

## Key Takeaways

1. **ColumnDataSource**: Central to Bokeh's data management, enables efficient updates and tool integration
2. **Interactive by Default**: Bokeh plots are automatically interactive with pan, zoom, and hover capabilities
3. **Browser-Based**: All visualizations render in HTML, requiring no server for static plots
4. **Layout Flexibility**: Multiple plots can be arranged using gridplot, column, or row layouts
5. **Rich Customization**: Extensive styling options for colors, sizes, labels, and themes
6. **Type-Specific Axes**: Special axis types (datetime, categorical) provide appropriate formatting

## Further Exploration

- Explore Bokeh Server for streaming/updating visualizations
- Add selection tools for data filtering
- Use CustomJS for client-side interactions
- Create linked plots with shared data sources
- Build dashboard applications with Bokeh layouts
