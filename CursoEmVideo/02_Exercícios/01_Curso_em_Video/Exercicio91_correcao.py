"""
(OK) - Crie um programa onde '4 jogadores' joguem um 'dado' e tenha resultados 'aleatórios'.
(OK) - Guarde esses resultados em um 'dicionário'.
(OK) - No final, coloque esse dicionários em 'ordem',
(OK) - sabendo que o 'vencedor' tirou o 'maior número' no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),
        'jogador5': randint(1, 6),
        'jogador6': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
# Para ORDENADR um DICIONÁRIOS, é possível utilizando o itemgetter com abaixo.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'     {i + 1}ª lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
