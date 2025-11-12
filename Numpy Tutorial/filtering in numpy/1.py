import numpy as np 

arr = np.array([12,23,12,33,55])

filter_data = []

for ele in arr: 
    if ele % 2 == 0 :
        filter_data.append(True)
    else :
        filter_data.append(False)

new_arr = arr[filter_data]
print(new_arr)