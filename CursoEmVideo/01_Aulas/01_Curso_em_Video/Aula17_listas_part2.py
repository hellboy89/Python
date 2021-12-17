"""

# Relembrar o exemplo de lista abaixo.
# E a saída dos parâmetros abaixo irá gerar uma lista SIMPLES.
# Nessa aula será falado de listas COMPOSTAS, que são basicamente listas dentro de listas.
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)
print()
# Abaixo iremos adicionar uma outra lista, dentro da lista acima.
pessoas = list()
# Lembrando de usar o parâmetro [:] para realizar uma cópia da lista acima.
pessoas.append(dados[:])
# O print abaixo irá aparecer uma lista dentro de outra lista, com o separador [[]].
print(pessoas)
print()

============================================================================

# No exemplo abaixo, temos 3 listas, dentro de uma lista principal.
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)
# Filtrando a saída. Pegando lista 0 e valor da posição 1.
print(pessoas[0][1])
# Pegando lista 2, e valor da posição 1.
print(pessoas[2][1])
# Pegando lista 1, e valor da posição 0.
print(pessoas[1][0])
# Se quiser motrar a parte inteira, so digitar a primeira parte.
print(pessoas[2])

============================================================================

# Uma forma de criar uma lista dentro de listas.
# Um pouco essa parte abaixo. Vou por partes.
# Adicionado uma nova lista 'Teste'.
teste = list()
# Adicionado esses 2 valores na lista.
teste.append('Gustavo')
teste.append(40)
# Criado uma segunda lista chamada "galera", que fará pasta da lista principal teste.
galera = list()
# Para vincular ela inteira utilizado o parâmetro abaixo [:].
galera.append(teste[:])
# Adicionado os 2 valores na lista.
teste[0] = 'Maria'
teste[1] = 22
# E novamente adionado uma cópia dela para a lista galera.
galera.append(teste[:])
print(galera)

============================================================================

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# Mostrando só a posição 0.
print(galera[0])
# Mostrando só a última posição.
print(galera[-1])
# Mostrando somente sa idades.
for i, v in enumerate(galera):
    print(v[:3][1])
print()
# Pegando a posição da lista 3 e 2.
print(galera[3][1])
print()
# Possível fazer outra forma com o FOR. Pegando só a idade.
for v in galera:
    print(v[1])
print()
# Possível fazer pegando só o nome.
for v in galera:
    print(v[0])
print()
# Também de forma melhor formatada.
for v in galera:
    print(f'{v[0]} tem {v[1]} anos.')
print()

============================================================================

# Adicionando valores na lista utilizando o FOR.
galera = list()
dado = list()
# Variáveis usadas para contagem para pegar os maiores e menores de idade.
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    # Lembrando de usar o [:] para fazer cópia de dados.
    galera.append(dado[:])
    # Importante utilizar o CLEAR, para ele limpar os dados após inserir uma novo valor, para não duplicar.
    dado.clear()
print(galera)
print()
# Filtrando pessoas que sejam maior que 21 anos.
for p in galera:
    if p[1] >= 21:
        print(f'A {p[0]} é maior de dade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
# Saída com a quantidade informada no contador mais acima.
print(f'Tem {totmai} maiores de idade e {totmen} menores de idade.')

============================================================================

"""

