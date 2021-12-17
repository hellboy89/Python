"""
(OK) - Faça um "mini-sistema" que utilize o "interactive help" do python.
(OK) - O usuário vai digitar o "comando" e o "manual" vai aparecer. 
(BUG NA FUNÇÃO DO WHILE) - Quando o usuário digitar a palavra "FIM", o programa se "encerrará".
(OK) - Use "cores".
"""
print('\033c')
from time import sleep
# Foi feito dessa forma abaixo a parte das cores para facilitar no código, pois agora pode-se informar a posição por número por exemplo [2] para verde.
c = {'\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     }

# Abaixo é como é tratado as cores dos menus.
def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep[2]

# Abaixo como é tratado as cores dos títulos e também a faixa de efeitos com o mesmo tamanho do título
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo("SISTEMA DE AJUDA", 2)
    # Tudo que será informado aqui terá a saída nos comandos anteriores.
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
