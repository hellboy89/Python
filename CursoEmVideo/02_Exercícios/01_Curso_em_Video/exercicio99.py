"""
(OK) - Faça um programa que tenha uma "função" chamada "maior()",
(OK) - que receba vários "parâmetros" com valores inteiros.
(OK) - Seu programa tem que analisar todos os valores e dizer qual deles é o "maior".
"""

from random import randint

lista1 = list()
lista2 = list()
lista3 = list()
lista4 = list()
lista5 = list()
def maior():
    print('-=' * 30)
    print(f'ANALISANDO VALORES...')
    print('-=' * 30)
    q_valores = randint(0,9)
    for i in range(0, q_valores):
        n_rand = randint(0, 9)
        lista1.append(n_rand)
    print(lista1, end=' ')
    print(f'O maior valor é {max(lista1)}')
    print('-=' * 30)
    for i in range(0, q_valores):
        n_rand = randint(0, 9)
        lista2.append(n_rand)
    print(lista2, end=' ')
    print(f'O maior valor é {max(lista2)}')
    print('-=' * 30)
    for i in range(0, q_valores):
        n_rand = randint(0, 9)
        lista3.append(n_rand)
    print(lista3, end=' ')
    print(f'O maior valor é {max(lista3)}')
    print('-=' * 30)
    for i in range(0, q_valores):
        n_rand = randint(0, 9)
        lista4.append(n_rand)
    print(lista4, end=' ')
    print(f'O maior valor é {max(lista4)}')
    print('-=' * 30)
    for i in range(0, q_valores):
        n_rand = randint(0, 9)
        lista5.append(n_rand)
    print(lista5, end=' ')
    print(f'O maior valor é {max(lista5)}')
    print('-=' * 30)

maior()

# Tenho que gerar valores randômicos dentro de uma lista onde será feito uma comparação do maior e menor.