import pandas as pd

# Load the banking data CSV file
file_path = "C:\Users\moham\Downloads\banking_data.csv"  # Update the path if necessary
df = pd.read_csv(file_path)

# 1. Filter out all rows where Transaction_Amount is greater than 2000
filtered_transactions = df[df['Transaction_Amount'] > 2000]
print("Transactions with amount greater than 2000:")
print(filtered_transactions)

# 2. Find all rows where Transaction_Type is 'Loan Payment' and Account_Balance is greater than 5000
loan_payment_filtered = df[(df['Transaction_Type'] == 'Loan Payment') & (df['Account_Balance'] > 5000)]
print("\nLoan payments where account balance is greater than 5000:")
print(loan_payment_filtered)

# 3. Extract transactions made in the 'Uptown' branch
uptown_transactions = df[df['Branch'] == 'Uptown']
print("\nTransactions made in the Uptown branch:")
print(uptown_transactions)


# 1. Add a new column called Transaction_Fee (2% of Transaction_Amount)
df['Transaction_Fee'] = df['Transaction_Amount'] * 0.02

# 2. Create a new column Balance_Status based on Account_Balance
df['Balance_Status'] = df['Account_Balance'].apply(lambda x: 'High Balance' if x > 5000 else 'Low Balance')

# Display the updated DataFrame with new columns
print("\nUpdated DataFrame with Transaction_Fee and Balance_Status columns:")
print(df.head())
