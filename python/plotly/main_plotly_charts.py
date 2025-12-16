#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "plotly>=5.18.0",
#     "pandas>=2.1.0",
#     "numpy>=1.26.0",
#     "statsmodels>=0.14.0",
# ]
# ///
"""
Comprehensive demonstration of Plotly chart types in Python.

This script showcases various Plotly visualization capabilities including:
- Line charts for time series data
- Bar charts for categorical comparisons
- Scatter plots for relationship analysis
- Pie charts for composition visualization
- Heatmaps for correlation matrices
- 3D surface plots for multi-dimensional data
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_line_chart():
    """Create an interactive line chart showing time series data."""
    print("\n" + "=" * 60)
    print("1. LINE CHART - Monthly Sales Trends")
    print("=" * 60)

    # Generate sample data
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='ME')
    sales = [45000, 52000, 48000, 61000, 58000, 72000,
             68000, 75000, 82000, 79000, 88000, 95000]

    df = pd.DataFrame({'Month': dates, 'Sales': sales})

    # Create line chart
    fig = px.line(df, x='Month', y='Sales',
                  title='Monthly Sales Performance 2023',
                  markers=True,
                  labels={'Sales': 'Revenue ($)', 'Month': 'Time Period'})

    fig.update_layout(hovermode='x unified')

    print(f"Created line chart with {len(sales)} data points")
    print(f"Sales range: ${min(sales):,} to ${max(sales):,}")
    print(f"Average monthly sales: ${np.mean(sales):,.2f}")

    # Save to HTML
    fig.write_html("python/plotly/output_line_chart.html")
    print("Saved: output_line_chart.html")


def create_bar_chart():
    """Create a grouped bar chart for category comparisons."""
    print("\n" + "=" * 60)
    print("2. BAR CHART - Product Category Performance")
    print("=" * 60)

    # Sample data
    categories = ['Electronics', 'Clothing', 'Food', 'Home', 'Sports']
    q1_sales = [120000, 85000, 95000, 70000, 60000]
    q2_sales = [135000, 92000, 88000, 75000, 68000]

    fig = go.Figure(data=[
        go.Bar(name='Q1 2023', x=categories, y=q1_sales),
        go.Bar(name='Q2 2023', x=categories, y=q2_sales)
    ])

    fig.update_layout(
        title='Quarterly Sales by Category',
        xaxis_title='Product Category',
        yaxis_title='Revenue ($)',
        barmode='group'
    )

    print(f"Comparing {len(categories)} categories across 2 quarters")
    print(f"Q1 Total: ${sum(q1_sales):,}")
    print(f"Q2 Total: ${sum(q2_sales):,}")
    print(f"Growth: {((sum(q2_sales) - sum(q1_sales)) / sum(q1_sales) * 100):.1f}%")

    fig.write_html("python/plotly/output_bar_chart.html")
    print("Saved: output_bar_chart.html")


def create_scatter_plot():
    """Create a scatter plot showing correlations."""
    print("\n" + "=" * 60)
    print("3. SCATTER PLOT - Marketing Spend vs Revenue")
    print("=" * 60)

    # Generate correlated data
    np.random.seed(42)
    marketing_spend = np.random.uniform(10000, 100000, 50)
    revenue = marketing_spend * 3.5 + np.random.normal(0, 15000, 50)
    categories = np.random.choice(['Digital', 'Print', 'TV'], 50)

    df = pd.DataFrame({
        'Marketing Spend': marketing_spend,
        'Revenue': revenue,
        'Channel': categories
    })

    fig = px.scatter(df, x='Marketing Spend', y='Revenue',
                     color='Channel',
                     title='Marketing ROI Analysis',
                     trendline='ols',
                     labels={'Marketing Spend': 'Marketing Investment ($)',
                            'Revenue': 'Generated Revenue ($)'})

    correlation = np.corrcoef(marketing_spend, revenue)[0, 1]

    print(f"Analyzed {len(df)} campaigns across 3 channels")
    print(f"Correlation coefficient: {correlation:.3f}")
    print(f"Average ROI: {(df['Revenue'].mean() / df['Marketing Spend'].mean()):.2f}x")

    fig.write_html("python/plotly/output_scatter_plot.html")
    print("Saved: output_scatter_plot.html")


def create_pie_chart():
    """Create a pie chart for composition analysis."""
    print("\n" + "=" * 60)
    print("4. PIE CHART - Market Share Distribution")
    print("=" * 60)

    companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Others']
    market_share = [28.5, 22.3, 18.7, 15.2, 15.3]

    fig = go.Figure(data=[go.Pie(
        labels=companies,
        values=market_share,
        hole=0.3,  # Creates a donut chart
        textinfo='label+percent',
        marker=dict(colors=px.colors.qualitative.Set3)
    )])

    fig.update_layout(title='Market Share Analysis 2023')

    print(f"Market distributed among {len(companies)} entities")
    print(f"Market leader: {companies[0]} with {market_share[0]}%")
    print(f"Top 3 companies control: {sum(market_share[:3]):.1f}%")

    fig.write_html("python/plotly/output_pie_chart.html")
    print("Saved: output_pie_chart.html")


def create_heatmap():
    """Create a heatmap for correlation matrix visualization."""
    print("\n" + "=" * 60)
    print("5. HEATMAP - Feature Correlation Matrix")
    print("=" * 60)

    # Generate sample correlation matrix
    np.random.seed(42)
    features = ['Price', 'Quality', 'Marketing', 'Reviews', 'Availability']
    n = len(features)

    # Create a realistic correlation matrix
    correlation_matrix = np.eye(n)
    correlation_matrix[0, 1] = correlation_matrix[1, 0] = 0.72
    correlation_matrix[0, 3] = correlation_matrix[3, 0] = -0.45
    correlation_matrix[1, 3] = correlation_matrix[3, 1] = 0.68
    correlation_matrix[2, 3] = correlation_matrix[3, 2] = 0.55
    correlation_matrix[1, 4] = correlation_matrix[4, 1] = 0.41

    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix,
        x=features,
        y=features,
        colorscale='RdBu',
        zmid=0,
        text=correlation_matrix,
        texttemplate='%{text:.2f}',
        textfont={"size": 10},
        colorbar=dict(title="Correlation")
    ))

    fig.update_layout(
        title='Feature Correlation Heatmap',
        xaxis_title='Features',
        yaxis_title='Features'
    )

    print(f"Analyzing correlations between {n} features")
    print("Strongest positive: Price-Quality (0.72)")
    print("Strongest negative: Price-Reviews (-0.45)")

    fig.write_html("python/plotly/output_heatmap.html")
    print("Saved: output_heatmap.html")


def create_3d_surface():
    """Create a 3D surface plot for multi-dimensional data."""
    print("\n" + "=" * 60)
    print("6. 3D SURFACE PLOT - Revenue Optimization")
    print("=" * 60)

    # Generate 3D surface data
    x = np.linspace(0, 100, 50)  # Marketing budget
    y = np.linspace(0, 50, 50)   # Product quality score
    X, Y = np.meshgrid(x, y)

    # Revenue function (simulated)
    Z = 1000 * np.sqrt(X) * np.log1p(Y) - 0.5 * X + 200 * Y

    fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Viridis')])

    fig.update_layout(
        title='Revenue Surface: Marketing Budget vs Product Quality',
        scene=dict(
            xaxis_title='Marketing Budget ($1000s)',
            yaxis_title='Quality Score',
            zaxis_title='Revenue ($1000s)'
        ),
        autosize=False,
        width=800,
        height=700
    )

    max_revenue_idx = np.unravel_index(Z.argmax(), Z.shape)
    optimal_marketing = X[max_revenue_idx]
    optimal_quality = Y[max_revenue_idx]
    max_revenue = Z[max_revenue_idx]

    print(f"3D surface with {X.shape[0]}x{X.shape[1]} data points")
    print(f"Optimal marketing budget: ${optimal_marketing:.0f}K")
    print(f"Optimal quality score: {optimal_quality:.1f}")
    print(f"Maximum revenue: ${max_revenue:.0f}K")

    fig.write_html("python/plotly/output_3d_surface.html")
    print("Saved: output_3d_surface.html")


def create_subplot_dashboard():
    """Create a dashboard with multiple subplots."""
    print("\n" + "=" * 60)
    print("7. DASHBOARD - Combined Visualizations")
    print("=" * 60)

    # Create subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Daily Traffic', 'Conversion Funnel',
                       'User Engagement', 'Revenue Trend'),
        specs=[[{'type': 'scatter'}, {'type': 'bar'}],
               [{'type': 'scatter'}, {'type': 'scatter'}]]
    )

    # Plot 1: Daily Traffic
    days = list(range(1, 31))
    traffic = [5000 + i * 100 + np.random.randint(-200, 200) for i in days]
    fig.add_trace(
        go.Scatter(x=days, y=traffic, mode='lines+markers', name='Traffic'),
        row=1, col=1
    )

    # Plot 2: Conversion Funnel
    stages = ['Visitors', 'Sign-ups', 'Trials', 'Paid']
    values = [10000, 3500, 1200, 450]
    fig.add_trace(
        go.Bar(x=stages, y=values, name='Funnel'),
        row=1, col=2
    )

    # Plot 3: User Engagement
    hours = list(range(24))
    engagement = [20 + 30 * np.sin((h - 6) * np.pi / 12) + np.random.randint(-5, 5)
                  for h in hours]
    fig.add_trace(
        go.Scatter(x=hours, y=engagement, fill='tozeroy', name='Engagement'),
        row=2, col=1
    )

    # Plot 4: Revenue Trend
    weeks = list(range(1, 13))
    revenue = [50000 * (1.1 ** (w/4)) for w in weeks]
    fig.add_trace(
        go.Scatter(x=weeks, y=revenue, mode='lines', name='Revenue'),
        row=2, col=2
    )

    fig.update_layout(height=800, title_text="Analytics Dashboard", showlegend=False)

    print("Created dashboard with 4 visualization panels")
    print(f"Average daily traffic: {np.mean(traffic):.0f} visitors")
    print(f"Conversion rate: {(values[-1] / values[0] * 100):.1f}%")
    print(f"Peak engagement hour: {hours[np.argmax(engagement)]}:00")

    fig.write_html("python/plotly/output_dashboard.html")
    print("Saved: output_dashboard.html")


def main():
    """Execute all Plotly chart demonstrations."""
    print("\n" + "=" * 60)
    print("PLOTLY CHARTS DEMONSTRATION")
    print("=" * 60)
    print("This program demonstrates various Plotly chart types")
    print("All charts are saved as interactive HTML files")

    # Create all charts
    create_line_chart()          # Line 35-60
    create_bar_chart()           # Line 63-92
    create_scatter_plot()        # Line 95-127
    create_pie_chart()           # Line 130-154
    create_heatmap()             # Line 157-195
    create_3d_surface()          # Line 198-241
    create_subplot_dashboard()   # Line 244-298

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("Created 7 interactive visualizations:")
    print("  • Line Chart: Time series trends")
    print("  • Bar Chart: Category comparisons")
    print("  • Scatter Plot: Correlation analysis")
    print("  • Pie Chart: Composition breakdown")
    print("  • Heatmap: Correlation matrix")
    print("  • 3D Surface: Multi-dimensional optimization")
    print("  • Dashboard: Combined analytics")
    print("\nAll HTML files can be opened in a web browser for interaction")
    print("=" * 60)


if __name__ == "__main__":
    main()
