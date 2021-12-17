valorcasa = 120_000
salario = 5_000
anospag = 10

prestmensal = valorcasa / (anospag * 12)
salariolimite = salario * 0.30

# print(prestmensal)
# print(salariolimite)

if prestmensal <= salariolimite:
    print('\nemprétimo AUTORIZADO!')
else:
    print('\nempréstimo NEGADO!')
