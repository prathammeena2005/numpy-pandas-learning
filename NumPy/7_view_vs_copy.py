import numpy as np
arr = np.array([10, 20, 30, 40, 50]) 

# view is a reference to the original array, so modifying the view will also modify the original array.
view = arr[1:3]
print(view)
view[0] = 99
print(view)
print(arr)

# copy creates a new array that is independent of the original array, so modifying the copy will not affect the original array.
copy = arr[1:3].copy()
copy[0] = 88
print(copy)
print(arr)