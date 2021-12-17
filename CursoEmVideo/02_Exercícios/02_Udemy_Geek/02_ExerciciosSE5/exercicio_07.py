num1 = int(input('informe um número: '))
num2 = int(input('informe um número: '))

if num1 > num2:
    print('o {} é maior do que o {}'.format(num1, num2))
elif num1 < num2:
    print('o {} é menor do que o {}'.format(num1, num2))
else:
    print('os números são iguais.')
