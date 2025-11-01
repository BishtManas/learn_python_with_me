import numpy as np

arr = np.array([12,23,344,34])

a = arr.copy()

b = arr.view()

print(a.base)# this return none because copy don't have their own data.
print(b.base)# this will return the actual array of arr so this will return.