import numpy as np

arr = np.random.randint(0, 10, size = 10)
print("Array: ", arr)
print("Mean: ", np.mean(arr))
print("Max: ", np.max(arr))
print("Min: ", np.min(arr))
print("Sum", np.sum(arr))
print("Sorted Array: ", np.sort(arr))
print("Shuffled Array: ", np.random.permutation(arr))
print("Squared Array: ", np.square(arr))
print("Square Root: ", np.sqrt(arr))
