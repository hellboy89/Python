"""
# Referência abaixo:
# https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado/learn/lecture/11892816#overview

# Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens com a diferença de serem DINÂMICO e poderem colocar QUALQUER tipo de dado.

# Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro poderá ter no máximo 5 valores.

# Já em python:

# - Dinâmico: Não possui tamanho fixo; podemos criar a lista e simplesmente ir adicionando elementos;
#    Não há limite de tamanho da lista, o limite é apenas o uso e armazenamento da memória RAM.

# - QUALQUER TIPO DE DADO: Não possuem tipo de dados fixo; Ou seja, podemos colocar qualquer tipo de dados;

As Listas em Python são representados por colchetes: []

============================================================================

"""

# Então qualquer valor que esteja entre colchetes [], é considerado uma lista.

teste = [1, 2, 5, 4, 2]
teste2 = ['g', 'e', 'e', 'k', ' ', 'J', 'u', 'a', 'n']
teste3 = []
teste4 = list(range(1, 11))
# Abaixo terá o mesmo resultado que o "teste2".
teste5 = list('Geek Juan')

print(teste)
print(teste2)
print(teste4)
print(teste5)
print(type(teste))

# Também há uma forma de checar se determinado valor está continudo numa lista.
# Utilizando condicionais é possível realizar essa checagem.
num = 18
if num in teste4:
    print(f'Encontrei o {num}.')
else:
    print(f'NÃO encontrei o {num}.')

if 'Juan' in teste5:
    print('tem Juan na lista.')
else:
    print('Não encontrei o Juan')

# Com esse comando abaixo executado no terminal do python, é possível ter uma série de opções que mostra as funções que posso utilizar na variável teste5.
dir(teste5)
# Pois iremos trabalhar com algumas dessas funções motradas na saída abaixo.
# SAÍDA
"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__
', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__n
ew__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'c
lear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""
