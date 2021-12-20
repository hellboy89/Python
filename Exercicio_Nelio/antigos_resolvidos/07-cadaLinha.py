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

print("Maior Elemento de Cada Linha: ")
for i in range(0, quantRep):
    maior = mat[i][0]
    for j in range(0, quantRep):
        if mat[i][j] > maior:
            maior = mat[i][j]
    print(f"{maior}")

