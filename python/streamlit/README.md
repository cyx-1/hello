# Streamlit Example: Building Interactive Web Applications

This example demonstrates how to build interactive web applications with Python using Streamlit, a powerful framework for creating data apps.

## Key Concepts Illustrated

1. **Text Elements** - Display formatted text, markdown, and code
2. **Interactive Widgets** - Text inputs, sliders, buttons, selectors
3. **Layout Components** - Columns, tabs, expanders, containers, sidebar
4. **Data Visualization** - Charts and graphs
5. **Session State** - Maintaining state across interactions
6. **Data Display** - Tables, metrics, and JSON

## Running the Example

```bash
uv run streamlit run main_streamlit.py
```

This will start a local web server (typically at `http://localhost:8501`) and open the app in your browser.

## Source Code Analysis

### 1. Page Configuration

**Source Code (main_streamlit.py:18-23):**
```python
st.set_page_config(
    page_title="Streamlit Demo",    # Line 19: Browser tab title
    page_icon="🚀",                  # Line 20: Browser tab icon
    layout="wide",                   # Line 21: Use full width
    initial_sidebar_state="expanded",# Line 22: Show sidebar by default
)
```

**Effect:**
- **Line 19:** Sets the browser tab title to "Streamlit Demo"
- **Line 20:** Displays a rocket emoji 🚀 in the browser tab
- **Line 21:** Uses wide layout mode (content spans full width)
- **Line 22:** Sidebar is expanded by default when the app loads

**💡 Key Insight:** `st.set_page_config()` must be the first Streamlit command, before any other `st` calls.

---

### 2. Session State Management

**Source Code (main_streamlit.py:27-31):**
```python
if "counter" not in st.session_state:      # Line 27: Check if key exists
    st.session_state.counter = 0           # Line 28: Initialize counter
if "messages" not in st.session_state:     # Line 29: Check messages
    st.session_state.messages = []         # Line 30: Initialize list
```

**Effect:**
- **Lines 27-28:** Initialize `counter` to 0 on first run
- **Lines 29-30:** Initialize empty `messages` list on first run
- Session state persists across reruns (button clicks, widget changes)

**💡 Key Insight:** Session state allows your app to remember values across interactions. Without it, variables would reset to their initial values on every interaction.

---

### 3. Text Elements and Formatting

**Source Code (main_streamlit.py:40-51):**
```python
st.header("1️⃣ Text Elements")                # Line 40: Large heading
st.write("Streamlit supports various...")    # Line 41: Regular text
st.markdown("""
- **Bold text** and *italic text*            # Line 43: Markdown formatting
- `Code snippets`                            # Line 44: Inline code
- [Links](https://streamlit.io)              # Line 45: Hyperlinks
""")
st.code("""
st.write("Hello World")                      # Line 48: Display code block
st.markdown("**Bold** text")                 # Line 49: with syntax highlighting
st.code("print('Code block')")               # Line 50
""", language="python")                      # Line 51: Specify language
```

**Visual Output:**
```
1️⃣ Text Elements
Streamlit supports various text formatting options:
• Bold text and italic text
• Code snippets
• Links

[Python code block with syntax highlighting showing examples]
```

**💡 Key Insight:** Streamlit supports multiple text rendering methods:
- `st.write()` - Universal write function
- `st.markdown()` - Full markdown support
- `st.code()` - Syntax-highlighted code blocks

---

### 4. Interactive Widgets - Input Controls

**Source Code (main_streamlit.py:60-74):**
```python
# Text input
name = st.text_input("Enter your name:",     # Line 61: Create text input
                     placeholder="John Doe") # Line 61: Placeholder text
if name:                                     # Line 62: Check if user entered text
    st.success(f"Hello, {name}! 👋")        # Line 63: Show success message

# Number input
age = st.number_input("Enter your age:",     # Line 66: Number input widget
                      min_value=0,           # Line 66: Minimum value
                      max_value=120,         # Line 66: Maximum value
                      value=25)              # Line 66: Default value
st.info(f"You are {age} years old")         # Line 67: Info message

# Slider
temperature = st.slider("Temperature (°C):", # Line 70: Slider widget
                        -20, 50, 20)         # Line 70: min, max, default
st.write(f"🌡️ Current: {temperature}°C")    # Line 71: Display value
```

