# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

from math import dist, sqrt

def _03_idades():
    print("Dados da Primeira Pessoa")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    print("Dados da Segunda Pessoa")
    nome2 = input("Nome: ")
    idade2 = int(input("Idade: "))
    mediaIdade = (idade + idade2) / 2
    print(f"A idade média de Maria Silva e João Melo é de {mediaIdade}")

# _03_idades()

def _03_soma():
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))
    soma = x + y
    print(f"Soma = {soma}")

# _03_soma()

def _03_troco():
    precoUnit = float(input("Preco unitário do produto: "))
    quantComp = float(input("Quantidade comprada: "))
    dinRec = float(input("Dinheiro recebido: "))
    troco = dinRec - (precoUnit * quantComp)
    print(f"Troco = {troco:.2f}")

# _03_troco()

def _03_circulo():
    raio = float(input("Digite o valor do raio do circulo: "))
    area = (raio ** 2) * 3.14159
    print(f"Area = {area:.3f}")

# _03_circulo()

def _03_pagamento():
    while True:
        nome = input("Nome: ")
        if nome:
            valorHora = float(input("Valor por hora: "))
            horasTrab = int(input("Horas trabalhadas: "))
            calc = valorHora * horasTrab
            print(f"O pagamento para {nome} deve ser R$ {calc:.2f}")
            break
        else:
            print("nome não pode ser vazio, tente novamente!")
        
# _03_pagamento()

def _03_consumo():
    distPerc = int(input("Distância Percorrida: "))
    combGast = float(input("Combustível Gasto: "))
    calc = distPerc / combGast
    print(f"Consumo Medio = {calc:.3f}")

# _03_consumo()

def _03_medidas():
    medA = float(input("Digite a medida de A: "))
    medB = float(input("Digite a medida de B: "))
    medC = float(input("Digite a medida de C: "))
    if medA > 0 and medB > 0 and medC > 0:
        areaQuad = medA ** 2
        areaTriang = (medA * medB) / 2
        areaTrap = ((medB + medA) * medC) / 2
        print(f"Area do Quadrado = {areaQuad:.4f}")
        print(f"Area do Triangulo = {areaTriang:.4f}")
        print(f"Area do Trapezio = {areaTrap:.4f}")
    else:
        print("as medidas precisam ser maior do que 0.")
        

# _03_medidas()

def _03_duracao():
    duracao = int(input("digite o tempo em segundos: "))
    horas = duracao // 3600
    resto = duracao % 3600
    minutos = resto // 60
    duracao = resto % 60
    print(f"{horas}:{minutos}:{duracao}")

# _03_duracao()

def _04_notas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    notaFinal = nota1 + nota2
    if notaFinal > 60:
        print(f"nota final = {notaFinal:.1f}")
    else:
        print(f"nota final = {notaFinal:.1f}")
        print("reprovado")

# _04_notas()

def _04_baskara():
    coefA = float(input("coeficiente de A: "))
    coefB = float(input("coeficiente de B: "))
    coefC = float(input("coeficiente de C: "))
    delta = (coefB * coefB) - (4 * coefA * coefC)
    if delta < 0:
        print("esta equação não tem raizes reais")
    else:
        x1 = ((- coefB) + sqrt(delta)) / (2 * coefA)
        x2 = ((- coefB) - sqrt(delta)) / (2 * coefA)
        print(f"x1 = {x1:.4f}")
        print(f"x2 = {x2:.4f}")

# _04_baskara()

def _04_menorDeTres():
    val1 = int(input("Digite o primeiro valor: "))
    val2 = int(input("Digite o segundo valor: "))
    val3 = int(input("Digite o terceiro valor: "))
    
    menor = val1

    if val2 < menor:
        menor = val2
    elif val3 < menor:
        menor = val3
    else:
        menor = val1

    print(f"menor = {menor}")

# _04_menorDeTres()

def _04_operadora():
    quantMin = int(input("Digite a quantidade de minutos: "))

    if quantMin <= 100:
        print(f"valor a pagar: R$ 50,00.")
    else:
        calc = ((quantMin - 100) * 2) + 50
        print(f"valor a pagar: R$ {calc:.2f}.")

# _04_operadora()

def _04_trocoVerificado():
    precoUnit = float(input("preco unitário do produto: "))
    quantComp = float(input("quantidade comprada: "))
    dinRec = float(input("dinheiro recebido: "))

    total = (precoUnit * quantComp)

    if dinRec > total:
        calc = dinRec - total
        print(f"troco = R$ {calc:.2f}")
    else:
        calc = total - dinRec
        print(f"dinheiro insuficiente. faltam R$ {calc:.2f}")

# _04_trocoVerificado()

def _04_glicose():
    glicose = float(input("Digite a medida da glicose: "))

    if glicose <= 100:
        return "normal"
    elif glicose > 100 and glicose <= 140:
        return "elevado"
    elif glicose > 140:
        return "diabetes"
    else:
        print("valor incorreto, tente novamente!")

# print(f"classificação: {_04_glicose()}")

def _04_dardo():
    distancias = []
    for v in range(0,3):
        valor = float(input(""))
        distancias.append(valor)

    return max(distancias)

# print(f"maior distância = {_04_dardo():.2f}")








