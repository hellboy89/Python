"""
(OK) - Faça um programa que tenha uma 'função" chamada 'área()', 
(OK) - que receba as dimensões de um terreno retangular (largura e cumprmento)
(OK) - e mostre a 'área do terreno'.
"""


def area(larg, comp):
    a = larg * comp
    print(f'a área de um terrno {larg}x{comp} é de {a}m².')


# Programa principal
print('  Controle de Terrenos')
print('-' * 20)
# Aqui foi feito a troca de uns nomes de variável, para notar que dá para fazer de muitas formas o envio de valores para os DEFs.
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
