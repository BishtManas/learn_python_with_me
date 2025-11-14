import numpy as np 

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for m in arr:
    print(m)# this will print the only element present in 3-d array 
    # in 3-d array  a single 2-d array is one element of 3-d array if you print the whole single element you must iterating through one by one.