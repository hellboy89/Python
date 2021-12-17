velocidade = int(input('qual velocidade do cidadão? '))
print('=-' * 30)
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('vc foi multado em R$ {:.2f}!'.format(multa))
else:
    print('dirija com cuidado!')
print('=-' * 30)
