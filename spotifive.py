import keyboard
import time
import threading
import pyautogui

# Variável para controlar se o clicker está ativado ou desativado
clicker_ativado = False

# Função para executar o click do mouse e pressionar a tecla F5
def clicker():
    while clicker_ativado:
        pyautogui.click()
        keyboard.press('F5')
        keyboard.release('F5')
        time.sleep(9)  # Intervalo de 3 segundos entre os cliques
SS
# Função para lidar com a ativação/desativação do clicker
def toggle_clicker():
    global clicker_ativado
    clicker_ativado = not clicker_ativado
    if clicker_ativado:
        print("Clicker ativado")
        # Inicia a thread do clicker
        clicker_thread = threading.Thread(target=clicker)
        clicker_thread.start()
    else:
        print("Clicker desativado")

# Função para lidar com os eventos de teclado
def keyboard_events(event):
    if event.event_type == 'down' and event.name == 'alt':
        # Verifica se a tecla Alt foi pressionada
        keyboard.hook(f5_press)
    elif event.event_type == 'up' and event.name == 'alt':
        # Verifica se a tecla Alt foi solta
        keyboard.unhook(f5_press)

def f5_press(event):
    if event.event_type == 'down' and event.name == '1':
        # Verifica se a tecla 1 foi pressionada enquanto a tecla Alt estava ativa
        toggle_clicker()

# Registra o manipulador de eventos de teclado
keyboard.hook(keyboard_events)

# Mantém o programa em execução
while True:
    pass
