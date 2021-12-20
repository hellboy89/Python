# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

def func1(nome, idade, temPeso=False, peso=0):
    if temPeso == True:
        return f"seu nome é {nome} e tem {idade}, peso {peso}"

def func2(utilizar=False):
    if utilizar == True:
        peso = "140kg"
        enviaFunc1 = func1("Juan", 32, True, peso)
        return enviaFunc1
    else:
        print("não foi permitido")

def func3(ligacao=False):
    if ligacao == True:
        lista = []
        soma = 0
        for numero in range(1,5):
            lista.append(numero)
            enviando = func1("Juan", 32)
            return f"{enviando}"
        for v in lista:
            soma += v
        return soma
    else:
        print("tá falso hein")

valores1 = func1("Juan Cleber", 32)
print(valores1)

valores2 = func2(True)
print(valores2)

valores3 = func3(True)
print(valores3)
