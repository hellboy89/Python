codProd = int(input("Código do produto comprado: "))
quantComp = int(input("Quantidade comprada: "))

if codProd == 1:
    valPag = 5.00 * quantComp
elif codProd == 2:
    valPag = 3.50 * quantComp
elif codProd == 3:
    valPag = 4.80 * quantComp
elif codProd == 4:
    valPag = 8.90 * quantComp
elif codProd == 5:
    valPag = 7.32 * quantComp
else:
    print("Valor incorreto, tente novamente.")

print(f"Valor a pagar: R$ {valPag:.2f}")
