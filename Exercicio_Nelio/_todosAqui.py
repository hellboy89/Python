# Comando abaixo limpa o terminal antes de executar o próximo código
from math import dist, sqrt
print("\x1bc")


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
    for v in range(0, 3):
        valor = float(input(""))
        distancias.append(valor)

    return max(distancias)

# print(f"maior distância = {_04_dardo():.2f}")


def _04_temperatura():
    while True:
        escala = input("vc vai digitar a temperatura em qual escala (c/f)? ")

        if "c" in escala:
            temp = float(input("digite a temperatura em Celsius: "))
            convert = temp * (9/5) + 32
            print(f"temperatura equivalente em Fahrenheit: {convert:.2f}")
        elif "f" in escala:
            temp = float(input("digite a temperatura em Celsius: "))
            convert = (temp - 32) * (5 / 9)
            print(f"temperatura equivalente em Fahrenheit: {convert:.2f}")
        else:
            return f"valor incorreto, tente novamente!"
            break

# print(_04_temperatura())


def _04_lanchonete():
    codProd = int(input("Codigo do produto comprado: "))
    quantComp = int(input("Quantidade Comprada: "))

    if codProd == 1:
        preco = 5.00
    elif codProd == 2:
        preco = 3.50
    elif codProd == 3:
        preco = 4.80
    elif codProd == 4:
        preco = 8.90
    elif codProd == 5:
        preco = 7.32

    if codProd >= 1 and codProd <= 5:
        valPag = preco * quantComp
        print(f"Valor a pagar: {valPag:.2f}")
    else:
        print("codigo invalido, tente novamente!")

# _04_lanchonete()


def _04_multiplos():
    print("digite dois numeros inteiros multiplos: ")
    num1 = float(input())
    num2 = float(input())

    if num1 % num2 == 0 or num2 % num1 == 0:
        print("sao multiplos")
    else:
        print("NAO sao multiplos")

# _04_multiplos()


def testeIsInteger():
    y = 1.0
    saber = y.is_integer()
    print(saber)

# testeIsInteger()


def _04_aumento():
    while True:
        sal = float(input("digite o salario da pessoa: "))
        if sal <= 1000.00:
            novoSal = (sal * 0.20) + sal
            aumento = sal * 0.20
            porcentagem = "20%"
        elif sal <= 3000.00:
            novoSal = (sal * 0.15) + sal
            aumento = sal * 0.15
            porcentagem = "15%"
        elif sal <= 8000.00:
            novoSal = (sal * 0.10) + sal
            aumento = sal * 0.10
            porcentagem = "10%"
        elif sal > 8000.00:
            novoSal = (sal * 0.05) + sal
            aumento = sal * 0.05
            porcentagem = "5%"

        print(f"Novo Salario = R$ {novoSal:.2f}")
        print(f"Aumento = R$ {aumento:.2f}")
        print(f"Porcentagem = {porcentagem}")

        continuar = input("quer continuar (s/n): ")

        if "n" in continuar:
            break

# _04_aumento()


def _04_tempoDeJogo():
    horaIni = int(input("hora inicial: "))
    horaFin = int(input("hora final: "))

    if horaIni < horaFin:
        resp = horaFin - horaIni
    else:
        resp = 24 - (horaIni - horaFin)

    print(f"o jogo durou {resp} horas.")

# _04_tempoDeJogo()


def _04_coordenadas():
    valX = float(input("valor de X: "))
    valY = float(input("valor de Y: "))

    if valX > 0 and valY > 0:
        print("Q1")
    elif valX < 0 and valY > 0:
        print("Q2")
    elif valX > 0 and valY < 0:
        print("Q4")
    elif valX == 0 and valY == 0:
        print("origem")
    elif valX > 0 and valY == 0:
        print("Eixo X")

# _04_coordenadas()


def _05_crescente():
    print('digite dois numeros: ')
    num1 = int(input())
    num2 = int(input())

    while num1 != num2:
        if num1 > num2:
            print('decrescente')
        else:
            print('crescente')
        print('digite dois numeros: ')
        num1 = int(input())
        num2 = int(input())

# _05_crescente()


def _05_mediaIdades():
    print('digite as idades:')
    soma = 0
    contador = 0
    idade = 0

    while idade >= 0:
        idade = int(input())
        if idade > 0:
            soma += idade
            contador += 1

    if soma >= 1:
        print(f'Media = {(soma / contador):.2f}')
    else:
        print('nao e possivel calcular.')

# _05_mediaIdades()


def _05_senhaFixa():

    senha = int(input("digite a senha: "))

    if senha == 2002:
        print('acesso permitido')
    else:
        listaSenhasErradas = []
        listaSenhasErradas.append(senha)

    while senha != 2002:
        senha = int(input('senha invalida! tente novamente: '))
        if senha == 2002:
            print('acesso permitido')
        else:
            listaSenhasErradas.append(senha)

    print("abaixo senhas erradas")
    for mostra in listaSenhasErradas:
        print(mostra, end=', ')

# _05_senhaFixa()


def _05_quadrante():
    while True:
        print("Digite os valores das coordenadas X e Y: ")
        valX = int(input())
        valY = int(input())

        if valX > 0 and valY > 0:
            print('quadrante Q1')
        elif valX > 0 and valY < 0:
            print('quadrante Q4')
        elif valX < 0 and valY < 0:
            print('quadrante Q3')
        elif valX < 0 and valY > 0:
            print('quadrante Q2')
        elif valX == 0 or valY == 0:
            break


_05_quadrante()


def _05_validacaoDeNota():
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))

    media = (nota1 + nota2) / 2



_05_quadrante()
