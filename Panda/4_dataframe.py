import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Frank"],
    "Age": [25, 30, 35, 40, 45],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"]
    }
df = pd.DataFrame(data)
print('Original DataFrame:')
print(df)
print('\nFirst 2 rows:')
print(df.head(2))
print('\nLast 3 rows:')
print(df.tail(3))
print('\nDataFrame info:')
print(df.info())
print('\nDataFrame description:')
print(df.describe())

# iloc and loc for indexing
print('\nElement at row 1, column 0 using iloc:', df.iloc[1, 0])
print('Elements from row 1 to 3 and column 0 to 1 using iloc:\n', df.iloc[1:4, 0:2])
print('\nElement at row 1, column "Name" using loc:', df.loc[1, "Name"])
print('Elements from row 1 to 3 and columns "Name" and "Age" using loc:\n', df.loc[1:3, ["Name", "Age"]])

# drop column
df_dropped = df.drop('Age', axis=1)
print('\nDataFrame after dropping "Age" column:')
print(df_dropped)
print('Shape of the modified DataFrame:', df_dropped.shape)

# Adding a new column
df["Salary"] = [50000, 60000, 70000, 80000, 90000]
print('\nDataFrame after adding "Salary" column:')
print(df)