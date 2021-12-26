quantRep = int(input("Quantos números você vai digitar? "))

for i in range(0, quantRep):
    num = int(input("Digite um número: "))
    if num < 0 and num % 2 != 0:
        print("Impar Negativo")
    elif num == 0:
        print("Nulo")
    elif num > 0 and num % 2 != 0:
        print("Impar Positivo")
    elif num < 0 and num % 2 == 0:
        print("Par Negativo")

