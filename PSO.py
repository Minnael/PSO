import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_particles(enxame, iteracao, ax):
    ax.clear()  # LIMPA O GRÁFICO ANTERIOR
    
    # Cria a malha para x e z
    x = np.linspace(-10, 10, 10)
    z = np.linspace(-10, 10, 10)
    x, z = np.meshgrid(x, z)
    
    # Calcula a função na malha (x, z)
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
        particle_x = particle.position_i[0]  # Extrai x da posição da partícula
        particle_z = particle.position_i[2]  # Extrai z da posição da partícula
        
        # Chama a nova função com x e z para calcular y
        particle_y = funcao(particle_x, particle_z)
        
        # Escolhe a cor para a partícula
        color = colors[idx % len(colors)]
        
        # Plota a partícula
        ax.scatter(particle_x, particle_z, particle_y, color=color, s=100)

    plt.pause(1)  # Pausa de x segundos para visualizar a atualização



class Particle:
    def __init__(self, inicio_particulas):
        self.position_i = []          # POSIÇÃO DA PARTÍCULA
        self.velocity_i = []          # VELOCIDADE DA PARTÍCULA
        self.pos_best_i = []          # MELHOR POSIÇÃO INDIVIDUAL
        self.err_best_i = -1          # MELHOR ERRO INDIVIDUAL
        self.err_i = -1               # ERRO INDIVIDUAL

        global dimensoes
        dimensoes = len(inicio_particulas)

        for i in range(dimensoes):
            self.velocity_i.append(random.uniform(-1, 1))
            self.position_i.append(inicio_particulas[i])

    def evaluate(self, funcao):
        # Supondo que `self.position_i` seja uma lista com pelo menos dois elementos.
        x = self.position_i[0]  # Primeiro elemento é x
        z = self.position_i[2]  # Terceiro elemento é z

        # Chama a função passando x e z
        self.err_i = funcao(x, z)

        # Atualiza o melhor erro e a melhor posição
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i.copy()
            self.err_best_i = self.err_i

    def atualizar_velocidade(self, pos_best_g):
        w = 0.5  # CONSTANTE DE INERCIA
        c1 = 1   # COGNITIVO
        c2 = 2   # SOCIAL

        for i in range(dimensoes):
            r1 = random.random()
            r2 = random.random()

            vel_cognitiva = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitiva + vel_social

    def atualizar_posicao(self, limites):
        for i in range(dimensoes):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            if self.position_i[i] > limites[i][1]:
                self.position_i[i] = limites[i][1]
            if self.position_i[i] < limites[i][0]:
                self.position_i[i] = limites[i][0]

class PSO:
    def __init__(self, funcao, inicio_particulas, limites, num_particulas, num_iteracoes):
        err_best_g = -1
        pos_best_g = []

        enxame = []
        for i in range(num_particulas):
            enxame.append(Particle(inicio_particulas))

        # INICIALIZA O GRÁFICO
        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection='3d')

        i = 0
        while i < num_iteracoes:
            for j in range(num_particulas):
                enxame[j].evaluate(funcao)

                if enxame[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g = list(enxame[j].position_i)
                    err_best_g = float(enxame[j].err_i)

            for j in range(num_particulas):
                enxame[j].atualizar_velocidade(pos_best_g)
                enxame[j].atualizar_posicao(limites)

            # print(f"Iteração {i+1}")
            # for index, particle in enumerate(swarm):
            # print(f"Partícula {index+1}: Posição = {particle.position_i}")
            
            plot_particles(enxame, i+1, ax)

            i += 1

        print(f'  POSICAO FINAL: {pos_best_g}')
        print(f'RESULTADO FINAL: {err_best_g}')

        plt.show()  # MANTÉM O GRÁFICO FINAL ABERTO

def funcao(x, z):
    return 2*x*z  # CORRESPONDE A 2 * X * Z

PSO(funcao, [10, 10, 10], [(-10, 10), (-10, 10), (-10, 10)], num_particulas=20, num_iteracoes=20)
