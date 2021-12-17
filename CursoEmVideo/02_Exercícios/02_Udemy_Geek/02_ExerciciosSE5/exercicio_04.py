import math

num = float(input('informe um número: '))

if num > 0:
    raizq = math.sqrt(num)
    print('o quadrado de {} é {}'.format(num, num ** 2))
    print('a raiz quadrada é {}'.format(raizq))
else:
    print('somente números positivos.')