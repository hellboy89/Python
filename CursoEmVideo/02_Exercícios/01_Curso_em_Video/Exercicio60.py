# faça um programa que leia um "número" qualquer e mostre o seu "fatorial".
# ex: 5 != 5x4x3x2x1 = 120

n = int(input('digite um número para calcular seu fatorial: '))
c = n
f = 1
print('calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    # print abaixo é para mostrar o X se caso C for maior do que 1, para a saída do comando ficar certinha.
    print(' x ' if c > 1 else ' = ', end='')
    # nesse dado abaixo ele irá multiplicar o valor de f * c para incrementar na variável mais acima.
    f *= c
    c -= 1
# a saída do comando abaixo irá aparecer junto acima, devido ao parâmetro end=''.
print('{}'.format(f))
