# Comando abaixo limpa o terminal antes de executar o próximo código
import os
os.system('cls' if os.name == 'nt' else 'clear')

def hehe(teste):
    print(teste)

def valor():
    return "teste"

def testeNadaFazer(texto, valor):
    return f"estou fazendo {texto} e tenho {valor} anos"

def verdadeOuMentira(teste):
    return teste

def calculo(val1, val2, val3, val4):
    soma = val1 + val2 + val3 + val4
    print(soma)

calculo(10, 20, 30, 50)

