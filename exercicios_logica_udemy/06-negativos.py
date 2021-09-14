quantRep = int(input("Quantos números você vai digitar: "))

vet: [float] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    vet[i] = int(input("Digite um número: "))

print("Números Digitados: ")
for i in range(0, quantRep):
    if vet[i] < 0:
        print(f"{vet[i]}")


