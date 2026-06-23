import numpy as np
arr = np.array([1, 2, 3, 4, 5]) 
print(arr[::2])
print(arr[2:5])
print(arr[-1:])
print(arr[-2:-5:-2])

matrix = np.array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

print(matrix[1, 2])
print(matrix[0:2, :])
print(matrix[:, 1:3])
print(matrix[1:, 1:]) 
print(matrix[:, 2])

# Iterating through a 2D array using np.nditer() and np.ndenumerate()
# np.nditer() 
for x in np.nditer(matrix):
    print(x, end=" ") 
    
# np.ndenumerate()
for idx, x in np.ndenumerate(matrix):
    print(idx, x)