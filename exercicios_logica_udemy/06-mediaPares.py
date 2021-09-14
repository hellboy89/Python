quantRep = int(input("Quantos elementos vai ter o vetor? "))

vet: [int] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    vet[i] = int(input("Digite um número: "))

somaPares = 0
contPares = 0
for i in range(0, quantRep):
    if vet[i] % 2 == 0:
        somaPares = somaPares + vet[i]
        contPares += 1

if contPares > 0:
    print(f"Media dos Pares = {(somaPares / contPares):.1f}")
else:
    print("Nenhum número par")



