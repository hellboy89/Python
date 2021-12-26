quantRep = int(input("Serão digitados dados de quantos produtos? "))

vetNome: [str] = [0 for x in range(quantRep)]
vetPrecComp: [float] = [0 for x in range(quantRep)]
vetPrecVend: [float] = [0 for x in range(quantRep)]
porcLucros: [float] = [0 for x in range(quantRep)]

for i in range(0, quantRep):
    print(f"Produto {i + 1}: ")
    vetNome[i] = input("Nome: ")
    vetPrecComp[i] = float(input("Preço de compra: "))
    vetPrecVend[i] = float(input("Preço de venda: "))

valTotCompra = 0
valTotVenda = 0

print("Dados digitados: ")
for i in range(0, quantRep):
    print(f"{vetNome[i]}", end=' ')
    print(f"{vetPrecComp[i]}", end=' ')
    print(f"{vetPrecVend[i]}")
    valTotCompra = valTotCompra + vetPrecComp[i]
    valTotVenda = valTotVenda + vetPrecVend[i]
    porcLucros[i] = (vetPrecVend[i] - vetPrecComp[i]) / vetPrecComp[i] * 100.0

lucAbaixo10 = 0
lucEnt10e20 = 0
lucAcima20 = 0

for i in range(quantRep):
    if porcLucros[i] < 10.0:
        lucAbaixo10 += 1
    elif porcLucros[i] < 20.0:
        lucEnt10e20 += 1
    else:
        lucAcima20 += 1

print("\nRELATÓRIOS: ")
print(f"Lucro abaixo de 10%: {lucAbaixo10}")
print(f"Lucro entre 10% e 20%: {lucEnt10e20}")
print(f"Lucro acima de 20%: {lucAcima20}")
print(f"Valor total de compra: {valTotCompra:.2f}")
print(f"Valor total de venda: {valTotVenda:.2f}")
print(f"Lucro total: {(valTotVenda - valTotCompra):.2f}")
