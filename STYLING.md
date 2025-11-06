# 🎨 STYLING & CUSTOMIZATION GUIDE

## Theme Customization

### Basic Theme Configuration

Edit `.streamlit/config.toml`:

```toml
[theme]
# Primary color - used for interactive elements
primaryColor = "#FF4B4B"

# Background color
backgroundColor = "#FFFFFF"

# Secondary background color - used for sidebar
secondaryBackgroundColor = "#F0F2F6"

# Text color
textColor = "#262730"

# Font family
font = "sans serif"  # Options: "sans serif", "serif", "monospace"
```

### Popular Color Schemes

#### 1. Professional Blue

```toml
[theme]
primaryColor = "#0068C9"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

#### 2. Dark Mode

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
```

#### 3. Nature Green

```toml
[theme]
primaryColor = "#00C851"
backgroundColor = "#FAFAFA"
secondaryBackgroundColor = "#E8F5E9"
textColor = "#1B5E20"
```

#### 4. Elegant Purple

```toml
[theme]
primaryColor = "#9C27B0"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F3E5F5"
textColor = "#4A148C"
```

## Custom CSS Styling

### Adding Custom CSS

In your page or app.py:

```python
st.markdown("""
    <style>
    /* Your custom CSS here */
    </style>
""", unsafe_allow_html=True)
```

### Useful CSS Classes

#### 1. Metric Cards

```css
.stMetric {
  background-color: #f0f2f6;
  padding: 1rem;
  border-radius: 0.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

#### 2. Headers

```css
.main-header {
  font-size: 2.5rem;
  font-weight: bold;
  color: #ff4b4b;
  text-align: center;
  padding: 1rem 0;
}

.sub-header {
  font-size: 1.5rem;
  color: #666;
  text-align: center;
  margin-bottom: 2rem;
}
```

#### 3. Sidebar

```css
[data-testid="stSidebar"] {
  background-color: #f0f2f6;
}

[data-testid="stSidebar"] > div:first-child {
  background-color: #f0f2f6;
}
```

#### 4. Buttons

```css
.stButton > button {
  background-color: #ff4b4b;
  color: white;
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  font-weight: bold;
  border: none;
  transition: all 0.3s;
}

