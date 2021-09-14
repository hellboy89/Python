quantRep = int(input("Quantas pessoas você vai digitar? "))

vetNome: [str] = [0 for x in range(quantRep)]
vetIdade: [int] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    print(f"Dados da {i + 1}a pessoa: ")
    vetNome[i] = input("Nome: ")
    vetIdade[i] = int(input("Idade: "))

maisVelho = vetIdade[0]
posicao = 0

print("Dados Digitados: ")
for i in range(0, quantRep):
    print(f"{vetNome[i]}", end=' ')
    print(f"{vetIdade[i]}")
    if vetIdade[i] > maisVelho:
        maisVelho = vetIdade[i]
        posicao = i

print(f"Pessoa mais velha: {vetNome[posicao]}")
