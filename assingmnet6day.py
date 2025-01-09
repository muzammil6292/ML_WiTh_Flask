#1question
import pandas as pd
data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000]
}

df = pd.DataFrame(data)
print(df)

#2 question
import pandas as pd

data1 = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000]
}

df = pd.DataFrame(data1)

print(df)

print("First 2 rows:")
print(df.head(2))

df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus column:")
print(df)

average_salary = df['Salary'].mean()
print(f"\nAverage Salary: {average_salary}")

filtered_employees = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(filtered_employees)
