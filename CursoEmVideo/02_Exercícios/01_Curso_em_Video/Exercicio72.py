# crie um programa que tenha uma "tupla" totalmente preenchida com uma contagem por extenso, de "zero" até "vinte"
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

while True:
    n = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
         'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')

    esc = int(input('digite um número: '))
    if 0 < esc <= 20:
        resp = n[esc - 1]
        print('vc digitou o número {}.'.format(resp))
    else:
        print('número errado!')
