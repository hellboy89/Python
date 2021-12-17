"""
=================================EXERCICIO-93===========================================
(OK) - Crie um programa que gerencie o aproveitamento de um 'jogador de futebol'. O programa vai ler o
     'nome do jogador' e 'quantas partidas' ele jogou.
(OK) - Depois vai ler a 'quantidade de gols' feito em 'cada partida'.
(OK) - No final, tudo isso será guardado em um 'dicionário',
(OK) - Incluindo o 'total de gols' feitos durante o campeonato.
===================================EXERCICIO-95=========================================
() - Aprimore o 'desafio93' para que ele funcione com 'vários jogadores',
() - Incluindo um sistema de visualização de 'detalhes do aproveitamento' de cada jogador.
============================================================================
() - Necessário criar uma CHAVE de Código por jogador, que começa do 0 no dicionário. Que será usado posteriormente para a ferramenta de busca.
"""

time = list()
jogador = dict()
partidas = list()
while True:
    # O clear também pode ser usado para limpar dicionário.
    jogador.clear()
    jogador['nome'] = str(input('nome do jogador: '))
    tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
    # Testar o funcionamento dele também com listas.
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'     Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('erro! responda apenas S ou N.')
    if resp == 'N':
        break
print('=-' * 30)
print('cod ', end='')
# Foi pego só a chave utilizando o KEYS, para ele poder mostrar o cod, nome, gols e total.
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
# Muitos FOR dentro de FOR.
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    # Aqui ele pegou só os valores para poder mostrar na segunda coluna do resultado.
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
# A PARTE DE BAIXO É PARA MOSTRAR OS DADOS NA TELA, DE CIMA É SÓ A COLETA.
while True:
    busca = int(input('mostrar dados de qual jogador? (999 PARA PARAR) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'erro! não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
