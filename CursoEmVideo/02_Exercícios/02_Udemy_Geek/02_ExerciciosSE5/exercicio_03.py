import math

num = float(input('informe um número: '))

if num > 0:
    raizq = math.sqrt(num)
    print('a raiz quadrada é {}'.format(raizq))
else:
    print('o número ao quadrado é {}'.format(num ** 2))
