# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

num1 = input("digite um numero: ")
num2 = input("digite um numero: ")

# tratamento de erros como abaixo, se caso se caso as variáveis 
# no try retornarem algum erro, irá para o bloco except.

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print("erro")


