import numpy as np

arr=np.array([1,2,3,4,5,6])

arr1=np.array([[7,8,9],[10,11,12]])

result=np.concatenate((arr,arr1.flatten()))


print("combined Array is:\n",result)



