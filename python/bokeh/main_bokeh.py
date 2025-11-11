#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "bokeh>=3.3.0",
#     "numpy>=1.24.0",
#     "pandas>=2.0.0",
# ]
# ///

"""
Bokeh Visualization Demonstration

This script demonstrates various Bokeh visualization capabilities including:
- Interactive scatter plots with hover tooltips
- Line plots with multiple series
- Bar charts with custom styling
- Time series visualization
- Grid layouts for multiple plots
- Custom color palettes and themes
"""

import numpy as np
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category20_20, Viridis256
from bokeh.plotting import figure, output_file, save


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

    # Create figure with tools
    p = figure(
        width=600,
        height=400,
        title="Interactive Scatter Plot with Hover Tooltips",
        tools="pan,wheel_zoom,box_zoom,reset,save"
    )

    # Add scatter renderer
    p.scatter(
        'x', 'y',
        source=source,
        size='sizes',
        color='colors',
        alpha=0.6,
        legend_label="Random Points"
    )

    # Add hover tool
    hover = HoverTool(tooltips=[
        ("Index", "@desc"),
        ("(X,Y)", "(@x{0.00}, @y{0.00})"),
        ("Size", "@sizes")
    ])
    p.add_tools(hover)

    # Customize appearance
    p.legend.location = "top_right"
    p.legend.click_policy = "hide"
    p.xaxis.axis_label = "X Axis"
    p.yaxis.axis_label = "Y Axis"

    print(f"[Line 85] Scatter plot created with {n} points and interactive hover tooltips")
    return p


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

    p = figure(
        width=600,
        height=400,
        title="Trigonometric Functions",
        tools="pan,wheel_zoom,box_zoom,reset,save"
    )

    # Plot multiple lines
    p.line(x, y_sin, legend_label="sin(x)", line_width=2, color="navy", alpha=0.8)
    p.line(x, y_cos, legend_label="cos(x)", line_width=2, color="red", alpha=0.8)
    p.line(x, y_tan, legend_label="tan(x) [clipped]", line_width=2, color="green", alpha=0.8)

    # Customize
    p.legend.location = "top_right"
    p.legend.click_policy = "hide"
    p.xaxis.axis_label = "x (radians)"
    p.yaxis.axis_label = "y"
    p.background_fill_color = "#fafafa"

    print("[Line 122] Line plot created with sin, cos, and tan functions")
    return p


def create_bar_chart():
    """Create a styled bar chart."""
    print("[Line 128] Creating bar chart with sample data...")

    categories = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
    revenue = [45000, 52000, 48000, 63000]
    expenses = [32000, 35000, 31000, 42000]

    # Create figure
    p = figure(
        x_range=categories,
        width=600,
        height=400,
        title="Quarterly Revenue vs Expenses",
        toolbar_location=None,
        tools=""
    )

    # Add bars
    p.vbar(
        x=[i - 0.2 for i in range(len(categories))],
        top=revenue,
        width=0.35,
        legend_label="Revenue",
        color="#1f77b4",
        alpha=0.8
    )

    p.vbar(
        x=[i + 0.2 for i in range(len(categories))],
        top=expenses,
        width=0.35,
        legend_label="Expenses",
        color="#ff7f0e",
        alpha=0.8
    )

    # Customize
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.yaxis.axis_label = "Amount ($)"
    p.y_range.start = 0

    print(f"[Line 170] Bar chart created with {len(categories)} quarters of financial data")
    return p


def create_time_series():
    """Create a time series visualization."""
    print("[Line 176] Creating time series plot with stock-like data...")

    # Generate time series data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    base_price = 100
    prices = base_price + np.cumsum(np.random.randn(len(dates)) * 2)
    volume = np.random.randint(1000000, 5000000, len(dates))

    source = ColumnDataSource(data=dict(
        dates=dates,
        prices=prices,
        volume=volume
    ))

    p = figure(
        width=600,
        height=400,
        title="Stock Price Simulation - 2024",
        x_axis_type="datetime",
        tools="pan,wheel_zoom,box_zoom,reset,save"
    )

    # Price line
    p.line('dates', 'prices', source=source, line_width=2, color='navy', alpha=0.8)

    # Add hover tool
    hover = HoverTool(tooltips=[
        ("Date", "@dates{%F}"),
        ("Price", "$@prices{0.2f}"),
        ("Volume", "@volume{0,0}")
    ], formatters={'@dates': 'datetime'})
    p.add_tools(hover)

    # Customize
    p.xaxis.axis_label = "Date"
    p.yaxis.axis_label = "Price ($)"
    p.background_fill_color = "#f5f5f5"

    print(f"[Line 215] Time series created with {len(dates)} days of simulated stock data")
    return p


