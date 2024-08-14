from PSO import PSO

def funcao(x, z):
   return 2*x*z 

PSO(funcao, [10, 10, 10], [(-10, 10), (-10, 10), (-10, 10)], num_particulas=20, num_iteracoes=20)