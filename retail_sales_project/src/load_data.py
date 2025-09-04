import pandas as pd

def load_sales_data(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Total_Sales'] = df['Quantity'] * df['Price']
    df.dropna(inplace=True)
    return df