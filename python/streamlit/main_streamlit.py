"""
Streamlit Example: Building Interactive Web Applications

This example showcases key Streamlit concepts:
1. Text elements and markdown formatting
2. Interactive widgets (buttons, sliders, text inputs)
3. Layout components (columns, sidebar, expanders)
4. Data visualization with charts
5. Session state management
6. File uploads and data display
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# Configure the page
st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Initialize session state
if "counter" not in st.session_state:
    st.session_state.counter = 0
if "messages" not in st.session_state:
    st.session_state.messages = []


# Header Section
st.title("🚀 Streamlit Interactive Demo")
st.markdown("*Building interactive web apps with Python made easy!*")
st.divider()


# Example 1: Text Elements
st.header("1️⃣ Text Elements")
st.write("Streamlit supports various text formatting options:")
st.markdown("""
- **Bold text** and *italic text*
- `Code snippets`
- [Links](https://streamlit.io)
""")
st.code("""
st.write("Hello World")
st.markdown("**Bold** text")
st.code("print('Code block')")
""", language="python")
st.divider()


# Example 2: Interactive Widgets
st.header("2️⃣ Interactive Widgets")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Widgets")

    # Text input
    name = st.text_input("Enter your name:", placeholder="John Doe")
    if name:
        st.success(f"Hello, {name}! 👋")

    # Number input
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
    st.info(f"You are {age} years old")

    # Slider
    temperature = st.slider("Temperature (°C):", -20, 50, 20)
    st.write(f"🌡️ Current temperature: {temperature}°C")

with col2:
    st.subheader("Selection Widgets")

    # Selectbox
    city = st.selectbox(
        "Choose a city:",
        ["New York", "London", "Tokyo", "Paris", "Sydney"]
    )
    st.write(f"📍 Selected: {city}")

    # Radio buttons
    theme = st.radio(
        "Select theme:",
        ["Light", "Dark", "Auto"],
        horizontal=True
    )
    st.write(f"🎨 Theme: {theme}")

    # Checkbox
    agree = st.checkbox("I agree to the terms and conditions")
    if agree:
        st.success("✅ Agreement confirmed!")

st.divider()


# Example 3: Session State & Buttons
st.header("3️⃣ Session State & Interactivity")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Increment", use_container_width=True):
        st.session_state.counter += 1

with col2:
    if st.button("➖ Decrement", use_container_width=True):
        st.session_state.counter -= 1

with col3:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.counter = 0

st.metric(
    label="Counter Value",
    value=st.session_state.counter,
    delta=1 if st.session_state.counter > 0 else 0
)
st.divider()


# Example 4: Data Visualization
st.header("4️⃣ Data Visualization")

# Generate sample data
chart_type = st.radio(
    "Select chart type:",
    ["Line Chart", "Area Chart", "Bar Chart"],
    horizontal=True
)

# Create sample data
dates = pd.date_range(start=datetime.now() - timedelta(days=30), periods=30, freq='D')
df_chart = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(100, 500, 30),
    'Revenue': np.random.randint(1000, 5000, 30),
})

if chart_type == "Line Chart":
    st.line_chart(df_chart.set_index('Date'))
elif chart_type == "Area Chart":
    st.area_chart(df_chart.set_index('Date'))
else:
    st.bar_chart(df_chart.set_index('Date'))

st.divider()


# Example 5: Data Display
st.header("5️⃣ Data Display")

# Create sample dataframe
df_display = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [1200, 25, 75, 350, 150],
    'Stock': [15, 120, 85, 30, 45],
    'Rating': [4.5, 4.2, 4.7, 4.6, 4.3],
})

tab1, tab2, tab3 = st.tabs(["📊 Table", "📈 Metrics", "🗂️ JSON"])

with tab1:
    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True,
    )

with tab2:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Products", len(df_display))
    col2.metric("Avg Price", f"${df_display['Price'].mean():.0f}")
    col3.metric("Total Stock", df_display['Stock'].sum())
    col4.metric("Avg Rating", f"{df_display['Rating'].mean():.2f}⭐")

with tab3:
    st.json({
        'products': df_display.to_dict('records'),
        'timestamp': datetime.now().isoformat(),
    })

st.divider()


# Example 6: Layout Components
st.header("6️⃣ Layout Components")

with st.expander("📦 Click to expand/collapse"):
    st.write("This is an expandable section!")
    st.write("You can hide/show content dynamically.")
    st.code("""
with st.expander("Title"):
    st.write("Hidden content")
    """, language="python")

with st.container():
    st.info("💡 **Container**: Groups elements together")
    st.write("Containers help organize your app structure.")

st.divider()


# Sidebar
with st.sidebar:
    st.header("🎛️ Sidebar")
    st.write("This is the sidebar - perfect for controls and settings!")

    show_advanced = st.checkbox("Show advanced options")

    if show_advanced:
        st.selectbox("Advanced Setting 1:", ["Option A", "Option B"])
        st.slider("Advanced Setting 2:", 0, 100, 50)

    st.divider()

    st.subheader("📝 Chat Example")
    user_message = st.text_input("Type a message:", key="chat_input")
    if st.button("Send") and user_message:
        st.session_state.messages.append({
            'time': datetime.now().strftime("%H:%M:%S"),
            'text': user_message
        })

    if st.session_state.messages:
        st.write("**Messages:**")
        for msg in st.session_state.messages[-5:]:  # Show last 5 messages
            st.text(f"[{msg['time']}] {msg['text']}")


# Footer
st.divider()
st.caption("🎉 Built with Streamlit - Turn data scripts into shareable web apps in minutes!")
