# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

# teste1 = 10 / 10
# teste2 = 10 / 102

# print(type(teste1),teste1)
# print(type(teste2),teste2)

# Para saber se o resultado é inteiro ou decimal, basta utilizar o recurso
# "is_integer()", como abaixo.
# saber = teste2.is_integer()
# print(saber)


def funcao(num):
    if num % 3 == 0 and num % 5 == 0:
        return "buzzfizz"
    elif num % 2 == 0:
        return "buzz"
    elif num % 5 == 0:
        return "fizz"
    else:
        return num

valor = int(input("Digite um valor: "))
testando = funcao(valor)
print(testando)
