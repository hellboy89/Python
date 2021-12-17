# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

kmpercorrido = float(input('informe a quantidade de km percorridos: '))
diasaluguel = float(input('informe a quantidade de dias de aluguel: '))

valorkm = kmpercorrido*0.15
valordias = diasaluguel*60.00

print('o valor a pagar por KM será {:.2f}'.format(valorkm))

print('o valor a pagar por dia será {:.2f}'.format(valordias))

print('o valor total é R$ {:.2f}'.format(valorkm+valordias))