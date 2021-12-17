"""
(OK) - Crie um programa que gerencie o aproveitamento de um 'jogador de futebol'. O programa vai ler o
     'nome do jogador' e 'quantas partidas' ele jogou.
(OK) - Depois vai ler a 'quantidade de gols' feito em 'cada partida'.
(OK) - No final, tudo isso será guardado em um 'dicionário',
(OK) - Incluindo o 'total de gols' feitos durante o campeonato.
"""

from typing import Pattern


jogador = dict()
partidas = list()
jogador['nome'] = str(input('nome do jogador: '))
tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'     Quantos gols na partida   {c}? ')))
jogador['gols'] = partidas[:]
# Esse operador SUM é interessante, pois com uma palavra foi possível somar as partidas, antes eu tinha feito com o FOR.
jogador['total'] = sum(partidas)
print('=-' * 30)
# Novamente com o ITEMS, foi possível fazer uma filtragem melhor da sáida.
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
