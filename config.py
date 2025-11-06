"""
Config file untuk menyimpan constants dan konfigurasi aplikasi
"""

# Konfigurasi umum
APP_TITLE = "Bank Transaction Dashboard"
APP_ICON = "💰"
PAGE_LAYOUT = "wide"

# Path data
DATA_PATH = "data/bank_transactions.csv"

# Kategori transaksi
CATEGORIES = [
    'Makanan & Minuman', 
    'Transport', 
    'Belanja', 
    'Tagihan', 
    'Hiburan',
    'Kesehatan', 
    'Pendidikan', 
    'Gaji', 
    'Investasi', 
    'Lainnya'
]

# Tipe transaksi
TRANSACTION_TYPES = ['Debit', 'Kredit']

# Color palette untuk charts
COLOR_PALETTE = {
    'primary': '#FF4B4B',
    'secondary': '#0068C9',
    'success': '#00C851',
    'warning': '#FFA900',
    'danger': '#FF4444',
    'info': '#33B5E5',
}

# Chart colors untuk kategori
CATEGORY_COLORS = {
    'Makanan & Minuman': '#FF6B6B',
    'Transport': '#4ECDC4',
    'Belanja': '#45B7D1',
    'Tagihan': '#FFA07A',
    'Hiburan': '#98D8C8',
    'Kesehatan': '#F7DC6F',
    'Pendidikan': '#BB8FCE',
    'Gaji': '#82E0AA',
    'Investasi': '#85C1E2',
    'Lainnya': '#95A5A6',
}

# Format currency
CURRENCY_FORMAT = "Rp {:,.0f}"

# Date format
DATE_FORMAT = "%Y-%m-%d"
DISPLAY_DATE_FORMAT = "%d %B %Y"
