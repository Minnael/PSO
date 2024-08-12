import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#--- FUNÇÃO DE CUSTO ----------------------------------------------------------+

def func_custom(x):
    return 2 * x[0] * x[2]  # Corresponde a 2 * x * z

#--- PRINCIPAL ----------------------------------------------------------------+

def plot_particles(swarm, iteration, ax):
    ax.clear()  # Limpa o gráfico anterior
    x = np.linspace(-10, 10, 100)
    z = np.linspace(-10, 10, 100)
    x, z = np.meshgrid(x, z)
    y = func_custom([x, 0, z])  # Calcula a função na malha

    # Configurações do gráfico
    ax.set_title(f'Iteração {iteration}')
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_zlabel('f(x, z)')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-200, 200])

    # Plotagem da superfície
    ax.plot_surface(x, z, y, cmap='viridis', alpha=0.6)

    # Lista de cores predefinidas
    colors = ['red', 'yellow', 'green', 'blue', 'pink', 'purple', 'orange', 'black']
    
    # Plotagem das partículas com cores predefinidas
    for idx, particle in enumerate(swarm):
        particle_x = particle.position_i[0]
        particle_z = particle.position_i[2]
        particle_y = func_custom(particle.position_i)
        color = colors[idx % len(colors)]  # Escolhe a cor com base no índice
        ax.scatter(particle_x, particle_z, particle_y, color=color, s=100)

    plt.pause(1)  # Pausa de 2 segundos para visualizar a atualização

class Particle:
    def __init__(self, x0):
        self.position_i = []          # posição da partícula
        self.velocity_i = []          # velocidade da partícula
        self.pos_best_i = []          # melhor posição individual
        self.err_best_i = -1          # melhor erro individual
        self.err_i = -1               # erro individual

        for i in range(num_dimensions):
            self.velocity_i.append(random.uniform(-1, 1))
            self.position_i.append(x0[i])

    def evaluate(self, costFunc):
        self.err_i = costFunc(self.position_i)

        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i.copy()
            self.err_best_i = self.err_i

    def update_velocity(self, pos_best_g):
        w = 0.5
        c1 = 1
        c2 = 2

        for i in range(num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel_cognitiva = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitiva + vel_social

    def update_position(self, bounds):
        for i in range(num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            if self.position_i[i] > bounds[i][1]:
                self.position_i[i] = bounds[i][1]
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i] = bounds[i][0]

class PSO:
    def __init__(self, costFunc, x0, bounds, num_particles, maxiter):
        global num_dimensions

        num_dimensions = len(x0)
        err_best_g = -1
        pos_best_g = []

        swarm = []
        for i in range(num_particles):
            swarm.append(Particle(x0))

        # Inicializa o gráfico
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        i = 0
        while i < maxiter:
            for j in range(num_particles):
                swarm[j].evaluate(costFunc)

                if swarm[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g = list(swarm[j].position_i)
                    err_best_g = float(swarm[j].err_i)

            for j in range(num_particles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)

            print(f"Iteração {i+1}")
            for index, particle in enumerate(swarm):
                print(f"Partícula {index+1}: Posição = {particle.position_i}")
            
            plot_particles(swarm, i+1, ax)

            i += 1

        print('/////////////// FINAL //////////////////')
        print(f'POSICAO FINAL: {pos_best_g}')
        print(f'RESULTADO FINAL: {err_best_g}')

        plt.show()  # Mantém o gráfico final aberto

#--- EXECUTAR -----------------------------------------------------------------+

initial = [5, 5, 5]
bounds = [(-10, 10), (-10, 10), (-10, 10)]
PSO(func_custom, initial, bounds, num_particles=20, maxiter=30)