"""
Reusable components untuk tables
"""

import streamlit as st
import pandas as pd
from utils import format_currency

def transaction_table(df, show_index=False, height=400):
    """
    Display transaction table dengan formatting
    
    Args:
        df: DataFrame transaksi
        show_index: Show index column
        height: Tinggi tabel
    """
    # Format untuk display
    df_display = df.copy()
    
    # Format tanggal
    df_display['Tanggal'] = pd.to_datetime(df_display['Tanggal']).dt.strftime('%d-%m-%Y')
    
    # Format jumlah
    df_display['Jumlah'] = df_display['Jumlah'].apply(format_currency)
    
    # Format saldo jika ada
    if 'Saldo' in df_display.columns:
        df_display['Saldo'] = df_display['Saldo'].apply(format_currency)
    
    # Display dengan styling
    st.dataframe(
        df_display,
        use_container_width=True,
        height=height,
        hide_index=not show_index
    )

def summary_table(df, title=None):
    """
    Display summary table
    
    Args:
        df: DataFrame summary
        title: Judul tabel
    """
    if title:
        st.subheader(title)
    
    # Format kolom yang berisi angka currency
    df_display = df.copy()
    
    for col in df_display.columns:
        if df_display[col].dtype in ['int64', 'float64'] and 'Jumlah' not in col:
            if df_display[col].max() > 1000:  # Kemungkinan currency
                df_display[col] = df_display[col].apply(format_currency)
    
    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True
    )

def category_breakdown_table(category_summary):
    """
    Display category breakdown table dengan progress bar
    
    Args:
        category_summary: DataFrame berisi ringkasan per kategori
    """
    st.subheader("📊 Breakdown per Kategori")
    
    total_all = category_summary['Total'].sum()
    
    for idx, row in category_summary.iterrows():
        col1, col2, col3 = st.columns([3, 2, 1])
        
        with col1:
            st.write(f"**{row['Kategori']}**")
        
        with col2:
            percentage = (row['Total'] / total_all * 100) if total_all > 0 else 0
            st.progress(percentage / 100)
        
        with col3:
            st.write(format_currency(row['Total']))
        
        st.write(f"*{row['Jumlah Transaksi']} transaksi ({percentage:.1f}%)*")
        st.divider()

def top_transactions_table(df, n=10, transaction_type=None):
    """
    Display top N transactions
    
    Args:
        df: DataFrame transaksi
        n: Jumlah transaksi yang ditampilkan
        transaction_type: Filter by type (Debit/Kredit)
    """
    df_filtered = df.copy()
    
    if transaction_type:
        df_filtered = df_filtered[df_filtered['Tipe'] == transaction_type]
    
    # Sort by amount descending
    top_df = df_filtered.nlargest(n, 'Jumlah')[['Tanggal', 'Kategori', 'Deskripsi', 'Jumlah', 'Tipe']]
    
    st.subheader(f"🔝 Top {n} Transaksi Terbesar" + (f" ({transaction_type})" if transaction_type else ""))
    
    transaction_table(top_df, height=300)

def comparison_table(data1, data2, labels=["Periode 1", "Periode 2"]):
    """
    Display comparison table untuk dua periode
    
    Args:
        data1: Dictionary summary untuk periode 1
        data2: Dictionary summary untuk periode 2
        labels: Labels untuk kedua periode
    """
    comparison_df = pd.DataFrame({
        'Metrik': ['Total Pemasukan', 'Total Pengeluaran', 'Saldo Bersih', 'Jumlah Transaksi'],
        labels[0]: [
            format_currency(data1['total_income']),
            format_currency(data1['total_expense']),
            format_currency(data1['balance']),
            f"{data1['transaction_count']:,}"
        ],
        labels[1]: [
            format_currency(data2['total_income']),
            format_currency(data2['total_expense']),
            format_currency(data2['balance']),
            f"{data2['transaction_count']:,}"
        ]
    })
    
    st.dataframe(
        comparison_df,
        use_container_width=True,
        hide_index=True
    )
