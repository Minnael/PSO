import random


class Enxame:
    def __init__(self):
        self.posicao_i = []           # POSIÇÃO DA PARTÍCULA
        self.velocidade_i = []        # VELOCIDADE DA PARTÍCULA
        self.melhor_posicao_i = []    # MELHOR POSIÇÃO INDIVIDUAL
        self.melhor_valor_i = -1      # MELHOR ERRO INDIVIDUAL
        self.valor_atual_i = -1       # ERRO INDIVIDUAL

        for i in range(3):
            self.velocidade_i.append(random.uniform(-1, 1))
            self.posicao_i.append(random.uniform(-500, 500))

    def avaliar(self, funcao):
        x = self.posicao_i[0]  
        y = self.posicao_i[1]  

        # CHAMA A FUNÇÃO PASSANDO X e Y
        self.valor_atual_i = funcao(x, y)

        # ATUALIZA O MELHOR VALOR E A MELHOR POSIÇÃO
        if self.valor_atual_i < self.melhor_valor_i or self.melhor_valor_i == -1:
            self.melhor_posicao_i = self.posicao_i.copy()
            self.melhor_valor_i = self.valor_atual_i

    def atualizar_velocidade(self, pos_best_g, iteracao_atual, num_iteracoes):
        w = 0.9 - iteracao_atual*((0.9 - 0.4)/num_iteracoes) # CONSTANTE DE INERCIA
        c1 = 1   # COGNITIVO
        c2 = 1   # SOCIAL

        for i in range(3):
            r1 = random.random()
            r2 = random.random()

            vel_cognitiva = c1 * r1 * (self.melhor_posicao_i[i] - self.posicao_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.posicao_i[i])
            self.velocidade_i[i] = w * self.velocidade_i[i] + vel_cognitiva + vel_social

    def atualizar_posicao(self, limites):
        for i in range(3):
            self.posicao_i[i] = self.posicao_i[i] + self.velocidade_i[i]

            if self.posicao_i[i]  > limites[i][1]:
                self.posicao_i[i] = limites[i][1]
            if self.posicao_i[i]  < limites[i][0]:
                self.posicao_i[i] = limites[i][0]