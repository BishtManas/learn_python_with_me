import numpy as np 

# reshaping of array from 1-D array to 3-D array 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)# the multiplication of these three number is equals to the number of element present in this array.

print(newarr)