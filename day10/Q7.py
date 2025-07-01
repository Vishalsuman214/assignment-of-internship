import numpy as np


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

combined = np.concatenate((arr1.flatten(), arr2.flatten()))

print("Average:", np.mean(combined))
print("Mean:", np.mean(combined))
print("Median:", np.median(combined))
print("mode:", np.bincount(combined).argmax())
