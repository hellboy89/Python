salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000.00:
    salPorc = salario + (salario * 0.20)
    aumento = ((salario * 0.20) - salario) + salario
    porc = "20%"
elif 1000.00 <= salario <= 3000.00:
    salPorc = salario + (salario * 0.15)
    aumento = ((salario * 0.15) - salario) + salario
    porc = "15%"
elif 3001.00 <= salario <= 8000.00:
    salPorc = salario + (salario * 0.10)
    aumento = ((salario * 0.10) - salario) + salario
    porc = "10%"
elif salario > 8000.00:
    salPorc = salario + (salario * 0.5)
    aumento = ((salario * 0.5) - salario) + salario
    porc = "5%"

print(f"Novo Salario = R$ {salPorc:.2f}")
print(f"Aumento = R$ {aumento:.2f}")
print(f"Porcentagem = {porc}")
