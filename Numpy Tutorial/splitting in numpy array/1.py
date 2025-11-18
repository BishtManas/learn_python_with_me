import numpy as np

arr = np.array([1,2,3,4,5,6])

new_arr = np.array_split(arr,3)# this will select randomaly form your array

print(new_arr)