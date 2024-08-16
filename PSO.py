from Enxame import Enxame
from Grafico import Grafico
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


# VARIÁVEL GLOBAL PARA CONTROLAR O ESTADO DE PAUSA
pausado = False

# FUNÇÃO CHAMADA PELO BOTÃO PAUSE
def alternar_pausa(event):
    global pausado
    pausado = not pausado  # ALTERNA ENTRE PAUSADO E NÃO PAUSADO

class PSO:
    def __init__(self, funcao, limites, num_particulas, num_iteracoes):
        melhor_valor_g = -1
        melhor_posicao_g = []

        enxame = []
        for i in range(num_particulas):
            enxame.append(Enxame())

        # INICIALIZA O GRÁFICO
        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection='3d')

        # ADICIONA O BOTÃO DE PAUSE
        pause_posicao = plt.axes([0.85, 0.03, 0.1, 0.05])
        pause_botao = Button(pause_posicao, 'Pause')
        #pause_botao.label.set_color('red')
        #pause_botao.color = 'red'
        pause_botao.hovercolor = 'lightgreen'
        pause_botao.on_clicked(alternar_pausa)

        i = 0
        while i < num_iteracoes:
            for j in range(num_particulas):
                enxame[j].avaliar(funcao)

                if enxame[j].valor_atual_i < melhor_valor_g or melhor_valor_g == -1:
                    melhor_posicao_g = list(enxame[j].posicao_i)
                    melhor_valor_g = float(enxame[j].valor_atual_i)

            for j in range(num_particulas):
                enxame[j].atualizar_velocidade(melhor_posicao_g, i, num_iteracoes)
                enxame[j].atualizar_posicao(limites)

            # print(f"Iteração {i+1}")
            # for index, particle in enumerate(swarm):
            # print(f"Partícula {index+1}: Posição = {particle.position_i}")
            
            Grafico(enxame, i+1, funcao, ax)

            # ESPERA O BOTÃO DE MOUSE SER DESATIVADO
            while pausado:
                plt.pause(0.1)

            i += 1

        print(f'POSICAO FINAL: {melhor_posicao_g}')
        print(f'RESULTADO FINAL: {melhor_valor_g}')

        plt.show()  # MANTÉM O GRÁFICO FINAL ABERTO
