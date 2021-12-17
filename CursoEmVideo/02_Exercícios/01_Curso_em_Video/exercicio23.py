# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = 78797

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
mm = numero // 10000 % 10

print('a unidade é {}'.format(u))
print('a dezena é {}'.format(d))
print('a centena é {}'.format(c))
print('o milhar é {}'.format(m))
print('o milhares é {}'.format(mm))
