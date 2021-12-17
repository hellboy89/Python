"""
(OK) - Crie um programa que gerencie o aproveitamento de um 'jogador de futebol'. O programa vai ler o
     'nome do jogador' e 'quantas partidas' ele jogou.
(OK) - Depois vai ler a 'quantidade de gols' feito em 'cada partida'.
(OK) - No final, tudo isso será guardado em um 'dicionário',
(OK) - Incluindo o 'total de gols' feitos durante o campeonato.
"""

dados = dict()
lista = list()

dados['nome'] = str(input('qual o nome do jogador: ')).title()
dados['quant_parti'] = int(input(f'qual a quantidade de partidas jogadas por {dados["nome"]}: '))
dados['soma_gols'] = 0

for c in range(1, dados['quant_parti'] + 1):
    lista.append(int(input(f'quantos gols fez na {c} partida: ')))
dados['gols_part'] = lista[:]
# CALCULAR A SOMA DOS GOLS
for i, v in enumerate(dados['gols_part']):
    dados['soma_gols'] += v
# =========================
print('-=' * 30)
print(dados)
print('-=' * 30)
print(f'O nome do jogador é: {dados["nome"]}')
print(f'O campo gols é: {dados["gols_part"]}')
print(f'O campo total foi: {dados["soma_gols"]}')
print('=-' * 30)
print(f'O jogador {dados["nome"]} jogou {dados["quant_parti"]} partidas.')
# APONTAR A QUANTIDADE DE GOLS PARA CADA PARTIDA.
for c in range(0, dados['quant_parti']):
    print(f'     => Na partida {c}, fez {dados["gols_part"][c]} gols.')
print(f'Somandos todos os gols foram {dados["soma_gols"]}.')
