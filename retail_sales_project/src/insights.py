def top_customers(df, n=10):
    return df.groupby('Customer_ID')['Total_Sales'].sum().sort_values(ascending=False).head(n)

def top_products(df, n=10):
    return df.groupby('Product_Name')['Total_Sales'].sum().sort_values(ascending=False).head(n)