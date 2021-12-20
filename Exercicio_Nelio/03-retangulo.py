# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

def retangulo(baseRet, alturaRet):
    from math import sqrt

    area = baseRet * alturaRet
    perimetro = (baseRet * 2) + (alturaRet * 2)
    diagonal = sqrt((baseRet ** 2) + (alturaRet ** 2))

    print(f"Area = {area:.4f}")
    print(f"Perimetro = {perimetro:.4f}")
    print(f"Diagonal = {diagonal:.4f}")

def verificaValores(baseRet, alturaRet):
    if baseRet.isdecimal() and alturaRet.isdecimal():
        baseRet = float(baseRet)
        alturaRet = float(alturaRet)
        retangulo(baseRet, alturaRet)
    else:
        while True:
            print("Valores não são números, tente novamente.")
            baseRet = input("Base do Retangulo: ")
            alturaRet = input("Altura do Retangulo: ")
            verificaValores(baseRet, alturaRet)


baseRet = input("Base do Retangulo: ")
alturaRet = input("Altura do Retangulo: ")

verificaValores(baseRet, alturaRet)
