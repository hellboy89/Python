from math import sqrt

num = int(input('informe um número: '))

if num > 0:
    raiz = sqrt(num)
    print(' a raiz quadrada é {}'.format(raiz))
else:
    print('o número é inválido, digite outro!')
