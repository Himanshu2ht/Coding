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
    # Convert the matrix to a sympy Matrix
    A_sympy = Matrix(A)
    
    # Compute the characteristic polynomial
    lambda_symbol = symbols('lambda')
    char_poly = A_sympy.charpoly(lambda_symbol)
    
    # Extract coefficients of the polynomial
    coeffs = char_poly.all_coeffs()
    
    # Reconstruct the polynomial with A substituted for lambda
    n = A_sympy.shape[0]
    result = Matrix.zeros(n, n)  # Initialize the result as a zero matrix
    for i, coeff in enumerate(reversed(coeffs)):  # reversed because highest power comes first
        result += coeff * (A_sympy ** i)  # A^i for powers of lambda
    
    # Check if the resulting matrix is zero
    return result == Matrix.zeros(n, n)

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
