# 📚 Developer Documentation

## Architecture Overview

### Project Structure

```
bank-transaction-dashboard/
├── app.py                      # Main entry point (Home page)
├── config.py                   # Configuration & constants
├── utils.py                    # Utility functions
├── generate_data.py           # Data generation script
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
├── README.md                  # User documentation
├── QUICKSTART.md              # Quick start guide
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose config
├── Procfile                   # Heroku deployment
├── runtime.txt                # Python version for Heroku
│
├── .streamlit/
│   └── config.toml           # Streamlit configuration
│
├── data/
│   └── bank_transactions.csv # Transaction data
│
├── components/               # Reusable components
│   ├── __init__.py          # Package initialization
│   ├── metrics.py           # Metric components
│   ├── charts.py            # Chart components
│   ├── filters.py           # Filter components
│   └── tables.py            # Table components
│
└── pages/                    # Multi-page app pages
    ├── 1_📊_Dashboard.py
    ├── 2_📈_Analytics.py
    └── 3_💳_Transactions.py
```

## Core Modules

### 1. config.py

Contains all application constants and configuration.

**Key Constants:**

- `APP_TITLE`: Application title
- `APP_ICON`: Application icon
- `DATA_PATH`: Path to data file
- `CATEGORIES`: List of transaction categories
- `TRANSACTION_TYPES`: List of transaction types
- `COLOR_PALETTE`: Color scheme
- `CATEGORY_COLORS`: Colors for each category

**Usage:**

```python
from config import CATEGORIES, COLOR_PALETTE
```

### 2. utils.py

Utility functions for data processing.

**Key Functions:**

#### `load_data()`

Load and parse transaction data from CSV.

- **Returns**: DataFrame
- **Raises**: Exception if file not found

#### `filter_data(df, start_date, end_date, categories, transaction_types)`

Filter DataFrame based on criteria.

- **Args**:
  - `df`: DataFrame to filter
  - `start_date`: Start date (optional)
  - `end_date`: End date (optional)
  - `categories`: List of categories (optional)
  - `transaction_types`: List of types (optional)
- **Returns**: Filtered DataFrame

#### `calculate_summary(df)`

Calculate summary statistics.

- **Returns**: Dict with keys:
  - `total_income`: Total credit
  - `total_expense`: Total debit
  - `balance`: Net balance
  - `transaction_count`: Number of transactions

#### `get_category_summary(df)`

Get summary per category.

- **Returns**: DataFrame with columns:
  - `Kategori`: Category name
  - `Total`: Total amount
  - `Jumlah Transaksi`: Transaction count

#### `get_monthly_summary(df)`

Get monthly income/expense summary.

- **Returns**: DataFrame with columns:
  - `Bulan`: Month period
  - `Income`: Total income
  - `Expense`: Total expense
  - `Balance`: Net balance

#### `format_currency(amount)`

Format number as Indonesian Rupiah.

- **Args**: `amount` (float/int)
- **Returns**: Formatted string (e.g., "Rp 1,000,000")

### 3. components/

Reusable UI components.

#### metrics.py

**Functions:**

- `summary_metrics(summary_data)`: Display 4-column summary
- `category_metrics(category_summary, top_n)`: Display top N categories
- `statistics_metrics(stats)`: Display descriptive statistics
- `metric_card(label, value, delta, delta_color, help_text)`: Single metric card

#### charts.py

**Functions:**

- `pie_chart(data, labels, title, colors)`: Create pie chart
- `bar_chart(data, x, y, title, color, horizontal)`: Create bar chart
- `line_chart(data, x, y, title, hue)`: Create line chart
- `box_plot(data, x, y, title)`: Create box plot
- `histogram_chart(data, column, bins, title)`: Create histogram
- `area_chart(data, x, y, title)`: Create area/stacked area chart
- `heatmap_chart(data, title, annot, fmt, cmap)`: Create heatmap

**All chart functions return matplotlib Figure object.**

#### filters.py

**Functions:**

- `date_range_filter(min_date, max_date, key_prefix)`: Date range picker
- `category_filter(categories, key, default)`: Multi-select category
- `transaction_type_filter(types, key, default)`: Multi-select type
- `amount_range_filter(min_amount, max_amount, key)`: Amount slider
- `search_filter(placeholder, key)`: Search text input

**All filter functions return selected values.**

#### tables.py

**Functions:**

- `transaction_table(df, show_index, height)`: Display formatted transaction table
- `summary_table(df, title)`: Display summary table
- `category_breakdown_table(category_summary)`: Category breakdown with progress bars
- `top_transactions_table(df, n, transaction_type)`: Top N transactions
- `comparison_table(data1, data2, labels)`: Compare two periods

## Pages Architecture

### Multi-page Navigation

Streamlit automatically creates navigation from files in `pages/` folder:

