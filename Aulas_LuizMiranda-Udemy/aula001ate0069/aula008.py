# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

nome = "Juan Cleber"
idade = int(input("idade: "))
anoAtual = 2021
anoNasc = anoAtual - idade
peso = int(input("peso: "))
altura = float(input("altura: "))

imc = (peso / (altura * altura))

print(f"O seu IMC é {imc:.2f}")

print(imc.isdigit())

