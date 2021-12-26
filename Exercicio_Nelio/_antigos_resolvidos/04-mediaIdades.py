print("Digite as idades: ")

num = 1
somaNum = 0
contador = 0

while num > 0:
    num = int(input())
    if num > 0:
        somaNum = somaNum + num
        contador += 1

if contador == 0:
    print("Impossível Calcular")
else:
    print(f"Media = {(somaNum / contador):.2f}")
