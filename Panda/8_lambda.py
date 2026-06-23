import numpy as np
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Alice"],
    "Age": [25, np.nan, 35, 40, 25],
    "Department": ["HR", "IT", "Finance", "Marketing", "HR"], 
    "Salary": [50000, 60000, 70000, np.nan, 50000]
    }

df = pd.DataFrame(data)

# Using Lambda Function to Create a New Column
df["Promoted Salary"] = df["Salary"].apply(lambda x: x * 1.2 if x > 50000 else x)
print("DataFrame with Promoted Salary:")
print(df)