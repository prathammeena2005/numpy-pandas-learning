import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Frank"],
    "Age": [25, 30, 35, 40, 45],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"], 
    "Salary": [50000, 60000, 70000, 80000, 90000]
    }
df = pd.DataFrame(data)
print('Original DataFrame:')
print(df)
# Broadcasting: Adding a constant value to a column
df['Promoted Salary'] = df['Salary'] + 5750
print('\nDataFrame after broadcasting:')
print(df)

print("\nUnique departments:")
print(df["Department"].unique())
print("\nDepartment counts:")
print(df["Department"].value_counts())