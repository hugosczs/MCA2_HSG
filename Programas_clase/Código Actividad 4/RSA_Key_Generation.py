import math

# 1: Generar dos primos diferentes p, q
p = 499 
q = 503 

# 2: Calcular módulo n
n = p * q

# 3: Calcular phi deEuler
phi = (p - 1) * (q - 1)

# 4: Elegir un entero e
e = 65537
if math.gcd(e, phi) != 1:
    e = 17 

# 5: Calcular el inverso multiplicativo modular d
d = pow(e, -1, phi)

# PASO 6: Retornar Llave Pública (n, e) yPrivada (n, d)
print(f"Llave Pública (n, e): ({n}, {e})")
print(f"Llave Privada (n, d): ({n}, {d})")