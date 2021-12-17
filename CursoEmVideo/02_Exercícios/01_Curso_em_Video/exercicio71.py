# crie um programa que simule o funcionamento de um "caixa eletrônico". No início, pergunte ao usuário
# qual será o "valor a ser sacado" (número inteiro) e o programa vai informar quantas "cédulas" de cada
# valor serão entregues. OBS.: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

print('=' * 30)
print('{:^30}'.format('BANCO JUAN'))
print('=' * 30)
valor = int(input('que valor você quer sacar? R$ '))
total = valor
# abaixo a cédula de 50 reais será o maior valor.
ced = 50
# variável de baixo irá colocar o valor total de cédulas.
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('volte sempre o BANCO JUAN agradece')

"""
# A idéia lógica do programa é fazer o VALOR TOTAL das cédulas chegar a 0, então fazendo um While, até o total ser 0 é dar break é a solução.

TAGS:
- calculo cédulas
- centralizar formatação
- exemplo while e aninhamento
"""
