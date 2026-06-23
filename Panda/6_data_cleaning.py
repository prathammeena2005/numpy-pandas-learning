import numpy as np
import pandas as pd

# Dealing with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Frank"],
    "Age": [25, np.nan, 35, 40, 45],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"], 
    "Salary": [50000, 60000, 70000, np.nan, 90000]
    }
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Dropping rows with missing values
print('\nDataFrame after dropping rows with any missing values:')
print(df.dropna())

# Filling missing values with mean and median
print('\nDataFrame after filling missing values in Age column with mean:')
print(df['Age'].fillna(df['Age'].mean()))
print('\nDataFrame after filling missing values in Salary column with median:')
print(df['Salary'].fillna(df['Salary'].median()))

# Forward and backward fill
print('\nDataFrame after forward fill:')
print(df.ffill())
print('\nDataFrame after backward fill:')
print(df.bfill())

# Replacing values
print()
print(df['Name'].replace('Charlie', 'John'))
