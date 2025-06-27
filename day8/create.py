import numpy as np

random_arr = np.random.rand(3, 3)
print("Random array (3x3):\n", random_arr)

# (4x2)

empty_arr = np.empty((4, 2))
print("\nEmpty array (4x2):\n", empty_arr)

# full array (4x2) with value 7
full_arr = np.full((4, 2), 7)
print("\nFull array (4x2) with value 7:\n", full_arr)

# 4 (3x5)
zeros_arr = np.zeros((3, 5))
print("\nZeros array (3x5):\n", zeros_arr)

# 5. (4x3x2)
ones_arr = np.ones((4, 3, 2))
print("\nOnes array (4x3x2):\n", ones_arr)
