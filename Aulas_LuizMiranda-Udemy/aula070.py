# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

import sys

# Geradores, Iteradores e Iteráveis em Python

lista = [0, 1, 2, 3, 4, 5]

lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__'))

lista2 = list(range(10))

# esse comando abaixo mostra o consumo em memória da lista, que no caso
# retornou 136 bits.

print(sys.getsizeof(lista2))

# se aumentar o tamanho da lista, aumenta a quantidade de bits.

lista3 = list(range(1000))

print(sys.getsizeof(lista3))





