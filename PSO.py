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
        err_best_g = -1
        pos_best_g = []

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
                enxame[j].evaluate(funcao)

                if enxame[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g = list(enxame[j].posicao_i)
                    err_best_g = float(enxame[j].err_i)

            for j in range(num_particulas):
                enxame[j].atualizar_velocidade(pos_best_g, i, num_iteracoes)
                enxame[j].atualizar_posicao(limites)

            # print(f"Iteração {i+1}")
            # for index, particle in enumerate(swarm):
            # print(f"Partícula {index+1}: Posição = {particle.position_i}")
            
            Grafico(enxame, i+1, funcao, ax)

            # ESPERA O BOTÃO DE MOUSE SER DESATIVADO
            while pausado:
                plt.pause(0.1)

            i += 1

        print(f'  POSICAO FINAL: {pos_best_g}')
        print(f'RESULTADO FINAL: {err_best_g}')

        plt.show()  # MANTÉM O GRÁFICO FINAL ABERTO
