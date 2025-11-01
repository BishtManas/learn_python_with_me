import numpy as np 

# the difference between copy and view is copy is just the new array and view is just view of new array.

# let's take an example 

# this an example for copy method 

arr = np.array([1,2,4,5,2,4])

a = arr.copy()

a[0] = 3

print(a)# this will change the element present in a 
print(arr)# by the use of copy method 