**Interactive Behavior:**
- **Line 61:** Text input box appears; user can type their name
- **Line 63:** Success message appears only when `name` is not empty
- **Line 66:** Number input with up/down arrows, validates range (0-120)
- **Line 70:** Slider bar that user can drag to adjust temperature (-20 to 50)
- Each widget interaction triggers a **rerun** of the entire script

**💡 Key Insight:** Every widget interaction causes the script to rerun from top to bottom. Session state is used to preserve values that need to persist.

---

### 5. Layout with Columns

**Source Code (main_streamlit.py:57-89):**
```python
col1, col2 = st.columns(2)                   # Line 57: Create 2 equal columns

with col1:                                   # Line 59: Context for left column
    st.subheader("Input Widgets")            # Line 60: Displayed in left column
    # ... input widgets ...

with col2:                                   # Line 76: Context for right column
    st.subheader("Selection Widgets")        # Line 77: Displayed in right column
    # ... selection widgets ...
```

**Visual Layout:**
```
┌─────────────────────────┬─────────────────────────┐
│ Input Widgets           │ Selection Widgets       │
│ • Text input            │ • Selectbox             │
│ • Number input          │ • Radio buttons         │
│ • Slider                │ • Checkbox              │
└─────────────────────────┴─────────────────────────┘
```

**💡 Key Insight:** `st.columns()` creates a horizontal layout. The `with` statement directs all subsequent commands to that column until the block ends.

---

### 6. Buttons and State Management

**Source Code (main_streamlit.py:96-110):**
```python
col1, col2, col3 = st.columns(3)             # Line 96: Three columns

with col1:
    if st.button("➕ Increment",              # Line 98: Create button
                 use_container_width=True):  # Line 98: Full width
        st.session_state.counter += 1        # Line 99: Modify state

with col2:
    if st.button("➖ Decrement",              # Line 102: Decrement button
                 use_container_width=True):
        st.session_state.counter -= 1        # Line 103: Decrease counter

with col3:
    if st.button("🔄 Reset",                 # Line 106: Reset button
                 use_container_width=True):
        st.session_state.counter = 0         # Line 107: Reset to 0

st.metric(                                   # Line 109: Display metric
    label="Counter Value",
    value=st.session_state.counter,          # Line 111: Current value
    delta=1 if st.session_state.counter > 0 else 0  # Line 112: Show delta
)
```

**Interactive Behavior:**
1. User clicks "➕ Increment" button
2. **Line 99** executes: `st.session_state.counter += 1`
3. Script reruns from top
4. **Line 111** displays new counter value
5. **Line 112** shows green arrow ▲ with delta "+1"

**Example Sequence:**
```
Initial state: counter = 0

Click "➕ Increment" → counter = 1  [Display: "1" with ▲1]
Click "➕ Increment" → counter = 2  [Display: "2" with ▲1]
Click "➖ Decrement" → counter = 1  [Display: "1" with ▲1]
Click "🔄 Reset"    → counter = 0  [Display: "0" with ▲0]
```

**💡 Key Insight:** Buttons return `True` only during the rerun triggered by clicking them. Session state persists the counter value across all reruns.

---

### 7. Data Visualization

**Source Code (main_streamlit.py:118-142):**
```python
chart_type = st.radio(                       # Line 118: Radio button selection
    "Select chart type:",
    ["Line Chart", "Area Chart", "Bar Chart"],
    horizontal=True
)

# Generate sample data
dates = pd.date_range(                       # Line 125: Create date range
    start=datetime.now() - timedelta(days=30),
    periods=30,
    freq='D'
)
df_chart = pd.DataFrame({                    # Line 129: Create DataFrame
    'Date': dates,                           # Line 130: 30 dates
    'Sales': np.random.randint(100, 500, 30),# Line 131: Random sales data
    'Revenue': np.random.randint(1000, 5000, 30),  # Line 132: Random revenue
})

if chart_type == "Line Chart":               # Line 135: Conditional rendering
    st.line_chart(df_chart.set_index('Date'))# Line 136: Display line chart
elif chart_type == "Area Chart":             # Line 137
    st.area_chart(df_chart.set_index('Date'))# Line 138: Display area chart
else:                                        # Line 139
    st.bar_chart(df_chart.set_index('Date')) # Line 140: Display bar chart
```

