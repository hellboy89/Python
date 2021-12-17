# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input('informe o valor do produto: '))
valor = (prod*5)/100

print('o valor com 5% de desconto é {:.2f}'.format(prod-valor))
