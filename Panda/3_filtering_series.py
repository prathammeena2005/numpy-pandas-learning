import pandas as pd

fruit_protein = {'Apple': 0.3, 'Banana': 1.1, 'Grapes': 0.6, 'Mango': 0.8}
s = pd.Series(fruit_protein)
# Filtering the Series
print(s > 0.6)
print(s[s > 0.6])

# Using logical operators for filtering 
# AND Operator
print((s > 0.5) & (s < 1.0))
print(s[(s > 0.5) & (s < 1.0)])

# OR Operator
print((s > 0.5) | (s < 1.0))
print(s[(s > 0.5) | (s < 1.0)])

# NOT Operator
print(s[~(s > 0.5)])