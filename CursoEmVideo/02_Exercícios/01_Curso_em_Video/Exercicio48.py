soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('a soma de todos os {} valores é {}'.format(cont, soma))

# n = 10
# print(n % 2)
# se são pares o resultado acima é 0.
# se são impares é 1.
