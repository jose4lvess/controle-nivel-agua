from colorama import Fore, Style, init
import time
import os

init(autoreset=True)

# Lista de níveis
niveis = [
    ("Muito baixo (crítico)", Fore.RED),
    ("Baixo", Fore.YELLOW),
    ("Médio", Fore.GREEN),
    ("Alto", Fore.CYAN),
    ("Muito alto (alerta)", Fore.BLUE)
]

# Função para limpar o terminal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função que define o nível com base na porcentagem
def classificar_nivel(porcentagem):
    if porcentagem <= 20:
        return 0
    elif porcentagem <= 40:
        return 1
    elif porcentagem <= 60:
        return 2
    elif porcentagem <= 80:
        return 3
    else:
        return 4

# Função para desenhar barra de nível
def barra_nivel(porcentagem):
    total = 20
    preenchido = int((porcentagem / 100) * total)
    return "[" + "█" * preenchido + "-" * (total - preenchido) + "]"

# Simulação
porcentagem = 10
subindo = True

while True:
    limpar_tela()

    nivel_index = classificar_nivel(porcentagem)
    descricao, cor = niveis[nivel_index]

    print("=== SISTEMA DE MONITORAMENTO DE ÁGUA ===\n")

    print(f"Nível do Reservatório: {cor}{descricao}")
    print(f"Volume: {porcentagem}%")
    print(barra_nivel(porcentagem))

    # Alertas
    if nivel_index == 0:
        print(Fore.RED + "\n⚠️ ALERTA CRÍTICO: nível muito baixo!")
    elif nivel_index == 4:
        print(Fore.BLUE + "\n⚠️ ALERTA: reservatório quase cheio!")

    # Simulação de subida e descida
    if subindo:
        porcentagem += 5
        if porcentagem >= 100:
            subindo = False
    else:
        porcentagem -= 5
        if porcentagem <= 0:
            subindo = True

    time.sleep(1)

# (Nunca chega aqui, mas mantém boa prática)
print(Style.RESET_ALL)
