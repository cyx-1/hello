# Plotly Charts Demonstration

This Python program demonstrates comprehensive data visualization capabilities using Plotly, showcasing 7 different chart types for various analytical needs.

## Requirements

**Python Version:** Python 3.11 or higher
**Key Dependencies:**
- `plotly>=5.18.0` - Interactive visualization library
- `pandas>=2.1.0` - Data manipulation and analysis
- `numpy>=1.26.0` - Numerical computing
- `statsmodels>=0.14.0` - Statistical modeling (for trendline analysis)

## Running the Program

```bash
uv run python main_plotly_charts.py
```

The program generates 7 interactive HTML files that can be opened in any web browser.

## Source Code Overview

### 1. Line Chart - Time Series Visualization (Lines 29-60)

**Purpose:** Display trends over time with monthly sales data

```python
36: dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='ME')
37: sales = [45000, 52000, 48000, 61000, 58000, 72000,
38:          68000, 75000, 82000, 79000, 88000, 95000]
40: df = pd.DataFrame({'Month': dates, 'Sales': sales})
42: fig = px.line(df, x='Month', y='Sales',
43:               title='Monthly Sales Performance 2023',
44:               markers=True,
45:               labels={'Sales': 'Revenue ($)', 'Month': 'Time Period'})
```

**Output:**
```
============================================================
1. LINE CHART - Monthly Sales Trends
============================================================
Created line chart with 12 data points
Sales range: $45,000 to $95,000
Average monthly sales: $68,583.33
Saved: output_line_chart.html
```

**Annotations:**
- Line 36: Uses 'ME' (Month End) frequency for pandas date range (pandas 2.1.0+ requirement)
- Lines 37-38: 12 months of sales data showing upward trend
- Line 42: `px.line()` creates interactive line chart with hover capabilities
- Line 44: `markers=True` adds data points for better visibility

---

### 2. Bar Chart - Category Comparison (Lines 63-92)

**Purpose:** Compare multiple categories across different time periods

```python
70: categories = ['Electronics', 'Clothing', 'Food', 'Home', 'Sports']
71: q1_sales = [120000, 85000, 95000, 70000, 60000]
72: q2_sales = [135000, 92000, 88000, 75000, 68000]
74: fig = go.Figure(data=[
75:     go.Bar(name='Q1 2023', x=categories, y=q1_sales),
76:     go.Bar(name='Q2 2023', x=categories, y=q2_sales)
77: ])
79: fig.update_layout(
80:     title='Quarterly Sales by Category',
81:     xaxis_title='Product Category',
82:     yaxis_title='Revenue ($)',
83:     barmode='group'
84: )
```

**Output:**
```
============================================================
2. BAR CHART - Product Category Performance
============================================================
Comparing 5 categories across 2 quarters
Q1 Total: $430,000
Q2 Total: $458,000
Growth: 6.5%
Saved: output_bar_chart.html
```

**Annotations:**
- Lines 70-72: Sample data for 5 product categories across 2 quarters
- Lines 75-76: Two bar series for side-by-side comparison
- Line 83: `barmode='group'` creates grouped (not stacked) bars
- Growth calculation shows 6.5% quarter-over-quarter improvement

---

### 3. Scatter Plot - Correlation Analysis (Lines 95-127)

**Purpose:** Analyze relationships between two continuous variables with trendline

```python
100: np.random.seed(42)
101: marketing_spend = np.random.uniform(10000, 100000, 50)
102: revenue = marketing_spend * 3.5 + np.random.normal(0, 15000, 50)
103: categories = np.random.choice(['Digital', 'Print', 'TV'], 50)
105: df = pd.DataFrame({
106:     'Marketing Spend': marketing_spend,
107:     'Revenue': revenue,
108:     'Channel': categories
109: })
111: fig = px.scatter(df, x='Marketing Spend', y='Revenue',
112:                  color='Channel',
113:                  title='Marketing ROI Analysis',
114:                  trendline='ols',
115:                  labels={'Marketing Spend': 'Marketing Investment ($)',
116:                         'Revenue': 'Generated Revenue ($)'})
118: correlation = np.corrcoef(marketing_spend, revenue)[0, 1]
```

**Output:**
```
============================================================
3. SCATTER PLOT - Marketing Spend vs Revenue
============================================================
Analyzed 50 campaigns across 3 channels
Correlation coefficient: 0.989
Average ROI: 3.50x
Saved: output_scatter_plot.html
```

**Annotations:**
- Line 100: Random seed ensures reproducible results
- Line 102: Revenue formula creates strong positive correlation (ROI ~3.5x)
- Line 114: `trendline='ols'` adds Ordinary Least Squares regression line (requires statsmodels)
- Line 118: Correlation coefficient 0.989 indicates very strong positive relationship
- Color-coded by channel for multi-dimensional analysis

