import os
import subprocess
import platform


def clear_layout():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    options = [
    "[1] Puxar CEP",
    "[2] Puxar IP",
    "[3] Validar CPF",
    "[4] Puxar informações do sistema",
    "[5] Consultar clima",
    "[6] Gerar senha aleatória",
    "[7] Calcular IMC",
    "[8] Converter moeda",
    "[9] Consultar horário",
    "[10] Sair"
]
    for option in options:
        print(option)
    
    option = input("Escolha uma opção: ")
    option = option
    
    while not option.isdigit() or int(option) < 1 or int(option) > 10:
        print("Escolha uma opção válida.")
        option = input("Escolha uma opção: ")
        
    option = int(option)
    match option:
        case 1:
            clear_layout()
            subprocess.run(['python3', 'python/cep.py'])
        case 10:
            clear_layout()
            exit()
        case _:
            ...
                    
                