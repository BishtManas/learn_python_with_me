# Reshape is view or copy let's check this 
import numpy as np 

arr5 = np.array([2,3,5,3,5,3])

print(arr5.reshape(3,2).base)# this will return the actual array so reshape is view