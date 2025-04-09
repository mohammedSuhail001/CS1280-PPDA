import numpy as np

# Create a 3x3 array with random integers between 1 and 20
arr = np.random.randint(1, 21, (3, 3))

# Calculate the mean of the array
mean_value = np.mean(arr)

# Replace elements less than 10 with 0
arr[arr < 10] = 0

print("Original Array:")
print(arr)
print("\nMean of the array:", mean_value)
