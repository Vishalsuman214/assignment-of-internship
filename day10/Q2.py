import numpy as np

arr=np.random.randint(1, 100, size=(2, 3,5))
print("original:",arr.shape)

move=np.moveaxis(arr, 0, -1)
print("moved:",move.shape)