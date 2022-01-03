# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

cont = []

for numero in range(10, 1, -1):
    cont.append(numero)

for n, valor in enumerate(cont):
    print(n, valor)

