import numpy as np

print("Enter elements for 5x3 Matrix (Row-wise):")
A = []
for i in range(5):
    row = list(map(int, input(f"Enter 3 elements for row {i+1}: ").split()))
    A.append(row)

print("\nEnter elements for 3x2 Matrix (Row-wise):")
B = []
for i in range(3):
    row = list(map(int, input(f"Enter 2 elements for row {i+1}: ").split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Multiplication
product = np.dot(A, B)

print("\nProduct Matrix (A x B):")
print(product)