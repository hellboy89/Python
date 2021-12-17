"""
# SÍMBOLOS DE SEPARAÇÃO
# () Tuplas
# [] Listas
# {} Dicionários
# LEMBRANDO QUE TUPLAS SÃO IMUTÁVEIS, NÃO É POSSÍVEL ALTERAR A SAÍDA, NEM ACRESCENTER UM ITEM.
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# Mostrar o tipo de saída
print(type(lanche))
print(lanche)
# Imprimindo saída por posição
print(lanche[1])
print(lanche[2])
# Lembrando que excluí o 2, só vai até o 1
print(lanche[0:2])
# Imprime da posição 1 até o fim.
print(lanche[1:])
# Irá pegar do último para o primeiro. Começando do Pudim
print(lanche[-1])
print(lanche[-4])
print(lanche[-3])
# Imprimindo a quantidade com o LEN.
print(len(lanche))
print()
# Imprimindo usando o FOR, que irá mostrar a saída separado por linha.
for c in lanche:
    print(c)
print()
# Imprimindo com o ENUMERATE é possível mostrar a posição, melhor entendimento.
for i, v in enumerate(lanche):
    print(i, v)
print()

============================================================================

# Possível também criar uma tupla sem os parênteses, PYTHON 3 reconhece automático.
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
# Imprindo o tipo de variável.
print(type(lanche))
# Na saída abaixo ele irá mostrar em parênteses, pois irá reconhecer a tupla de automaticamente.
print(lanche)
# Abaixo é para colocar a saída em ordem alfabética, com o SORTED.
# A Saída do comando SORTED é mostrado em [], para espeficiar que ele transformou em um LISTA.
print(sorted(lanche))
# Mostrando posições
for i, v in enumerate(lanche):
    print(i, v)
print()
# Filtrando posições
print(lanche[1])
print(lanche[-1])
# Lembrando que sempre exclui a última posição, só vai até o 2.
print(lanche[1:3])
# Deixando apenas o [:], ele vai deixar como está.
print(lanche[:])
# Aqui ele mostra do início até o elemento 2, como exclui o 2, só vai até o 1 na posição.
print(lanche[:2])
# Assim mostra tudo.
print(lanche[:4])
# Aqui ele irá começar a pegar da posição -2 (lembrando que começa na -1), e vai té final que é o -1.
print(lanche[-2:])
# Esses dois abaixo tem a mesma saída como exemplo
print(lanche[-3:])
print(lanche[1:])
print()
# No exemplo abaixo para tentar MUTAR uma TUPLA, irá dar erro, pois pela regra é IMUTÁVEL.
# lanche[1] = 'Refrigerante'
# print(lanche)
# Possível filtrar utilizando o FOR também.
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print()
# Contando itens na lista.
print(len(lanche))
print()
# Outra forma de filtrar com o FOR.
# Desse modo abaixo irá imprimir uma contagem.
for cont in range(0, len(lanche)):
    print(cont)
print()
# Desse irá imprimir só a saída do resultado.
# Onde em cada array irá imrimir uma posição da tupla diferente, mostrando a saída de todos na tupla.
for cont in range(0, len(lanche)):
    print(lanche[cont])
print()
# Essa saída abaixo seria exatamente igual a de cima, mas simplificada.
# Foi mostrada dessas duas formas, pois há necessidades que é mais fácil usar uma delas.
for comida in lanche:
    print(comida)
print()
# Talvez eu precise mostrar a posição do elemento.
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}.')
print()
# Também possível usar da segunda maneira, usando o enumerate.
# Onde POS é o índice, e lanche é a variável.
for pos, lanche in enumerate(lanche):
    print(f'Eu vou comer {lanche}, na posição {pos}.')
print()

============================================================================

# No Exemplo abaixo irá juntar o resultado das tuplas.
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
# Mostrar o tamanho das tuplas.
print(len(c))
# Aqui mostra o número de vezes que aparece o número 5. Método COUNT.
print(c.count(5))
# Aqui mostra o número de vezes que aparece o 4.
print(c.count(4))
# O número 9. Se não aparecer nada é 0.
print(c.count(9))
# Usando o INDEX, ele mostra a posição onde setá o valor.
print(c.index(8))
print()
print(c)
# Se caso o valor já existir. Como existe o número 2, em dois locais diferentes,
# ele irá mostrar o primeiro que está na posição 0 mesmo.
print(c.index(2))
# Para resolver isso é necessário resolver com o posicionamento. Para ele buscar a partir da posição 1.
# Buscando o 2 a partir da posição 1.
print(c.index(2, 1))
# Como no 5 que está na posição 1, mas se eu quiser ver o outro, marco a posição.
print(c.index(5))
# Pegar o segundo 5.
print(c.index(5, 2))

============================================================================

# Colocando dados de tipos diferentes.
pessoa = ('Gustavo', 39, 'M', 99.88)
# Possível também apagar toda a saída da variável.
del (pessoa)
# A saída abaixo irá gerar um erro, pois como eu apaguei toda a variável acima, não tem o que imprimir.
# Mas somente consigo fazer com o parâmetro acima, não é possível remover o item, como é IMUTÁVEL.
print(pessoa)

============================================================================

"""

