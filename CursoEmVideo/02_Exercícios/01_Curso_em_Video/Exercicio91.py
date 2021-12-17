"""
(OK) - Crie um programa onde '4 jogadores' joguem um 'dado' e tenha resultados 'aleatórios'.
(OK) - Guarde esses resultados em um 'dicionário'.
(FALTANDO) - No final, coloque esse dicionários em 'ordem',
(FALTANDO) - sabendo que o 'vencedor' tirou o 'maior número' no dado.
"""

from random import randint
from collections import OrderedDict

dado = dict()
lista = list()

for c in range(0, 4):
    dado['Número'] = randint(1, 6)
    cont = c
    dado['Jogador'] = cont + 1
    lista.append(dado.copy())
print(lista)
print()
print('>>>>> VALORES SORTEADOS <<<<<')
for i, v in enumerate(lista):
    print('O Jogador {}, tirou o número {}.'.format(v['Jogador'], v['Número']))
print('=-' * 30)
print('>>>>> RANKING DOS JOGADORES <<<<<')
for i, v in enumerate(lista):
    print('{}ª lugar: Jogador{} com {}'.format(i+1, v['Jogador'], v['Número']))

