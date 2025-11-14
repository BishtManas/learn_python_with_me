import numpy as np

arr = np.array([12,23,34,23,34,23,12]) # consider we have this type of array

# we want to find the 23's index so this is the method for those cases
print(np.where(arr == 23))# this will give me the all possible index where 23 is present 