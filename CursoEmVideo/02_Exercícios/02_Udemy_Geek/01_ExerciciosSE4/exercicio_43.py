valortotal = float(input('qual valor total: '))

totalpagar = valortotal * 0.10

valordescontototal = valortotal - totalpagar

parcela = (valortotal + totalpagar) / 3

comissaovista = valortotal * 0.05

comissaoparc = valordescontototal * 0.05

print('o total com desconto de 10% é {}'.format(totalpagar))
print('o valor de cada parcela, no parcelamento de 3x sem juros é {}'.format(parcela))
print('a comissã odo vendedor para pagamento a vista é {}'.format(comissaovista))
print('a comissão do vendedor para venda parcelada é {}'.format(comissaoparc))
