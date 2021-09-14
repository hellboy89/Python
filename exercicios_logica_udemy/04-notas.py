nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

notaFinal = nota1 + nota2

print(f"Nota Final = {notaFinal:.1f}")

if notaFinal > 60.0:
    print("Aprovado")
else:
    print("Reprovado")
