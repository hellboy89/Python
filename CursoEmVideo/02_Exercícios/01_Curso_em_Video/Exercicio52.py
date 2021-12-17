num = int(input('digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1:35:43m', end='')
        tot = tot + 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('e por isso ele É PRIMO!')
else:
    print('e por isso ele NÃO É PRIMO!')
