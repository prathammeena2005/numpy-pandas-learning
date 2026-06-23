import numpy as np
import pandas as pd

# Duplicate Handling
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Alice"],
    "Age": [25, np.nan, 35, 40, 25],
    "Department": ["HR", "IT", "Finance", "Marketing", "HR"], 
    "Salary": [50000, 60000, 70000, np.nan, 50000]
    }

df = pd.DataFrame(data)
print("Duplicates in the DataFrame:")
print(df[df.duplicated()])
print("\nDataFrame after removing duplicates:")
print(df.drop_duplicates())
