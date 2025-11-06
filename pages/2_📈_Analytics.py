"""
Analytics Page - Analisis Mendalam dengan Berbagai Chart
"""

import streamlit as st
import pandas as pd
import numpy as np

# Import components
from components.charts import (
    pie_chart, bar_chart, line_chart, box_plot, 
    histogram_chart, area_chart, heatmap_chart
)
from components.filters import date_range_filter, category_filter, transaction_type_filter
from components.metrics import summary_metrics

# Import utilities
from utils import (
    load_data, filter_data, calculate_summary, 
    get_category_summary, get_monthly_summary
)
from config import CATEGORIES, TRANSACTION_TYPES, CATEGORY_COLORS

# Page config
st.set_page_config(
    page_title="Analytics | Bank Transaction",
    page_icon="📈",
    layout="wide"
)

def render_sidebar_filters():
    """Render filters di sidebar"""
    st.sidebar.header("🎯 Filter Data")
    
    # Submenu untuk analytics
    st.sidebar.subheader("📊 Menu Analisis")
    analysis_type = st.sidebar.radio(
        "Pilih Jenis Analisis:",
        ["Overview", "Kategori", "Time Series", "Distribusi", "Perbandingan"],
        help="Pilih jenis analisis yang ingin ditampilkan"
    )
    
    # Load data
    df = load_data()
    
    # Date range filter
    min_date = df['Tanggal'].min().date()
    max_date = df['Tanggal'].max().date()
    
    st.sidebar.subheader("📅 Periode")
    start_date, end_date = date_range_filter(min_date, max_date, key_prefix="analytics")
    
    # Category filter
    st.sidebar.subheader("🏷️ Kategori")
    selected_categories = category_filter(CATEGORIES, key="analytics_category", default=CATEGORIES)
    
    # Transaction type filter
    st.sidebar.subheader("💳 Tipe Transaksi")
    selected_types = transaction_type_filter(TRANSACTION_TYPES, key="analytics_type", default=TRANSACTION_TYPES)
    
    # Apply filters
    filtered_df = filter_data(
        df,
        start_date=start_date,
        end_date=end_date,
        categories=selected_categories,
        transaction_types=selected_types
    )
    
    st.sidebar.info(f"📊 Menampilkan **{len(filtered_df)}** dari **{len(df)}** transaksi")
    
    return filtered_df, df, analysis_type

def render_overview_analysis(df):
    """Render overview analysis"""
    st.header("📊 Overview Analysis")
    
    summary = calculate_summary(df)
    summary_metrics(summary)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💸 Breakdown Debit vs Kredit")
        
        type_summary = df.groupby('Tipe')['Jumlah'].sum()
        
        fig = pie_chart(
            data=type_summary.values,
            labels=type_summary.index,
            title="Proporsi Debit vs Kredit",
            colors=['#FF6B6B', '#82E0AA']
        )
        st.pyplot(fig)
    
    with col2:
        st.subheader("📊 Transaksi per Tipe")
        
        type_count = df.groupby('Tipe').size().reset_index()
        type_count.columns = ['Tipe', 'Jumlah']
        
        fig = bar_chart(
            data=type_count,
            x='Tipe',
            y='Jumlah',
            title="Jumlah Transaksi per Tipe"
        )
        st.pyplot(fig)

