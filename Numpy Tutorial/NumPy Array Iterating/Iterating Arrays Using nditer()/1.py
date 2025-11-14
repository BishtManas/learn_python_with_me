import numpy as np 

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# this is 3 -d array

# by using this method you can directly print all element with the help of nditer()

for m in np.nditer(arr):
    print(m)# this method print all the element by using the only single loop