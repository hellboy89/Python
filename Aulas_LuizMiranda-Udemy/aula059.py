# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

# ==========> EXEMPLO 1

def ola_mundo():
    return 'Ola mundo'

def mestre(funcao):
    return funcao()

# com o valor abaixo, eu jogo o valor que está dentro de "ola_mundo",
# para dentro da função mestre.

executando = mestre(ola_mundo)
print(executando)

# ==========> EXEMPLO 2

def valor1(valor):
    return f"o valor informado é {valor}"

def soma(funcao):
    return 10

executando2 = soma(valor1)
print(executando2)

# ==========> EXEMPLO 3

def valor2(valor):
    print("seu nome é {nome}")

def nome(funcao):
    return "Juan Cleber"

executando3 = nome(valor2)
print(executando3)

# ==========> EXEMPLO 4

def mestre(funcao, *args, **kargs):
    return funcao(*args, **kargs)

def fala_oi(nome):
    return f"Oi {nome}"

def saudacao(nome, saudacao):
    return f"{saudacao} {nome}"

executando4 = mestre(fala_oi, "Juan")
print(executando4)
executando5 = mestre(saudacao, "Juan", saudacao="Boa noite!")
print(executando5)

# ==========> EXEMPLO 5

def mestre2(funcao, *args, **kargs):
    return funcao(*args, **kargs)

def soma_valores(*soma, **kargs):
    contSoma = 0
    for v in soma:
        contSoma += v
    return contSoma

executando6 = mestre2(soma_valores, 10, 10, 20)
executando7 = mestre2(soma_valores, 10, 20, 30, 40, 50, teste = 80)
print(executando6)
print(executando7)
