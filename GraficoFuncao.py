import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def funcao(x, y):
   return 2 * ((-x * np.sin(np.sqrt(abs(x)))) - y * np.sin(np.sqrt(abs(y)))) * (x / 250)

x = np.linspace(-1500, 1500, 1080)
y = np.linspace(-1000, 1000, 1080)
X, Y = np.meshgrid(x, y)

Z = funcao(X, Y)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')

ax.set_title('Gráfico 3D da função')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

ax.set_zlim(-22000, 22000) 

plt.grid()
plt.show()
