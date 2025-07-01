import numpy as np

A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])

B = np.array([9, -6, 17])

x = np.linalg.solve(A, B)
print("Solution using solve():", x)

A_inv = np.linalg.inv(A)
x2 = np.dot(A_inv, B)
print("Solution using inverse:", x2)
