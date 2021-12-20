# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

# abaixo será mostrado como modificar uma tupla, pois tuplas por padrão
# são imutáveis, para isso é necessário converte-las em listas, e após
# isso, converter elas novamente para tuplas.

# ==========> EXEMPLO 1

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3000
ti = tuple(t1)

print(t1)

# ==========> EXEMPLO 2

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (6, 7, 8, 9, 10)

soma = ()
soma = list(soma)

for v in range(0, 5):
    adicao = tupla1[v] + tupla2[v]
    soma.append(adicao)

soma = tuple(soma)
print(soma)
