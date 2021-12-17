"""

# Pré-requisito para essa aula é conhecer os recursos do FOR.
# São utilizados para gerar uma sequência numérica, não de form aleatória, mas de maneira específicada.

# FORMAS GERAIS
# range(valor_de_parada)
# OBS.: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Como abaixo não especifiquei um valor inicial, irá começar sempre de 0, indo até o 11.
# Nunca irá pegar o valor final que é o 11, irá até o 10.
# Exemplo 1
for num in range(11):
    print(num, end=' ')

============================================================================

# Exemplo 2
# Range (valor_de_inicio, valor_de_parada)
# Padrão acima é muito utilizado pelo LOOP FOR. Especificando o valor de início.
for num in range(4, 11):
    print(num, end=' ')

============================================================================

# Exemplo 3
# range(valor_de_inicio, valor_de_parada, passo)
# irá pular de 2 em 2.
# Não esquecer que nunca pega o último número do valor_de_parada, sempre termina em um anterior.
for num in range(5, 50, 5):
    print(num, end=' ')

============================================================================

# Exemplo 4 (inversa)
# range(valor_de_inicio, valor_de_parada, passo)
# Invesa pois irá contar de trás para frente.
for num in range(10, 0, -1):
    print(num, end=' ')

# Se eu definir uma variável como abaixo, com o valor "range(inicio,fim)" ela irá gerar um valor do tipo "range", como possível ver no type abaixo.
rang = range(0, 10)
print(type(rang))

# Mas se precisar gerar uma lista com esses valores, basta fazer como abaixo.
rang2 = range(0, 30)
lista = list(rang2)
print(lista)

============================================================================
"""

