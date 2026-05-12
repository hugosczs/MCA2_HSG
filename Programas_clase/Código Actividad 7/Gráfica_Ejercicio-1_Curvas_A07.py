import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi/3, np.pi/3, 500)
y1 = 8*np.cos(x)
y2 = 1/np.cos(x)**2

plt.plot(x, y1, label='8cos(x)')
plt.plot(x, y2, label='sec^2(x)')
plt.fill_between(x, y1, y2, alpha=0.3)
plt.legend()
plt.grid()
plt.show()