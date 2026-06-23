import numpy as np

# concatenate is used to combine two or more arrays into a single array. It can be used to combine arrays of the same shape along a specified axis.
arr1 = np.array([1, 2])
arr2 = np.array([10, 20])

combine = np.concatenate((arr1, arr2))
print('Combined array =', combine)

# vstack is used to stack arrays vertically (row-wise). It takes a sequence of arrays and stacks them along the first axis (axis=0).
arr3 = np.array([[1], [2]])
arr4 = np.array([[10], [20]])
vertical_stack = np.vstack((arr3, arr4))
print('Vertically stacked array =', vertical_stack)

# hstack is used to stack arrays horizontally (column-wise). It takes a sequence of arrays and stacks them along the second axis (axis=1).
arr5 = np.array([[1, 2], [3, 4]])
arr6 = np.array([[10, 20], [30, 40]])
horizontal_stack = np.hstack((arr5, arr6))
print('Horizontally stacked array =', horizontal_stack)

# split is used to split an array into multiple sub-arrays. It can be used to split an array into equal parts or based on specified indices.
arr7 = np.array([[1, 2], [3, 4], [5, 6]])
split_array = np.split(arr7, 3, axis=0)
print('Split arrays =', split_array)

# repeat is used to repeat elements of an array. It can be used to create a new array by repeating the elements of the original array a specified number of times.
arr8 = np.array([11, 22, 33])
print(np.repeat(arr8, 2))

# tile is used to create a new array by repeating the original array a specified number of times along each axis. It can be used to create a larger array by tiling the original array.
print(np.tile(arr8, 2))