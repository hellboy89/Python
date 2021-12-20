# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

def soma(num1=0, num2=0, num3=0):
    soma = num1 + num2 + num3
    return soma

def verificaValores(num1, num2, num3):
    if num1.isdecimal() and num2.isdecimal() and num3.isdecimal():
        return True
    else:
        return False

while True:
    num1 = input("valor1: ")
    num2 = input("valor2: ")
    num3 = input("valor3: ")

    verifica = verificaValores(num1, num2, num3)

    if verifica == True:
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        somaLogo = soma(num1, num2, num3)
        print(somaLogo)
    else:
        print(f"Digite somente números!")
        break
