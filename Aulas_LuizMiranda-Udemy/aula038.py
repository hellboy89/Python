# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

teste = ["Juan", 32, 1.98]

print(teste)
print(type(teste))

# imprimindo dados numa única lista
for lista in teste:
    print(lista, end=" ")

# se quiser adicionar valores na lista, basta fazer como abaixo.
teste.extend("Alves")

# adicionar o texto inteiro
teste.append("Alves")

# se quiser posso adicionar em qualquer posição do índice.
teste.insert(0, "Bonitão")

# aqui apaga o último elemento com o valor pop.
teste.pop()

# adicionando varios elementos na lista.
cont = 0
while cont <= 25:
    cont += 1
    teste.append(cont)

# excluindo linhas entre 0 e 5
del(teste[0:5])

# se quiser excluir só um elemento
del(teste[0])

# selecionando o maior valor
print("\npegando maior e menor valor")
teste2 = [1, 2, 3, 4, 5, 6]
print(max(teste2)) 
print(min(teste2))

# lembrando que isso não altera a variável, mas sim os valores após ela.
print(f"\n{teste}")

# se quiser posso criar uma lista automática com a função range, como abaixo
teste3 = list(range(1,15))
# pulando de 10 em 10.
teste4 = list(range(0,100,10))
print(teste3)
print(teste4)

# entrada de dados para a lista

teste5 = []

while True:
    entrada = input("qual o valor? ")

    if entrada.isnumeric():
        entrada = int(entrada)
        teste5.append(entrada)
        print(teste5)
    else:
        print("Digite somente numeros")


