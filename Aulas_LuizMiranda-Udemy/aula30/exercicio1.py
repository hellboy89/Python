# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")


def verificaNum(num):
    if num.isnumeric():
        num = int(num)
        # print(type(num))
        if num % 2 != 0:
            print(f"o {num} é IMPAR")
        else:
            print(f"o {num} é PAR")
    else:
        print("errado, não é um numero")


verificaNum(input("Digite um numero: "))

