# crie um programa que leia "vários números" inteirios pelo teclado. O programa só vai parar
# quando o usuário digitar o valor de "999", que é a "condição de parada". No final mostre
# "quantos números" foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0

while True:
    n = int(input('digite um número: '))
    if n == 999:
        print('\n parando função!')
        break
    soma += n

print('\na soma dos números é {}.\n'.format(soma))
