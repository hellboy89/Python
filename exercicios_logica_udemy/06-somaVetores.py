quantRep = int(input("Quantos valores vai ter cada vetor? "))

vetA: [int] = [0 for x in range(quantRep)]
vetB: [int] = [0 for x in range(quantRep)]

print("Digite os valores de A: ")
for i in range(0, quantRep):
    vetA[i] = int(input())

print("Digite os valores de B: ")
for i in range(0, quantRep):
    vetB[i] = int(input())

print("Vetor Resultante: ")
for i in range(0, quantRep):
    print(f"{vetA[i] + vetB[i]}")


