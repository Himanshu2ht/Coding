# Practical 7 : Compute Gradient of a scalar field, Divergence
# and Curl of a vector field.

import sympy as sp

# Define symbols (coordinates)
x, y, z = sp.symbols('x y z')

# Example Scalar Field f(x, y, z)
f = x**2 + y**2 + z**2

# Example Vector Field A(x, y, z)
A_x = x * y
A_y = y * z
A_z = z * x
A = sp.Matrix([A_x, A_y, A_z])

# 1. Compute the Gradient of the scalar field f
gradient_f = sp.Matrix([sp.diff(f, var) for var in (x, y, z)])
print("Gradient of f(x, y, z):")
sp.pprint(gradient_f)

# 2. Compute the Divergence of the vector field A
divergence_A = sp.diff(A_x, x) + sp.diff(A_y, y) + sp.diff(A_z, z)
print("\nDivergence of A(x, y, z):")
sp.pprint(divergence_A)

# 3. Compute the Curl of the vector field A
curl_A = sp.Matrix([
    sp.diff(A_z, y) - sp.diff(A_y, z),  # i-component
    sp.diff(A_x, z) - sp.diff(A_z, x),  # j-component
    sp.diff(A_y, x) - sp.diff(A_x, y)   # k-component
])
print("\nCurl of A(x, y, z):")
sp.pprint(curl_A)

