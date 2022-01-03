# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

# os SETS no python, são parecidos com dicionários, a diferença é que,
# dicionários tem chaves e valores, SETS só tem valores, como abaixo.

s1 = {1, 2, 3, 4, 5}

print(type(s1))

# criando um set vazio e adicionando elementos.

s2 = set()
s2.add(1)
s2.add(10)
s2.add(20)

# removendo elementos.

s2.discard(10)

print(s2)
