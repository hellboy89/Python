quantRep = int(input("Qual a ordem da matriz? "))

mat: [int] = [[0 for x in range(quantRep)] for x in range(quantRep)]

for i in range(0, quantRep):
    for j in range(0, quantRep):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Dados Digitados: ")
for i in range(0, quantRep):
    for j in range(0, quantRep):
        print(f"{mat[i][j]}", end=' ')
    print()

somaAcimaDiag = 0

for i in range(2, quantRep):
    for j in range(2, quantRep):
        if mat[i][j] == mat[i][j]:
            somaAcimaDiag = somaAcimaDiag + mat[i][j]

print(f"Soma dos elementos acima da diagonal principal = {somaAcimaDiag}")
