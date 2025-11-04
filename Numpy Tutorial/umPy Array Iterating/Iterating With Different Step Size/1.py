import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):# the first one is for row and column and the second one is for number of element present in the list
  print(x)