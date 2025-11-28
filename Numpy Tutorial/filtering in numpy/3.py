import numpy as np 

gp = np.array([34,23,45,67,56,22])

filter_data = []

for age in gp:
    if age > 25:
        filter_data.append(True)
    else:
        filter_data.append(False)

new_data = age(filter_data)
print(new_data)