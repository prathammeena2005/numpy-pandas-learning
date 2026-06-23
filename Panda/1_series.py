import pandas as pd

# Creating a Series from a list
s = pd.Series([11, 22, 33, 44, 55])
print('Series:\n', s)
print('Data type:', s.dtype)
print('Values:', s.values)
print('Index:', s.index)
print('Shape:', s.shape)
print('Name:', s.name)     
s.name = 'My Series'
print('Updated name:', s.name)

# Creating a Series from a dictionary
fruit_protein = {'Apple': 0.3, 'Banana': 1.1, 'Grapes': 0.6, 'Mango': 0.8}
s_dict = pd.Series(fruit_protein)
print('Series from dictionary:\n', s_dict)
s_dict.name = 'Fruit Protein Content'
print('Series with updated name:\n', s_dict)