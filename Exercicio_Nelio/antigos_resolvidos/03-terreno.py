larg = float(input("Digite a largura do terreno: "))
comp = float(input("Digite o comprimento do terreno: "))
metro = float(input("Digite o valor do metro quadrado: "))

area = larg * comp
preco = area * metro

print(f"Area do Terreno = {area:.2f}")
print(f"Preço do Terreno = {preco:.2f}")
