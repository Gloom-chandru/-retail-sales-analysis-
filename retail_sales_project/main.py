from src.load_data import load_sales_data
from src.eda import plot_category_sales, plot_monthly_sales
from src.insights import top_customers, top_products

# Load and prepare data
df = load_sales_data('data/retail_sales.csv')

# Run visual analysis
plot_category_sales(df)
plot_monthly_sales(df)

# Print insights
print("\n🔝 Top Customers:\n", top_customers(df))
print("\n🏆 Top Products:\n", top_products(df))