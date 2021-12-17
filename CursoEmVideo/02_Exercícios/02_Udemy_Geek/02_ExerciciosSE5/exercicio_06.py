num1 = int(input('digite um número: '))
num2 = int(input('digite outro número: '))

if num1 > num2:
    print('o número {} é maior do que o {}.'.format(num1, num2))
    print('o número {} é maior em {}.'.format(num1, num1 - num2))
elif num1 < num2:
    print('o número {} é menor do que o {}'.format(num1, num2))
    print('o número {} é menor em {}.'.format(num1, num1 - num2))

