"""
Reusable components untuk filters
"""

import streamlit as st
from datetime import datetime, timedelta

def date_range_filter(min_date, max_date, key_prefix="date"):
    """
    Create date range filter
    
    Args:
        min_date: Tanggal minimum
        max_date: Tanggal maksimum
        key_prefix: Prefix untuk key
    
    Returns:
        Tuple (start_date, end_date)
    """
    col1, col2 = st.columns(2)
    
    with col1:
        start_date = st.date_input(
            "📅 Dari Tanggal",
            value=min_date,
            min_value=min_date,
            max_value=max_date,
            key=f"{key_prefix}_start"
        )
    
    with col2:
        end_date = st.date_input(
            "📅 Sampai Tanggal",
            value=max_date,
            min_value=min_date,
            max_value=max_date,
            key=f"{key_prefix}_end"
        )
    
    return start_date, end_date

def category_filter(categories, key="category_filter", default=None):
    """
    Create multiselect category filter
    
    Args:
        categories: List kategori yang tersedia
        key: Key untuk widget
        default: Default selected categories
    
    Returns:
        List kategori yang dipilih
    """
    selected = st.multiselect(
        "🏷️ Pilih Kategori",
        options=categories,
        default=default or categories,
        key=key,
        help="Pilih satu atau lebih kategori untuk difilter"
    )
    
    return selected

def transaction_type_filter(transaction_types, key="type_filter", default=None):
    """
    Create multiselect transaction type filter
    
    Args:
        transaction_types: List tipe transaksi yang tersedia
        key: Key untuk widget
        default: Default selected types
    
    Returns:
        List tipe transaksi yang dipilih
    """
    selected = st.multiselect(
        "💳 Pilih Tipe Transaksi",
        options=transaction_types,
        default=default or transaction_types,
        key=key,
        help="Pilih Debit (pengeluaran) atau Kredit (pemasukan)"
    )
    
    return selected

def amount_range_filter(min_amount, max_amount, key="amount_filter"):
    """
    Create amount range slider
    
    Args:
        min_amount: Jumlah minimum
        max_amount: Jumlah maksimum
        key: Key untuk widget
    
    Returns:
        Tuple (min_selected, max_selected)
    """
    selected_range = st.slider(
        "💰 Range Jumlah Transaksi",
        min_value=float(min_amount),
        max_value=float(max_amount),
        value=(float(min_amount), float(max_amount)),
        key=key,
        format="Rp %.0f",
        help="Geser untuk memilih range jumlah transaksi"
    )
    
    return selected_range

def quick_date_filter(key="quick_date"):
    """
    Create quick date range selector
    
    Args:
        key: Key untuk widget
    
    Returns:
        Tuple (start_date, end_date) atau None jika Custom dipilih
    """
    today = datetime.now().date()
    
    options = {
        "Hari Ini": (today, today),
        "7 Hari Terakhir": (today - timedelta(days=7), today),
        "30 Hari Terakhir": (today - timedelta(days=30), today),
        "3 Bulan Terakhir": (today - timedelta(days=90), today),
        "Custom": None
    }
    
    selected = st.selectbox(
        "⚡ Quick Filter Tanggal",
        options=list(options.keys()),
        key=key
    )
    
    return options[selected]

def search_filter(placeholder="Cari transaksi...", key="search"):
    """
    Create search text input
    
    Args:
        placeholder: Placeholder text
        key: Key untuk widget
    
    Returns:
        Search query string
    """
    query = st.text_input(
        "🔍 Cari",
        placeholder=placeholder,
        key=key,
        help="Cari berdasarkan deskripsi transaksi"
    )
    
    return query.lower() if query else ""

def reset_filters_button(key="reset"):
    """
    Create reset filters button
    
    Args:
        key: Key untuk widget
    
    Returns:
        Boolean - True jika tombol diklik
    """
    return st.button(
        "🔄 Reset Filter",
        key=key,
        use_container_width=True,
        help="Reset semua filter ke default"
    )
