import numpy as np

arr=np.array([[1,2,3],[np.nan,5,6],[7,8,9]])


arr=np.nan_to_num(arr,nan=0)
print(arr)


arr_t=arr.T
print("\nTransposed array:")
print(arr_t)