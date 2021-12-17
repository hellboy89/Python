"""

for c in range(10, 1, -1):
    print(c, end=' ')

# CONTAR DE TRÁS PRA FRENTE.

============================================================================

inicio = int(input('início: '))
fim = int(input('fim: '))
passo = int(input('passo: '))

for c in range(inicio, fim, passo):
    print(c, end=' ')

============================================================================

inicio = 90
fim = 40
passo = 10
for i in range(inicio, fim, -passo):
    print(i)

============================================================================

from random import randint

lista = list()


for i in range(0, 9):
    n_rand = randint(0, 9)
    lista.append(n_rand)


print(n_rand)
print()
print(lista)
print()
# Abaixo para filtrar o maior valor da lista.
print(max(lista))

# Agora preciso filtrar qual dos valores é o maior!
# Então para colocar vários valores aleatório dentro de uma lista, tenho que colocar tudo dentro de um for.
# Preciso colocar vários valores diferentes dentro de uma lista, utilizando o randint

============================================================================

from random import randint

lista = list()
lista_par = list()

for c in range(0, 10):
    rand = randint(0, 10)
    lista.append(rand)
print(lista)
print('\n\n')

for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
print(lista_par)
print(f'a soma dos valores pares é {sum(lista_par)}')


# A função SUM, funciona basicamente como acima, serve também para somar todos os valores de uma lista.

"""

teste = (input('digite um valor: '))
print(teste)