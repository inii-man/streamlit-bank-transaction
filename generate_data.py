import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed untuk reproducibility
np.random.seed(42)

# Generate 100 transaksi bank
n_transactions = 100

# Date range: 3 bulan terakhir
end_date = datetime.now()
start_date = end_date - timedelta(days=90)
date_range = pd.date_range(start=start_date, end=end_date, periods=n_transactions)

# Kategori transaksi
categories = ['Makanan & Minuman', 'Transport', 'Belanja', 'Tagihan', 'Hiburan', 
              'Kesehatan', 'Pendidikan', 'Gaji', 'Investasi', 'Lainnya']

# Tipe transaksi
transaction_types = ['Debit', 'Kredit']

# Deskripsi untuk setiap kategori
descriptions = {
    'Makanan & Minuman': ['Restoran ABC', 'Cafe XYZ', 'Supermarket', 'Warteg', 'McDonald\'s'],
    'Transport': ['Grab', 'Gojek', 'Bensin', 'Parkir', 'Tol'],
    'Belanja': ['Tokopedia', 'Shopee', 'Lazada', 'Alfamart', 'Indomaret'],
    'Tagihan': ['Listrik PLN', 'Air PDAM', 'Internet', 'Telepon', 'Streaming'],
    'Hiburan': ['Bioskop', 'Spotify', 'Netflix', 'Konser', 'Game'],
    'Kesehatan': ['Apotek', 'Rumah Sakit', 'Klinik', 'Vitamin', 'Gym'],
    'Pendidikan': ['Kursus', 'Buku', 'Seminar', 'Workshop', 'Pelatihan'],
    'Gaji': ['Gaji Bulanan', 'Bonus', 'THR', 'Freelance', 'Komisi'],
    'Investasi': ['Saham', 'Reksadana', 'Emas', 'Deposito', 'Crypto'],
    'Lainnya': ['Transfer', 'Tarik Tunai', 'Setor Tunai', 'Administrasi', 'Lain-lain']
}

# Generate data
data = []
saldo = 5000000  # Saldo awal 5 juta

for date in date_range:
    # Tentukan kategori
    category = np.random.choice(categories, p=[0.15, 0.10, 0.12, 0.08, 0.08, 
                                                0.05, 0.05, 0.10, 0.07, 0.20])
    
    # Tentukan tipe transaksi (Gaji dan Investasi biasanya Kredit)
    if category in ['Gaji', 'Investasi']:
        trans_type = 'Kredit'
        amount = np.random.randint(3000000, 10000000) if category == 'Gaji' else np.random.randint(100000, 2000000)
    else:
        trans_type = np.random.choice(['Debit'], p=[1.0])  # Kebanyakan debit
        if category == 'Tagihan':
            amount = np.random.randint(100000, 800000)
        elif category == 'Belanja':
            amount = np.random.randint(50000, 1500000)
        elif category == 'Makanan & Minuman':
            amount = np.random.randint(15000, 300000)
        elif category == 'Transport':
            amount = np.random.randint(10000, 200000)
        else:
            amount = np.random.randint(20000, 500000)
    
    # Update saldo
    if trans_type == 'Kredit':
        saldo += amount
    else:
        saldo -= amount
    
    # Pilih deskripsi random dari kategori
    description = np.random.choice(descriptions[category])
    
    data.append({
        'Tanggal': date.strftime('%Y-%m-%d'),
        'Kategori': category,
        'Tipe': trans_type,
        'Jumlah': amount,
        'Deskripsi': description,
        'Saldo': saldo
    })

# Buat DataFrame
df = pd.DataFrame(data)

# Simpan ke CSV
df.to_csv('data/bank_transactions.csv', index=False)
print(f"✅ Data transaksi berhasil dibuat: {len(df)} transaksi")
print(f"📁 File disimpan di: data/bank_transactions.csv")
print(f"\nPreview data:")
print(df.head(10))
