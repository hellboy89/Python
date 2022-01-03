# Comando abaixo limpa o terminal antes de executar o próximo código
import os
os.system('cls' if os.name == 'nt' else 'clear')


def testeLista():
    lista = ["01", "02", "03"]
    listaConvert = []
    # print(type(lista))
    for valores in lista:
        convert = int(lista[valores])
        listaConvert.append(convert)

    print(lista)
    print(listaConvert)

# testeLista()


def testeSoma():
    val1 = 10
    val2 = 20
    soma = val1 + val2
    print(f"a soma e {soma}")


def deletarDadosBanco():
    nome = input("qual nome para apagar do banco? ")
    comando = f"delete from cadastro where nome = '{nome}'"

    meucursor.execute(comando)

    open.commit()

    print(meucursor.rowcount, "dados removidos")


def inserirDados():

    while True:
        nome = input("qual nome: ")
        sobrenome = input("qual sobrenome: ")

        sql = "INSERT INTO cadastro (nome, sobrenome) VALUES (%s, %s)"
        valores = (nome, sobrenome)

        if nome and sobrenome:
            meucursor.execute(sql, valores)
            open.commit()
            print(meucursor.rowcount, "gravacao inserida")
            continue
        else:
            break


def verDados():
    meucursor.execute("select nome, sobrenome from cadastro")
    meuresultado = meucursor.fetchall()

    for x in meuresultado:
        print(x)


def abrirConexao(opcoes):
    import mysql.connector
    global open

    open = mysql.connector.connect(
        user='root',
        password='#Teste123',
        host="localhost",
        database="testewin01"
    )

    global meucursor
    meucursor = open.cursor()

    while True:

        if opcoes == "1":
            verDados()
            break
        elif opcoes == "2":
            inserirDados()
            break
        elif opcoes == "3":
            deletarDadosBanco()
            break
        else:
            break


def fazer():
    print("o que gostaria de fazer? ")
    print("[1] Visualizar dados da tabela cadastro")
    print("[2] inserir dados na tabela cadastro")
    print("[3] deletar dados")
    print("[s] SAIR")
    opcoes = input("informe: ")
    abrirConexao(opcoes)


fazer()
