"""
Utility functions untuk data processing dan formatting
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from config import DATA_PATH, CURRENCY_FORMAT, DATE_FORMAT

def load_data():
    """Load data transaksi dari CSV"""
    try:
        df = pd.read_csv(DATA_PATH)
        df['Tanggal'] = pd.to_datetime(df['Tanggal'])
        return df
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def format_currency(amount):
    """Format angka ke format currency Indonesia"""
    return CURRENCY_FORMAT.format(amount)

def format_number(number):
    """Format angka dengan separator"""
    return f"{number:,.0f}"

def get_date_range(df):
    """Get tanggal minimum dan maksimum dari data"""
    return df['Tanggal'].min(), df['Tanggal'].max()

def filter_data(df, start_date=None, end_date=None, categories=None, transaction_types=None):
    """
    Filter dataframe berdasarkan kriteria yang diberikan
    
    Args:
        df: DataFrame yang akan difilter
        start_date: Tanggal mulai
        end_date: Tanggal akhir
        categories: List kategori yang dipilih
        transaction_types: List tipe transaksi yang dipilih
    
    Returns:
        DataFrame yang sudah difilter
    """
    filtered_df = df.copy()
    
    # Filter by date range
    if start_date:
        filtered_df = filtered_df[filtered_df['Tanggal'] >= pd.to_datetime(start_date)]
    if end_date:
        filtered_df = filtered_df[filtered_df['Tanggal'] <= pd.to_datetime(end_date)]
    
    # Filter by categories
    if categories and len(categories) > 0:
        filtered_df = filtered_df[filtered_df['Kategori'].isin(categories)]
    
    # Filter by transaction types
    if transaction_types and len(transaction_types) > 0:
        filtered_df = filtered_df[filtered_df['Tipe'].isin(transaction_types)]
    
    return filtered_df

def calculate_summary(df):
    """
    Hitung summary statistics dari dataframe
    
    Returns:
        Dictionary berisi total income, expense, balance, dan transaction count
    """
    total_income = df[df['Tipe'] == 'Kredit']['Jumlah'].sum()
    total_expense = df[df['Tipe'] == 'Debit']['Jumlah'].sum()
    balance = total_income - total_expense
    transaction_count = len(df)
    
    return {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'transaction_count': transaction_count
    }

def get_category_summary(df):
    """
    Get summary per kategori
    
    Returns:
        DataFrame berisi total amount per kategori
    """
    category_summary = df.groupby('Kategori')['Jumlah'].agg(['sum', 'count']).reset_index()
    category_summary.columns = ['Kategori', 'Total', 'Jumlah Transaksi']
    category_summary = category_summary.sort_values('Total', ascending=False)
    return category_summary

def get_monthly_summary(df):
    """
    Get summary per bulan
    
    Returns:
        DataFrame berisi income dan expense per bulan
    """
    df_monthly = df.copy()
    df_monthly['Bulan'] = df_monthly['Tanggal'].dt.to_period('M')
    
    monthly_income = df_monthly[df_monthly['Tipe'] == 'Kredit'].groupby('Bulan')['Jumlah'].sum()
    monthly_expense = df_monthly[df_monthly['Tipe'] == 'Debit'].groupby('Bulan')['Jumlah'].sum()
    
    monthly_summary = pd.DataFrame({
        'Income': monthly_income,
        'Expense': monthly_expense
    }).fillna(0)
    
    monthly_summary['Balance'] = monthly_summary['Income'] - monthly_summary['Expense']
    monthly_summary.index = monthly_summary.index.astype(str)
    
    return monthly_summary.reset_index()

def get_daily_transactions(df):
    """
    Get jumlah transaksi per hari
    
    Returns:
        DataFrame berisi count transaksi per hari
    """
    daily = df.groupby(df['Tanggal'].dt.date).size().reset_index()
    daily.columns = ['Tanggal', 'Jumlah Transaksi']
    return daily

def calculate_statistics(df):
    """
    Hitung statistik descriptive
    
    Returns:
        Dictionary berisi mean, median, max, min amount
    """
    amounts = df['Jumlah']
    
    return {
        'mean': amounts.mean(),
        'median': amounts.median(),
        'max': amounts.max(),
        'min': amounts.min(),
        'std': amounts.std()
    }
