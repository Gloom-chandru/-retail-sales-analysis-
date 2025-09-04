import matplotlib.pyplot as plt
import seaborn as sns
from src.plot_utils import save_and_show_plot

def plot_category_sales(df):
    category_sales = df.groupby('Category')['Total_Sales'].sum().sort_values()
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=category_sales.values, y=category_sales.index, palette='viridis', ax=ax)
    ax.set_title('Sales by Category')
    save_and_show_plot(fig, 'category_sales.png')

def plot_monthly_sales(df):
    monthly_sales = df.resample('M', on='Date')['Total_Sales'].sum()
    fig, ax = plt.subplots(figsize=(12,6))
    monthly_sales.plot(marker='o', color='teal', ax=ax)
    ax.set_title('Monthly Sales Trend')
    ax.grid(True)
    save_and_show_plot(fig, 'monthly_sales.png')