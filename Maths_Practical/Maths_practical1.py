# Practical 1 : Find cofactor, determinant, adjoint and inverse of a matrix.

# Taking Input of Matrix From user (User Define matrix Input)
# NR: Number of Rows
# NC: Number of Column
import numpy as np

NR = int(input("Enter the number of rows: "))
NC = int(input("Enter the number of columns: "))

print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
A = np.array(entries).reshape(NR, NC)
print("Matrix A is as follows:", "\n", A)

# For finding the inverse of a Matrix
A_Inverse = np.linalg.inv(A)
print("Inverse of A is", "\n", A_Inverse)

# For finding the transpose of a Matrix
Transpose_of_A_Inverse = np.transpose(A_Inverse)
print("Transpose of A Inverse is", "\n", Transpose_of_A_Inverse)

# For finding the determinant of a Matrix
Determinant_of_A = np.linalg.det(A)
print("Determinant of A is", "\n", Determinant_of_A)

# For finding the cofactor of a Matrix
Cofactor_of_A = np.dot(Transpose_of_A_Inverse, Determinant_of_A)
print("The Cofactor of a Matrix is:", "\n", Cofactor_of_A)

# For finding the Adjoint of a Matrix
Adjoint_of_A = np.transpose(Cofactor_of_A)
print("The Adjoint of a Matrix is:", "\n", Adjoint_of_A)

print("End of code")