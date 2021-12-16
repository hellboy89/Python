# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

teste = ["Juan", "Cleber", "Faria", "Alves"]

for valor in teste:
    print(valor, end=" ")

print()

teste2 = ["Juan", "Cleber"]
teste2.insert(0, "J")

comeca_com_j = False

for valor in teste2:
    if valor.lower().startswith('j'):
        comeca_com_j = True


if comeca_com_j:
    print("Começa com J")
else:
    print("Não começa com J.")

print(f"Lista completa é: {teste2}")

