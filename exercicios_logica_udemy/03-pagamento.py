nome = input("Nome: ")
valHora = float(input("Valor por hora: "))
horasTrab = float(input("Horas trabalhadas: "))

print(f"O pagamento para {nome} deve ser {(valHora * horasTrab):.2f}")
