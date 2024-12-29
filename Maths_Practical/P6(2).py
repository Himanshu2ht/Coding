import numpy as np
from scipy.linalg import eig
from sympy import Matrix, symbols

# Function to check diagonalizability
def is_diagonalizable(A):
    # Compute eigenvalues and eigenvectors using numpy
    eigenvalues, eigenvectors = eig(A)
    
    # Check if eigenvectors are linearly independent
    if np.linalg.matrix_rank(eigenvectors) == A.shape[0]:
        return True, eigenvalues
    else:
        return False, eigenvalues

# Function to verify the Cayley-Hamilton theorem
def verify_cayley_hamilton(A):
    # Convert numpy array to sympy Matrix
    A_sympy = Matrix(A)
    
    # Compute the characteristic polynomial
    lambda_symbol = symbols('lambda')
    char_poly = A_sympy.charpoly(lambda_symbol)
    
    # The coefficients of the characteristic polynomial
    coeffs = char_poly.all_coeffs()

    # Initialize the result as a zero matrix
    result = Matrix.zeros(*A.shape)

    # Substitute the matrix A into the polynomial
    for i, coeff in enumerate(reversed(coeffs)):
        result += coeff * (A_sympy ** i)
    
    # Check if the result is the zero matrix
    return result == Matrix.zeros(*A.shape)

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
