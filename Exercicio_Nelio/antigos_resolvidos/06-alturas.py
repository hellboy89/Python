quantRep = int(input("Quantas pessoas serão digitadas? "))

vetNome: [str] = [0 for x in range(quantRep)]
vetIdade: [int] = [0 for x in range(quantRep)]
vetAlt: [float] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    print(f"Dados da {i + 1}a pessoa: ")
    vetNome[i] = str(input("Nome: "))
    vetIdade[i] = int(input("Idade: "))
    vetAlt[i] = float(input("Altura: "))

somaAlt = 0
contador = 0
contadorMenos16 = 0
idadeMenos16 = 0
idadeSoma = 0
print("Dados Digitados: ")
for i in range(0, quantRep):
    print(f"{vetNome[i]}", end=' ')
    print(f"{vetIdade[i]}", end=' ')
    print(f"{vetAlt[i]}", end=' ')
    print()
    somaAlt = somaAlt + vetAlt[i]
    contador += 1
    idadeSoma = idadeSoma + vetIdade[i]
    if vetIdade[i] < 16:
        idadeMenos16 = idadeMenos16 + vetIdade[i]
        contadorMenos16 += 1

porcMenos16 = contadorMenos16 / contador * 100

print(f"\nAltura média: {(somaAlt / contador):.2f}")
print(f"Pessoas com menos de 16 anos: {porcMenos16:.1f}%")

for i in range(0, quantRep):
    if vetIdade[i] < 16:
        print(f"{vetNome[i]}")

