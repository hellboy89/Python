"""
(OK) - Crie um programa que tenha uma "função" chamada "voto()"
(OK) - que recebe como "parâmetro" o "ano de nascimento" de uma pessoa,
(OK) - "retornando" um valor "literal"
(OK) - Indicando se uma pessoa tem voto "NEGADO, OPCIONAL ou OBRIGATÓRIO" nas eleições.
"""
from datetime import date, datetime
print('\033c')


def voto(nasc, ano_atual):
    idade = ano_atual - nasc
    if idade < 18:
        print(f'vc tem {idade} anos, voto negado!')
    elif idade > 18 and idade < 65:
        print(f'vc tem {idade} anos, voto obrigatório!')
    else:
        print(f'vc tem {idade} anos, voto opcional!')
    return idade


print('-=' * 40)
# Entrada de dados
voto(int(input('informe a sua data de nascimento: ')),
     datetime.now().year)


print()
