# Crie um programa que vai gerar "cinco números aleatórios" e colocar em uma "tupla". Depois disso, mostre a
# "listagem de números" gerados e também indique o "menor" e o "maior" valor que estão na tupla.

from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('todos os valores foram {}.'.format(n))
print('o maior valor sorteado foi {}.'.format(max(n)))
print('o menor valor sorteado foi {}.'.format(min(n)))
