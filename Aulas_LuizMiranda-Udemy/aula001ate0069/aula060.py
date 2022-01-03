# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

lista = [
    ["p1", 13],
    ["p2", 6],
    ["p3", 50],
    ["p4", 17]
]

def func(item):
    return item[1]

# ordenando valores de uma lista, do maior para o menor, utilizando a
# função "reverse=True", se tirar ela irá ficar do menor para o maior.

lista.sort(key=func, reverse=True)
print(lista)

