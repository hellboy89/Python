# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

def percentual(valor=0, percente=100):
    calc = ((valor * percente) / 100) + valor
    return calc

valor = int(input("qual valor: "))
percent = int(input("qual percentual: "))

calc = percentual(valor, percent)

print(f"valor: {calc}1")
