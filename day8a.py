import pandas as pd

# Load the sales data CSV file
file_path = "C:\Users\moham\Downloads\sales_data.csv" 
df = pd.read_csv(file_path)

high_sales_df = df[df['Sales'] > 1000]
print("Rows where sales are greater than 1000:")
print(high_sales_df)

region_sales_df = df[df['Region'] == 'East']
print("\nSales records for the East region:")
print(region_sales_df)


df['Profit_Per_Unit'] = df['Profit'] / df['Quantity']


df['High_Sales'] = df['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')

print("\nUpdated DataFrame with Profit_Per_Unit and High_Sales columns:")
print(df.head())
