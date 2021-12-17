valor = 780_000.00

p1 = (valor * 46) / 100
p2 = (valor * 32) / 100
p3 = valor - (p1 + p2)

print('o valor do primeiro ganhador é {}'.format(p1))
print('o valor do segundo ganhador é {}'.format(p2))
print('o valor do terceiro ganhador é {}'.format(p3))

print('soma de tudo é {}'.format(p1 + p2 + p3))
