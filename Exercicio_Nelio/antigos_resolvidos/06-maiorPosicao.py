quantRep = int(input("Quantos números você vai digitar? "))

vet: [float] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    vet[i] = float(input("Digite um número: "))

maior = vet[0]
posicao = 0

for i in range(0, quantRep):
    if maior < vet[i]:
        maior = vet[i]
        posicao = i

print(f"\nMaior Valor = {maior:.2f}")
print(f"Posição do maior valor = {posicao}")


