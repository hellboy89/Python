# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")


def quantLetras(nome):
    quantLet = len(nome)

    if quantLet <= 4:
        print("Seu nome é curto.")
    elif quantLet > 4 and quantLet <= 6:
        print("Seu nome é normal.")
    elif quantLet > 6:
        print("Seu nome é muito grande")

quantLetras(input("Qual seu nome? "))

