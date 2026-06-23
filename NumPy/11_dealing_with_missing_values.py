import numpy as np

# np.nan is used to represent missing values in NumPy arrays
arr = np.array([[1, 2], [3, np.nan]])   
print('Original array:', arr)

# Check for missing values
print('Is there any missing value in the array?', np.isnan(arr))

# np.inf is used to represent positive and negative infinity in NumPy arrays
arr_inf = np.array([[1, 2], [3, np.inf]])  
print('Array with infinite values:', arr_inf)

# Check for infinite values
print('Is there any infinite value in the array?', np.isinf(arr_inf))

# Replace missing values with a specific value (e.g., 0)
arr_filled = np.nan_to_num(arr, nan=0) 
print('Array after filling missing values:', arr_filled)