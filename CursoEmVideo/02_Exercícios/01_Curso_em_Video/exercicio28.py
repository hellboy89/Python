import random

numero = int(input('Escolha um número: '))

rand = random.randrange(1, 5 + 1)

if numero == rand:
    print('número certo escolhido!')
else:
    print('número ERRADO!')

print('\nnúmero sorteado foi {}'.format(rand))