**Interactive Behavior:**
1. **Lines 125-133:** Generate DataFrame with 30 days of random data
2. **Line 118:** User selects chart type via radio buttons
3. **Lines 135-140:** Display corresponding chart based on selection
4. Charts automatically update when user changes selection

**Visual Output Example:**
```
Select chart type: ○ Line Chart ● Area Chart ○ Bar Chart

[Interactive chart showing Sales and Revenue over 30 days]
- X-axis: Dates (last 30 days)
- Y-axis: Values
- Two series: Sales (blue) and Revenue (red)
- Hover tooltip shows exact values
```

**💡 Key Insight:** Streamlit provides built-in chart components that automatically render pandas DataFrames. The index becomes the x-axis.

---

### 8. Tabs for Content Organization

**Source Code (main_streamlit.py:154-174):**
```python
tab1, tab2, tab3 = st.tabs(["📊 Table",      # Line 154: Create 3 tabs
                            "📈 Metrics",
                            "🗂️ JSON"])

with tab1:                                   # Line 156: Table tab content
    st.dataframe(                            # Line 157: Interactive table
        df_display,                          # Line 158: DataFrame to display
        use_container_width=True,            # Line 159: Full width
        hide_index=True,                     # Line 160: Hide row numbers
    )

with tab2:                                   # Line 162: Metrics tab content
    col1, col2, col3, col4 = st.columns(4)   # Line 163: 4 metric columns
    col1.metric("Total Products",            # Line 164: First metric
                len(df_display))
    col2.metric("Avg Price",                 # Line 165: Second metric
                f"${df_display['Price'].mean():.0f}")
    col3.metric("Total Stock",               # Line 166: Third metric
                df_display['Stock'].sum())
    col4.metric("Avg Rating",                # Line 167: Fourth metric
                f"{df_display['Rating'].mean():.2f}⭐")

with tab3:                                   # Line 169: JSON tab content
    st.json({                                # Line 170: Display JSON
        'products': df_display.to_dict('records'),  # Line 171: Convert to dict
        'timestamp': datetime.now().isoformat(),    # Line 172: Add timestamp
    })
```

**Visual Output:**

**Tab 1 (📊 Table):**
```
┌─────────────┬────────┬────────┬────────┐
│ Product     │ Price  │ Stock  │ Rating │
├─────────────┼────────┼────────┼────────┤
│ Laptop      │ 1200   │ 15     │ 4.5    │
│ Mouse       │ 25     │ 120    │ 4.2    │
│ Keyboard    │ 75     │ 85     │ 4.7    │
│ Monitor     │ 350    │ 30     │ 4.6    │
│ Headphones  │ 150    │ 45     │ 4.3    │
└─────────────┴────────┴────────┴────────┘
```

**Tab 2 (📈 Metrics):**
```
┌─────────┬─────────┬─────────┬─────────┐
│ Total   │ Avg     │ Total   │ Avg     │
│ Products│ Price   │ Stock   │ Rating  │
├─────────┼─────────┼─────────┼─────────┤
│    5    │  $360   │  295    │ 4.46⭐  │
└─────────┴─────────┴─────────┴─────────┘
```

**Tab 3 (🗂️ JSON):**
```json
{
  "products": [
    {"Product": "Laptop", "Price": 1200, "Stock": 15, "Rating": 4.5},
    ...
  ],
  "timestamp": "2025-11-04T14:30:00.123456"
}
```

**💡 Key Insight:**
- **Line 154:** `st.tabs()` creates tabbed interface; only active tab content is visible
- **Lines 164-167:** `.metric()` displays large numbers with optional deltas
- **Line 157:** `st.dataframe()` creates sortable, filterable table automatically

---

### 9. Expandable Sections

