quantLinhas = int(input("Quantas linhas vai ter cada matriz? "))
quantColunas = int(input("Quantas colunas vai ter cada matriz? "))

matA: [int] = [[0 for x in range(quantColunas)] for x in range(quantLinhas)]
matB: [int] = [[0 for x in range(quantColunas)] for x in range(quantLinhas)]

print("Digite os valores da matriz A: ")
for i in range(0, quantLinhas):
    for j in range(0, quantColunas):
        matA[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Digite os valores da matriz B: ")
for i in range(0, quantLinhas):
    for j in range(0, quantColunas):
        matB[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Matriz Soma: ")
for i in range(0, quantLinhas):
    for j in range(0, quantColunas):
        print(f"{matA[i][j] + matB[i][j]}", end=' ')
    print()
