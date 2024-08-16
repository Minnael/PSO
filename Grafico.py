import numpy as np
import matplotlib.pyplot as plt

def Grafico(enxame, iteracao, funcao, ax):
   ax.clear()  # LIMPA O GRÁFICO ANTERIOR
    
   # CRIAR A MALHA PARA X, Z
   x = np.linspace(-500, 500, 100)
   y = np.linspace(-500, 500, 100)
   x, y = np.meshgrid(x, y)
    
   # CALCULA A FUNÇÃO NA MALHA X, Z
   z = funcao(x, y)  # Chama a nova função com x e z
    
   # CONFIGURAÇÕES DO GRÁFICO
   ax.set_title(f'Iteração {iteracao}')
   ax.set_xlabel('x')
   ax.set_ylabel('y')
   ax.set_zlabel('F(x, y)')

   # PLOTAGEM DA SUPERFÍCIE
   ax.plot_surface(x, y, z, cmap='viridis', alpha=0.4)
    

   # LISTA DE CORES PREDEFINIDAS
   colors = ['red', 'yellow', 'green', 'blue', 'pink', 'purple', 'orange', 'black']
    
   # PLOTAGEM DAS PARTÍCULAS COM CORES PREDEFINIDAS
   for idx, particula in enumerate(enxame):
      particula_x = particula.posicao_i[0]  # EXTRAI X DA POSIÇÃO DA PARTICULA
      particula_y = particula.posicao_i[1]  # EXTRAI Z DA POSICAO DA PARTICULA
        
      # CHAMA A NOVA FUNÇÃO COM X, Z PARA CALCULAR Y
      particle_y = funcao(particula_x, particula_y)
        
      # ESCOLHE A COR PARA A PARTICULA
      color = colors[idx % len(colors)]
        
      # PLOTA A PARTICULA
      ax.scatter(particula_x, particula_y, particle_y, color=color, s=100)
    
   plt.pause(1)




'''
ESBOÇO DA FUNÇÃO APENAS:
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definição da função
def funcao(x, y):
    return 2 * ((-x * np.sin(np.sqrt(abs(x)))) - y * np.sin(np.sqrt(abs(y)))) * (x / 250)

# Criação da grade de valores para x e y
x = np.linspace(-500, 500, 100)
y = np.linspace(-500, 500, 100)
x, y = np.meshgrid(x, y)

# Cálculo dos valores de z com base na função
z = funcao(x, y)

# Criação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotagem da superfície
ax.plot_surface(x, y, z, cmap='viridis')

# Adição de rótulos aos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')

# Exibição do gráfico
plt.show()
'''


'''
   RASTRIGIN:
   x = np.linspace(-5.12, 5.12, 400)
   z = np.linspace(-5.12, 5.12, 400)
   ax.set_xlim([-6, 6])
   ax.set_ylim([-6, 6])
   ax.set_zlim([0, 100])
'''
