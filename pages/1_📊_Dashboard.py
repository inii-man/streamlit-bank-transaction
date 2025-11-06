"""
Dashboard Page - Overview dan Summary
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Import components
from components.metrics import summary_metrics, category_metrics, statistics_metrics
from components.charts import pie_chart, line_chart, bar_chart
from components.filters import date_range_filter, category_filter, transaction_type_filter
from components.tables import top_transactions_table

# Import utilities
from utils import load_data, filter_data, calculate_summary, get_category_summary, get_monthly_summary, calculate_statistics
from config import CATEGORIES, TRANSACTION_TYPES, CATEGORY_COLORS

# Page config
st.set_page_config(
    page_title="Dashboard | Bank Transaction",
    page_icon="📊",
    layout="wide"
)

def render_sidebar_filters():
    """Render filters di sidebar"""
    st.sidebar.header("🎯 Filter Data")
    
    # Load data
    df = load_data()
    
    # Date range filter
    min_date = df['Tanggal'].min().date()
    max_date = df['Tanggal'].max().date()
    
    st.sidebar.subheader("📅 Periode")
    start_date, end_date = date_range_filter(min_date, max_date, key_prefix="dashboard")
    
    # Category filter
    st.sidebar.subheader("🏷️ Kategori")
    selected_categories = category_filter(CATEGORIES, key="dashboard_category", default=CATEGORIES)
    
    # Transaction type filter
    st.sidebar.subheader("💳 Tipe Transaksi")
    selected_types = transaction_type_filter(TRANSACTION_TYPES, key="dashboard_type", default=TRANSACTION_TYPES)
    
    # Apply filters
    filtered_df = filter_data(
        df,
        start_date=start_date,
        end_date=end_date,
        categories=selected_categories,
        transaction_types=selected_types
    )
    
    # Show info
    st.sidebar.info(f"📊 Menampilkan **{len(filtered_df)}** dari **{len(df)}** transaksi")
    
    return filtered_df, df

def main():
    """Main function untuk dashboard page"""
    
    # Header
    st.title("📊 Dashboard")
    st.markdown("Overview lengkap dari transaksi keuangan Anda")
    st.markdown("---")
    
    # Render filters dan get data
    filtered_df, original_df = render_sidebar_filters()
    
    # Check if data kosong
    if len(filtered_df) == 0:
        st.warning("⚠️ Tidak ada data untuk filter yang dipilih. Silakan ubah filter.")
        return
    
    # Summary metrics
    st.subheader("💰 Ringkasan Keuangan")
    summary = calculate_summary(filtered_df)
    summary_metrics(summary)
    
    st.markdown("---")
    
    # Two columns layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Distribusi Kategori")
        
        # Category breakdown
        category_summary = get_category_summary(filtered_df[filtered_df['Tipe'] == 'Debit'])
        
        if len(category_summary) > 0:
            # Pie chart
            fig = pie_chart(
                data=category_summary['Total'].values,
                labels=category_summary['Kategori'].values,
                title="Pengeluaran per Kategori",
                colors=[CATEGORY_COLORS.get(cat, '#95A5A6') for cat in category_summary['Kategori']]
            )
            st.pyplot(fig)
        else:
            st.info("Tidak ada data pengeluaran untuk ditampilkan")
    
    with col2:
        st.subheader("📈 Top 5 Kategori Pengeluaran")
        
        if len(category_summary) > 0:
            # Bar chart
            top_5 = category_summary.head(5)
            fig = bar_chart(
                data=top_5,
                x='Kategori',
                y='Total',
                title="Top 5 Pengeluaran Terbesar"
            )
            st.pyplot(fig)
        else:
            st.info("Tidak ada data untuk ditampilkan")
    
    st.markdown("---")
    
    # Monthly trend
    st.subheader("📈 Trend Bulanan")
    
    monthly_summary = get_monthly_summary(filtered_df)
    
    if len(monthly_summary) > 0:
        fig = line_chart(
            data=monthly_summary,
            x='Bulan',
            y=['Income', 'Expense', 'Balance'],
            title="Pemasukan, Pengeluaran, dan Saldo per Bulan"
        )
        st.pyplot(fig)
    else:
        st.info("Tidak ada data trend bulanan")
    
    st.markdown("---")
    
    # Statistics
    st.subheader("📊 Statistik Transaksi")
    stats = calculate_statistics(filtered_df)
    statistics_metrics(stats)
    
    st.markdown("---")
    
    # Top transactions
    col1, col2 = st.columns(2)
    
    with col1:
        top_transactions_table(filtered_df, n=5, transaction_type="Debit")
    
    with col2:
        top_transactions_table(filtered_df, n=5, transaction_type="Kredit")
    
    st.markdown("---")
    
    # Category metrics
    if len(category_summary) > 0:
        category_metrics(category_summary, top_n=5)

if __name__ == "__main__":
    main()
