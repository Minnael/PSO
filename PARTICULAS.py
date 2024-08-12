import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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