# 🚀 Quick Start Guide

## Instalasi Cepat

### 1. Clone atau Download Project

```bash
cd /path/to/project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`

## 📱 Navigasi Aplikasi

### Home (app.py)

- Landing page dengan overview
- Quick stats
- Preview transaksi terbaru

### 📊 Dashboard (Sidebar → Dashboard)

Klik menu **Dashboard** di sidebar untuk melihat:

- Summary metrics (pemasukan, pengeluaran, saldo, jumlah transaksi)
- Distribusi kategori (pie chart & bar chart)
- Trend bulanan (line chart)
- Top transaksi terbesar
- Statistik deskriptif

**Filter yang tersedia:**

- 📅 Date range
- 🏷️ Kategori (multi-select)
- 💳 Tipe transaksi (Debit/Kredit)

### 📈 Analytics (Sidebar → Analytics)

Klik menu **Analytics** di sidebar, lalu pilih sub-menu:

1. **Overview**: Breakdown debit vs kredit
2. **Kategori**: Analisis per kategori dengan box plot
3. **Time Series**: Trend dan area chart
4. **Distribusi**: Histogram dan heatmap
5. **Perbandingan**: Compare 2 periode

**Filter yang tersedia:**

- Semua filter dari Dashboard
- Plus: pilihan jenis analisis di sidebar

### 💳 Transactions (Sidebar → Transactions)

Klik menu **Transactions** di sidebar untuk melihat semua transaksi.

**Sub-menu View Options:**

- Semua Transaksi
- Hanya Debit
- Hanya Kredit
- Kategori Tertentu

**Filter yang tersedia:**

- 📅 Date range
- 🏷️ Kategori
- 💳 Tipe transaksi
- 💰 Amount range (slider)
- 🔍 Search (cari deskripsi)

**Fitur tambahan:**

- Sorting (by date, amount, category, type)
- 3 tabs view: Tabel, Per Kategori, Statistik
- Download CSV

## 🎯 Tips Penggunaan

### 1. Filter Data

Gunakan sidebar untuk filter data:

- Pilih date range untuk periode tertentu
- Select/deselect kategori yang ingin dilihat
- Pilih Debit saja atau Kredit saja

### 2. Export Data

Di halaman Transactions:

1. Apply filter sesuai kebutuhan
2. Scroll ke bawah sidebar
3. Klik tombol "⬇️ Download CSV"

### 3. Analisis Mendalam

Di halaman Analytics:

1. Pilih jenis analisis di sidebar (Overview, Kategori, dll)
2. Apply filter
3. Explore berbagai chart

### 4. Sort Transaksi

Di halaman Transactions:

1. Pilih kolom untuk sorting
2. Pilih ascending atau descending
3. Toggle show index jika diperlukan

## 🔧 Troubleshooting

### Port sudah digunakan

Jika port 8501 sudah digunakan:

```bash
streamlit run app.py --server.port 8502
```

### Module not found

Install ulang dependencies:

```bash
pip install -r requirements.txt
```

### Data tidak muncul

Pastikan file `data/bank_transactions.csv` ada. Jika tidak:

```bash
python generate_data.py
```

## 🎨 Customization

### Mengganti Theme

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF4B4B"  # Ganti warna
backgroundColor = "#FFFFFF"
```

### Menambah Data

1. Edit `data/bank_transactions.csv` atau
2. Modify `generate_data.py` dan run:

```bash
python generate_data.py
```

### Menambah Kategori

Edit `config.py`:

```python
CATEGORIES = [
    'Kategori Baru',
    # ... existing
]
```

## 📊 Struktur Data CSV

Format yang diperlukan:

```csv
Tanggal,Kategori,Tipe,Jumlah,Deskripsi,Saldo
2025-08-08,Tagihan,Debit,359178,Streaming,4640822
```

**Kolom:**

- **Tanggal**: YYYY-MM-DD format
- **Kategori**: Salah satu dari CATEGORIES di config.py
- **Tipe**: "Debit" atau "Kredit"
- **Jumlah**: Nominal (integer)
- **Deskripsi**: Text deskripsi
- **Saldo**: Saldo setelah transaksi (optional untuk display)

## 🚢 Deploy ke Production

### Streamlit Cloud (Gratis & Mudah)

1. Push ke GitHub
2. Kunjungi https://share.streamlit.io
3. Connect repository
4. Deploy!

### Heroku

```bash
heroku create your-app-name
git push heroku main
```

### Docker

```bash
docker build -t bank-dashboard .
docker run -p 8501:8501 bank-dashboard
```

## 📞 Need Help?

Cek `README.md` untuk dokumentasi lengkap atau lihat code untuk memahami cara kerja setiap component.

---

**Selamat menggunakan Bank Transaction Dashboard! 💰📊**