.stButton > button:hover {
  background-color: #e63946;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
```

#### 5. Dataframes

```css
[data-testid="stDataFrame"] {
  border-radius: 0.5rem;
  overflow: hidden;
}
```

## Chart Customization

### Matplotlib Style

In `components/charts.py`:

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set global style
plt.style.use('seaborn-v0_8-darkgrid')  # or 'ggplot', 'fivethirtyeight'
sns.set_palette("husl")
```

### Custom Color Palettes

Edit `config.py`:

```python
# Pastel colors
CATEGORY_COLORS = {
    'Makanan & Minuman': '#FFB3BA',
    'Transport': '#BAFFC9',
    'Belanja': '#BAE1FF',
    # ...
}

# Vibrant colors
CATEGORY_COLORS = {
    'Makanan & Minuman': '#FF6B6B',
    'Transport': '#4ECDC4',
    'Belanja': '#45B7D1',
    # ...
}

# Monochrome
CATEGORY_COLORS = {
    'Makanan & Minuman': '#2C3E50',
    'Transport': '#34495E',
    'Belanja': '#7F8C8D',
    # ...
}
```

### Chart Style Templates

#### Modern Minimalist

```python
def styled_bar_chart(data, x, y, title):
    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.bar(data[x], data[y], color='#3498db', alpha=0.8)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Minimal grid
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Title styling
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)

    # Label styling
    ax.set_xlabel(x, fontsize=12)
    ax.set_ylabel(y, fontsize=12)

    plt.tight_layout()
    return fig
```

#### Bold & Colorful

```python
def colorful_pie_chart(data, labels, title):
    fig, ax = plt.subplots(figsize=(10, 6))

    colors = plt.cm.Set3(range(len(data)))

    wedges, texts, autotexts = ax.pie(
        data,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        explode=[0.05] * len(data)  # Explode all slices
    )

    # Bold text
    for text in texts:
        text.set_fontsize(12)
        text.set_fontweight('bold')

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)

    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)

    plt.tight_layout()
    return fig
```

## Component Styling

### Metric Cards with Icons

```python
def styled_metric(label, value, icon="📊"):
    st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 1rem;
            color: white;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        '>
            <div style='font-size: 3rem;'>{icon}</div>
            <div style='font-size: 0.9rem; opacity: 0.9;'>{label}</div>
            <div style='font-size: 2rem; font-weight: bold;'>{value}</div>
        </div>
    """, unsafe_allow_html=True)
```

### Info Cards

```python
def info_card(title, content, color="#3498db"):
    st.markdown(f"""
        <div style='
            background-color: {color}15;
            border-left: 4px solid {color};
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        '>
            <h4 style='color: {color}; margin-bottom: 0.5rem;'>{title}</h4>
            <p style='color: #666; margin: 0;'>{content}</p>
        </div>
    """, unsafe_allow_html=True)
```

## Layout Customization

### Wide Layout with Custom Columns

```python
st.set_page_config(layout="wide", page_title="Dashboard")

# Custom column widths
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    # Sidebar-like content
    pass

with col2:
    # Main content
    pass

with col3:
    # Additional info
    pass
```

### Tabs with Custom Styling

```python
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Analysis", "💳 Details"])

with tab1:
    st.markdown("### Overview Content")
    # Content
```

### Expandable Sections

```python
with st.expander("🔍 Advanced Filters", expanded=False):
    # Filter widgets
    pass

with st.expander("📊 Additional Charts"):
    # More charts
    pass
```

## Animation & Interactivity

### Loading Animation

```python
with st.spinner('Loading data...'):
    time.sleep(2)  # Simulate loading
    data = load_data()
st.success('Data loaded successfully!')
```

### Progress Bar

```python
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)
```

### Balloons 🎈

```python
if st.button('Celebrate!'):
    st.balloons()
```

## Responsive Design

### Mobile-Friendly Layout

```python
# Check if mobile (simplified)
is_mobile = st.sidebar.checkbox("Mobile View", value=False)

if is_mobile:
    # Single column layout
    st.write("Content")
else:
    # Multi-column layout
    col1, col2 = st.columns(2)
```

### Adaptive Chart Sizes

```python
# Get screen width
width = st.sidebar.slider("Chart Width", 6, 14, 10)

fig, ax = plt.subplots(figsize=(width, width*0.6))
# Chart code
st.pyplot(fig)
```

## Custom Fonts

### Google Fonts

In `app.py` or page files:

```python
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

    <style>
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)
```

## Icon Libraries

### Using Emojis

```python
st.title("💰 Bank Dashboard")
st.subheader("📊 Analytics")
st.metric("Total", "Rp 1M", delta="📈 +10%")
```

### Unicode Icons

```python
# Currency: ₹ € $ £ ¥
# Arrows: ↑ ↓ → ←
# Shapes: ● ■ ◆ ★
# Check: ✓ ✗ ✔ ✘
```

## Best Practices

### 1. Consistent Color Scheme

- Use same colors throughout app
- Define colors in config.py
- Use color for meaning (red=danger, green=success)

### 2. Whitespace

- Use `st.markdown("---")` for separators
- Add padding/margins in CSS
- Don't overcrowd the interface

### 3. Typography

- Max 2-3 font families
- Clear hierarchy (title > header > body)
- Consistent font sizes

### 4. Visual Hierarchy

- Most important info at top
- Use size and color for emphasis
- Group related elements

### 5. Accessibility

- Sufficient color contrast
- Readable font sizes (min 14px)
- Alternative text for icons
- Keyboard navigation support

## Example: Complete Custom Theme

Create `custom_theme.py`:

```python
import streamlit as st

def apply_custom_theme():
    st.markdown("""
        <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

        /* Global Styles */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* Header */
        .main-header {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            padding: 2rem 0;
        }

        /* Metrics */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 0.5rem;
            padding: 0.75rem 2rem;
            font-weight: 600;
            transition: transform 0.2s;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }

        /* Cards */
        .element-container {
            animation: fadeIn 0.5s;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
    """, unsafe_allow_html=True)

# Use in app.py or pages
apply_custom_theme()
```

---

**Happy Styling! 🎨✨**
