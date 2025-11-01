import numpy as np 

arr = np.array([1,4,2,5,6])

b = arr.view()

b[0] = 3

print(b)# this will change the both array so view is basically for viewing the actual array.
print(arr)