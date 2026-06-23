# Data Types and Type Casting in Numpy Array
import numpy as np

# Data Types 
arr1 = np.array([1, 4, 8, 11, 14])
print(arr1.dtype)

arr2 = np.array([7, 11.11, 16, 21, 36])
print(arr2.dtype)

arr3 = np.array(['Pratham', 20, 14.2])
print(arr3.dtype)

arr4 = np.array([True, False])
print(arr4.dtype)

arr5 = np.array([1+2j, 3+4j, 5+6j])
print(arr5.dtype)

# Type Casting
arr6 = np.array([5, 9, 14, 25, 34])
narr6 = arr6.astype('float')
print(narr6,',' , narr6.dtype)

arr7 = np.array([7.5, 12.3, 18.9, 27.6])
narr7 = arr7.astype('int')
print(narr7,',' , narr7.dtype)