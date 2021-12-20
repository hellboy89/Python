# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")


def saudacao(horas):
    if horas.isnumeric():
        horas = int(horas)
        if horas >= 0 and horas <= 11:
            print("bom dia")
        elif horas >= 12 and horas <= 18:
            print("boa tarde")
        elif horas >= 18 and horas < 24:
            print("boa noite")
        else:
            print("deu ruim")
    else:
        print("não é um numero, tente novamente.")

saudacao(input("que horas são: "))
