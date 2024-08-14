from PSO import PSO
import numpy as np

def funcao(x, y):
   return 2*((-x*np.sin(np.sqrt(abs(x))))-y*np.sin(np.sqrt(abs(y)))) * (x/250)

PSO(funcao, [(-500, 500), (-500, 500), (-500, 500)], num_particulas=15, num_iteracoes=40)





'''
def funcao_rastrigin(x, z):
   A = 10
   return A * 2 + (x**2 - A * np.cos(2 * np.pi * x)) + (z**2 - A * np.cos(2 * np.pi * z))

#RASTRIGIN PSO(funcao_rastrigin, [0, 50, 0], [(-10, 10), (-10, 10), (-10, 10)], num_particulas=20, num_iteracoes=20)
'''