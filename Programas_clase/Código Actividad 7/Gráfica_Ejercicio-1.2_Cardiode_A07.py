import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

a = 1
t = np.linspace(0, 2*np.pi, 500)

x = a*(2*np.cos(t) - np.cos(2*t))
y = a*(2*np.sin(t) - np.sin(2*t))

plt.plot(x, y)
plt.axis('equal')
plt.grid()
plt.savefig('Cardiode.png')
plt.show()

def integrando(t):
    y = 2*np.sin(t) - np.sin(2*t)
    dx = -2*np.sin(t) + 2*np.sin(2*t)
    return y * dx

area, _ = integrate.quad(integrando, 0, np.pi)
print("Area =", -area)
print("Area =", -area, "(3π =", 3*np.pi, ")")