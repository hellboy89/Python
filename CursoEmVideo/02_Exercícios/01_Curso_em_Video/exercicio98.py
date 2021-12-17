"""
(OK) - Faça um programa que tenha um "função" chamada "contador()".
(OK) - que receba 3 "parâmetros: início, fim e passo" e realize a contagem.
(OK) - Seu programa tem que realizar "três contagens" através da função criada:
(OK) - A) De 1 até 10, de 1 em 1
(OK) - B) De 10 até 0, de 2 em 2
(FIZ, MAS COM LIMITAÇÕES) - C) Uma contagem "personalizada".
"""

from time import sleep


def contador():
    print('-=' * 30)
    print(f'Contagem de 1 até 10 de 1 em 1: ')
    for c in range(1, 10+1):
        sleep(0.1)
        print(c, end=' ')
    print()
    print('-=' * 30)
    print(f'Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        sleep(0.1)
        print(c, end=' ')
    print()
    print('-=' * 30)
    print(f'Agora é sua vez de personalizar a contagem!')
    inicio = int(input('início: '))
    fim = int(input('fim: '))
    passo = int(input('passo: '))
    print('-=' * 30)
    print(
        f'A contagem de {inicio} até {fim} pulando de {passo} em {passo} é: ', end=' ')
    for c in range(inicio, fim, passo):
        sleep(0.2)
        print(c, end=' ')


contador()
print('\n')

# EXERCÍCIO NÃO ATENDE COMPLETAMENTE AO DO PROFESSOR, POIS HÁ UM PROBLEMA NA CONTAGEM, QUE NÃO CONTA DE TRÁS PARA FRENTE E NEM NÚMEROS NEGATIVOS.
# PRECISO FAZER UMA CONTAGEM DE DO MAIOR PARA O MENOR.
# ESTUDAR SOBRE A "DOCUMENTAÇÃO DO FOR", PARA APRENDER MAIS FUNÇÕES SOBRE CONTAGENS.
