#this the another example for filtering in numpy 
import numpy as np

#this is the method without using if and else.
#we take the same example as we take in previous file 
#for checking the number is odd or even
arr = np.array([12,23,12,33,55])# this is our previous array

filter_array = arr % 2 == 0 
new_array = arr[filter_array]
print(new_array)# this will show the same output as shown in previous file