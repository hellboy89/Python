"""
(OK) - Faça um programa que tenha uma "função" chamada "ficha()",
(OK) - que receba dois "parâmetros opcionais": o "nome" de um jogador e quantos "gols" ele marcou.
(OK) - O programa deverá ser capaz de mostrar a "ficha do jogador", mesmo que algum dado não tenha sido informado corretamente.
"""
print('\033c')


def ficha(nome=0, n_gols=0):
    if nome == '':
        print(f'O jogador <desconhecido> fez {n_gols} gols.')
    else:
        print(f'O jogador {nome} fez {n_gols} gols.')


# Entrada de dados
ficha(str(input('nome: ')).title(), int(input('quantos gols: '))) 


print()

# COMO POR EXEMPLO SE EU NÃO INFORMAR O NOME DO JOGADOR, ELE TERÁ O VALOR "<DESCONHECIDO>"
# PARA ALTERAR UM VALOR DE UMA VARIÁVEL DENTRO DO DEF, TALVEZ EU TENHA QUE TRANSFORMAR ELA EM UMA VARIÁVEL "GLOBAL"
