quantLinhas = int(input("Qual a quantidade de linhas da matriz? "))
quantColunas = int(input("Qual a quantidade de colunas da matriz? "))

mat: [int] = [[0 for x in range(quantColunas)] for x in range(quantLinhas)]

for i in range(0, quantLinhas):
    for j in range(0, quantColunas):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Dados Digitados: ")
for i in range(0, quantLinhas):
    for j in range(0, quantColunas):
        print(f"{mat[i][j]}", end=' ')
    print()

print("\nValores Negativos: ")
for i in range(0, quantLinhas):
    for j in range(0, quantColunas):
        if mat[i][j] < 0:
            print(f"{mat[i][j]} ")

