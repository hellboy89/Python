"""
(OK) - Faça um programa que tenha uma "lista" chamada "números".
(OK) - e duas "funções" chamadas "sorteia()" e "somaPar()".
(OK) - A primeira função vai sortear "5 números" e vai colocá-los dentro da lista
(OK) - a segunda função vai mostrar a "soma" entre todos os "pares" sorteadas pela função anterior.
"""

from random import randint

numeros = list()
numeros_par = list()


def sorteia():
    for c in range(0, 5+1):
        sort_n = randint(0, 9)
        numeros.append(sort_n)
    print(f'Os 5 valores sorteados foram {numeros}.')


def somaPar():
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            numeros_par.append(v)
    print(f'os valores pares são: {numeros_par}')
    print(f'a soma dos números pares é {sum(numeros_par)}')


sorteia()
somaPar()

# ANTES TENHO QUE TESTAR A FUNÇÃO "SUM" QUE PODE SER ÚTIL.
# TENHO QUE ACHAR UMA FORMA DE SOMAR SOMENTE OS VALORES PARES
