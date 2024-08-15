import numpy as np
import random

# Função a ser minimizada
def funcao(x, y, z):
    return 2 * ((-x * np.sin(np.sqrt(abs(x)))) - y * np.sin(np.sqrt(abs(y)))) * (x / 250)

# Inicializa a população com indivíduos aleatórios
def inicializar_populacao(tamanho_populacao, limites):
    populacao = []

    for _ in range(tamanho_populacao):
        individuo = np.array([
            random.uniform(limites[0], limites[1]), # Gene X
            random.uniform(limites[0], limites[1]), # Gene Y
            random.uniform(limites[0], limites[1]), # Gene Z
        ])
        populacao.append(individuo)

    return populacao

# Avalia a aptidão de cada indivíduo na população
def avaliar_populacao(populacao):
    aptidoes = []
    
    for individuo in populacao:
        x, y, z = individuo  
        aptidao = funcao(x, y, z)  
        aptidoes.append(aptidao)  
    
    return aptidoes

# Seleciona os pais para a reprodução com base na aptidão (menores valores)
def selecionar_pais(populacao, aptidoes, num_pais):
   # Combina cada indivíduo com sua aptidão em uma lista de tuplas
   individuos_com_aptidoes = list(zip(populacao, aptidoes))
    
   # Ordena a lista de tuplas pela aptidão, do menor para o maior (aptidão menor é melhor)
   individuos_ordenados = sorted(individuos_com_aptidoes, key=lambda x: x[1])

   # Seleciona os primeiros 'num_pais' indivíduos da lista ordenada (os melhores)
   pais_selecionados = [individuo[0] for individuo in individuos_ordenados[:num_pais]]
    
   return pais_selecionados

# Realiza cruzamento (crossover) entre os pais para criar nova geração
def cruzamento(pais, taxa_cruzamento):
    nova_geracao = []
    for _ in range(len(pais) // 2):
        if random.random() < taxa_cruzamento:
            ponto_corte = random.randint(1, len(pais[0]) - 1)
            pai1, pai2 = random.sample(pais, 2)
            filho1 = np.concatenate((pai1[:ponto_corte], pai2[ponto_corte:]))
            filho2 = np.concatenate((pai2[:ponto_corte], pai1[ponto_corte:]))
            nova_geracao.extend([filho1, filho2])
    return nova_geracao


# Realiza a mutação em alguns indivíduos da nova geração
def mutacao(populacao, taxa_mutacao, limites):
    for individuo in populacao:
        if random.random() < taxa_mutacao:
            indice_mutacao = random.randint(0, len(individuo) - 1)
            individuo[indice_mutacao] = random.uniform(limites[0], limites[1])
    return populacao


# Algoritmo genético principal
def algoritmo_genetico(tamanho_populacao, limites, num_geracoes, taxa_cruzamento, taxa_mutacao):
    populacao = inicializar_populacao(tamanho_populacao, limites) 
    melhor_solucao = None 
    melhor_aptidao = float('inf') 

    for _ in range(num_geracoes):
        aptidoes = avaliar_populacao(populacao) 
        pais = selecionar_pais(populacao, aptidoes, tamanho_populacao // 2) 
        filhos = cruzamento(pais, taxa_cruzamento) 
        filhos = mutacao(filhos, taxa_mutacao, limites)  

        populacao = pais + filhos 
        aptidoes = avaliar_populacao(populacao)  # Recalcula aptidões após criar nova geração 
        
        melhor_aptidao_geracao = min(aptidoes) 
        if melhor_aptidao_geracao < melhor_aptidao: 
            melhor_aptidao = melhor_aptidao_geracao 
            melhor_solucao = populacao[aptidoes.index(melhor_aptidao_geracao)] 

    return melhor_solucao, melhor_aptidao 

# Parâmetros do algoritmo
tamanho_populacao = 250
limites = (-500, 500)
num_geracoes = 250
taxa_cruzamento = 0.7
taxa_mutacao = 0.01

# Executa o algoritmo genético
melhor_solucao, melhor_aptidao = algoritmo_genetico(tamanho_populacao, limites, num_geracoes, taxa_cruzamento, taxa_mutacao)

print("Melhor solução encontrada:", melhor_solucao)
print("Valor da função para a melhor solução:", melhor_aptidao)
