escTemp = input("Você vai digitar a temperatura em qual escala (C/F)? ").upper()

if escTemp == "F":
    tempFah = float(input("Digite a temperatura em Fahrenheit: "))
    tempCel = (5 / 9) * (tempFah - 32)
    print(f"Temperatura equivalente em Celsius: {tempCel:.2f}")
elif escTemp == "C":
    tempCel = float(input("Digite a temperatura em Celsius: "))
    tempFah = (tempCel * 1.80) + 32
    print(f"Temperatura equivalente em Fahrenheit: {tempFah:.2f}")
