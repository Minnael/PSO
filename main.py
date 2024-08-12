from PSO import PSO


def func_custom(x):
   return 2 * x[0] * x[2]  # Corresponde a 2 * x * z

initial = [5, 5, 5]
bounds = [(-10, 10), (-10, 10), (-10, 10)]
PSO(func_custom, initial, bounds, num_particles=20, maxiter=30)