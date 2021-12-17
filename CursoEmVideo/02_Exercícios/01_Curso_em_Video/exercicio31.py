kmviagem = int(input('digite a distância em km: '))

if kmviagem <= 200:
    print('o valor da passagem é R$ {:.2f}'.format(kmviagem * 0.50))
elif kmviagem > 200:
    print('o valor da passagem é R$ {:.2f}'.format(kmviagem * 0.45))
