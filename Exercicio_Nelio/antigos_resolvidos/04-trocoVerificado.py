precoUnit = float(input("Preço unitário do produto: "))
quantComp = int(input("Quantidade comprada: "))
dinheiroRec = float(input("Dinheiro recebido: "))

valorTot = precoUnit * quantComp

if valorTot > dinheiroRec:
    troco1 = (precoUnit * quantComp) - dinheiroRec
    print(f"Dinheiro Insuficiente. Faltam {troco1:.2f} Reais.")
else:
    troco2 = dinheiroRec - (precoUnit * quantComp)
    print(f"Troco = {troco2:.2f}")
