import numpy as np
from sympy import Matrix, simplify

# a)
print("-" * 30)
print("a) Hilbert")
A_mat = Matrix([[1, 1/2, 1/3], 
                [1/2, 1/3, 1/4], 
                [1/3, 1/4, 1/5]])

eigen_a = A_mat.eigenvects()
print("\nEigenvalores: ")
for val, mult, vecs in eigen_a:
    print(f"--> {val.evalf(5)}")
for j, vec in enumerate(vecs):
        print(f"--> Eigenvector: {vec.tolist()}")

# b)
print("\n" + "-" * 30)
print("b) Vandermonde")
B_np = np.array([
    [1, 1, 1, 1],
    [1.01, 1.02, 1.03, 1.04],
    [1.01**2, 1.02**2, 1.03**2, 1.04**2],
    [1.01**3, 1.02**3, 1.03**3, 1.04**3]
])

vals_b, vecs_b = np.linalg.eig(B_np)
print("\nEigenvalores: ")
print(vals_b)
print("\nEigenvector:")
print(vecs_b[:, np.argmax(np.abs(vals_b))])

# c)
print("\n" + "-" * 30)
print("c) 2x2")
C_mat = Matrix([[1, 2], 
                [2, 4.0001]])

eigen_c = C_mat.eigenvects()
for val, mult, vecs in eigen_c:
    print(f"--> Eigenvalor: {val}")
    print(f"-->Vector: {vecs[0].tolist()}")

print(f"\nFin :)")