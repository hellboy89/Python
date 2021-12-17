salbase = float(input('informe o seu salário base: '))

grat = salbase * 0.05

imposto = salbase * 0.07

total = salbase+grat-imposto

print('a gratificação é {}'.format(grat))

print('com desconto do imposto o total ficaria {}'.format(total))
