from sympy import Matrix
from sympy.matrices import GramSchmidt

# Function to find orthonormal basis using Gram-Schmidt process
def gram_schmidt_orthonormalization(vectors):
    sympy_vectors = [Matrix(vec) for vec in vectors]
    
    # Check if the vectors are linearly independent
    try:
        orthonormal_basis = GramSchmidt(sympy_vectors, orthonormal=True)
        return orthonormal_basis
    except ValueError:
        return "The vectors are linearly dependent, and orthogonalization cannot be performed."

# Example of linearly independent vectors
vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Orthonormal basis
orthonormal_basis = gram_schmidt_orthonormalization(vectors)
print("Orthonormal basis:", orthonormal_basis)
