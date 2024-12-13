# Check the diagonalizable property of matrices and find the corresponding eigenvalue and verify the Cayley-Hamilton theorem.
import numpy as np
from scipy.linalg import eig
from sympy import Matrix, symbols, det

# Function to check diagonalizability
def is_diagonalizable(A):
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = eig(A)
    
    # Check the geometric multiplicity (number of independent eigenvectors)
    # If the number of independent eigenvectors matches the size of the matrix, it's diagonalizable
    rank = np.linalg.matrix_rank(eigenvectors)
    if rank == A.shape[0]:
        return True, eigenvalues
    else:
        return False, eigenvalues

# Function to verify the Cayley-Hamilton theorem
def verify_cayley_hamilton(A):
    # Convert matrix to sympy Matrix
    A_sympy = Matrix(A)
    
    # Compute the characteristic polynomial
    lambda_symbol = symbols('lambda')
    char_poly = A_sympy.charpoly(lambda_symbol)
    
    # The characteristic polynomial as a sympy expression
    characteristic_polynomial = char_poly.as_expr()

    # Replace lambda with the matrix A in the characteristic polynomial
    A_substitution = characteristic_polynomial.subs(lambda_symbol, A_sympy)
    
    # Check if the result is the zero matrix (Cayley-Hamilton should hold)
    return A_substitution.is_zero

# Example matrix
A = np.array([[4, -1, 1],
              [-1, 4, -2],
              [1, -2, 3]])

# Step 1: Check if the matrix is diagonalizable
diagonalizable, eigenvalues = is_diagonalizable(A)
print("Is the matrix diagonalizable?", diagonalizable)
print("Eigenvalues of the matrix:", eigenvalues)

# Step 2: Verify Cayley-Hamilton theorem
is_cayley_hamilton_true = verify_cayley_hamilton(A)
print("Does the matrix satisfy the Cayley-Hamilton theorem?", is_cayley_hamilton_true)