def render_category_analysis(df):
    """Render category analysis"""
    st.header("🏷️ Category Analysis")
    
    category_summary = get_category_summary(df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Total per Kategori")
        
        fig = bar_chart(
            data=category_summary,
            x='Kategori',
            y='Total',
            title="Total Transaksi per Kategori",
            horizontal=True
        )
        st.pyplot(fig)
    
    with col2:
        st.subheader("🥧 Distribusi Kategori")
        
        fig = pie_chart(
            data=category_summary['Total'].values,
            labels=category_summary['Kategori'].values,
            title="Distribusi per Kategori",
            colors=[CATEGORY_COLORS.get(cat, '#95A5A6') for cat in category_summary['Kategori']]
        )
        st.pyplot(fig)
    
    st.markdown("---")
    
    st.subheader("📦 Box Plot - Distribusi Jumlah per Kategori")
    
    fig = box_plot(
        data=df,
        x='Kategori',
        y='Jumlah',
        title="Distribusi Jumlah Transaksi per Kategori"
    )
    st.pyplot(fig)

def render_time_series_analysis(df):
    """Render time series analysis"""
    st.header("📈 Time Series Analysis")
    
    # Monthly trend
    st.subheader("📊 Trend Bulanan")
    
    monthly_summary = get_monthly_summary(df)
    
    if len(monthly_summary) > 0:
        fig = line_chart(
            data=monthly_summary,
            x='Bulan',
            y=['Income', 'Expense'],
            title="Trend Pemasukan dan Pengeluaran Bulanan"
        )
        st.pyplot(fig)
        
        st.markdown("---")
        
        # Area chart untuk balance
        st.subheader("💰 Balance Over Time")
        
        fig = area_chart(
            data=monthly_summary,
            x='Bulan',
            y=['Income', 'Expense'],
            title="Stacked Area: Income dan Expense"
        )
        st.pyplot(fig)
        
        st.markdown("---")
        
        # Daily transactions
        st.subheader("📅 Transaksi Harian")
        
        daily_df = df.groupby(df['Tanggal'].dt.date).agg({
            'Jumlah': 'sum',
            'Tipe': 'count'
        }).reset_index()
        daily_df.columns = ['Tanggal', 'Total Amount', 'Count']
        
        fig = line_chart(
            data=daily_df,
            x='Tanggal',
            y='Total Amount',
            title="Total Transaksi Harian"
        )
        st.pyplot(fig)

def render_distribution_analysis(df):
    """Render distribution analysis"""
    st.header("📊 Distribution Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Histogram - Distribusi Jumlah")
        
        fig = histogram_chart(
            data=df,
            column='Jumlah',
            bins=30,
            title="Distribusi Jumlah Transaksi"
        )
        st.pyplot(fig)
    
    with col2:
        st.subheader("📈 Statistik Deskriptif")
        
        stats_df = df['Jumlah'].describe().reset_index()
        stats_df.columns = ['Metric', 'Value']
        stats_df['Value'] = stats_df['Value'].apply(lambda x: f"Rp {x:,.0f}")
        
        st.dataframe(stats_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Heatmap - Transaksi per kategori dan bulan
    st.subheader("🔥 Heatmap - Kategori vs Bulan")
    
    df_heatmap = df.copy()
    df_heatmap['Bulan'] = df_heatmap['Tanggal'].dt.to_period('M').astype(str)
    
    pivot_table = df_heatmap.pivot_table(
        values='Jumlah',
        index='Kategori',
        columns='Bulan',
        aggfunc='sum',
        fill_value=0
    )
    
    if not pivot_table.empty:
        fig = heatmap_chart(
            data=pivot_table,
            title="Total Transaksi per Kategori dan Bulan",
            annot=False,
            fmt=".0f"
        )
        st.pyplot(fig)

def render_comparison_analysis(df):
    """Render comparison analysis"""
    st.header("🔄 Comparison Analysis")
    
    # Split data menjadi 2 periode
    df_sorted = df.sort_values('Tanggal')
    mid_idx = len(df_sorted) // 2
    
    df_period1 = df_sorted.iloc[:mid_idx]
    df_period2 = df_sorted.iloc[mid_idx:]
    
    period1_label = f"{df_period1['Tanggal'].min().strftime('%Y-%m-%d')} - {df_period1['Tanggal'].max().strftime('%Y-%m-%d')}"
    period2_label = f"{df_period2['Tanggal'].min().strftime('%Y-%m-%d')} - {df_period2['Tanggal'].max().strftime('%Y-%m-%d')}"
    
    st.info(f"📊 Membandingkan 2 periode:\n\n**Periode 1**: {period1_label}\n\n**Periode 2**: {period2_label}")
    
    # Summary comparison
    from components.tables import comparison_table
    
    summary1 = calculate_summary(df_period1)
    summary2 = calculate_summary(df_period2)
    
    st.subheader("💰 Perbandingan Summary")
    comparison_table(summary1, summary2, labels=["Periode 1", "Periode 2"])
    
    st.markdown("---")
    
    # Category comparison
    st.subheader("🏷️ Perbandingan Kategori")
    
    cat1 = get_category_summary(df_period1)
    cat2 = get_category_summary(df_period2)
    
    # Merge data
    comparison_df = pd.merge(
        cat1[['Kategori', 'Total']],
        cat2[['Kategori', 'Total']],
        on='Kategori',
        how='outer',
        suffixes=(' P1', ' P2')
    ).fillna(0)
    
    fig = bar_chart(
        data=comparison_df.melt(id_vars='Kategori', var_name='Periode', value_name='Total'),
        x='Kategori',
        y='Total',
        title="Perbandingan Total per Kategori"
    )
    
    # Manually create grouped bar chart
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(comparison_df['Kategori']))
    width = 0.35
    
    ax.bar(x - width/2, comparison_df['Total P1'], width, label='Periode 1', color='#FF6B6B')
    ax.bar(x + width/2, comparison_df['Total P2'], width, label='Periode 2', color='#4ECDC4')
    
    ax.set_xlabel('Kategori')
    ax.set_ylabel('Total')
    ax.set_title('Perbandingan Total per Kategori')
    ax.set_xticks(x)
    ax.set_xticklabels(comparison_df['Kategori'], rotation=45, ha='right')
    ax.legend()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    
    plt.tight_layout()
    st.pyplot(fig)

def main():
    """Main function untuk analytics page"""
    
    # Header
    st.title("📈 Analytics")
    st.markdown("Analisis mendalam dari data transaksi Anda")
    st.markdown("---")
    
    # Render filters dan get data
    filtered_df, original_df, analysis_type = render_sidebar_filters()
    
    # Check if data kosong
    if len(filtered_df) == 0:
        st.warning("⚠️ Tidak ada data untuk filter yang dipilih. Silakan ubah filter.")
        return
    
    # Render berdasarkan analysis type
    if analysis_type == "Overview":
        render_overview_analysis(filtered_df)
    elif analysis_type == "Kategori":
        render_category_analysis(filtered_df)
    elif analysis_type == "Time Series":
        render_time_series_analysis(filtered_df)
    elif analysis_type == "Distribusi":
        render_distribution_analysis(filtered_df)
    elif analysis_type == "Perbandingan":
        render_comparison_analysis(filtered_df)

if __name__ == "__main__":
    main()
