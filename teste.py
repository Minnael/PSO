import threading
import time
import keyboard  # Biblioteca para detectar eventos do teclado

# Variável global para controlar o estado do código
codigo_congelado = False

def monitorar_botao():
    global codigo_congelado
    while True:
        if keyboard.is_pressed('p'):  # Monitora se a tecla 'p' foi pressionada
            codigo_congelado = not codigo_congelado
            if codigo_congelado:
                print("Código congelado!")
            else:
                print("Código liberado!")
            time.sleep(0.5)  # Pequena pausa para evitar múltiplas detecções da mesma tecla

# Função que representa o código principal que será congelado
def codigo_principal():
    while True:
        if not codigo_congelado:
            print("Código rodando...")
        time.sleep(4)  # Simula o tempo de execução do código

# Cria e inicia a thread que monitora o botão
thread_monitor = threading.Thread(target=monitorar_botao)
thread_monitor.daemon = True
thread_monitor.start()

# Executa o código principal
codigo_principal()
