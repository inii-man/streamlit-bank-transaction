"""
Transactions Page - Detail Semua Transaksi dengan Filter Lengkap
"""

import streamlit as st
import pandas as pd

# Import components
from components.filters import (
    date_range_filter, category_filter, transaction_type_filter,
    amount_range_filter, search_filter
)
from components.tables import transaction_table, category_breakdown_table
from components.metrics import summary_metrics

# Import utilities
from utils import load_data, filter_data, calculate_summary, get_category_summary, format_currency
from config import CATEGORIES, TRANSACTION_TYPES

# Page config
st.set_page_config(
    page_title="Transactions | Bank Transaction",
    page_icon="💳",
    layout="wide"
)

def render_sidebar_filters():
    """Render filters di sidebar dengan submenu"""
    st.sidebar.header("🎯 Filter Transaksi")
    
    # Submenu untuk view options
    st.sidebar.subheader("👁️ Opsi Tampilan")
    
    view_option = st.sidebar.radio(
        "Pilih Tampilan:",
        ["Semua Transaksi", "Hanya Debit", "Hanya Kredit", "Kategori Tertentu"],
        help="Pilih cara menampilkan transaksi"
    )
    
    # Load data
    df = load_data()
    
    # Date range filter
    min_date = df['Tanggal'].min().date()
    max_date = df['Tanggal'].max().date()
    
    st.sidebar.subheader("📅 Periode")
    start_date, end_date = date_range_filter(min_date, max_date, key_prefix="transactions")
    
    # Category filter
    st.sidebar.subheader("🏷️ Kategori")
    
    if view_option == "Kategori Tertentu":
        selected_categories = category_filter(CATEGORIES, key="trans_category", default=[])
    else:
        selected_categories = category_filter(CATEGORIES, key="trans_category", default=CATEGORIES)
    
    # Transaction type filter
    st.sidebar.subheader("💳 Tipe Transaksi")
    
    if view_option == "Hanya Debit":
        selected_types = ["Debit"]
    elif view_option == "Hanya Kredit":
        selected_types = ["Kredit"]
    else:
        selected_types = transaction_type_filter(TRANSACTION_TYPES, key="trans_type", default=TRANSACTION_TYPES)
    
    # Amount range filter
    st.sidebar.subheader("💰 Range Jumlah")
    min_amount = df['Jumlah'].min()
    max_amount = df['Jumlah'].max()
    amount_range = amount_range_filter(min_amount, max_amount, key="trans_amount")
    
    # Search filter
    st.sidebar.subheader("🔍 Pencarian")
    search_query = search_filter(placeholder="Cari deskripsi...", key="trans_search")
    
    # Apply filters
    filtered_df = filter_data(
        df,
        start_date=start_date,
        end_date=end_date,
        categories=selected_categories,
        transaction_types=selected_types
    )
    
    # Apply amount filter
    filtered_df = filtered_df[
        (filtered_df['Jumlah'] >= amount_range[0]) & 
        (filtered_df['Jumlah'] <= amount_range[1])
    ]
    
    # Apply search filter
    if search_query:
        filtered_df = filtered_df[
            filtered_df['Deskripsi'].str.lower().str.contains(search_query, na=False)
        ]
    
    # Show info
    st.sidebar.info(f"📊 Menampilkan **{len(filtered_df)}** dari **{len(df)}** transaksi")
    
    # Export options
    st.sidebar.subheader("📥 Export Data")
    
    if len(filtered_df) > 0:
        # Convert to CSV
        csv = filtered_df.to_csv(index=False)
        
        st.sidebar.download_button(
            label="⬇️ Download CSV",
            data=csv,
            file_name="transactions_export.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    return filtered_df, df, view_option

def render_transaction_details(df):
    """Render detail transaksi dengan berbagai view"""
    
    st.subheader("📋 Detail Transaksi")
    
    # Tabs untuk berbagai view
    tab1, tab2, tab3 = st.tabs(["📊 Tabel", "🏷️ Per Kategori", "📈 Statistik"])
    
    with tab1:
        # Sorting options
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            sort_by = st.selectbox(
                "Urutkan berdasarkan:",
                ["Tanggal", "Jumlah", "Kategori", "Tipe"],
                key="sort_by"
            )
        
        with col2:
            sort_order = st.radio(
                "Urutan:",
                ["Descending", "Ascending"],
                horizontal=True,
                key="sort_order"
            )
        
        with col3:
            show_index = st.checkbox("Tampilkan Index", value=False)
        
        # Sort dataframe
        df_sorted = df.sort_values(
            by=sort_by,
            ascending=(sort_order == "Ascending")
        )
        
        # Display table
        transaction_table(df_sorted, show_index=show_index, height=500)
        
        # Summary di bawah table
        st.markdown("---")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Transaksi", len(df))
        
        with col2:
            total_debit = df[df['Tipe'] == 'Debit']['Jumlah'].sum()
            st.metric("Total Debit", format_currency(total_debit))
        
        with col3:
            total_kredit = df[df['Tipe'] == 'Kredit']['Jumlah'].sum()
            st.metric("Total Kredit", format_currency(total_kredit))
        
        with col4:
            avg_amount = df['Jumlah'].mean()
            st.metric("Rata-rata", format_currency(avg_amount))
    
    with tab2:
        # Category breakdown
        category_summary = get_category_summary(df)
        
        if len(category_summary) > 0:
            category_breakdown_table(category_summary)
        else:
            st.info("Tidak ada data kategori untuk ditampilkan")
    
    with tab3:
        # Statistics
        st.markdown("#### 📊 Statistik Deskriptif")
        
        stats_df = df['Jumlah'].describe().reset_index()
        stats_df.columns = ['Metric', 'Value']
        
        # Format display
        stats_display = []
        for _, row in stats_df.iterrows():
            metric = row['Metric']
            value = row['Value']
            
            if metric == 'count':
                stats_display.append({'Metrik': 'Jumlah Data', 'Nilai': f"{int(value):,}"})
            else:
                stats_display.append({'Metrik': metric.capitalize(), 'Nilai': format_currency(value)})
        
        st.dataframe(
            pd.DataFrame(stats_display),
            use_container_width=True,
            hide_index=True
        )
        
        st.markdown("---")
        
        # Additional stats
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 💸 Statistik Debit")
            debit_df = df[df['Tipe'] == 'Debit']
            
            if len(debit_df) > 0:
                st.metric("Total Debit", format_currency(debit_df['Jumlah'].sum()))
                st.metric("Rata-rata Debit", format_currency(debit_df['Jumlah'].mean()))
                st.metric("Jumlah Transaksi", len(debit_df))
            else:
                st.info("Tidak ada transaksi debit")
        
        with col2:
            st.markdown("#### 💰 Statistik Kredit")
            kredit_df = df[df['Tipe'] == 'Kredit']
            
            if len(kredit_df) > 0:
                st.metric("Total Kredit", format_currency(kredit_df['Jumlah'].sum()))
                st.metric("Rata-rata Kredit", format_currency(kredit_df['Jumlah'].mean()))
                st.metric("Jumlah Transaksi", len(kredit_df))
            else:
                st.info("Tidak ada transaksi kredit")

def main():
    """Main function untuk transactions page"""
    
    # Header
    st.title("💳 Transactions")
    st.markdown("Detail lengkap semua transaksi dengan filter dan pencarian")
    st.markdown("---")
    
    # Render filters dan get data
    filtered_df, original_df, view_option = render_sidebar_filters()
    
    # Check if data kosong
    if len(filtered_df) == 0:
        st.warning("⚠️ Tidak ada transaksi yang sesuai dengan filter. Silakan ubah filter.")
        return
    
    # Summary metrics
    st.subheader("💰 Ringkasan")
    summary = calculate_summary(filtered_df)
    summary_metrics(summary)
    
    st.markdown("---")
    
    # Transaction details
    render_transaction_details(filtered_df)
    
    st.markdown("---")
    
    # Info footer
    st.info(f"""
        💡 **Tips Penggunaan:**
        - Gunakan filter di sidebar untuk menyaring transaksi
        - Gunakan pencarian untuk menemukan transaksi spesifik
        - Klik tab berbeda untuk melihat data dari perspektif yang berbeda
        - Download CSV untuk analisis lebih lanjut di Excel
    """)

if __name__ == "__main__":
    main()
