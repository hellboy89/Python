"""
# Exemplo de tuplas.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[0])
# Filtrando em ordem alfabética.
print(sorted(lanche[1:3]))
# Se eu tentar usar o parâmetro abaixo irá gerar erro. Pois tuplas são IMUTÁVEIS.
# lanche[3] = 'Picole'
# PARA ISSO EXISTEM AS LISTAS, POIS POR ELAS É POSSÍVEL MUDAR OS ELEMENTOS.
# Identificando.
# Tuplas ()
# Listas []
# Dicionários {}

============================================================================

# Possível diferenciar pelos [] que são listas, agora sim são MUTÁVEIS.
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
# Abaixo parâmetro para mudar o valor na lista.
lanche[3] = 'Picole'
lanche[1] = 'Coca-Cola'
print(lanche)
# Filtrando
print(lanche[1])
print(lanche[3])
# Mostrando saída.
print(f'Quer comer {lanche[2]} com {lanche[1]}. Delícia!')
# Adicionando elemento, utilizando o APPEND. Que sempre irá para o final da lista com o APPEND.
lanche.append('Cookie')
print(lanche)
# Para adicionar o item numa posição específica é necessário usar o método INSERT().
# Onde 'cachorro-quente' irá ficar na posição 0.
lanche.insert(0, 'Cachorro-Quente')
print(lanche)
# Possível acrescentar em qualquer posição necessária.
lanche.insert(2, 'Empadão')
print(lanche)
# Para elimitar um elemento da lista é possível com o comando DEL. Tirando o Cookie, que é o último.
del lanche[-1]
print(lanche)
# Ou também utilizando o comando POP. Tirando a primeira posição.
lanche.pop(1)
print(lanche)
# Também possível excluir pelo nome do item na lista, utilizando o REMOVE. Como pizza.
# Após os itens elimitados eles irão se reposicionar para não perder o índice.
lanche.remove('Pizza')
print(lanche)
# Também possível utilizar o comando POP(), mas sem apontar o índice. Assim irá remover o último.
lanche.pop()
print(lanche)
print()
# Também possível remover o item somente se ele estiver na lista. Para isso iremos filtar com o IF.
# Lembrando de lembrar do operador IN, pois sempre muito útil para estruturas compostas.
if 'Empadão' in lanche:
    lanche.remove('Empadão')

============================================================================

# Adicionando valores automáticos na lista usando range.
valores = list(range(4, 11))
print(valores)
# Mostrando os índices.
for i, v in enumerate(valores):
    print(f'Posição {i} está o valor {v}')

============================================================================

# Organizando com o método SORT().
valores = [8, 2, 5, 4, 9, 3, 0]
# Possível utilizar só o parâmetro como abaixo.
valores.sort()
print(valores)
print()
# Ou já indicar o SORT() diratamente na impressão. Que seria a mesma coisa, mas com apenas uma linha.
print(sorted(valores))
# Possível também colocar na ordem inverta com o reverse=True. No caso desse não é como o de cima,
# teria que utilizar separado mesmo.
valores.sort(reverse=True)
print(valores)
# Contando elementos com LEN.
print(len(valores))

============================================================================

# Abaixo um exemplo de Tupla, irá dar erro, pois Tuplas são IMUTÁVEIS.
# num = (2, 5, 9, 1)
# num[2] = 3
# print(num)
# Mas fazendo o mesmo exemplo acima com Listas. Repara que tem que trocar o () por [].
# Já é possível realizar alteração, pois uma lista é MUTÁVEL.
num = [2, 5, 9, 1]
num[2] = 3
# Para adicionar o valor 7 no fim da lista
num.append(7)
# Usando o SORT() para organizar alfabeticamente.
num.sort()
# Comando abaixo irá adicionar o 0 na posição 2.
num.insert(2, 0)
# Comando abaixo irá adicionar o número 2 na posição 2.
num.insert(2, 2)
# Comand oadicionar o 5 na posição 2.
num.insert(2, 5)
# Utilizando o comando abaixo irá remover apenas o último valor.
num.pop()
# Mas posso também definir a posição com o POP().
num.pop(2)
print(num)
# Para mover o elemento usando o método REMOVE(). Irá remover o número 2 não importa a posição.
num.remove(2)
# Mas se remover um número que não está na lista como abaixo, irá dar um erro na saída.
# num.remove(4)
# Para resolver isso acima, necessário utilizar o IF com o operador IN.
# Lembrar da utilidade do IN com para lista composta. MUITA IMPORTANTE!
if 5 in num:
    num.remove(5)
    print('valor removido!')
else:
    print('inexistente!')

print(num)
print()
# Pegando o número de elementos.
print(f'Essa lista tem {len(num)} elementos.')

============================================================================

# Adicionando valores na lista.
# O valor list() seria o mesmo que [].
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
print()
# Podendo mostrar a saída também com o FOR.
for v in valores:
    print(v, end='...')
print()
print()
# Podendo fazer com o Enumerate também.
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('FINAL DA LISTA! ')

============================================================================

# Abaixo exemplo com entrada de dados do usuário.
valores = list()
for cont in range(0, 5):
    valores.append(int(input('digite um valor: ')))
# Aqui um for para organização da sáida dos dados acima.
for i, v in enumerate(valores):
    print(f'foi digitado {v} na posição {i}.')

============================================================================

# Abaixo um exemplo de cópia de lista. No exemplo abaixo é uma lista comum, onde não tá sendo
# utilizado a função de cópia [:]. Por isso a saída de A e B seram iguais
a = [2, 3, 4, 7]
b = a
# O parâmetro abaixo ira mudar a posição 2 (que é 4) para o valor 8.
b[2] = 8
# Lembrando que após feito a alteração acima, ele irá alterar nas 2 LISTAS.
print(f'A lista A é: {a}')
print(f'A lista B é: {b}')

a = [2, 3, 4, 7]
# Para resolvermos a falha acima, usaremos o parâmetro [:] que fará uma cópia completa da lista A.
b = a[:]
b[2] = 8
print(f'A lista A é: {a}')
print(f'A lista B é: {b}')

============================================================================

"""

