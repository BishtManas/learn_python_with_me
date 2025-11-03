import numpy as np 

arr = np.array([[1, 2, 3], [4, 5, 6]])# this is a 2 dimension array with order 2 x 3 

newarr = arr.reshape(-1)# this -1 helps to find the unknown dinmension so this will return a 1 dimension array.

print(newarr)