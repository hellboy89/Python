quantCasos = int(input("Quantos casos de teste serão digitados? "))

quantCoelhos = 0
quantRatos = 0
quantSapos = 0
totalCob = 0

for i in range(0, quantCasos):
    quantCob = int(input("Quantidade de cobaias: "))
    tipoCob = input("Tipo de Cobaia: ").upper()
    totalCob = totalCob + quantCob

    if tipoCob == "C":
        quantCoelhos = quantCoelhos + quantCob
    elif tipoCob == "R":
        quantRatos = quantRatos + quantCob
    elif tipoCob == "S":
        quantSapos = quantSapos + quantCob

porcCoelhos = quantCoelhos / totalCob * 100
porcRatos = quantRatos / totalCob * 100
porcSapos = quantSapos / totalCob * 100

print("Relatorio Final: ")
print(f"Total: {totalCob}")
print(f"Total de Coelhos: {quantCoelhos}")
print(f"Total de Ratos: {quantRatos}")
print(f"Total de Sapos: {quantSapos}")
print(f"Percentual de Coelhos: {porcCoelhos:.2f}")
print(f"Percentual de Ratos: {porcRatos:.2f}")
print(f"Percentual de Sapos: {porcSapos:.2f}")
