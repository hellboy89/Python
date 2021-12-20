# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

def func0(*valores):
    soma = 0
    for numeros in valores:
        soma += numeros
    return soma

def func1(*valores):
    lista = []
    for v in valores:
        if v >= 0:
            lista.append(v)
    envia0 = func0(lista)
    return envia0

def func2(*valores):
    return valores

envia1 = func1(10, 20, 30, 40)
print(f"valores func1: {envia1}")

envia2 = func2(11, 21, 31, 41)
print(f"valores func2: {envia2}")

