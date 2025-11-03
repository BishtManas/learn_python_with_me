import numpy as np 

# Reshape of the array from 1-D to 2-D 

# let's suppose we have this arr in 1 dimension 

arr = np.array([1,2,3,4,5,6,7,8,9])# the length of the array is nine so we keep one thing in our mind is 
# if we want to reshape the array from one dimension to another dimension the multiplication should be equal to the number of element present in that particular array or length
# so in this array the element is nine so the multiplication be like 3 x 3, 9 x 1 , or 1 x 9 

newarr = arr.reshape(3,3) 

print(newarr)