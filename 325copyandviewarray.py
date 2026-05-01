import numpy as np
inputlist = list(map(int,input().split(" ")))
original_array = np.array(inputlist)
view_array = original_array.view()
copy_array =original_array.copy()
view_array[0] = 99
print("Original array after modifying view:", original_array)
print("View array:", view_array)
copy_array[1] = 88
print("Original array after modifying copy:", original_array)
print("Copy array:", copy_array)
