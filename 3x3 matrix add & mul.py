import numpy as np

# Generate two 3x3 matrices with random integers (1 to 9)
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
addition = A + B
print("\nMatrix Addition (A + B):")
print(addition)

# Matrix Multiplication
multiplication = np.dot(A, B)
print("\nMatrix Multiplication (A x B):")
print(multiplication