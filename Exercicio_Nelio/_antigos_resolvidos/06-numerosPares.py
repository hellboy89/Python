quantRep = int(input("Quantos números você vai digitar? "))

vet: [int] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    vet[i] = int(input("Digite um número: "))

contadorPar = 0
print("\nNúmeros Pares: ")
for i in range(0, quantRep):
    if vet[i] % 2 == 0:
        print(f"{vet[i]} ", end=' ')
        contadorPar += 1

print(f"\n\nQuantida de Pares = {contadorPar}")
