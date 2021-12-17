def terreno(larg, comp, valMetQuad):
    calcTerreno = larg * comp
    calcPreco = calcTerreno * valMetQuad

    print(f"Area do Terreno = {calcTerreno:.2f}")
    print(f"Preco do Terreno = {calcPreco:.2f}")

def confereValores(larg, comp, valMetQuad):
    while True:
        if larg.isnumeric() and comp.isnumeric() and valMetQuad.isnumeric():
            larg = float(larg)
            comp = float(comp)
            valMetQuad = float(valMetQuad)
            terreno(larg, comp, valMetQuad)
            break
        else:
            print("Não é um número, digite novamente.")
            break

larg = input("digite a largura: ")
comp = input("digite o comprimento: ")
valMetQuad = input("valor do metro quadrado: ")

confereValores(larg, comp, valMetQuad)

