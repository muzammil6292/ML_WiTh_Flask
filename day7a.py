import pandas as pd

# Load the sales data CSV file
file_path = 'sales_data.csv'  # Update the path if needed
df = pd.read_csv("C:\Users\moham\Downloads\sales_data.csv")

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Print basic statistics of the numerical columns
print("\nBasic statistics of numerical columns:")
print(df.describe())


# Load the sales data CSV file
file_path = 'sales_data.csv'  # Update with the correct path if needed
df = pd.read_csv("C:\Users\moham\Downloads\sales_data.csv")

# 1. Calculate the total sales for each region
total_sales_by_region = df.groupby('Region')['Sales'].sum()
print("Total sales for each region:")
print(total_sales_by_region)

# 2. Find the most sold product (based on quantity)
most_sold_product = df.groupby('Product')['Quantity'].sum().idxmax()
max_quantity = df.groupby('Product')['Quantity'].sum().max()
print("\nMost sold product based on quantity:")
print(f"Product: {most_sold_product}, Quantity Sold: {max_quantity}")

# 3. Compute the average profit margin for each product
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100  # Calculate profit margin
average_profit_margin_by_product = df.groupby('Product')['Profit Margin'].mean()

print("\nAverage profit margin for each product:")
print(average_profit_margin_by_product)
