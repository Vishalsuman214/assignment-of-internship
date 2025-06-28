import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[6, 7, 8], [9, 10, 11]])

# Maximum and minimum values in 1D array
max_value = np.max(arr_1d)
min_value = np.min(arr_1d)

print("Original 1D array:")
print(arr_1d)
print("\nMaximum value:", max_value)
print("Minimum value:", min_value)

# Find number of rows and columns in 2D array
rows, cols = arr_2d.shape
print("\nNumber of rows:", rows)
print("Number of columns:", cols)

# Select elements
print("\nAll elements in arr_1d:")
for x in arr_1d:
    print(x)

print("\nElement at index 2 in arr_1d:", arr_1d[2])
print("Element at row 1, col 2 in arr_2d:", arr_2d[1, 2])

# Find sum of values in 2D array using for loop
total = 0
for y in arr_2d:
    for val in y:
        total += val
print("\nSum of all elements in arr_2d:", total)

# All operations
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
