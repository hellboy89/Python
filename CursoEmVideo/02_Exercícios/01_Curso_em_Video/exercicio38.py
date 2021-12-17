n1 = int(input('digite um valor para comparação: '))
n2 = int(input('digite outro valor para comparação: '))

if n1 > n2:
    print('o valor {} é maior do que {}.'.format(n1, n2))
elif n1 < n2:
    print('o valor {} é menor do que {}.'.format(n1, n2))
elif n1 == n2:
    print('os valores são iguais')