def create_heatmap():
    """Create a heatmap visualization."""
    print("[Line 221] Creating heatmap with correlation matrix...")

    # Generate correlation-like data
    categories = ['Feature A', 'Feature B', 'Feature C', 'Feature D', 'Feature E']

    # Create correlation matrix
    x_labels = []
    y_labels = []
    colors_list = []
    correlation_values = []

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

    source = ColumnDataSource(data=dict(
        x=x_labels,
        y=y_labels,
        colors=colors_list,
        correlation=correlation_values
    ))

    p = figure(
        x_range=categories,
        y_range=list(reversed(categories)),
        width=500,
        height=500,
        title="Feature Correlation Heatmap",
        toolbar_location="below",
        tools="hover,save"
    )

    p.rect('x', 'y', width=1, height=1, source=source, color='colors', line_color=None)

    # Add hover tool
    hover = p.select_one(HoverTool)
    hover.tooltips = [("Features", "@x vs @y"), ("Correlation", "@correlation{0.00}")]

    # Customize
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "10px"
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = np.pi / 4

    print(f"[Line 277] Heatmap created with {len(categories)}x{len(categories)} correlation matrix")
    return p


def create_area_chart():
    """Create a stacked area chart."""
    print("[Line 283] Creating stacked area chart...")

    # Generate data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    product_a = [20, 25, 30, 28, 35, 40, 38, 42, 45, 48, 50, 55]
    product_b = [15, 18, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45]
    product_c = [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38]

    p = figure(
        x_range=months,
        width=600,
        height=400,
        title="Monthly Sales by Product",
        toolbar_location="right",
        tools="pan,wheel_zoom,box_zoom,reset,save"
    )

    # Create stacked areas
    p.varea(x=list(range(len(months))), y1=0, y2=product_c, alpha=0.7, color="#3b5b92", legend_label="Product C")

    product_b_stacked = [product_c[i] + product_b[i] for i in range(len(months))]
    p.varea(x=list(range(len(months))), y1=product_c, y2=product_b_stacked, alpha=0.7, color="#e8743b", legend_label="Product B")

    product_a_stacked = [product_b_stacked[i] + product_a[i] for i in range(len(months))]
    p.varea(x=list(range(len(months))), y1=product_b_stacked, y2=product_a_stacked, alpha=0.7, color="#19a974", legend_label="Product A")

    # Customize
    p.xaxis.ticker = list(range(len(months)))
    p.xaxis.major_label_overrides = {i: months[i] for i in range(len(months))}
    p.legend.location = "top_left"
    p.yaxis.axis_label = "Sales (thousands)"

    print(f"[Line 318] Stacked area chart created with {len(months)} months of product sales")
    return p


def main():
    """Main function to create and save all visualizations."""
    print("=" * 70)
    print("BOKEH VISUALIZATION DEMONSTRATION")
    print("=" * 70)
    print()

    print("[Line 327] Starting visualization generation...")
    print()

    # Create all plots
    scatter = create_scatter_plot()
    print()

    line = create_line_plot()
    print()

    bar = create_bar_chart()
    print()

    timeseries = create_time_series()
    print()

    heatmap = create_heatmap()
    print()

    area = create_area_chart()
    print()

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

    print()
    print("=" * 70)
    print("VISUALIZATION COMPLETE")
    print("=" * 70)
    print(f"Output file: {output_filename}")
    print()
    print("Summary:")
    print("  ✓ Interactive scatter plot with 500 points and hover tooltips")
    print("  ✓ Multi-line plot showing trigonometric functions")
    print("  ✓ Grouped bar chart with quarterly financial data")
    print("  ✓ Time series plot with 365 days of simulated stock prices")
    print("  ✓ Heatmap showing 5x5 correlation matrix")
    print("  ✓ Stacked area chart with 12 months of product sales")
    print()
    print(f"Open '{output_filename}' in a web browser to view the interactive visualizations.")
    print("=" * 70)


if __name__ == "__main__":
    main()