- File naming: `N_emoji_PageName.py`
- N: Order number (1, 2, 3, ...)
- emoji: Optional emoji icon
- PageName: Display name

### Page Structure

Each page follows this pattern:

```python
import streamlit as st
from components import *
from utils import *
from config import *

# Page config
st.set_page_config(...)

def render_sidebar_filters():
    """Render sidebar filters"""
    # Filter logic
    return filtered_data

def main():
    """Main page logic"""
    st.title("Page Title")

    # Get filtered data
    df = render_sidebar_filters()

    # Render content
    # ...

if __name__ == "__main__":
    main()
```

## Data Schema

### CSV Format

```csv
Tanggal,Kategori,Tipe,Jumlah,Deskripsi,Saldo
2025-08-08,Tagihan,Debit,359178,Streaming,4640822
```

**Columns:**

- `Tanggal` (datetime): Transaction date (YYYY-MM-DD)
- `Kategori` (string): Category (must be in CATEGORIES)
- `Tipe` (string): "Debit" or "Kredit"
- `Jumlah` (int): Amount in Rupiah
- `Deskripsi` (string): Transaction description
- `Saldo` (int): Balance after transaction

## Adding New Features

### Add New Page

1. Create file in `pages/`:

   ```
   pages/4_🎯_NewPage.py
   ```

2. Follow page structure pattern

3. Import necessary components

### Add New Component

1. Create function in appropriate component file:

   ```python
   # components/charts.py
   def new_chart(data, ...):
       fig, ax = plt.subplots(figsize=(10, 6))
       # Chart logic
       return fig
   ```

2. Add to `__init__.py`:

   ```python
   from .charts import new_chart
   __all__ = [..., 'new_chart']
   ```

3. Use in pages:
   ```python
   from components.charts import new_chart
   fig = new_chart(data)
   st.pyplot(fig)
   ```

### Add New Category

1. Edit `config.py`:

   ```python
   CATEGORIES = [
       'New Category',
       # ... existing
   ]

   CATEGORY_COLORS = {
       'New Category': '#HexColor',
       # ... existing
   }
   ```

2. Regenerate data:
   ```bash
   python generate_data.py
   ```

### Add New Filter

1. Create function in `components/filters.py`:

   ```python
   def new_filter(options, key):
       selected = st.selectbox("Label", options, key=key)
       return selected
   ```

2. Use in page:
   ```python
   from components.filters import new_filter
   value = new_filter(options, key="my_filter")
   ```

## Best Practices

### 1. Code Organization

- Keep functions small and focused
- Use docstrings for all functions
- Follow Python naming conventions
- Group related functionality

### 2. State Management

- Use `st.session_state` for persistent data
- Clear state when needed
- Avoid redundant data loading

### 3. Performance

- Cache expensive operations
- Filter data before processing
- Use efficient pandas operations
- Limit data display size

### 4. Error Handling

```python
try:
    data = load_data()
except Exception as e:
    st.error(f"Error: {str(e)}")
    st.stop()
```

### 5. User Experience

- Show loading states
- Provide helpful error messages
- Add tooltips and help text
- Use consistent styling

## Testing

### Manual Testing Checklist

- [ ] Home page loads correctly
- [ ] Dashboard displays metrics
- [ ] Charts render properly
- [ ] Filters work as expected
- [ ] Search functionality works
- [ ] Export CSV downloads
- [ ] All pages navigate correctly
- [ ] Responsive on different screen sizes

### Test Data Generation

Modify `generate_data.py` to create test scenarios:

```python
# Edge cases
n_transactions = 5  # Small dataset
n_transactions = 1000  # Large dataset
```

## Deployment

### Environment Variables

For production, consider using environment variables:

```python
# config.py
import os

DATA_PATH = os.getenv('DATA_PATH', 'data/bank_transactions.csv')
```

### Streamlit Cloud

- Automatic deployment from GitHub
- Free tier available
- Built-in secrets management

### Docker

Build and run:

```bash
docker build -t bank-dashboard .
docker run -p 8501:8501 bank-dashboard
```

Or use Docker Compose:

```bash
docker-compose up
```

### Heroku

Deploy with Git:

```bash
git init
heroku create your-app-name
git add .
git commit -m "Initial commit"
git push heroku main
```

## Troubleshooting

### Common Issues

1. **Port already in use**

   ```bash
   streamlit run app.py --server.port 8502
   ```

2. **Module not found**

   ```bash
   pip install -r requirements.txt
   ```

3. **Data not loading**

   - Check DATA_PATH in config.py
   - Verify CSV format
   - Check file permissions

4. **Chart not displaying**
   - Ensure matplotlib backend is correct
   - Check data format
   - Verify figure is returned

## API Reference

See inline docstrings in each module for detailed API documentation.

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## License

MIT License - see LICENSE file

---

**For questions or issues, refer to README.md or check the code!**
