import random


class Enxame:
    def __init__(self, inicio_particulas):
        self.position_i = []          # POSIÇÃO DA PARTÍCULA
        self.velocity_i = []          # VELOCIDADE DA PARTÍCULA
        self.pos_best_i = []          # MELHOR POSIÇÃO INDIVIDUAL
        self.err_best_i = -1          # MELHOR ERRO INDIVIDUAL
        self.err_i = -1               # ERRO INDIVIDUAL

        global dimensoes
        dimensoes = len(inicio_particulas)

        for i in range(dimensoes):
            self.velocity_i.append(random.uniform(-1, 1))
            self.position_i.append(inicio_particulas[i])

    def evaluate(self, funcao):
        # Supondo que `self.position_i` seja uma lista com pelo menos dois elementos.
        x = self.position_i[0]  # Primeiro elemento é x
        z = self.position_i[2]  # Terceiro elemento é z

        # Chama a função passando x e z
        self.err_i = funcao(x, z)

        # ATUALIZA O MELHOR ERRO E A MELHOR POSIÇÃO
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i.copy()
            self.err_best_i = self.err_i

    def atualizar_velocidade(self, pos_best_g):
        w = 0.5  # CONSTANTE DE INERCIA
        c1 = 1   # COGNITIVO
        c2 = 2   # SOCIAL

        for i in range(dimensoes):
            r1 = random.random()
            r2 = random.random()

            vel_cognitiva = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitiva + vel_social

    def atualizar_posicao(self, limites):
        for i in range(dimensoes):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            if self.position_i[i] > limites[i][1]:
                self.position_i[i] = limites[i][1]
            if self.position_i[i] < limites[i][0]:
                self.position_i[i] = limites[i][0]