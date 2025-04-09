import numpy as np

# Create two 3x3 matrices with random integers between 1 and 10
matrix_A = np.random.randint(1, 11, (3, 3))
matrix_B = np.random.randint(1, 11, (3, 3))

# Perform matrix subtraction
matrix_subtraction = np.subtract(matrix_A, matrix_B)

# Perform element-wise division (handling division by zero)
matrix_division = np.divide(matrix_A, matrix_B, where=matrix_B != 0)

print("Matrix A:")
print(matrix_A)

print("\nMatrix B:")
print(matrix_B)

print("\nMatrix Subtraction (A - B):")
print(matrix_subtraction)

print("\nElement-wise Division (A / B):")
print(matrix_division)
