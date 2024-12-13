# Practical 2 : Convert a matrix into echelon form and find its rank.

import numpy as np

# Taking Input of Matrix From user (User Define matrix Input)
# NR: Number of Rows
# NC: Number of Column
NR = int(input("Enter the number of rows: "))
NC = int(input("Enter the number of columns: "))

print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix = np.array(entries).reshape(NR, NC)
print("Matrix X is as follows:", "\n", matrix)

# For finding the Rank of a Matrix
print("The Rank of a Matrix is:", np.linalg.matrix_rank(matrix))
