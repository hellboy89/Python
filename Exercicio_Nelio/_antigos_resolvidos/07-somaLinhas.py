quantLinhas = int(input("Qual a quantidade de linhas da matriz? "))
quantColunas = int(input("Qual a quantidade de colunas da matriz? "))

mat: [[int]] = [[0 for x in range(quantColunas)] for x in range(quantLinhas)]
vetSoma: [float] = [0 for x in range(quantLinhas)]

for i in range(0, quantLinhas):
    print(f"Digite os elementos da {i + 1}a. linha: ")
    for j in range(0, quantColunas):
        mat[i][j] = float(input())

print("Dados Digitados: ")
for i in range(0, quantLinhas):
    for j in range(0, quantColunas):
        print(f"{mat[i][j]} ", end=' ')
    print()

for i in range(0, quantLinhas):
    vetSoma[i] = 0
    for j in range(0, quantColunas):
        vetSoma[i] = vetSoma[i] + mat[i][j]

print("Vetor Gerado: ")
for i in range(0, quantLinhas):
    print(f"{vetSoma[i]} ")
