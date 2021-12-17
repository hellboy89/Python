"""
(OK) - Crie um programa que vai ler "vários números"
(OK) - e colocar em uma "lista". Depois disso, mostre:
(OK) - a) "quantos números foram digitados.
(OK) - b) a lista de valores ordenada de forma "decrescente".
(DIFÍCIL, SOLUÇÃO PARECIA ÓBVIA.) - c) se o valor "5" foi digitado e está ou não na "lista".
"""
lista = []

while True:
    n = int(input('digite um número: '))
    lista.append(n)
    perg = str(input('deseja continuar [N]: ')).lower()
    if perg in 'Nn':
        break
print(lista)

print('foram digitados {} números.'.format(len(lista)))
lista.sort(reverse=True)
print('os valores ordenados de forma decrescente são: {}'.format(lista))
if 5 in lista:
    print('o valor 5 faz parte da lista.')
else:
    print('o valor 5 NÃO faz parte.')