---

### 4. Pie Chart - Composition Analysis (Lines 130-154)

**Purpose:** Display proportional distribution of market share

```python
137: companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Others']
138: market_share = [28.5, 22.3, 18.7, 15.2, 15.3]
140: fig = go.Figure(data=[go.Pie(
141:     labels=companies,
142:     values=market_share,
143:     hole=0.3,  # Creates a donut chart
144:     textinfo='label+percent',
145:     marker=dict(colors=px.colors.qualitative.Set3)
146: )])
```

**Output:**
```
============================================================
4. PIE CHART - Market Share Distribution
============================================================
Market distributed among 5 entities
Market leader: Company A with 28.5%
Top 3 companies control: 69.5%
Saved: output_pie_chart.html
```

**Annotations:**
- Line 143: `hole=0.3` creates donut chart (0 = full pie, 1 = complete hole)
- Line 144: `textinfo='label+percent'` shows both company names and percentages
- Top 3 companies (69.5%) indicate moderately concentrated market
- Interactive: hover shows exact values and percentages

---

### 5. Heatmap - Correlation Matrix (Lines 157-196)

**Purpose:** Visualize correlations between multiple features

```python
163: features = ['Price', 'Quality', 'Marketing', 'Reviews', 'Availability']
164: n = len(features)
166: # Create a realistic correlation matrix
167: correlation_matrix = np.eye(n)
168: correlation_matrix[0, 1] = correlation_matrix[1, 0] = 0.72
169: correlation_matrix[0, 3] = correlation_matrix[3, 0] = -0.45
170: correlation_matrix[1, 3] = correlation_matrix[3, 1] = 0.68
171: correlation_matrix[2, 3] = correlation_matrix[3, 2] = 0.55
172: correlation_matrix[1, 4] = correlation_matrix[4, 1] = 0.41
174: fig = go.Figure(data=go.Heatmap(
175:     z=correlation_matrix,
176:     x=features,
177:     y=features,
178:     colorscale='RdBu',
179:     zmid=0,
180:     text=correlation_matrix,
181:     texttemplate='%{text:.2f}',
182:     textfont={"size": 10},
183:     colorbar=dict(title="Correlation")
184: ))
```

**Output:**
```
============================================================
5. HEATMAP - Feature Correlation Matrix
============================================================
Analyzing correlations between 5 features
Strongest positive: Price-Quality (0.72)
Strongest negative: Price-Reviews (-0.45)
Saved: output_heatmap.html
```

**Annotations:**
- Line 167: `np.eye(n)` creates identity matrix (diagonal = 1.0 for self-correlation)
- Lines 168-172: Symmetric matrix construction (correlation is bidirectional)
- Line 178: `colorscale='RdBu'` uses Red-Blue diverging scale
- Line 179: `zmid=0` centers the color scale at zero
- Line 181: `texttemplate` formats displayed values to 2 decimal places
- Interpretation: Higher prices correlate with better quality (0.72) but worse reviews (-0.45)

---

### 6. 3D Surface Plot - Multi-dimensional Optimization (Lines 199-241)

**Purpose:** Visualize how two input variables affect an output in 3D space

```python
205: x = np.linspace(0, 100, 50)  # Marketing budget
206: y = np.linspace(0, 50, 50)   # Product quality score
207: X, Y = np.meshgrid(x, y)
209: # Revenue function (simulated)
210: Z = 1000 * np.sqrt(X) * np.log1p(Y) - 0.5 * X + 200 * Y
212: fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Viridis')])
214: fig.update_layout(
215:     title='Revenue Surface: Marketing Budget vs Product Quality',
216:     scene=dict(
217:         xaxis_title='Marketing Budget ($1000s)',
218:         yaxis_title='Quality Score',
219:         zaxis_title='Revenue ($1000s)'
220:     ),
221:     autosize=False,
222:     width=800,
223:     height=700
224: )
226: max_revenue_idx = np.unravel_index(Z.argmax(), Z.shape)
227: optimal_marketing = X[max_revenue_idx]
228: optimal_quality = Y[max_revenue_idx]
229: max_revenue = Z[max_revenue_idx]
```

**Output:**
```
============================================================
6. 3D SURFACE PLOT - Revenue Optimization
============================================================
3D surface with 50x50 data points
Optimal marketing budget: $100K
Optimal quality score: 50.0
Maximum revenue: $49268K
Saved: output_3d_surface.html
```

