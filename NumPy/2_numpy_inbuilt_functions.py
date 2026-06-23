# Numpy inbuilt functions
import numpy as np
arr=(10, 15, 20, 25, 30)

# 1. np.arr() is used to create a numpy array from a list or tuple.
arr1 = np.array(arr)
print("Array 1:", arr1)

# 2. np.arange() is used to create a numpy array with a range of values.
arr2 = np.arange(10, 30, 5)  
print("Array 2:", arr2)

# 3. np.zeros() is used to create a numpy array filled with zeros.
arr3 = np.zeros((2, 3))
print("Array 3:", arr3)

# 4. np.ones() is used to create a numpy array filled with ones.
arr4 = np.ones((2, 3))
print("Array 4:", arr4)

# 5. np.linspace() is used to create a numpy array with evenly spaced values between a specified range.
arr5 = np.linspace(0, 1, 5)
print("Array 5:", arr5)

# 6. np.logspace() is used to create a numpy array with logarithmically spaced values between a specified range.
arr6 = np.logspace(1, 3, 5)
print("Array 6:", arr6)

# np.full() is used to create a numpy array filled with a specified value.
arr7 = np.full((2, 3), 7)
print("Array 7:", arr7)

# np.empty() is used to create a numpy array without initializing its values.
arr8 = np.empty((2, 3))
print("Array 8:", arr8)

# np.eye() is used to create a 2D array with ones on the diagonal and zeros elsewhere.
arr9 = np.eye(3)
print("Array 9:", arr9)

# np.random.rand() is used to create a numpy array with random values between 0 and 1.
arr10 = np.random.rand(2, 3)
print("Array 10:", arr10)
 
# np.random.randint() is used to create a numpy array with random integers between a specified range.
arr11 = np.random.randint(0, 10, (2, 3))
print("Array 11:", arr11)

# np.random.randn() is used to create a numpy array with random values from a standard normal distribution.
arr12 = np.random.randn(2, 3)
print("Array 12:", arr12)

# arr.dim is used to get the number of dimensions of a numpy array.
new_arr= np.array([[1, 2, 3], [4, 5, 6]])
print("Dimensions of Array 1:", arr1.ndim)
print("Dimensions of New Array:", new_arr.ndim)

# arr.shape is used to get the shape of a numpy array.
print("Shape of Array 1:", arr1.shape)
print("Shape of New Array:", new_arr.shape)

# arr.size is used to get the total number of elements in a numpy array.
print("Size of Array 1:", arr1.size)
print("Size of New Array:", new_arr.size)


# Reshape, Ravel and Flatten
_1Dlist = [1, 2, 3, 4, 5, 6]
_2Darr = np.array(_1Dlist).reshape(2, 3)
print("2D Array:\n", _2Darr)
# np.reshape() is used to change the shape of a numpy array without changing its data.
reshaped_arr = np.array(_1Dlist).reshape(3, 2)
print("Reshaped Array:\n", reshaped_arr)

# np.ravel() is used to flatten a numpy array into a 1D array.
raveled_arr = _2Darr.ravel()
print("Raveled Array:", raveled_arr)

# np.flatten() is used to flatten a numpy array into a 1D array. It returns a copy of the original array.
flattened_arr = _2Darr.flatten()
print("Flattened Array:", flattened_arr)
