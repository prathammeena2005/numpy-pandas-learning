import pandas as pd

s = pd.Series([11, 22, 33, 44, 55])
# Accessing elements using indexing
print('Element at index 0:', s[0])
print('Element at index 2:', s[2])
print('Elements from index 3 onwards:\n', s[3:5])

# iloc and loc for indexing
# In iloc stop value is excluded and in loc stop value is included
print('Element at index 1 using iloc:', s.iloc[1])
print('Elements between index 1 to 3 using iloc:\n', s.iloc[1:3])
print('Element at index 1 using loc:', s.loc[1])
print('Elements between index 1 to 3 using loc:\n', s.loc[1:3])

s.name = 'Calories'
fruits = ['Apple', 'Grapes', 'Pineapple', 'Orange', 'Mango']
s.index = fruits
print('Series :\n', s)