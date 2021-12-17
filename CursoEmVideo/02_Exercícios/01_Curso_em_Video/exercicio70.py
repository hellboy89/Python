# crie um programa que leia o "nome" e o "preço" de "vários produtos". O programa deverá perguntar se o "usuário"
# vai continuar. No final, mostre:
# a) qual é o "total gasto" na compra.
# b) quantos produtos custam "mais" de "R$ 1000".
# c) qual é o "nome" do produto mais "barato".

totalpreco = mais1000 = menorp = cont = 0
# variável vazia abaixo utilizada para coletar o nome do produto.
barato = ' '
while True:
    nome = str(input('informe o nome do produto: '))
    preco = float(input('informe o valor do produto: '))
    perg = str(input('deseja continuar? [S/N]: ')).strip()[0].lower()
    cont += 1
    totalpreco += preco
    if perg == 'n':
        break
    if preco > 1000:
        mais1000 += 1
    # Aqui mostra uma forma de realizar separação de um valor menor, muito interessante.
    if cont == 1:
        menorp = preco
        barato = nome
    else:
        if preco < menorp:
            menorp = preco
            barato = nome
    # ==========================================
print('o total da compra foi R$ {:.2f}.'.format(totalpreco))
print('o número de produtos que custam mais de R$ 1000,00 é {}.'.format(mais1000))
print('o nome do produto mais barato é {}, que custa R$ {}.'.format(barato, menorp))
