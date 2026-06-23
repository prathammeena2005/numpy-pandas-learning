import numpy as np
import pandas as pd

data1 = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Alice"],
    "Age": [25, np.nan, 35, 40, 25],
    "Department": ["HR", "IT", "Finance", "Marketing", "HR"], 
    "Salary": [50000, 60000, 70000, np.nan, 50000]
    }
df1 = pd.DataFrame(data1)

data2 = {
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"],
    "Location": ["New York", "San Francisco", "Chicago", "Los Angeles", "Boston"]
    }
df2 = pd.DataFrame(data2)

# Concat
print(pd.concat([df1, df2]))
print('\n')
print(pd.concat([df1, df2], axis=1))
print('\n')

# Merge
print(pd.merge(df1, df2, on="Department"))