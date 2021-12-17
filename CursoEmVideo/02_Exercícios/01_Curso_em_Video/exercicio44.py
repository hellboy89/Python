preco = float(input('informe o valor do produto: '))
cond = int(input('''Informe a condição de pagamento: 
1. A vista dinheiro/cheque: 10% de desconto.
2. A vista no cartão: 5% de desconto.
3. Em até 2x no cartão: preço normal. 
4. 3x ou mais no cartão: 20% de juros.\n'''))

if cond == 1:
    desc = preco - (preco * 0.10)
    print('o valor total ficaria: R$ {:.2f}'.format(desc))
elif cond == 2:
    desc = preco - (preco * 0.05)
    print('o valor total ficaria: R$ {:.2f}'.format(desc))
elif cond == 3:
    print('o valor ficaria R$ {:.2f}.'.format(preco))
elif cond == 4:
    juros = preco + (preco * 0.20)
    numpar = int(input('informe a quantidade de parcelas: '))
    parcela = juros / numpar
    print('sua compra será parcelada em {}x de R$ {:.2f}.'.format(numpar, parcela))
else:
    print('ESSE VALOR NÃO EXISTE, TENTE NOVAMENTE!')
