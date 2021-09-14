quantRep = int(input("Quantas pessoas serão digitadas? "))

vetAlt: [float] = [0 for x in range(quantRep)]
vetGen: [str] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    vetAlt[i] = float(input(f"Altura da {i + 1}a pessoa: "))
    vetGen[i] = input(f"Genero da {i + 1}a pessoa: ").upper()
    print()

menorAlt = vetAlt[0]
maiorAlt = vetAlt[0]
somaAltF = 0
contF = 0
contM = 0
print("Dados Pessoais: ")
for i in range(0, quantRep):
    print(f"{vetAlt[i]}", end='  ')
    print(f"{vetGen[i]}")
    if maiorAlt < vetAlt[i]:
        maiorAlt = vetAlt[i]
    if menorAlt > vetAlt[i]:
        menorAlt = vetAlt[i]
    if vetGen[i] == "F":
        somaAltF = somaAltF + vetAlt[i]
        contF += 1
    elif vetGen[i] == "M":
        contM += 1

print(f"\nMenor Altura = {menorAlt:.2f}")
print(f"Maior Altura = {maiorAlt:.2f}")
print(f"Media das alturas das mulheres = {(somaAltF / contF):.2f}")
print(f"Número de homens = {contM}")