**Annotations:**
- Line 207: `meshgrid()` creates 2D grid of all (x,y) combinations
- Line 210: Complex revenue function showing diminishing returns on marketing
- Line 212: `go.Surface()` creates 3D surface plot with color gradient
- Lines 226-229: Find optimal point by locating maximum revenue value
- Interactive: Rotate, zoom, and pan the 3D visualization
- Use case: Optimization and sensitivity analysis

---

### 7. Dashboard - Multiple Subplots (Lines 244-297)

**Purpose:** Combine multiple visualizations into a single dashboard

```python
250: fig = make_subplots(
251:     rows=2, cols=2,
252:     subplot_titles=('Daily Traffic', 'Conversion Funnel',
253:                    'User Engagement', 'Revenue Trend'),
254:     specs=[[{'type': 'scatter'}, {'type': 'bar'}],
255:            [{'type': 'scatter'}, {'type': 'scatter'}]]
256: )
258: # Plot 1: Daily Traffic
259: days = list(range(1, 31))
260: traffic = [5000 + i * 100 + np.random.randint(-200, 200) for i in days]
261: fig.add_trace(
262:     go.Scatter(x=days, y=traffic, mode='lines+markers', name='Traffic'),
263:     row=1, col=1
264: )
266: # Plot 2: Conversion Funnel
267: stages = ['Visitors', 'Sign-ups', 'Trials', 'Paid']
268: values = [10000, 3500, 1200, 450]
269: fig.add_trace(
270:     go.Bar(x=stages, y=values, name='Funnel'),
271:     row=1, col=2
272: )
274: # Plot 3: User Engagement
275: hours = list(range(24))
276: engagement = [20 + 30 * np.sin((h - 6) * np.pi / 12) + np.random.randint(-5, 5)
277:               for h in hours]
278: fig.add_trace(
279:     go.Scatter(x=hours, y=engagement, fill='tozeroy', name='Engagement'),
280:     row=2, col=1
281: )
283: # Plot 4: Revenue Trend
284: weeks = list(range(1, 13))
285: revenue = [50000 * (1.1 ** (w/4)) for w in weeks]
286: fig.add_trace(
287:     go.Scatter(x=weeks, y=revenue, mode='lines', name='Revenue'),
288:     row=2, col=2
289: )
291: fig.update_layout(height=800, title_text="Analytics Dashboard", showlegend=False)
```

**Output:**
```
============================================================
7. DASHBOARD - Combined Visualizations
============================================================
Created dashboard with 4 visualization panels
Average daily traffic: 6558 visitors
Conversion rate: 4.5%
Peak engagement hour: 12:00
Saved: output_dashboard.html
```

**Annotations:**
- Line 250: `make_subplots()` creates 2x2 grid layout
- Line 254: `specs` defines chart type for each position
- Lines 261-289: Each `add_trace()` places visualization in specific subplot
- Line 276: Sinusoidal function models daily engagement pattern
- Line 285: Exponential growth formula (10% every 4 weeks)
- Dashboard combines multiple KPIs in single view for comprehensive analysis

---

## Key Features Demonstrated

1. **Interactive Elements:**
   - Hover tooltips with detailed information
   - Zoom and pan capabilities
   - Click legends to show/hide data series
   - 3D rotation and perspective adjustment

2. **Statistical Analysis:**
   - Trendline with OLS regression (scatter plot)
   - Correlation coefficient calculation
   - Optimal value identification (3D surface)

3. **Visual Design:**
   - Color scales (RdBu, Viridis, Set3)
   - Custom labels and titles
   - Grouped and stacked layouts
   - Donut charts with hole parameter

4. **Data Formats:**
   - Time series (line chart)
   - Categorical (bar chart, pie chart)
   - Continuous correlations (scatter plot)
   - Multi-dimensional (3D surface)
   - Matrix data (heatmap)

## Output Files

All visualizations are saved as standalone HTML files in the `python/plotly/` directory:
- `output_line_chart.html`
- `output_bar_chart.html`
- `output_scatter_plot.html`
- `output_pie_chart.html`
- `output_heatmap.html`
- `output_3d_surface.html`
- `output_dashboard.html`

Each file can be opened directly in a web browser without requiring a Python environment or server.

## Version Notes

- **Pandas 2.1.0+:** Required for 'ME' (Month End) frequency in date_range (Line 37)
- **Plotly 5.18.0+:** Provides latest interactive features and performance improvements
- **Statsmodels 0.14.0+:** Required for trendline='ols' in scatter plots (Line 114)
- **NumPy 1.26.0+:** Ensures compatibility with pandas 2.1.0+

This demonstration provides a foundation for building sophisticated data visualizations for business intelligence, scientific computing, and data analysis applications.
