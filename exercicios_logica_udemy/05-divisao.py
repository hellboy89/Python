quantRep = int(input("Quantos casos você vai digitar? "))

for i in range(0, quantRep):
    numerador = float(input("Entre com o numerador: "))
    denominador = float(input("Entre com o denominador: "))

    if denominador == 0:
        print("Divisão Impossível")
    else:
        resultado = numerador / denominador
        print(f"Divisão = {resultado:.2f}")


