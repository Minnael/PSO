import numpy as np
import matplotlib.pyplot as plt

def Grafico(enxame, iteracao, funcao, ax):
   ax.clear()  # LIMPA O GRÁFICO ANTERIOR
    
   # CRIAR A MALHA PARA X, Z
   x = np.linspace(-10, 10, 10)
   z = np.linspace(-10, 10, 10)
   x, z = np.meshgrid(x, z)
    
   # CALCULA A FUNÇÃO NA MALHA X, Z
   y = funcao(x, z)  # Chama a nova função com x e z
    
   # CONFIGURAÇÕES DO GRÁFICO
   ax.set_title(f'Iteração {iteracao}')
   ax.set_xlabel('X')
   ax.set_ylabel('Z')
   ax.set_zlabel('f(x, z)')
   ax.set_xlim([-10, 10])
   ax.set_ylim([-10, 10])
   ax.set_zlim([-200, 200])

   # PLOTAGEM DA SUPERFÍCIE
   ax.plot_surface(x, z, y, cmap='viridis', alpha=0.6)
    

   # LISTA DE CORES PREDEFINIDAS
   colors = ['red', 'yellow', 'green', 'blue', 'pink', 'purple', 'orange', 'black']
    
   # PLOTAGEM DAS PARTÍCULAS COM CORES PREDEFINIDAS
   for idx, particle in enumerate(enxame):
      particle_x = particle.position_i[0]  # EXTRAI X DA POSIÇÃO DA PARTICULA
      particle_z = particle.position_i[2]  # EXTRAI Z DA POSICAO DA PARTICULA
        
      # CHAMA A NOVA FUNÇÃO COM X, Z PARA CALCULAR Y
      particle_y = funcao(particle_x, particle_z)
        
      # ESCOLHE A COR PARA A PARTICULA
      color = colors[idx % len(colors)]
        
      # PLOTA A PARTICULA
      ax.scatter(particle_x, particle_z, particle_y, color=color, s=100)
    
   plt.pause(1)