import numpy as np
import matplotlib.pyplot as plt

# a)
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x_range = np.linspace(-5, 5, 10)
y_range = np.linspace(-5, 5, 10)
X, Y = np.meshgrid(x_range, y_range)

Z1 = (1 - X - 0.5*Y) * 3
Z2 = (0 - 0.5*X - (1/3)*Y) * 4
Z3 = (0 - (1/3)*X - 0.25*Y) * 5

ax.plot_surface(X, Y, Z1, alpha=0.5, color='blue')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='green')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='red')

ax.set_title("a) Hilbert")
plt.show()

# b)
plt.figure(figsize=(8, 6))
t = np.linspace(1.00, 1.05, 500)

plt.plot(t, np.ones_like(t), label='(x^0)')
plt.plot(t, t, label='(x^1)')
plt.plot(t, t**2, label='(x^2)')
plt.plot(t, t**3, label='(x^3)')

plt.title("b) Vandermonde")
plt.xlabel("Coeficientes")
plt.ylabel("Potencia")
plt.legend()
plt.grid(True)  
plt.show()

# c)
plt.figure(figsize=(8, 6))
x = np.linspace(0, 2, 400)

y1 = (3 - x) / 2
y2 = (6.0001 - 2 * x) / 4.0001

plt.plot(x, y1, 'blue', label='x + 2y = 3')
plt.plot(x, y2, 'red', linestyle='--', label='2x + 4.0001y = 6.0001')

plt.title("c) 2x2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()