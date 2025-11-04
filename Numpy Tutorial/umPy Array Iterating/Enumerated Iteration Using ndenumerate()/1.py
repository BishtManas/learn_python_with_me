import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):# this will print the actual index of the element present in array.
  print(idx, x)