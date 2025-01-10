import random

class Enxame:
    def __init__(self, limites):
        self.posicao_i = []           # POSIÇÃO DA PARTÍCULA
        self.velocidade_i = []        # VELOCIDADE DA PARTÍCULA
        self.melhor_posicao_i = []    # MELHOR POSIÇÃO INDIVIDUAL
        self.melhor_valor_i = float('inf')  # MELHOR VALOR DA PARTÍCULA INDIVIDUAL (inicializado como infinito)
        self.valor_atual_i = float('inf')   # VALOR ATUAL DA PARTÍCULA

        # Inicializa posição e velocidade respeitando os limites fornecidos
        for limite in limites:
            self.posicao_i.append(random.uniform(limite[0], limite[1]))
            self.velocidade_i.append(random.uniform(-abs(limite[1] - limite[0]), abs(limite[1] - limite[0])))

    def avaliar(self, funcao):
        # Avalia a função objetivo para a posição atual da partícula
        self.valor_atual_i = funcao(self.posicao_i)

        # Atualiza o melhor valor e a melhor posição individual se necessário
        if self.valor_atual_i < self.melhor_valor_i:
            self.melhor_posicao_i = self.posicao_i.copy()
            self.melhor_valor_i = self.valor_atual_i

    def atualizar_velocidade(self, pos_best_g, iteracao_atual, num_iteracoes):
        # Parâmetros de inércia, cognição e social
        w = 0.9 - iteracao_atual * ((0.9 - 0.4) / num_iteracoes)  # Redução linear de inércia
        c1 = 1   # Coeficiente cognitivo
        c2 = 1   # Coeficiente social

        for i in range(len(self.posicao_i)):
            r1 = random.random()
            r2 = random.random()

            vel_cognitiva = c1 * r1 * (self.melhor_posicao_i[i] - self.posicao_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.posicao_i[i])
            self.velocidade_i[i] = w * self.velocidade_i[i] + vel_cognitiva + vel_social

    def atualizar_posicao(self, limites):
        # Atualiza a posição da partícula e aplica restrições de limites
        for i in range(len(self.posicao_i)):
            self.posicao_i[i] += self.velocidade_i[i]

            # Garante que a posição está dentro dos limites
            if self.posicao_i[i] > limites[i][1]:
                self.posicao_i[i] = limites[i][1]
            elif self.posicao_i[i] < limites[i][0]:
                self.posicao_i[i] = limites[i][0]
