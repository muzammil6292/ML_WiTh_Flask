import pandas as pd

# Load the banking data CSV file
file_path = "C:\Users\moham\Downloads\banking_data.csv"  # Update the file path if necessary
df = pd.read_csv(file_path)

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Generate basic statistics for numerical columns
print("\nBasic statistics of numerical columns:")
print(df[['Transaction_Amount', 'Account_Balance']].describe())

# Check for missing values in the dataset
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# 1. Group by Account_Type and calculate the total sum of Transaction_Amount
total_transaction_by_account_type = df.groupby('Account_Type')['Transaction_Amount'].sum()
print("\nTotal sum of Transaction_Amount by Account Type:")
print(total_transaction_by_account_type)

# 2. Calculate the average Account_Balance for each Account_Type
avg_balance_by_account_type = df.groupby('Account_Type')['Account_Balance'].mean()
print("\nAverage Account_Balance for each Account Type:")
print(avg_balance_by_account_type)

# 3. Group by Branch and calculate the total number of transactions per branch
total_transactions_by_branch = df.groupby('Branch').size()
print("\nTotal number of transactions per branch:")
print(total_transactions_by_branch)

# 4. Calculate the average transaction amount per branch
avg_transaction_by_branch = df.groupby('Branch')['Transaction_Amount'].mean()
print("\nAverage transaction amount per branch:")
print(avg_transaction_by_branch)
