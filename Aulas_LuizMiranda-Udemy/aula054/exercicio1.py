# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

def saudacao(msg, nome):
    print(f"\n{msg}, {nome}\n")

def verificaDigito(msg, nome):
    if msg.isdigit() == False and msg.isdigit() == False:
        return True
    else:
        return False

while True:
    msg = input("Saudacao: ")
    nome = input("Nome: ")

    valor = verificaDigito(msg, nome)
    if valor == True:
        saudacao(msg, nome)
    else:
        print("valor invalido, tente novamente, mais tarde.")
        break

