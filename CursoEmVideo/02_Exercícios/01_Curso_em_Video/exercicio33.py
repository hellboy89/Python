a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
c = int(input('digite o terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c

print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))
