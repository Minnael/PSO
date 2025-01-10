from Enxame import Enxame
from Grafico import Grafico
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Variável global para controlar o estado de pausa
pausado = False

def alternar_pausa(event):
    """Alterna entre o estado de pausa e execução."""
    global pausado
    pausado = not pausado
    if pausado:
        pause_botao.label.set_text('Resume')  # Atualiza texto do botão
    else:
        pause_botao.label.set_text('Pause')  # Retorna ao texto original

class PSO:
    def __init__(self, funcao, limites, num_particulas, num_iteracoes):
        """
        Inicializa o algoritmo PSO.
        :param funcao: Função objetivo a ser minimizada.
        :param limites: Lista de tuplas representando os limites de cada dimensão.
        :param num_particulas: Número de partículas no enxame.
        :param num_iteracoes: Número total de iterações.
        """
        # Melhor valor global (inicialmente infinito para problemas de minimização)
        melhor_valor_grupo = float('inf')
        melhor_posicao_grupo = []

        # Inicializa o enxame
        enxame = [Enxame(limites) for _ in range(num_particulas)]

        # Inicializa o gráfico
        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection='3d')

        # Adiciona o botão de pausa
        global pause_botao  # Torna a variável acessível na função alternar_pausa
        pause_posicao = plt.axes([0.85, 0.03, 0.1, 0.05])
        pause_botao = Button(pause_posicao, 'Pause')
        pause_botao.hovercolor = 'lightgreen'
        pause_botao.on_clicked(alternar_pausa)

        # Laço principal de iterações
        for i in range(num_iteracoes):
            # Avaliação e atualização do melhor global
            for particula in enxame:
                particula.avaliar(funcao)
                if particula.valor_atual_i < melhor_valor_grupo:
                    melhor_posicao_grupo = particula.posicao_i.copy()
                    melhor_valor_grupo = particula.valor_atual_i

            # Atualização de velocidade e posição
            for particula in enxame:
                particula.atualizar_velocidade(melhor_posicao_grupo, i, num_iteracoes)
                particula.atualizar_posicao(limites)

            # Atualiza o gráfico para a iteração atual
            Grafico(enxame, i + 1, funcao, ax)

            # Controle de pausa
            while pausado:
                plt.pause(0.1)

        # Resultados finais
        print("\n==== RESULTADOS FINAIS ====")
        print(f"Posição Final: {melhor_posicao_grupo}")
        print(f"Resultado Final: {melhor_valor_grupo:.4f}")

        plt.show()  # Mantém o gráfico final aberto
