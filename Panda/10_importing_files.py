import pandas as pd

data = pd.read_csv('C:\\Users\\prath\\Downloads\\archive\\data.csv')
print('Shape ', data.shape)
print('\nDescription')
print(data.describe())
print('\nInformation')   
print(data.info())
print('\nFirst 5 rows')
print(data.head())