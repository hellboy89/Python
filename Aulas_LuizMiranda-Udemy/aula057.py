# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

valor = 10

# é possível converter uma variável local em global, fazendo como abaixo
# definindo o valor o tipo global separadamente.
# mas não é uma pratica muito comum.

def func():
    global valor
    valor = 20
    print(valor)

func()

print(valor)
