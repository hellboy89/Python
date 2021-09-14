quantRep = int(input("Quantos números você vai digitar: "))

vet: [float] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    vet[i] = float(input("Digite um número: "))

soma = 0
contagem = 0
print("Valores = ", end='')
for i in range(0, quantRep):
    print(f"{vet[i]:.1f}", end='  ')
    soma = soma + vet[i]
    contagem += 1

print(f"\nSoma = {soma:.2f}")
print(f"Media = {(soma / contagem):.2f}")

