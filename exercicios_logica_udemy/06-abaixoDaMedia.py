quantRep = int(input("Quantos elementos vai ter o vetor? "))

vet: [float] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    vet[i] = float(input("Digite um número: "))

somaVetor = 0
contador = 0
for i in range(0, quantRep):
    somaVetor = somaVetor + vet[i]
    contador += 1

print(f"Media do vetor = {(somaVetor / contador):.3f}")

print(f"Elementos abaixo da média: ")
for i in range(0, quantRep):
    if (somaVetor / contador) > vet[i]:
        print(f"{vet[i]:.1f} ")



