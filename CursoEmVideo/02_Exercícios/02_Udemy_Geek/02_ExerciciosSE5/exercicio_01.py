n1 = int(input('informe um número: '))
n2 = int(input('informe um número: '))

if n1 > n2:
    print('o valor {} é maior do que {}'.format(n1, n2))
elif n1 < n2:
    print('o valor {} é menor do que {}'.format(n1, n2))
else:
    print('os valores são iguais.')
