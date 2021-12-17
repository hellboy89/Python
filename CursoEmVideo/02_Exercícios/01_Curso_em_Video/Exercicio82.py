"""
(OK) - Crie um programa que vai ler "vários números".
(OK) - E colocar em uma "lista". Depois disso,
(OK) - Crie "duas listas extras" que vão conter apenas os valores "pares" e os valores "impares" digitados.
(OK) - Ao final, mostre o conteúdo das "três listas" geradas.
"""

lista = []
listapar = []
listaimp = []

while True:
    n = int(input('digite um número: '))
    if n % 2 == 0:
        listapar.append(n)
        lista.append(n)
    if n % 2 == 1:
        listaimp.append(n)
        lista.append(n)
    perg = str(input('quer continuar [N]: ')).lower().strip()[0]
    if perg in 'Nn':
        break

lista.sort()
listapar.sort()
listaimp.sort()
print('todos os números da lista são {}.'.format(lista))
print('os números pares são {}.'.format(listapar))
print('os números impares são {}.'.format(listaimp))
