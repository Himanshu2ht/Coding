import numpy as np
from sympy import Matrix

# Function to generate basis of column space, null space, row space, and left null space of a matrix
def matrix_spaces(A):
    A_sympy = Matrix(A)

    # Basis of column space (columns of the matrix)
    col_space_basis = A_sympy.columnspace()

    # Basis of null space
    null_space_basis = A_sympy.nullspace()

    # Basis of row space (rows of the matrix)
    row_space_basis = A_sympy.rowspace()

    # Basis of left null space (null space of the transpose)
    left_null_space_basis = Matrix(A.T).nullspace()

    return col_space_basis, null_space_basis, row_space_basis, left_null_space_basis

# Example matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Generate spaces
col_space, null_space, row_space, left_null_space = matrix_spaces(A)
print("Column space basis:", col_space)
print("Null space basis:", null_space)
print("Row space basis:", row_space)
print("Left null space basis:", left_null_space)
