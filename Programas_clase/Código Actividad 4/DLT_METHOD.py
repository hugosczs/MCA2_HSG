import numpy as np

# 1. DATOS DE LA TABLA X, Y, Z

# Puntos 3D (cm)
world_points = np.array([
    [0, 0, 10],      # A
    [19.5, 0, 10],   # B
    [19.5, 32, 10],  # C
    [0, 32, 10],     # D
    [0, 0, 41],      # E
    [19.5, 0, 41],   # F
    [19.5, 32, 41]   # G
])

# Puntos 2D (pixeles) de A, B, C, D, E, F, G hechos en Paint.
image_points = np.array([
    [233, 1324],  # A
    [677, 1556],  # B
    [1024, 1071], # C
    [708, 46],    # D
    [156, 257],   # E
    [778, 433],   # F
    [1202, 147]   # G
])

# 2. PINHOLE MODEL (calcular f)

print("=== CÁLCULO DE f (Pinhole Model) ===")

f_values = []

for i in range(len(world_points)):
    X, Y, Z = world_points[i]
    u, v = image_points[i]

    if X != 0:
        f = (u * Z) / X
        f_values.append(f)
        print(f"Punto {i}: f = {f:.2f}")

f_promedio = np.mean(f_values)
print(f"\nf promedio ≈ {f_promedio:.2f}")

# 3. DLT

print("\n=== DLT ===")

M = []
B = []

for i in range(len(world_points)):
    X, Y, Z = world_points[i]
    u, v = image_points[i]

    M.append([X, Y, Z, 1, 0, 0, 0, 0, -u*X, -u*Y, -u*Z])
    M.append([0, 0, 0, 0, X, Y, Z, 1, -v*X, -v*Y, -v*Z])

    B.append(u)
    B.append(v)

M = np.array(M)
B = np.array(B)

L, _, _, _ = np.linalg.lstsq(M, B, rcond=None)

print("Parámetros DLT:")
print(L)

# 4. VALIDACIÓN

print("\n=== VALIDACIÓN ===")

def proyectar(X, Y, Z, L):
    u = (L[0]*X + L[1]*Y + L[2]*Z + L[3]) / (L[8]*X + L[9]*Y + L[10]*Z + 1)
    v = (L[4]*X + L[5]*Y + L[6]*Z + L[7]) / (L[8]*X + L[9]*Y + L[10]*Z + 1)
    return u, v

for i in range(len(world_points)):
    X, Y, Z = world_points[i]
    u_real, v_real = image_points[i]

    u_calc, v_calc = proyectar(X, Y, Z, L)

    error_u = abs(u_real - u_calc)
    error_v = abs(v_real - v_calc)

    print(f"Punto {i}: error_u = {error_u:.2f}, error_v = {error_v:.2f}")