from time import sleep
print('=='*10)
n = int(input('escolha um número para fazermos a tabuada: '))
print('=='*10)
if n >= 0 and n <= 10:
    for c in range(0, 10 + 1):
        sleep(0.2)
        print('{} x {} = {}'.format(n, c, n * c))
else:
    print('número incorreto, tente novamente')
