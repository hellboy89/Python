print("Digite dois números: ")
valX = int(input())
valY = int(input())

if valX > valY:
    troca = valX
    valX = valY
    valY = troca

soma = 0
for i in range(valX + 1, valY):
    if i % 2 != 0:
        soma = soma + i

print(f"Soma dos Impares = {soma}")

