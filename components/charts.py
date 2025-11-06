"""
Reusable components untuk charts menggunakan matplotlib dan seaborn
"""

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from config import CATEGORY_COLORS, COLOR_PALETTE

# Set style seaborn
sns.set_style("whitegrid")
sns.set_palette("husl")

def pie_chart(data, labels, title="Pie Chart", colors=None):
    """
    Create pie chart
    
    Args:
        data: Array atau Series data
        labels: Array atau list labels
        title: Judul chart
        colors: List warna (optional)
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Filter data yang > 0
    mask = data > 0
    data_filtered = data[mask]
    labels_filtered = [labels[i] for i in range(len(labels)) if mask[i]]
    
    if colors:
        colors_filtered = [colors[i] for i in range(len(colors)) if mask[i]]
    else:
        colors_filtered = None
    
    wedges, texts, autotexts = ax.pie(
        data_filtered, 
        labels=labels_filtered,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors_filtered
    )
    
    # Styling
    for text in texts:
        text.set_fontsize(10)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    
    return fig

def bar_chart(data, x, y, title="Bar Chart", color=None, horizontal=False):
    """
    Create bar chart
    
    Args:
        data: DataFrame
        x: Kolom untuk x-axis
        y: Kolom untuk y-axis
        title: Judul chart
        color: Warna bar (optional)
        horizontal: Jika True, buat horizontal bar
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    if horizontal:
        sns.barplot(data=data, y=x, x=y, ax=ax, color=color or COLOR_PALETTE['primary'])
        ax.set_xlabel(y, fontsize=11)
        ax.set_ylabel(x, fontsize=11)
    else:
        sns.barplot(data=data, x=x, y=y, ax=ax, color=color or COLOR_PALETTE['primary'])
        ax.set_xlabel(x, fontsize=11)
        ax.set_ylabel(y, fontsize=11)
        
        # Rotate x labels jika panjang
        if len(data) > 5:
            plt.xticks(rotation=45, ha='right')
    
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    # Format y-axis dengan separator
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    
    plt.tight_layout()
    
    return fig

def line_chart(data, x, y, title="Line Chart", hue=None):
    """
    Create line chart
    
    Args:
        data: DataFrame
        x: Kolom untuk x-axis
        y: Kolom untuk y-axis (bisa list untuk multiple lines)
        title: Judul chart
        hue: Kolom untuk grouping (optional)
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    if isinstance(y, list):
        for col in y:
            ax.plot(data[x], data[col], marker='o', label=col, linewidth=2)
        ax.legend()
    else:
        if hue:
            for key, grp in data.groupby(hue):
                ax.plot(grp[x], grp[y], marker='o', label=key, linewidth=2)
            ax.legend()
        else:
            ax.plot(data[x], data[y], marker='o', linewidth=2, color=COLOR_PALETTE['primary'])
    
    ax.set_xlabel(x, fontsize=11)
    ax.set_ylabel(y if isinstance(y, str) else 'Value', fontsize=11)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    # Format y-axis dengan separator
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    
    # Rotate x labels
    plt.xticks(rotation=45, ha='right')
    
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return fig

def heatmap_chart(data, title="Heatmap", annot=True, fmt=".0f", cmap="YlOrRd"):
    """
    Create heatmap
    
    Args:
        data: DataFrame atau matrix
        title: Judul chart
        annot: Show annotations
        fmt: Format annotations
        cmap: Color map
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    sns.heatmap(data, annot=annot, fmt=fmt, cmap=cmap, ax=ax, cbar_kws={'label': 'Amount'})
    
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    
    return fig

def box_plot(data, x, y, title="Box Plot"):
    """
    Create box plot
    
    Args:
        data: DataFrame
        x: Kolom untuk x-axis
        y: Kolom untuk y-axis
        title: Judul chart
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    sns.boxplot(data=data, x=x, y=y, ax=ax, hue=x, palette="Set2", legend=False)
    
    ax.set_xlabel(x, fontsize=11)
    ax.set_ylabel(y, fontsize=11)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    # Format y-axis dengan separator
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    return fig

def histogram_chart(data, column, bins=30, title="Histogram"):
    """
    Create histogram
    
    Args:
        data: DataFrame
        column: Kolom yang akan diplot
        bins: Jumlah bins
        title: Judul chart
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.hist(data[column], bins=bins, color=COLOR_PALETTE['secondary'], alpha=0.7, edgecolor='black')
    
    ax.set_xlabel(column, fontsize=11)
    ax.set_ylabel('Frequency', fontsize=11)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return fig

def area_chart(data, x, y, title="Area Chart"):
    """
    Create area chart
    
    Args:
        data: DataFrame
        x: Kolom untuk x-axis
        y: Kolom untuk y-axis (bisa list untuk stacked area)
        title: Judul chart
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    if isinstance(y, list):
        ax.stackplot(data[x], *[data[col] for col in y], labels=y, alpha=0.7)
        ax.legend(loc='upper left')
    else:
        ax.fill_between(data[x], data[y], alpha=0.7, color=COLOR_PALETTE['primary'])
    
    ax.set_xlabel(x, fontsize=11)
    ax.set_ylabel(y if isinstance(y, str) else 'Value', fontsize=11)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    # Format y-axis dengan separator
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    
    plt.xticks(rotation=45, ha='right')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return fig
