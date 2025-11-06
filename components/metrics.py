"""
Reusable components untuk metrics cards
"""

import streamlit as st
from utils import format_currency

def metric_card(label, value, delta=None, delta_color="normal", help_text=None):
    """
    Display metric card dengan styling
    
    Args:
        label: Label metric
        value: Nilai metric
        delta: Perubahan nilai (optional)
        delta_color: Warna delta (normal, inverse, off)
        help_text: Text bantuan (optional)
    """
    st.metric(
        label=label,
        value=value,
        delta=delta,
        delta_color=delta_color,
        help=help_text
    )

def summary_metrics(summary_data):
    """
    Display summary metrics dalam 4 kolom
    
    Args:
        summary_data: Dictionary berisi total_income, total_expense, balance, transaction_count
    """
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Total Pemasukan",
            value=format_currency(summary_data['total_income']),
            help="Total pemasukan (Kredit)"
        )
    
    with col2:
        st.metric(
            label="💸 Total Pengeluaran",
            value=format_currency(summary_data['total_expense']),
            help="Total pengeluaran (Debit)"
        )
    
    with col3:
        balance = summary_data['balance']
        st.metric(
            label="💵 Saldo Bersih",
            value=format_currency(balance),
            delta=format_currency(balance),
            delta_color="normal" if balance >= 0 else "inverse",
            help="Selisih pemasukan dan pengeluaran"
        )
    
    with col4:
        st.metric(
            label="📊 Total Transaksi",
            value=f"{summary_data['transaction_count']:,}",
            help="Jumlah total transaksi"
        )

def category_metrics(category_summary, top_n=5):
    """
    Display top N kategori dalam kolom
    
    Args:
        category_summary: DataFrame berisi ringkasan per kategori
        top_n: Jumlah kategori yang ditampilkan
    """
    st.subheader(f"🏆 Top {top_n} Kategori")
    
    top_categories = category_summary.head(top_n)
    
    cols = st.columns(min(top_n, len(top_categories)))
    
    for idx, (col, row) in enumerate(zip(cols, top_categories.itertuples())):
        with col:
            st.metric(
                label=f"#{idx+1} {row.Kategori}",
                value=format_currency(row.Total),
                delta=f"{row._3} transaksi",
                help=f"Total pengeluaran untuk {row.Kategori}"
            )

def statistics_metrics(stats):
    """
    Display statistik descriptive
    
    Args:
        stats: Dictionary berisi mean, median, max, min
    """
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📊 Rata-rata",
            value=format_currency(stats['mean']),
            help="Nilai rata-rata transaksi"
        )
    
    with col2:
        st.metric(
            label="📊 Median",
            value=format_currency(stats['median']),
            help="Nilai tengah transaksi"
        )
    
    with col3:
        st.metric(
            label="📈 Maksimum",
            value=format_currency(stats['max']),
            help="Transaksi terbesar"
        )
    
    with col4:
        st.metric(
            label="📉 Minimum",
            value=format_currency(stats['min']),
            help="Transaksi terkecil"
        )
