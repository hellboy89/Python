"""
(OK) - Faça um programa que tenha uma 'função" chamada 'área()', 
(OK) - que receba as dimensões de um terreno retangular (largura e cumprmento)
(OK) - e mostre a 'área do terreno'.
"""

# Calcular área é: A = b x h
# A = Área, b = base, h = altura


def area(a, b):
    area = a * b
    print('  \nCALCULO DE TERRENO   ')
    print('=-' * 13)
    print(f'a altura é {a}')
    print(f'a largura é {b}')
    print(f'a area de um terreno {a:.1f}x{b:.1f} é de {area:.1f}m²\n')


area(float(input('informe o valor da altura: ')), float(input('informe o valor da base: ')))