**Source Code (main_streamlit.py:179-186):**
```python
with st.expander("📦 Click to expand/collapse"):  # Line 179: Collapsible section
    st.write("This is an expandable section!")   # Line 180: Hidden content
    st.write("You can hide/show content...")     # Line 181: More content
    st.code("""                                  # Line 182: Code example
with st.expander("Title"):
    st.write("Hidden content")
    """, language="python")
```

**Interactive Behavior:**
1. Initially shows: `📦 Click to expand/collapse` with ▶ arrow (collapsed)
2. User clicks → Arrow changes to ▼, content appears
3. User clicks again → Arrow changes back to ▶, content hides

**💡 Key Insight:** Expanders are perfect for:
- Optional/advanced settings
- Documentation and help text
- Hiding verbose output until needed

---

### 10. Sidebar

**Source Code (main_streamlit.py:194-217):**
```python
with st.sidebar:                                 # Line 194: Sidebar context
    st.header("🎛️ Sidebar")                     # Line 195: Sidebar content
    st.write("This is the sidebar...")          # Line 196

    show_advanced = st.checkbox(                 # Line 198: Checkbox widget
        "Show advanced options"
    )

    if show_advanced:                            # Line 200: Conditional display
        st.selectbox("Advanced Setting 1:",      # Line 201: Only shown if checked
                     ["Option A", "Option B"])
        st.slider("Advanced Setting 2:",         # Line 202: Only shown if checked
                  0, 100, 50)

    st.subheader("📝 Chat Example")              # Line 206
    user_message = st.text_input(                # Line 207: Chat input
        "Type a message:",
        key="chat_input"                         # Line 209: Unique key
    )
    if st.button("Send") and user_message:       # Line 210: Send button
        st.session_state.messages.append({       # Line 211: Add to messages
            'time': datetime.now().strftime("%H:%M:%S"),  # Line 212
            'text': user_message                 # Line 213
        })

    if st.session_state.messages:                # Line 215: Show messages
        st.write("**Messages:**")
        for msg in st.session_state.messages[-5:]:  # Line 217: Last 5 messages
            st.text(f"[{msg['time']}] {msg['text']}")  # Line 218
```

**Interactive Chat Behavior:**
1. User types "Hello World" in text input (Line 207)
2. User clicks "Send" button (Line 210)
3. **Line 211-214:** Message added to `st.session_state.messages` with timestamp
4. **Line 217-218:** Last 5 messages displayed:
   ```
   Messages:
   [14:30:15] Hello World
   [14:30:22] How are you?
   [14:30:28] Great!
   ```

**💡 Key Insight:**
- **Line 194:** `with st.sidebar:` places all content in the collapsible sidebar
- **Line 209:** `key` parameter required for widgets that might have duplicate labels
- **Line 211:** Session state stores message history across reruns

---

## Application Flow

```
1. User opens app → Script runs top to bottom
2. User interacts (button/widget) → Script reruns entirely
3. Session state persists → Values remembered
4. Widgets display current state → UI updates
```

## Key Takeaways

1. **Automatic Reruns** - Every interaction triggers a full script rerun
2. **Session State** - Persist data across reruns with `st.session_state`
3. **Layout Control** - Use columns, tabs, expanders, sidebar for organization
4. **Built-in Widgets** - Rich set of input controls (sliders, buttons, text, etc.)
5. **Data Display** - Automatic rendering of pandas DataFrames and charts
6. **Pythonic API** - Write Python code, get a web app instantly

## When to Use Streamlit

✅ **Good for:**
- Data science dashboards and visualizations
- Machine learning model demos
- Internal tools and admin panels
- Rapid prototyping of web apps
- Data exploration and analysis tools

❌ **Not ideal for:**
- Production web applications with complex routing
- Apps requiring fine-grained control over HTML/CSS
- Real-time multi-user applications
- Mobile-first applications

## Version Requirements

- **Python:** >=3.11 (specified in pyproject.toml)
- **Streamlit:** >=1.51.0
- **Pandas:** >=2.3.3
- **NumPy:** >=2.3.4

All dependencies are managed via `uv` and specified in `pyproject.toml`.

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
