import numpy as np
import matplotlib.pyplot as plt

def Grafico(enxame, iteracao, funcao, ax):
    ax.clear()  # LIMPA O GRÁFICO ANTERIOR
    
    # CRIAR A MALHA PARA X e Y
    x = np.linspace(-500, 500, 100)
    y = np.linspace(-500, 500, 100)
    x, y = np.meshgrid(x, y)
    
    # CALCULA A FUNÇÃO NA MALHA X e Y
    z = np.array([funcao([xi, yi]) for xi, yi in zip(x.flatten(), y.flatten())])
    z = z.reshape(x.shape)  # Ajusta o formato para o meshgrid
    
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
        particula_y = particula.posicao_i[1]  # EXTRAI Y DA POSIÇÃO DA PARTICULA
        
        # CALCULA Z PARA A PARTICULA (passando como lista)
        particle_z = funcao([particula_x, particula_y])
        
        # ESCOLHE A COR PARA A PARTICULA
        color = colors[idx % len(colors)]
        
        # PLOTA A PARTICULA
        ax.scatter(particula_x, particula_y, particle_z, color=color, s=100)
    
    plt.pause(1)
