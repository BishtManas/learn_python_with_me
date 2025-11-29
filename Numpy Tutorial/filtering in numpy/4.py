import numpy as np 

gp = np.array([34,23,45,67,56,22])

filter_data = gp > 25

new_data = gp[filter_data]#this will give the same output as in previous method of filtering.