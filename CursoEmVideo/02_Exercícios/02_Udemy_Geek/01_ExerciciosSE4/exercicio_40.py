dias = float(input('quantos dias o encanador irá ficar: '))

diaria = 30.00

imposto = (dias*30)*8/100

valdesconto = (dias*diaria)-imposto

print('o total de valor a pagar é R$ {}, com impostos será o total de R$ {}'.format(dias*30,valdesconto))