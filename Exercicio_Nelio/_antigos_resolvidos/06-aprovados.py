quantRep = int(input("Quantos alunos serão digitados? "))

vetNome: [str] = [0 for x in range(quantRep)]
vetNota1: [float] = [0 for x in range(quantRep)]
vetNota2: [float] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno: ")
    vetNome[i] = input()
    vetNota1[i] = float(input())
    vetNota2[i] = float(input())

posicao = 0
print("Alunos aprovados: ")
for i in range(0, quantRep):
    if (vetNota1[i] + vetNota2[i]) / 2 >= 6.0:
        posicao = i
        print(f"{vetNome[posicao]}")

