base = int(input('''Deseja converter para:
Escreva 1 para binário.
Escreva 2 para octal.
Escreve 3 para hexadecima. \n'''))

if base == 1:
    num = int(input('digite um número: '))
    print('O número {} em binário ficaria {}.'.format(num, bin(num)[2:]))
elif base == 2:
    num = int(input('digite um número: '))
    print('O número {} em octal ficaria {}.'.format(num, oct(num)[2:]))
elif base == 3:
    num = int(input('digite um número: '))
    print('o número {} em hexadecimal ficaria {}.'.format(num, hex(num)[2:]))
else:
    print('número incorreto, TENTE NOVAMENTE!')
