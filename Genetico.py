import numpy as np
import random

# FUNÇÃO A SER MINIMIZADA
def funcao(x, y):
    return 2 * ((-x * np.sin(np.sqrt(abs(x)))) - y * np.sin(np.sqrt(abs(y)))) * (x / 250)

# INICIALIZA A POPULAÇÃO COM INDIVÍDUOS ALEATÓRIOS
def inicializar_populacao(tamanho_populacao, limites):
    populacao = []

    for _ in range(tamanho_populacao):
        individuo = np.array([
            random.uniform(limites[0], limites[1]), # GENE X
            random.uniform(limites[0], limites[1]), # GENE Y
            #RANDOM.UNIFORM(LIMITES[0], LIMITES[1]), # GENE Z
        ])
        populacao.append(individuo)

    return populacao

# AVALIA A APTIDÃO DE CADA INDIVÍDUO NA POPULAÇÃO
def avaliar_populacao(populacao):
    aptidoes = []
    
    for individuo in populacao:
        x, y = individuo  
        aptidao = funcao(x, y)  
        aptidoes.append(aptidao)  
    
    return aptidoes

# SELECIONA OS PAIS PARA A REPRODUÇÃO COM BASE NA APTIDÃO (MENORES VALORES)
def selecionar_pais(populacao, aptidoes, num_pais):
   # COMBINA CADA INDIVÍDUO COM SUA APTIDÃO EM UMA LISTA DE TUPLAS
   individuos_com_aptidoes = list(zip(populacao, aptidoes))
    
   # ORDENA A LISTA DE TUPLAS PELA APTIDÃO, DO MENOR PARA O MAIOR (APTIDÃO MENOR É MELHOR)
   individuos_ordenados = sorted(individuos_com_aptidoes, key=lambda x: x[1])

   # SELECIONA OS PRIMEIROS 'NUM_PAIS' INDIVÍDUOS DA LISTA ORDENADA (OS MELHORES)
   pais_selecionados = [individuo[0] for individuo in individuos_ordenados[:num_pais]]
    
   return pais_selecionados

# REALIZA CRUZAMENTO (CROSSOVER) ENTRE OS PAIS PARA CRIAR NOVA GERAÇÃO
def cruzamento(pais, taxa_cruzamento):
    nova_geracao = []
    for _ in range(len(pais) // 2):
        if random.random() < taxa_cruzamento:
            ponto_corte = random.randint(0, len(pais[0]) - 1)
            pai1, pai2 = random.sample(pais, 2)
            filho1 = np.concatenate((pai1[:ponto_corte], pai2[ponto_corte:]))
            filho2 = np.concatenate((pai2[:ponto_corte], pai1[ponto_corte:]))
            nova_geracao.extend([filho1, filho2])
    return nova_geracao


# REALIZA A MUTAÇÃO EM ALGUNS INDIVÍDUOS DA NOVA GERAÇÃO
def mutacao(populacao, taxa_mutacao, limites):
    for individuo in populacao:
        if random.random() < taxa_mutacao:
            indice_mutacao = random.randint(0, len(individuo) - 1)
            individuo[indice_mutacao] = random.uniform(limites[0], limites[1])
    return populacao


# ALGORITMO GENÉTICO PRINCIPAL
def algoritmo_genetico(tamanho_populacao, limites, num_geracoes, taxa_cruzamento, taxa_mutacao):
    populacao = inicializar_populacao(tamanho_populacao, limites) 
    melhor_solucao = None 
    melhor_aptidao = float('inf') 

    for i in range(num_geracoes):
        aptidoes = avaliar_populacao(populacao) 
        pais = selecionar_pais(populacao, aptidoes, tamanho_populacao // 2) 
        filhos = cruzamento(pais, taxa_cruzamento) 
        filhos = mutacao(filhos, taxa_mutacao, limites)  

        populacao = pais + filhos 
        aptidoes = avaliar_populacao(populacao)  # RECALCULA APTIDÕES APÓS CRIAR NOVA GERAÇÃO 
        
        melhor_aptidao_geracao = min(aptidoes) 
        if melhor_aptidao_geracao < melhor_aptidao: 
            melhor_aptidao = melhor_aptidao_geracao 
            melhor_solucao = populacao[aptidoes.index(melhor_aptidao_geracao)]
            melhor_geracao = i 

    return melhor_solucao, melhor_aptidao, melhor_geracao 

# PARÂMETROS DO ALGORITMO
tamanho_populacao = 35
limites = (-500, 500)
num_geracoes = 1000
taxa_cruzamento = 0.7
taxa_mutacao = 0.01

# EXECUTA O ALGORITMO GENÉTICO
melhor_solucao, melhor_aptidao, geracao = algoritmo_genetico(tamanho_populacao, limites, num_geracoes, taxa_cruzamento, taxa_mutacao)

print("Melhor solução encontrada:", melhor_solucao)
print("Valor da função para a melhor solução:", melhor_aptidao)
print("Geração:", geracao)
