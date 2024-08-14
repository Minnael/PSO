import random


class Enxame:
    def __init__(self):
        self.posicao_i = []           # POSIÇÃO DA PARTÍCULA
        self.velocidade_i = []        # VELOCIDADE DA PARTÍCULA
        self.pos_best_i = []          # MELHOR POSIÇÃO INDIVIDUAL
        self.err_best_i = -1          # MELHOR ERRO INDIVIDUAL
        self.err_i = -1               # ERRO INDIVIDUAL

        for i in range(3):
            self.velocidade_i.append(random.uniform(-1, 1))
            self.posicao_i.append(random.uniform(-500, 500))

    def evaluate(self, funcao):
        # Supondo que `self.posicao_i` seja uma lista com pelo menos dois elementos.
        x = self.posicao_i[0]  # Primeiro elemento é x
        z = self.posicao_i[2]  # Terceiro elemento é z

        # Chama a função passando x e z
        self.err_i = funcao(x, z)

        # ATUALIZA O MELHOR ERRO E A MELHOR POSIÇÃO
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.posicao_i.copy()
            self.err_best_i = self.err_i

    def atualizar_velocidade(self, pos_best_g, iteracao_atual, num_iteracoes):
        w = 0.9 - iteracao_atual*((0.9 - 0.4)/num_iteracoes) # CONSTANTE DE INERCIA
        c1 = 1   # COGNITIVO
        c2 = 1   # SOCIAL

        for i in range(3):
            r1 = random.random()
            r2 = random.random()

            vel_cognitiva = c1 * r1 * (self.pos_best_i[i] - self.posicao_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.posicao_i[i])
            self.velocidade_i[i] = w * self.velocidade_i[i] + vel_cognitiva + vel_social

    def atualizar_posicao(self, limites):
        for i in range(3):
            self.posicao_i[i] = self.posicao_i[i] + self.velocidade_i[i]

            if self.posicao_i[i] > limites[i][1]:
                self.posicao_i[i] = limites[i][1]
            if self.posicao_i[i] < limites[i][0]:
                self.posicao_i[i] = limites[i][0]