# Practical 5 : Verify the linear dependence of vectors.
# Generate a linear combination of given vectors of Rn/ matrices of the same size.

import numpy as np

def is_linearly_dependent(vectors):
    # Convert the list of vectors to a numpy matrix (each vector is a column)
    A = np.column_stack(vectors)

    # Perform row reduction (Gaussian elimination)
    rank = np.linalg.matrix_rank(A)

    # If the rank of the matrix is less than the number of vectors, they are linearly dependent
    if rank < A.shape[1]:
        print("The vectors are linearly dependent.")
        # Find a non-trivial solution to the equation A * c = 0
        # where c is the vector of coefficients
        # Solve A * c = 0 (using least squares)
        c = np.linalg.lstsq(A, np.zeros(A.shape[0]), rcond=None)[0]
        print("Non-trivial linear combination (coefficients):")
        print(c)
    else:
        print("The vectors are linearly independent.")

def generate_linear_combination(vectors, coefficients):
    # Linear combination of vectors based on given coefficients
    result = np.zeros_like(vectors[0])
    for i, vec in enumerate(vectors):
        result += coefficients[i] * vec
    return result

# Example: 3 vectors in R^3 (3D space)
v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
v3 = np.array([3, 6, 9])

vectors = [v1, v2, v3]

# Check if the vectors are linearly dependent
is_linearly_dependent(vectors)

# Example: Generating a linear combination
coefficients = np.array([2, -1, 1])  # coefficients for the linear combination
linear_combination = generate_linear_combination(vectors, coefficients)
print("\nGenerated linear combination:")
print(linear_combination)
