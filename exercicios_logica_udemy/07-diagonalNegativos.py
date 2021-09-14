quantRep = int(input("Qual a ordem da Matriz? "))

mat: [[int]] = [[0 for x in range(quantRep)] for x in range(quantRep)]

for i in range(0, quantRep):
    for j in range(0, quantRep):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

somaNeg = 0

print("Dados Digitados")
for i in range(0, quantRep):
    for j in range(0, quantRep):
        print(f"{mat[i][j]} ", end=' ')
        if mat[i][j] < 0:
            somaNeg += 1
    print()

print("Diagonal Principal: ")
for i in range(0, quantRep):
    for j in range(0, quantRep):
        if mat[i] == mat[j]:
            print(f"{mat[i][j]}", end=' ')

print(f"\nQuantidade de Negativos = {somaNeg}")
