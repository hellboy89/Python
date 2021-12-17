amigo1 = float(input('informe o valor investido: '))
amigo2 = float(input('informe o valor investido: '))
amigo3 = float(input('informe o valor investido: '))

total = 1_000_000.00

partamig1 = total * amigo1 / 100
partamig2 = total * amigo2 / 100
partamig3 = total * amigo3 / 100

print('a parte do amigo 1 é: {:.2f}'.format(partamig1))
print('a parte do amigo 2 é: {:.2f}'.format(partamig2))
print('a parte do amigo 3 é: {:.2f}'.format(partamig3))
