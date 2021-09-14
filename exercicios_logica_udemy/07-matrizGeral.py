from math import pow

quantRep = int(input("Qual a ordem da matriz? "))

mat: [float] = [[0 for x in range(quantRep)] for x in range(quantRep)]

for i in range(0, quantRep):
    for j in range(0, quantRep):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: "))

somaPositivos = 0

print("Dados Digitados: ")
for i in range(0, quantRep):
    for j in range(0, quantRep):
        print(f"{mat[i][j]:.1f}", end=' ')
        if mat[i][j] > 0:
            somaPositivos = somaPositivos + mat[i][j]
    print()

print(f"\nSoma dos Positivos: {somaPositivos:.1f}")

escLinha = int(float(input("Escolha uma linha: ")))
print("Linha escolhida: ")
for i in range(0, quantRep):
    print(f"{mat[escLinha][i]}", end=' ')

escColuna = int(input(f"\nEscolha uma coluna: "))
print("Coluna escolhida: ")
for i in range(0, quantRep):
    print(f"{mat[i][escColuna]:.1f}", end=' ')

print(f"\nDiagonal Principal: ")
for i in range(0, quantRep):
    print(f"{mat[i][i]:.1f}", end=' ')

for i in range(0, quantRep):
    for j in range(0, quantRep):
        if mat[i][j] < 0:
            mat[i][j] = pow(mat[i][j], 2);

print("\n\nMatriz Alterada: ")

for i in range(0, quantRep):
    for j in range(0, quantRep):
        print(f"{mat[i][j]:.1f}", end=' ')
    print()



