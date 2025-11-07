import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.



print(arr)