precoUnit = float(input("Preço unitário do produto: "))
quantComp = int(input("Quantidade Comprada: "))
dinRec = float(input("Dinheiro recebido: "))

print(f"Troco = {(dinRec - (precoUnit * quantComp)):.2f}")
