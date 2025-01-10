from PSO import PSO
import numpy as np

# Parâmetros do problema
P_demand = 100  # Demanda total de energia
limites = [(10, 50), (20, 60), (30, 70)]  # Limites de operação das usinas
coeficientes = [(0.02, 1.5, 10), (0.03, 2, 20), (0.01, 2.5, 30)]  # Coeficientes a, b, c
penalidade_peso = 1000  # Peso da penalidade

# Função objetivo
def funcao(variaveis):
    P = [0] * len(coeficientes)  # Inicializa o vetor P com zeros
    for i, var in enumerate(variaveis):
        P[i] = var  # Substitui os valores conhecidos
    
    # Calcula os custos
    C = [a * P[i]**2 + b * P[i] + c for i, (a, b, c) in enumerate(coeficientes)]
    
    # Custo total
    custo_total = sum(C)
    
    # Penalidade para equilíbrio de potência
    demanda = sum(P)
    penalidade_equilibrio = abs(demanda - P_demand) * penalidade_peso
    
    # Penalidade para limites de operação
    penalidade_limites = sum([
        penalidade_peso * (max(0, P[i] - limites[i][1]) + max(0, limites[i][0] - P[i]))
        for i in range(len(P))
    ])
    
    return custo_total + penalidade_equilibrio + penalidade_limites


# Chamada do PSO
PSO(funcao, limites, num_particulas=15, num_iteracoes=40)
