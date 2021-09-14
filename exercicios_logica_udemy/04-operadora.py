quantMin = int(input("Digite a quantidade de minutos: "))
valorMin = 100.00

if quantMin <= 100:
    print(f"Valor a pagar: R$ 50.00")
elif quantMin >= 100:
    minutosExcedidos = (quantMin - 100) * 2
    total = 50 + minutosExcedidos
    print(f"Valor a pagar: R$ {total:.2f}")
