import numpy as np
arr = np.array ([10,15,20,30,25,27,32,42,45,55,56,65,62,69,72,85,87,92,95,98,99])
print("orginal Array :  ", arr)
print("count the number of values in each array : ", np.bincount(arr))

newarr = arr.reshape(7,3)
print("Reshaped Array  :", newarr)