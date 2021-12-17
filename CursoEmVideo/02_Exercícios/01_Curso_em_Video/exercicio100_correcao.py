"""
(OK) - Faça um programa que tenha uma "lista" chamada "números".
(OK) - e duas "funções" chamadas "sorteia()" e "somaPar()".
(OK) - A primeira função vai sortear "5 números" e vai colocá-los dentro da lista
(OK) - a segunda função vai mostrar a "soma" entre todos os "pares" sorteadas pela função anterior.
"""

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.2)
    print('PRONTO')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)
