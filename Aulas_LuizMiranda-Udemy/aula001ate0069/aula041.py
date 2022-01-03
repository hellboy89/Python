# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

frase = "Apredendo Programação Dia Após Dia"

# Gerando uma lista a partir de uma frase na variável.

lista_1 = frase.split(' ')

print(lista_1)

frase2 = "O Brasil é Penta."

lista_2 = frase2.split(' ')

# Função utilizada para numerar indices.

for indice, valor in enumerate(lista_2):
    print(indice, valor)


lista_3 = [
    [1,2],
    [3,4],
    [5,6]
]

for v in lista_3:
    print(v[0], v[1])

# usando várias variáveis ao mesmo tempo.

num1, num2, num3 = [1, 2, 3]

print(num1)
print(num2)
print(num3)

