import numpy as np

arr = np.array([12,23,34,23,34,23,12])

#like in this array you want to find where the number is divisible by 2
print(np.where( arr%2 == 0))# this will give you all posible values of index where the number is divisible by 2.
