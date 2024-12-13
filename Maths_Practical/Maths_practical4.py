# Solve a system of equations using the Gauss Jordan method.

import numpy as np

# Taking input for Coefficient Matrix (A)
print("Enter the dimensions of the coefficient matrix (A):")
NR = int(input("Enter the number of rows: "))
NC = int(input("Enter the number of columns: "))

# Taking input for the elements of matrix A
print("Enter the elements of the coefficient matrix (A) in a single line (separated by spaces):")
Coefficients_Entries = list(map(float, input().split()))
Coefficient_Matrix = np.array(Coefficients_Entries).reshape(NR, NC)
print("Coefficient Matrix (A) is as follows:\n", Coefficient_Matrix, "\n")

# Taking input for Column Matrix (B)
print("Enter the elements of the column matrix (B) in a single line (separated by spaces):")
Column_Entries = list(map(float, input().split()))
Column_Matrix = np.array(Column_Entries).reshape(NR, 1)
print("Column Matrix (B) is as follows:\n", Column_Matrix, "\n")

#Solution of homogenous system of equations using Gauss Jordan
inv_ofcoefficient_matrix = np.linalg.inv(Coefficient_Matrix)
Solution_of_the_system_of_equations=np.matmul(inv_ofcoefficient_matrix,Column_Matrix)
print("Solution of the system of Equations using GAUSS JORDAN")
print(Solution_of_the_system_of_equations)
