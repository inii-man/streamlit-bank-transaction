# 💰 Bank Transaction Dashboard

Dashboard analisis transaksi bank yang dibangun dengan Streamlit, Pandas, NumPy, Matplotlib, dan Seaborn.

## ✨ Fitur

### 🏠 Home Page

- Welcome screen dengan quick stats
- Preview transaksi terbaru
- Navigasi mudah ke halaman lain

### 📊 Dashboard

- **Summary Metrics**: Total pemasukan, pengeluaran, saldo bersih, dan jumlah transaksi
- **Distribusi Kategori**: Pie chart dan bar chart untuk pengeluaran per kategori
- **Trend Bulanan**: Line chart untuk melihat trend pemasukan dan pengeluaran
- **Top Transaksi**: Tabel transaksi terbesar (debit dan kredit)
- **Statistik**: Rata-rata, median, max, min transaksi
- **Filter**: Date range, kategori, dan tipe transaksi

### 📈 Analytics

5 Sub-menu analisis mendalam:

1. **Overview**: Breakdown debit vs kredit
2. **Kategori**: Analisis per kategori dengan box plot
3. **Time Series**: Trend bulanan, area chart, dan transaksi harian
4. **Distribusi**: Histogram, statistik deskriptif, dan heatmap
5. **Perbandingan**: Perbandingan 2 periode waktu

### 💳 Transactions

- **Tabel Interaktif**: Semua transaksi dengan sorting dan pagination
- **Filter Lengkap**: Date range, kategori, tipe, amount range, dan search
- **Multiple Views**: Tabel, per kategori, dan statistik
- **Export CSV**: Download data yang sudah difilter
- **Sidebar dengan Sub-menu**: View options untuk tampilan yang berbeda

## 🏗️ Struktur Project

```
.
├── app.py                          # Main application
├── config.py                       # Configuration dan constants
├── utils.py                        # Utility functions
├── generate_data.py               # Script untuk generate CSV
├── requirements.txt               # Dependencies
├── .streamlit/
│   └── config.toml               # Streamlit configuration
├── data/
│   └── bank_transactions.csv     # Data transaksi (100 records)
├── components/                    # Reusable components
│   ├── metrics.py                # Metric cards
│   ├── charts.py                 # Chart components (matplotlib & seaborn)
│   ├── filters.py                # Filter components
│   └── tables.py                 # Table components
└── pages/                         # Multiple pages
    ├── 1_📊_Dashboard.py
    ├── 2_📈_Analytics.py
    └── 3_💳_Transactions.py
```

## 🚀 Cara Menjalankan

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate Data (Opsional - sudah ada CSV)

```bash
python generate_data.py
```

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

## 📦 Dependencies

- **streamlit**: Framework untuk web app
- **pandas**: Data manipulation dan analysis
- **numpy**: Numerical computing
- **matplotlib**: Plotting dan visualization
- **seaborn**: Statistical data visualization

## 🎨 Best Practices yang Diterapkan

### 1. **Modular Architecture**

- Komponen dipisah ke folder `components/`
- Setiap halaman di folder `pages/` dengan auto-navigation
- Utility functions di `utils.py`
- Configuration di `config.py`

### 2. **Reusable Components**

- `metrics.py`: Reusable metric cards
- `charts.py`: Reusable chart functions
- `filters.py`: Reusable filter widgets
- `tables.py`: Reusable table components

### 3. **Clean Code**

- Docstrings untuk setiap function
- Type hints untuk parameter
- Consistent naming convention
- Comments untuk logic yang kompleks

### 4. **User Experience**

- Responsive layout dengan columns
- Interactive filters di sidebar
- Loading states dan error handling
- Help text dan tooltips
- Export functionality

### 5. **Data Management**

- CSV sebagai data source
- Pandas untuk efficient data processing
- Caching dengan session state
- Data validation dan filtering

### 6. **Visualization**

- Matplotlib dan Seaborn untuk professional charts
- Consistent color palette
- Proper labels dan formatting
- Multiple chart types untuk insights yang berbeda

## 📊 Data Structure

CSV memiliki kolom:

- **Tanggal**: Tanggal transaksi (YYYY-MM-DD)
- **Kategori**: Kategori transaksi (10 kategori)
- **Tipe**: Debit atau Kredit
- **Jumlah**: Nominal transaksi (dalam Rupiah)
- **Deskripsi**: Deskripsi transaksi
- **Saldo**: Saldo setelah transaksi

## 🎯 Fitur Filter

### Sidebar Filters

1. **Date Range**: Pilih periode transaksi
2. **Kategori**: Multi-select kategori
3. **Tipe Transaksi**: Debit/Kredit
4. **Amount Range**: Slider untuk range jumlah
5. **Search**: Cari berdasarkan deskripsi

### Sidebar Sub-menu

- **Dashboard**: Filter standar
- **Analytics**: 5 jenis analisis (Overview, Kategori, Time Series, Distribusi, Perbandingan)
- **Transactions**: View options (Semua, Hanya Debit, Hanya Kredit, Kategori Tertentu)

## 🚢 Deploy ke Cloud

### Streamlit Cloud (Recommended)

1. Push code ke GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Deploy!

### Heroku

1. Buat `Procfile`:

```
web: streamlit run app.py --server.port=$PORT
```

2. Deploy:

```bash
heroku create your-app-name
git push heroku main
```

### Docker

1. Buat `Dockerfile`:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

2. Build dan run:

```bash
docker build -t bank-dashboard .
docker run -p 8501:8501 bank-dashboard
```

## 📝 Customization

### Menambah Kategori Baru

Edit `config.py`:

```python
CATEGORIES = [
    'Kategori Baru',
    # ... existing categories
]

CATEGORY_COLORS = {
    'Kategori Baru': '#HexColor',
    # ... existing colors
}
```

### Menambah Chart Baru

Buat function di `components/charts.py`:

```python
def new_chart(data, ...):
    fig, ax = plt.subplots(figsize=(10, 6))
    # Your chart logic
    return fig
```

### Menambah Page Baru

Buat file di `pages/`:

```
pages/4_🎯_New_Page.py
```

## 🤝 Contributing

Silakan fork dan buat pull request untuk improvement!

## 📄 License

MIT License - Feel free to use for your projects!

## 👨‍💻 Author

Built with ❤️ using Streamlit

---

**Happy Analyzing! 📊💰**
