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

dados = dict()
list_nome = list()

list_n_partidas = list()
list_n_gols = list()
while True:
    list_nome.append(str(input('nome do jogador: ')).title())
    list_n_partidas.append(int(input('quantas partidas: ')))
    # Necessário filtrar o list_n_partidas abaixo para ele pegar sempre o último valor, não somente o 0. O que resolveu foi o '-1'.
    for c in range(1, list_n_partidas[-1] + 1):
        list_n_gols.append(int(input(f'quantos GOLs fez na {c}ª partida: ')))
    perg = str(input('Deseja continuar? [N] '))
    if perg in 'Nn':
        break
dados['nome'] = list_nome[:]
dados['n_partidas'] = list_n_partidas[:]
dados['n_gols'] = list_n_gols[:]
# SEPARAR O CÓDIGO DE CADA JOGADOR
list_codigo = list()
for i, v in enumerate(dados['nome']):
    list_codigo.append(i)
dados['codigo'] = list_codigo[:]
# SEPARAR OS GOLS POR JOGADOR


print(dados)

# CONTINUAR NO TESTE.PY, COLOQUEI ALGUMAS NOTAS.
# PARA FAZER ISSO TENHO QUE FAZER UMA COMPARAÇÃO ENTRE DUAS CHAVES QUE É O 'NOME' E O 'N_PARTIDAS', POR ESSA ÚLTIMA CONSIGO SELECIONAR A QUANTIDADE DE GOLS QUE SERÃO PEGUES.
# TENHO ESSE OUTRO PROBLEMA AGORA, TENHO QUE SEPARAR OS GOLS QUE SÃO DO JOGADOR ESPECÍFICO, PARA NÃO MISTURAR...
# {'nome': ['Romario', 'Ronaldo'], 'n_partidas': [2, 3], 'n_gols': [3, 1, 3, 5, 1], 'codigo': [0, 1]}

