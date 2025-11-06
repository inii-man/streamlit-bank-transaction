"""
Main App - Bank Transaction Dashboard
Multi-page Streamlit app dengan sidebar navigation
"""

import streamlit as st
from config import APP_TITLE, APP_ICON, PAGE_LAYOUT
from utils import load_data

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=PAGE_LAYOUT,
    initial_sidebar_state="expanded"
)

# Custom CSS untuk styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    """Main function untuk menampilkan home page"""
    
    # Load data
    try:
        df = load_data()
        
        # Simpan di session state
        if 'data' not in st.session_state:
            st.session_state['data'] = df
        
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        st.stop()
    
    # Header
    st.markdown(f'<div class="main-header">{APP_ICON} {APP_TITLE}</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Dashboard Analisis Transaksi Bank</div>', unsafe_allow_html=True)
    
    # Welcome section
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ### 👋 Selamat Datang!
        
        Dashboard ini membantu Anda untuk:
        - 📊 **Memantau transaksi** keuangan secara real-time
        - 📈 **Menganalisis pola** pengeluaran dan pemasukan
        - 🎯 **Mengelola budget** dengan lebih efektif
        - 📉 **Memvisualisasikan** data keuangan Anda
        
        **Gunakan sidebar di kiri** untuk navigasi ke halaman lain:
        - **Dashboard**: Overview transaksi dan statistik utama
        - **Analytics**: Analisis mendalam dengan berbagai chart
        - **Transactions**: Detail semua transaksi dengan filter lengkap
        """)
        
        st.info("💡 **Tips**: Gunakan filter di sidebar untuk menyaring data sesuai kebutuhan Anda!")
    
    st.markdown("---")
    
    # Quick stats
    st.subheader("📊 Quick Stats")
    
    from components.metrics import summary_metrics
    from utils import calculate_summary
    
    summary = calculate_summary(df)
    summary_metrics(summary)
    
    st.markdown("---")
    
    # Recent transactions preview
    st.subheader("🕐 Transaksi Terbaru")
    
    recent_df = df.sort_values('Tanggal', ascending=False).head(5)
    
    from components.tables import transaction_table
    transaction_table(recent_df, height=250)
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
        <div style='text-align: center; color: #666; padding: 2rem;'>
            <p>💰 Bank Transaction Dashboard | Built with Streamlit</p>
            <p>Data diperbarui secara real-time</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
