# Comparision between NumPy array and Python list
import numpy as np
import time
import sys

# Speed test for multiplying each element by 2 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*100000 
# Time taken to multiply each element in Python list
start_time = time.time()
for i in range(len(lst)):
    lst[i] = lst[i] * 2
end_time = time.time()
print(f"Time taken to multiply elements in Python list: {end_time - start_time:} seconds")
# Time taken to multiply each element in NumPy array
arr = np.array(lst)
start_time = time.time()
mumpy_array = arr * 2
end_time = time.time()
print(f"Time taken to multiply elements in NumPy array: {end_time - start_time:} seconds")

# Memory usage comparison
print(f"Memory usage of Python list: {sys.getsizeof(lst)} bytes")
print(f"Memory usage of NumPy array: {arr.nbytes} bytes")
