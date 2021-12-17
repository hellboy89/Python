"""
(OK) - Crie um programa que tenha a "função leiaInt()",
(OK) - que vai funcionar de forma semelhante a função "input()" do python.
(OK) - só que fazendo "validação" para aceitar apenas um valor numérico.
EX: n = leiaInt('digite um n')
"""

print('\033c')


def leiaInt(valor):
    if valor[0] in 'ABCDEFGHIJLMNOPQRSTUVXZWYÇ':
        print('\033[1;31mERRO, digite um número inteiro.\033[m')
    else:
        print(f'vc digitou o valor \033[1;34m{valor}\033[m')

leiaInt(input('digite um valor: ').capitalize())

print()
