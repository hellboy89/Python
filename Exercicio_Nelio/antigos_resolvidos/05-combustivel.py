codComb = 0
alcool = 0
gasolina = 0
diesel = 0
while codComb != 4:
    codComb = float(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))
    if codComb == 1:
        alcool += 1
    elif codComb == 2:
        gasolina += 1
    elif codComb == 3:
        diesel += 1
    else:
        print("Valor incorreto, tente novamente.")

print("Muito Obrigado")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")



