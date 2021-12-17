# Desenvolva um programa que leia "quatro valores" pelo "teclado" e guarde-os em uma "tupla". No final, mostre:
# a) quantas vezes apareceu o valor "9".
# b) em que posição foi digitado o primeiro valor "3".
# c) quais foram os números "pares".

n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
n3 = int(input('terceiro valor: '))
n4 = int(input('quarto valor: '))

tupla = (n1, n2, n3, n4)
# primeira questão.
print('o valor 9 apareceu {} vezes.'.format(tupla.count(9)))
# segunda questão.
if 3 in tupla:
    print('o valor 3 apareceu na {}ª posição'.format(tupla.index(3) + 1))
else:
    print('o valor 3 não apareceu em nenhuma posição')
# terceira questão.
print('os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
