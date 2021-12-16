# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

cont = 0

# possível utilizar o break para sair da repetição.
# também possível utilizar o "continue" para iniciar novamente a repetição.

cont = 0

while True:
    cont += 1
    continuar = input("quer continuar? ")

    if continuar != "s":
        cont -= 1
        print(f"contador total é {cont}")
        break

print("\nfim do while")
