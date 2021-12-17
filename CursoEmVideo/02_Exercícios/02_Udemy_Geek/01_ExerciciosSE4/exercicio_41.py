valor = float(input('Informe o valor de hora de trabalho.'))

horas = int(input('Informe as horas trabalhadas.'))

acumulado = valor * horas

porcentagem = acumulado * 0.10

salario = acumulado + porcentagem

print('Salário:', salario)
